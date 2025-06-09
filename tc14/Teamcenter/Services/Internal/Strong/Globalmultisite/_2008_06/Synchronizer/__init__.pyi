import System
import Teamcenter.Services.Internal.Strong.Globalmultisite._2007_06.Synchronizer
import Teamcenter.Soa.Client.Model
import typing

class GetExportedObjectsResponse:
    def __init__(self, ) -> None: ...
    ExportedObjectsList: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class NamesAndValues:
    def __init__(self, ) -> None: ...
    Name: str
    Value: str

class TransferFormula:
    def __init__(self, ) -> None: ...
    OptionSetName: str
    OptionSetUid: str
    OptionOverrides: list[NamesAndValues]
    SessionOptions: list[NamesAndValues]
    TransferModeName: str
    TransferModeUid: str
    XsltFMSTicket: str
    Reason: str

class Synchronizer:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetCandidatesForClasseswOpts(self, TargetSite: int, ClassList: list[str], TransferFormula: TransferFormula) -> Teamcenter.Services.Internal.Strong.Globalmultisite._2007_06.Synchronizer.SyncResponse: ...
    def GetCandidatesForObjectswOpts(self, TargetSite: int, ObjectList: list[Teamcenter.Services.Internal.Strong.Globalmultisite._2007_06.Synchronizer.ObjectsByClass], TransferFormula: TransferFormula) -> Teamcenter.Services.Internal.Strong.Globalmultisite._2007_06.Synchronizer.SyncResponse: ...
    def GetExportedObjects(self, TargetSiteId: int, ClassList: list[str]) -> GetExportedObjectsResponse: ...

