import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class CommitDatasetFileInfo:
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.ModelObject
    CreateNewVersion: bool
    DatasetFileTicketInfos: list[DatasetFileTicketInfo]

class DatasetFileInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    FileName: str
    NamedReferencedName: str
    IsText: bool
    AllowReplace: bool

class DatasetFileTicketInfo:
    def __init__(self, ) -> None: ...
    DatasetFileInfo: DatasetFileInfo
    Ticket: str

class FileTicketsResponse:
    def __init__(self, ) -> None: ...
    Tickets: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetDatasetWriteTicketsInputData:
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.ModelObject
    CreateNewVersion: bool
    DatasetFileInfos: list[DatasetFileInfo]

class GetDatasetWriteTicketsResponse:
    def __init__(self, ) -> None: ...
    CommitInfo: list[CommitDatasetFileInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FileManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CommitDatasetFiles(self, CommitInput: list[CommitDatasetFileInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetDatasetWriteTickets(self, Inputs: list[GetDatasetWriteTicketsInputData]) -> GetDatasetWriteTicketsResponse: ...
    def GetFileReadTickets(self, Files: list[Teamcenter.Soa.Client.Model.ModelObject]) -> FileTicketsResponse: ...

