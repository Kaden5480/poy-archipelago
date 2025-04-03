from typing import Callable

from worlds.AutoWorld import World
from BaseClasses import CollectionState

from .data.data_store import DataStore

from .names.items import *
from .names.regions import *


class Rules:
    """
    A helper for building a variety of
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
        item: ItemName,
        count: int = 1
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the provided item
        is currently accessible.

        :param item: The item to check
        :param count: The number of this item to check for
        :returns: The rule for checking this
        """

        return lambda state: state.has(item.value, self.player, count)

    def has_item_suffix(
        self,
        suffix: ItemSuffix,
        region: RegionName,
        count: int = 1
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the provided item suffix
        found in the given region is currently accessible.

        :param suffix: The suffix of the item
        :param region: The region this item is found in
        :param count: The number of this item to check for
        :returns: The rule for checking this
        """

        item = self.store.items.get_data_suffix(suffix, region)

        return lambda state: state.has(item.name, self.player, count)

    # Tool checks
    def has_crampons(
        self,
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether crampons are currently unlocked.

        :returns: The rule for checking this
        """

        return lambda state: self.has_item(state, ItemName.TOOL_CRAMPONS_6) \
                or self.has_item(state, ItemName.TOOL_CRAMPONS_10)

    def has_ice_axes(
        self,
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether ice axes are currently unlocked.

        :returns: The rule for checking this
        """

        return lambda state: self.has_item(state, ItemName.TOOL_ICE_AXES)

    # Event checks
    def has_all_photograph(
        self,
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether all of the picture pieces
        have been acquired.

        :returns: The rule for checking this
        """

        items = {
            BaseItemName.PICTURE_FRAGMENT.value: 4,
            BaseItemName.PICTURE_FRAME.value: 1,
        }

        return lambda state: state.has_all_counts(items, self.player)

    def has_all_artefacts(
        self,
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether all artefacts are unlocked.

        This is used for checking the event for unlocking
        all artefacts, which grants +5 ropes and
        infinite chalk and coffee.

        :returns: The rule for checking this
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

            BaseItemName.PICTURE_FRAGMENT.value: 4,
            BaseItemName.PICTURE_FRAME.value: 1,
        }

        return lambda state: state.has_all_counts(items, self.player)

    # Stamp checks
    def has_stamp(
        self,
        peak: PeakName
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the stamp for the given
        peak is currently accessible.

        :param state: The current state
        :param peak: The peak to check the stamp for
        :returns: The rule for checking this
        """

        data = self.store.items.get_data_stamp(peak)
        return lambda state: state.has(data.name, self.player)

    def has_stamps(
        self,
        category: type[PeakName],
        count: int
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether at least a given number of
        stamps are unlocked for a given category
        of peaks.

        :param category: The category to check stamps for
        :param count: The number of stamps to check for
        :returns: The rule for checking this
        """

        stamps = self.store.items.get_data_stamps(category)

        return lambda state: [
            state.has(data.name, self.player)
            for data in stamps
        ].count(True) >= count

    # Category unlock checks
    def unlocked_intermediate(
        self,
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the intermediate category
        was unlocked (15 fundamental stamps).

        :returns: The rule for checking this
        """

        return self.has_stamps(FundamentalsRegionName, 15)

    def unlocked_advanced(
        self,
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the advanced category
        was unlocked (5 intermediate stamps).

        :returns: The rule for checking this
        """

        return self.has_stamps(IntermediateRegionName, 5)

    def unlocked_expert(
        self,
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the expert category
        was unlocked (3 advanced stamps).

        :returns: The rule for checking this
        """

        return self.has_stamps(AdvancedRegionName, 3)

    def unlocked_greats(
        self,
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the alpine greats category
        was unlocked (10 essential stamps).

        :returns: The rule for checking this
        """

        return self.has_stamps(EssentialsRegionName, 10)

    def unlocked_arctic(
        self,
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the arduous and arctic category
        was unlocked (3 alpine greats stamps).

        :returns: The rule for checking this
        """

        return self.has_stamps(GreatsRegionName, 3)
