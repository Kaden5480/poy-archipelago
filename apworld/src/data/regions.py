from enum import StrEnum
from typing import Callable

from BaseClasses import Entrance, \
                        Region

from .items import PoYItemName
from .locations import PoYLocationData, \
                       PeaksLocation

class PoYRegionName(StrEnum):
    GALES_CABIN                  = "Great Gales Cabin"
    NORTHERN_CABIN               = "Northern Cabin"
    ALPS_CABIN                   = "Alps Cabin"

    # Fundamentals
    GALES_GREENHORNS_TOP         = "Greenhorn's Top"
    GALES_PALTRY_PEAK            = "Paltry Peak"
    GALES_OLD_MILL               = "Old Mill"
    GALES_GRAY_GULLY             = "Gray Gully"
    GALES_THE_LIGHTHOUSE         = "The Lighthouse"
    GALES_OLD_MAN_OF_SJOR        = "Old Man of Sjór"
    GALES_GIANTS_SHELF           = "Giant's Shelf"
    GALES_EVERGREENS_END         = "Evergreen's End"
    GALES_THE_TWINS              = "The Twins"
    GALES_OLD_GROVES_SKELF       = "Old Grove's Skelf"
    GALES_HANGMANS_LEAP          = "Hangman's Leap"
    GALES_LANDS_END              = "Land's End"
    GALES_OLD_LANGR              = "Old Langr"
    GALES_ALDR_GROTTO            = "Aldr Grotto"
    GALES_THREE_BROTHERS         = "Three Brothers"
    GALES_WALTERS_CRAG           = "Walter's Crag"
    GALES_THE_GREAT_CREVICE      = "The Great Crevice"
    GALES_OLD_HAGGER             = "Old Hagger"
    GALES_UGSOME_STORR           = "Ugsome Stórr"
    GALES_WUTHERING_CREST        = "Wuthering Crest"

    # Intermediate
    GALES_PORTERS_BOULDER        = "Porter's Boulder"
    GALES_JOTUNNS_THUMB          = "Jotunn's Thumb"
    GALES_OLD_SKERRY             = "Old Skerry"
    GALES_HAMARR_STONE           = "Hamarr Stone"
    GALES_GIANTS_NOSE            = "Giant's Nose"
    GALES_WALTERS_BOULDER        = "Walter's Boulder"
    GALES_SUNDERED_SONS          = "Sundered Sons"
    GALES_OLD_WEALDS_BOULDER     = "Old Weald's Boulder"
    GALES_LEANING_SPIRE          = "Leaning Spire"
    GALES_CROMLECH               = "Cromlech"

    # Advanced
    GALES_WALKERS_PILLAR         = "Walker's Pillar"
    GALES_GREAT_GAOL             = "Great Gaol"
    GALES_ELDENHORN              = "Eldenhorn"
    GALES_ST_HAELGA              = "St. Haelga"
    GALES_YMIRS_SHADOW           = "Ymir's Shadow"

    # Expert
    NORTHERN_GREAT_BULWARK       = "Great Bulwark"
    NORTHERN_SOLEMN_TEMPEST      = "Solemn Tempest"

    # Essentials
    ALPS_TUTORS_TOWER            = "Tutor's Tower"
    ALPS_STOUGR_BOULDER          = "Stougr Boulder"
    ALPS_MARAS_ARCH              = "Mara's Arch"
    ALPS_GRAINNE_SPIRE           = "Grainne Spire"
    ALPS_GREAT_BOK_TREE          = "Great Bók Tree"
    ALPS_TREPPENWALD             = "Treppenwald"
    ALPS_CASTLE_OF_THE_SWAN_KING = "Castle of the Swan King"
    ALPS_SEASIDE_TRIBUNE         = "Seaside Tribune"
    ALPS_IVORY_GRANITES          = "Ivory Granites"
    ALPS_OLD_REKKJA              = "Old Rekkja"
    ALPS_QUIETUDE                = "Quietude"
    ALPS_ELJUNS_FOLLY            = "Eljun's Folly"

    # Alpine Greats
    ALPS_EINVALD_FALLS           = "Einvald Falls"
    ALPS_ALMATTR_DAM             = "Almáttr Dam"
    ALPS_DUNDERHORN              = "Dunderhorn"
    ALPS_MHOR_DRUIM              = "Mhòr Druim"
    ALPS_WELKIN_PASS             = "Welkin Pass"

    # Arduous and Arctic
    ALPS_SEIGR_CRAEG             = "Seigr Craeg"
    ALPS_ULLRS_CHASM             = "Ullr's Chasm"
    ALPS_GREAT_SILF              = "Great Silf"
    ALPS_TOWERING_VISIR          = "Towering Vísir"
    ALPS_ELDRIS_WALL             = "Eldris Wall"
    ALPS_MOUNT_MHORGORM          = "Mount Mhòrgorm"


gales_fundamentals: list[PoYRegionName] = [
    GALES_GREENHORNS_TOP,
    GALES_PALTRY_PEAK,
    GALES_OLD_MILL,
    GALES_GRAY_GULLY,
    GALES_THE_LIGHTHOUSE,
    GALES_OLD_MAN_OF_SJOR,
    GALES_GIANTS_SHELF,
    GALES_EVERGREENS_END,
    GALES_THE_TWINS,
    GALES_OLD_GROVES_SKELF,
    GALES_HANGMANS_LEAP,
    GALES_LANDS_END,
    GALES_OLD_LANGR,
    GALES_ALDR_GROTTO,
    GALES_THREE_BROTHERS,
    GALES_WALTERS_CRAG,
    GALES_THE_GREAT_CREVICE,
    GALES_OLD_HAGGER,
    GALES_UGSOME_STORR,
    GALES_WUTHERING_CREST,
]

gales_intermediate: list[PoYRegionName] = [
    GALES_PORTERS_BOULDER,
    GALES_JOTUNNS_THUMB,
    GALES_OLD_SKERRY,
    GALES_HAMARR_STONE,
    GALES_GIANTS_NOSE,
    GALES_WALTERS_BOULDER,
    GALES_SUNDERED_SONS,
    GALES_OLD_WEALDS_BOULDER,
    GALES_LEANING_SPIRE,
    GALES_CROMLECH,
]

gales_advanced: list[PoYRegionName] = [
    GALES_WALKERS_PILLAR,
    GALES_GREAT_GAOL,
    GALES_ELDENHORN,
    GALES_ST_HAELGA,
    GALES_YMIRS_SHADOW,
]

northern_expert: list[PoYRegionName] = [
    NORTHERN_GREAT_BULWARK,
    NORTHERN_SOLEMN_TEMPEST,
]

alps_essentials: list[PoYRegionName] = [
    ALPS_TUTORS_TOWER,
    ALPS_STOUGR_BOULDER,
    ALPS_MARAS_ARCH,
    ALPS_GRAINNE_SPIRE,
    ALPS_GREAT_BOK_TREE,
    ALPS_TREPPENWALD,
    ALPS_CASTLE_OF_THE_SWAN_KING,
    ALPS_SEASIDE_TRIBUNE,
    ALPS_IVORY_GRANITES,
    ALPS_OLD_REKKJA,
    ALPS_QUIETUDE,
    ALPS_ELJUNS_FOLLY,
]

alps_greats: list[PoYRegionName] = [
    ALPS_EINVALD_FALLS,
    ALPS_ALMATTR_DAM,
    ALPS_DUNDERHORN,
    ALPS_MHOR_DRUIM,
    ALPS_WELKIN_PASS,
]

alps_arctic: list[PoYRegionName] = [
    ALPS_SEIGR_CRAEG,
    ALPS_ULLRS_CHASM,
    ALPS_GREAT_SILF,
    ALPS_TOWERING_VISIR,
    ALPS_ELDRIS_WALL,
    ALPS_MOUNT_MHORGORM,
]


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
        :param categories: A tuple of (list[PoYRegionName], Callable)
                           which indicates each category and the required
                           book to access the category
        :returns: The created cabin data
        """

        connections = {}

        for regions, rule in categories:
            connections.update({
                region_name: rule
                for region_name in regions
            })

        data = PoYRegionData(id, name)
        data.connections = connections


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
        Initializes PoYRegions.

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
            (gales_fundamentals, lambda state: state.has(PoYItemName.BOOK_GALES_FUNDAMENTALS)),
            (gales_intermediate, lambda state: state.has(PoYItemName.BOOK_GALES_INTERMEDIATE)),
            (gales_advanced,     lambda state: state.has(PoYItemName.BOOK_GALES_ADVANCED))
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
            (northern_expert, lambda state: state.has(PoYItemName.BOOK_NORTHERN_EXPERT) \
                    and state.has(PoYItemName.TOOLS_ICE_AXES))
        )

        # Northern cabin can always access the DLC
        self.northern_cabin.add_connection(PoYRegionName.ALPS_CABIN)

        ### Alps DLC
        self.alps_cabin = PoYRegionData.create_cabin(
            handler.new_id(),
            PoYRegionName.ALPS_CABIN,
            (alps_essentials, lambda state: state.has(PoYItemName.BOOK_ALPS_ESSENTIALS)),
            (alps_greats,     lambda state: state.has(PoYItemName.BOOK_ALPS_GREATS)),
            (alps_arctic,     lambda state: state.has(PoYItemName.BOOK_ALPS_ARCTIC) \
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
