import Teamcenter.Soa.Client.Model
import typing

class GetTransientFileTicketsResponse:
    """
    
            Holds the response returned from the getTransientFileTicketsForUpload
            operation.
            
    """
    def __init__(self, ) -> None: ...
    TransientFileTicketInfos: list[TransientFileTicketInfo]
    """The requested transient files ticket information."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """This contains the status of the operation."""

class TransientFileInfo:
    """
    Holds the basic information for a file to be uploaded.
    """
    def __init__(self, ) -> None: ...
    FileName: str
    """The name of the file. Path of the file should not be supplied."""
    IsBinary: bool
    """True if the file is of binary type, false for text files."""
    DeleteFlag: bool
    """True if the file should be deleted from temporary storage after it is read."""

class TransientFileTicketInfo:
    """
    Holds the file information with a ticket added.
    """
    def __init__(self, ) -> None: ...
    TransientFileInfo: TransientFileInfo
    """The unique identifier of the file to be uploaded."""
    Ticket: str
    """Holds the basic information for a file to be uploaded."""

class FileManagement:
    """
    Interface FileManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetTransientFileTicketsForUpload(self, TransientFileInfos: list[TransientFileInfo]) -> GetTransientFileTicketsResponse:
        """    
             This operation gets the tickets for the desired files to be uploaded to the transient
             volume. These tickets can be used to upload corresponding files via FileManagementUtility::putFileViaTicket. The TransientFileInfo contains the basic information for a file to
             be uploaded such as file name, file type and whether the file should be deleted after
             reading.
             

Use Cases:

             This operation supports the uploading of files into the FMS transient volume.
             

Teamcenter Component:

             FMS Tc Integration - The integration of the FMS with the Tc Server.
             
        :param TransientFileInfos: 
                         List containing the details of the files for which the tickets are requested.
             
        :return: structure,
             which will contain the file tickets and status of the operation.
        """
        ...

