from typing import Callable

from worlds.AutoWorld import World
from BaseClasses import CollectionState

from .data.data_store import DataStore

from .names.items import *
from .names.locations import *
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

    # Allow more easily adding rules
    def add_loc_rule(
        self,
        location: LocationName,
        rule: Callable[[CollectionState], bool]
    ) -> None:
        """
        Adds a rule to a location, if it exists.

        :param location: The location to add a rule for
        :param rule: The rule to add for accessing this location
        """

        if (loc := self.world.poy_get_location(location)) is not None:
            loc.poy_add_rule(rule)

    def add_region_rule(
        self,
        region_a: RegionName,
        region_b: RegionName,
        rule: Callable[[CollectionState], bool]
    ) -> None:
        """
        Adds a rule to go from region_a to region_b.

        :param region_a: The beginning region
        :param region_b: The end region
        :param rule: The rule for whether region_b
                     can be accessed from region_a
        """

        if (reg_a := self.world.poy_get_region(region_a)) is not None:
            reg_a.poy_add_rule(region_b, rule)

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

        try:
            item.value

        except:
            print(f"{item} has no .value")

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

    def has_any(
        self,
        items: list[ItemName],
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether any of the provided items
        are currently accessible.

        :param items: The items to check
        :returns: The rule for checking this
        """

        names = list(map(str, items))
        return lambda state: state.has_any(
            names, self.player
        )

    # Tool checks
    def has_crampons(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the player has crampons.

        :returns: The rule for checking this
        """

        return lambda state: self.has_item(BaseItemName.TOOL_CRAMPONS_6)(state) \
                or self.has_item(BaseItemName.TOOL_CRAMPONS_10)(state)

    def has_ice_axes(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the player has ice axes.

        :returns: The rule for checking this
        """

        return self.has_item(BaseItemName.TOOL_ICE_AXES)

    def has_pocketwatch(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the player has the pocketwatch.
        """

        return self.has_item(BaseItemName.TOOL_POCKETWATCH)

    # Event checks
    def has_all_photograph(
        self
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
        self
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

    # Specific tool checks
    def unlocked_barometer(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the barometer can be unlocked.

        :returns: The rule to check this
        """

        items = [
            BaseItemName.HAT_1,
            BaseItemName.HAT_2,
            BaseItemName.SHOE,
            BaseItemName.SLEEPING_BAG,
            BaseItemName.SAFETY_HELMET,
            BaseItemName.BACKPACK,
            BaseItemName.SHOVEL,
            BaseItemName.PICTURE_FRAGMENT,
            BaseItemName.COFFEE_2,
        ]

        has_stamps = self.has_stamps(FundamentalsRegionName, 5)
        has_any_item = self.has_any(items)

        return lambda state: has_stamps(state) and has_any_item(state)

    def unlocked_chalk(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the chalk bag can be unlocked.

        :returns: The rule to check this
        """

        has_stamps = self.has_stamps(FundamentalsRegionName, 18)

        return lambda state: self.unlocked_advanced()(state) \
                or has_stamps(state)

    def unlocked_coffee(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether coffee (the tool) can be unlocked.

        :returns: The rule to check this
        """

        twins = self.has_stamp(FundamentalsRegionName.THE_TWINS)
        has_coffee = self.has_item(BaseItemName.COFFEE_2)

        return lambda state: twins(state) or has_coffee(state)

    def unlocked_crampons_6(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the 6 point crampons can be unlocked.

        :returns: The rule to check this
        """

        old_groves = self.has_stamp(
            FundamentalsRegionName.OLD_GROVES_SKELF
        )
        enough_peaks = self.has_stamps(
            FundamentalsRegionName, 10
        )

        return lambda state: old_groves(state) or enough_peaks(state)

    def unlocked_crampons_10(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the 10 point crampons can be unlocked.

        :returns: The rule to check this
        """

        advanced = self.has_stamps(AdvancedRegionName, 3)
        base_peaks = self.has_stamps_base(22)

        return lambda state: advanced(state) and base_peaks(state)

    def unlocked_ice_axes(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether ice axes can be unlocked.

        :returns: The rule to check this
        """

        ymirs = self.has_stamp(AdvancedRegionName.YMIRS_SHADOW)
        advanced = self.has_stamps(AdvancedRegionName, 3)

        return lambda state: ymirs(state) or advanced(state)

    def unlocked_phonograph(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the phonograph can be unlocked.

        :returns: The rule to check this
        """

        paltry = self.has_stamp(FundamentalsRegionName.PALTRY_PEAK)
        fundamentals = self.has_stamps(FundamentalsRegionName, 2)

        return lambda state: paltry(state) or fundamentals(state)

    def unlocked_pipe(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the pipe can be unlocked.

        TODO: implement this and time attack stuff

        :returns: The rule to check this
        """

        return self.has_time_attacks(
            BaseItemName.TIME_ATTACK_INTERMEDIATE, 10
        )

    def unlocked_pocketwatch(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the pocketwatch can be unlocked.

        :returns: The rule to check this
        """

        return self.has_stamps(IntermediateRegionName, 2)

    def unlocked_rope(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether rope can be unlocked.

        :returns: The rule to check this
        """

        gray_gully = self.has_stamp(
            FundamentalsRegionName.GRAY_GULLY
        )
        fundamentals = self.has_stamps(
            FundamentalsRegionName, 3
        )

        return lambda state: gray_gully(state) \
                or fundamentals(state)

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

    def has_stamps_base(
        self,
        count: int
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the player has unlocked at least
        `count` base game stamps.

        :param count: The number of base game stamps to check for
        :returns: The rule for checking this
        """

        stamps = self.store.items.get_data_stamps_base()

        return lambda state: [
            state.has(data.name, self.player)
            for data in stamps
        ].count(True) >= count

    # Time attack checks
    def has_time_attacks(
        self,
        time_attack: ItemName,
        count: int
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the player has achieved
        at least `count` time attacks in a given category.

        :param time_attack: The time attack category to check
        :param count: The number of time attacks to check for
        """

        return self.has_item(time_attack, count)

    # Category unlock checks
    def unlocked_intermediate(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the intermediate category
        was unlocked (15 fundamental stamps).

        :returns: The rule for checking this
        """

        return self.has_stamps(FundamentalsRegionName, 15)

    def unlocked_advanced(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the advanced category
        was unlocked (5 intermediate stamps).

        :returns: The rule for checking this
        """

        return self.has_stamps(IntermediateRegionName, 5)

    def unlocked_expert(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the expert category
        was unlocked (3 advanced stamps).

        :returns: The rule for checking this
        """

        return self.has_stamps(AdvancedRegionName, 3)

    def unlocked_greats(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the alpine greats category
        was unlocked (10 essential stamps).

        :returns: The rule for checking this
        """

        return self.has_stamps(EssentialsRegionName, 10)

    def unlocked_arctic(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether the arduous and arctic category
        was unlocked (3 alpine greats stamps).

        :returns: The rule for checking this
        """

        return self.has_stamps(GreatsRegionName, 3)

    # All peaks unlocks
    def all_fundamentals(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether all 20 fundamentals have been completed.

        :returns: The rule for checking this
        """

        return self.has_stamps(FundamentalsRegionName, 20)

    def all_intermediate(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether all 10 intermediates have been completed.
        """

        return self.has_stamps(IntermediateRegionName, 10)

    def all_advanced(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether all 5 advanced have been completed.
        """

        return self.has_stamps(AdvancedRegionName, 5)

    def all_expert(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether all 2 expert peaks have been completed.
        """

        return self.has_stamps(ExpertRegionName, 2)

    def all_base_peaks(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether all base game stamps have been collected.
        """

        return lambda state: self.all_fundamentals()(state) \
                and self.all_intermediate()(state) \
                and self.all_advanced()(state) \
                and self.all_expert()(state)

    # All peaks time attacks
    def all_fundamentals_time_attack(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether all time attacks have been
        unlocked in the fundamentals.
        """

        return self.has_time_attacks(
            BaseItemName.TIME_ATTACK_FUNDAMENTALS,
            20
        )

    def all_intermediate_time_attack(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether all time attacks have been
        unlocked in the intermediate category.
        """

        return self.has_time_attacks(
            BaseItemName.TIME_ATTACK_INTERMEDIATE,
            10
        )

    def all_advanced_time_attack(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether all time attacks have been
        unlocked in the advanced category.
        """

        return self.has_time_attacks(
            BaseItemName.TIME_ATTACK_ADVANCED,
            5
        )

    def all_base_time_attacks(
        self
    ) -> Callable[[CollectionState], bool]:
        """
        Checks whether all time attacks in the base game
        have been beaten
        """

        return lambda state: self.all_fundamentals_time_attack()(state) \
                and self.all_intermediate_time_attack()(state) \
                and self.all_advanced_time_attack()(state)
