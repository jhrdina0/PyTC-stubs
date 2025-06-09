import System
import Teamcenter.Services.Strong.Core._2006_03.FileManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ReplaceFileInput:
    """
    
            This structure contains the input to the replaceFiles
            operation.  This includes the transient volume write ticket used to upload the new
            file.  This is the FMS write ticket issued by the getTransientFileTicketsForUpload
            operation.  The replaceFiles operation uses
            this ticket to locate the data file in the transient volume.  This structure also
            includes a flag to indicate if the original file name should be updated.
            
    """
    def __init__(self, ) -> None: ...
    ImanFile: Teamcenter.Soa.Client.Model.Strong.ImanFile
    """The ImanFile object whose file is to be replaced."""
    NewFileTicket: str
    """
            The transient file write ticket that was used to upload the new file to the transient
            volume.
            """
    RetainOriginalFileName: bool
    """
            If set to true, the original file name of the ImanFile object will not be
            changed.  If false, the original file name will be changed to the file name of the
            new file as set in newFileTicket.
            """

class FileManagement:
    """
    Interface FileManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CommitDatasetFilesInBulk(self, CommitInput: list[Teamcenter.Services.Strong.Core._2006_03.FileManagement.CommitDatasetFileInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ReplaceFiles(self, Inputs: list[ReplaceFileInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation replaces an existing volume file with a new file that has already
             been uploaded to a transient volume.  It uploads the file from the transient volume
             to the regular Teamcenter volume.  The original volume file is replaced with the
             new file, and the ImanFile references the new file.  Note that there is no
             new ImanFile object created.  This operation includes the ability to change
             the original file name or retain its existing value.  The file type on the ImanFile
             object is updated to match the value from the input write tickets.  The tickets for
             the upload to the transient volume can be obtained by calling getTransientFileTicketsForUpload.
             

             This operation is used for replacing an existing file in a volume when the original
             file content is to be replaced with a newly encrypted file.
             

Use Cases:

             There are very specific cases where this operation should be used. One use case is
             where encryption software needs to replace the contents of the original file with
             the encrypted contents.
             

Dependencies:

             getTransientFileTicketsForUpload
             

Teamcenter Component:

             FMS Tc Integration - The integration of the FMS with the Tc Server.
             
        :param Inputs: 
                         The input to this operation includes a list of write tickets used to upload the new
                         file to the transient volume.  It also includes a flag to indicate if the original
                         file name on the <b>ImanFile</b> should be updated to match the new file.  This new
                         file replaces the existing file referenced by the <b>ImanFile</b> object.
             
        :return: 
        """
        ...

