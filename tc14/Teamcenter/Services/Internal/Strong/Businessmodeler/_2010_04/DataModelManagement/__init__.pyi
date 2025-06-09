import System
import Teamcenter.Services.Internal.Strong.Businessmodeler._2007_01.DataModelManagement
import Teamcenter.Soa.Client.Model
import typing

class ChangedTemplateFileInput:
    def __init__(self, ) -> None: ...
    TemplateDirectory: str
    TemplateFile: str
    Timestamp: System.DateTime

class DataModelDeploymentInput:
    def __init__(self, ) -> None: ...
    DeploymentFileTicket: str
    DeploymentFileType: int

class TemplateFileInput:
    def __init__(self, ) -> None: ...
    TemplateDirectory: str
    TemplateFile: str

class TemplateFileOutput:
    def __init__(self, ) -> None: ...
    TemplateDirectory: str
    TemplateFile: str
    TemplateFileTicket: str
    Timestamp: System.DateTime

class TemplateFilesResponse:
    def __init__(self, ) -> None: ...
    Outputs: list[TemplateFileOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DataModelManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def DeployDataModel(self, Inputs: list[DataModelDeploymentInput], DeployOption: str, UpdaterUpdateOption: str, UpdaterModeOption: str) -> Teamcenter.Services.Internal.Strong.Businessmodeler._2007_01.DataModelManagement.ImportDataModelResponse: ...
    def GetChangedTemplateFiles(self, Inputs: list[ChangedTemplateFileInput], RetrieveFiles: bool) -> TemplateFilesResponse: ...
    def GetTemplateFiles(self, Inputs: list[TemplateFileInput]) -> TemplateFilesResponse: ...

