import System
import Teamcenter.Services.Loose.Core._2006_03.FileManagement
import Teamcenter.Soa.Client.Model
import typing

class ReplaceFileInput:
    def __init__(self, ) -> None: ...
    ImanFile: Teamcenter.Soa.Client.Model.ModelObject
    NewFileTicket: str
    RetainOriginalFileName: bool

class FileManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CommitDatasetFilesInBulk(self, CommitInput: list[Teamcenter.Services.Loose.Core._2006_03.FileManagement.CommitDatasetFileInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ReplaceFiles(self, Inputs: list[ReplaceFileInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

