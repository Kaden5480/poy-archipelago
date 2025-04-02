from typing import Callable, \
                   ClassVar

from worlds.AutoWorld import World
from BaseClasses import CollectionState, \
                        Entrance, \
                        Item, \
                        Location, \
                        Region

from .data.data_store import DataStore
from .data.items import ItemData
from .data.locations import LocationData
from .data.regions import RegionData

from .names.regions import *
from .names.items import *

from .rules import Rules
from .options import PeaksOptions

GAME: str = "Peaks of Yore"

class PeaksItem(Item):
    game: str = GAME


class PeaksLocation(Location):
    game: str = GAME


class PeaksRegion(Region):
    game: str = GAME

    __poy_connections: dict[str, Entrance] = {}

    def poy_connect(
        self,
        region: "PeaksRegion",
        rule: Callable[[CollectionState], bool] | None = None
    ) -> None:
        """
        Connects this region to another region.

        :param region: The region to connect to
        :param rule: The access rule for this connection, if any
        """

        self.__poy_connections[region.name] = self.connect(
            region,
            f"{self.name} -> {region.name}",
            rule
        )

    def poy_get_connection(
        self,
        region: RegionName
    ) -> Entrance | None:
        """
        Gets the entrance for a connection from this region
        to another given region.

        :param region: The name of the region this connection is for
        :returns: The connection if found, None otherwise
        """

        return self.__poy_connections.get(region.value, None)


class PeaksWorld(World):
    """
    Travel around The Great Gales to climb challenging peaks in this
    physics-based climbing adventure set in 1887. Meet like-minded
    mountaineers, unlock helpful climbing gear, and become a pioneer
    of mountaineering.
    """

    game: str = GAME

    options_dataclass = PeaksOptions
    options: PeaksOptions

    poy_data: ClassVar[DataStore] = DataStore()

    # Required by AP
    item_name_to_id: ClassVar[dict[str, int]] = {item.name: item.id for item in poy_data.items}
    location_name_to_id: ClassVar[dict[str, int]] = {location.name: location.id for location in poy_data.locations}

    poy_rules: Rules

    poy_created_regions: dict[RegionName, PeaksRegion] = {}

    def __init__(self, *args, **kwargs) -> None:
        self.poy_rules = Rules(self.poy_data, self)

        super().__init__(*args, **kwargs)

    # Extensions
    def poy_create_region(self, name: RegionName) -> None:
        """
        Creates a region given its name.

        :param name: The name of the region to create
        """

        data: RegionData = self.poy_data.regions.get_data(name)
        self.poy_created_regions[name] = PeaksRegion(
            data.name, self.player,
            self.multiworld
        )

    def poy_create_regions(
        self,
        category: type[RegionName]
    ) -> None:
        """
        Creates all regions in a given category.

        :param category: The category to create regions for
        """

        for region in category:
            self.poy_create_region(region)

    def poy_get_region(
        self,
        name: RegionName
    ) -> PeaksRegion:
        """
        Gets a created region by its name.

        :param name: The name of the region to find
        :returns: The region if found, None otherwise
        """

        return self.poy_created_regions.get(name, None)

    def poy_connect_category(
        self,
        category: type[RegionName],
    ) -> None:
        """
        Creates connections from a category to its
        related peaks.

        :param category: The category to create connections for
        """

        # Get the name of the category
        category_name = getattr(category, "CATEGORY")

        # Get the category region itself
        category_region = self.poy_get_region(category_name)

        for peak in category:
            # Don't link the category to itself
            if peak == category_name:
                continue

            region = self.poy_get_region(peak)

            # Connect the category region to all peaks under it
            category_region.poy_connect(region)

    def poy_connect_cabins(self) -> None:
        """
        Creates connection rules for the cabins.

        This also applies basic access rules
        such as requiring books to reach a category region,
        and requiring the northern range ticket for the northern
        cabin.
        """

        cabin_gales = self.poy_get_region(CabinRegionName.GALES)
        cabin_northern = self.poy_get_region(CabinRegionName.NORTHERN)
        cabin_alps = self.poy_get_region(CabinRegionName.ALPS)

        ### Connections from cabins to their categories

        # Great Gales categories
        cabin_gales.poy_connect(
            self.poy_get_region(FundamentalsRegionName.CATEGORY),
            lambda state: self.poy_rules.has_item(
                state, BaseItemName.BOOK_GALES_FUNDAMENTALS
            )
        )
        cabin_gales.poy_connect(
            self.poy_get_region(IntermediateRegionName.CATEGORY),
            lambda state: self.poy_rules.has_item(
                state, BaseItemName.BOOK_GALES_INTERMEDIATE
            )
        )
        cabin_gales.poy_connect(
            self.poy_get_region(AdvancedRegionName.CATEGORY),
            lambda state: self.poy_rules.has_item(
                state, BaseItemName.BOOK_GALES_ADVANCED
            )
        )

        # Northern range categories

        # Due to an access rule set below with the northern
        # range ticket, this implicitly requires access to
        # the northern cabin before being reachable
        cabin_northern.poy_connect(
            self.poy_get_region(ExpertRegionName.CATEGORY),
            lambda state: self.poy_rules.has_item(
                state, BaseItemName.BOOK_NORTHERN_EXPERT
            )
        )

        # Alps DLC categories
        cabin_alps.poy_connect(
            self.poy_get_region(EssentialsRegionName.CATEGORY),
            lambda state: state.poy_rules.has_item(
                state, DlcItemName.BOOK_ALPS_ESSENTIALS
            )
        )
        cabin_alps.poy_connect(
            self.poy_get_region(GreatsRegionName.CATEGORY),
            lambda state: state.poy_rules.has_item(
                state, DlcItemName.BOOK_ALPS_GREATS
            )
        )
        cabin_alps.poy_connect(
            self.poy_get_region(ArcticRegionName.CATEGORY),
            lambda state: state.poy_rules.has_item(
                state, DlcItemName.BOOK_ALPS_ARCTIC
            )
        )

        ### Connections between cabins

        # The gales cabin connects to the northern one
        # through the ticket
        cabin_gales.poy_connect(
            cabin_northern,
            lambda state: self.poy_rules.has_item(
                state, BaseItemName.TICKET_NORTHERN_RANGE
            )
        )
        # And the northern one can connect back always
        cabin_northern.poy_connect(cabin_gales)

        # The northern cabin has one-way access to the alps
        cabin_northern.poy_connect(cabin_alps)

        # The gales cabin always has access to the DLC
        # and vice versa
        cabin_gales.poy_connect(cabin_alps)
        cabin_alps.poy_connect(cabin_gales)

    def poy_create_location(self, name: str) -> None:
        """
        Creates a location given its name.

        :param name: The name of the location to create
        :returns: The created location
        """

        location: LocationData = self.poy_data.locations.get_data_str(name)
        return PeaksLocation(
            self.player, location.name,
            location.id, location.region
        )

    # Overrides
    def generate_early(self) -> None:
        """
        Early generation of the world.

        Checks the provided options and pushes
        precollected items where necessary
        """

        # Access to the fundamentals and essentials book is a given
        self.multiworld.push_precollected(
            self.create_item(BaseItemName.BOOK_GALES_FUNDAMENTALS.value)
        )
        self.multiworld.push_precollected(
            self.create_item(DlcItemName.BOOK_ALPS_ESSENTIALS.value)
        )

    def create_regions(self) -> None:
        """
        Creates all regions and the connections between them.
        """

        peak_categories = (
            FundamentalsRegionName, IntermediateRegionName,
            AdvancedRegionName, ExpertRegionName,
            EssentialsRegionName, GreatsRegionName,
            ArcticRegionName
        )

        # Create cabin regions separately
        self.poy_create_regions(CabinRegionName)

        # Build regions for each category of peaks,
        # along with the connections from the category
        # to its related peaks
        #
        # e.g.
        # "Fundamentals" category connects to:
        #  - Greenhorn's Top
        #  - Paltry Peak
        #  ...
        for category in peak_categories:
            self.poy_create_regions(category)
            self.poy_connect_category(category)

        # Connect cabins to their categories,
        # and to each other where applicable
        #
        # This also sets any applicable access rules,
        # such as requiring books/tickets for accessing
        # categories/cabins
        self.poy_connect_cabins()

        # Create the menu region
        menu_region = PeaksRegion(
            "Menu", self.player,
            self.multiworld
        )
        self.poy_created_regions["Menu"] = menu_region

        # Connect the menu to the Gales Cabin
        menu_region.poy_connect(self.poy_get_region(CabinRegionName.GALES))

    def create_item(self, name: str) -> PeaksItem:
        """
        Creates an item on demand given its name.

        :param name: The name of the item to create
        :returns: The created item
        """

        item: ItemData = self.poy_data.items.get_data_str(name)
        return PeaksItem(
            item.name, item.classification,
            item.id, self.player
        )

    def create_items(self) -> None:
        """
        Creates all items, adding them to the world's item pool.
        """

        for data in self.poy_data.items:
            item = self.create_item(data.name)

    def set_rules(self) -> None:
        """
        Sets access rules on entrances, locations,
        and items to try to mitigate soft locks.
        """

    def connect_entrances(self) -> None:
        """
        Performs entrance randomisation.
        """
