from worlds.AutoWorld import World
from BaseClasses import CollectionState

from .data.data_store import DataStore

from .names.items import *
from .names.regions import *


class Rules:
    """
    A helper for checking a variety of
    different rules.
    """

    __store: DataStore
    __world: World

    def __init__(
        self,
        store: DataStore,
        world: World
    ) -> None:
        """
        Initializes a Rules object.

        :param store: The data store containing all data
        :param world: The current world for checking rules against
        """

        self.__store = store
        self.__world = world

    @property
    def store(self) -> DataStore:
        return self.__store

    @property
    def player(self) -> int:
        return self.__world.player

    @property
    def world(self) -> World:
        return self.__world

    # Basic checks
    def has_item(
        self,
        state: CollectionState,
        item: ItemName,
        count: int = 1
    ) -> bool:
        """
        Checks whether the provided item
        is currently accessible.

        :param state: The current state
        :param item: The item to check
        :param count: The number of this item to check for
        :returns: True if this item is accessible, False otherwise
        """

        return state.has(item.value, self.player, count)

    def has_item_suffix(
        self,
        state: CollectionState,
        suffix: ItemSuffix,
        region: RegionName,
        count: int = 1
    ) -> bool:
        """
        Checks whether the provided item suffix
        found in the given region is currently accessible.

        :param state: The current state
        :param suffix: The suffix of the item
        :param region: The region this item is found in
        :param count: The number of this item to check for
        :returns: True if this item is accessible, False otherwise
        """

        item = self.store.items.get_data_suffix(suffix, region)
        return state.has(item.name, self.player, count)

    # Tool checks
    def has_crampons(
        self,
        state: CollectionState
    ) -> bool:
        """
        Checks whether crampons are currently unlocked.

        :param state: The current state
        :returns: True if they are, False otherwise
        """

        return self.has_item(state, ItemName.TOOL_CRAMPONS_6) \
                or self.has_item(state, ItemName.TOOL_CRAMPONS_10)

    def has_ice_axes(
        self,
        state: CollectionState
    ) -> bool:
        """
        Checks whether ice axes are currently unlocked.

        :param state: The current state
        :returns: True if they are, False otherwise
        """

        return self.has_item(state, ItemName.TOOL_ICE_AXES)

    # Event checks
    def has_all_photograph(
        self,
        state: CollectionState
    ) -> bool:
        """
        Checks whether all of the picture pieces
        have been acquired.

        This is used for checking the event for
        unlocking double length rope (and also as
        part of collecting all artefacts).

        :param state: The current state
        :returns: True if they have been, False otherwise
        """

        items = {
            BaseItemName.PICTURE_FRAGMENT.value: 4,
            BaseItemName.PICTURE_FRAME.value: 1,
        }

        return state.has_all_counts(items, self.player)

    def has_all_artefacts(
        self,
        state: CollectionState
    ) -> bool:
        """
        Checks whether all artefacts are unlocked.

        This is used for checking the event for unlocking
        all artefacts, which grants +5 ropes and
        infinite chalk and coffee.

        :param state: The current state
        :returns: True if they have been, False otherwise
        """

        items = {
            BaseItemName.HAT_1.value: 1,
            BaseItemName.HAT_2.value: 1,
            BaseItemName.SHOE.value: 1,
            BaseItemName.SLEEPING_BAG.value: 1,
            BaseItemName.SAFETY_HELMET.value: 1,
            BaseItemName.BACKPACK.value: 1,
            BaseItemName.SHOVEL.value: 1,
            BaseItemName.STATUE_FUNDAMENTALS.value: 1,
            BaseItemName.STATUE_INTERMEDIATE.value: 1,
            BaseItemName.STATUE_ADVANCED.value: 1,
            BaseItemName.CHALK_2.value: 2,
            BaseItemName.COFFEE_2.value: 2,
        }

        return self.has_all_photograph() \
                and state.has_all_counts(items, self.player)

    # Stamp checks
    def has_stamp(
        self,
        state: CollectionState,
        peak: PeakName
    ) -> bool:
        """
        Checks whether the stamp for the given
        peak is currently accessible.

        :param state: The current state
        :param peak: The peak to check the stamp for
        """

        data = self.store.items.get_data_stamp(peak)
        return state.has(data.name, self.player)

    def has_stamps(
        self,
        state: CollectionState,
        category: type[PeakName],
        count: int
    ) -> bool:
        """
        Checks whether at least a given number of
        stamps are unlocked for a given category
        of peaks.

        :param state: The current state
        :param category: The category to check stamps for
        :param count: The number of stamps to check for
        """

        return [
            state.has(data.name, self.player)
            for data in self.store.items.get_data_stamps(category)
        ].count(True) >= count

    # Category unlock checks
    def unlocked_intermediate(
        self,
        state: CollectionState
    ) -> bool:
        """
        Checks whether the intermediate category
        was unlocked (15 fundamental stamps).

        :param state: The current state
        :returns: True if it has been, False otherwise
        """

        return self.has_stamps(
            state,
            FundamentalsRegionName,
            15
        )

    def unlocked_advanced(
        self,
        state: CollectionState
    ) -> bool:
        """
        Checks whether the advanced category
        was unlocked (5 intermediate stamps).

        :param state: The current state
        :returns: True if it has been, False otherwise
        """

        return self.has_stamps(
            state,
            IntermediateRegionName,
            5
        )

    def unlocked_expert(
        self,
        state: CollectionState
    ) -> bool:
        """
        Checks whether the expert category
        was unlocked (3 advanced stamps).

        :param state: The current state
        :returns: True if it has been, False otherwise
        """

        return self.has_stamps(
            state,
            AdvancedRegionName,
            3
        )

    def unlocked_greats(
        self,
        state: CollectionState
    ) -> bool:
        """
        Checks whether the alpine greats category
        was unlocked (10 essential stamps).

        :param state: The current state
        :returns: True if it has been, False otherwise
        """

        return self.has_stamps(
            state,
            EssentialsRegionName,
            10
        )

    def unlocked_arctic(
        self,
        state: CollectionState
    ) -> bool:
        """
        Checks whether the arduous and arctic category
        was unlocked (3 alpine greats stamps).

        :param state: The current state
        :returns: True if it has been, False otherwise
        """

        return self.has_stamps(
            state,
            GreatsRegionName,
            3
        )
