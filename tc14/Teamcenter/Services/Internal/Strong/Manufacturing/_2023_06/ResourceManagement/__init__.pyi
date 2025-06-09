import Teamcenter.Services.Internal.Strong.Manufacturing._2022_12.ResourceManagement
import Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ICOToTargetClassMappings:
    def __init__(self, ) -> None: ...
    SourceIcoID: str
    TargetItemName: str
    TargetClassID: str

class MapToSingleTargetClassInput:
    def __init__(self, ) -> None: ...
    TargetItemTypeName: str

class MapToMultiTargetClassesInput:
    def __init__(self, ) -> None: ...
    TotalProductsCount: int
    TargetItemTypeName: str
    IcoToTargetClassMappings: list[ICOToTargetClassMappings]
    LogFileInfo: Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement.RMFileTicket

class ImportVendorData2In:
    def __init__(self, ) -> None: ...
    VendorPackageId: str
    VendorPackageDirectory: str
    DoCheckVendorProducts: bool
    DoImportVendorProducts: bool
    DoMapToSingleTargetClass: bool
    DoMapToMultiTargetClasses: bool
    DoImport3DModels: bool
    ImportVendorProductsInput: Teamcenter.Services.Internal.Strong.Manufacturing._2022_12.ResourceManagement.ImportVendorProductsInput
    MapToSingleTargetClassInput: MapToSingleTargetClassInput
    MapToMultiTargetClassesInput: MapToMultiTargetClassesInput

class MapToSingleTargetClassInfo:
    def __init__(self, ) -> None: ...
    TotalProductsCount: int
    SuccessSingleMappingCount: int
    SavedSearch: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    MultiTargetClassesInfo: list[MultiTargetClassesInfo]
    LogFileInfo: Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement.RMFileTicket

class MapToMultiTargetClassesInfo:
    def __init__(self, ) -> None: ...
    TotalProductsCount: int
    TotalMultiMappingCount: int
    SuccessMultiMappingCount: int
    LogFileInfo: Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement.RMFileTicket

class ImportVendorData2Response:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    ImportedProductCount: int
    MappedProductCount: int
    ImportVendorProductsInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2022_12.ResourceManagement.ImportVendorProductsInfo
    MapToSingleTargetClassInfo: MapToSingleTargetClassInfo
    MapToMultiTargetClassesInfo: MapToMultiTargetClassesInfo
    Import3DModelsInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2022_12.ResourceManagement.Import3DModelsInfo

class MultiTargetClassesInfo:
    def __init__(self, ) -> None: ...
    SourceIcoID: str
    SourceClassID: str
    SourceClassName: str
    TargetItemName: str
    TargetClasses: list[TargetClasses]

class TargetClasses:
    def __init__(self, ) -> None: ...
    TargetClassID: str
    TargetClassName: str

class ResourceManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ImportVendorData2(self, ImportVendorData2In: ImportVendorData2In) -> ImportVendorData2Response: ...

