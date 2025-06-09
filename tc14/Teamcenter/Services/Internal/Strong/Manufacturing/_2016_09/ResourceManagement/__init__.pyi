import System
import Teamcenter.Soa.Client.Model
import typing

class CatalogInfo3:
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
    LogoUrl: str
    DisclaimerText: str
    GtcVersion: str
    VendorHierarchyVersion: str
    DownloadSecurity: str
    OnlineConnectionConfiguration: str

class GetVendorCatalogInfo3Response:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    CatalogInfo: list[CatalogInfo3]

class ResourceManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExtractHolderData(self, IcoIds: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetVendorCatalogInfo3(self, CatalogTypeFilter: int) -> GetVendorCatalogInfo3Response: ...

