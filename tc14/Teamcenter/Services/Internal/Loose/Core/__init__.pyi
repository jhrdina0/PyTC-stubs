import System
import Teamcenter.Schemas.Soa._2006_03.Base
import Teamcenter.Services.Internal.Loose.Core._2008_06.FileManagement
import Teamcenter.Services.Internal.Loose.Core._2010_09.FileManagement
import Teamcenter.Services.Internal.Loose.Core._2014_10.FileManagement
import Teamcenter.Services.Internal.Loose.Core._2017_05.FileManagement
import Teamcenter.Services.Internal.Loose.Core._2018_11.FileManagement
import Teamcenter.Services.Loose.Core._2006_03.FileManagement
import Teamcenter.Services.Loose.Core._2007_01.FileManagement
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class FileManagementRestBindingStub(FileManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CommitRegularFiles(self, Inputs: list[Teamcenter.Services.Internal.Loose.Core._2008_06.FileManagement.CommitUploadedRegularFilesInput]) -> Teamcenter.Services.Internal.Loose.Core._2008_06.FileManagement.CommitUploadedRegularFilesResponse: ...
    def GetRegularFileTicketsForUpload(self, Inputs: list[Teamcenter.Services.Internal.Loose.Core._2008_06.FileManagement.GetRegularFileWriteTicketsInput]) -> Teamcenter.Services.Internal.Loose.Core._2008_06.FileManagement.GetRegularFileWriteTicketsResponse: ...
    def GetWriteTickets(self, Inputs: list[Teamcenter.Services.Internal.Loose.Core._2008_06.FileManagement.WriteTicketsInput]) -> Teamcenter.Services.Internal.Loose.Core._2008_06.FileManagement.FileTicketsResponse: ...
    def UpdateImanFileCommits(self, CleanupInfo: list[str]) -> Teamcenter.Services.Internal.Loose.Core._2008_06.FileManagement.UpdateImanFileCommitsResponse: ...
    def GetFileTransferTickets(self, ImanFiles: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Internal.Loose.Core._2008_06.FileManagement.GetFileTransferTicketsResponse: ...
    def CommitReplacedFiles(self, CommitInfos: list[Teamcenter.Services.Internal.Loose.Core._2010_09.FileManagement.CommitReplacedFileInfo], Flags: list[bool]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetPlmdFileTicketForDownload(self, Infos: list[Teamcenter.Services.Internal.Loose.Core._2014_10.FileManagement.DatashareManagerDownloadInfo]) -> Teamcenter.Services.Internal.Loose.Core._2014_10.FileManagement.GetPlmdFileTicketResponse: ...
    def GetPlmdFileTicketForUpload(self, Infos: list[Teamcenter.Services.Internal.Loose.Core._2014_10.FileManagement.DatashareManagerUploadInfo]) -> Teamcenter.Services.Internal.Loose.Core._2014_10.FileManagement.GetPlmdFileTicketResponse: ...
    def PostCleanUpFileCommits(self, Files: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetPlmdFileTicketForReplace(self, Infos: list[Teamcenter.Services.Internal.Loose.Core._2017_05.FileManagement.DatashareManagerReplaceInfo]) -> Teamcenter.Services.Internal.Loose.Core._2014_10.FileManagement.GetPlmdFileTicketResponse: ...
    def GetTransientFileTicketsForDownload(self, Tickets: list[Teamcenter.Services.Internal.Loose.Core._2018_11.FileManagement.GetTransientTicketsDownloadInput]) -> Teamcenter.Services.Internal.Loose.Core._2018_11.FileManagement.GetTransientTicketsDownloadResponse: ...
    def GetDatasetTicketsForChunkedUpload(self, Inputs: list[Teamcenter.Services.Loose.Core._2006_03.FileManagement.GetDatasetWriteTicketsInputData]) -> Teamcenter.Services.Loose.Core._2006_03.FileManagement.GetDatasetWriteTicketsResponse: ...
    def GetTransientTicketsForChunkedUpload(self, TransientFileInfos: list[Teamcenter.Services.Loose.Core._2007_01.FileManagement.TransientFileInfo]) -> Teamcenter.Services.Loose.Core._2007_01.FileManagement.GetTransientFileTicketsResponse: ...

class FileManagementService:
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> FileManagementService: ...
    def CommitRegularFiles(self, Inputs: list[Teamcenter.Services.Internal.Loose.Core._2008_06.FileManagement.CommitUploadedRegularFilesInput]) -> Teamcenter.Services.Internal.Loose.Core._2008_06.FileManagement.CommitUploadedRegularFilesResponse: ...
    def GetRegularFileTicketsForUpload(self, Inputs: list[Teamcenter.Services.Internal.Loose.Core._2008_06.FileManagement.GetRegularFileWriteTicketsInput]) -> Teamcenter.Services.Internal.Loose.Core._2008_06.FileManagement.GetRegularFileWriteTicketsResponse: ...
    def GetWriteTickets(self, Inputs: list[Teamcenter.Services.Internal.Loose.Core._2008_06.FileManagement.WriteTicketsInput]) -> Teamcenter.Services.Internal.Loose.Core._2008_06.FileManagement.FileTicketsResponse: ...
    def UpdateImanFileCommits(self, CleanupInfo: list[str]) -> Teamcenter.Services.Internal.Loose.Core._2008_06.FileManagement.UpdateImanFileCommitsResponse: ...
    def GetFileTransferTickets(self, ImanFiles: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Internal.Loose.Core._2008_06.FileManagement.GetFileTransferTicketsResponse: ...
    def CommitReplacedFiles(self, CommitInfos: list[Teamcenter.Services.Internal.Loose.Core._2010_09.FileManagement.CommitReplacedFileInfo], Flags: list[bool]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetPlmdFileTicketForDownload(self, Infos: list[Teamcenter.Services.Internal.Loose.Core._2014_10.FileManagement.DatashareManagerDownloadInfo]) -> Teamcenter.Services.Internal.Loose.Core._2014_10.FileManagement.GetPlmdFileTicketResponse: ...
    def GetPlmdFileTicketForUpload(self, Infos: list[Teamcenter.Services.Internal.Loose.Core._2014_10.FileManagement.DatashareManagerUploadInfo]) -> Teamcenter.Services.Internal.Loose.Core._2014_10.FileManagement.GetPlmdFileTicketResponse: ...
    def PostCleanUpFileCommits(self, Files: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetPlmdFileTicketForReplace(self, Infos: list[Teamcenter.Services.Internal.Loose.Core._2017_05.FileManagement.DatashareManagerReplaceInfo]) -> Teamcenter.Services.Internal.Loose.Core._2014_10.FileManagement.GetPlmdFileTicketResponse: ...
    def GetTransientFileTicketsForDownload(self, Tickets: list[Teamcenter.Services.Internal.Loose.Core._2018_11.FileManagement.GetTransientTicketsDownloadInput]) -> Teamcenter.Services.Internal.Loose.Core._2018_11.FileManagement.GetTransientTicketsDownloadResponse: ...
    def GetDatasetTicketsForChunkedUpload(self, Inputs: list[Teamcenter.Services.Loose.Core._2006_03.FileManagement.GetDatasetWriteTicketsInputData]) -> Teamcenter.Services.Loose.Core._2006_03.FileManagement.GetDatasetWriteTicketsResponse: ...
    def GetTransientTicketsForChunkedUpload(self, TransientFileInfos: list[Teamcenter.Services.Loose.Core._2007_01.FileManagement.TransientFileInfo]) -> Teamcenter.Services.Loose.Core._2007_01.FileManagement.GetTransientFileTicketsResponse: ...

class SessionRestBindingStub(SessionService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def InitTypeByNames(self, TypeNames: list[str]) -> Teamcenter.Schemas.Soa._2006_03.Base.ModelSchema: ...
    def InitTypeByUids(self, Uids: list[str]) -> Teamcenter.Schemas.Soa._2006_03.Base.ModelSchema: ...
    def RefreshPOMCachePerRequest(self, Refresh: bool) -> bool: ...
    def GetProperties(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Attributes: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DisableUserSessionState(self, Names: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CancelOperation(self, Id: str) -> bool: ...
    def GetSecurityToken(self, Duration: int) -> str: ...

class SessionService:
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SessionService: ...
    def InitTypeByNames(self, TypeNames: list[str]) -> Teamcenter.Schemas.Soa._2006_03.Base.ModelSchema: ...
    def InitTypeByUids(self, Uids: list[str]) -> Teamcenter.Schemas.Soa._2006_03.Base.ModelSchema: ...
    def RefreshPOMCachePerRequest(self, Refresh: bool) -> bool: ...
    def GetProperties(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Attributes: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DisableUserSessionState(self, Names: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CancelOperation(self, Id: str) -> bool: ...
    def GetSecurityToken(self, Duration: int) -> str: ...

