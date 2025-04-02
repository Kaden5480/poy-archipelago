from enum import StrEnum

from .items import BaseItemName, \
                   DlcItemName, \
                   ItemSuffix

class BaseLocationName(StrEnum):
    """
    Locations which exist in the base game.
    """

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
    TOOL_ARTEFACT_MAP                 = BaseItemName.TOOL_ARTEFACT_MAP
    TOOL_BAROMETER                    = BaseItemName.TOOL_BAROMETER
    TOOL_CHALK_BAG                    = BaseItemName.TOOL_CHALK_BAG
    TOOL_COFFEE                       = BaseItemName.TOOL_COFFEE
    TOOL_CRAMPONS_6                   = BaseItemName.TOOL_CRAMPONS_6
    TOOL_CRAMPONS_10                  = BaseItemName.TOOL_CRAMPONS_10
    TOOL_ICE_AXES                     = BaseItemName.TOOL_ICE_AXES
    TOOL_MONOCULAR                    = BaseItemName.TOOL_MONOCULAR
    TOOL_PHONOGRAPH                   = BaseItemName.TOOL_PHONOGRAPH
    TOOL_PIPE                         = BaseItemName.TOOL_PIPE
    TOOL_POCKETWATCH                  = BaseItemName.TOOL_POCKETWATCH
    TOOL_ROPE                         = BaseItemName.TOOL_ROPE

    ALL_PICTURES_ROPE_DOUBLE          = "All Picture Pieces (Double Length Ropes)"

    # All artefacts
    ALL_ARTEFACTS_INFINITE_COFFEE     = "All Artefacts (Infinite Coffee)"
    ALL_ARTEFACTS_INFINITE_CHALK      = "All Artefacts (Infinite Chalk)"
    ALL_ARTEFACTS_ROPES               = "All Artefacts (Rope)"

    # All of each category
    ALL_FUNDAMENTALS_MEDAL            = "All Fundamentals (Medal)"
    ALL_FUNDAMENTALS_ROPES            = "All Fundamentals (Ropes)"
    ALL_FUNDAMENTALS_CHALK            = "All Fundamentals (Chalk)"
    ALL_FUNDAMENTALS_COFFEE           = "All Fundamentals (Coffee)"

    ALL_INTERMEDIATE_MEDAL            = "All Intermediate (Medal)"
    ALL_INTERMEDIATE_ROPES            = "All Intermediate (Ropes)"
    ALL_INTERMEDIATE_CHALK            = "All Intermediate (Chalk)"
    ALL_INTERMEDIATE_COFFEE           = "All Intermediate (Coffee)"

    ALL_ADVANCED_MEDAL                = "All Advanced (Medal)"
    ALL_ADVANCED_ROPES                = "All Advanced (Ropes)"
    ALL_ADVANCED_CHALK                = "All Advanced (Chalk)"
    ALL_ADVANCED_COFFEE               = "All Advanced (Coffee)"

    TICKET_NORTHERN_RANGE             = BaseItemName.TICKET_NORTHERN_RANGE

    BOOK_GALES_FUNDAMENTALS           = BaseItemName.BOOK_GALES_FUNDAMENTALS
    BOOK_GALES_INTERMEDIATE           = BaseItemName.BOOK_GALES_INTERMEDIATE
    BOOK_GALES_ADVANCED               = BaseItemName.BOOK_GALES_ADVANCED
    BOOK_NORTHERN_EXPERT              = BaseItemName.BOOK_NORTHERN_EXPERT


class DlcLocationName(StrEnum):
    """
    Locations which exist in the DLC.
    """

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

    # Symbolic locations for unlocking books
    BOOK_ALPS_ESSENTIALS              = DlcItemName.BOOK_ALPS_ESSENTIALS
    BOOK_ALPS_GREATS                  = DlcItemName.BOOK_ALPS_GREATS
    BOOK_ALPS_ARCTIC                  = DlcItemName.BOOK_ALPS_ARCTIC


class LocationSuffix(StrEnum):
    """
    Locations which are generated based
    upon suffixes instead.
    """

    TIME_ATTACK     = "Time Attack"
    STAMP           = ItemSuffix.STAMP
    STAMP_FREE_SOLO = ItemSuffix.STAMP_FREE_SOLO


# Location names excluding suffixes
LocationName = BaseLocationName | DlcLocationName
