from enum import IntEnum, \
                 StrEnum

from BaseClasses import CollectionState, \
                        Region

class PeakNames(StrEnum):
    CABIN_GALES    = "Great Gales Cabin"
    CABIN_NORTHERN = "Northern Cabin"
    CABIN_ALPS     = "Alps Cabin"

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


gales_fundamentals: list[PeakNames] = [
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

gales_intermediate: list[PeakNames] = [
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

gales_advanced: list[PeakNames] = [
    GALES_WALKERS_PILLAR,
    GALES_GREAT_GAOL,
    GALES_ELDENHORN,
    GALES_ST_HAELGA,
    GALES_YMIRS_SHADOW,
]

northern_expert: list[PeakNames] = [
    NORTHERN_GREAT_BULWARK,
    NORTHERN_SOLEMN_TEMPEST,
]

alps_essentials: list[PeakNames] = [
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

alps_greats: list[PeakNames] = [
    ALPS_EINVALD_FALLS,
    ALPS_ALMATTR_DAM,
    ALPS_DUNDERHORN,
    ALPS_MHOR_DRUIM,
    ALPS_WELKIN_PASS,
]

alps_arctic: list[PeakNames] = [
    ALPS_SEIGR_CRAEG,
    ALPS_ULLRS_CHASM,
    ALPS_GREAT_SILF,
    ALPS_TOWERING_VISIR,
    ALPS_ELDRIS_WALL,
    ALPS_MOUNT_MHORGORM,
]

class CabinCategory(IntEnum):
    Gales = 0
    Northern = 1
    Alps = 2


class PeakCategory(IntEnum):
    GalesFundamentals = 0
    GalesIntermediate = 1
    GalesAdvanced = 2
    NorthernExpert = 3
    AlpsEssentials = 4
    AlpsGreats = 5
    AlpsArctic = 6


class PoYRegion(Region):
    id: int
    name: str
    regions: list[PoYRegion]
    connections: list[Entrance]

    def __init__(self, id: int, name: str, *args, **kwargs) -> None:
        """
        Initializes a PoYRegion.

        :param id: The id of this region
        :param name: The name of this region
        :param args: Arguments which can be passed to Region
        :param kwargs: Keyword arguments which can be passed to Region
        """

        self.id = id
        self.name = name
        self.regions = []
        self.connections = []

        super().__init__(*args, **kwargs)

    def can_access(self, state: CollectionState) -> bool:
        """
        Determines whether this region can be accessed, given
        the current state.

        :param state: The current state to check against
        """

        return True

    def link_to(self, region: PoYRegion, name: str = "") -> None:
        """
        Links this region to another region.

        :param region: The region which this region links to
        :param name: The name to assign to the created connection
        """

        regions.append(region)

        if len(name) < 1:
            name = f"{self.name} -> {region} connection"

        connection: Entrance = self.connect(
            region, name,
            lambda state: region.can_access(state)
        )

        connections.append(connection)


# Cabin regions don't need to implement anything extra
class CabinRegion(PoYRegion):
    category: CabinCategory

    def __init__(self, id: int, name: str, category: CabinCategory, *args, **kwargs) -> None:
        """
        Initializes a CabinRegion.

        :param id: The id of this cabin
        :param name: The name of this cabin
        :param category: The category (book) this cabin region is from
        :param args: Arguments which can be passed to Region
        :param kwargs: Keyword arguments which can be passed to Region
        """

        self.category = category
        super().__init__(id, name, *args, **kwargs)

    def can_access(self, state: CollectionState) -> bool:
        """
        Determines whether this cabin can be accessed, given
        the current state.

        :param state: The current state to check against
        """

        return True


class PeakRegion(PoYRegion):
    category: PeakCategory

    def __init__(self, id: int, name: str, category: PeakCategory, *args, **kwargs) -> None:
        """
        Initializes a PeakRegion.

        :param id: The id of this peak
        :param name: The name of this peak
        :param category: The category (book) this peak region is from
        :param args: Arguments which can be passed to Region
        :param kwargs: Keyword arguments which can be passed to Region
        """

        self.category = category
        super().__init__(id, name, *args, **kwargs)

    def can_access(self, state: CollectionState) -> bool:
        """
        Determines whether this peak can be accessed.

        :param state: The current state to check against
        """

        return state.has(f"{category.name} Book")

    def link_to(self, cabin: CabinRegion, next_peak: PeakRegion | None) -> None:
        """
        Links a peak to its next peak (if there is one)
        and back to the cabin through the Stamper.

        :param cabin: The cabin which can be returned to from this peak
        :param next_peak: The peak which comes after this one, or None
        """

        super().link_to(cabin, f"{self.name} return to cabin")

        if next_peak is None:
            return

        super().link_to(next_peak, f"{next_peak.name} -> {self.name} through stamper")


class PoYRegions:
    handler: IDHandler

    gales_cabin: CabinRegion
    northern_cabin: CabinRegion
    alps_cabin: CabinRegion

    gales_peaks: dict[PeakNames, PeakRegion]
    northern_peaks: dict[PeakNames, PeakRegion]
    alps_peaks: dict[PeakNames, PeakRegion]

    def __init__(self, handler: IDHandler) -> None:
        """
        Initializes the region information for all regions.

        :param handler: The ID handler for assigning IDs to regions
        """

        self.handler = handler

        self.gales_cabin = CabinRegion(
            handler.new_id(), PeakNames.CABIN_GALES.value, CabinCategory.Gales
        )
        self.northern_cabin = CabinRegion(
            handler.new_id(), PeakNames.CABIN_NORTHERN.value, CabinCategory.Northern
        )
        self.alps_cabin = CabinRegion(
            handler.new_id(), PeakNames.CABIN_ALPS.value, CabinCategory.Alps
        )

        # Great Gales
        gales_fundamental_peaks = self.create_category(PeakCategory.GalesFundamentals, gales_fundamentals)
        gales_intermediate_peaks = self.create_category(PeakCategory.GalesIntermediate, gales_intermediate)
        gales_advanced_peaks = self.create_category(PeakCategory.GalesAdvanced, gales_advanced)

        self.gales_peaks = {
            **gales_fundamental_peaks,
            **gales_intermediate_peaks,
            **gales_advanced_peaks,
        }

        # Northern Range
        self.northern_peaks = self.create_category(PeakCategory.NorthernExpert, northern_expert)

        # Alps DLC
        alps_essentials_peaks = self.create_category(PeakCategory.AlpsEssentials, alps_essentials)
        alps_great_peaks = self.create_category(PeakCategory.AlpsGreats, alps_greats)
        alps_arctic_peaks = self.create_category(PeakCategory.AlpsArctic, alps_arctic)

        self.alps_peaks = [
            **alps_essentials_peaks,
            **alps_greats_peaks,
            **alps_arctic_peaks,
        ]

    def create_category(
        self,
        category: PeakCategory,
        peaks: list[PeakNames]
    ) -> dict[PeakNames, PeakRegion]:
        """
        Creates a dictionary mapping
        peak names to regions for a given category.

        :param handler: The handler used for assigning IDs
        :param peaks: The peak names under a given category
        :param category: The category these peaks are within
        """

        return dict([
            (peak, PeakRegion(self.handler.new_id(), peak.value, category))
            for peak in peaks
        ])

    def create_conns() -> None:
        """
        Creates connections between all regions.
        """

        # Tickets to northern range and alps DLC
        self.gales_cabin.link_to(self.northern_cabin)
        self.gales_cabin.link_to(self.alps_cabin)

        # Tickets to gales and alps DLC
        self.northern_cabin.link_to(self.gales_cabin)
        self.northern_cabin.link_to(self.alps_cabin)

        # Ticket to gales
        self.alps_cabin.link_to(self.gales_cabin)

        # Link cabins to peaks
        self.create_peak_conns(self.gales_cabin, list(self.gales_peaks.values))
        self.create_peak_conns(self.northern_cabin, list(self.northern_peaks.values))
        self.create_peak_conns(self.alps_cabin, list(self.alps_peaks))

    def create_peak_conns(
        cabin: CabinRegion,
        peaks: list[PeakRegion]
    ) -> None:
        """
        Creates connections between
        cabins and their corresponding peaks.

        :param cabin: The cabin for the list of peaks
        :param peaks: The list of peaks which can be accessed
                      from the provided cabin
        """

        peaks_len = len(peaks)
        for i, peak in enumerate(peaks):
            # The link from the cabin to the peak
            # is through the bag on the peak
            cabin.link_to(peak)

            # The last peak in the list can't access
            # the next peak from the stamper, as there isn't
            # a next peak
            next_peak: PeakRegion | None = None
            if i < peaks_len - 1:
                next_peak = peaks[i + 1]

            # The links to the next peak and back to
            # the cabin through the stamper
            peak.link_to(cabin, next_peak)
