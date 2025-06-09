import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CommitDatasetFileInfo:
    """
    
            Used in the commitDatasetFiles operation
            to pass information for committing ImanFile instances uploaded to a Teamcenter
            volume with the associated Dataset instances.
            
    """
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            The Dataset object to which the ImanFile object(s) representing the
            data files uploaded to the Teamcenter volume.
            """
    CreateNewVersion: bool
    """
            If this flag is true, a new DatasetRevision will be created to reference the
            new set of files uploaded to the Teamcenter volume.  Any existing DatasetRevision
            will be unaltered, but the new DatasetRevision will have the files attached
            as named references.
            
            If this flag is false, the uploaded files are attached to the current most recent
            DatasetRevision of this Dataset as named references.
            
"""
    DatasetFileTicketInfos: list[DatasetFileTicketInfo]
    """
            A vector of DatasetFileTicketInfo objects representing each ImanFile
            object attached to the given Dataset as a named reference.
            """

class DatasetFileInfo:
    """
    The structure defining the basic information for a file to be uploaded to a Dataset.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            An identifier defined by the caller to track the related object.
            
"""
    FileName: str
    """
            The name of the file to be uploaded.
            
            This is the filename only and should not contain the path to the filename.
            
            Exception: When used with the FileManagementUtility::putFiles()
            operation, this should contain the full path and file name.
            """
    NamedReferencedName: str
    """The named reference relation to the file."""
    IsText: bool
    """A flag to indicate if the file is text (TRUE) or binary (FALSE)."""
    AllowReplace: bool
    """A flag to indicate if the file may be overwritten (TRUE) or not (FALSE)."""

class DatasetFileTicketInfo:
    """
    
            A structure representing an ImanFile object attached to a given Dataset
            as a named reference.
            
    """
    def __init__(self, ) -> None: ...
    DatasetFileInfo: DatasetFileInfo
    """The structure defining the basic information for a file to be uploaded to a Dataset."""
    Ticket: str
    """The FMS write ticket used to transfer the file to the appropriate Teamcenter volume."""

class FileTicketsResponse:
    """
    
            Holds a ServiceData object and a map (ImanFile,
            string) of read tickets.  If the request completes successfully, each input ImanFile
            object will appear as a key in the output map
            
            and the string value associated with each entry will be a valid FMS ticket associated
            with that ImanFile.  Returned from the getFileReadTickets
            operation.
            
    """
    def __init__(self, ) -> None: ...
    Tickets: System.Collections.Hashtable
    """
            A map of the input ImanFile objects to FMS tickets used to access files in
            the Teamcenter volume.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The Teamcenter Services structure used to return status of the operation.  Any errors
            that occurred during the operation are returned here.
            """

class GetDatasetWriteTicketsInputData:
    """
    
            A vector of GetDatasetWriteTicketsInputData
            structures which holds the Dataset objects and related DatasetFileTicketInfo.  The calling client must construct this
            input.
            
    """
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            The Dataset object to which the ImanFile object(s) representing the
            data files uploaded to the Teamcenter volume are associated.
            """
    CreateNewVersion: bool
    """
            If this flag is true, a new DatasetRevision will be created to reference the
            new set of files uploaded to the Teamcenter volume.  Any existing DatasetRevision
            will be unaltered, but the new DatasetRevision will have the files attached
            as named references.
            
            If this flag is false, the uploaded files are attached to the current most recent
            DatasetRevision of this Dataset as named references.
            
"""
    DatasetFileInfos: list[DatasetFileInfo]
    """
            A vector of DatasetFileInfo structures where
            each contains information specific to each Dataset to be created.
            """

class GetDatasetWriteTicketsResponse:
    """
    
            Holds a ServiceData object and a vector of
            dataset commit information.  If the request completes successfully, the information
            in the vector can be used to commit the Dataset to the database.
            
    """
    def __init__(self, ) -> None: ...
    CommitInfo: list[CommitDatasetFileInfo]
    """A vector of CommitDatasetFileInfo structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The Teamcenter Services structure used to return status of the operation.  Any errors
            that occurred during the operation are returned here.
            """

class FileManagement:
    """
    Interface FileManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CommitDatasetFiles(self, CommitInput: list[CommitDatasetFileInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation supports the upload (addition) of files to a Teamcenter volume.  The
             mechanism for a client application adding files to a Teamcenter volume contains several
             steps.  This mechanism is implemented in the com.teamcenter.soa.client.FileManagementUtility
             class, which provides this functionality to clients in a consistent, reusable package.
             The com.teamcenter.soa.client.FileManagementUtility
             class invokes this operation after successfully uploading a file to a Teamcenter
             volume.
             
             This operation was unintentionally published.  It is supported only for internal
             Siemens PLM purposes.  Customers should not invoke this operation.
             

Use Cases:

             This operation supports the upload (addition) of files representing named references
             of a Dataset object to a Teamcenter volume.
             

Dependencies:

             getDatasetWriteTickets
             

Teamcenter Component:

             FMS Tc Integration - The integration of the FMS with the Tc Server.
             
        :param CommitInput: 
                         The vector of <font face="courier" height="10">CommitDatasetFileInfo</font> structures
                         returned in the commitInfo element of the <font face="courier" height="10">GetDatasetWriteTicketsResponse</font>
                         structure returned by the <font face="courier" height="10">FileManagementService::getDatasetWriteTickets</font>
                         operation.  In the event of partial upload success, the <font face="courier" height="10">com.teamcenter.soa.client.FileManagementUtility</font>
                         class removes all of the <font face="courier" height="10">CommitDatasetFileInfo</font>
                         structures representing the files that failed to upload to the Teamcenter volume
                         from this vector, before invoking the <font face="courier" height="10">FileManagementService::commitDatasetFiles</font>
                         operation.
             
        :return: object.  This Teamcenter Services structure is used to return status of the operation.
             Any errors that occurred during the operation are returned here.
        """
        ...
    def GetDatasetWriteTickets(self, Inputs: list[GetDatasetWriteTicketsInputData]) -> GetDatasetWriteTicketsResponse:
        """    
             This operation obtains File Management System (FMS) write tickets and file storage
             information for a set of supplied Dataset objects. The write tickets are used
             to transfer files from a local storage to Teamcenter volume, and the file storage
             information can be used to commit Dataset objects referencing those transferred
             files.
             
             The caller will provide a vector of GetDatasetWriteTicketsInputData
             objects that contains one or more Dataset objects and information about each
             associated file (e.g., filename, text/binary flag, etc.).  Upon return, the GetDatasetWriteTicketsResponse object will contain
             FMS write tickets that can be used to upload the file to the Teamcenter volume, and
             Dataset information that can be used to commit the changes to the database
             by using the FileManagementService commitDatasetFiles() operation.
             
             This operation supports the upload (addition) of files representing named references
             of a Dataset object to a Teamcenter volume.
             
             This operation was unintentionally published.  It is supported only for internal
             Siemens PLM purposes.  Customers should not invoke this operation.
             

Use Cases:

             This operation supports the upload (addition) of files representing named references
             of a Dataset object to a Teamcenter volume.
             

Teamcenter Component:

             FMS Tc Integration - The integration of the FMS with the Tc Server.
             
        :param Inputs: 
                         A vector of <font face="courier" height="10">GetDatasetWriteTicketsInputData</font>
                         structures which holds the <b>Dataset</b> objects and related <font face="courier" height="10">DatasetFileTicketInfo</font>.  The calling client must construct this
                         input.
             
        :return: ().
        """
        ...
    def GetFileReadTickets(self, Files: list[Teamcenter.Soa.Client.Model.Strong.ImanFile]) -> FileTicketsResponse:
        """    
             This operation obtains File Management System (FMS) read tickets for a set of supplied
             
ImanFile objects.  The supplied tickets are used to transfer files from a
             Teamcenter volume
             
             to local storage.  The files input parameter
             contains a list of the ImanFile objects to be read
             
             from the Teamcenter volume and transferred to local storage.
             
             FMS requires tickets for all file transfers to and from Teamcenter volumes.  An FMS
             read ticket is
             
             required to obtain a file from a Teamcenter volume, while an FMS write ticket is
             needed to place a file in the Teamcenter volume.  It is often times more expedient
             to request several tickets at one time, especially if it is known ahead of time that
             many files will need to be moved.  For this reason, the caller may supply multiple
             ImanFile objects, for which FMS tickets are desired, in the input vector.
             
             This operation was unintentionally published.  It is supported only for internal
             Siemens PLM purposes.  Customers should not invoke this operation.
             

Use Cases:

             This operation supports the download of data files represented by ImanFile
             objects from a Teamcenter volume into a local client environment.
             

Teamcenter Component:

             FMS Tc Integration - The integration of the FMS with the Tc Server.
             
        :param Files: 

        :return: , string) of read tickets.
        """
        ...

