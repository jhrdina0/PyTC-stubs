import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DatasetsForFile:
    def __init__(self, ) -> None: ...
    FileName: str
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset

class DatasetsForFileInput:
    def __init__(self, ) -> None: ...
    ClientID: str
    FileNames: list[str]
    ParentObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject

class DatasetsForFileOutput:
    def __init__(self, ) -> None: ...
    ClientID: str
    DatasetsForFile: list[DatasetsForFile]

class DatasetsForFileResponse:
    def __init__(self, ) -> None: ...
    Output: list[DatasetsForFileOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def QueryForFileExistence(self, Input: list[DatasetsForFileInput]) -> DatasetsForFileResponse: ...

