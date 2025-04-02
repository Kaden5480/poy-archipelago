from .id_handler import IDHandler

from .items import Items
from .locations import Locations
from .regions import Regions

class DataStore:
    """
    The container for all region, location, and item data.
    """

    __items: Items
    __locations: Locations
    __regions: Regions

    def __init__(self) -> None:
        """
        Initializes a DataStore object.
        """

        handler = IDHandler()

        self.__items = Items(handler)
        self.__locations = Locations(handler)
        self.__regions = Regions(handler)

    @property
    def items(self) -> Items:
        return self.__items

    @property
    def locations(self) -> Locations:
        return self.__locations

    @property
    def regions(self) -> Regions:
        return self.__regions
