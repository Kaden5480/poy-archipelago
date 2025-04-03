from dataclasses import dataclass

from Options import PerGameCommonOptions
from Options import Choice, \
                    DeathLink, \
                    Toggle

class EnableFundamentalsOption(Toggle):
    """
    Whether fundamental peaks and collectables should be available for randomisation.
    """

    display_name = "Enable Fundamentals"

class EnableIntermediateOption(Toggle):
    """
    Whether intermediate peaks and collectables should be available for randomisation.
    """

    display_name = "Enable Intermediate"

class EnableAdvancedOption(Toggle):
    """
    Whether advanced peaks and collectables should be available for randomisation.
    """

    display_name = "Enable Advanced"

class EnableExpertOption(Toggle):
    """
    Whether expert peaks and collectables should be available for randomisation.
    """

    display_name = "Enable Expert"

class EnableEssentialsOption(Toggle):
    """
    Whether essentials peaks and collectables should be available for randomisation.

    This requires you to own the DLC.
    """

    display_name = "Enable Essentials"

class EnableGreatsOption(Toggle):
    """
    Whether alpine greats peaks and collectables should be available for randomisation.

    This requires you to own the DLC.
    """

    display_name = "Enable Alpine Greats"

class EnableArcticOption(Toggle):
    """
    Whether arctic and arduous peaks and collectables should be available for randomisation.

    This requires you to own the DLC.
    """

    display_name = "Enable Arduous and Arctic"


## Goals ##

class GoalOption(Choice):
    """
    TODO: Implement this
    What the goal for victory should be.
    """

    display_name         = "Goal"
    option_oas_member    = 0
    option_oas_president = 1
    option_all_peaks     = 2
    option_everything    = 3
    default              = 0


## Items ##

class StartingBarometerOption(Toggle):
    """
    Whether you should start with the Barometer and Map.
    """

    display_name = "Start With Barometer and Map"


class StartingHandsOption(Choice):
    """
    TODO: Implement this
    Which hand(s) to start with.

    - **Both Hands:** Start with both hands.
    - **Left Hand:** Start with only your left hand.
    - **Right Hand:** Start with only your right hand.
    - **No Hands:** Start with no hands.
    """

    display_name = "Starting Hands"
    option_both = 0
    option_left = 1
    option_right = 2
    option_neither = 3
    default = 0


## Regions ##

class RequireCramponsOption(Toggle):
    """
    Require crampons to access Expert/Arduous and Arctic peaks.
    """

    display_name = "Require Crampons"


## Randomisation ##

class RandomiseLevelsOption(Toggle):
    """
    TODO: Implement this
    Whether the entrances and exits to levels should be randomised.
    """

    display_name = "Randomise Levels"


class RandomiseItemsOption(Toggle):
    """
    Whether the items should be randomised.
    """

    display_name = "Randomise Items"


class RandomiseItemsWeightedOption(Toggle):
    """
    Whether items significant to progression should
    be more likely to end up where other progression items would be.
    """

    display_name = "Weighted Item Randomisation"


class RandomiseStampsOption(Toggle):
    """
    Whether stamps should be randomised.
    """

    display_name = "Randomise Stamps"

class NoLogicOption(Toggle):
    """
    [Low] TODO: Implement this
    Whether all randomisation rules should be thrown out the window.
    """

    display_name = "No Logic"


@dataclass
class PeaksOptions(PerGameCommonOptions):
    death_link: DeathLink

    enable_fundamentals: EnableFundamentalsOption
    enable_intermediate: EnableIntermediateOption
    enable_advanced: EnableAdvancedOption
    enable_expert: EnableExpertOption
    enable_essentials: EnableEssentialsOption
    enable_greats: EnableGreatsOption
    enable_arctic: EnableArcticOption

    # Goal
    goal: GoalOption

    # Items
    starting_barometer: StartingBarometerOption
    starting_hands: StartingHandsOption

    # Regions
    require_crampons: RequireCramponsOption

    # Randomisation
    randomise_levels: RandomiseLevelsOption
    randomise_items: RandomiseItemsOption
    randomise_items_weighted: RandomiseItemsWeightedOption
    randomise_stamps: RandomiseStampsOption
    no_logic: NoLogicOption
