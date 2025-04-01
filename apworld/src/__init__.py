from worlds.AutoWorld import World
from worlds.generic.Rules import add_rule

from BaseClasses import Entrance, \
                        Item, \
                        Location, \
                        Region

from .data.id_handler import IDHandler
from .data.regions import CabinName, \
                          PeakName

from .options import PeaksOptions

GAME: str = "Peaks of Yore"


class PeaksItem(Item):
    game: str = GAME


class PeaksLocation(Location):
    game: str = GAME
    poy_data: PoYLocationData

    def __init__(self, data: PoYLocationData, *args, **kwargs) -> None:
        """
        Initializes a PeaksLocation.

        :param data: The data for this location
        :param args: Arguments to pass to Location
        :param kwargs: Keyword arguments to pass to Location
        """

        self.poy_data = data
        super().__init__(*args, **kwargs)

    def poy_create_item(self, world: "PeaksWorld") -> None:
        """
        Creates the item which is locked behind this location.
        """

        item: PeaksItem = world.create_item(self.poy_data.item_name)
        self.place_locked_item(item)


class PeaksRegion(Region):
    game: str = GAME
    poy_data: PoYRegionData
    poy_connections: dict[str, Entrance]

    # Example for Northern Cabin
    #connections = [
    #    PeakName.NORTHERN_GREAT_BULWARK,
    #    PeakName.NORTHERN_SOLEMN_TEMPEST,
    #]
    #rules_connections = {
    #    PeakName.NORTHERN_GREAT_BULWARK: lambda state: state.has(ItemName.TOOLS_ICE_AXES),
    #    PeakName.NORTHERN_SOLEMN_TEMPEST: lambda state: state.has(ItemName.TOOLS_ICE_AXES),
    #}
    #locations = world.poy_data_locations[this.name]
    #

    def __init__(self, data: PoYRegionData, *args, **kwargs) -> None:
        """
        Initializes a PeaksRegion.

        :param data: The data for this region
        :param args: Arguments to pass to Region
        :param kwargs: Keyword arguments to pass to Region
        """

        self.poy_data = data
        super().__init__(*args, **kwargs)

    def poy_create_connections(self, world: "PeaksWorld") -> None:
        """
        Creates all required connections for this region.
        """

        for region_name in self.poy_data.connections:
            self.poy_connections[region_name] = self.connect(
                world.poy_created_regions[region_name]
            )

    def poy_create_locations(self, world: "PeaksWorld") -> None:
        """
        Creates all locations for this region.
        """

        for data in self.poy_data.locations:
            location = PeaksLocation(
                data, world.player, data.name, self
            )
            location.poy_create_item(world)

            self.locations.append(location)

    def poy_set_rules(self) -> None:
        """
        Sets access rules for entrance randomisation.
        """

        # Set region access rules
        for region_name, rule in self.poy_data.rules_connections.items():
            add_rule(
                self.poy_connections[region_name],
                rule
            )


class PeaksWorld(World):
    """
    Travel around The Great Gales to climb challenging peaks in this
    physics-based climbing adventure set in 1887. Meet like-minded
    mountaineers, unlock helpful climbing gear, and become a pioneer
    of mountaineering.
    """

    game = GAME

    options_dataclass = PeaksOptions
    options: PeaksOptions

    # Regions which have been created for this world
    poy_created_regions: dict[str, PeaksRegion]

    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes a PeaksWorld.
        """

        # Build the tables of all regions, locations, and items
        handler = IDHandler()

        self.poy_data_regions = PeaksRegions(handler)

        super().__init__(*args, **kwargs)

    @override
    def create_item(self, name: str) -> PeaksItem:
        """
        Creates an item on demand given its name.

        :param name: The name of the item to create
        :returns: The created item
        """

        item: PoYItemData = self.poy_items.get_item(name)
        return PeaksItem(name, item.classification, item.id, self.player)

    def poy_create_region(self, name: str, data: PoYRegionData | None) -> PeaksRegion:
        region = PeaksRegion(data, name, self.player, self.multiworld)

        self.poy_created_regions[name] = region
        self.multiworld.regions.append(region)

        return region

    def poy_create_category(self, category: List[PoYRegionData]) -> None:
        """
        Creates all regions within a given category.

        :param category: The data for regions within this category
        """

        for data in category:
            self.poy_create_region(data.name, data)

    @override
    def create_regions(self) -> None:
        """
        Creates all the regions.
        """

        # Add enabled categories
        if self.options.enable_fundamentals is True:
            self.poy_create_category(category_fundamentals)

        if self.options.enable_intermediate is True:
            self.poy_create_category(category_intermediate)

        if self.options.enabled_advanced is True:
            self.poy_create_category(category_advanced)

        if self.options.enable_expert is True:
            self.poy_create_category(category_expert)

        if self.options.enable_alp_essentials is True:
            self.poy_create_category(category_alp_essentials)

        if self.options.enable_alp_greats is True:
            self.poy_create_category(category_alp_greats)

        if self.options.enable_alp_arctic is True:
            self.poy_create_category(category_alp_arctic)

        # Add cabins for regions
        # which are enabled

        # Add gales cabin
        if self.options.enable_fundamentals is True \
                or self.options.enable_intermediate is True \
                or self.options.enable_advanced is True:
            self.poy_create_region(
                cabin_gales.name, cabin_gales
            )

        # Add northern cabin
        if self.options.enable_expert is True:
            self.poy_create_region(
                cabin_northern.name, cabin_northern
            )

        # Add alps cabin
        if self.options.enable_alp_essentials is True \
                or self.options.enable_alp_greats is True \
                or self.options.enable_alp_arctic is True:
            self.poy_create_region(
                cabin_alps.name, cabin_alps
            )

        # Connect the menu to the gales cabin
        self.poy_created_regions["Menu"] = self.poy_create_region("Menu", None)
        self.poy_created_regions["Menu"].connect(
            self.poy_created_regions[cabin_gales.name]
        )

        for region in self.poy_created_regions.value():
            region.poy_create_connections(self)
            region.poy_create_locations(self)

    @override
    def set_rules(self) -> None:
        """
        Creates access rules for regions, locations, and items.
        """

        for region in self.poy_created_regions:
            region.poy_set_rules()
