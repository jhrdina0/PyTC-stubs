import System
import Teamcenter.Services.Strong.Ai._2006_03.Ai
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class Configuration2:
    """
    Configuration structure.
    """
    def __init__(self, ) -> None: ...
    UseDefaultRevisionRule: bool
    """
            if true - the Teamcenter preferences are used to pick up the rev rule. Overrides
            everything if present.
            """
    RevRuleName: str
    """if id is NULLTAG, then used to specify the revisionrule by name."""
    VariantRule: Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef
    """ApplicationRef of a variantrule - only needed if revrule is being specified elsewhere."""
    ConfiguringObject: Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef
    """revisionrule object or structurecontext"""
    RelatedContexts: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef]
    """
            vector of ApplicationRefs specifying the structure contexts to help create the linked
            windows
            """

class GenerateScopedMultipleStructureResponse:
    """
    GenerateScopedMultipleStructureResponse struct
    """
    def __init__(self, ) -> None: ...
    Ticket: str
    """The transient file ticket to be used for downloading the generated plmxml"""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            partial failures are returned - along with object ids for each plmxml data could
            not be generated.
            """

class GenerateScopedSyncRequestResponse:
    """
    GenerateScopedSyncRequestResponse struct
    """
    def __init__(self, ) -> None: ...
    Request: Teamcenter.Soa.Client.Model.Strong.RequestObject
    """request"""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """partial failures are returned - object ids for each sync data could not be created."""

class ObjectsWithConfig:
    """
    structure to specify multiple objects with each set potentially having it's own configuration
    """
    def __init__(self, ) -> None: ...
    Apprefs: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef]
    """vector of ApplicationRefs specifying the objects to be included in the plmxml generation"""
    Config: Configuration2
    """configuration to be used for the above set of objects."""

class Ai:
    """
    Interface Ai
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GenerateScopedMultipleStructure(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[ObjectsWithConfig], ExportTransferMode: str, ServerMode: int) -> GenerateScopedMultipleStructureResponse:
        """    
             GenerateScopedMultipleStructure: Same as GenerateScopedSyncRequest - except no aiObject
             is needed. If specified - it is only used to get the TransferMode (in case the exportTransferMode
             is not specified). objects or occurrence group objects - specified as application
             refs. The configuration is optional if the ids consist of StructureContexts. ApplicationRefs
             can be ids of occurrence from a previous export from TC, or APNs or AbsOccs, or OccurrenceGroup
             or an Item/Itemrev(only one in that last case). If the Appref is custom (non TcEng
             AppRef), occurrence appref must resolve to AbsOccurrence or APN ), or they can be
             ids of structure context/occurrence group objects. The return is the transient file
             ticket for the plmxml file generated. In case any of the input apprefs cannot be
             processed they will be returned in the data member of response. Errors during plmxml
             processing will be returned in partialerror as xml string, based on TcError.xsd in
             iman_data folder. Configuration structure can be used to specify default revrule
             (if true) all other fields are ignored. Basically, they are declared in the order
             of precedence (where duplication is possible).
             

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
    def GenerateScopedSyncRequest(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[ObjectsWithConfig], RequestDetail: Teamcenter.Services.Strong.Ai._2006_03.Ai.RequestDetail) -> GenerateScopedSyncRequestResponse:
        """    
             Generates a new Sync Request for the given occurrences (from any context) or Structure
             Context objects or occurrence group objects - specified as application refs. The
             configuration is optional if the ids consist of StructureContexts. ApplicationRefs
             can be ids of occurrence from a previous export from TC, or APNs or AbsOccs, or OccurrenceGroup
             or an Item/Itemrev(only one in that last case). If the Appref is custom (non TcEng
             AppRef), occurrence appref must resolve to AbsOccurrence or APN ), or they can be
             ids of structure context/occurrence group objects. The return will be the details
             of the newly created Sync Request. Note that the name, desc, scope, updateType of
             this request are based on the passed in requestDetail. The other fields of the RequestDetail
             are not used during input. In case any of the input apprefs cannot be processed they
             will be returned in the failedIndices structure. Errors during plmxml processing
             will be returned in partialerror , based on TcError.xsd in iman_data folder.
             

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
             
        :param RequestDetail: 
                         The details (name, description, scope, updateType(incremental)) are used in the creation
                         of the sync request. Set the scope type to RequestScope_Whole and updatetype to UpdateType_Full
                         if this structure is not to be used.
             
        :return: partial failures are returned in data.
        """
        ...

