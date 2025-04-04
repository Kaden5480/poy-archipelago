from typing import Iterator, \
                   cast

from .id_handler import IDHandler

from ..names.regions import *

class RegionData:
    __id: int
    __name: str

    def __init__(self, id: int, name: str) -> None:
        """
        Initializes a RegionData object.

        :param id: The ID of this region
        :param name: The name of this region
        """

        self.__id = id
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name


class Regions:
    __handler: IDHandler
    __regions: dict[str, RegionData]

    def __init__(self, handler: IDHandler) -> None:
        """
        Initializes a Regions object.

        :param handler: The handler to assign IDs with
        """

        self.__handler = handler
        self.__regions = {}

        self.__create_all()

    def __iter__(self) -> Iterator[RegionData]:
        """
        Supports iterating over this object to
        get data for all regions.
        """

        return iter(self.__regions.values())

    def get_data_str(
        self,
        name: str
    ) -> RegionData:
        """
        Gets the region data for a given region.

        :param name: The name of the region to get data for
        :returns: The region's data
        """

        return self.__regions[name]

    def get_data(
        self,
        name: RegionName
    ) -> RegionData:
        """
        Gets the region data for a given region.

        :param name: The name of the region to get data for
        :returns: The region's data
        """

        return self.get_data_str(name.value)

    def get_data_for_category(
        self,
        category: type[RegionName]
    ) -> list[RegionData]:
        """
        Gets all region data in a given category

        :param category: The category to get region data for
        :returns: A list of all region data for this category
        """

        return [self.get_data(cast(RegionName, peak)) for peak in category]

    def __create_data(
        self,
        region: RegionName
    ) -> None:
        """
        Creates the data for a region.
        """

        self.__regions[region.value] = RegionData(
            self.__handler.new_id(), region.value
        )

    def __create_category(
        self,
        category: type[RegionName]
    ) -> None:
        """
        Creates region data for all regions
        in a given category.

        :param category: The category to create region data for
        """

        for region in category:
            self.__create_data(cast(RegionName, region))

    def __create_all(self) -> None:
        """
        Creates all region data.
        """

        self.__create_category(CabinRegionName)
        self.__create_category(FundamentalsRegionName)
        self.__create_category(IntermediateRegionName)
        self.__create_category(AdvancedRegionName)
        self.__create_category(ExpertRegionName)
        self.__create_category(EssentialsRegionName)
        self.__create_category(GreatsRegionName)
        self.__create_category(ArcticRegionName)
