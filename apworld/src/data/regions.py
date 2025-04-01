from enum import IntEnum

from BaseClasses import CollectionState, \
                        Region

gales_fundamental_names = [
    "Greenhorn's Top",
    "Paltry Peak",
    "Old Mill",
    "Gray Gully",
    "The Lighthouse",
    "Old Man of Sjór",
    "Giant's Shelf",
    "Evergreen's End",
    "The Twins",
    "Old Grove's Skelf",
    "Hangman's Leap",
    "Land's End",
    "Old Langr",
    "Aldr Grotto",
    "Three Brothers",
    "Walter's Crag",
    "The Great Crevice",
    "Old Hagger",
    "Ugsome Stórr",
    "Wuthering Crest",
]

gales_intermediate_names = [
    "Porter's Boulder",
    "Jotunn's Thumb",
    "Old Skerry",
    "Hamarr Stone",
    "Giant's Nose",
    "Walter's Boulder",
    "Sundered Sons",
    "Old Weald's Boulder",
    "Leaning Spire",
    "Cromlech",
]

gales_advanced_names = [
    "Walker's Pillar",",
    "Great Gaol",
    "Eldenhorn",
    "St. Haelga",
    "Ymir's Shadow",
]

northern_expert_names = [
    "Great Bulwark",
    "Solemn Tempest",
]

alps_essentials_names = [
    "Tutor's Tower",
    "Stougr Boulder",
    "Mara's Arch",
    "Grainne Spire",
    "Great Bók Tree",
    "Treppenwald",
    "Castle of the Swan King",
    "Seaside Tribune",
    "Ivory Granites",
    "Old Rekkja",
    "Quietude",
    "Eljun's Folly",
]

alps_greats_names = [
    "Einvald Falls",
    "Almáttr Dam",
    "Dunderhorn",
    "Mhòr Druim",
    "Welkin Pass",
]

alps_arctic_names = [
    "Seigr Craeg",
    "Ullr's Chasm",
    "Great Silf",
    "Towering Vísir",
    "Eldris Wall",
    "Mount Mhòrgorm",
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

    def __init__(self, id: int, name: str, category; CabinCategory, *args, **kwargs) -> None:
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
    gales_cabin: CabinRegion
    northern_cabin: CabinRegion
    alps_cabin: CabinRegion

    gales_peaks: list[PeakRegion] = []
    northern_peaks: list[PeakRegion] = []
    alps_peaks: list[PeakRegion] = []

    def __init__(self, handler: IDHandler) -> None:
        """
        Initializes the region information for all regions.

        :param handler: The ID handler for assigning IDs to regions
        """

        self.gales_cabin = CabinRegion(
            handler.new_id(), "Great Gales Cabin", CabinCategory.Gales
        )
        self.northern_cabin = CabinRegion(
            handler.new_id(), "Northern Cabin", CabinCategory.Northern
        )
        self.alps_cabin = CabinRegion(
            handler.new_id(), "Alps Cabin", CabinCategory.Alps
        )

        # Great Gales
        gales_fundamental_peaks = [
            PeakRegion(handler.new_id(), name, PeakCategory.GalesFundamentals)
            for peak in gales_fundamental_names
        ]

        gales_intermediate_peaks = [
            PeakRegion(handler.new_id(), name, PeakCategory.GalesIntermediate)
            for peak in gales_intermediate_names
        ]

        gales_advanced_peaks = [
            PeakRegion(handler.new_id(), name, PeakCategory.GalesAdvanced)
            for peak in gales_advanced_names
        ]

        self.gales_peaks = [
            *gales_fundamental_peaks,
            *gales_intermediate_peaks,
            *gales_advanced_peaks,
        ]

        # Northern Range
        self.northern_peaks = [
            PeakRegion(handler.new_id(), name, PeakCategory.NorthernExpert)
            for peak in northern_expert_names
        ]

        # Alps DLC
        alps_essentials_peaks = [
            PeakRegion(handler.new_id(), name, PeakCategory.AlpsEssentials)
            for peak in alps_essentials_names
        ]

        alps_greats_peaks = [
            PeakRegion(handler.new_id(), name, PeakCategory.AlpsGreats)
            for peak in alps_greats_names
        ]

        alps_arctic_peaks = [
            PeakRegion(handler.new_id(), name, PeakCategory.AlpsArctic)
            for peak in alps_arctic_names
        ]

        self.alps_peaks = [
            *alps_essentials_peaks,
            *alps_greats_peaks,
            *alps_arctic_peaks,
        ]

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
        self.create_peak_conns(self.gales_cabin, self.gales_peaks)
        self.create_peak_conns(self.northern_cabin, self.northern_peaks)
        self.create_peak_conns(self.alps_cabin, self.alps_peaks)

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
