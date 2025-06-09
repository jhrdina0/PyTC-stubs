import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DatashareManagerDownloadInfo:
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    ImanFile: Teamcenter.Soa.Client.Model.Strong.ImanFile
    AbsoluteFilePath: str

class DatashareManagerUploadInfo:
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    NamedReferenceName: str
    AbsoluteFilePath: str

class GetPlmdFileTicketResponse:
    def __init__(self, ) -> None: ...
    Ticket: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FileManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPlmdFileTicketForDownload(self, Infos: list[DatashareManagerDownloadInfo]) -> GetPlmdFileTicketResponse: ...
    def GetPlmdFileTicketForUpload(self, Infos: list[DatashareManagerUploadInfo]) -> GetPlmdFileTicketResponse: ...
    def PostCleanUpFileCommits(self, Files: list[Teamcenter.Soa.Client.Model.Strong.ImanFile]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

