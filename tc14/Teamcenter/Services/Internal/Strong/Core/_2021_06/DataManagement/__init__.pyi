import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FileNameRelation:
    def __init__(self, ) -> None: ...
    FileName: str
    RelationName: str

class GenerateDatasetNameOutput:
    def __init__(self, ) -> None: ...
    WorkspaceObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    FileNameDatasetNameMap: System.Collections.Hashtable

class GenerateDatasetNameResponse:
    def __init__(self, ) -> None: ...
    Output: list[GenerateDatasetNameOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GenerateDsNameInput:
    def __init__(self, ) -> None: ...
    WorkspaceObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    FileNameRelations: list[FileNameRelation]
    AdditionalInfo: System.Collections.Hashtable

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GenerateDatasetName(self, Input: list[GenerateDsNameInput]) -> GenerateDatasetNameResponse: ...

