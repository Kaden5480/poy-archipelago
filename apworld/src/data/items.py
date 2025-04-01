from enum import StrEnum

from BaseClasses import ItemClassification

class ItemName(StrEnum):
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

    STATUE_FUNDAMENTALS               = "Fundamental Statue (Walter's Crag)"
    STATUE_INTERMEDIATE               = "Intermediate Statue (Leaning Spire)"
    STATUE_ADVANCED                   = "Advanced Statue (Ymir's Shadow)"
    STATUE_EXPERT                     = "Expert Statue (Great Bulwark)"

    # Bird seeds
    BIRD_SEEDS_THREE_BROTHERS         = "Bird Seeds +1 (Three Brothers)"
    BIRD_SEEDS_OLD_SKERRY             = "Bird Seeds +1 (Old Skerry)"
    BIRD_SEEDS_GREAT_GAOL             = "Bird Seeds +1 (Great Gaol)"
    BIRD_SEEDS_ELDENHORN              = "Bird Seeds +1 (Eldenhorn)"
    BIRD_SEEDS_YMIRS_SHADOW           = "Bird Seeds +1 (Ymir's Shadow)"

    # Chalk
    CHALK_WALKERS_PILLAR              = "Chalk +2 (Walker's Pillar)"
    CHALK_ELDENHORN                   = "Chalk +2 (Eldenhorn)"

    # Coffee
    COFFEE_OLD_LANGR                  = "Coffee +2 (Old Langr)"
    COFFEE_WUTHERING_CREST            = "Coffee +2 (Wuthering Crest)"

    # Ropes
    ROPE_OLD_MAN_OF_SJOR              = "Rope +2 (Old Man of Sjór)"
    ROPE_EVERGREENS_END               = "Rope +2 (Evergreen's End)"
    ROPE_HANGMANS_LEAP                = "Rope +2 (Hangman's Leap)"
    ROPE_LANDS_END                    = "Rope +2 (Land's End)"
    ROPE_WALTERS_CRAG                 = "Rope +2 (Walter's Crag)"
    ROPE_THE_GREAT_CREVICE            = "Rope +2 (The Great Crevice)"
    ROPE_OLD_HAGGER                   = "Rope +2 (Old Hagger)"
    ROPE_UGSOME_STORR                 = "Rope +2 (Ugsome Stórr)"
    ROPE_WUTHERING_CREST              = "Rope +2 (Wuthering Crest)"
    ROPE_GREAT_GAOL                   = "Rope +2 (Great Gaol)"
    ROPE_ELDENHORN                    = "Rope +2 (Eldenhorn)"
    ROPE_YMIRS_SHADOW                 = "Rope +2 (Ymir's Shadow)"

    # NPC interactions
    NPC_COFFEE_THE_TWINS              = "Coffee +5 (The Twins Interaction)"
    NPC_COFFEE_GIANTS_NOSE            = "Coffee +5 (Giant's Nose Interaction)"
    NPC_ROPE_WALTERS_CRAG             = "Rope +1 (Walter's Crag Co-Climb)"
    NPC_ROPE_WALKERS_PILLAR           = "Rope +1 (Walker's Pillar Co-Climb)"
    NPC_ROPE_GREAT_GAOL               = "Rope +1 (Great Gaol Interaction)"
    NPC_ROPE_ST_HAELGA                = "Rope +1 (St. Haelga Interaction)"

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

    TOOL_BAROMETER_MAP                = "Barometer + Map"
    TOOL_CHALK_BAG                    = "Chalk Bag"
    TOOL_COFFEE                       = "Coffee"
    TOOL_CRAMPONS_6                   = "Crampons (6 Point)"
    TOOL_CRAMPONS_10                  = "Crampons (10 Point)"
    TOOL_ICE_AXES                     = "Ice Axes"
    TOOL_MONOCULAR                    = "Monocular"
    TOOL_PHONOGRAPH                   = "Phonograph"
    TOOL_PIPE                         = "Pipe"
    TOOL_POCKETWATCH                  = "Pocketwatch"
    TOOL_ROPE                         = "Rope"
    TOOL_ROPE_DOUBLE                  = "Rope (Double Length)"


class PoYItem:
    id: int
    name: str
    classification: ItemClassification

    def __init__(self, id: int, name: ItemName, classification: ItemClassification) -> None:
        """
        Initializes a PoYItem.

        :param id: The ID of this item
        :param name: The name of this item
        :param classification: The classification of this item
        """

        self.id = id
        self.name = name.value
        self.classification = classification


class PoYItems:
    collectables_base: dict[str, PoYItem]
    collectables_dlc: dict[str, PoYItem]
    tools: dict[str, PoYItem]

    # All items
    items: dict[str, PoYItem]

    def __init__(self, handler: IDHandler) -> None:
        """
        Initializes the item information for all items.

        :param handler: The ID handler for assigning IDs to items
        """

        self.collectables_base = self.items_as_dict([
            # Artefacts
            PoYItem(handler.new_id(), ItemName.HAT_OLD_MILL,                      ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.PICTURE_GRAY_GULLY,                ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.SHOE_OLD_MAN_OF_SJOR,              ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.SLEEPING_BAG_GIANTS_SHELF,         ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.HAT_EVERGREENS_END,                ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.SAFETY_HELMET_OLD_GROVES_SKELF,    ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.PICTURE_LANDS_END,                 ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.BACKPACK_ALDR_GROTTO,              ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.SHOVEL_THREE_BROTHERS,             ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.STATUE_FUNDAMENTALS,               ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.PICTURE_THE_GREAT_CREVICE,         ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.STATUE_INTERMEDIATE,               ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.PICTURE_FRAME_GREAT_GAOL,          ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.PICTURE_ST_HAELGA,                 ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.STATUE_ADVANCED,                   ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.STATUE_EXPERT,                     ItemClassification.progression),

            # Bird seeds
            PoYItem(handler.new_id(), ItemName.BIRD_SEEDS_THREE_BROTHERS,         ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.BIRD_SEEDS_OLD_SKERRY,             ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.BIRD_SEEDS_GREAT_GAOL,             ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.BIRD_SEEDS_ELDENHORN,              ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.BIRD_SEEDS_YMIRS_SHADOW,           ItemClassification.filler),

            # Chalk
            PoYItem(handler.new_id(), ItemName.CHALK_WALKERS_PILLAR,              ItemClassification.useful | ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.CHALK_ELDENHORN,                   ItemClassification.useful | ItemClassification.progression),

            # Coffee
            PoYItem(handler.new_id(), ItemName.COFFEE_OLD_LANGR,                  ItemClassification.useful | ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.COFFEE_WUTHERING_CREST,            ItemClassification.useful | ItemClassification.progression),

            # Ropes
            PoYItem(handler.new_id(), ItemName.ROPE_OLD_MAN_OF_SJOR,              ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.ROPE_EVERGREENS_END,               ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.ROPE_HANGMANS_LEAP,                ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.ROPE_LANDS_END,                    ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.ROPE_WALTERS_CRAG,                 ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.ROPE_THE_GREAT_CREVICE,            ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.ROPE_OLD_HAGGER,                   ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.ROPE_UGSOME_STORR,                 ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.ROPE_WUTHERING_CREST,              ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.ROPE_GREAT_GAOL,                   ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.ROPE_ELDENHORN,                    ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.ROPE_YMIRS_SHADOW,                 ItemClassification.filler),

            # NPC interactions
            PoYItem(handler.new_id(), ItemName.NPC_COFFEE_THE_TWINS,              ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.NPC_COFFEE_GIANTS_NOSE,            ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.NPC_ROPE_WALTERS_CRAG,             ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.NPC_ROPE_WALKERS_PILLAR,           ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.NPC_ROPE_GREAT_GAOL,               ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.NPC_ROPE_ST_HAELGA,                ItemClassification.filler),
        ])

        self.collectables_dlc = self.items_as_dict([
            # Gentiana
            PoYItem(handler.new_id(), ItemName.GENTIANA_MARAS_ARCH,               ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.GENTIANA_TREPPENWALD,              ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.GENTIANA_QUIETUDE,                 ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.GENTIANA_ELJUNS_FOLLY,             ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.GENTIANA_EINVALD_FALLS,            ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.GENTIANA_MHOR_DRUIM,               ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.GENTIANA_TOWERING_VISIR,           ItemClassification.progression),

            # Edelweiss
            PoYItem(handler.new_id(), ItemName.EDELWEISS_GREAT_BOK_TREE,          ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.EDELWEISS_CASTLE_OF_THE_SWAN_KING, ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.EDELWEISS_IVORY_GRANITES,          ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.EDELWEISS_DUNDERHORN,              ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.EDELWEISS_WELKIN_PASS,             ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.EDELWEISS_TOWERING_VISIR,          ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.EDELWEISS_ELDRIS_WALL,             ItemClassification.progression),

            # Idols
            PoYItem(handler.new_id(), ItemName.IDOL_OF_CRIMPS_1,                  ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_CRIMPS_2,                  ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_CRUELTY_1,                 ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_CRUELTY_2,                 ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_FEATHERS_1,                ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_FEATHERS_2,                ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_GREATER_BALANCE_1,         ItemClassification.useful | ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_GREATER_BALANCE_2,         ItemClassification.useful | ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_ICE_1,                     ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_ICE_2,                     ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_PINCHES_1,                 ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_PINCHES_2,                 ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_PITCHES_1,                 ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_PITCHES_2,                 ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_SLOPERS_1,                 ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_SLOPERS_2,                 ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_SUNDOWN_1,                 ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_SUNDOWN_2,                 ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_SEEDS_1,                   ItemClassification.useful | ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.IDOL_OF_SEEDS_2,                   ItemClassification.useful | ItemClassification.progression),
        ])

        self.tools = self.items_as_dict([
            PoYItem(handler.new_id(), ItemName.TOOL_BAROMETER_MAP,                ItemClassification.useful),
            PoYItem(handler.new_id(), ItemName.TOOL_CHALK_BAG,                    ItemClassification.useful),
            PoYItem(handler.new_id(), ItemName.TOOL_COFFEE,                       ItemClassification.useful),
            PoYItem(handler.new_id(), ItemName.TOOL_CRAMPONS_6,                   ItemClassification.useful),
            PoYItem(handler.new_id(), ItemName.TOOL_CRAMPONS_10,                  ItemClassification.useful),
            PoYItem(handler.new_id(), ItemName.TOOL_ICE_AXES,                     ItemClassification.useful | ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.TOOL_MONOCULAR,                    ItemClassification.useful | ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.TOOL_PHONOGRAPH,                   ItemClassification.filler),
            PoYItem(handler.new_id(), ItemName.TOOL_PIPE,                         ItemClassification.useful),
            PoYItem(handler.new_id(), ItemName.TOOL_POCKETWATCH,                  ItemClassification.useful | ItemClassification.progression),
            PoYItem(handler.new_id(), ItemName.TOOL_ROPE,                         ItemClassification.useful),
            PoYItem(handler.new_id(), ItemName.TOOL_ROPE_DOUBLE,                  ItemClassification.useful),
        ])

        self.items = [
            **self.collectables_base,
            **self.collectables_dlc,
            **self.tools,
        ]

    def items_as_dict(self, items: list[PoYItem]) -> dict[str, PoYItem]:
        """
        Generates a dictionary mapping the names of items
        to the items themselves.

        :param items: The items to create a dictionary for
        :returns: The generated dictionary
        """

        return dict([
            (item.name, item) for item in items
        ])

    def get_item(self, name: str) -> PoYItem:
        """
        Gets an item given its name.

        :param name: The name of the item to search for
        :returns: The item with the given name
        """

        return self.items[name]
