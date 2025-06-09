import Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class Import3DModelsInfo:
    def __init__(self, ) -> None: ...
    TotalCount: int
    SuccessCount: int
    LogFileInfo: Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement.RMFileTicket

class ImportVendorProductsInput:
    def __init__(self, ) -> None: ...
    ClassId: str
    ProductCount: int
    ImportOption: int

class MapVendorProductsInput:
    def __init__(self, ) -> None: ...
    TargetItemTypeName: str

class ImportVendorDataIn:
    def __init__(self, ) -> None: ...
    VendorPackageId: str
    VendorPackageDirectory: str
    DoCheckVendorProducts: bool
    DoImportVendorProducts: bool
    DoMapVendorProducts: bool
    DoImport3DModels: bool
    ImportVendorProductsInput: ImportVendorProductsInput
    MapVendorProductsInput: MapVendorProductsInput

class ImportVendorProductsInfo:
    def __init__(self, ) -> None: ...
    TotalCount: int
    SuccessCount: int
    SavedSearch: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    LogFileInfo: Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement.RMFileTicket

class MapVendorProductsInfo:
    def __init__(self, ) -> None: ...
    TotalCount: int
    SuccessCount: int
    SavedSearch: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    LogFileInfo: Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement.RMFileTicket

class ImportVendorDataResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    ImportedProductCount: int
    MappedProductCount: int
    ImportVendorProductsInfo: ImportVendorProductsInfo
    MapVendorProductsInfo: MapVendorProductsInfo
    Import3DModelsInfo: Import3DModelsInfo

class ResourceManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ImportVendorData(self, ImportVendorDataIn: ImportVendorDataIn) -> ImportVendorDataResponse: ...

