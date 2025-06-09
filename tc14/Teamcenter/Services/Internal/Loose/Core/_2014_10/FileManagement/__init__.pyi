import System
import Teamcenter.Soa.Client.Model
import typing

class DatashareManagerDownloadInfo:
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.ModelObject
    ImanFile: Teamcenter.Soa.Client.Model.ModelObject
    AbsoluteFilePath: str

class DatashareManagerUploadInfo:
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.ModelObject
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
    def PostCleanUpFileCommits(self, Files: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

