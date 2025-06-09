import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetProcessHistoryAuditRecordsResponse:
    def __init__(self, ) -> None: ...
    ProcessNames: list[str]
    RootProcessHistoryAuditRecords: list[ProcessHistoryAuditRecordStruct]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ProcessHistoryAuditRecordStruct:
    def __init__(self, ) -> None: ...
    AuditRecord: Teamcenter.Soa.Client.Model.Strong.Fnd0AuditLog
    ChildrenAuditRecords: list[ProcessHistoryAuditRecordStruct]
    SecondaryAuditRecords: list[Teamcenter.Soa.Client.Model.Strong.Fnd0SecondaryAudit]

class ProcessHistoryManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetProcssHistoryAuditRecords(self, WsoObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject) -> GetProcessHistoryAuditRecordsResponse: ...

