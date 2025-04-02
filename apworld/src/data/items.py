from BaseClasses import ItemClassification

from .id_handler import IDHandler

from ..names.items import ItemName, \
                          BaseItemName, \
                          DlcItemName

class ItemData:
    # This item's ID
    __id: int

    # The name of the item
    __name: str

    # The item's classification
    __classification: ItemClassification

    def __init__(
        self,
        id: int,
        name: str,
        classification: ItemClassification
    ) -> None:
        """
        Initializes an ItemData object.

        :param id: The ID to assign to this item
        :param name: The name of this item
        :param classification: The classification of this item
        """

        self.__id = id
        self.__name = name
        self.__classification = classification

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def classification(self) -> ItemClassification:
        return self.__classification


class Items:
    __handler: IDHandler
    __items: dict[str, ItemData]

    def __init__(self, handler: IDHandler) -> None:
        """
        Initializes a PoYItems object.

        :param handler: The handler to assign IDs with
        """

        self.__handler = handler
        self.__items = {}

        self.__create_all()

    def get_data(
        self,
        name: ItemName
    ) -> ItemData:
        """
        Gets data for a given item name.

        :param name: The name of the item to get the data for
        :returns: The item's data
        """

        return self.__items.get[name.value]

    def __create_data(
        self,
        name: ItemName,
        classification: ItemClassification
    ) -> None:
        """
        Creates data for an item with the given name
        and classification, adding it to the
        dictionary of items.

        :param name: The name of the item
        :param classification: The classification of the item
        """

        self.__items[name.value] = ItemData(
            self.__handler.new_id(), name.value, classification
        )


    def __create_all() -> None:
        """
        Creates all data for items.
        """

        ## Base game
        # Artefacts
        self.__create_data(BaseItemName.HAT_1,                     ItemClassification.progression)
        self.__create_data(BaseItemName.HAT_2,                     ItemClassification.progression)
        self.__create_data(BaseItemName.SHOE,                      ItemClassification.progression)
        self.__create_data(BaseItemName.SLEEPING_BAG,              ItemClassification.progression)
        self.__create_data(BaseItemName.SAFETY_HELMET,             ItemClassification.progression)
        self.__create_data(BaseItemName.BACKPACK,                  ItemClassification.progression)
        self.__create_data(BaseItemName.SHOVEL,                    ItemClassification.progression)
        self.__create_data(BaseItemName.PICTURE_FRAGMENT,          ItemClassification.progression)
        self.__create_data(BaseItemName.PICTURE_FRAME,             ItemClassification.progression)
        self.__create_data(BaseItemName.STATUE_FUNDAMENTALS,       ItemClassification.progression)
        self.__create_data(BaseItemName.STATUE_INTERMEDIATE,       ItemClassification.progression)
        self.__create_data(BaseItemName.STATUE_ADVANCED,           ItemClassification.progression)
        self.__create_data(BaseItemName.STATUE_EXPERT,             ItemClassification.progression)

        # Consumables
        self.__create_data(BaseItemName.BIRD_SEEDS,                ItemClassification.filler)
        self.__create_data(BaseItemName.CHALK,                     ItemClassification.useful | ItemClassification.progression)
        self.__create_data(BaseItemName.COFFEE_2,                  ItemClassification.useful | ItemClassification.progression)
        self.__create_data(BaseItemName.COFFEE_5,                  ItemClassification.filler)
        self.__create_data(BaseItemName.ROPES_1,                   ItemClassification.filler)
        self.__create_data(BaseItemName.ROPES_2,                   ItemClassification.filler)

        # Tools
        self.__create_data(BaseItemName.TOOL_ARTEFACT_MAP,         ItemClassification.useful)
        self.__create_data(BaseItemName.TOOL_BAROMETER,            ItemClassification.useful)
        self.__create_data(BaseItemName.TOOL_CHALK_BAG,            ItemClassification.useful)
        self.__create_data(BaseItemName.TOOL_COFFEE,               ItemClassification.useful)
        self.__create_data(BaseItemName.TOOL_CRAMPONS_6,           ItemClassification.useful | ItemClassification.progression)
        self.__create_data(BaseItemName.TOOL_CRAMPONS_10,          ItemClassification.useful | ItemClassification.progression)
        self.__create_data(BaseItemName.TOOL_ICE_AXES,             ItemClassification.useful | ItemClassification.progression)
        self.__create_data(BaseItemName.TOOL_MONOCULAR,            ItemClassification.useful | ItemClassification.progression)
        self.__create_data(BaseItemName.TOOL_PHONOGRAPH,           ItemClassification.filler)
        self.__create_data(BaseItemName.TOOL_PIPE,                 ItemClassification.useful)
        self.__create_data(BaseItemName.TOOL_POCKETWATCH,          ItemClassification.useful | ItemClassification.progression)
        self.__create_data(BaseItemName.TOOL_ROPE,                 ItemClassification.useful)
        self.__create_data(BaseItemName.TOOL_ROPE_DOUBLE,          ItemClassification.useful)

        ## Alps DLC
        # Flowers
        self.__create_data(DlcItemName.GENTIANA,                  ItemClassification.progression)
        self.__create_data(DlcItemName.EDELWEISS,                 ItemClassification.progression)

        # Idols
        self.__create_data(DlcItemName.IDOL_OF_CRIMPS_1,          ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_CRIMPS_2,          ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_CRUELTY_1,         ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_CRUELTY_2,         ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_FEATHERS_1,        ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_FEATHERS_2,        ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_GREATER_BALANCE_1, ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_GREATER_BALANCE_2, ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_ICE_1,             ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_ICE_2,             ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_PINCHES_1,         ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_PINCHES_2,         ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_PITCHES_1,         ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_PITCHES_2,         ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_SLOPERS_1,         ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_SLOPERS_2,         ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_SUNDOWN_1,         ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_SUNDOWN_2,         ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_SEEDS_1,           ItemClassification.progression)
        self.__create_data(DlcItemName.IDOL_OF_SEEDS_2,           ItemClassification.progression)

        ## Extra items which can be randomised
        self.__create_data(DlcItemName.TICKET_NORTHERN_RANGE,     ItemClassification.progression)

        self.__create_data(DlcItemName.BOOK_GALES_FUNDAMENTALS,   ItemClassification.progression)
        self.__create_data(DlcItemName.BOOK_GALES_INTERMEDIATE,   ItemClassification.progression)
        self.__create_data(DlcItemName.BOOK_GALES_ADVANCED,       ItemClassification.progression)
        self.__create_data(DlcItemName.BOOK_NORTHERN_EXPERT,      ItemClassification.progression)
        self.__create_data(DlcItemName.BOOK_ALPS_ESSENTIALS,      ItemClassification.progression)
        self.__create_data(DlcItemName.BOOK_ALPS_GREATS,          ItemClassification.progression)
        self.__create_data(DlcItemName.BOOK_ALPS_ARCTIC,          ItemClassification.progression)

        self.__create_data(DlcItemName.STAMP_GALES_FUNDAMENTALS,  ItemClassification.progression)
        self.__create_data(DlcItemName.STAMP_GALES_INTERMEDIATE,  ItemClassification.progression)
        self.__create_data(DlcItemName.STAMP_GALES_ADVANCED,      ItemClassification.progression)
        self.__create_data(DlcItemName.STAMP_NORTHERN_EXPERT,     ItemClassification.progression)
        self.__create_data(DlcItemName.STAMP_ALPS_ESSENTIALS,     ItemClassification.progression)
        self.__create_data(DlcItemName.STAMP_ALPS_GREATS,         ItemClassification.progression)
        self.__create_data(DlcItemName.STAMP_ALPS_ARCTIC,         ItemClassification.progression)
