from enum import IntEnum, \
                 StrEnum

from BaseClasses import CollectionState, \
                        Region

class CabinName(StrEnum):
    GALES    = "Great Gales Cabin"
    NORTHERN = "Northern Cabin"
    ALPS     = "Alps Cabin"


class PeakName(StrEnum):
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


gales_fundamentals: list[PeakName] = [
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

gales_intermediate: list[PeakName] = [
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

gales_advanced: list[PeakName] = [
    GALES_WALKERS_PILLAR,
    GALES_GREAT_GAOL,
    GALES_ELDENHORN,
    GALES_ST_HAELGA,
    GALES_YMIRS_SHADOW,
]

northern_expert: list[PeakName] = [
    NORTHERN_GREAT_BULWARK,
    NORTHERN_SOLEMN_TEMPEST,
]

alps_essentials: list[PeakName] = [
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

alps_greats: list[PeakName] = [
    ALPS_EINVALD_FALLS,
    ALPS_ALMATTR_DAM,
    ALPS_DUNDERHORN,
    ALPS_MHOR_DRUIM,
    ALPS_WELKIN_PASS,
]

alps_arctic: list[PeakName] = [
    ALPS_SEIGR_CRAEG,
    ALPS_ULLRS_CHASM,
    ALPS_GREAT_SILF,
    ALPS_TOWERING_VISIR,
    ALPS_ELDRIS_WALL,
    ALPS_MOUNT_MHORGORM,
]


class PoYRegion:
    id: int
    name: str

    def __init__(self, id: int, name: str) -> None:
        """
        Initializes a PoYRegion.

        :param id: The id of this region
        :param name: The name of this region
        """

        self.id = id
        self.name = name


class CabinRegion(PoYRegion):
    def __init__(self, id: int, name: CabinName) -> None:
        """
        Initializes a CabinRegion.

        :param id: The id of this cabin
        :param name: The name of this cabin
        """

        super().__init__(id, name.value)


class PeakRegion(PoYRegion):
    def __init__(self, id: int, name: PeakName) -> None:
        """
        Initializes a PeakRegion.

        :param id: The id of this peak
        :param name: The name of this peak
        """

        super().__init__(id, name.value)


class PoYRegions:
    handler: IDHandler

    # Cabins
    gales_cabin: CabinRegion
    northern_cabin: CabinRegion
    alps_cabin: CabinRegion

    # Great Gales
    gales_peaks: dict[PeakName, PeakRegion]
    gales_fundamental_peaks: dict[PeakName, PeakRegion]
    gales_intermediate_peaks: dict[PeakName, PeakRegion]
    gales_advanced_peaks: dict[PeakName, PeakRegion]

    # Nothern Range
    northern_peaks: dict[PeakName, PeakRegion]

    # Alps DLC
    alps_peaks: dict[PeakName, PeakRegion]
    alps_essentials_peaks: dict[PeakName, PeakRegion]
    alps_greats_peaks: dict[PeakName, PeakRegion]
    alps_arctic_peaks: dict[PeakName, PeakRegion]

    def __init__(self, handler: IDHandler) -> None:
        """
        Initializes the region information for all regions.

        :param handler: The ID handler for assigning IDs to regions
        """

        self.handler = handler

        self.gales_cabin = CabinRegion(
            handler.new_id(), CabinName.GALES
        )
        self.northern_cabin = CabinRegion(
            handler.new_id(), CabinName.NORTHERN
        )
        self.alps_cabin = CabinRegion(
            handler.new_id(), CabinName.ALPS
        )

        # Great Gales
        self.gales_fundamental_peaks = self.create_category(gales_fundamentals)
        self.gales_intermediate_peaks = self.create_category(gales_intermediate)
        self.gales_advanced_peaks = self.create_category(gales_advanced)

        self.gales_peaks = {
            **self.gales_fundamental_peaks,
            **self.gales_intermediate_peaks,
            **self.gales_advanced_peaks,
        }

        # Northern Range
        self.northern_peaks = self.create_category(northern_expert)

        # Alps DLC
        self.alps_essentials_peaks = self.create_category(alps_essentials)
        self.alps_great_peaks = self.create_category(alps_greats)
        self.alps_arctic_peaks = self.create_category(alps_arctic)

        self.alps_peaks = [
            **self.alps_essentials_peaks,
            **self.alps_greats_peaks,
            **self.alps_arctic_peaks,
        ]

    def create_category(
        self,
        peaks: list[PeakName]
    ) -> dict[PeakName, PeakRegion]:
        """
        Creates a dictionary mapping
        peak names to regions for a given category.

        :param handler: The handler used for assigning IDs
        :param peaks: The peak names within this region
        """

        return dict([
            (peak, PeakRegion(self.handler.new_id(), peak.value))
            for peak in peaks
        ])
