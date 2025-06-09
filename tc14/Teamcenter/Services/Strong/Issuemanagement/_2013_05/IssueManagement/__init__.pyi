import System
import Teamcenter.Soa.Client.Model
import typing

class AdditionalFiles:
    """
    
            Structure that contains file name, FMS download ticket and type information for additional
            files to download.
            
    """
    def __init__(self, ) -> None: ...
    FileTicket: str
    """The FMS ticket to download the file."""
    FileName: str
    """The file name."""
    FileType: str
    """The named reference name for the file or type."""

class GetIssueSceneFileInput:
    """
    The input to get issue scene files.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    PvDataset: Teamcenter.Soa.Client.Model.ModelObject
    """
            The product view dataset object that contains issue scene data files and assembly
            configuration.
            """
    AdditionalFiles: list[str]
    """List of product view dataset named reference names or types to download."""

class GetIssueSceneFileOutput:
    """
    Structure contains issue scene file names and file tickets to download.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the GetIssueSceneFileInput.clientId. This can be used by
            the caller to indentify this data structure with the source input data.
            """
    IssuesceneFileTicket: str
    """The FMS ticket for the  generated issue scene PLMXML file."""
    IssuesceneFileName: str
    """The issue scene PLMXML file name."""
    Files: list[AdditionalFiles]
    """Additional files that can be downloaded."""

class GetIssueSceneFileResp:
    """
    Get issue scene file response.
    """
    def __init__(self, ) -> None: ...
    Outputs: list[GetIssueSceneFileOutput]
    """GetIssueSceneFileOutput structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data that may contain error messages or partial errors."""

class IssueManagement:
    """
    Interface IssueManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetIssueSceneFiles(self, Inputs: list[GetIssueSceneFileInput]) -> GetIssueSceneFileResp:
        """    
             This operation builds a BOM window based on the product view dataset, traverses the
             BOM window and outputs a BomWriterExport flavored PLMXML file that lists visible
             BOM lines and contains view stat data. The applications (for example, NX Bookmark
             function) that support PLMXML in BomWriterExport format can download the generated
             PLMXML and other files from the product view dataset to launch issue scene.
             

Use Cases:

             NX Issue Tracking provides the functionalities to browse, capture and launch issue
             reports from NX environment in managed mode. NX calls this function with a product
             view dataset which is the snapshot for the issue. A generated BomWriterExport flavored
             PLMXML and other files can be downloaded and launch into NX to re-build issue scene.
             

Teamcenter Component:

             Issue Management - Teamcenter Issue Management is an application that allows users
             to capture issue, share issue data and collaborate on the business process to resolve
             issue in product life management.
             
        :param Inputs: 
                         Inputs to get issue scene files.
             
        :return: This operation returns the named reference names and FMS tickets for downloading
             the requested files. The following partial error may be returned: 261001 - Retrieve
             configuration context failed or the named reference does not exist 261002 - Rebuild
             BOM window from configuration context failed. 261003 - Retrieve view stat data from
             pv-view xml file failed. 261004 - Retrieve pv-view xml file failed or the file does
             not exist. 261005 - Retrieve pv-structure xml file failed or the file does not exist.
             261006 - Generate BomWriterExport flavored PLMXML file failed. 261007 - Download
             file failed.
        """
        ...

