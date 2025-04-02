from enum import StrEnum

class BaseItemName(StrEnum):
    """
    Items found within the base game.
    """

    # Artefacts
    HAT_1                   = "Hat #1"
    HAT_2                   = "Hat #2"
    SHOE                    = "Shoe"
    SLEEPING_BAG            = "Sleeping Bag"
    SAFETY_HELMET           = "Safety Helmet"
    BACKPACK                = "Backpack"
    SHOVEL                  = "Shovel"

    PICTURE_FRAGMENT        = "Picture Fragment"
    PICTURE_FRAME           = "Picture Frame"

    STATUE_FUNDAMENTALS     = "Fundamental Statue"
    STATUE_INTERMEDIATE     = "Intermediate Statue"
    STATUE_ADVANCED         = "Advanced Statue"
    STATUE_EXPERT           = "Expert Statue"

    # Consumables
    BIRD_SEEDS              = "Bird Seeds +1"
    CHALK_2                 = "Chalk +2"
    COFFEE_2                = "Coffee +2"
    COFFEE_5                = "Coffee +5"
    ROPES_1                 = "Rope +1"
    ROPES_2                 = "Rope +2"

    # Tools
    TOOL_ARTEFACT_MAP       = "Artefact Map"
    TOOL_BAROMETER          = "Barometer"
    TOOL_CHALK_BAG          = "Chalk Bag"
    TOOL_COFFEE             = "Coffee Unlock"
    TOOL_CRAMPONS_6         = "Crampons (6 Point)"
    TOOL_CRAMPONS_10        = "Crampons (10 Point)"
    TOOL_ICE_AXES           = "Ice Axes"
    TOOL_MONOCULAR          = "Monocular"
    TOOL_PHONOGRAPH         = "Phonograph"
    TOOL_PIPE               = "Pipe"
    TOOL_POCKETWATCH        = "Pocketwatch"
    TOOL_ROPE               = "Rope Unlock"
    TOOL_ROPE_DOUBLE        = "Rope (Double Length)"

    # Infinite from getting all artefacts
    TOOL_INFINITE_CHALK     = "Infinite Chalk"
    TOOL_INFINITE_COFFEE    = "Infinite Coffee"

    # Medals for completing all peaks
    MEDAL_FUNDAMENTALS      = "Fundamentals Medal"
    MEDAL_INTERMEDIATE      = "Intermediate Medal"
    MEDAL_ADVANCED          = "Advanced Medal"

    # Ticket to access the northern cabin
    TICKET_NORTHERN_RANGE   = "Northern Range Ticket"

    # The books to access each category
    BOOK_GALES_FUNDAMENTALS = "Fundamentals Book"
    BOOK_GALES_INTERMEDIATE = "Intermediate Book"
    BOOK_GALES_ADVANCED     = "Advanced Book"
    BOOK_NORTHERN_EXPERT    = "Expert Book"


class DlcItemName(StrEnum):
    """
    Items found within the DLC.
    """

    GENTIANA                  = "Gentiana"
    EDELWEISS                 = "Edelweiss"

    # Idols
    IDOL_OF_CRIMPS_1          = "Idol of Crimps #1"
    IDOL_OF_CRIMPS_2          = "Idol of Crimps #2"
    IDOL_OF_CRUELTY_1         = "Idol of Cruelty #1"
    IDOL_OF_CRUELTY_2         = "Idol of Cruelty #2"
    IDOL_OF_FEATHERS_1        = "Idol of Feathers #1"
    IDOL_OF_FEATHERS_2        = "Idol of Feathers #2"
    IDOL_OF_GREATER_BALANCE_1 = "Idol of Greater Balance #1"
    IDOL_OF_GREATER_BALANCE_2 = "Idol of Greater Balance #2"
    IDOL_OF_ICE_1             = "Idol of Ice #1"
    IDOL_OF_ICE_2             = "Idol of Ice #2"
    IDOL_OF_PINCHES_1         = "Idol of Pinches #1"
    IDOL_OF_PINCHES_2         = "Idol of Pinches #2"
    IDOL_OF_PITCHES_1         = "Idol of Pitches #1"
    IDOL_OF_PITCHES_2         = "Idol of Pitches #2"
    IDOL_OF_SLOPERS_1         = "Idol of Slopers #1"
    IDOL_OF_SLOPERS_2         = "Idol of Slopers #2"
    IDOL_OF_SUNDOWN_1         = "Idol of Sundown #1"
    IDOL_OF_SUNDOWN_2         = "Idol of Sundown #2"
    IDOL_OF_SEEDS_1           = "Idol of Seeds #1"
    IDOL_OF_SEEDS_2           = "Idol of Seeds #2"

    # The books to access each category
    BOOK_ALPS_ESSENTIALS      = "Essentials Book"
    BOOK_ALPS_GREATS          = "Alpine Greats Book"
    BOOK_ALPS_ARCTIC          = "Arduous and Arctic Book"


class ItemSuffix(StrEnum):
    """
    Items which are generated based
    upon suffixes instead.
    """

    STAMP           = "Stamp"
    STAMP_FREE_SOLO = "Stamp (Free Solo)"


# All item names, excluding suffixes
ItemName = BaseItemName | DlcItemName
