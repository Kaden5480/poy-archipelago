from BaseClasses import ItemClassification

class PoYItem:
    id: int
    name: str
    classification: ItemClassification

    def __init__(self, id: int, name: str, classification: ItemClassification) -> None:
        """
        Initializes a PoYItem.

        :param id: The ID of this item
        :param name: The name of this item
        :param classification: The classification of this item
        """

        self.id = id
        self.name = name
        self.classification = classification

class PoYItems:
    collectables_base: list[PoYItem]
    collectables_dlc: list[PoYItem]
    tools: list[PoYItem]

    def __init__(self, handler: IDHandler) -> None:
        """
        Initializes the item information for all items.

        :param handler: The ID handler for assigning IDs to items
        """

        self.collectables_base = [
            # Artefacts
            PoYItem(handler.new_id(), "Hat (Old Mill)",                               ItemClassification.progression),
            PoYItem(handler.new_id(), "Picture Fragment (Gray Gully)",                ItemClassification.progression),
            PoYItem(handler.new_id(), "Shoe (Old Man of Sjór)",                       ItemClassification.progression),
            PoYItem(handler.new_id(), "Sleeping Bag (Giant's Shelf)",                 ItemClassification.progression),
            PoYItem(handler.new_id(), "Hat (Evergreen's End)",                        ItemClassification.progression),
            PoYItem(handler.new_id(), "Safety Helmet (Old Grove's Skelf)",            ItemClassification.progression),
            PoYItem(handler.new_id(), "Picture Fragment (Land's End)",                ItemClassification.progression),
            PoYItem(handler.new_id(), "Backpack (Aldr Grotto)",                       ItemClassification.progression),
            PoYItem(handler.new_id(), "Shovel (Three Brothers)",                      ItemClassification.progression),
            PoYItem(handler.new_id(), "Fundamental Statue (Walter's Crag)",           ItemClassification.progression),
            PoYItem(handler.new_id(), "Picture Fragment (The Great Crevice)",         ItemClassification.progression),
            PoYItem(handler.new_id(), "Intermediate Statue (Leaning Spire)",          ItemClassification.progression),
            PoYItem(handler.new_id(), "Picture Frame (Great Gaol)",                   ItemClassification.progression),
            PoYItem(handler.new_id(), "Picture Fragment (St. Haelga)",                ItemClassification.progression),
            PoYItem(handler.new_id(), "Advanced Statue (Ymir's Shadow)",              ItemClassification.progression),
            PoYItem(handler.new_id(), "Expert Statue (Great Bulwark)",                ItemClassification.progression),

            # Bird seeds
            PoYItem(handler.new_id(), "Bird Seeds +1 (Three Brothers)",               ItemClassification.filler),
            PoYItem(handler.new_id(), "Bird Seeds +1 (Old Skerry)",                   ItemClassification.filler),
            PoYItem(handler.new_id(), "Bird Seeds +1 (Great Gaol)",                   ItemClassification.filler),
            PoYItem(handler.new_id(), "Bird Seeds +1 (Eldenhorn)",                    ItemClassification.filler),
            PoYItem(handler.new_id(), "Bird Seeds +1 (Ymir's Shadow)",                ItemClassification.filler),

            # Chalk
            PoYItem(handler.new_id(), "Chalk +2 (Walker's Pillar)",                   ItemClassification.useful | ItemClassification.progression),
            PoYItem(handler.new_id(), "Chalk +2 (Eldenhorn)",                         ItemClassification.useful | ItemClassification.progression),

            # Coffee
            PoYItem(handler.new_id(), "Coffee +2 (Old Langr)",                        ItemClassification.useful | ItemClassification.progression),
            PoYItem(handler.new_id(), "Coffee +2 (Wuthering Crest)",                  ItemClassification.useful | ItemClassification.progression),

            # Ropes
            PoYItem(handler.new_id(), "Rope +2 (Old Man of Sjór)",                    ItemClassification.filler),
            PoYItem(handler.new_id(), "Rope +2 (Evergreen's End)",                    ItemClassification.filler),
            PoYItem(handler.new_id(), "Rope +2 (Hangman's Leap)",                     ItemClassification.filler),
            PoYItem(handler.new_id(), "Rope +2 (Land's End)",                         ItemClassification.filler),
            PoYItem(handler.new_id(), "Rope +2 (Walter's Crag)",                      ItemClassification.filler),
            PoYItem(handler.new_id(), "Rope +2 (The Great Crevice)",                  ItemClassification.filler),
            PoYItem(handler.new_id(), "Rope +2 (Old Hagger)",                         ItemClassification.filler),
            PoYItem(handler.new_id(), "Rope +2 (Ugsome Stórr)",                       ItemClassification.filler),
            PoYItem(handler.new_id(), "Rope +2 (Wuthering Crest)",                    ItemClassification.filler),
            PoYItem(handler.new_id(), "Rope +2 (Great Gaol)",                         ItemClassification.filler),
            PoYItem(handler.new_id(), "Rope +2 (Eldenhorn)",                          ItemClassification.filler),
            PoYItem(handler.new_id(), "Rope +2 (Ymir's Shadow)",                      ItemClassification.filler),

            # NPC interactions
            PoYItem(handler.new_id(), "Coffee +5 (The Twins Interaction)",            ItemClassification.filler),
            PoYItem(handler.new_id(), "Coffee +5 (Giant's Nose Interaction)",         ItemClassification.filler),
            PoYItem(handler.new_id(), "Rope +1 (Walter's Crag Co-Climb)",             ItemClassification.filler),
            PoYItem(handler.new_id(), "Rope +1 (Walker's Pillar Co-Climb)",           ItemClassification.filler),
            PoYItem(handler.new_id(), "Rope +1 (Great Gaol Interaction)",             ItemClassification.filler),
            PoYItem(handler.new_id(), "Rope +1 (St. Haelga Interaction)",             ItemClassification.filler),
        ]

        self.collectables_dlc = [
            # Gentiana
            PoYItem(handler.new_id(), "Gentiana (Mara's Arch)",                       ItemClassification.progression),
            PoYItem(handler.new_id(), "Gentiana (Treppenwald)",                       ItemClassification.progression),
            PoYItem(handler.new_id(), "Gentiana (Quietude)",                          ItemClassification.progression),
            PoYItem(handler.new_id(), "Gentiana (Eljun's Folly)",                     ItemClassification.progression),
            PoYItem(handler.new_id(), "Gentiana (Einvald Falls)",                     ItemClassification.progression),
            PoYItem(handler.new_id(), "Gentiana (Mhòr Druim)",                        ItemClassification.progression),
            PoYItem(handler.new_id(), "Gentiana (Towering Vísir)",                    ItemClassification.progression),

            # Edelweiss
            PoYItem(handler.new_id(), "Edelweiss (Great Bók Tree)",                   ItemClassification.progression),
            PoYItem(handler.new_id(), "Edelweiss (Castle of the Swan King)",          ItemClassification.progression),
            PoYItem(handler.new_id(), "Edelweiss (Ivory Granites)",                   ItemClassification.progression),
            PoYItem(handler.new_id(), "Edelweiss (Dunderhorn)",                       ItemClassification.progression),
            PoYItem(handler.new_id(), "Edelweiss (Welkin Pass)",                      ItemClassification.progression),
            PoYItem(handler.new_id(), "Edelweiss (Towering Vísir)",                   ItemClassification.progression),
            PoYItem(handler.new_id(), "Edelweiss (Eldris Wall)",                      ItemClassification.progression),

            # Idols
            PoYItem(handler.new_id(), "Idol of Crimps #1 (Grainne Spire)",            ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Crimps #2 (Great Bók Tree) ",          ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Cruelty #1 (Ivory Granites)",          ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Cruelty #2 (Mount Mhòrgorm)",          ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Feathers #1 (Mhòr Druim)",             ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Feathers #2 (Welkin Pass)",            ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Greater Balance #1 (Ullr's Chasm)",    ItemClassification.useful | ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Greater Balance #2 (Towering Vísir)",  ItemClassification.useful | ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Ice #1 (Mhòr Druim)",                  ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Ice #2 (Eldris Wall)",                 ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Pinches #1 (Seaside Tribune)",         ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Pinches #2 (Towering Vísir)",          ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Pitches #1 (Castle of the Swan King)", ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Pitches #2 (Eljun's Folly)",           ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Slopers #1 (Castle of the Swan King)", ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Slopers #2 (Old Rekkja)",              ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Sundown #1 (Castle of the Swan King)", ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Sundown #2 (Dunderhorn)",              ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Seeds #1 (Treppenwald)",               ItemClassification.useful | ItemClassification.progression),
            PoYItem(handler.new_id(), "Idol of Seeds #2 (Eldris Wall)",               ItemClassification.useful | ItemClassification.progression),
        ]

        self.tools = [
            PoYItem(handler.new_id(), "Barometer + Map",                              ItemClassification.useful),
            PoYItem(handler.new_id(), "Chalk Bag",                                    ItemClassification.useful),
            PoYItem(handler.new_id(), "Coffee",                                       ItemClassification.useful),
            PoYItem(handler.new_id(), "Crampons (6 Point)",                           ItemClassification.useful),
            PoYItem(handler.new_id(), "Crampons (10 Point)",                          ItemClassification.useful),
            PoYItem(handler.new_id(), "Ice Axes",                                     ItemClassification.useful | ItemClassification.progression),
            PoYItem(handler.new_id(), "Monocular",                                    ItemClassification.useful | ItemClassification.progression),
            PoYItem(handler.new_id(), "Phonograph",                                   ItemClassification.filler),
            PoYItem(handler.new_id(), "Pipe",                                         ItemClassification.useful),
            PoYItem(handler.new_id(), "Pocketwatch",                                  ItemClassification.useful | ItemClassification.progression),
            PoYItem(handler.new_id(), "Rope",                                         ItemClassification.useful),
            PoYItem(handler.new_id(), "Rope (Double Length)",                         ItemClassification.useful),
        ]
