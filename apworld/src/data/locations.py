from .id_handler import IDHandler

from ..names.items import ItemName, \
                          BaseItemName, \
                          DlcItemName

from ..names.locations import LocationName, \
                              BaseLocationName, \
                              DlcLocationName, \
                              LocationSuffix

from ..names.regions import RegionName, \
                            CabinRegionName, \
                            PeakName, \
                            FundamentalsRegionName, \
                            IntermediateRegionName, \
                            AdvancedRegionName, \
                            ExpertRegionName, \
                            EssentialsRegionName, \
                            GreatsRegionName, \
                            ArcticRegionName

class LocationData:
    __id: int
    __name: str
    __item_name: str

    def __init__(
        self,
        id: int,
        name: str,
        item_name: str
    ) -> None:
        """
        Initializes a LocationData object.

        :param id: The ID of this location
        :param name: The name of this location
        :param item_name: The item locked behind this location (or dropped by it)
        """

        self.__id = id
        self.__name = name
        self.__item_name = item_name

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def item_name(self) -> str:
        return self.__item_name


class Locations:
    __handler: IDHandler
    __region_to_locations: dict[str, list[LocationData]]
    __locations: dict[str, LocationData]

    def __init__(self, handler: IDHandler) -> None:
        """
        Initializes a Locations object.

        :param handler: The handler to assign IDs with
        """

        self.__handler = handler
        self.__region_to_locations = {}
        self.__locations = {}

        self.__create_all()

    def get_data(
        self,
        name: LocationName
    ) -> LocationData | None:
        """
        Gets data for a location by a given name.

        :param name: The name of the location to get data for
        :returns: The location data, or None if not found
        """

        return self.__locations.get(name.value, None)

    def get_data_suffix(
        self,
        region: RegionName,
        suffix: LocationSuffix
    ) -> LocationData | None:
        """
        Gets data for a location by a given region
        and location suffix.

        :param region: The region the location is within
        :param suffix: The suffix of the location
        :returns: The data for this location or None if not found
        """

        return self.__locations.get(
            f"{region.value} {suffix.value}",
            None
        )

    def get_data_for_region(
        self,
        region: RegionName
    ) -> list[LocationData]:
        """
        Gets data for all locations in a given region.

        :param region: The region to get locations for
        :returns: The list of all location data for this region,
                  or an empty list of none was found
        """

        return self.__region_to_locations.get(
            region.value, []
        )

    def __create_data(
        self,
        name: LocationName | LocationSuffix,
        region: RegionName,
        item_name: ItemName
    ) -> None:
        """
        Creates location data and stores it.

        :param name: The name of the location, or its suffix
        :param region_name: The region this location is for
        :param item_name: The item locked behind this location
        """

        region_name = region.value

        # By default, just use the name of the location
        data_name = name.value

        # If a suffix is provided, append the suffix
        # to the name of the region
        if type(name) == LocationSuffix:
            data_name = f"{region_name.value} {name.value}"

        # Create the data
        data = LocationData(
            self.__handler.new_id(), data_name, item_name.value
        )

        # If this region has no list of locations yet,
        # create an empty list for it
        if region_name not in self.__region_to_locations:
            self.__region_to_locations[region_name] = []

        # Store the location data
        self.__region_to_locations[region_name].append(data)
        self.__locations[data_name] = data

    def __create_stamps(
        self,
        category: PeakName,
        stamp: ItemName
    ) -> None:
        """
        Creates the stamp locations for all
        peaks in a given category.

        :param category: The peaks in the category
        :param stamp: The type of stamp for this category
        """

        for region in category:
            self.__create_data(
                LocationSuffix.STAMP,
                region, stamp
            )

    def __create_all(self) -> None:
        """
        Creates data for all locations.
        """

        ## Base game
        # Artefacts
        self.__create_data(
            BaseLocationName.HAT_OLD_MILL,
            FundamentalsRegionName.OLD_MILL,
            BaseItemName.HAT_1
        )
        self.__create_data(
            BaseLocationName.HAT_EVERGREENS_END,
            FundamentalsRegionName.EVERGREENS_END,
            BaseItemName.HAT_2
        )
        self.__create_data(
            BaseLocationName.SHOE_OLD_MAN_OF_SJOR,
            FundamentalsRegionName.OLD_MAN_OF_SJOR,
            BaseItemName.SHOE
        )
        self.__create_data(
            BaseLocationName.SLEEPING_BAG_GIANTS_SHELF,
            FundamentalsRegionName.GIANTS_SHELF,
            BaseItemName.SLEEPING_BAG
        )
        self.__create_data(
            BaseLocationName.SAFETY_HELMET_OLD_GROVES_SKELF,
            FundamentalsRegionName.OLD_GROVES_SKELF,
            BaseItemName.SAFETY_HELMET
        )
        self.__create_data(
            BaseLocationName.BACKPACK_ALDR_GROTTO,
            FundamentalsRegionName.ALDR_GROTTO,
            BaseItemName.BACKPACK
        )
        self.__create_data(
            BaseLocationName.SHOVEL_THREE_BROTHERS,
            FundamentalsRegionName.THREE_BROTHERS,
            BaseItemName.SHOVEL
        )

        # The picture pieces
        self.__create_data(
            BaseLocationName.PICTURE_GRAY_GULLY,
            FundamentalsRegionName.GRAY_GULLY,
            BaseItemName.PICTURE_FRAGMENT
        )
        self.__create_data(
            BaseLocationName.PICTURE_LANDS_END,
            FundamentalsRegionName.LANDS_END,
            BaseItemName.PICTURE_FRAGMENT
        )
        self.__create_data(
            BaseLocationName.PICTURE_THE_GREAT_CREVICE,
            FundamentalsRegionName.THE_GREAT_CREVICE,
            BaseItemName.PICTURE_FRAGMENT
        )
        self.__create_data(
            BaseLocationName.PICTURE_ST_HAELGA,
            AdvancedRegionName.ST_HAELGA,
            BaseItemName.PICTURE_FRAGMENT
        )
        self.__create_data(
            BaseLocationName.PICTURE_FRAME_GREAT_GAOL,
            AdvancedRegionName.GREAT_GAOL,
            BaseItemName.PICTURE_FRAME
        )

        # Statues
        self.__create_data(
            BaseLocationName.STATUE_FUNDAMENTALS_WALTERS_CRAG,
            FundamentalsRegionName.WALTERS_CRAG,
            BaseItemName.STATUE_FUNDAMENTALS
        )
        self.__create_data(
            BaseLocationName.STATUE_INTERMEDIATE_LEANING_SPIRE,
            IntermediateRegionName.LEANING_SPIRE,
            BaseItemName.STATUE_INTERMEDIATE
        )
        self.__create_data(
            BaseLocationName.STATUE_ADVANCED_YMIRS_SHADOW,
            AdvancedRegionName.YMIRS_SHADOW,
            BaseItemName.STATUE_ADVANCED
        )
        self.__create_data(
            BaseLocationName.STATUE_EXPERT_BULWARK,
            ExpertRegionName.GREAT_BULWARK,
            BaseItemName.STATUE_EXPERT
        )

        # Bird seeds
        self.__create_data(
            BaseLocationName.BIRD_SEEDS_THREE_BROTHERS,
            FundamentalsRegionName.THREE_BROTHERS,
            BaseItemName.BIRD_SEEDS
        )
        self.__create_data(
            BaseLocationName.BIRD_SEEDS_OLD_SKERRY,
            IntermediateRegionName.OLD_SKERRY,
            BaseItemName.BIRD_SEEDS
        )
        self.__create_data(
            BaseLocationName.BIRD_SEEDS_GREAT_GAOL,
            AdvancedRegionName.GREAT_GAOL,
            BaseItemName.BIRD_SEEDS
        )
        self.__create_data(
            BaseLocationName.BIRD_SEEDS_ELDENHORN,
            AdvancedRegionName.ELDENHORN,
            BaseItemName.BIRD_SEEDS
        )
        self.__create_data(
            BaseLocationName.BIRD_SEEDS_YMIRS_SHADOW,
            AdvancedRegionName.YMIRS_SHADOW,
            BaseItemName.BIRD_SEEDS
        )

        # Chalk
        self.__create_data(
            BaseLocationName.CHALK_WALKERS_PILLAR,
            AdvancedRegionName.WALKERS_PILLAR,
            BaseItemName.CHALK
        )
        self.__create_data(
            BaseLocationName.CHALK_ELDENHORN,
            AdvancedRegionName.ELDENHORN,
            BaseItemName.CHALK
        )

        # Coffee
        self.__create_data(
            BaseLocationName.COFFEE_OLD_LANGR,
            FundamentalsRegionName.OLD_LANGR,
            BaseItemName.COFFEE_2
        )
        self.__create_data(
            BaseLocationName.COFFEE_WUTHERING_CREST,
            FundamentalsRegionName.WUTHERING_CREST,
            BaseItemName.COFFEE_2
        )

        # Rope
        self.__create_data(
            BaseLocationName.ROPE_OLD_MAN_OF_SJOR,
            FundamentalsRegionName.OLD_MAN_OF_SJOR,
            BaseItemName.ROPES_2
        )
        self.__create_data(
            BaseLocationName.ROPE_EVERGREENS_END,
            FundamentalsRegionName.EVERGREENS_END,
            BaseItemName.ROPES_2
        )
        self.__create_data(
            BaseLocationName.ROPE_HANGMANS_LEAP,
            FundamentalsRegionName.HANGMANS_LEAP,
            BaseItemName.ROPES_2
        )
        self.__create_data(
            BaseLocationName.ROPE_LANDS_END,
            FundamentalsRegionName.LANDS_END,
            BaseItemName.ROPES_2
        )
        self.__create_data(
            BaseLocationName.ROPE_WALTERS_CRAG,
            FundamentalsRegionName.WALTERS_CRAG,
            BaseItemName.ROPES_2
        )
        self.__create_data(
            BaseLocationName.ROPE_THE_GREAT_CREVICE,
            FundamentalsRegionName.THE_GREAT_CREVICE,
            BaseItemName.ROPES_2
        )
        self.__create_data(
            BaseLocationName.ROPE_OLD_HAGGER,
            FundamentalsRegionName.OLD_HAGGER,
            BaseItemName.ROPES_2
        )
        self.__create_data(
            BaseLocationName.ROPE_UGSOME_STORR,
            FundamentalsRegionName.UGSOME_STORR,
            BaseItemName.ROPES_2
        )
        self.__create_data(
            BaseLocationName.ROPE_WUTHERING_CREST,
            FundamentalsRegionName.WUTHERING_CREST,
            BaseItemName.ROPES_2
        )
        self.__create_data(
            BaseLocationName.ROPE_GREAT_GAOL,
            AdvancedRegionName.GREAT_GAOL,
            BaseItemName.ROPES_2
        )
        self.__create_data(
            BaseLocationName.ROPE_ELDENHORN,
            AdvancedRegionName.ELDENHORN,
            BaseItemName.ROPES_2
        )
        self.__create_data(
            BaseLocationName.ROPE_YMIRS_SHADOW,
            AdvancedRegionName.YMIRS_SHADOW,
            BaseItemName.ROPES_2
        )

        # NPC events
        self.__create_data(
            BaseLocationName.NPC_COFFEE_THE_TWINS,
            FundamentalsRegionName.THE_TWINS,
            BaseItemName.COFFEE_5
        )
        self.__create_data(
            BaseLocationName.NPC_COFFEE_GIANTS_NOSE,
            IntermediateRegionName.GIANTS_NOSE,
            BaseItemName.COFFEE_5
        )
        self.__create_data(
            BaseLocationName.NPC_ROPE_WALTERS_CRAG,
            FundamentalsRegionName.WALTERS_CRAG,
            BaseItemName.ROPES_1
        )
        self.__create_data(
            BaseLocationName.NPC_ROPE_WALKERS_PILLAR,
            AdvancedRegionName.WALKERS_PILLAR,
            BaseItemName.ROPES_1
        )
        self.__create_data(
            BaseLocationName.NPC_ROPE_GREAT_GAOL,
            AdvancedRegionName.GREAT_GAOL,
            BaseItemName.ROPES_1
        )
        self.__create_data(
            BaseLocationName.NPC_ROPE_ST_HAELGA,
            AdvancedRegionName.ST_HAELGA,
            BaseItemName.ROPES_1
        )

        # Tools

        # The artefact map and barometer are locked behind
        # 5 fundamentals AND any items in the fundamentals
        self.__create_data(
            BaseLocationName.TOOL_ARTEFACT_MAP,
            FundamentalsRegionName.CATEGORY,
            BaseItemName.TOOL_ARTEFACT_MAP
        )
        self.__create_data(
            BaseLocationName.TOOL_BAROMETER,
            FundamentalsRegionName.CATEGORY,
            BaseItemName.TOOL_BAROMETER
        )

        # The rules for unlocking chalk involve checks
        # for advanced OR fundamental peaks, so set rules for
        # this instead
        self.__create_data(
            BaseLocationName.TOOL_CHALK_BAG,
            CabinRegionName.GALES,
            BaseItemName.TOOL_CHALK_BAG
        )

        # The coffee is locked behind fundamentals
        # but can be accessed by either completing the twins,
        # OR picking up a coffee box
        self.__create_data(
            BaseLocationName.TOOL_COFFEE,
            FundamentalsRegionName.CATEGORY,
            BaseItemName.TOOL_COFFEE
        )

        # Crampons are locked behind Old Grove's Skelf
        # OR by completing any 10 base game peaks
        #
        # As progression only increases for the base game
        # in the Gales or Northern range, we can assume
        # access to the Gales cabin is required, as the
        # Northern range would never give enough peaks
        self.__create_data(
            BaseLocationName.TOOL_CRAMPONS_6,
            CabinRegionName.GALES,
            BaseItemName.TOOL_CRAMPONS_6
        )

        # 10 point crampons require at least 3 advanced peaks
        # AND 22 base game peaks in total, so access should be
        # locked behind advanced
        self.__create_data(
            BaseLocationName.TOOL_CRAMPONS_10,
            AdvancedRegionName.CATEGORY,
            BaseItemName.TOOL_CRAMPONS_10
        )

        # Ice axes are locked behind 3 advanced OR ymir's shadow
        self.__create_data(
            BaseLocationName.TOOL_ICE_AXES,
            AdvancedRegionName.CATEGORY,
            BaseItemName.TOOL_ICE_AXES
        )

        # Monocular locked behind three brothers
        self.__create_data(
            BaseLocationName.TOOL_MONOCULAR,
            FundamentalsRegionName.THREE_BROTHERS,
            BaseItemName.TOOL_MONOCULAR
        )

        # Phonograph is locked behind either completing
        # paltry peak OR completing at least 2 fundamentals
        self.__create_data(
            BaseLocationName.TOOL_PHONOGRAPH,
            FundamentalsRegionName.CATEGORY,
            BaseItemName.TOOL_PHONOGRAPH
        )

        # Need to beat all intermediate time trials
        # for the pipe
        self.__create_data(
            BaseLocationName.TOOL_PIPE,
            IntermediateRegionName.CATEGORY,
            BaseItemName.TOOL_PIPE
        )

        # Pocketwatch is given after completing at least 2
        # intermediate peaks
        self.__create_data(
            BaseLocationName.TOOL_POCKETWATCH
            IntermediateRegionName.CATEGORY,
            BaseItemName.TOOL_POCKETWATCH
        )

        # Rope is given after gray gully, or completing
        # at least 3 fundamentals
        self.__create_data(
            BaseLocationName.TOOL_ROPE,
            FundamentalsRegionName.CATEGORY,
            BaseItemName.TOOL_ROPE
        )

        # Double length rope is given after
        # collecting all picture pieces
        # The last picture pieces are on advanced peaks
        self.__create_data(
            BaseLocationName.TOOL_ROPE_DOUBLE,
            AdvancedRegionName.CATEGORY,
            BaseItemName.TOOL_ROPE_DOUBLE
        )

        ## DLC
        # Gentiana
        self.__create_data(
            DlcLocationName.GENTIANA_MARAS_ARCH,
            EssentialsRegionName.MARAS_ARCH,
            DlcItemName.GENTIANA
        )
        self.__create_data(
            DlcLocationName.GENTIANA_TREPPENWALD,
            EssentialsRegionName.TREPPENWALD,
            DlcItemName.GENTIANA
        )
        self.__create_data(
            DlcLocationName.GENTIANA_QUIETUDE,
            EssentialsRegionName.QUIETUDE,
            DlcItemName.GENTIANA
        )
        self.__create_data(
            DlcLocationName.GENTIANA_ELJUNS_FOLLY,
            EssentialsRegionName.ELJUNS_FOLLY,
            DlcItemName.GENTIANA
        )
        self.__create_data(
            DlcLocationName.GENTIANA_EINVALD_FALLS,
            GreatsRegionName.EINVALD_FALLS,
            DlcItemName.GENTIANA
        )
        self.__create_data(
            DlcLocationName.GENTIANA_MHOR_DRUIM,
            GreatsRegionName.MHOR_DRUIM,
            DlcItemName.GENTIANA
        )
        self.__create_data(
            DlcLocationName.GENTIANA_TOWERING_VISIR,
            ArcticRegionName.TOWERING_VISIR,
            DlcItemName.GENTIANA
        )

        # Edelweiss
        self.__create_data(
            DlcLocationName.EDELWEISS_GREAT_BOK_TREE,
            EssentialsRegionName.GREAT_BOK_TREE,
            DlcItemName.EDELWEISS
        )
        self.__create_data(
            DlcLocationName.EDELWEISS_CASTLE_OF_THE_SWAN_KING,
            EssentialsRegionName.CASTLE_OF_THE_SWAN_KING,
            DlcItemName.EDELWEISS
        )
        self.__create_data(
            DlcLocationName.EDELWEISS_IVORY_GRANITES,
            EssentialsRegionName.IVORY_GRANITES,
            DlcItemName.EDELWEISS
        )
        self.__create_data(
            DlcLocationName.EDELWEISS_DUNDERHORN,
            GreatsRegionName.DUNDERHORN,
            DlcItemName.EDELWEISS
        )
        self.__create_data(
            DlcLocationName.EDELWEISS_WELKIN_PASS,
            GreatsRegionName.WELKIN_PASS,
            DlcItemName.EDELWEISS
        )
        self.__create_data(
            DlcLocationName.EDELWEISS_TOWERING_VISIR,
            ArcticRegionName.TOWERING_VISIR,
            DlcItemName.EDELWEISS
        )
        self.__create_data(
            DlcLocationName.EDELWEISS_ELDRIS_WALL,
            ArcticRegionName.ELDRIS_WALL,
            DlcItemName.EDELWEISS
        )

        # Idols
        self.__create_data(
            DlcLocationName.IDOL_OF_CRIMPS_1,
            EssentialsRegionName.GRAINNE_SPIRE,
            DlcItemName.IDOL_OF_CRIMPS_1
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_CRIMPS_2,
            EssentialsRegionName.GREAT_BOK_TREE,
            DlcItemName.IDOL_OF_CRIMPS_2
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_CRUELTY_1,
            EssentialsRegionName.IVORY_GRANITES,
            DlcItemName.IDOL_OF_CRUELTY_1
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_CRUELTY_2,
            ArcticRegionName.MOUNT_MHORGORM,
            DlcItemName.IDOL_OF_CRUELTY_2
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_FEATHERS_1,
            GreatsRegionName.MHOR_DRUIM,
            DlcItemName.IDOL_OF_FEATHERS_1
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_FEATHERS_2,
            GreatsRegionName.WELKIN_PASS,
            DlcItemName.IDOL_OF_FEATHERS_2
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_GREATER_BALANCE_1,
            ArcticRegionName.ULLRS_CHASM,
            DlcItemName.IDOL_OF_GREATER_BALANCE_1
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_GREATER_BALANCE_2,
            ArcticRegionName.TOWERING_VISIR,
            DlcItemName.IDOL_OF_GREATER_BALANCE_2
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_ICE_1,
            GreatsRegionName.MHOR_DRUIM,
            DlcItemName.IDOL_OF_ICE_1
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_ICE_2,
            ArcticRegionName.ELDRIS_WALL,
            DlcItemName.IDOL_OF_ICE_2
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_PINCHES_1,
            EssentialsRegionName.SEASIDE_TRIBUNE,
            DlcItemName.IDOL_OF_PINCHES_1
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_PINCHES_2,
            ArcticRegionName.TOWERING_VISIR,
            DlcItemName.IDOL_OF_PINCHES_2
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_PITCHES_1,
            EssentialsRegionName.CASTLE_OF_THE_SWAN_KING,
            DlcItemName.IDOL_OF_PITCHES_1
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_PITCHES_2,
            EssentialsRegionName.ELJUNS_FOLLY,
            DlcItemName.IDOL_OF_PITCHES_2
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_SLOPERS_1,
            EssentialsRegionName.CASTLE_OF_THE_SWAN_KING,
            DlcItemName.IDOL_OF_SLOPERS_1
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_SLOPERS_2,
            EssentialsRegionName.OLD_REKKJA,
            DlcItemName.IDOL_OF_SLOPERS_2
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_SUNDOWN_1,
            EssentialsRegionName.CASTLE_OF_THE_SWAN_KING,
            DlcItemName.IDOL_OF_SUNDOWN_1
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_SUNDOWN_2,
            GreatsRegionName.DUNDERHORN,
            DlcItemName.IDOL_OF_SUNDOWN_2
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_SEEDS_1,
            EssentialsRegionName.TREPPENWALD,
            DlcItemName.IDOL_OF_SEEDS_1
        )
        self.__create_data(
            DlcLocationName.IDOL_OF_SEEDS_2,
            ArcticRegionName.ELDRIS_WALL,
            DlcItemName.IDOL_OF_SEEDS_2
        )

        # Tickets
        # The northern range ticket is accessible after
        # beating 3 advanced peaks or ymir's shadow
        self.__create_data(
            PoYLocationData.TICKET_NORTHERN_RANGE,
            AdvancedRegionName.CATEGORY,
            BaseItemName.TICKET_NORTHERN_RANGE
        )

        # Books
        # Fundamentals always accessible from the cabin
        self.__create_data(
            BaseLocationName.BOOK_FUNDAMENTALS,
            CabinRegionName.GALES,
            BaseItemName.BOOK_FUNDAMENTALS
        )

        # Intermediate book requires fundamentals access
        self.__create_data(
            BaseLocationName.BOOK_INTERMEDIATE,
            FundamentalsRegionName.CATEGORY,
            BaseItemName.BOOK_INTERMEDIATE
        )

        # Advanced book requires intermediate access
        self.__create_data(
            BaseLocationName.BOOK_ADVANCED,
            IntermediateRegionName.CATEGORY,
            BaseItemName.BOOK_ADVANCED
        )

        # Expert book requires advanced access
        self.__create_data(
            BaseLocationName.BOOK_NORTHERN_EXPERT,
            AdvancedRegionName.CATEGORY,
            BaseItemName.BOOK_NORTHERN_EXPERT
        )

        # DLC books
        # Essentials is unlocked as soon as you get
        # access to the Alps cabin (always have access normally anyway)
        self.__create_data(
            DlcLocationName.BOOK_ALPS_ESSENTIALS,
            CabinRegionName.ALPS,
            DlcItemName.BOOK_ALPS_ESSENTIALS
        )

        # Alpine greats requires access to the essentials
        self.__create_data(
            DlcLocationName.BOOK_ALPS_GREATS,
            EssentialsRegionName.CATEGORY,
            DlcItemName.BOOK_ALPS_GREATS
        )

        # Arduous and arctic requires access to the alpine greats
        self.__create_data(
            DlcLocationName.BOOK_ALPS_ARCTIC,
            GreatsRegionName.CATEGORY,
            DlcItemName.BOOK_ALPS_ARCTIC
        )

        # Create stamp locations for all peaks in each category
        self.__create_stamps(FundamentalsRegionName, BaseItemName.STAMP_FUNDAMENTALS)
        self.__create_stamps(IntermediateRegionName, BaseItemName.STAMP_INTERMEDIATE)
        self.__create_stamps(AdvancedRegionName,     BaseItemName.STAMP_ADVANCED)
        self.__create_stamps(ExpertRegionName,       BaseItemName.STAMP_NORTHERN_EXPERT)
        self.__create_stamps(EssentialsRegionName,   DlcItemName.STAMP_ALPS_ESSENTIALS)
        self.__create_stamps(GreatsRegionName,       DlcItemName.STAMP_ALPS_GREATS)
        self.__create_stamps(ArcticRegionName,       DlcItemName.STAMP_ALPS_ARCTIC)
