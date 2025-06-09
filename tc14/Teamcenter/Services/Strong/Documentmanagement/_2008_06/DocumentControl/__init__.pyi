import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FileInfo:
    """
    File information
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """The client id"""
    FileName: str
    """The file name"""
    NamedReferencedName: str
    """The Dataset named reference information."""
    IsText: bool
    """True means Text format, otherwise it is Binary format."""
    AllowReplace: bool
    """Allow to replace or not."""

class FileTicketInfo:
    """
    File ticket information structure
    """
    def __init__(self, ) -> None: ...
    FileInfo: FileInfo
    """The file information."""
    Ticket: str
    """The FMS ticket."""

class CommitDatasetInfo:
    """
    Commit dataset information
    """
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """The Dataset created."""
    DsTypeName: str
    """The Dataset type name."""
    FileTicketInfo: FileTicketInfo
    """The file ticket information."""

class GetAdditionalFilesForCheckinInputs:
    """
    The structure contains the item revision and file names.
    """
    def __init__(self, ) -> None: ...
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The item revision"""
    Filenames: list[str]
    """The full file path and file names."""

class GetAdditionalFilesForCheckinOutputs:
    """
    The structure contains the item revision and vector of CommitDatasetInfo structure.
    """
    def __init__(self, ) -> None: ...
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The item revision"""
    DatasetInfos: list[CommitDatasetInfo]
    """The dataset information."""

class GetAdditionalFilesForCheckinOutputsResponse:
    """
    The structure contains vector of GetAdditionalFilesForCheckinOutputs and the serviceData.
    """
    def __init__(self, ) -> None: ...
    Outs: list[GetAdditionalFilesForCheckinOutputs]
    """The vector of GetAdditionalFilesForCheckinOutputs."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class GetCheckinModeAndFilesOutputs:
    """
    
            The structure contains the ItemRevision and vector of file names and the check
            in mode.
            
    """
    def __init__(self, ) -> None: ...
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The ItemRevision business object"""
    Filenames: list[str]
    """
            The list of file names that are currently downloaded locally when the ItemRevision
            was checked out
            """
    Mode: str
    """The CheckIn mode"""

class GetCheckinModeAndFilesOutputsResponse:
    """
    The structure contains vector of getCheckinModeAndFilesOutput structure and serviceData.
    """
    def __init__(self, ) -> None: ...
    Outs: list[GetCheckinModeAndFilesOutputs]
    """The list of Struct GetCheckinModeAndFilesOutputs"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The Service Data. Partial errors and failures are updated and returned through this
            object
            """

class PostCreateInfo:
    """
    Post create information
    """
    def __init__(self, ) -> None: ...
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The ItemRevision business object that is newly created"""
    CommitInfos: list[CommitDatasetInfo]
    """The list of CommitDatasetInfo struct"""

class PostCreateInputs:
    """
    Document Management Post Create Inputs
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """The client id"""
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The newly created ItemRevision"""
    FileNames: list[str]
    """Attached file names"""

class PostCreateResponse:
    """
    Post Create Response structure
    """
    def __init__(self, ) -> None: ...
    Output: list[PostCreateInfo]
    """List of PostCreateInfo struct"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The Service Data. Partial errors and failures are updated and returned through this
            object
            """

class DocumentControl:
    """
    Interface DocumentControl
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAdditionalFilesForCheckin(self, Inputs: list[GetAdditionalFilesForCheckinInputs]) -> GetAdditionalFilesForCheckinOutputsResponse:
        """    
             This operation is used in conjunction with the getCheckinModeAndFiles operation during
             the Check In process. getCheckinModeAndFiles takes a list of ItemRevision objects
             that have been checked out, and returns the list of source files that have been downloaded
             to the client. This operation takes the list of downloaded files returned by getCheckinModeAndFiles,
             and returns the subset of those files that are eligible for Check In.
             

Use Cases:

Check In


             This method is called after the getCheckinModeAndFiles operation, but before the
             files are checked in.
             

Dependencies:

             getCheckinModeAndFiles
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param Inputs: 
                         The input is vector of GetAdditionalFilesForCheckinInputs structure.
             
        :return: 
        """
        ...
    def PostCreate(self, Input: list[PostCreateInputs]) -> PostCreateResponse:
        """    
             This operation is to be called by the client after the creation of the ItemRevision
             business object, if there are local files to be attached to the newly created ItemRevision.
             For ItemRevision under Item Revision Definition Control (IRDC) it will
             replace any datasets copied from a template with new datasets for the local files.
             The client will then need to import the local files in the volume based on the return
             information from the SOA.  For ItemRevision not under IRDC control,
             the commitInfos list field from the return PostCreateInfo
             structure for this ItemRevision will be empty.
             

Use Cases:

Create new item from the RAC

             During the new item create on RAC, if the ItemRevision business object is
             under IRDC control,  the Attach Files panel will be enabled in the create
             wizard dialog,  if user choose to attach local files in the Attach Files panel, the
             template files for the IRDC will be replaced for the newly created ItemRevision
             business object, and instead the new datasets will be created for the local files;
             if user choose not to attach any local files in the Attach Files panel, then the
             template files for the IRDC will be used for the newly created ItemRevision.
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param Input: 
                         input is the list of <font face="courier" height="10">PostCreateInput</font> structure,
                         which contains client id, <b>ItemRevision</b> business object and list of file names
             
        :return: 
        """
        ...
    def GetCheckinModeAndFiles(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> GetCheckinModeAndFilesOutputsResponse:
        """    
             Get the CheckIn mode and files for ItemRevision business objects.  This is
             called before CheckIn to get from the server the source files that are currently
             checked out and downloaded locally and how the system is going to search for translated
             files locally for CheckIn. The information here is going to be used to search additional
             files in the client.  If the ItemRevision business object is under Item Revision
             Definition Configuration (IRDC), the CheckIn mode value is retrieved from
             the IRDC object; otherwise it will be an empty string.
             
             CheckIn mode is used to check in translated files that are already in the directory
             with the source file or the first level subdirectory.
             
             There are three CheckIn modes:
             

Same File Name: Attaches and checks in the derived files only if
             they have the same name as the source dataset.
             
Any File Name: Attaches and checks in the derived files no matter
             what names they have.
             
None: Does not attach and check in any derived files.
             


             Refers to Business Modeler IDE Guide > Creating data model objects to represent objects
             in Teamcenter > Working with document management > Create an Item Revision definition
             configuration (IRDC) for more information, the Checkin mode is defined by
             Derived Visualization Files to Checkin from the IRDC Checkin Page Info tab.
             

Use Cases:

Check in ItemRevision under IRDC control

             When a user checks out an ItemRevision business object under IRDC control,
             the user has the option to download the source files into user local machine.  If
             the user then checks in the ItemRevision, the system will search for the translated
             files in the source file directory according to the specified CheckIn mode. This
             functionality supports client side rendering to provide the derived datasets.
             
             For example, there is case where some AutoCAD file cannot be converted to a certain
             format by the server; user can find the translated files in the local directory to
             check in instead.
             


Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param Inputs: 
                         The vector of <b>ItemRevision</b>s to be checked in
             
        :return: 
        """
        ...

