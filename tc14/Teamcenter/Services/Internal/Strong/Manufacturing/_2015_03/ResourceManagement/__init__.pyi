import System
import Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement
import Teamcenter.Soa.Client.Model
import typing

class GtcPackageImportResult:
    def __init__(self, ) -> None: ...
    Status: int
    IcoId: str
    IcoUid: str
    WsoUid: str
    ClassId: str
    Report: list[str]

class ImportStep3DModels2Response:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    ImportStep3DModelResults: list[GtcPackageImportResult]

class ImportStepP21Files3Response:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    LogFileTicket: Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement.RMFileTicket
    ImportStepP21ProductResults: list[GtcPackageImportResult]

class MapClassificationObjectResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    TargetIcoUid: str
    TargetWsoUid: str

class UnzipGtcPackageResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    GtcPackageServerDirectory: str

class ResourceManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ImportStep3DModels2(self, IcoIds: list[str]) -> ImportStep3DModels2Response: ...
    def ImportStepP21Files3(self, ClassId: str, CatalogRootDirectory: str, ImportOption: int) -> ImportStepP21Files3Response: ...
    def MapClassificationObject(self, SourceIcoId: str, TargetItemId: str, TargetItemName: str, TargetItemTypeName: str, TargetItemRevId: str, TargetItemDescription: str, TargetClassId: str, Options: int) -> MapClassificationObjectResponse: ...
    def UnzipGtcPackage(self, TransientFmsZipFileTicket: str) -> UnzipGtcPackageResponse: ...

