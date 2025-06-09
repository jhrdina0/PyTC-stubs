import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ChangesetResponse:
    def __init__(self, ) -> None: ...
    BriefcaseWriteTickets: list[FileInformation]
    ChangesetWriteTickets: list[FileInformation]
    FmsURL: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FileInformation:
    def __init__(self, ) -> None: ...
    FileName: str
    FileTicket: str

class IModelData:
    def __init__(self, ) -> None: ...
    IModel: Teamcenter.Soa.Client.Model.Strong.Pdm0IModel
    LatestChangeset: Teamcenter.Soa.Client.Model.Strong.Pdm0ChangeSet
    BriefcaseReadTickets: list[FileInformation]
    ChangesetReadTickets: list[FileInformation]
    FmsURL: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class IncrementalUpdateResponse:
    def __init__(self, ) -> None: ...
    ObjectsToCreate: list[str]
    ObjectsToUpdateMap: System.Collections.Hashtable
    ObjectsToDeleteMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PdmCore:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateChangesetAndUpdateIModelData(self, Pdm0IModel: Teamcenter.Soa.Client.Model.Strong.Pdm0IModel, Pdm0ParentChangeSetId: str, ChangesetName: str, ChangesetFileName: str, Pdm0Id: str) -> ChangesetResponse: ...
    def GetIModelData(self, IModelID: str, ContextID: str) -> IModelData: ...
    def GetIncrementalUpdates(self, RootObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject, ExternalIds: list[str]) -> IncrementalUpdateResponse: ...

