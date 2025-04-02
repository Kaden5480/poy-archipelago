from worlds.AutoWorld import World

from BaseClasses import CollectionState, \
                        Entrance, \
                        Item, \
                        Location, \
                        Region

from .data.id_handler import IDHandler
from .data.regions import PeaksRegion, \
                          PoYRegions, \
                          PoYRegionName, \
                          gales_fundamentals, \
                          gales_intermediate, \
                          gales_advanced, \
                          northern_expert, \
                          alps_essentials, \
                          alps_greats, \
                          alps_arctic

from .data.locations import PoYLocationName, \
                            PoYLocations

from .data.items import PoYItemName, \
                        PoYItems

from .options import PeaksOptions

GAME: str = "Peaks of Yore"



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

    # Data
    poy_data_regions: PoYRegions
    poy_data_items: PoYItems
    poy_data_locations: PoYLocations

    # Regions which have been created for this world
    poy_created_regions: dict[PoYRegionName, PeaksRegion]

    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes a PeaksWorld.
        """

        # Build the tables of all regions, locations, and items
        handler = IDHandler()

        self.poy_data_items = PoYItems(handler)
        self.poy_data_locations = PoYLocations(handler)
        self.poy_data_regions = PoYRegions(handler)

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

    def poy_create_region(self, name: PoYRegionName, data: PoYRegionData | None) -> PeaksRegion:
        region = PeaksRegion(data, name.value, self.player, self.multiworld)

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

    def poy_push_precollected(self, *names) -> None:
        """
        Pushes an item as precollected.

        :param names: The names of the item to push
        """

        for name in names:
            self.multiworld.push_precollected(
                self.create_item(name.value)
            )

    @override
    def generate_early(self) -> None:
        """
        Early generation of the world.
        """

        # Start with barometer and map
        if self.options.starting_barometer is True:
            self.poy_push_precollected(
                PoYItemName.TOOL_BAROMETER
                PoYItemName.TOOL_ARTEFACT_MAP
            )

        # Force fundamentals
        self.poy_push_precollected(
            PoYItemName.BOOK_GALES_FUNDAMENTALS
        )

        # TODO: potential issues with some categories being enabled/disabled
        # e.g. intermediate but no fundamentals to access it

    @override
    def create_regions(self) -> None:
        """
        Creates all the regions.
        """

        self.poy_created_regions = {}

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
    def create_items(self) -> None:
        """
        Creates items, adding them to the item pool.
        """

        local_pool = []
        self.multiworld.itempool += self.local_pool

    def add_cabin_rule(
        self,
        cabin: PoYRegionName,
        category: list[PoYRegionName],
        rule: Callable[[object], bool]
    ) -> None:
        """
        Adds a rule for accessing different peaks
        from the cabin.

        :param cabin: The cabin to add a rule for
        :param category: The category to add a rule for
        :param rule: The rule to add
        """

        connections = self.poy_created_regions[cabin].poy_connections

        for region_name, entrance in connections:
            if region_name in category:
                continue

            add_rule(entrance, rule)

    @override
    def set_rules(self) -> None:
        """
        Creates access rules for regions, locations, and items.
        """

        # Create access rules for regions
        # Intermediate
        if self.options.enable_intermediate is True:
            self.add_cabin_rule(
                PoYRegionName.GALES_CABIN,
                gales_intermediate,
                lambda state: state.has(
                    PoYItemName.STAMP_GALES_FUNDAMENTALS.value
                    self.player,
                    count = 15
                )
            )

        # Advanced
        if self.options.enable_advanced is True:
            self.add_cabin_rule(
                PoYRegionName.GALES_CABIN,
                gales_advanced,
                lambda state: state.has(
                    PoYItemName.STAMP_GALES_INTERMEDIATE.value,
                    self.player,
                    count = 5
                )
            )

        # TODO: Ymir's shadow gives access as well
        # Expert
        if self.options.enable_expert is True:
            self.add_cabin_rule(
                PoYRegionName.GALES_CABIN,
                [PoYRegionName.NORTHERN_CABIN],
                lambda state: state.has(
                    PoYItemName.STAMP_GALES_ADVANCED.value,
                    self.player,
                    count = 3
                )
            )

        # Tool unlocks
        # TODO: These aren't really accurate, a stamp
        # location needs to be made for a lot of these unlocks
        add_rule(
            self.multiworld.get_location(PoYLocationName.TOOL_CRAMPONS_6),
            lambda state: state.has(
                STAMP_GALES_FUNDAMENTALS.value,
                self.player,
                count = 10
            )
        )
        add_rule(
            self.multiworld.get_location(PoYLocationName.TOOL_CRAMPONS_10),
            lambda state: state.has(
                STAMP_GALES_ADVANCED.value,
                self.player,
                count = 3
            )
        )
        add_rule(
            self.multiworld.get_location(PoYLocationName.TOOL_ICE_AXES),
            lambda state: state.has(
                STAMP_GALES_ADVANCED.value,
                self.player,
                count = 3
            )
        )


        # If require crampons is set, make sure
        # that Expert and Arduous and Arctic peaks require
        # access to crampons before being accessible
        if self.options.require_crampons is True:
            def has_crampons(state: CollectionState) -> bool:
                return state.has(PoYItemName.TOOL_CRAMPONS_6.value, self.player) \
                        or state.has(PoYItemName.TOOL_CRAMPONS_10.value, self.player)

            region: PeaksRegion = self.poy_created_regions[PoYRegionName.NORTHERN_CABIN]
            for region in self.poy_data_regions.northern_expert.keys():
                add_rule(region, has_crampons)

            if self.options.enable_alps_arctic is True:
                region: PeaksRegion = self.poy_created_regions[PoYRegionName.ALPS_CABIN]
                for region in self.poy_data_regions.alps_arctic.keys():
                    add_rule(region, has_crampons)

        ## DLC
        # Alpine greats
        if self.options.enable_alp_greats is True
            self.add_cabin_rule(
                PoYRegionName.ALPS_CABIN,
                alps_greats,
                lambda state: state.has(
                    PoYItemName.STAMP_ALPS_ESSENTIALS.value,
                    self.player,
                    count = 10
                )
            )

        # Arduous and Arctic
        if self.options.enable_alp_arctic is True:
            self.add_cabin_rule(
                PoYRegionName.ALPS_CABIN,
                alps_arctic,
                lambda state: state.has(
                    PoYItemName.STAMP_ALPS_GREATS.value,
                    self.player,
                    count = 3
                )
            )


    @override
    def connect_entrances(self) -> None:
        """
        Connects entrances for randomisation.
        """

        if self.options.randomise_levels is False:
            return
