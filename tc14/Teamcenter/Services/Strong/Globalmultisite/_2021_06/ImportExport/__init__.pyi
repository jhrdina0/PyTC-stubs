import System
import System.Collections
import Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport
import Teamcenter.Soa.Client.Model
import typing

class ExportFilesOfflineFileInfo:
    """
    File information structure contain file property map.
    """
    def __init__(self, ) -> None: ...
    Properties: System.Collections.Hashtable

class ExportFilesOfflineResponse:
    """
    Response structure for exportFilesOffline operation.
    """
    def __init__(self, ) -> None: ...
    Files: list[ExportFilesOfflineFileInfo]
    """A list of exported ImanFile objects information."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data contains the partial errors."""

class ImportNXFileInfo:
    """
    
            Structure to hold UID of Dataset and file ticket for importing one NX native file
            into a corresponding NX Dataset.
            
    """
    def __init__(self, ) -> None: ...
    DatasetUid: str
    """
            UID for a NX Dataset:
            
            &#61607;    UGMASTER
            
            &#61607;    UGPART
            """
    Ticket: str
    """The FMS write ticket used to transfer the NX file to the transient volume."""

class ImportExport:
    """
    Interface ImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExportFilesOffline(self, Uids: list[str], Options: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue]) -> ExportFilesOfflineResponse: ...
    def ImportNXFiles(self, Inputs: list[ImportNXFileInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

