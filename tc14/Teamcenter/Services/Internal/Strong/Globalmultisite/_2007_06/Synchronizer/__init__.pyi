import System
import Teamcenter.Soa.Client.Model
import typing

class CheckSyncStateResponse:
    def __init__(self, ) -> None: ...
    ReplicaSyncStatusList: list[GmsSyncStatus]
    LogFmsTicket: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GmsSyncStatus:
    def __init__(self, ) -> None: ...
    CandidateObject: str
    SyncStatus: str

class ObjectsByClass:
    def __init__(self, ) -> None: ...
    ClassName: str
    ObjectsList: list[str]

class OwnershipChangeReplicaUpdateResponse:
    def __init__(self, ) -> None: ...
    LogFmsTicket: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ReplicaDeletionMasterUpdateResponse:
    def __init__(self, ) -> None: ...
    LogFmsTicket: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class StubReplicationMasterUpdateResponse:
    def __init__(self, ) -> None: ...
    LogFmsTicket: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SyncResponse:
    def __init__(self, ) -> None: ...
    CandidateObjectsList: list[str]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Synchronizer:
    def __init__(self , *args: typing.Any) -> None: ...
    def CheckReplicaSyncState(self, ReplicaSite: int, SyncType: str, RevisionRule: str, InputReplicaGSIdentityList: list[str]) -> CheckSyncStateResponse: ...
    def CreateExportRecordOnStubReplication(self, ReplicaSite: int, TransferFormula: str, TransactionID: str, InputReplicaGSIdentityList: list[str]) -> StubReplicationMasterUpdateResponse: ...
    def GetCandidatesToSynchronizeForListOfClasses(self, TargetSite: int, ClassList: list[str]) -> SyncResponse: ...
    def GetCandidatesToSynchronizeForListOfObjects(self, TargetSite: int, ObjectsListToProcess: list[ObjectsByClass]) -> SyncResponse: ...
    def UpdateMasterObjectsOnReplicaDeletion(self, ReplicaSite: int, InputReplicaGSIdentityList: list[str], ConvertToStub: bool) -> ReplicaDeletionMasterUpdateResponse: ...
    def UpdateObjectsOnOwnershipChange(self, NewOwningSite: int, InputReplicaGSIdentityList: list[str]) -> OwnershipChangeReplicaUpdateResponse: ...

