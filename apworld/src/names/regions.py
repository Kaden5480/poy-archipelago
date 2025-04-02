from enum import StrEnum

class CabinRegionName(StrEnum):
    """
    The names of all cabin regions.
    """

    GALES    = "Great Gales Cabin"
    NORTHERN = "Northern Cabin"
    ALPS     = "Alps Cabin"


class FundamentalsRegionName(StrEnum):
    """
    The names of all fundamentals peaks.
    """

    GREENHORNS_TOP    = "Greenhorn's Top"
    PALTRY_PEAK       = "Paltry Peak"
    OLD_MILL          = "Old Mill"
    GRAY_GULLY        = "Gray Gully"
    THE_LIGHTHOUSE    = "The Lighthouse"
    OLD_MAN_OF_SJOR   = "Old Man of Sjór"
    GIANTS_SHELF      = "Giant's Shelf"
    EVERGREENS_END    = "Evergreen's End"
    THE_TWINS         = "The Twins"
    OLD_GROVES_SKELF  = "Old Grove's Skelf"
    HANGMANS_LEAP     = "Hangman's Leap"
    LANDS_END         = "Land's End"
    OLD_LANGR         = "Old Langr"
    ALDR_GROTTO       = "Aldr Grotto"
    THREE_BROTHERS    = "Three Brothers"
    WALTERS_CRAG      = "Walter's Crag"
    THE_GREAT_CREVICE = "The Great Crevice"
    OLD_HAGGER        = "Old Hagger"
    UGSOME_STORR      = "Ugsome Stórr"
    WUTHERING_CREST   = "Wuthering Crest"


class IntermediateRegionName(StrEnum):
    """
    The names of all intermediate peaks.
    """

    PORTERS_BOULDER    = "Porter's Boulder"
    JOTUNNS_THUMB      = "Jotunn's Thumb"
    OLD_SKERRY         = "Old Skerry"
    HAMARR_STONE       = "Hamarr Stone"
    GIANTS_NOSE        = "Giant's Nose"
    WALTERS_BOULDER    = "Walter's Boulder"
    SUNDERED_SONS      = "Sundered Sons"
    OLD_WEALDS_BOULDER = "Old Weald's Boulder"
    LEANING_SPIRE      = "Leaning Spire"
    CROMLECH           = "Cromlech"


class AdvancedRegionName(StrEnum):
    """
    The names of all advanced peaks.
    """

    WALKERS_PILLAR = "Walker's Pillar"
    GREAT_GAOL     = "Great Gaol"
    ELDENHORN      = "Eldenhorn"
    ST_HAELGA      = "St. Haelga"
    YMIRS_SHADOW   = "Ymir's Shadow"


class ExpertRegionName(StrEnum):
    """
    The names of all expert peaks.
    """

    NORTHERN_GREAT_BULWARK  = "Great Bulwark"
    NORTHERN_SOLEMN_TEMPEST = "Solemn Tempest"


class EssentialsRegionName(StrEnum):
    """
    The names of all essentials peaks.
    """

    TUTORS_TOWER            = "Tutor's Tower"
    STOUGR_BOULDER          = "Stougr Boulder"
    MARAS_ARCH              = "Mara's Arch"
    GRAINNE_SPIRE           = "Grainne Spire"
    GREAT_BOK_TREE          = "Great Bók Tree"
    TREPPENWALD             = "Treppenwald"
    CASTLE_OF_THE_SWAN_KING = "Castle of the Swan King"
    SEASIDE_TRIBUNE         = "Seaside Tribune"
    IVORY_GRANITES          = "Ivory Granites"
    OLD_REKKJA              = "Old Rekkja"
    QUIETUDE                = "Quietude"
    ELJUNS_FOLLY            = "Eljun's Folly"


class GreatsRegionName(StrEnum):
    """
    The names of all alpine greats peaks.
    """

    EINVALD_FALLS = "Einvald Falls"
    ALMATTR_DAM   = "Almáttr Dam"
    DUNDERHORN    = "Dunderhorn"
    MHOR_DRUIM    = "Mhòr Druim"
    WELKIN_PASS   = "Welkin Pass"


class ArcticRegionName(StrEnum):
    """
    The names of all arduous and arctic peaks.
    """

    SEIGR_CRAEG    = "Seigr Craeg"
    ULLRS_CHASM    = "Ullr's Chasm"
    GREAT_SILF     = "Great Silf"
    TOWERING_VISIR = "Towering Vísir"
    ELDRIS_WALL    = "Eldris Wall"
    MOUNT_MHORGORM = "Mount Mhòrgorm"


# Different groups of categories (for each cabin)
GalesPeakName = FundamentalsRegionName \
        | IntermediateRegionName \
        | AdvancedRegionName

NorthernPeakName = ExpertRegionName
AlpsPeakName = EssentialsRegionName \
        | GreatsRegionName \
        | ArcticRegionName

# Base and DLC peak groupings
BasePeakName = GalesPeakName | NorthernPeakName
DlcPeakName = AlpsPeakName

# Everything
RegionName = CabinName | BasePeakName | DlcPeakName
