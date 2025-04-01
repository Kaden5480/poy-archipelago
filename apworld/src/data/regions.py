from typing import Callable

from BaseClasses import Entrance, \
                        Region

from .locations import PoYLocationData, \
                       PeaksLocation


class PoYRegionData:
    id: int
    name: PoYRegionName

    # Any regions which can be accessed from this region,
    # including applicable access rules for being able
    # to reach them
    connections: dict[PoYRegionName, Callable[[object], bool] | None]

    # Locations which are accessible within this region
    locations: list[PoYLocationData]

    def __init__(self, id: int, name: PoYRegionName) -> None:
        """
        Initializes a PoYRegionData.

        :param id: The ID of this data
        :param name: The name of this region
        """

        self.id = id
        self.name = name
        self.connections = {}
        self.locations = []

    def add_connection(
        self,
        region_name: PoYRegionName,
        rule: Callable[[object], bool] | None = None
    ) -> None:
        """
        Adds a connection to a given region name,
        with the provided rule to access it.

        :param region_name: The region to add a connection for
        :param rule: The rule which locks this region, if any
        """

        self.connections[region_name] = rule

    def add_location(self, location: PoYLocationData) -> None:
        """
        Adds a location to this region.

        :param location: The location to add
        """

        self.locations.append(location)

    @staticmethod
    def create_cabin(
        id: int,
        name: PoYRegionName,
        *categories
    ) -> PoYRegionData:
        """
        Creates data for a cabin, assigning
        connections to the categories it can access
        along with rules which indicate which books
        are required to access the category.

        :param id: The ID of the cabin
        :param name: The name of the cabin
        :param categories: A tuple of (PoYRegionData, Callable)
                           which indicates each category and the required
                           book to access the category
        :returns: The created cabin data
        """

        connections = {}

        for regions, rule in categories:
            connections.update({
                region_data.name: rule
                for region_data in regions
            })

        data = PoYRegionData(id, name)
        data.connections = connections


class PeaksRegion(Region):
    game: str = "Peaks of Yore"
    poy_data: PoYRegionData
    poy_connections: dict[PoYRegionName, Entrance]

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

        for region_name in self.poy_data.connections.keys():
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
        for region_name, rule in self.poy_data.connections.items():
            if rule is None:
                continue

            add_rule(
                self.poy_connections[region_name],
                rule
            )


class PoYRegions:
    handler: IDHandler

    # Cabins
    gales_cabin: PoYRegionData
    northern_cabin: PoYRegionData
    alps_cabin: PoYRegionData

    # Peaks
    gales_fundamentals: dict[PoYRegionName, PoYRegionData]
    gales_intermediate: dict[PoYRegionName, PoYRegionData]
    gales_advanced: dict[PoYRegionName, PoYRegionData]

    northern_expert: dict[PoYRegionName, PoYRegionData]

    alps_essentials: dict[PoYRegionName, PoYRegionData]
    alps_greats: dict[PoYRegionName, PoYRegionData]
    alps_arctic: dict[PoYRegionName, PoYRegionData]

    def __init__(self, handler: IDHandler) -> None:
        """
        Initializes a PoYRegions.

        :param handler: The handler for assigning IDs to data
        """

        self.handler = handler

        ## Peaks
        # Great Gales
        self.gales_fundamentals = self.create_category(gales_fundamentals)
        self.gales_intermediate = self.create_category(gales_intermediate)
        self.gales_advanced = self.create_category(gales_advanced)

        # Northern Range
        self.northern_expert = self.create_category(northern_expert)

        # Alps DLC
        self.alps_essentials = self.create_category(alps_essentials)
        self.alps_greats = self.create_category(alps_greats)
        self.alps_arctic = self.create_category(alps_arctic)

        # Cabins
        ### Great Gales
        self.gales_cabin = PoYRegionData.create_cabin(
            handler.new_id(),
            PoYRegionName.GALES_CABIN,
            (self.gales_fundamentals.keys(), lambda state: state.has(PoYItemName.BOOK_GALES_FUNDAMENTALS)),
            (self.gales_intermediate.keys(), lambda state: state.has(PoYItemName.BOOK_GALES_INTERMEDIATE)),
            (self.gales_advanced.keys(),     lambda state: state.has(PoYItemName.BOOK_GALES_ADVANCED))
        )

        # Gales cabin can always access the DLC
        self.gales_cabin.add_connection(PoYRegionName.ALPS_CABIN)

        # Must unlock the ticket to the northern range to
        # access the northern cabin
        self.gales_cabin.add_connection(
            PoYRegionName.NORTHERN_CABIN,
            lambda state: state.has(PoYItemName.TICKET_NORTHERN_RANGE)
        )

        ### Northern Range
        self.northern_cabin = PoYRegionData.create_cabin(
            handler.new_id(),
            PoYRegionName.NORTHERN_CABIN,
            # Need the expert book and ice axes to be able to access bulwark + st
            (self.northern_expert, lambda state: state.has(PoYItemName.BOOK_NORTHERN_EXPERT) \
                    and state.has(PoYItemName.TOOLS_ICE_AXES))
        )

        # Northern cabin can always access the DLC
        self.northern_cabin.add_connection(PoYRegionName.ALPS_CABIN)

        ### Alps DLC
        self.alps_cabin = PoYRegionData.create_cabin(
            handler.new_id(),
            PoYRegionName.ALPS_CABIN,
            (self.alps_essentials, lambda state: state.has(PoYItemName.BOOK_ALPS_ESSENTIALS)),
            (self.alps_greats,     lambda state: state.has(PoYItemName.BOOK_ALPS_GREATS)),
            (self.alps_arctic,     lambda state: state.has(PoYItemName.BOOK_ALPS_ARCTIC) \
                    and state.has(PoYItemName.TOOLS_ICE_AXES))
        )

        # Alps cabin can always access the Gales cabin
        self.alps_cabin.add_connection(PoYRegionName.GALES_CABIN)

    def create_category(
        self,
        category: list[PoYRegionName]
    ) -> dict[PoYRegionName, PoYRegionData]:
        """
        Creates name to data mappings for all regions
        in a given category.

        :param category: The peaks in the category
        :returns: The mappings
        """

        return {
            name: PoYRegionData(self.handler.new_id(), name)
            for name in category
        }
