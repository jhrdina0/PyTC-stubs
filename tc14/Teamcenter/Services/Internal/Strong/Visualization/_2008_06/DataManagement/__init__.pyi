import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BaseObjInfo:
    def __init__(self, ) -> None: ...
    BaseObj: Teamcenter.Soa.Client.Model.ModelObject
    PropertiesInfo: System.Collections.Hashtable

class CreateTwoDSnapshotOutput:
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    Form: Teamcenter.Soa.Client.Model.ModelObject
    References: list[NamedRefsInDataset]
    AttachRelation: Teamcenter.Soa.Client.Model.Strong.ImanRelation

class CreateTwoDSnapshotResponse:
    def __init__(self, ) -> None: ...
    SnapshotOutput: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DatasetInfo:
    def __init__(self, ) -> None: ...
    Tool: str
    DatasetType: str
    DatasetName: str
    DatasetDesc: str

class FormInfo:
    def __init__(self, ) -> None: ...
    Name: str
    Description: str
    FormType: str
    AttributesMap: System.Collections.Hashtable
    SaveDB: bool

class GetLatestFileReadTicketsInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    NamedRef: Teamcenter.Soa.Client.Model.Strong.ImanFile
    OriginalFilename: str

class GetLatestFileReadTicketsOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    NamedRefUID: str
    OriginalFilename: str
    ReadTicket: str

class GetLatestFileReadTicketsResponse:
    def __init__(self, ) -> None: ...
    GetLatestFileReadTicketsOutput: list[GetLatestFileReadTicketsOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GRMRelationOutput:
    def __init__(self, ) -> None: ...
    Relation: Teamcenter.Soa.Client.Model.Strong.ImanRelation
    PropertiesInfo: System.Collections.Hashtable

class IdInfo:
    def __init__(self, ) -> None: ...
    Id: Teamcenter.Soa.Client.Model.ModelObject
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    Operation: str
    IdAdditionalInfo: System.Collections.Hashtable

class MarkupInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    AttachToLocation: Teamcenter.Soa.Client.Model.ModelObject
    CreateDatasetInfo: DatasetInfo
    BaseObjInfo: BaseObjInfo
    UploadData: list[NamedRefUploadOrUpdateInfo]

class MarkupOutput:
    def __init__(self, ) -> None: ...
    MarkupDatset: Teamcenter.Soa.Client.Model.Strong.Dataset
    References: list[NamedRefsInDataset]
    AttachRelation: Teamcenter.Soa.Client.Model.Strong.ImanRelation
    Relation: GRMRelationOutput

class MarkupResponse:
    def __init__(self, ) -> None: ...
    MarkupInfo: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MarkupUpdateInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    MarkupDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    BaseObjInfo: BaseObjInfo
    UploadData: list[NamedRefUploadOrUpdateInfo]

class MarkupUpdateOutput:
    def __init__(self, ) -> None: ...
    MarkupDatset: Teamcenter.Soa.Client.Model.Strong.Dataset
    References: list[NamedRefsInDataset]
    Relation: GRMRelationOutput

class MarkupUpdateResponse:
    def __init__(self, ) -> None: ...
    MarkupInfo: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MetaDataStampTicketsResponse:
    def __init__(self, ) -> None: ...
    Tickets: list[str]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class NamedRefsInDataset:
    def __init__(self, ) -> None: ...
    ClientFileId: str
    UploadedFile: Teamcenter.Soa.Client.Model.Strong.ImanFile
    UploadedFilename: str
    UploadedFileRefNames: str

class NamedRefUploadOrUpdateInfo:
    def __init__(self, ) -> None: ...
    ClientFileId: str
    FileState: str
    FileName: str
    RefName: str
    FileTicket: str
    NewObject: Teamcenter.Soa.Client.Model.ModelObject
    ExistingObject: Teamcenter.Soa.Client.Model.ModelObject

class SaveSessionOutput:
    def __init__(self, ) -> None: ...
    SessionModelDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    Reference: NamedRefsInDataset

class SaveSessionResponse:
    def __init__(self, ) -> None: ...
    SessionToSessionModelInfo: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ServerInfo:
    def __init__(self, ) -> None: ...
    Protocol: str
    Hostpath: str
    Servermode: int
    ServerAdditionalInfo: System.Collections.Hashtable

class SessionInfo:
    def __init__(self, ) -> None: ...
    SessionDescriminator: str
    SessionAdditionalInfo: System.Collections.Hashtable

class SessionModelInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    AttachToLocation: Teamcenter.Soa.Client.Model.ModelObject
    CreateDatasetInfo: DatasetInfo
    SessionModelBaseObjs: list[BaseObjInfo]
    UploadData: list[NamedRefUploadOrUpdateInfo]

class SessionModelOutput:
    def __init__(self, ) -> None: ...
    SessionModelDatset: Teamcenter.Soa.Client.Model.Strong.Dataset
    References: list[NamedRefsInDataset]
    AttachRelation: Teamcenter.Soa.Client.Model.Strong.ImanRelation
    Relations: list[GRMRelationOutput]

class SessionModelResponse:
    def __init__(self, ) -> None: ...
    SessionModelInfo: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SessionModelUpdateOutput:
    def __init__(self, ) -> None: ...
    SessionModelDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    References: list[NamedRefsInDataset]
    Relations: list[GRMRelationOutput]

class SessionModelUpdateResponse:
    def __init__(self, ) -> None: ...
    SessionModelInfo: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class TwoDSnapshotInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    SourceItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    CreateDatasetInfo: DatasetInfo
    NamedRefInfo: list[NamedRefUploadOrUpdateInfo]
    CreateFormInfo: FormInfo

class UpdateSessionModelWithSessionInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    SessionModelDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    UploadSessionFile: NamedRefUploadOrUpdateInfo

class UpdateSesssionModel:
    def __init__(self, ) -> None: ...
    ClientId: str
    SessionModelDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    SessionModelBaseObjs: list[BaseObjInfo]
    UploadData: list[NamedRefUploadOrUpdateInfo]

class UpdateTwoDSnapshotInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    SnapshotDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    NamedRefInfo: list[NamedRefUploadOrUpdateInfo]

class UpdateTwoDSnapshotOutput:
    def __init__(self, ) -> None: ...
    SnapshotDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    References: list[NamedRefsInDataset]

class UpdateTwoDSnapshotResponse:
    def __init__(self, ) -> None: ...
    UpdateSnapshotInfo: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class UserAgentDataInfo:
    def __init__(self, ) -> None: ...
    UserApplication: str
    UserAppVersion: str
    UserAdditionalInfo: System.Collections.Hashtable

class VVITicketsResponse:
    def __init__(self, ) -> None: ...
    Ticket: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def AuthenticateUser(self, Username: str, Password: str) -> bool: ...
    def CreateLaunchFile(self, IdInfos: list[IdInfo], ServerInfo: ServerInfo, UserDataAgentInfo: UserAgentDataInfo, SessionInfo: SessionInfo) -> VVITicketsResponse: ...
    def CreateMarkup(self, Inputs: list[MarkupInput]) -> MarkupResponse: ...
    def CreateSessionModel(self, Inputs: list[SessionModelInput]) -> SessionModelResponse: ...
    def CreateTwoDSnapshot(self, Input: list[TwoDSnapshotInput]) -> CreateTwoDSnapshotResponse: ...
    def GetLatestFileReadTickets(self, Info: list[GetLatestFileReadTicketsInfo]) -> GetLatestFileReadTicketsResponse: ...
    def GetMetaDataStamp(self, Application: str, Servermode: int, Ids: list[Teamcenter.Soa.Client.Model.ModelObject]) -> MetaDataStampTicketsResponse: ...
    def SaveSession(self, Inputs: list[UpdateSessionModelWithSessionInput]) -> SaveSessionResponse: ...
    def UpdateMarkup(self, Inputs: list[MarkupUpdateInput]) -> MarkupUpdateResponse: ...
    def UpdateSessionModel(self, Inputs: list[UpdateSesssionModel]) -> SessionModelUpdateResponse: ...
    def UpdateTwoDSnaphot(self, Input: list[UpdateTwoDSnapshotInput]) -> UpdateTwoDSnapshotResponse: ...

