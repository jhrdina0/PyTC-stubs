import System
import Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement
import Teamcenter.Soa.Client.Model
import typing

class CatalogInfo2:
    def __init__(self, ) -> None: ...
    VendorName: str
    VendorAcronym: str
    VendorCatalogVersion: str
    VendorCatalogLanguage: str
    VendorCatalogDescription: str
    VendorCatalogShortDescription: str
    VendorCatalogId: str
    VendorCatalogRootClassId: str
    VendorCatalogRootDir: str
    GtcPackageCreationDate: str
    GtcHierarchyVersion: str
    GtcPackageId: str

class GetVendorCatalogInfo2Response:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    CatalogInfo: list[CatalogInfo2]

class ResourceManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetStepP21FileCounts2(self, ClassIds: list[str], CatalogRootDirectories: list[str]) -> Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement.GetStepP21FileCountsResponse: ...
    def GetVendorCatalogInfo2(self, CatalogTypes: int) -> GetVendorCatalogInfo2Response: ...
    def ImportStepP21Files2(self, ClassId: str, CatalogRootDirectory: str, ImportOptions: int) -> Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement.ImportStepP21FilesResponse: ...

