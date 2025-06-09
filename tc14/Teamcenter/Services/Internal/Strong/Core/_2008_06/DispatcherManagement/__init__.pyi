import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateDatasetOfVersionArgs:
    def __init__(self, ) -> None: ...
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    DatasetName: str
    TypeName: str
    Tool: Teamcenter.Soa.Client.Model.ModelObject
    Version: int

class CreateDatasetOfVersionResponse:
    def __init__(self, ) -> None: ...
    CreatedDatasets: list[Teamcenter.Soa.Client.Model.Strong.Dataset]
    SvcData: Teamcenter.Soa.Client.Model.ServiceData

class InsertDatasetVersionArgs:
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.ModelObject
    VersionNumber: int

class InsertDatasetVersionResponse:
    def __init__(self, ) -> None: ...
    DatasetTags: list[Teamcenter.Soa.Client.Model.ModelObject]
    SvcData: Teamcenter.Soa.Client.Model.ServiceData

class InternalDataFiles:
    def __init__(self, ) -> None: ...
    Key: str
    File: Teamcenter.Soa.Client.Model.Strong.ImanFile

class InternalKeyValueArguments:
    def __init__(self, ) -> None: ...
    Key: str
    Value: str

class QueryDispatcherRequestsArgs:
    def __init__(self, ) -> None: ...
    Providers: list[str]
    Services: list[str]
    States: list[str]
    Priorities: list[int]
    ModifiedDate: str
    PrimaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    TaskID: list[str]
    Type: list[str]
    UnLoaded: bool

class QueryDispatcherRequestsOutput:
    def __init__(self, ) -> None: ...
    QueriedRequests: list[Teamcenter.Soa.Client.Model.ModelObject]

class QueryDispatcherRequestsResponse:
    def __init__(self, ) -> None: ...
    OutputObjects: list[QueryDispatcherRequestsOutput]
    SvcData: Teamcenter.Soa.Client.Model.ServiceData

class UpdateDispatcherRequestArgs:
    def __init__(self, ) -> None: ...
    RequestToUpdate: Teamcenter.Soa.Client.Model.ModelObject
    CurrentState: str
    NextState: str
    Type: str
    KeyValueArgs: list[InternalKeyValueArguments]
    DataFiles: list[InternalDataFiles]

class UpdateDispatcherRequestOutput:
    def __init__(self, ) -> None: ...
    RequestUpdated: Teamcenter.Soa.Client.Model.ModelObject
    WasRequestUpdated: bool

class UpdateDispatcherRequestResponse:
    def __init__(self, ) -> None: ...
    OutputObjects: list[UpdateDispatcherRequestOutput]
    SvcData: Teamcenter.Soa.Client.Model.ServiceData

class DispatcherManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateDatasetOfVersion(self, Inputs: list[CreateDatasetOfVersionArgs]) -> CreateDatasetOfVersionResponse: ...
    def InsertDatasetVersion(self, Inputs: list[InsertDatasetVersionArgs]) -> InsertDatasetVersionResponse: ...
    def QueryDispatcherRequests(self, Inputs: list[QueryDispatcherRequestsArgs]) -> QueryDispatcherRequestsResponse: ...
    def UpdateDispatcherRequests(self, Inputs: list[UpdateDispatcherRequestArgs]) -> UpdateDispatcherRequestResponse: ...

