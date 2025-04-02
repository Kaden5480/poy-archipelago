from enum import StrEnum

from .id_handler import IDHandler

from ..names.regions import RegionName, \
                            CabinRegionName, \
                            PeakName, \
                            FundamentalsRegionName, \
                            IntermediateRegionName, \
                            AdvancedRegionName, \
                            ExpertRegionName, \
                            EssentialsRegionName, \
                            GreatsRegionName, \
                            ArcticRegionName

class RegionData:
    id: int
    name: str

    def __init__(self, id: int, name: str) -> None:
        """
        Initializes a RegionData object.

        :param id: The ID of this region
        :param name: The name of this region
        """

        self.id = id
        self.name = name


class Regions:
    handler: IDHandler

    regions: dict[str, RegionData]

    def __init__(self, handler: IDHandler) -> None:
        """
        Initializes a Regions object.

        :param handler: The handler to assign IDs with
        """

        self.handler = handler
        self.regions = {}

        self.create_category(CabinRegionName)
        self.create_category(FundamentalsRegionName)
        self.create_category(IntermediateRegionName)
        self.create_category(AdvancedRegionName)
        self.create_category(ExpertRegionName)
        self.create_category(EssentialsRegionName)
        self.create_category(GreatsRegionName)
        self.create_category(ArcticRegionName)

    def create_data(
        self,
        region: RegionName
    ) -> None:
        """
        Creates the data for a region.
        """

        self.regions[region] = RegionData(
            self.handler.new_id(), region.value
        )

    def create_category(
        self,
        category: RegionName
    ) -> None:
        """
        Creates region data for all regions
        in a given category.

        :param category: The category to create region data for
        """

        for region in category:
            self.create_data(region)

    def get_data(
        self,
        name: RegionName
    ) -> None:
        """
        Gets the region data for a given region.

        :param name: The name of the region to get data for
        :returns: The region's data
        """

        return self.regions[region.value]

    def get_data_for_category(
        self,
        category: RegionName
    ) -> list[RegionData]:
        """
        Gets all region data in a given category

        :param category: The category to get region data for
        :returns: A list of all region data for this category
        """

        return [self.get_data(region) for region in category]
