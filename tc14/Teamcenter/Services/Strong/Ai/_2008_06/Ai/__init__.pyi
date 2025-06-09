import System
import Teamcenter.Services.Strong.Ai._2006_03.Ai
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CompareConfigurationContextsResponse:
    """
    CompareConfigurationContextsResponse struct
    """
    def __init__(self, ) -> None: ...
    CompareResults: list[bool]
    """
            bool array pointing to the result in the compares. Only successful (true/false) are
            returned here.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            any partial errors are reported here. For example: if any pair comparison fails -
            that failed index with the failed message will be reported like this.
            """

class Configuration:
    """
    Configuration structure.
    """
    def __init__(self, ) -> None: ...
    ExistingWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """
BOMWindow representing the window from which target application was launched.
            Must be initialized to NULL by client if unused.
            """
    UseDefaultRevisionRule: bool
    """If true use default RevisionRule. Used if none of the above options are provided."""
    RevRuleName: str
    """
            Name of RevisionRule. Used if existingWindow and configuringObject are not
            provided.
            """
    VariantRule: Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef
    """
            ApplicationReference representing classic VariantRule.Used in case existingWindow
            is not provided and other options do not yield a VariantRule.
            """
    ConfiguringObject: Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef
    """
            A CollaborationContext or StructureContext object.Used if existingWindow
            is not provided.
            """

class ConfigurationContextPair:
    """
    ConfigurationContextPair struct
    """
    def __init__(self, ) -> None: ...
    Src: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """src configurationcontext object to use in compare"""
    Other: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """target configurationcontext object to use in compare."""

class GenerateScopedMultipleStructure2Response:
    """
    GenerateScopedMultipleStructure2Response struct
    """
    def __init__(self, ) -> None: ...
    Ticket: str
    """The transient file ticket to be used for downloading the generated plmxml"""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            partial failures are returned - along with object ids for each plmxml data could
            not be generated.
            """

class GenerateScopedSyncRequest2Response:
    """
    GenerateScopedSyncRequest2Response struct
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
    Config: Configuration
    """configuration to be used for the above set of objects."""
    RefContexts: list[ReferenceContext]
    """
            If passing process object, this parameter can be used to specify how to setup the
            reference Product/Plant structure for that Process. If unused, pass an empty vector.
            """

class ReferenceContext:
    """
    
            structure to specify the reference structure, in the case of process element like
            MEProcessRevision, MEOpRevision, a process APN etc.
            
    """
    def __init__(self, ) -> None: ...
    TopLineObject: Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef
    """
            ApplicationRef specifying the object to be set as the topline of the reference structure.
            It is optional if config structure's configuringObject is an StructureContext object.
            If not needed - pass an empty ApplicationRef.
            """
    Config: Configuration
    """configuration to be used to construct the reference window."""

class Ai:
    """
    Interface Ai
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CompareConfigurationContexts(self, ConfigurationsToCompare: list[ConfigurationContextPair]) -> CompareConfigurationContextsResponse:
        """    
             compareConfigurationContexts: allows clients to check if configurationcontext with
             different uids are equivalent or not. This is because a configurationcontext is used
             to capture runtime revisionrules and there might be 2 configurationcontext created
             with same set of runtime rules. This interface is for backward compatibility with
             Ai. configurationsToCompare pairs of configurationContexts to compare with one other.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param ConfigurationsToCompare: 
                         vector of configurations to compare.
             
        :return: a bool vector which has the results for successful comparisions - either true or
             false. Any pair that gives an error - the index of such a failed error is returned
             in the serviceData member.
        """
        ...
    def GenerateScopedMultipleStructure2(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[ObjectsWithConfig], ExportTransferMode: str, ServerMode: int) -> GenerateScopedMultipleStructure2Response:
        """    
             GenerateScopedMultiple2Structure: Same as GenerateScopedSyncRequest2 - except no
             aiObject is needed. If specified - it is only used to get the TransferMode (in case
             the exportTransferMode is not specified). objects or occurrence group objects - specified
             as application refs. The configuration is optional if the ids consist of StructureContexts.
             ApplicationRefs can be ids of occurrence from a previous export from TC, or APNs
             or AbsOccs, or OccurrenceGroup or an Item/Itemrev(only one in that last case). If
             the Appref is custom (non TcEng AppRef), occurrence appref must resolve to AbsOccurrence
             or APN ), or they can be ids of structure context/occurrence group objects. The return
             is the transient file ticket for the plmxml file generated. In case any of the input
             apprefs cannot be processed they will be returned in the data member of response.
             Errors during plmxml processing will be returned in partialerror as xml string, based
             on TcError.xsd in iman_data folder. Configuration structure can be used to specify
             default revrule (if true) all other fields are ignored. Basically, they are declared
             in the order of precedence (where duplication is possible).
             

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
    def GenerateScopedSyncRequest2(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[ObjectsWithConfig], RequestDetail: Teamcenter.Services.Strong.Ai._2006_03.Ai.RequestDetail) -> GenerateScopedSyncRequest2Response:
        """    
             generateScopedSyncRequest2: Generates a new Sync Request for the given occurrences
             (from any context) or Structure Context objects or occurrence group objects - specified
             as application refs. The configuration is optional if the ids consist of StructureContexts.
             ApplicationRefs can be ids of occurrence from a previous export from TC, or APNs
             or AbsOccs, or OccurrenceGroup or an Item/Itemrev(only one in that last case). If
             the Appref is custom (non TcEng AppRef), occurrence appref must resolve to AbsOccurrence
             or APN ), or they can be ids of structure context/occurrence group objects. The return
             will be the details of the newly created Sync Request. Note that the name, desc,
             scope, updateType of this request are based on the passed in requestDetail. The other
             fields of the RequestDetail are not used during input. In case any of the input apprefs
             cannot be processed they will be returned in the failedIndices structure. Errors
             during plmxml processing will be returned in partialerror , based on TcError.xsd
             in iman_data folder. This differs from generateScopedSyncRequest, in that it allows
             you to specify the reference structures for process.
             

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

