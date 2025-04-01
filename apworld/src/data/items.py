from enum import StrEnum

from .id_handler import IDHandler

class PoYItemName(StrEnum):
    ## Base game
    # Artefacts
    HAT_1                     = "Hat #1"
    HAT_2                     = "Hat #2"
    SHOE                      = "Shoe"
    SLEEPING_BAG              = "Sleeping Bag"
    SAFETY_HELMET             = "Safety Helmet"
    BACKPACK                  = "Backpack"
    SHOVEL                    = "Shovel"

    PICTURE_FRAGMENT          = "Picture Fragment"
    PICTURE_FRAME             = "Picture Frame"

    STATUE_FUNDAMENTALS       = "Fundamental Statue"
    STATUE_INTERMEDIATE       = "Intermediate Statue"
    STATUE_ADVANCED           = "Advanced Statue"
    STATUE_EXPERT             = "Expert Statue"

    # Consumables
    BIRD_SEEDS                = "Bird Seeds +1"
    CHALK                     = "Chalk +2"
    COFFEE_2                  = "Coffee +2"
    COFFEE_5                  = "Coffee +5"
    ROPES_1                   = "Rope +1"
    ROPES_2                   = "Rope +2"

    # Tools
    TOOL_ARTEFACT_MAP         = "Artefact Map"
    TOOL_BAROMETER            = "Barometer"
    TOOL_CHALK_BAG            = "Chalk Bag"
    TOOL_COFFEE               = "Coffee"
    TOOL_CRAMPONS_6           = "Crampons (6 Point)"
    TOOL_CRAMPONS_10          = "Crampons (10 Point)"
    TOOL_ICE_AXES             = "Ice Axes"
    TOOL_MONOCULAR            = "Monocular"
    TOOL_PHONOGRAPH           = "Phonograph"
    TOOL_PIPE                 = "Pipe"
    TOOL_POCKETWATCH          = "Pocketwatch"
    TOOL_ROPE                 = "Rope"
    TOOL_ROPE_DOUBLE          = "Rope (Double Length)"

    ## Alps DLC
    # Flowers
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

    ## Extra items which can be randomised
    BOOK_GALES_FUNDAMENTALS   = "Fundamentals Book"
    BOOK_GALES_INTERMEDIATE   = "Intermediate Book"
    BOOK_GALES_ADVANCED       = "Advanced Book"
    BOOK_NORTHERN_EXPERT      = "Expert Book"
    BOOK_ALPS_ESSENTIALS      = "Essentials Book"
    BOOK_ALPS_GREATS          = "Alpine Greats Book"
    BOOK_ALPS_ARCTIC          = "Arduous and Arctic Book"


base_items = [
    HAT_1,
    HAT_2,
    SHOE,
    SLEEPING_BAG,
    SAFETY_HELMET,
    BACKPACK,
    SHOVEL,
    PICTURE_FRAGMENT,
    PICTURE_FRAME,
    STATUE_FUNDAMENTALS,
    STATUE_INTERMEDIATE,
    STATUE_ADVANCED,
    STATUE_EXPERT,
    BIRD_SEEDS,
    CHALK,
    COFFEE_2,
    COFFEE_5,
    ROPES_1,
    ROPES_2,
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

dlc_items = [
    GENTIANA,
    EDELWEISS,
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


class PoYItemData:
    id: int
    name: PoYItemName
    classification: ItemClassification

    def __init__(
        self,
        name: PoYItemName,
        classification: ItemClassification
    ) -> None:
        """
        Initializes PoYItemData.

        :param name: The name of this item
        :param classification: The classification of this item
        """

        self.name = name
        self.classification = classification


class PoYItems:
    handler: IDHandler

    items: dict[PoYItemName, PoYItemData]

    def __init__(self, handler: IDHandler) -> None:
        """
        Initializes a PoYItems object.

        :param handler: The handler to assign IDs with
        """

        self.handler = handler
        self.items = {}

        ## Base game
        # Artefacts
        self.create_item(PoYItemName.HAT_1,                     ItemClassification.progression)
        self.create_item(PoYItemName.HAT_2,                     ItemClassification.progression)
        self.create_item(PoYItemName.SHOE,                      ItemClassification.progression)
        self.create_item(PoYItemName.SLEEPING_BAG,              ItemClassification.progression)
        self.create_item(PoYItemName.SAFETY_HELMET,             ItemClassification.progression)
        self.create_item(PoYItemName.BACKPACK,                  ItemClassification.progression)
        self.create_item(PoYItemName.SHOVEL,                    ItemClassification.progression)
        self.create_item(PoYItemName.PICTURE_FRAGMENT,          ItemClassification.progression)
        self.create_item(PoYItemName.PICTURE_FRAME,             ItemClassification.progression)
        self.create_item(PoYItemName.STATUE_FUNDAMENTALS,       ItemClassification.progression)
        self.create_item(PoYItemName.STATUE_INTERMEDIATE,       ItemClassification.progression)
        self.create_item(PoYItemName.STATUE_ADVANCED,           ItemClassification.progression)
        self.create_item(PoYItemName.STATUE_EXPERT,             ItemClassification.progression)

        # Consumables
        self.create_item(PoYItemName.BIRD_SEEDS,                ItemClassification.filler)
        self.create_item(PoYItemName.CHALK,                     ItemClassification.useful | ItemClassification.progression)
        self.create_item(PoYItemName.COFFEE_2,                  ItemClassification.useful | ItemClassification.progression)
        self.create_item(PoYItemName.COFFEE_5,                  ItemClassification.filler)
        self.create_item(PoYItemName.ROPES_1,                   ItemClassification.filler)
        self.create_item(PoYItemName.ROPES_2,                   ItemClassification.filler)

        # Tools
        self.create_item(PoYItemName.TOOL_ARTEFACT_MAP,         ItemClassification.useful)
        self.create_item(PoYItemName.TOOL_BAROMETER,            ItemClassification.useful)
        self.create_item(PoYItemName.TOOL_CHALK_BAG,            ItemClassification.useful)
        self.create_item(PoYItemName.TOOL_COFFEE,               ItemClassification.useful)
        self.create_item(PoYItemName.TOOL_CRAMPONS_6,           ItemClassification.useful | ItemClassification.progression)
        self.create_item(PoYItemName.TOOL_CRAMPONS_10,          ItemClassification.useful | ItemClassification.progression)
        self.create_item(PoYItemName.TOOL_ICE_AXES,             ItemClassification.useful | ItemClassification.progression)
        self.create_item(PoYItemName.TOOL_MONOCULAR,            ItemClassification.useful | ItemClassification.progression)
        self.create_item(PoYItemName.TOOL_PHONOGRAPH,           ItemClassification.filler)
        self.create_item(PoYItemName.TOOL_PIPE,                 ItemClassification.useful)
        self.create_item(PoYItemName.TOOL_POCKETWATCH,          ItemClassification.useful | ItemClassification.progression)
        self.create_item(PoYItemName.TOOL_ROPE,                 ItemClassification.useful)
        self.create_item(PoYItemName.TOOL_ROPE_DOUBLE,          ItemClassification.useful)

        ## Alps DLC
        # Flowers
        self.create_item(PoYItemName.GENTIANA,                  ItemClassification.progression)
        self.create_item(PoYItemName.EDELWEISS,                 ItemClassification.progression)

        # Idols
        self.create_item(PoYItemName.IDOL_OF_CRIMPS_1,          ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_CRIMPS_2,          ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_CRUELTY_1,         ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_CRUELTY_2,         ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_FEATHERS_1,        ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_FEATHERS_2,        ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_GREATER_BALANCE_1, ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_GREATER_BALANCE_2, ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_ICE_1,             ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_ICE_2,             ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_PINCHES_1,         ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_PINCHES_2,         ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_PITCHES_1,         ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_PITCHES_2,         ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_SLOPERS_1,         ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_SLOPERS_2,         ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_SUNDOWN_1,         ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_SUNDOWN_2,         ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_SEEDS_1,           ItemClassification.progression)
        self.create_item(PoYItemName.IDOL_OF_SEEDS_2,           ItemClassification.progression)

        ## Extra items which can be randomised
        self.create_item(PoYItemName.BOOK_GALES_FUNDAMENTALS,   ItemClassification.progression)
        self.create_item(PoYItemName.BOOK_GALES_INTERMEDIATE,   ItemClassification.progression)
        self.create_item(PoYItemName.BOOK_GALES_ADVANCED,       ItemClassification.progression)
        self.create_item(PoYItemName.BOOK_NORTHERN_EXPERT,      ItemClassification.progression)
        self.create_item(PoYItemName.BOOK_ALPS_ESSENTIALS,      ItemClassification.progression)
        self.create_item(PoYItemName.BOOK_ALPS_GREATS,          ItemClassification.progression)
        self.create_item(PoYItemName.BOOK_ALPS_ARCTIC,          ItemClassification.progression)

    def create_item(
        self,
        name: PoYItemName,
        classification: ItemClassification
    ) -> None:
        """
        Creates an item with the given name
        and classification, adding it to the
        dictionary of items.

        :param name: The name of the item
        :param classification: The classification of the item
        """

        self.items[name] = PoYItemData(
            self.handler.new_id(), name, classification
        )


class PeaksItem(Item):
    game: str = GAME
