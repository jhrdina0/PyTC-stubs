import System
import Teamcenter.Soa.Client.Model
import typing

class CallToRemoteSiteResponse:
    def __init__(self, ) -> None: ...
    MsgIDs: list[str]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ChangeOwnershipInfo:
    def __init__(self, ) -> None: ...
    ReplicaSiteId: int
    ListOfGSIdentities: list[str]

class ConfirmExportResponse:
    def __init__(self, ) -> None: ...
    OwnershipChanges: list[ChangeOwnershipInfo]
    StubReplication: list[StubReplicationInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DryRunExportResponse:
    def __init__(self, ) -> None: ...
    FmsTicketForReport: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ExportObjectsResponse:
    def __init__(self, ) -> None: ...
    SitesResponse: list[ExportObjectsSiteResponseInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ExportObjectsSiteResponseInfo:
    def __init__(self, ) -> None: ...
    SiteId: int
    FileFmsTickets: list[str]
    LogFmsTickets: list[str]

class ImportObjectsResponse:
    def __init__(self, ) -> None: ...
    FmsTicketOfFailedObjs: str
    LogFmsTicket: str
    Servicedata: Teamcenter.Soa.Client.Model.ServiceData

class NamesAndValues:
    def __init__(self, ) -> None: ...
    Name: str
    Value: str

class OwningSiteAndObjs:
    def __init__(self, ) -> None: ...
    OwningSiteId: int
    Objs: list[Teamcenter.Soa.Client.Model.ModelObject]

class StubReplicationInfo:
    def __init__(self, ) -> None: ...
    MasterSiteId: int
    ListOfGSIdentities: list[str]

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

class ImportExport:
    def __init__(self , *args: typing.Any) -> None: ...
    def ConfirmExport(self, TargetSite: int, TcGSMessageId: str, FmsTicketOfFailedObjs: str, Commit: bool) -> ConfirmExportResponse: ...
    def DryRunExport(self, TargetSites: list[int], ExpObjList: list[str], TcGSMessageId: str, InputData: TransferFormula) -> DryRunExportResponse: ...
    def ExportObjects(self, TargetSites: list[int], ExpObjList: list[str], TcGSMessageId: str, InputData: TransferFormula, Synchronize: bool) -> ExportObjectsResponse: ...
    def ImportObjects(self, MasterSite: int, TcGSMessageId: str, FmsTickets: list[str], InputData: TransferFormula, Synchronize: bool) -> ImportObjectsResponse: ...
    def RequestExportToRemoteSites(self, Reason: str, Sites: list[Teamcenter.Soa.Client.Model.ModelObject], Objects: list[Teamcenter.Soa.Client.Model.ModelObject], OptionSet: Teamcenter.Soa.Client.Model.ModelObject, OptionNameAndValues: list[NamesAndValues], SessionOptionNamesAndValues: list[NamesAndValues]) -> CallToRemoteSiteResponse: ...
    def RequestImportFromRemoteSites(self, Reason: str, OwningSitesAndObjs: list[OwningSiteAndObjs], OptionSet: Teamcenter.Soa.Client.Model.ModelObject, OptionNamesAndValues: list[NamesAndValues], SessionOptionNamesAndValues: list[NamesAndValues]) -> CallToRemoteSiteResponse: ...

