import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class CommitUploadedRegularFilesInput:
    def __init__(self, ) -> None: ...
    FileName: str
    FileTicket: str
    ClientId: str

class CommitUploadedRegularFilesResponse:
    def __init__(self, ) -> None: ...
    Files: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FileInfo:
    def __init__(self, ) -> None: ...
    ClientFileId: str
    RefName: str
    IsText: bool
    FileName: str

class FileInfoTicket:
    def __init__(self, ) -> None: ...
    ClientFileId: str
    Ticket: str

class FileTicketsResponse:
    def __init__(self, ) -> None: ...
    Tickets: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetFileTransferTicketsResponse:
    def __init__(self, ) -> None: ...
    ReadTickets: System.Collections.Hashtable
    WriteTickets: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetRegularFileWriteTicketsInput:
    def __init__(self, ) -> None: ...
    RegularFileInfos: list[RegularFileInfo]
    ClientId: str

class GetRegularFileWriteTicketsResponse:
    def __init__(self, ) -> None: ...
    WriteTickets: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class RegularFileInfo:
    def __init__(self, ) -> None: ...
    FileName: str
    IsText: bool

class UpdateImanFileCommitsResponse:
    def __init__(self, ) -> None: ...
    Delays: System.Collections.Hashtable
    WriteTickets: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class WriteTicketsInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    DatasetTypeName: str
    Version: int
    FileInfos: list[FileInfo]

class FileManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CommitRegularFiles(self, Inputs: list[CommitUploadedRegularFilesInput]) -> CommitUploadedRegularFilesResponse: ...
    def GetRegularFileTicketsForUpload(self, Inputs: list[GetRegularFileWriteTicketsInput]) -> GetRegularFileWriteTicketsResponse: ...
    def GetWriteTickets(self, Inputs: list[WriteTicketsInput]) -> FileTicketsResponse: ...
    def UpdateImanFileCommits(self, CleanupInfo: list[str]) -> UpdateImanFileCommitsResponse: ...
    def GetFileTransferTickets(self, ImanFiles: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetFileTransferTicketsResponse: ...

