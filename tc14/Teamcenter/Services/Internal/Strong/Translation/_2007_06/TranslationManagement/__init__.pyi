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

class QueryTranslationRequestsArgs:
    def __init__(self, ) -> None: ...
    Providers: list[str]
    Services: list[str]
    States: list[str]
    Priorities: list[int]
    ModifiedDate: str
    PrimaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    TaskIDs: list[str]

class QueryTranslationRequestsOutput:
    def __init__(self, ) -> None: ...
    QueriedRequests: list[Teamcenter.Soa.Client.Model.ModelObject]

class QueryTranslationRequestsResponse:
    def __init__(self, ) -> None: ...
    OutputObjects: list[QueryTranslationRequestsOutput]
    SvcData: Teamcenter.Soa.Client.Model.ServiceData

class UpdateTranslationRequestArgs:
    def __init__(self, ) -> None: ...
    RequestToUpdate: Teamcenter.Soa.Client.Model.ModelObject
    Priority: int
    CurrentState: str
    NextState: str
    TaskID: str
    TranslatorArgs: list[str]

class UpdateTranslationRequestOutput:
    def __init__(self, ) -> None: ...
    RequestUpdated: Teamcenter.Soa.Client.Model.ModelObject
    WasRequestUpdated: bool

class UpdateTranslationRequestResponse:
    def __init__(self, ) -> None: ...
    OutputObjects: list[UpdateTranslationRequestOutput]
    SvcData: Teamcenter.Soa.Client.Model.ServiceData

class TranslationManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateDatasetOfVersion(self, Inputs: list[CreateDatasetOfVersionArgs]) -> CreateDatasetOfVersionResponse: ...
    def InsertDatasetVersion(self, Inputs: list[InsertDatasetVersionArgs]) -> InsertDatasetVersionResponse: ...
    def QueryTranslationRequests(self, Inputs: list[QueryTranslationRequestsArgs]) -> QueryTranslationRequestsResponse: ...
    def UpdateTranslationRequest(self, Inputs: list[UpdateTranslationRequestArgs]) -> UpdateTranslationRequestResponse: ...

