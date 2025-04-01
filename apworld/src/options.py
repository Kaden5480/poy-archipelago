from Options import PerGameCommonOptions
from Options import Choice, \
                    DeathLink, \
                    Toggle

class EnableDLCOption(Toggle):
    """
    Whether DLC peaks and collectables should be available for randomisation.

    This requires you to own the Alps DLC.
    """

    display_name = "Enable DLC"

## Items ##

class StartingBarometerOption(Toggle):
    """
    Whether you should start with the Barometer and Map.
    """

    display_name = "Start With Barometer and Map"

class StartingHandsOption(Choice):
    """
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

class RandomiseLevelsOption(Toggle):
    """
    Whether the entrances and exits to levels should be randomised.
    """

    display_name = "Randomise Levels"

@dataclass
class PeaksOptions(PerGameCommonOptions):
    death_link: DeathLink

    enable_dlc: EnableDLCOption

    # Items
    starting_barometer: StartingBarometerOption
    starting_hands: StartingHandsOption

    # Regions
    require_crampons: RequireCramponsOption
    randomise_levels: RandomiseLevelsOption
