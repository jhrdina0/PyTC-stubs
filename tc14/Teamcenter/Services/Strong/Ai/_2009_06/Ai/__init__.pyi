import System
import Teamcenter.Services.Strong.Ai._2008_06.Ai
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GenerateScopedMultipleStructure3Response:
    """
    GenerateScopedMultipleStructure3Response struct
    """
    def __init__(self, ) -> None: ...
    Ticket: str
    """The transient file ticket to be used for downloading the generated plmxml"""
    FileTickets: list[str]
    """The transient file tickets for any files exported during generation of plmxml"""
    RelativeFolderName: str
    """
            Name of the folder where the transient fileTickets have to be downloaded relative
            to the folder where plmxml file is downloaded.
            """
    FileNames: list[str]
    """filenames as they appear in the transient volume under the plmxml created folder."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            partial failures are returned - along with object ids for each plmxml data could
            not be generated.
            """

class Ai:
    """
    Interface Ai
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPersistentObjects(self, InputLines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Given a set of bomlines from the same window, create a private structure context
             and return that. If the input contains any persistent objects like a workspaceobject
             - those will be returned as is.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param InputLines: 
                         list of bomlines from the same bomwindow, for which a StructureContext needs to be
                         created. Note that if input has persistent objects - they will be returned as is.
             
        :return: The serviceData willl have any newly created StructureContext object and partialErrors.
             In addition - if any persistent objects are passed in - they will be returned as
             objects.
        """
        ...
    def GenerateScopedMultipleStructure3(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[Teamcenter.Services.Strong.Ai._2008_06.Ai.ObjectsWithConfig], ExportTransferMode: str, ServerMode: int) -> GenerateScopedMultipleStructure3Response:
        """    
             GenerateScopedMultipleStructure3: Same as GenerateScopedMultipleStructure2 - except
             filetickets are returned. If aiObject is specified - it is only used to get the TransferMode
             (in case the exportTransferMode is not specified). objects or occurrence group objects
             - specified as application refs. The configuration is optional if the ids consist
             of StructureContexts. ApplicationRefs can be ids of occurrence from a previous export
             from TC, or APNs or AbsOccs, or OccurrenceGroup or an Item/Itemrev(only one in that
             last case). If the Appref is custom (non TcEng AppRef), occurrence appref must resolve
             to AbsOccurrence or APN ), or they can be ids of structure context/occurrence group
             objects. The return is the transient file ticket for the plmxml file generated. In
             case any of the input apprefs cannot be processed they will be returned in the data
             member of response. Errors during plmxml processing will be returned in partialerror
             as xml string, based on TcError.xsd in iman_data folder. Configuration structure
             can be used to specify default revrule (if true) all other fields are ignored. Basically,
             they are declared in the order of precedence (where duplication is possible).
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param AiObject: 
                         The Application Interface object under which the new sync request is to be created.
             
        :param ObjectsToProcess: 
                         The list of objects for which a single plmxml will be generated. The configuration
                         for each of the                             object is also specified here.
             
        :param ExportTransferMode: 
                         Name of the transfermode for exporting plmxml.
             
        :param ServerMode: 
                         values are 2 or 4 (2-tier or 4-tier). Used in the generation of transient ticket.
             
        :return: partial failures are returned in data.
        """
        ...

