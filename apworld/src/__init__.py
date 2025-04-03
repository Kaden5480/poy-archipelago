from typing import Callable, \
                   ClassVar

from worlds.AutoWorld import World
from BaseClasses import CollectionState, \
                        Entrance, \
                        Item, \
                        ItemClassification, \
                        Location, \
                        Region

from .data.data_store import DataStore
from .data.items import ItemData
from .data.locations import LocationData
from .data.regions import RegionData

from .names.items import *
from .names.locations import *
from .names.regions import *

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

        :param region: The region to connect to, if any
        :param rule: The access rule for this connection, if any
        """

        if region is None:
            return

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

    poy_created_regions: dict[str, PeaksRegion] = {}
    poy_created_items: dict[str, list[ItemData]] = {}

    def __init__(self, *args, **kwargs) -> None:
        self.poy_rules = Rules(self.poy_data, self)

        super().__init__(*args, **kwargs)

    # Extensions
    def poy_ignore_region(
        self,
        name: RegionName
    ) -> bool:
        """
        Whether this region should be ignored as
        it's disabled by the user.

        :param name: The name of the region
        :returns: True if it should be ignored, False otherwise
        """

        # Check cabins
        if name == CabinRegionName.GALES is True:
            return not self.options.enable_fundamental \
                    and not self.options.enable_intermediate \
                    and not self.options.enable_advanced \

        if name == CabinRegionName.NORTHERN:
            return not self.options.enable_expert

        if name == CabinRegionName.ALPS:
            return not self.options.enable_essentials \
                    and not self.options.enable_greats \
                    and not self.options.enable_arctic

        # Check peak categories
        if type(name) == FundamentalsRegionName:
            return not self.options.enable_fundamentals

        if type(name) == IntermediateRegionName:
            return not self.options.enable_intermediate

        if type(name) == AdvancedRegionName:
            return not self.options.enable_advanced

        if type(name) == ExpertRegionName:
            return not self.options.enable_expert

        if type(name) == EssentialsRegionName:
            return not self.options.enable_essentials

        if type(name) == GreatsRegionName:
            return not self.options.enable_greats

        if type(name) == ArcticRegionName:
            return not self.options.enable_arctic

        return False

    def poy_create_region(self, name: RegionName) -> None:
        """
        Creates a region given its name.
        This also creates all locations for this region.

        :param name: The name of the region to create
        """

        # If this region is ignored, don't create it
        if self.poy_ignore_region(name) is True:
            return

        data: RegionData = self.poy_data.regions.get_data(name)
        region: PeaksRegion = PeaksRegion(
            data.name, self.player,
            self.multiworld
        )

        print(f"Created region: {name}")

        self.poy_created_regions[name.value] = region
        self.multiworld.regions.append(region)

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

    def poy_get_region_str(
        self,
        name: str
    ) -> PeaksRegion | None:
        """
        Gets a created region by its name.

        :param name: The name of the region to find
        :returns: The region if found, None otherwise
        """

        return self.poy_created_regions.get(name, None)

    def poy_get_region(
        self,
        name: RegionName
    ) -> PeaksRegion | None:
        """
        Gets a created region by its name.

        :param name: The name of the region to find
        :returns: The region if found, None otherwise
        """

        return self.poy_get_region_str(name.value)

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

        if category_region is None:
            return

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
        if cabin_gales is not None:
            cabin_gales.poy_connect(
                self.poy_get_region(FundamentalsRegionName.CATEGORY),
                self.poy_rules.has_item(
                    BaseItemName.BOOK_GALES_FUNDAMENTALS
                )
            )
            cabin_gales.poy_connect(
                self.poy_get_region(IntermediateRegionName.CATEGORY),
                self.poy_rules.has_item(
                    BaseItemName.BOOK_GALES_INTERMEDIATE
                )
            )
            cabin_gales.poy_connect(
                self.poy_get_region(AdvancedRegionName.CATEGORY),
                self.poy_rules.has_item(
                    BaseItemName.BOOK_GALES_ADVANCED
                )
            )

        # Northern range categories

        # Due to an access rule set below with the northern
        # range ticket, this implicitly requires access to
        # the northern cabin before being reachable
        if cabin_northern is not None:
            cabin_northern.poy_connect(
                self.poy_get_region(ExpertRegionName.CATEGORY),
                self.poy_rules.has_item(
                    BaseItemName.BOOK_NORTHERN_EXPERT
                )
            )

        # Alps DLC categories
        if cabin_alps is not None:
            cabin_alps.poy_connect(
                self.poy_get_region(EssentialsRegionName.CATEGORY),
                self.poy_rules.has_item(
                    DlcItemName.BOOK_ALPS_ESSENTIALS
                )
            )
            cabin_alps.poy_connect(
                self.poy_get_region(GreatsRegionName.CATEGORY),
                self.poy_rules.has_item(
                    DlcItemName.BOOK_ALPS_GREATS
                )
            )
            cabin_alps.poy_connect(
                self.poy_get_region(ArcticRegionName.CATEGORY),
                self.poy_rules.has_item(
                    DlcItemName.BOOK_ALPS_ARCTIC
                )
            )

        ### Connections between cabins

        # The gales cabin connects to the northern one
        # through the ticket
        # Also always has access to the DLC
        if cabin_gales is not None:
            cabin_gales.poy_connect(
                cabin_northern,
                self.poy_rules.has_item(
                    BaseItemName.TICKET_NORTHERN_RANGE
                )
            )
            cabin_gales.poy_connect(cabin_alps)

        # Northern cabin has access to Gales and DLC
        if cabin_northern is not None:
            cabin_northern.poy_connect(cabin_gales)
            cabin_northern.poy_connect(cabin_alps)

        # Alps cabin can always access Gales cabin
        if cabin_alps is not None:
            cabin_alps.poy_connect(cabin_gales)

    # Overrides
    def generate_early(self) -> None:
        """
        Early generation of the world.

        Checks the provided options and pushes
        precollected items where necessary
        """

        # Check at least one category is enabled
        if any([
            self.options.enable_fundamentals,
            self.options.enable_intermediate,
            self.options.enable_advanced,
            self.options.enable_expert,
            self.options.enable_essentials,
            self.options.enable_greats,
            self.options.enable_arctic
        ]) is False:
            raise Exception("At least one category of peaks must be enabled")

        # TODO: Decide the starting cabin early
        # TODO: Give access to a book for whichever categories
        # are enabled

        # Access to the fundamentals and essentials book is a given
        self.multiworld.push_precollected(
            self.poy_create_item(BaseItemName.BOOK_GALES_FUNDAMENTALS.value)
        )
        self.multiworld.push_precollected(
            self.poy_create_item(DlcItemName.BOOK_ALPS_ESSENTIALS.value)
        )

    def create_regions(self) -> None:
        """
        Creates all regions and the connections between them.
        """

        # Create the menu region
        menu_region = PeaksRegion(
            "Menu", self.player,
            self.multiworld
        )
        self.poy_created_regions["Menu"] = menu_region
        self.multiworld.regions.append(menu_region)

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

        # Connect the menu to any accessible cabin
        connected = False
        for cabin in CabinRegionName:
            if self.poy_ignore_region(cabin) is True:
                break

            menu_region.poy_connect(
                self.poy_get_region(cabin)
            )
            connected = True

        # If the generation made it this far,
        # one of the categories must be enabled
        # so a cabin should be reachable
        assert connected is True

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

    def poy_create_item(self, name: str) -> PeaksItem:
        """
        Creates an item and adds it to the item pool,
        along with tracking it in poy_created_items.

        :param name: The name of the item to make
        :returns: The created item
        """

        item = self.create_item(name)

        if name not in self.poy_created_items:
            self.poy_created_items[name] = []

        self.poy_created_items[name].append(item)

        return item

    def create_items(self) -> None:
        """
        Creates all items, adding them to the world's item pool.
        """

        local_pool: list[PeaksItem] = []

        # Iterate over all locations creating
        # their default items, unless they already
        # have been pushed to the multiworld
        data: LocationData
        for data in self.poy_data.locations:
            # Check this region is enabled
            region = self.poy_get_region_str(data.region)
            if region is None:
                continue

            item_name: str = data.item_name

            item_count: int = len(self.poy_created_items.get(item_name, []))
            max_item_count: int = self.poy_data.locations \
                    .get_max_item_count(item_name)

            location: PeaksLocation = PeaksLocation(
                self.player,
                data.name,
                data.id,
                region
            )
            location.progress_type = data.progress_type

            item: PeaksItem = self.create_item(item_name)

            # Lock stamps and time attack
            if not self.options.randomise_stamps \
                    and data.name.endswith(LocationSuffix.STAMP) is True:
                location.place_locked_item(item)

            elif data.name.endswith(LocationSuffix.TIME_ATTACK) is True:
                location.place_locked_item(item)

            # Or just add it to the pool if randomised
            elif item_count < max_item_count:
                if self.options.randomise_items:
                    local_pool.append(item)
                else:
                    location.place_locked_item(item)

            region.locations.append(location)

        # Add all items to the item pool
        self.multiworld.itempool += local_pool

    def set_rules(self) -> None:
        """
        Sets access rules on entrances, locations,
        and items to try to mitigate soft locks.
        """

        self.multiworld.completion_condition[self.player] \
                = self.poy_rules.has_item(BaseItemName.SHOE)

    def connect_entrances(self) -> None:
        """
        Performs entrance randomisation.
        """

        if not self.options.randomise_levels:
            return
