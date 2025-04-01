from enum import StrEnum

from .id_handler import IDHandler
from .items import PoYItemName
from .regions import PoYRegionName

class PoYLocationName(StrEnum):
    ## Base game
    # Artefacts
    HAT_OLD_MILL                      = "Hat (Old Mill)"
    HAT_EVERGREENS_END                = "Hat (Evergreen's End)"
    SHOE_OLD_MAN_OF_SJOR              = "Shoe (Old Man of Sjór)"
    SLEEPING_BAG_GIANTS_SHELF         = "Sleeping Bag (Giant's Shelf)"
    SAFETY_HELMET_OLD_GROVES_SKELF    = "Safety Helmet (Old Grove's Skelf)"
    BACKPACK_ALDR_GROTTO              = "Backpack (Aldr Grotto)"
    SHOVEL_THREE_BROTHERS             = "Shovel (Three Brothers)"

    PICTURE_GRAY_GULLY                = "Picture Fragment (Gray Gully)"
    PICTURE_LANDS_END                 = "Picture Fragment (Land's End)"
    PICTURE_THE_GREAT_CREVICE         = "Picture Fragment (The Great Crevice)"
    PICTURE_ST_HAELGA                 = "Picture Fragment (St. Haelga)"
    PICTURE_FRAME_GREAT_GAOL          = "Picture Frame (Great Gaol)"

    STATUE_FUNDAMENTALS_WALTERS_CRAG  = "Fundamental Statue (Walter's Crag)"
    STATUE_INTERMEDIATE_LEANING_SPIRE = "Intermediate Statue (Leaning Spire)"
    STATUE_ADVANCED_YMIRS_SHADOW      = "Advanced Statue (Ymir's Shadow)"
    STATUE_EXPERT_BULWARK             = "Expert Statue (Great Bulwark)"

    # Bird seeds
    BIRD_SEEDS_THREE_BROTHERS         = "Bird Seeds (Three Brothers)"
    BIRD_SEEDS_OLD_SKERRY             = "Bird Seeds (Old Skerry)"
    BIRD_SEEDS_GREAT_GAOL             = "Bird Seeds (Great Gaol)"
    BIRD_SEEDS_ELDENHORN              = "Bird Seeds (Eldenhorn)"
    BIRD_SEEDS_YMIRS_SHADOW           = "Bird Seeds (Ymir's Shadow)"

    # Chalk
    CHALK_WALKERS_PILLAR              = "Chalk Box (Walker's Pillar)"
    CHALK_ELDENHORN                   = "Chalk Box (Eldenhorn)"

    # Coffee
    COFFEE_OLD_LANGR                  = "Coffee Box (Old Langr)"
    COFFEE_WUTHERING_CREST            = "Coffee Box (Wuthering Crest)"

    # Ropes
    ROPE_OLD_MAN_OF_SJOR              = "Rope (Old Man of Sjór)"
    ROPE_EVERGREENS_END               = "Rope (Evergreen's End)"
    ROPE_HANGMANS_LEAP                = "Rope (Hangman's Leap)"
    ROPE_LANDS_END                    = "Rope (Land's End)"
    ROPE_WALTERS_CRAG                 = "Rope (Walter's Crag)"
    ROPE_THE_GREAT_CREVICE            = "Rope (The Great Crevice)"
    ROPE_OLD_HAGGER                   = "Rope (Old Hagger)"
    ROPE_UGSOME_STORR                 = "Rope (Ugsome Stórr)"
    ROPE_WUTHERING_CREST              = "Rope (Wuthering Crest)"
    ROPE_GREAT_GAOL                   = "Rope (Great Gaol)"
    ROPE_ELDENHORN                    = "Rope (Eldenhorn)"
    ROPE_YMIRS_SHADOW                 = "Rope (Ymir's Shadow)"

    # NPC interactions
    NPC_COFFEE_THE_TWINS              = "Coffee Box (The Twins Interaction)"
    NPC_COFFEE_GIANTS_NOSE            = "Coffee Box (Giant's Nose Interaction)"
    NPC_ROPE_WALTERS_CRAG             = "Rope (Walter's Crag Co-Climb)"
    NPC_ROPE_WALKERS_PILLAR           = "Rope (Walker's Pillar Co-Climb)"
    NPC_ROPE_GREAT_GAOL               = "Rope (Great Gaol Interaction)"
    NPC_ROPE_ST_HAELGA                = "Rope (St. Haelga Interaction)"

    # Tools
    TOOL_ARTEFACT_MAP                 = PoYItemName.TOOL_ARTEFACT_MAP
    TOOL_BAROMETER                    = PoYItemName.TOOL_BAROMETER
    TOOL_CHALK_BAG                    = PoYItemName.TOOL_CHALK_BAG
    TOOL_COFFEE                       = PoYItemName.TOOL_COFFEE
    TOOL_CRAMPONS_6                   = PoYItemName.TOOL_CRAMPONS_6
    TOOL_CRAMPONS_10                  = PoYItemName.TOOL_CRAMPONS_10
    TOOL_ICE_AXES                     = PoYItemName.TOOL_ICE_AXES
    TOOL_MONOCULAR                    = PoYItemName.TOOL_MONOCULAR
    TOOL_PHONOGRAPH                   = PoYItemName.TOOL_PHONOGRAPH
    TOOL_PIPE                         = PoYItemName.TOOL_PIPE
    TOOL_POCKETWATCH                  = PoYItemName.TOOL_POCKETWATCH
    TOOL_ROPE                         = PoYItemName.TOOL_ROPE
    TOOL_ROPE_DOUBLE                  = PoYItemName.TOOL_ROPE_DOUBLE

    ## DLC
    # Gentiana
    GENTIANA_MARAS_ARCH               = "Gentiana (Mara's Arch)"
    GENTIANA_TREPPENWALD              = "Gentiana (Treppenwald)"
    GENTIANA_QUIETUDE                 = "Gentiana (Quietude)"
    GENTIANA_ELJUNS_FOLLY             = "Gentiana (Eljun's Folly)"
    GENTIANA_EINVALD_FALLS            = "Gentiana (Einvald Falls)"
    GENTIANA_MHOR_DRUIM               = "Gentiana (Mhòr Druim)"
    GENTIANA_TOWERING_VISIR           = "Gentiana (Towering Vísir)"

    # Edelweiss
    EDELWEISS_GREAT_BOK_TREE          = "Edelweiss (Great Bók Tree)"
    EDELWEISS_CASTLE_OF_THE_SWAN_KING = "Edelweiss (Castle of the Swan King)"
    EDELWEISS_IVORY_GRANITES          = "Edelweiss (Ivory Granites)"
    EDELWEISS_DUNDERHORN              = "Edelweiss (Dunderhorn)"
    EDELWEISS_WELKIN_PASS             = "Edelweiss (Welkin Pass)"
    EDELWEISS_TOWERING_VISIR          = "Edelweiss (Towering Vísir)"
    EDELWEISS_ELDRIS_WALL             = "Edelweiss (Eldris Wall)"

    # Idols
    IDOL_OF_CRIMPS_1                  = "Idol of Crimps #1 (Grainne Spire)"
    IDOL_OF_CRIMPS_2                  = "Idol of Crimps #2 (Great Bók Tree) "
    IDOL_OF_CRUELTY_1                 = "Idol of Cruelty #1 (Ivory Granites)"
    IDOL_OF_CRUELTY_2                 = "Idol of Cruelty #2 (Mount Mhòrgorm)"
    IDOL_OF_FEATHERS_1                = "Idol of Feathers #1 (Mhòr Druim)"
    IDOL_OF_FEATHERS_2                = "Idol of Feathers #2 (Welkin Pass)"
    IDOL_OF_GREATER_BALANCE_1         = "Idol of Greater Balance #1 (Ullr's Chasm)"
    IDOL_OF_GREATER_BALANCE_2         = "Idol of Greater Balance #2 (Towering Vísir)"
    IDOL_OF_ICE_1                     = "Idol of Ice #1 (Mhòr Druim)"
    IDOL_OF_ICE_2                     = "Idol of Ice #2 (Eldris Wall)"
    IDOL_OF_PINCHES_1                 = "Idol of Pinches #1 (Seaside Tribune)"
    IDOL_OF_PINCHES_2                 = "Idol of Pinches #2 (Towering Vísir)"
    IDOL_OF_PITCHES_1                 = "Idol of Pitches #1 (Castle of the Swan King)"
    IDOL_OF_PITCHES_2                 = "Idol of Pitches #2 (Eljun's Folly)"
    IDOL_OF_SLOPERS_1                 = "Idol of Slopers #1 (Castle of the Swan King)"
    IDOL_OF_SLOPERS_2                 = "Idol of Slopers #2 (Old Rekkja)"
    IDOL_OF_SUNDOWN_1                 = "Idol of Sundown #1 (Castle of the Swan King)"
    IDOL_OF_SUNDOWN_2                 = "Idol of Sundown #2 (Dunderhorn)"
    IDOL_OF_SEEDS_1                   = "Idol of Seeds #1 (Treppenwald)"
    IDOL_OF_SEEDS_2                   = "Idol of Seeds #2 (Eldris Wall)"


base_locations = [
    HAT_OLD_MILL,
    HAT_EVERGREENS_END,
    SHOE_OLD_MAN_OF_SJOR,
    SLEEPING_BAG_GIANTS_SHELF,
    SAFETY_HELMET_OLD_GROVES_SKELF,
    BACKPACK_ALDR_GROTTO,
    SHOVEL_THREE_BROTHERS,
    PICTURE_GRAY_GULLY,
    PICTURE_LANDS_END,
    PICTURE_THE_GREAT_CREVICE,
    PICTURE_ST_HAELGA,
    PICTURE_FRAME_GREAT_GAOL,
    STATUE_FUNDAMENTALS_WALTERS_CRAG,
    STATUE_INTERMEDIATE_LEANING_SPIRE,
    STATUE_ADVANCED_YMIRS_SHADOW,
    STATUE_EXPERT_BULWARK,
    BIRD_SEEDS_THREE_BROTHERS,
    BIRD_SEEDS_OLD_SKERRY,
    BIRD_SEEDS_GREAT_GAOL,
    BIRD_SEEDS_ELDENHORN,
    BIRD_SEEDS_YMIRS_SHADOW,
    CHALK_WALKERS_PILLAR,
    CHALK_ELDENHORN,
    COFFEE_OLD_LANGR,
    COFFEE_WUTHERING_CREST,
    ROPE_OLD_MAN_OF_SJOR,
    ROPE_EVERGREENS_END,
    ROPE_HANGMANS_LEAP,
    ROPE_LANDS_END,
    ROPE_WALTERS_CRAG,
    ROPE_THE_GREAT_CREVICE,
    ROPE_OLD_HAGGER,
    ROPE_UGSOME_STORR,
    ROPE_WUTHERING_CREST,
    ROPE_GREAT_GAOL,
    ROPE_ELDENHORN,
    ROPE_YMIRS_SHADOW,
    NPC_COFFEE_THE_TWINS,
    NPC_COFFEE_GIANTS_NOSE,
    NPC_ROPE_WALTERS_CRAG,
    NPC_ROPE_WALKERS_PILLAR,
    NPC_ROPE_GREAT_GAOL,
    NPC_ROPE_ST_HAELGA,
    TOOL_ARTEFACT_MAP,
    TOOL_BAROMETER,
    TOOL_CHALK_BAG,
    TOOL_COFFEE,
    TOOL_CRAMPONS_6,
    TOOL_CRAMPONS_10,
    TOOL_ICE_AXES,
    TOOL_MONOCULAR,
    TOOL_PHONOGRAPH,
    TOOL_PIPE,
    TOOL_POCKETWATCH,
    TOOL_ROPE,
    TOOL_ROPE_DOUBLE,
]

dlc_locations = [
    GENTIANA_MARAS_ARCH,
    GENTIANA_TREPPENWALD,
    GENTIANA_QUIETUDE,
    GENTIANA_ELJUNS_FOLLY,
    GENTIANA_EINVALD_FALLS,
    GENTIANA_MHOR_DRUIM,
    GENTIANA_TOWERING_VISIR,
    EDELWEISS_GREAT_BOK_TREE,
    EDELWEISS_CASTLE_OF_THE_SWAN_KING,
    EDELWEISS_IVORY_GRANITES,
    EDELWEISS_DUNDERHORN,
    EDELWEISS_WELKIN_PASS,
    EDELWEISS_TOWERING_VISIR,
    EDELWEISS_ELDRIS_WALL,
    IDOL_OF_CRIMPS_1,
    IDOL_OF_CRIMPS_2,
    IDOL_OF_CRUELTY_1,
    IDOL_OF_CRUELTY_2,
    IDOL_OF_FEATHERS_1,
    IDOL_OF_FEATHERS_2,
    IDOL_OF_GREATER_BALANCE_1,
    IDOL_OF_GREATER_BALANCE_2,
    IDOL_OF_ICE_1,
    IDOL_OF_ICE_2,
    IDOL_OF_PINCHES_1,
    IDOL_OF_PINCHES_2,
    IDOL_OF_PITCHES_1,
    IDOL_OF_PITCHES_2,
    IDOL_OF_SLOPERS_1,
    IDOL_OF_SLOPERS_2,
    IDOL_OF_SUNDOWN_1,
    IDOL_OF_SUNDOWN_2,
    IDOL_OF_SEEDS_1,
    IDOL_OF_SEEDS_2,
]

class PoYLocationData:
    id: int
    name: PoYLocationName
    item_name: PoYItemName

    def __init__(
        self,
        id: int,
        name: PoYLocationName,
        item_name: PoYItemName
    ) -> None:
        """
        Initializes a PoYLocationData object.

        :param id: The ID of this location
        :param name: The name of this location
        :param item_name: The item locked behind this location (or dropped by it)
        """

        self.id = id
        self.name = name
        self.item_name = item_name


class PoYLocations:
    handler: IDHandler

    locations: dict[PoYRegionName, PoYLocationData]

    def __init__(self, handler: IDHandler) -> None:
        """
        Initializes a PoYLocations object.

        :param handler: The handler to assign IDs with
        """

        self.handler = handler

        ## Base game
        # Artefacts
        self.create_location(
            PoYLocationName.HAT_OLD_MILL,
            PoYRegionName.GALES_OLD_MILL,
            PoYItemName.HAT_1
        )
        self.create_location(
            PoYLocationName.HAT_EVERGREENS_END,
            PoYRegionName.GALES_EVERGREENS_END,
            PoYItemName.HAT_2
        )
        self.create_location(
            PoYLocationName.SHOE_OLD_MAN_OF_SJOR,
            PoYRegionName.GALES_OLD_MAN_OF_SJOR,
            PoYItemName.SHOE
        )
        self.create_location(
            PoYLocationName.SLEEPING_BAG_GIANTS_SHELF,
            PoYRegionName.GALES_GIANTS_SHELF,
            PoYItemName.SLEEPING_BAG
        )
        self.create_location(
            PoYLocationName.SAFETY_HELMET_OLD_GROVES_SKELF,
            PoYRegionName.GALES_OLD_GROVES_SKELF,
            PoYItemName.SAFETY_HELMET
        )
        self.create_location(
            PoYLocationName.BACKPACK_ALDR_GROTTO,
            PoYRegionName.GALES_ALDR_GROTTO,
            PoYItemName.BACKPACK
        )
        self.create_location(
            PoYLocationName.SHOVEL_THREE_BROTHERS,
            PoYRegionName.GALES_THREE_BROTHERS,
            PoYItemName.SHOVEL
        )
        self.create_location(
            PoYLocationName.PICTURE_GRAY_GULLY,
            PoYRegionName.GALES_GRAY_GULLY,
            PoYItemName.PICTURE_FRAGMENT
        )
        self.create_location(
            PoYLocationName.PICTURE_LANDS_END,
            PoYRegionName.GALES_LANDS_END,
            PoYItemName.PICTURE_FRAGMENT
        )
        self.create_location(
            PoYLocationName.PICTURE_THE_GREAT_CREVICE,
            PoYRegionName.GALES_THE_GREAT_CREVICE,
            PoYItemName.PICTURE_FRAGMENT
        )
        self.create_location(
            PoYLocationName.PICTURE_ST_HAELGA,
            PoYRegionName.GALES_ST_HAELGA,
            PoYItemName.PICTURE_FRAGMENT
        )
        self.create_location(
            PoYLocationName.PICTURE_FRAME_GREAT_GAOL,
            PoYRegionName.GALES_GREAT_GAOL,
            PoYItemName.PICTURE_FRAME
        )
        self.create_location(
            PoYLocationName.STATUE_FUNDAMENTALS_WALTERS_CRAG,
            PoYRegionName.GALES_WALTERS_CRAG,
            PoYItemName.STATUE_FUNDAMENTALS
        )
        self.create_location(
            PoYLocationName.STATUE_INTERMEDIATE_LEANING_SPIRE,
            PoYRegionName.GALES_LEANING_SPIRE,
            PoYItemName.STATUE_INTERMEDIATE
        )
        self.create_location(
            PoYLocationName.STATUE_ADVANCED_YMIRS_SHADOW,
            PoYRegionName.GALES_YMIRS_SHADOW,
            PoYItemName.STATUE_ADVANCED
        )
        self.create_location(
            PoYLocationName.STATUE_EXPERT_BULWARK,
            PoYRegionName.NORTHERN_GREAT_BULWARK,
            PoYItemName.STATUE_EXPERT
        )

        # Bird seeds
        self.create_location(
            PoYLocationName.BIRD_SEEDS_THREE_BROTHERS,
            PoYRegionName.GALES_THREE_BROTHERS,
            PoYItemName.BIRD_SEEDS
        )
        self.create_location(
            PoYLocationName.BIRD_SEEDS_OLD_SKERRY,
            PoYRegionName.GALES_OLD_SKERRY,
            PoYItemName.BIRD_SEEDS
        )
        self.create_location(
            PoYLocationName.BIRD_SEEDS_GREAT_GAOL,
            PoYRegionName.GALES_GREAT_GAOL,
            PoYItemName.BIRD_SEEDS
        )
        self.create_location(
            PoYLocationName.BIRD_SEEDS_ELDENHORN,
            PoYRegionName.GALES_ELDENHORN,
            PoYItemName.BIRD_SEEDS
        )
        self.create_location(
            PoYLocationName.BIRD_SEEDS_YMIRS_SHADOW,
            PoYRegionName.GALES_YMIRS_SHADOW,
            PoYItemName.BIRD_SEEDS
        )

        # Chalk
        self.create_location(
            PoYLocationName.CHALK_WALKERS_PILLAR,
            PoYRegionName.GALES_WALKERS_PILLAR,
            PoYItemName.CHALK
        )
        self.create_location(
            PoYLocationName.CHALK_ELDENHORN,
            PoYRegionName.GALES_ELDENHORN,
            PoYItemName.CHALK
        )

        # Coffee
        self.create_location(
            PoYLocationName.COFFEE_OLD_LANGR,
            PoYRegionName.GALES_OLD_LANGR,
            PoYItemName.COFFEE_2
        )
        self.create_location(
            PoYLocationName.COFFEE_WUTHERING_CREST,
            PoYRegionName.GALES_WUTHERING_CREST,
            PoYItemName.COFFEE_2
        )

        # Rope
        self.create_location(
            PoYLocationName.ROPE_OLD_MAN_OF_SJOR,
            PoYRegionName.GALES_OLD_MAN_OF_SJOR,
            PoYItemName.ROPES_2
        )
        self.create_location(
            PoYLocationName.ROPE_EVERGREENS_END,
            PoYRegionName.GALES_EVERGREENS_END,
            PoYItemName.ROPES_2
        )
        self.create_location(
            PoYLocationName.ROPE_HANGMANS_LEAP,
            PoYRegionName.GALES_HANGMANS_LEAP,
            PoYItemName.ROPES_2
        )
        self.create_location(
            PoYLocationName.ROPE_LANDS_END,
            PoYRegionName.GALES_LANDS_END,
            PoYItemName.ROPES_2
        )
        self.create_location(
            PoYLocationName.ROPE_WALTERS_CRAG,
            PoYRegionName.GALES_WALTERS_CRAG,
            PoYItemName.ROPES_2
        )
        self.create_location(
            PoYLocationName.ROPE_THE_GREAT_CREVICE,
            PoYRegionName.GALES_THE_GREAT_CREVICE,
            PoYItemName.ROPES_2
        )
        self.create_location(
            PoYLocationName.ROPE_OLD_HAGGER,
            PoYRegionName.GALES_OLD_HAGGER,
            PoYItemName.ROPES_2
        )
        self.create_location(
            PoYLocationName.ROPE_UGSOME_STORR,
            PoYRegionName.GALES_UGSOME_STORR,
            PoYItemName.ROPES_2
        )
        self.create_location(
            PoYLocationName.ROPE_WUTHERING_CREST,
            PoYRegionName.GALES_WUTHERING_CREST,
            PoYItemName.ROPES_2
        )
        self.create_location(
            PoYLocationName.ROPE_GREAT_GAOL,
            PoYRegionName.GALES_GREAT_GAOL,
            PoYItemName.ROPES_2
        )
        self.create_location(
            PoYLocationName.ROPE_ELDENHORN,
            PoYRegionName.GALES_ELDENHORN,
            PoYItemName.ROPES_2
        )
        self.create_location(
            PoYLocationName.ROPE_YMIRS_SHADOW,
            PoYRegionName.GALES_YMIRS_SHADOW,
            PoYItemName.ROPES_2
        )

        # NPC events
        self.create_location(
            PoYLocationName.NPC_COFFEE_THE_TWINS,
            PoYRegionName.GALES_THE_TWINS,
            PoYItemName.COFFEE_5
        )
        self.create_location(
            PoYLocationName.NPC_COFFEE_GIANTS_NOSE,
            PoYRegionName.GALES_GIANTS_NOSE,
            PoYItemName.COFFEE_5
        )
        self.create_location(
            PoYLocationName.NPC_ROPE_WALTERS_CRAG,
            PoYRegionName.GALES_WALTERS_CRAG,
            PoYItemName.ROPES_1
        )
        self.create_location(
            PoYLocationName.NPC_ROPE_WALKERS_PILLAR,
            PoYRegionName.GALES_WALKERS_PILLAR,
            PoYItemName.ROPES_1
        )
        self.create_location(
            PoYLocationName.NPC_ROPE_GREAT_GAOL,
            PoYRegionName.GALES_GREAT_GAOL,
            PoYItemName.ROPES_1
        )
        self.create_location(
            PoYLocationName.NPC_ROPE_ST_HAELGA,
            PoYRegionName.GALES_ST_HAELGA,
            PoYItemName.ROPES_1
        )

        # Tools
        self.create_location(
            PoYLocationName.TOOL_ARTEFACT_MAP,
            PoYRegionName.GALES_CABIN,
            PoYItemName.TOOL_ARTEFACT_MAP
        )
        self.create_location(
            PoYLocationName.TOOL_BAROMETER,
            PoYRegionName.GALES_CABIN,
            PoYItemName.TOOL_BAROMETER
        )
        self.create_location(
            PoYLocationName.TOOL_CHALK_BAG,
            PoYRegionName.GALES_CABIN,
            PoYItemName.TOOL_CHALK_BAG
        )
        self.create_location(
            PoYLocationName.TOOL_COFFEE,
            PoYRegionName.GALES_THE_TWINS,
            PoYItemName.TOOL_COFFEE
        )
        self.create_location(
            PoYLocationName.TOOL_CRAMPONS_6,
            PoYRegionName.GALES_CABIN,
            PoYItemName.TOOL_CRAMPONS_6
        )
        self.create_location(
            PoYLocationName.TOOL_CRAMPONS_10,
            PoYRegionName.GALES_CABIN,
            PoYItemName.TOOL_CRAMPONS_10
        )
        self.create_location(
            PoYLocationName.TOOL_ICE_AXES,
            PoYRegionName.GALES_CABIN,
            PoYItemName.TOOL_ICE_AXES
        )
        self.create_location(
            PoYLocationName.TOOL_MONOCULAR,
            PoYRegionName.GALES_THREE_BROTHERS,
            PoYItemName.TOOL_MONOCULAR
        )
        self.create_location(
            PoYLocationName.TOOL_PHONOGRAPH,
            PoYRegionName.GALES_CABIN,
            PoYItemName.TOOL_PHONOGRAPH
        )
        self.create_location(
            PoYLocationName.TOOL_PIPE,
            PoYRegionName.GALES_CABIN,
            PoYItemName.TOOL_PIPE
        )
        self.create_location(
            PoYLocationName.TOOL_POCKETWATCH
            PoYRegionName.GALES_CABIN,
            PoYItemName.TOOL_POCKETWATCH
        )
        self.create_location(
            PoYLocationName.TOOL_ROPE,
            PoYRegionName.GALES_CABIN,
            PoYItemName.TOOL_ROPE
        )
        self.create_location(
            PoYLocationName.TOOL_ROPE_DOUBLE,
            PoYRegionName.GALES_CABIN,
            PoYItemName.TOOL_ROPE_DOUBLE
        )

        ## DLC
        # Gentiana
        self.create_location(
            PoYLocationName.GENTIANA_MARAS_ARCH,
            PoYRegionName.ALPS_MARAS_ARCH,
            PoYItemName.GENTIANA
        )
        self.create_location(
            PoYLocationName.GENTIANA_TREPPENWALD,
            PoYRegionName.ALPS_TREPPENWALD,
            PoYItemName.GENTIANA
        )
        self.create_location(
            PoYLocationName.GENTIANA_QUIETUDE,
            PoYRegionName.ALPS_QUIETUDE,
            PoYItemName.GENTIANA
        )
        self.create_location(
            PoYLocationName.GENTIANA_ELJUNS_FOLLY,
            PoYRegionName.ALPS_ELJUNS_FOLLY,
            PoYItemName.GENTIANA
        )
        self.create_location(
            PoYLocationName.GENTIANA_EINVALD_FALLS,
            PoYRegionName.ALPS_EINVALD_FALLS,
            PoYItemName.GENTIANA
        )
        self.create_location(
            PoYLocationName.GENTIANA_MHOR_DRUIM,
            PoYRegionName.ALPS_MHOR_DRUIM,
            PoYItemName.GENTIANA
        )
        self.create_location(
            PoYLocationName.GENTIANA_TOWERING_VISIR,
            PoYRegionName.ALPS_TOWERING_VISIR,
            PoYItemName.GENTIANA
        )

        # Edelweiss
        self.create_location(
            PoYLocationName.EDELWEISS_GREAT_BOK_TREE,
            PoYRegionName.ALPS_GREAT_BOK_TREE,
            PoYItemName.EDELWEISS
        )
        self.create_location(
            PoYLocationName.EDELWEISS_CASTLE_OF_THE_SWAN_KING,
            PoYRegionName.ALPS_CASTLE_OF_THE_SWAN_KING,
            PoYItemName.EDELWEISS
        )
        self.create_location(
            PoYLocationName.EDELWEISS_IVORY_GRANITES,
            PoYRegionName.ALPS_IVORY_GRANITES,
            PoYItemName.EDELWEISS
        )
        self.create_location(
            PoYLocationName.EDELWEISS_DUNDERHORN,
            PoYRegionName.ALPS_DUNDERHORN,
            PoYItemName.EDELWEISS
        )
        self.create_location(
            PoYLocationName.EDELWEISS_WELKIN_PASS,
            PoYRegionName.ALPS_WELKIN_PASS,
            PoYItemName.EDELWEISS
        )
        self.create_location(
            PoYLocationName.EDELWEISS_TOWERING_VISIR,
            PoYRegionName.ALPS_TOWERING_VISIR,
            PoYItemName.EDELWEISS
        )
        self.create_location(
            PoYLocationName.EDELWEISS_ELDRIS_WALL,
            PoYRegionName.ALPS_ELDRIS_WALL,
            PoYItemName.EDELWEISS
        )

        # Idols
        self.create_location(
            PoYLocationName.IDOL_OF_CRIMPS_1,
            PoYRegionName.ALPS_GRAINNE_SPIRE,
            PoYItemName.IDOL_OF_CRIMPS_1
        )
        self.create_location(
            PoYLocationName.IDOL_OF_CRIMPS_2,
            PoYRegionName.ALPS_GREAT_BOK_TREE,
            PoYItemName.IDOL_OF_CRIMPS_2
        )
        self.create_location(
            PoYLocationName.IDOL_OF_CRUELTY_1,
            PoYRegionName.ALPS_IVORY_GRANITES,
            PoYItemName.IDOL_OF_CRUELTY_1
        )
        self.create_location(
            PoYLocationName.IDOL_OF_CRUELTY_2,
            PoYRegionName.ALPS_MOUNT_MHORGORM,
            PoYItemName.IDOL_OF_CRUELTY_2
        )
        self.create_location(
            PoYLocationName.IDOL_OF_FEATHERS_1,
            PoYRegionName.ALPS_MHOR_DRUIM,
            PoYItemName.IDOL_OF_FEATHERS_1
        )
        self.create_location(
            PoYLocationName.IDOL_OF_FEATHERS_2,
            PoYRegionName.ALPS_WELKIN_PASS,
            PoYItemName.IDOL_OF_FEATHERS_2
        )
        self.create_location(
            PoYLocationName.IDOL_OF_GREATER_BALANCE_1,
            PoYRegionName.ALPS_ULLRS_CHASM,
            PoYItemName.IDOL_OF_GREATER_BALANCE_1
        )
        self.create_location(
            PoYLocationName.IDOL_OF_GREATER_BALANCE_2,
            PoYRegionName.ALPS_TOWERING_VISIR,
            PoYItemName.IDOL_OF_GREATER_BALANCE_2
        )
        self.create_location(
            PoYLocationName.IDOL_OF_ICE_1,
            PoYRegionName.ALPS_MHOR_DRUIM,
            PoYItemName.IDOL_OF_ICE_1
        )
        self.create_location(
            PoYLocationName.IDOL_OF_ICE_2,
            PoYRegionName.ALPS_ELDRIS_WALL,
            PoYItemName.IDOL_OF_ICE_2
        )
        self.create_location(
            PoYLocationName.IDOL_OF_PINCHES_1,
            PoYRegionName.ALPS_SEASIDE_TRIBUNE,
            PoYItemName.IDOL_OF_PINCHES_1
        )
        self.create_location(
            PoYLocationName.IDOL_OF_PINCHES_2,
            PoYRegionName.ALPS_TOWERING_VISIR,
            PoYItemName.IDOL_OF_PINCHES_2
        )
        self.create_location(
            PoYLocationName.IDOL_OF_PITCHES_1,
            PoYRegionName.ALPS_CASTLE_OF_THE_SWAN_KING,
            PoYItemName.IDOL_OF_PITCHES_1
        )
        self.create_location(
            PoYLocationName.IDOL_OF_PITCHES_2,
            PoYRegionName.ALPS_ELJUNS_FOLLY,
            PoYItemName.IDOL_OF_PITCHES_2
        )
        self.create_location(
            PoYLocationName.IDOL_OF_SLOPERS_1,
            PoYRegionName.ALPS_CASTLE_OF_THE_SWAN_KING,
            PoYItemName.IDOL_OF_SLOPERS_1
        )
        self.create_location(
            PoYLocationName.IDOL_OF_SLOPERS_2,
            PoYRegionName.ALPS_OLD_REKKJA,
            PoYItemName.IDOL_OF_SLOPERS_2
        )
        self.create_location(
            PoYLocationName.IDOL_OF_SUNDOWN_1,
            PoYRegionName.ALPS_CASTLE_OF_THE_SWAN_KING,
            PoYItemName.IDOL_OF_SUNDOWN_1
        )
        self.create_location(
            PoYLocationName.IDOL_OF_SUNDOWN_2,
            PoYRegionName.ALPS_DUNDERHORN,
            PoYItemName.IDOL_OF_SUNDOWN_2
        )
        self.create_location(
            PoYLocationName.IDOL_OF_SEEDS_1,
            PoYRegionName.ALPS_TREPPENWALD,
            PoYItemName.IDOL_OF_SEEDS_1
        )
        self.create_location(
            PoYLocationName.IDOL_OF_SEEDS_2,
            PoYRegionName.ALPS_ELDRIS_WALL,
            PoYItemName.IDOL_OF_SEEDS_2
        )

    def create_location(
        self,
        name: PoYLocationName,
        region_name: PoYRegionName,
        item_name: PoYItemName
    ) -> None:
        """
        Creates a location and stores it.

        :param name: The name of the location
        :param region_name: The region this location is for
        :param item_name: The item locked behind this location
        """

        if region_name not in self.locations:
            self.locations[region_name] = []

        self.locations[region_name].append(PoYLocationData(
            name, item_name
        ))


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
