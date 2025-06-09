import System
import Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport
import Teamcenter.Services.Strong.Globalmultisite._2010_04.ImportExport
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ImportObjectsFromPLMXMLWithDSMResp:
    """
    
            The response for importObjectsFromPLMXMLWithDSM operation. It holds the file read
            tickets for uploading the Dataset named reference files, the file read ticket for
            the import log file, and any partial failures.
            
    """
    def __init__(self, ) -> None: ...
    NamedRefPLMDFileTickets: list[str]
    """
            The FMS read tickets are used to upload the Dataset named reference files. These
            files are in .plmd format. On Teamcenster services client, files must be uploaded
            using these tickets thru Data Share Manager system after the calling of this operation.
            The API DownloadFilesWithDM from IFileManager class can be used to perform the upload.
            """
    LogFileTicket: Teamcenter.Services.Strong.Globalmultisite._2010_04.ImportExport.FileTicket
    """
            The FMS read ticket is used to download the generated import log file from the FMS
            transient volume. The API DownLoadTransientFile from FmsFileCacheProxy can be used
            to perform the download.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data contains the errors."""

class ImportExport:
    """
    Interface ImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ImportObjectsFromPLMXMLWithDSM(self, XmlFileTicket: str, NamedRefFolderPath: str, Transfermode: Teamcenter.Soa.Client.Model.Strong.TransferMode, IcRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision, SessionOptions: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues]) -> ImportObjectsFromPLMXMLWithDSMResp: ...

