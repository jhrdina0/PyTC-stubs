import System
import System.Collections
import Teamcenter.Services.Strong.Manufacturing._2008_06.Core
import Teamcenter.Services.Strong.Manufacturing._2008_06.DataManagement
import Teamcenter.Services.Strong.Manufacturing._2008_06.TimeManagement
import Teamcenter.Services.Strong.Manufacturing._2008_12.IPAManagement
import Teamcenter.Services.Strong.Manufacturing._2009_06.StructureManagement
import Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement
import Teamcenter.Services.Strong.Manufacturing._2009_10.MFGPropertyCollector
import Teamcenter.Services.Strong.Manufacturing._2009_10.Model
import Teamcenter.Services.Strong.Manufacturing._2009_10.ModelDefinitions
import Teamcenter.Services.Strong.Manufacturing._2009_10.StructureManagement
import Teamcenter.Services.Strong.Manufacturing._2009_10.StructureSearch
import Teamcenter.Services.Strong.Manufacturing._2010_09.Core
import Teamcenter.Services.Strong.Manufacturing._2010_09.ImportExport
import Teamcenter.Services.Strong.Manufacturing._2010_09.TimeManagement
import Teamcenter.Services.Strong.Manufacturing._2011_06.DataManagement
import Teamcenter.Services.Strong.Manufacturing._2011_06.StructureManagement
import Teamcenter.Services.Strong.Manufacturing._2012_02.Constraints
import Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement
import Teamcenter.Services.Strong.Manufacturing._2012_02.IPAManagement
import Teamcenter.Services.Strong.Manufacturing._2012_02.Model
import Teamcenter.Services.Strong.Manufacturing._2012_09.DataManagement
import Teamcenter.Services.Strong.Manufacturing._2012_09.Validation
import Teamcenter.Services.Strong.Manufacturing._2013_05.Core
import Teamcenter.Services.Strong.Manufacturing._2013_05.DataManagement
import Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement
import Teamcenter.Services.Strong.Manufacturing._2013_05.ImportExport
import Teamcenter.Services.Strong.Manufacturing._2013_05.StructureManagement
import Teamcenter.Services.Strong.Manufacturing._2013_05.StructureSearch
import Teamcenter.Services.Strong.Manufacturing._2013_05.TimeWayPlan
import Teamcenter.Services.Strong.Manufacturing._2013_12.Model
import Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement
import Teamcenter.Services.Strong.Manufacturing._2014_06.DataManagement
import Teamcenter.Services.Strong.Manufacturing._2014_06.ResourceManagement
import Teamcenter.Services.Strong.Manufacturing._2014_06.StructureSearch
import Teamcenter.Services.Strong.Manufacturing._2014_12.IPAManagement
import Teamcenter.Services.Strong.Manufacturing._2014_12.Model
import Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch
import Teamcenter.Services.Strong.Manufacturing._2014_12.Validation
import Teamcenter.Services.Strong.Manufacturing._2015_03.StructureManagement
import Teamcenter.Services.Strong.Manufacturing._2015_10.ImportExport
import Teamcenter.Services.Strong.Manufacturing._2015_10.StructureManagement
import Teamcenter.Services.Strong.Manufacturing._2016_03.ImportExport
import Teamcenter.Services.Strong.Manufacturing._2017_05.ImportExport
import Teamcenter.Services.Strong.Manufacturing._2017_05.Validation
import Teamcenter.Services.Strong.Manufacturing._2017_11.DataManagement
import Teamcenter.Services.Strong.Manufacturing._2018_06.DataManagement
import Teamcenter.Services.Strong.Manufacturing._2018_11.StructureManagement
import Teamcenter.Services.Strong.Manufacturing._2019_06.DataManagement
import Teamcenter.Services.Strong.Manufacturing._2020_04.Core
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ConstraintsRestBindingStub(ConstraintsService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetPrecedenceConstraintPaths(self, InputData: list[Teamcenter.Services.Strong.Manufacturing._2012_02.Constraints.GetPrecedenceConstraintPathsInputs]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.Constraints.GetPrecedenceConstraintPathsResponse: ...
    def GetPrecedenceConstraints(self, InputData: list[Teamcenter.Services.Strong.Manufacturing._2012_02.Constraints.GetPrecedenceConstraintsIn]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.Constraints.GetPrecedenceConstraintsResponse: ...
    def ValidateConstraintConsistency(self, InputData: list[Teamcenter.Services.Strong.Manufacturing._2012_02.Constraints.ValidateConstraintConsistencyInputs]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.Constraints.ValidateConstraintConsistencyResponse: ...
    def ValidateProcessAreaAssignments(self, InputData: list[Teamcenter.Services.Strong.Manufacturing._2012_02.Constraints.ValidateProcessAreaAssignmentsInputs]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.Constraints.ValidateProcessAreaAssignmentsResponse: ...

class ConstraintsService:
    """
    
            Contains service methods to fetch/validate constraints
            


Library Reference:

TcSoaManufacturingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ConstraintsService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetPrecedenceConstraintPaths(self, InputData: list[Teamcenter.Services.Strong.Manufacturing._2012_02.Constraints.GetPrecedenceConstraintPathsInputs]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.Constraints.GetPrecedenceConstraintPathsResponse:
        """    
             Returns all operations/processes in the precedence chain starting from the given
             start operation/process up to the end operation/process, i.e., all operations/processes
             succeeding the start operation/process and preceding the end operation/process.
             
        :param InputData: 
                         The input data contains the list of start and end operation or process lines.
             
        :return: A structure holding a vector of constraint paths for each input structure.
        """
        ...
    def GetPrecedenceConstraints(self, InputData: list[Teamcenter.Services.Strong.Manufacturing._2012_02.Constraints.GetPrecedenceConstraintsIn]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.Constraints.GetPrecedenceConstraintsResponse:
        """    
             Fetches all precedence constraints defined on the given input objects - traverses
             'm' levels in the predecessor chain and 'n' levels in the successor chain.
             
        :param InputData: 
                         The list of input objects (Mfg0BvrProcess / Mfg0BvrOperation) whose precedence constraints
                         are to be fetched along with the number of levels to be traversed in the predecessor
                         and successor chains.
             
        :return: Returns a map of predecessors and successors for each object
        """
        ...
    def ValidateConstraintConsistency(self, InputData: list[Teamcenter.Services.Strong.Manufacturing._2012_02.Constraints.ValidateConstraintConsistencyInputs]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.Constraints.ValidateConstraintConsistencyResponse:
        """    
             This SOA invokes the consistency check service. It checks whether the constraints
             defined in the product BOP or a sub structure thereof are consistent.
             
        :param InputData: 
                         A vector of ValidateConstraintConsistencyInputs structures that defines one or multiple
                         substructures to check.
             
        :return: A set of error descriptions for each input structure.
        """
        ...
    def ValidateProcessAreaAssignments(self, InputData: list[Teamcenter.Services.Strong.Manufacturing._2012_02.Constraints.ValidateProcessAreaAssignmentsInputs]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.Constraints.ValidateProcessAreaAssignmentsResponse:
        """    
             This SOA invokes the constraint validation service. It checks whether the assignments
             of operations or processes of a Product BOP to process areas in a Plant BOP are consistent
             with the constraint definitions.
             
        :param InputData: 
                         A vector of ValidateProcessAreaAssignmentsInputs structures that define the the Plant
                         and Product BOPs and the set of nodes to validate in the Plant BOP.
             
        :return: A structure that contains a list of errors for each input structure.
        """
        ...

class CoreRestBindingStub(CoreService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def FindCheckedOutsInStructure(self, SearchScope: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2008_06.Core.FindCheckedOutsInStructureResponse: ...
    @typing.overload
    def FindNodeInContext(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2010_09.Core.FindNodeInContextInputInfo]) -> Teamcenter.Services.Strong.Manufacturing._2010_09.Core.FindNodeInContextResponse: ...
    @typing.overload
    def FindNodeInContext(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2013_05.Core.FindNodeInContextInputInfo]) -> Teamcenter.Services.Strong.Manufacturing._2010_09.Core.FindNodeInContextResponse: ...
    def GetAffectedProperties(self, Arguments: list[Teamcenter.Services.Strong.Manufacturing._2010_09.Core.GetAffectedPropertiesArg], RequestedProperties: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def MatchObjectsAgainstVariantRules(self, Args: list[Teamcenter.Services.Strong.Manufacturing._2013_05.Core.MatchObjectsAgainstVariantRulesArg]) -> Teamcenter.Services.Strong.Manufacturing._2013_05.Core.MatchObjectsAgainstVariantRulesResponse: ...
    def CancelManufacturingCheckout(self, RootObjects: list[Teamcenter.Soa.Client.Model.ModelObject], AdditionalInfo: Teamcenter.Services.Strong.Manufacturing._2020_04.Core.AdditionalInfo) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class CoreService:
    """
    
            Contains Core Services
            


Library Reference:

TcSoaManufacturingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> CoreService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def FindCheckedOutsInStructure(self, SearchScope: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2008_06.Core.FindCheckedOutsInStructureResponse:
        """    Finds all the checked out items in the objects.
        :param SearchScope: 
                         Vector of lines, that we would like to get all the checked out objects from.
             
        :return: Structure that contains a vector of all the checked out objects in search scope,
             also holds services exceptions.
        """
        ...
    @typing.overload
    def FindNodeInContext(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2010_09.Core.FindNodeInContextInputInfo]) -> Teamcenter.Services.Strong.Manufacturing._2010_09.Core.FindNodeInContextResponse: ...
    @typing.overload
    def FindNodeInContext(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2013_05.Core.FindNodeInContextInputInfo]) -> Teamcenter.Services.Strong.Manufacturing._2010_09.Core.FindNodeInContextResponse: ...
    def GetAffectedProperties(self, Arguments: list[Teamcenter.Services.Strong.Manufacturing._2010_09.Core.GetAffectedPropertiesArg], RequestedProperties: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Returns the runtime properties of dependent nodes which are affected when the duration
             of one or more nodes has been changed in a process or operation structure.
             
        :param Arguments: 
                         A list of GetAffectedPropertiesChanges structures that describe the changes that
                         have been made to a process or operation structure.
             
        :param RequestedProperties: 
                         The names of the properties that are to be retrieved. In the first version only the
                         properties that are processed by the Gantt application are accepted (Mfg0calc_duration,
                         Mfg0calc_start_time, Mfg0calc_dur_start_time).
             
        :return: A ServiceData structure that contains the computed property values in the DataObject
             member. The structure also informs about errors that occurred during the course of
             the operation.
        """
        ...
    def MatchObjectsAgainstVariantRules(self, Args: list[Teamcenter.Services.Strong.Manufacturing._2013_05.Core.MatchObjectsAgainstVariantRulesArg]) -> Teamcenter.Services.Strong.Manufacturing._2013_05.Core.MatchObjectsAgainstVariantRulesResponse:
        """    
             This operation takes a list of pairs of runtime object and variant rule lists and
             determines for each object/variant rule combination of each pair whether the object
             is configured-in for the specified variant rule. Thereby it takes all aspects of
             an object into account that determine the visibility of the object, such as the variant
             conditions of the object itself and of all its parent objects as well as the conditions
             of any assigned object and that of its respective parent objects. The results will
             depend on the configuration state for IC, revision rule, effectivity etc of the implied
             windows, including reference windows.
             
             If a variant rule supplied in the arguments list is not matched by the variant configuration
             of any involved window a warning message will be added to the response structure,
             which indicates that the visibility check regarding the specific variant rule cannot
             be reliably performed because the configuration of the window contradicts the variant
             rule.
             
             This operation currently does not support modular variants. Only saved variant rules
             (business object VariantRule) for the classic variant model are accepted or
             alternatively,  product variants (type Mfg0BvrProductVariant) which are linked
             to VariantRule objects.
             

        :param Args: 
                         A list of structures, where each entry describes a list of runtime objects and a
                         list of variant rules or product variants that are matched against each other.
             
        :return: 300062: If there is no variant rule associated with a product variant.
        """
        ...
    def CancelManufacturingCheckout(self, RootObjects: list[Teamcenter.Soa.Client.Model.ModelObject], AdditionalInfo: Teamcenter.Services.Strong.Manufacturing._2020_04.Core.AdditionalInfo) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class DataManagementRestBindingStub(DataManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateOrUpdateMEActivityFolders(self, ActivityInfos: list[Teamcenter.Services.Strong.Manufacturing._2008_06.DataManagement.MEActivityFolderInfo]) -> Teamcenter.Services.Strong.Manufacturing._2008_06.DataManagement.CreateOrUpdateMEActivityFolderResponse: ...
    def CreateOrUpdateMENXObjects(self, MeObjectInfos: list[Teamcenter.Services.Strong.Manufacturing._2008_06.DataManagement.MENXObjectInfo], Container: Teamcenter.Soa.Client.Model.Strong.Folder) -> Teamcenter.Services.Strong.Manufacturing._2008_06.DataManagement.CreateOrUpdateMENXObjectResponse: ...
    def CreateObjects(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement.CreateIn]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement.CreateResponse: ...
    def DisconnectObjects(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement.DisconnectInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CloseContexts(self, Contexts: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CloseViews(self, StructureContext: Teamcenter.Soa.Client.Model.ModelObject, Views: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def OpenContexts(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2011_06.DataManagement.OpenContextInput]) -> Teamcenter.Services.Strong.Manufacturing._2011_06.DataManagement.OpenContextsResponse: ...
    def OpenViews(self, Context: Teamcenter.Soa.Client.Model.ModelObject, StructureContext: Teamcenter.Soa.Client.Model.ModelObject, Views: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2011_06.DataManagement.OpenViewsResponse: ...
    def AddAssociatedContexts(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AddAssociationInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def AssociateAndAllocateByPreview(self, Input: Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AssociateAndAllocateInput, AllocationMap: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AssociateAndAllocateResponse: ...
    def AutomaticAllocatePreview(self, Input: Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AssociateAndAllocateInput) -> Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AutomaticAllocatePreviewResponse: ...
    def AutomaticAssociateAndAllocate(self, Input: Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AssociateAndAllocateInput) -> Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AssociateAndAllocateResponse: ...
    def ConnectObjects(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.ConnectObjectsInputData]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.ConnectObjectResponse: ...
    def DisconnectFromOrigin(self, InputVector: list[Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.DisconnectFromOriginInputData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetAssociatedContexts(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.GetAssociatedContextsInputData]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AssociationResponse: ...
    def ApplyConfigObjects(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2012_09.DataManagement.ApplyConfigInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateOrUpdateConfigObjects(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2012_09.DataManagement.CreateConfigInput]) -> Teamcenter.Services.Strong.Manufacturing._2012_09.DataManagement.CreateConfigResponse: ...
    def CreateAttachments(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement.CreateIn]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement.CreateResponse: ...
    def SetAttributes(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2013_05.DataManagement.ObjectAttributesInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SyncStudyAndSource(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2013_05.DataManagement.SyncStudyInput]) -> Teamcenter.Services.Strong.Manufacturing._2013_05.DataManagement.SyncStudyResponse: ...
    def AddOrRemoveAssociatedContexts(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2014_06.DataManagement.AddOrRemoveContextsInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def EstablishOriginLink(self, Input: Teamcenter.Services.Strong.Manufacturing._2014_06.DataManagement.EstablishOriginLinkInfo) -> Teamcenter.Services.Strong.Manufacturing._2014_06.DataManagement.EstablishOriginLinkResponse: ...
    def GetProcessResourceRelatedInfo(self, Input: list[Teamcenter.Soa.Client.Model.ModelObject], ObjectPreference: str) -> Teamcenter.Services.Strong.Manufacturing._2014_06.DataManagement.ProcResourceResponseInfo: ...
    def CloneAssemblyAndProcessObjects(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2014_06.DataManagement.CloneAssemblyInputData]) -> Teamcenter.Services.Strong.Manufacturing._2014_06.DataManagement.CloneAssemblyResponse: ...
    def GetConnectorInfo(self, ItemRevs: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2017_11.DataManagement.GetConnectorResponse: ...
    def GetPhysicalAttachmentsInScope(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2017_11.DataManagement.GetPhysicalAttachmentsInput]) -> Teamcenter.Services.Strong.Manufacturing._2017_11.DataManagement.GetPhysicalAttachmentsResponse: ...
    def RemovePhysicalAttachementRelation(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2017_11.DataManagement.RemovePhysicalAttachmentRelInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetConnectorInfo(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2017_11.DataManagement.SetConnectorInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetPhysicalAttachementsInScope(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2017_11.DataManagement.SetPhysicalAttachmentsInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetOccurrenceKinematicsInformation(self, OccKinematicsInfoinput: list[Teamcenter.Services.Strong.Manufacturing._2018_06.DataManagement.GetOccKinematicsInfoInput]) -> Teamcenter.Services.Strong.Manufacturing._2018_06.DataManagement.GetOccurrenceKinematicsInfoResponse: ...
    def SetOccurrenceKinematicsInformation(self, OccInfoInputMap: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def PublishSelectionFromStudyToSource(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2019_06.DataManagement.SelectedSyncPublishStudyInput]) -> Teamcenter.Services.Strong.Manufacturing._2019_06.DataManagement.SelectedStudySourceResponse: ...
    def SyncSelectionInStudyWithSource(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2019_06.DataManagement.SelectedSyncPublishStudyInput]) -> Teamcenter.Services.Strong.Manufacturing._2019_06.DataManagement.SelectedStudySourceResponse: ...

class DataManagementService:
    """
    
            This service provides operations to perform data management related functionalities
            on a given input.
            

            Use cases supported by this service include:
            

Creation of manufacturing objects .
            
Connect and disconnect manufacturing objects.
            
Open and close the manufacturing contexts and views.
            
Create IDIC for assembly parts in EBOM and PMI contexts.
            
Allocation from source Prouduct BOP to a target Plant BOP on the
            basis of reference Product BOP
            
Add, remove or retrieve associated contexts for the given input context.
            
Create, update or apply the configuration object based on the given
            input.
            
Automatically assign the manufacturing feature objects from source
            structure to the given target structure.
            
Clone and assembly in mBOM as a reaction to changes in eBOM planning
            or clone a process in Bill of Process as a reaction to changes in mBOM.
            
Create, link and synchronize twin PlantBOP or Bill of Equipment structure.
            
Set, retrieve or remove the physical attachment relations for the
            given inputs.
            
Set or retrieve the kinematics information for the given input.
            
Publish or synchronize the Mfg0BvrSimStudy structure to the associated
            Bill of Process structure.
            




Library Reference:

TcSoaManufacturingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DataManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateOrUpdateMEActivityFolders(self, ActivityInfos: list[Teamcenter.Services.Strong.Manufacturing._2008_06.DataManagement.MEActivityFolderInfo]) -> Teamcenter.Services.Strong.Manufacturing._2008_06.DataManagement.CreateOrUpdateMEActivityFolderResponse:
        """    
             Allows the user to create and/or update a MEActivityFolder.  If the given MEActivity
             object exists but the input attribute values that differ from those already set,
             an attempt is made to update the values if possible. If multiple level of sub activities
             are to be created those activities can be passed in as the objects if they already
             exist in database. The created folder and updated folders are returned to the client
             through the createdObjects and updatedObject list of the service data respectively.
             
        :param ActivityInfos: 
                         Input is a vector of MEActivityFolderInfo structs. A Boolean value part of the structure
                         signifying if the input data represents the complete representation of the folder
                         tools, predecessors, and contents or if it represents objects to be appended to the
                         existing folder tools, predecessors, and contents (folder context information) if
                         complete is true, then the expectation is that the entire folder context information
                         is supplied and any folder context not supplied that currently exist in Teamcenter
                         will be removed from the folder context, if complete is false, the input context
                         elements will be appended to the input folder.
             
        :return: contains map between the index of the input structure and the created or updated
             object, All Object ids that were successfully created or updated are added to ServiceData.
             Objects/object ids that failed the find are returned in a list of failures in the
             ServiceData with its index.
        """
        ...
    def CreateOrUpdateMENXObjects(self, MeObjectInfos: list[Teamcenter.Services.Strong.Manufacturing._2008_06.DataManagement.MENXObjectInfo], Container: Teamcenter.Soa.Client.Model.Strong.Folder) -> Teamcenter.Services.Strong.Manufacturing._2008_06.DataManagement.CreateOrUpdateMENXObjectResponse:
        """    
             Allows the user to create and/or update a MENXObject. If the given MENXObject object
             exists but the input attribute values that differ from those already set, an attempt
             is made to update the values if possible.
             
        :param MeObjectInfos: 
                         Input is a vector of MENXObjectInfo structs.
             
        :param Container: 
                         The folder into which the created objects are to be placed. This can be a NULLTAG
                         in which case the created objects will not be inserted into any folder.
             
        :return: contains map between the index of the input structure and the created or updated
             object, All Object ids that were successfully created or updated are added to ServiceData.
             Objects/object ids that failed the find are returned in a list of failures in the
             ServiceData with its index.
        """
        ...
    def CreateObjects(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement.CreateIn]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement.CreateResponse:
        """    
             Generic operation for creation of manufacturing objects. This will also create any
             secondary(compounded) objects that need to be created, assuming the CreateInput for
             the secondary object is represented in the recursive CreateInput object e.g. Item
             is Primary Object that also creates ItemMasterForm, ItemRevision and ItemRevision
             in turn creates ItemRevisionMasterForm. The input for all these levels is passed
             in through the recursive CreateInput object. This operation creates the persistent
             objects and the runtime objects accordingly. This operation also connects the created
             objects to the specified target. The connection will be done by the relation defined
             as default.
             
        :param Input: 
                         a list of CreateIn objects representing the Create Input for Business Objects to
                         be created
             
        :return: Contains a list of tags representing the objects that were created. Any failure will
             be returned with client id mapped to error message in the ServiceData list of partial
             errors.
        """
        ...
    def DisconnectObjects(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement.DisconnectInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    Generic operation to disconnect objects.
        :param Input: 
                         A list of disconnectInput objects for the objects to disconnect
             
        :return: Any failure will be returned with client id mapped to error message in the ServiceData
             list of partial errors.
        """
        ...
    def CloseContexts(self, Contexts: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This method is used to close contexts (base view windows). For each context, this
             method closes the base view window and all the open views (OG windows) associated
             to it
             
        :param Contexts: 
                         A vector with the contexts (top lines of the windows) to close
             
        :return: The service data of the operation
        """
        ...
    def CloseViews(self, StructureContext: Teamcenter.Soa.Client.Model.ModelObject, Views: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    This method is used to close opened views (OG windows).
        :param StructureContext: 
                         The structure context containing the views. Can be NULL if not using structire context.
             
        :param Views: 
                         A vector with the open views (top lines of the OG windows) to close
             
        :return: The service data of the operation
        """
        ...
    def OpenContexts(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2011_06.DataManagement.OpenContextInput]) -> Teamcenter.Services.Strong.Manufacturing._2011_06.DataManagement.OpenContextsResponse:
        """    This method is used to open existing objects in new base view windows.
        :param Input: 
                         A list of OpenContextInput representing the objects to open
             
        :return: The response of the operation
        """
        ...
    def OpenViews(self, Context: Teamcenter.Soa.Client.Model.ModelObject, StructureContext: Teamcenter.Soa.Client.Model.ModelObject, Views: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2011_06.DataManagement.OpenViewsResponse:
        """    
             This method is used to open views (OG windows) for an already opened context (base
             view window).
             
        :param Context: 
                         The context (top line of the base view window) for which the views will be opened
             
        :param StructureContext: 
                         The structure context containing the context. This can be null
             
        :param Views: 
                         A vector with the views to open
             
        :return: The response of the operation
        """
        ...
    def AddAssociatedContexts(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AddAssociationInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Generic operation for setting different kinds of associations. It could be between
             Plant BOP and Product BOP (Leading Plant BOP in the future), Product (root) and Process
             (root) structures, regular Plant (Workarea) (root) and Process (root) structures,
             EBOM-MBOM. For now we will use it as threshold for Plant BOP and Product BOP. Other
             types are defined as target. This SOA will be used for add operation. Remove/disconnect
             (future) will be implemented in separate SOA.
             
        :param Input: 
                         list of AddAssociationInput BOMLines for the contexts to be associated.
             
        :return: ServiceData
        """
        ...
    def AssociateAndAllocateByPreview(self, Input: Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AssociateAndAllocateInput, AllocationMap: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AssociateAndAllocateResponse:
        """    
             This function is the second function call in case a preview is required for automatic
             allocation this function does the actual allocation from Source Product BOP to a
             Target Plant BOP on the basis of a Reference Product BOP. This is done by passing
             the allocation map back to the server which we recived in the  automaticAllocatePreview
             command. This function also associates the Source Product BOP with the Target Plant
             BOP in case they are not associated. This function can throw the following exceptions,
             Reference Product BOP is not linked to the Target Plant BOP and Some allocation from
             the source structure to the target structure were unsuccessful please see the log
             for more details. Both these error messages will have the severity level of error.
             
        :param Input: 
                         Input specifying source, target and reference objects.
             
        :param AllocationMap: 
                         Map of allocations from the source structure to the target structure.
             
        :return: Response containing the log file ticket and service data.
        """
        ...
    def AutomaticAllocatePreview(self, Input: Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AssociateAndAllocateInput) -> Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AutomaticAllocatePreviewResponse:
        """    
             This function is the first function call in case a preview is required for automatic
             allocation from Source Product BOP to a Target Plant BOP on the basis of a Reference
             Product BOP. This function finds the allocated lines from the reference product BOP
             to the Plant BOP and equivalent lines in the source Product BOP and generates a preview
             for the automatic allocation in CSV format . Also this function returns an allocationMap,
             which needs to be sent back to server in case the user wants to go ahead with the
             allocation , for which it calls the second server call associateAndAllocateMap command
             . This function can throw the following exceptions, Reference Product BOP is not
             linked to the Target Plant BOP . This error messages will have severity level of
             error.
             
        :param Input: 
                         Input specifying source, target and reference objects.
             
        :return: Response containing allocation map, CSV file ticket and service data.
        """
        ...
    def AutomaticAssociateAndAllocate(self, Input: Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AssociateAndAllocateInput) -> Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AssociateAndAllocateResponse:
        """    
             This function is a single call function that does the allocation from Source Product
             BOP to a Target Plant BOP on the basis of a Reference Product BOP. This function
             finds the allocated lines from the reference product BOP to the Plant BOP and equivalent
             lines in the source Product BOP and does the allocation from the Source Product BOP
             to the Target Plant BOP in a single call. This function also associates the Source
             Product BOP with the Target Plant BOP in case they are not associated. This function
             can throw the following exceptions, Reference Product BOP is not linked to the Target
             Plant BOP and Some allocation from the source structure to the target structure were
             unsuccessful please see the log for more details. Both these error messages will
             have the severity level of error.
             
        :param Input: 
                         Input specifying source, target and reference objects.
             
        :return: Response containing the service data and log file path.
        """
        ...
    def ConnectObjects(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.ConnectObjectsInputData]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.ConnectObjectResponse:
        """    
             Generic operation for connecting MFG nodes       int        quantityNum - number
             of BOMLines to create (used in paste special). Default value is 1. int        occurrenceNumber
             - for packed lines. Number of occurrences to create (used in paste special). Default
             value is 1. int        findNumber - find number. Always passed by client.
             
        :param Input: 
                         A list of ConnectInput BOMLines for the nodes to connect
             
        :return: Generic operation for connecting MFG nodes
        """
        ...
    def DisconnectFromOrigin(self, InputVector: list[Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.DisconnectFromOriginInputData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Disconnects objects and their children from their origin relation. Origin relation
             is created when the objects are assigned from the Product BOP/Generic BOP to the
             Plant BOP/Product BOP. This functionality removes the origin relation created during
             the assignment. Also this functionality can be called recursively for the processes
             below. This functionality can return an error in the following conditions, the object
             on which disconnect function was called called does not have an origin in case of
             non-recursive calls. This error will have a severity level of information. And This
             functionality is not available on this type of object only ProcessAreas, WorkAreas,
             Partitions, Processes and Operations type objects are expected.
             
        :param InputVector: 
                         Vector of DisconnectFromOriginInputData specifying the lines to be disconnected and
                         whether the children are to be recursively disconnected too.
             
        :return: Service data containing the errors that occurred during the disconnect command.
        """
        ...
    def GetAssociatedContexts(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.GetAssociatedContextsInputData]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AssociationResponse:
        """    Returns associated contexts with the input context.
        :param Input: 
                         input
             
        :return: Returns associated contexts with the input context
        """
        ...
    def ApplyConfigObjects(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2012_09.DataManagement.ApplyConfigInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    Apply configuration objects to applicable business objects.
        :param Input: 
                         Input parameters for applying configuration objects
             
        :return: Service Data
        """
        ...
    def CreateOrUpdateConfigObjects(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2012_09.DataManagement.CreateConfigInput]) -> Teamcenter.Services.Strong.Manufacturing._2012_09.DataManagement.CreateConfigResponse:
        """    Creates or updates the configuration objects based on the input data.
        :param Input: 
                         Vector of CreateConfigInput structure which contains the information for creating
                         or updating context objects.
             
        :return: Contains the created or updated object and the service data.
        """
        ...
    def CreateAttachments(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement.CreateIn]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement.CreateResponse:
        """    
             This service operation creates the attachment objects for a business object(s).
             
             The operation considers the Incremental Change applied on the window of the object
             for which attachment is to be created.
             
             The operation takes following inputs.
             

clientId - Unique client Identifier.
             
context - The business objects of the BOM Line. The
             IC applied on the window of this line is considered while creating the attachment.
             
target - The business object which is used as primary object
             to connect the newly created object.
             
relation name - The name of the relation used to connect the
             target.
             
data - Input data for create operation.
             



Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         A list of CreateIn objects representing the Create Input for Business Objects to
                         be created.
             
        :return: 
        """
        ...
    def SetAttributes(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2013_05.DataManagement.ObjectAttributesInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service operation sets the attributes of objects attached to the business object(s).
             For example, if some attributes of a Form attached to an Item needs
             to be edited, this operation can be used.
             
             The operation considers the Incremental Change applied on the window of the object
             whose attachment is to be edited.
             
             The operation takes the business objects of the BOMLine and its attached object
             which is to be edited. Along with that, it takes the name(s) of attributes  and their
             corresponding values to be set.
             
             This operation can set multiple attributes of multiple attached objects.
             


Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         The input structure contains object(s) to be edited and the details of the attributes
                         or relations which need to be edited.
             
        :return: 
        """
        ...
    def SyncStudyAndSource(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2013_05.DataManagement.SyncStudyInput]) -> Teamcenter.Services.Strong.Manufacturing._2013_05.DataManagement.SyncStudyResponse:
        """    
             This operation synchronizes a Simulation Study with the source BOP structure it is
             associated with.
             
        :param Input: 
                         The Mfg0BvrStudy objects to synchronize and the direction to synchronize (to/from
                         the study).
             
        :return: The FMS file ticket to the log file for the study synchronization.
        """
        ...
    def AddOrRemoveAssociatedContexts(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2014_06.DataManagement.AddOrRemoveContextsInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def EstablishOriginLink(self, Input: Teamcenter.Services.Strong.Manufacturing._2014_06.DataManagement.EstablishOriginLinkInfo) -> Teamcenter.Services.Strong.Manufacturing._2014_06.DataManagement.EstablishOriginLinkResponse: ...
    def GetProcessResourceRelatedInfo(self, Input: list[Teamcenter.Soa.Client.Model.ModelObject], ObjectPreference: str) -> Teamcenter.Services.Strong.Manufacturing._2014_06.DataManagement.ProcResourceResponseInfo:
        """    
             This service operation fetches the information related to process resource (work
             content performed by resource(s) in a manufacturing plant ) and the operation/process
             that are allocated/unallocated to process-resource. The operation takes object for
             which information is required. The object can be process station, process line, process
             area, or process resource. The object must be in the context of Plant Bill of Processes
             (BOP).
             

Use Cases:

             Use Case 1: Fetching process resource for a given process area.
             
             This operation can be used to fetch the process resource of specific process area.
             In context of a Plant BOP, this operation can be called on the process area BOM line.
             In response, all the process lines and process stations under the process area are
             fetched apart from  process resources for each process station and allocated/unallocated
             operations/processes. The result is populated on a view providing information on
             process resources, process station it belongs to and allocated/unallocated operations/processes.
             

             Use Case 2: Fetching processes/operations for a given process resource.
             
             This operation can be used to fetch the process/operation that are allocated to process
             resource.
             
             In context of a Plant BOP, this operation can be called on the process resource BOM
             line. In response, all allocated/unallocated operations/processes are fetched. The
             result is populated on a view providing information on process resources and allocated
             operations/processes.
             

             Use Case 3: Fetching processes/operaions that are not allocated to process resource
             for a given process area  and process
             
             This operation can be used to fetch the process/operation that are not allocated
             to process resource. In context of a Plant BOP, this operation can be called on the
             process area or process BOM line. In response, all unallocated operations/processes
             are fetched. The result is populated on a view providing information on process resources
             and unallocated operations/processes.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 

        :param ObjectPreference: 
                         Specifies the object that response must return. The valid values are Process, Operation
                         and ProcessAndOperation denoting respectively that process of type Mfg0BvrProcess,
                         operation of type Mfg0BvrOperation and both process and operation that are allocated
                         to process resource will be returned in the response.
             
        :return: 
        """
        ...
    def CloneAssemblyAndProcessObjects(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2014_06.DataManagement.CloneAssemblyInputData]) -> Teamcenter.Services.Strong.Manufacturing._2014_06.DataManagement.CloneAssemblyResponse:
        """    
             This operation clones an assembly in manufacturing Bill of Material (mBOM) as a reaction
             to changes in engineering BOM (eBOM) planning or clones a process in Bill Of Processes
             as a reaction to changes in mBOM planning. As a result of this operation, the original
             assembly/process is cloned and occurrence effectivity is set correctly on both original
             and cloned assembly/process.
             

             For eBOM-mBOM cloning some of the parts from the new assembly in the mBOM are replaced
             with the new parts that were introduced to the eBOM as a replacement in that unit
             effectivity.
             

             For mBOM-BOP cloning the process that used to refer to the original assembly in the
             mBOM is cloned and all references are fixed to point at the new assembly.
             

Use Cases:

             Clone subassembly with effectivity Use Case.
             
             Use Case Description:
             
             In this use case, the user detects changes in the eBOM, and would like to make the
             appropriate changes to the Mbom. The changes entail cloning the target assembly where
             the parts are in the mBom.
             
             Use Case Goal:
             
             Handle changes in eBOM by creating the appropriate stock-able assembly in the mBom.
             

             Description:
             
             This use case may be regarded as a direct continuation of the Clone assembly with
             effectivity Use Case. In this use case, the user continues to handle the change,
             by cloning the process to which the "original" assembly was assigned (and its hierarchy),
             and fixing all internal references to the new copy.
             
             Use Case Goals:
             
             Handle changes in mBom by creating the appropriate structure to consume it in the
             BOP.
             



Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         Contains source object that should be cloned, target parent object for the cloned
                         object and additional parameters that govern the functionality.
             
        :return: 
        """
        ...
    def GetConnectorInfo(self, ItemRevs: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2017_11.DataManagement.GetConnectorResponse:
        """    
             Connector is Product and Manufacturing Information (PMI) object created by NX which
             is used to define the connection between two components used on shop floor. This
             operation retrieves the information of connectors represented as a Mfg0MEConnectorTableRow
             in Mfg0MEConnectorTable.
             
Mfg0MEConnectorTableRow has information about connector type, connector name,
             connector ID and transformation.
             
             The Mfg0MEConnectorTableForm holds Mfg0MEConnectorTable and is related
             to ItemRevision through the relation Mfg0MEConnectorTblFormRel.


Use Cases:

             Connector is Product and Manufacturing Information (PMI) object created by NX which
             is used to define the connection between two components used on shop floor. E.g.
             Mfg0Conveyor and Mfg0Conveyor or Mfg0Conveyor and Mfg0MERobot.
             Line Designer user wants to retrieve connector information for ItemRevision.


Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param ItemRevs: 
                         List of <b>ItemRevision</b> for which connector information is required.
             
        :return: 251081: Connector information is not defined for the input object.
        """
        ...
    def GetPhysicalAttachmentsInScope(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2017_11.DataManagement.GetPhysicalAttachmentsInput]) -> Teamcenter.Services.Strong.Manufacturing._2017_11.DataManagement.GetPhysicalAttachmentsResponse:
        """    
             This operation retrievs all physical attachments (Mfg0MEPhysicalAttachment
             or Mfg0MEMountToolToRobot) relations defined between two BOMLine
             objects that are children of the given scope Mfg0BvrWorkarea and context Mfg0BvrWorkarea
             acting as a root of the structure.
             
             This operation
             

Processes the input scope Mfg0BvrWorkarea under root context
             Mfg0BvrWorkarea in Bill of Equipment structure.
             
Traverses   the scope, finds the AbsOccurrence under the scope
             related with Mfg0MEPhysicalAttachment or Mfg0MEMountToolToRobot relation.
             From primary AbsOccurrence of relation Mfg0MEPhysicalAttachment or
             Mfg0MEMountToolToRobot it collects source BOMLine and from secondary
             AbsOccurrence it collects target BOMLine along with the relation properties
             on Mfg0MEPhysicalAttachment or Mfg0MEMountToolToRobot.
             



Use Cases:

             Line Designer user wants to retrieve mount and attachment information for the BOMLine
             connections with Mfg0MEPhysicalAttachment relation in a given scope of Mfg0BvrWorkarea
             and Mfg0BvrWorkarea acting as a root of the structure.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         Input structure containing scope and context information for which the attachments
                         need to be retrieved.
             
        :return: 253077: The input scope is invalid. Scope cannot be root line in the structure.
        """
        ...
    def RemovePhysicalAttachementRelation(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2017_11.DataManagement.RemovePhysicalAttachmentRelInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes Mfg0MEPhysicalAttachment or Mfg0MEMountToolToRobot
             relation between the AbsOccurrence of given source BOMLine and target
             BOMLine objects for given scope Mfg0BvrWorkarea and context Mfg0BvrWorkarea
             acting as a root of the structure.
             

Use Cases:

             Line Designer user wants to disconnect two connected resource object (for e.g.
             Mfg0MEFactoryTool from the Mfg0MERobot ) which are connected with Mfg0MEPhysicalAttachment
             or Mfg0MEMountToolToRobot relation in a given scope Mfg0BvrWorkarea
             and context Mfg0BvrWorkarea acting as a root of the structure.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         Input structure containing information about the context <b>Mfg0BvrWorkarea</b>,
                         scope <b>Mfg0BvrWorkarea</b> and the source and target <b>BOMLine</b>.
             
        :return: relation between the given source and target object.
        """
        ...
    def SetConnectorInfo(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2017_11.DataManagement.SetConnectorInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Connector is Product and Manufacturing Information (PMI) object created by NX which
             is used to define the connection between two components used on shop floor. This
             operation sets the connector information stored as Mfg0MEConnectorTableRow
             in Mfg0MEConnectorTable. The Mfg0MEConnectorTableForm is attached to
             the ItemRevision.
             
             If the Mfg0MEConnectorTableForm is not related to the ItemRevision
             the operation first creates Mfg0MEConnectorTableForm and attaches it to the
             given ItemRevision with a relation Mfg0MEConnectorTblFormRel.

             If given input connector id is not present in Mfg0MEConnectorTableRow, then
             a Mfg0MEConnectorTableRow is added in Mfg0MEConnectorTable with information
             connector type, connector name, connector ID and transformation.
             
             If given input connector id is present in Mfg0MEConnectorTableRow,the row
             is updated with latest information.
             
             All the Mfg0MEConnectorTableRow for which information is not given are removed
             from Mfg0MEConnectorTable.


Use Cases:

             Line Designer user wants to add, remove or update the connector information for
             ItemRevision


Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         Input structure containing information about the <b>ItemRevision</b> and the connectors
                         information. i.e. connector type, connector name, connector ID and transformation.
             
        :return: 251083:The value provided for input property  is not valid.
        """
        ...
    def SetPhysicalAttachementsInScope(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2017_11.DataManagement.SetPhysicalAttachmentsInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates physical attachment Mfg0MEPhysicalAttachment or  Mfg0MEMountToolToRobot
             relation between the AbsOccurrence of given source BOMLine and target
             BOMLine objects for given scope Mfg0BvrWorkarea and context Mfg0BvrWorkarea
             acting as a root of the structure.
             

Use Cases:

             Line Designer user wants to set mount and attach information for BOMLine (e.g.
             Mfg0MEFactoryTool and Mfg0MERobot) using  Mfg0MEPhysicalAttachment
             or Mfg0MEMountToolToRobot relation in a given scope Mfg0BvrWorkarea
             and context Mfg0BvrWorkarea acting as a root of the structure.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         Input structure containing information about the scope <b>(Mfg0BvrWorkarea)</b>,
                         the source<b> (BOMLine) </b>and target <b>(BOMLine)</b> objects and <b>Mfg0MEPhysicalAttachment</b>
                         or <b>Mfg0MEMountToolToRobot</b> relation properties.
             
        :return: 
        """
        ...
    def GetOccurrenceKinematicsInformation(self, OccKinematicsInfoinput: list[Teamcenter.Services.Strong.Manufacturing._2018_06.DataManagement.GetOccKinematicsInfoInput]) -> Teamcenter.Services.Strong.Manufacturing._2018_06.DataManagement.GetOccurrenceKinematicsInfoResponse:
        """    
             In Line Designer (LD) and Process Simulate (PS), resource occurrence has specific
             poses and joint values. This operation retrieves occurrence kinematics information
             of Mfg0MEResourceRevision or ItemRevision from Bill of Equipment structure
             for the given scope Mfg0BvrWorkarea and context Mfg0BvrWorkarea acting
             as a root of the structure
             

Use Cases:

             Line Designer or Process Simulate user wants to get the occurrence kinematics information
             for occurrence of Mfg0MEResourceRevision or ItemRevision from Bill
             of Equipment structure
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param OccKinematicsInfoinput: 
                         Input structure containing context and scope for which the occurrence kinematics
                         information of resource occurrence is required
             
        :return: 253180: The input context is invalid. Context should be root line of the Bill of
             Equipment structure.
        """
        ...
    def SetOccurrenceKinematicsInformation(self, OccInfoInputMap: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             In Line Designer (LD) and Process Simulate (PS), resource occurrence used has specific
             poses and joint values. This operation creates a relation between AbsOccData
             and Mfg0OccKinematicsInfo using relation Mfg0OccKinematicsRel. The
             occurrence kinematics information is stored as an XML reference on the dataset Mfg0OccKinematicsInfo


Use Cases:

             Line Designer or Process Simulate user wants to set the occurrence kinematics information
             for occurrence of Mfg0MEResourceRevision or ItemRevision


Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param OccInfoInputMap: 
                         A map <b>(BOMLine, Dataset)</b> containing <b>BOMLine</b> representing the occurrence
                         of <b>Mfg0MEResourceRevision</b> or <b>ItemRevision</b> and the dataset <b>Mfg0OccKinematicsInfo</b>
                         having occurrence kinematics information.
             
        :return: in the Bill of Equipment structure.
        """
        ...
    def PublishSelectionFromStudyToSource(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2019_06.DataManagement.SelectedSyncPublishStudyInput]) -> Teamcenter.Services.Strong.Manufacturing._2019_06.DataManagement.SelectedStudySourceResponse: ...
    def SyncSelectionInStudyWithSource(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2019_06.DataManagement.SelectedSyncPublishStudyInput]) -> Teamcenter.Services.Strong.Manufacturing._2019_06.DataManagement.SelectedStudySourceResponse: ...

class ImportExportRestBindingStub(ImportExportService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ImportManufaturingFeatures(self, Input: Teamcenter.Services.Strong.Manufacturing._2010_09.ImportExport.ImportInput) -> Teamcenter.Services.Strong.Manufacturing._2010_09.ImportExport.ImportResponse: ...
    @typing.overload
    def ImportManufacturingFeatures(self, Input: Teamcenter.Services.Strong.Manufacturing._2013_05.ImportExport.AdvancedImportInput) -> Teamcenter.Services.Strong.Manufacturing._2013_05.ImportExport.AdvancedImportResponse: ...
    @typing.overload
    def ImportManufacturingFeatures(self, Input: Teamcenter.Services.Strong.Manufacturing._2015_10.ImportExport.ImportManufaturingFeaturesInput) -> Teamcenter.Services.Strong.Manufacturing._2015_10.ImportExport.ImportManufaturingFeaturesResponse: ...
    @typing.overload
    def ImportManufacturingFeatures(self, Input: Teamcenter.Services.Strong.Manufacturing._2016_03.ImportExport.ImportManufaturingFeaturesInput) -> Teamcenter.Services.Strong.Manufacturing._2015_10.ImportExport.ImportManufaturingFeaturesResponse: ...
    def ExportToBriefcase(self, Reason: str, Sites: list[Teamcenter.Soa.Client.Model.ModelObject], Objects: list[Teamcenter.Soa.Client.Model.ModelObject], TransferOptionSet: Teamcenter.Soa.Client.Model.ModelObject, OptionNameAndValues: System.Collections.Hashtable, SessionOptionNamesAndValues: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Manufacturing._2016_03.ImportExport.MfgExportToBriefcaseResponse: ...
    def ImportFromBriefcase(self, FmsTicket: str, OptionSetTag: Teamcenter.Soa.Client.Model.ModelObject, OptionNamesAndValues: System.Collections.Hashtable, SessionOptionAndValues: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Manufacturing._2017_05.ImportExport.MfgImportFromBriefcaseResponse: ...

class ImportExportService:
    """
    
            Contains import-export services
            


Library Reference:

TcSoaManufacturingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ImportExportService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ImportManufaturingFeatures(self, Input: Teamcenter.Services.Strong.Manufacturing._2010_09.ImportExport.ImportInput) -> Teamcenter.Services.Strong.Manufacturing._2010_09.ImportExport.ImportResponse:
        """    imports MFGs from a given PLMXML file to TC.
        :param Input: 
                         The input contains the PLMXML file and the root of the structure to which the data
                         should be imported.
             
        :return: return a path to the log file and a ServiceData that contains errors
        """
        ...
    @typing.overload
    def ImportManufacturingFeatures(self, Input: Teamcenter.Services.Strong.Manufacturing._2013_05.ImportExport.AdvancedImportInput) -> Teamcenter.Services.Strong.Manufacturing._2013_05.ImportExport.AdvancedImportResponse: ...
    @typing.overload
    def ImportManufacturingFeatures(self, Input: Teamcenter.Services.Strong.Manufacturing._2015_10.ImportExport.ImportManufaturingFeaturesInput) -> Teamcenter.Services.Strong.Manufacturing._2015_10.ImportExport.ImportManufaturingFeaturesResponse: ...
    @typing.overload
    def ImportManufacturingFeatures(self, Input: Teamcenter.Services.Strong.Manufacturing._2016_03.ImportExport.ImportManufaturingFeaturesInput) -> Teamcenter.Services.Strong.Manufacturing._2015_10.ImportExport.ImportManufaturingFeaturesResponse: ...
    def ExportToBriefcase(self, Reason: str, Sites: list[Teamcenter.Soa.Client.Model.ModelObject], Objects: list[Teamcenter.Soa.Client.Model.ModelObject], TransferOptionSet: Teamcenter.Soa.Client.Model.ModelObject, OptionNameAndValues: System.Collections.Hashtable, SessionOptionNamesAndValues: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Manufacturing._2016_03.ImportExport.MfgExportToBriefcaseResponse:
        """    
             This operation is applicable specifically for Manufacturing Process Planner MPP
             application.
             
             This operation combines following two operations.
             
             Teamcenter::Soa::GlobalMultiSite::_2008_06::ImportExport exportObjectsToOfflinePackage
             
             Teamcenter::Soa::GlobalMultiSite::_2008_06::ImportExport requestExportToRemoteSites
             
             In addition, it creates internal objects which are helpful in supplier collaboration
             use cases for manufacturing objects. Details in the use case section.
             

Use Cases:

Use Case 1:  Exporting objects to the briefcase by transferring the ownership
             to the supplier.

             User wants to export Collaboration Context (CC) object in MPP to the
             briefcase to be used by the supplier at remote site.
             
             The CC may contain product structure(s), bill of processes (BOP) such
             as plant BOP, plant structure etc.
             
             While exporting, the user wants to transfer ownership of few objects in the CC
             to the supplier so that the supplier can make changes to those objects on the other
             site.
             
             The user selects the CC and uses the menu option Tools, Export To, Briefcase...
             
             he menu option opens a dialog that allows user to set a destination site, a transfer
             option set, a list of traverse options and a list of session options.
             
             In this case, all the objects which can be traversed by the transfer option set and
             session options will be exported into an output TC XML file.
             
             The files and datasets related to exported objects will be downloaded and packed
             into the briefcase file along with the TC XML file.
             

             In addition, the internal object, Appearance Path Node (APN) will be created
             for the identified BOMLine objects in the CC. The BOMLine objects
             are identified based on the preference MERuleForBriefcaseExport.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Reason: 
                         The reason for the export, the size is limited to 240 characters. This can be blank.
             
        :param Sites: 
                         The destination sites, only one site is supported as of now. The site should be marked
                         as offline in the <b>Organization</b> application in Teamcenter to perform a briefcase
                         export.
             
        :param Objects: 
                         List of objects  to be exported such as <b>CC</b>, <b>BOMLine</b>.
             
        :param TransferOptionSet: 
                         The <b>TransferOptionSet</b> can be created/modified/customized by the end user.
             
        :param OptionNameAndValues: 
                         Please refer the documentation of the PLM XML Export Import administration tool for
                         more details.
             
        :param SessionOptionNamesAndValues: 
                         processUnconfiguredByOccEff
             
        :return: 
        """
        ...
    def ImportFromBriefcase(self, FmsTicket: str, OptionSetTag: Teamcenter.Soa.Client.Model.ModelObject, OptionNamesAndValues: System.Collections.Hashtable, SessionOptionAndValues: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Manufacturing._2017_05.ImportExport.MfgImportFromBriefcaseResponse:
        """    
             This operation is applicable specifically for Manufacturing Process Planner MPP application.
             
             This operation performs following operation
             
             Teamcenter::Soa::GlobalMultiSite::_2008_06::ImportExport importObjectsFromOfflinePackage
             
             In addition to this, it supports asynchronous import of briefcase.
             

Use Cases:

Use Case 1: Importing objects from briefcase

             This operation can be used in Manufacturing Process Planner (MPP) application to
             import Briefcase file into Teamcenter. Briefcase file is a zipped file containing
             TC XML and data set files. The TC XML file specifies the object to be imported. The
             import dialog presents various option sets to control the objects during import.
             
             First time import will create the objects and upload the datasets. Subsequent import
             of same object will update it. Importer log is generated and presented after the
             import.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param FmsTicket: 
                         The FMS file ticket for the briefcase file, the file should be uploaded to the server
                         before calling this operation.
             
        :param OptionSetTag: 
                         A reference to the <b>TransferOptionSet</b> object, this object holds the list of
                         options and their default values which can influence importing briefcase.
             
        :param OptionNamesAndValues: 
                         For example: For option opt_imp_XXX  in TransferOptionSet, the default value is false.
                         It can be overridden by adding the option with new value as true.
             
        :param SessionOptionAndValues: 
                         For example: A session option modified_objects_only specifies whether to import modified
                         object.
             
        :return: 
        """
        ...

class IPAManagementRestBindingStub(IPAManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def DeletefilteredIPA(self, Processes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GenerateSearchScope(self, Processes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2008_12.IPAManagement.IPAManagementGenerateSearchScopeResponse: ...
    def GetFilteredIPA(self, Processes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2008_12.IPAManagement.IPAManagementGetFilteredIPAResponse: ...
    def SaveSearchResult(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2008_12.IPAManagement.IPAManagementSaveSearchResultInput]) -> Teamcenter.Services.Strong.Manufacturing._2008_12.IPAManagement.IPAManagementSaveSearchResultResponse: ...
    def DeleteFilteredIPA(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2012_02.IPAManagement.DeleteFilteredIPAInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetFilteredIPAType(self, Processes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.IPAManagement.GetFilteredIPATypeResponse: ...
    def CleanIPATree(self, ProcessWindow: Teamcenter.Soa.Client.Model.ModelObject, ForceCleanAll: bool) -> Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement.CleanIPATreeResponse: ...
    def DoesIPAExist(self, ProcessWindow: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement.IPAExistResponse: ...
    def GenerateIPATree(self, IpaInput: Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement.IPATreeInput) -> Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement.GenerateIPATreeResponse: ...
    def LocalUpdateIPATree(self, ProcessLines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement.LocalUpdateIPATreeResponse: ...
    def UpdateIPATree(self, IpaInput: Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement.IPATreeInput) -> Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement.GenerateIPATreeResponse: ...
    def FindAndRepopulateDynamicIPAs(self, InputBOPLines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2014_12.IPAManagement.FindAndRepopulateDynamicIPAsResponse: ...
    def RepopulateDynamicIPAs(self, Input: Teamcenter.Services.Strong.Manufacturing._2014_12.IPAManagement.RepopulateDynamicIPAsData) -> Teamcenter.Services.Strong.Manufacturing._2014_12.IPAManagement.RepopulateDynamicIPAsResponse: ...

class IPAManagementService:
    """
    
            This service provides operations to perform In Process Assembly (IPA) Related functionality
            on a given input.
            

            Use cases supported by this service include:
            

Creating, updating and deleting IPA for the input process root.
            
Creating, updating and deleting filtered IPA for the input processes.
            
Creating, updating and deleting dynamic IPA for the input processes.
            




Library Reference:

TcSoaManufacturingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> IPAManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def DeletefilteredIPA(self, Processes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    Deletes the filteredIPA structure from the process.
        :param Processes: 
                         Input Vector of process lines, from which we want to delete the filteredIPA.
             
        :return: serviceData This is a common data strucuture used to return sets of Teamcenter Data
             Model object from a service request. This also holds services exceptions.
        """
        ...
    def GenerateSearchScope(self, Processes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2008_12.IPAManagement.IPAManagementGenerateSearchScopeResponse:
        """    
             find the IPA under the given process (for each process) and retrives the bomlines
             from under it.
             
        :param Processes: 
                         processes Vector of process lines, that we would like to get all the search scope
                         from.
             
        :return: IPAManagementGenerateSearchScopeResponse Return Structure see discription in structure
             definition file.
        """
        ...
    def GetFilteredIPA(self, Processes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2008_12.IPAManagement.IPAManagementGetFilteredIPAResponse:
        """    Return the filteredIPA structure from the process.
        :param Processes: 
                         Input Vector of process lines, from which we want to find the filteredIPA.
             
        :return: IPAManagementGetFilteredIPAResponse Return Structure see discription in structure
             definition file.
        """
        ...
    def SaveSearchResult(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2008_12.IPAManagement.IPAManagementSaveSearchResultInput]) -> Teamcenter.Services.Strong.Manufacturing._2008_12.IPAManagement.IPAManagementSaveSearchResultResponse:
        """    Saves the search result in a new/updated structure.
        :param Input: 
                         Input Vector of IPAManagementSaveSearchResultInput Structures see discription in
                         structure definition file.
             
        :return: IPAManagementSaveSearchResultResponse Return Structure see discription in structure
             definition file.
        """
        ...
    def DeleteFilteredIPA(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2012_02.IPAManagement.DeleteFilteredIPAInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This API will delete the filtered IPA(s) under the process depending on the boolean
             member "isRecursive" of the input structure. If " isRecursive" is true, then all
             the filtered IPAs in the hierarchy of the member "process" will be deleted. Else
             just one filtered IPA directly under the process will be deleted.
             
        :param Input: 
                         Contains the information about deleting filtered IPAs.
             
        :return: the standard serviceData that contains errors\notes from executing the deletion.
        """
        ...
    def GetFilteredIPAType(self, Processes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.IPAManagement.GetFilteredIPATypeResponse:
        """    
             For each process, return the type of the FIPA used for this process structure.  For
             processes from the same process structure, the answer is the same. Therefore, from
             perforemence point of view, it is better to pass the process context (topline) as
             an input, instead of sending several processes from the same structure.
             
        :param Processes: 
                         a vector of processes.
             
        :return: For each process, return the type of the FIPA used for this process structure (can
             be either flat or nested). If there is no FIPA for this process structure, return
             unset.
        """
        ...
    def CleanIPATree(self, ProcessWindow: Teamcenter.Soa.Client.Model.ModelObject, ForceCleanAll: bool) -> Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement.CleanIPATreeResponse:
        """    
             This operation removes the In-Process Assembly (IPA) occurrences from the process
             structure and deletes the IPA occurrence group from product structure. This operation
             cleans only the IPA which has been configured by current configuration rule and configuring
             structure.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param ProcessWindow: 
                         Window of the process structure containing the IPA that is to be deleted.
             
        :param ForceCleanAll: 
                         This flag is used to forcefully delete all IPAs. This functionality is not supported
                         currently.
             
        :return: 515182:Â Â Â Â Â Â Â Â Could not find the log file.
        """
        ...
    def DoesIPAExist(self, ProcessWindow: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement.IPAExistResponse:
        """    
             This operation checks if an In-Process Assembly tree exists for a process structure.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param ProcessWindow: 
                         Window of the process structure.
             
        :return: 
        """
        ...
    def GenerateIPATree(self, IpaInput: Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement.IPATreeInput) -> Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement.GenerateIPATreeResponse:
        """    
             An In-Process Assembly (IPA) is an aggregation of incoming parts into stations. IPA
             is generated based on consumed item(s) from a product structure in a process structure.
             Teamcenter creates a tree structure representing the IPA by traversing the process
             structure and collecting IPAs from previous process elements and adding the selected
             line's consumed objects.
             

             The IPA is stored as an occurrence group and is displayed in a separate tab beside
             the base view of the root product.
             

             When the assembly tree is created by the operation, it places a configuration file
             as an attachment on the process for which the IPA is generated.
             

             Teamcenter sends an e-mail notification to the recipients specified in the input
             after completion of the operation. This e-mail contains information about the IPA
             creation, as well as log files that are created during generation of the IPA.
             


Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param IpaInput: 
                         All the details for IPA generation that includes the name of the IPA, process types,
                         consumption types, occurrence group type, effectivity, email notification details
                         etc.
             
        :return: 
        """
        ...
    def LocalUpdateIPATree(self, ProcessLines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement.LocalUpdateIPATreeResponse:
        """    
             This operation is used to perform a local update on an In-Process Assembly (IPA)
             tree. Local update changes the IPA on which the operation is invoked. If necessary,
             it also updates the occurrence pointing to this in-process assembly in the process
             structure.
             

             If the IPA has not been created and attached to the matching process, Teamcenter
             also changes the matching process and adds the incoming IPA as MEWorkpiece. This
             happens only if a process whose type is in the process types list of the configuration
             details during the initial IPA generation.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param ProcessLines: 
                         List of processes in the process structure on which local update requested.
             
        :return: 515182:Â Â Â Â Â Â Â Â Could not find the log file.
        """
        ...
    def UpdateIPATree(self, IpaInput: Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement.IPATreeInput) -> Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement.GenerateIPATreeResponse:
        """    
             This operation is used to update an In-Process Assembly (IPA) tree that already exists,
             when a process structure is changed. The options set at creation of the assembly
             tree may be changed for example process types, consumed occurrence types, name of
             the report on errors and problems, e-mail notification configuration.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param IpaInput: 
                         All the details for updating IPA that includes the name of the IPA, process types,
                         consumption types, occurrence group type, effectivity, email notification details
                         etc.
             
        :return: 
        """
        ...
    def FindAndRepopulateDynamicIPAs(self, InputBOPLines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2014_12.IPAManagement.FindAndRepopulateDynamicIPAsResponse:
        """    
             This operation recieves a list of ImanItemBOPLine as an input.
             
             (The type of of the bop line objects can be either Mfg0BvrProcess or Mfg0BvrShdStudy).
             

             For every given object:
             
             1. If the object does not have any dynamic IPAs, the operation issues an error.
             

             2. If the dynamic IPAs (that belong to the given object) are empty, the operation
             re-calculates them.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param InputBOPLines: 
                         (The type of of the bop line objects can be either Mfg0BvrProcess or Mfg0BvrShdStudy).
             
        :return: 2. 25440: The given object doesn't have any dynamic IPA.
        """
        ...
    def RepopulateDynamicIPAs(self, Input: Teamcenter.Services.Strong.Manufacturing._2014_12.IPAManagement.RepopulateDynamicIPAsData) -> Teamcenter.Services.Strong.Manufacturing._2014_12.IPAManagement.RepopulateDynamicIPAsResponse:
        """    
             The operation converts the given input list of absolute occurrence IDs to a list
             of objects (ImanItemBOPLine) and calculates/regenerates & returns dynamic
             in-process assembly nodes and its related information. The input object contains
             the top BOPLine and a list of absolute occurrence IDs of processes(Mfg0BvrProcess)
             or shared studies(Mfg0BvrShdStudy).
             

             For every given absolute occurrence IDs
             

If the object doesn't have any dynamic in-process-assembly (IPA)
             as children, the operation issues an error.
             
If the dynamic IPA nodes (that belong to the given object) are empty,
             the operation re-calculates them.
             
The response of the operation includes the dynamic IPA nodes that
             belongs to the object. For each dynamic IPA, the response includes its content (i.e.
             parts underneath) and occurrence information. Both the consumed part object (BOPLine)
             and referenced part object (BOMLine) are returned along with their related
             occurrence information.
             



             This data is returned for every given object, no matter whether its dynamic IPA nodes
             were originally empty or not.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         The top <b>BOPLine</b> and a list of absolute occurrence IDs of processes (<b>Mfg0BvrProcess</b>)
                         or shared studies (<b>Mfg0BvrShdStudy</b>).
             
        :return: 
        """
        ...

class MFGPropertyCollectorRestBindingStub(MFGPropertyCollectorService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CollectProperties(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2009_10.MFGPropertyCollector.CollectPropertiesInputInfo]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.MFGPropertyCollector.CollectPropertiesResponse: ...

class MFGPropertyCollectorService:
    """
    
            This service will provide server functionality to collect property values for every
            node in the BOP structure.
            


Library Reference:

TcSoaManufacturingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> MFGPropertyCollectorService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CollectProperties(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2009_10.MFGPropertyCollector.CollectPropertiesInputInfo]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.MFGPropertyCollector.CollectPropertiesResponse:
        """    
             This function will call a Mfg function that takes the MfgNode, traversal rules and
             property names to collect and return a list of property values of input properties
             for every MfgNode in the BOP structure based on traversal rules.
             
        :param Input: 
                         MfgNode, traversal rules and property names to collect
             
        :return: a list of property values of input properties for every MfgNode in the BOP structure
        """
        ...

class ModelDefinitionsRestBindingStub(ModelDefinitionsService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetManufacturingPropretyDescs(self, Inputs: list[Teamcenter.Services.Strong.Manufacturing._2009_10.ModelDefinitions.PropDescInfo]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.ModelDefinitions.AttachedPropDescsResponse: ...
    def GetValidRelationTypes(self, RelationTypesInput: list[Teamcenter.Services.Strong.Manufacturing._2009_10.ModelDefinitions.RelationTypesInput]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.ModelDefinitions.GetValidRelationTypesResponse: ...

class ModelDefinitionsService:
    """
    
            Meta data
            


Library Reference:

TcSoaManufacturingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ModelDefinitionsService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetManufacturingPropretyDescs(self, Inputs: list[Teamcenter.Services.Strong.Manufacturing._2009_10.ModelDefinitions.PropDescInfo]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.ModelDefinitions.AttachedPropDescsResponse:
        """    
             Get the attached property descriptor based on input type name and property names
             structure.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Inputs: 
                         - vector of structure of PropDescInfo with type name and property names vector.
             
        :return: 300401: The input property is NULL.
        """
        ...
    def GetValidRelationTypes(self, RelationTypesInput: list[Teamcenter.Services.Strong.Manufacturing._2009_10.ModelDefinitions.RelationTypesInput]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.ModelDefinitions.GetValidRelationTypesResponse:
        """    
             This service returns a list of occurrence types that are valid for assignment between
             two received object types.
             
        :param RelationTypesInput: 
                         Vector of source and target types pairs.
             
        :return: List of valid occurrence types.
        """
        ...

class ModelRestBindingStub(ModelService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CalculateCriticalPath(self, Roots: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.Model.CalculateCriticalPathResponse: ...
    def CreateFlow(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2009_10.Model.FlowInput]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.Model.FlowResponse: ...
    def EditLogicalAssignments(self, LaEditVec: list[Teamcenter.Services.Strong.Manufacturing._2009_10.Model.LogicalAssignmentData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetResolvedNodesFromLA(self, InputObjects: list[Teamcenter.Services.Strong.Manufacturing._2009_10.Model.ResolvedNodesInput]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.Model.GetResolvedNodesFromLAResponse: ...
    def RemoveFlow(self, Input: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ResolveLogicalAssignments(self, LaVec: list[Teamcenter.Soa.Client.Model.ModelObject], ResolveObjects: list[Teamcenter.Services.Strong.Manufacturing._2009_10.Model.ResolveData], ExternalSources: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetCandidateToolsForToolRequirement(self, ResolveObjects: list[Teamcenter.Services.Strong.Manufacturing._2012_02.Model.ToolRequirementInput]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.Model.CandidateToolsForToolRequirement: ...
    def GetToolRequirements(self, ParentObject: list[Teamcenter.Soa.Client.Model.ModelObject], ToolRequirementStatus: list[str]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.Model.ToolRequirementResponse: ...
    def ResolveToolRequirement(self, ResolveObjects: list[Teamcenter.Services.Strong.Manufacturing._2012_02.Model.ResolveDataInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UpdateFlows(self, Input: list[Teamcenter.Soa.Client.Model.ModelObject], IsSubHierarchies: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ComputeAppearancePath(self, Input: Teamcenter.Services.Strong.Manufacturing._2013_12.Model.AppearancePathInput) -> Teamcenter.Services.Strong.Manufacturing._2013_12.Model.ComputeAppearancePathResponse: ...
    def ValidateScopeFlowsConsistency(self, RootLines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2014_12.Model.ValidateScopeFlowsConsistencyResponse: ...

class ModelService:
    """
    
            This service provides operations to perform scope flows, tool requirements and logical
            assignment related functionalities on a given input.
            

            Use cases supported by this service include:
            

Creating, updating and removing the scope flows for the given manufacturing
            objects.
            
Resolving or editing the logical assignments or retrieving the resolved
            nodes for given logical assignment.
            
Retrieving or editing the tool requirements for the given input.
            




Library Reference:

TcSoaManufacturingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ModelService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CalculateCriticalPath(self, Roots: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.Model.CalculateCriticalPathResponse:
        """    
             Calculate the critical paths for MFGBVRProcess, MFGBVROperation or MFGBVRActivity
             and their corresponding APS objects. A critical path is the sequence of processes,
             operations or activities that determine the minimum duration of the root object.
             Thereby only those MFG objects will be considered that are either direct sub elements
             or implementers of the root object.
             
        :param Roots: 
                         The list of MFG BVR or APS root objects the critical path is to be calculated for.
             
        :return: For each object in the roots vector the list of critical paths. There maybe more
             than one per object if multiple paths of the same length exist.
        """
        ...
    def CreateFlow(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2009_10.Model.FlowInput]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.Model.FlowResponse:
        """    Create a new mfgFlow object between two mfg objects i.e process or operation
        :param Input: 
                         a vector of  FlowInput structures.
             
        :return: Flow Response a vector of all the new created flow objects
        """
        ...
    def EditLogicalAssignments(self, LaEditVec: list[Teamcenter.Services.Strong.Manufacturing._2009_10.Model.LogicalAssignmentData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    This service enables editing the values of Logical Assignment objects.
        :param LaEditVec: 
                         Vector of objects to edit.
             
        :return: Service Data object that contains errors
        """
        ...
    def GetResolvedNodesFromLA(self, InputObjects: list[Teamcenter.Services.Strong.Manufacturing._2009_10.Model.ResolvedNodesInput]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.Model.GetResolvedNodesFromLAResponse:
        """    
             This service returns the resolved nodes for each of the received Logical Assignment
             objects.
             
        :param InputObjects: 
                         Input objects for which to return resolved nodes.
             
        :return: Response object
        """
        ...
    def RemoveFlow(self, Input: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    Removing existing Flow objects.
        :param Input: 
                         a vector of  Flows to remove.
             
        :return: Service Data object
        """
        ...
    def ResolveLogicalAssignments(self, LaVec: list[Teamcenter.Soa.Client.Model.ModelObject], ResolveObjects: list[Teamcenter.Services.Strong.Manufacturing._2009_10.Model.ResolveData], ExternalSources: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service will resolve and re-resolve logical assignments to concrete assignments
             against the product structure.
             
        :param LaVec: 
                         Vector of Logical Assignment objects to resolve
             
        :param ResolveObjects: 
                         Vector of objects to resolve for each object the service will resolve all its Logical
                         Assignments
             
        :param ExternalSources: 
                         Vector of loaded product structures on which to run the resolve mechanism
             
        :return: Service Data object that contains errors and a list of Logical Assignment objects
             that were actually updated.
        """
        ...
    def GetCandidateToolsForToolRequirement(self, ResolveObjects: list[Teamcenter.Services.Strong.Manufacturing._2012_02.Model.ToolRequirementInput]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.Model.CandidateToolsForToolRequirement:
        """    
             Gets the candidate tools against which Tool Requirement could be resolved. The candidate
             tools are fetched based on the search criteria specified on the Tool Requirement.
             The input parameter tool source specifies the source from where candidate tools are
             supposed to be fetched.  The candidate tool can be fetched only in the Plant BOP.
             
        :param ResolveObjects: 
                         Input structure specifying Operation. Tool Requirement for which candidate tools
                         are to be fetched. And tool source from where tools are to be fetched.
             
        :return: Specifies the candidate tools that match the search criteria of the Tool requirement.
             Further resolveToolRequirement  could be used to resolve the TR with one of the candidate
             tools.
        """
        ...
    def GetToolRequirements(self, ParentObject: list[Teamcenter.Soa.Client.Model.ModelObject], ToolRequirementStatus: list[str]) -> Teamcenter.Services.Strong.Manufacturing._2012_02.Model.ToolRequirementResponse:
        """    
             Fetches the Tool Requirement for the given operation or process. Based on the status
             of the Tool Requirement. either all. resolved or unresolved Tool Requirements are
             returned. The respective options for the status are ALL. RESOLVED and UNRESOLVED.
             Note that the Tool requirement assigned to child operation or process is not considered.
             
        :param ParentObject: 
                         Specifies the Operation of type Mfg0BvrOperation or Process of type Mfg0BvrProcess.
             
        :param ToolRequirementStatus: 
                         Specifies the status of the Tool requirement. The possible values are ALL &amp; RESOLVED
                         and UNRESOLVED. RESOLVED indicates that the Tool Requirement is resolved against
                         the Tool. This option is relevant only for the Plant BOP where it is allowed to resolve
                         the Tool Requirement.  UNRESOLVED indicates that the Tool Requirement is not resolved
                         ALL includes both resolved and unresolved Tool Requirement.
             
        :return: Specifies the Tool Requirements of type Mfg0BVRToolRequirement that are assigned
             to an Operation or Process
        """
        ...
    def ResolveToolRequirement(self, ResolveObjects: list[Teamcenter.Services.Strong.Manufacturing._2012_02.Model.ResolveDataInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Resolves the Tool Requirement with the provided tool. As a result the Tool is assigned
             to the Tool Requirement and to the Operation for which Tool Requirement is defined.
             This resolve operation  is allowed only in the Plant BOP.
             
        :param ResolveObjects: 
                         Specifies the data required for resolving the Tool requirement.
             
        :return: Service data will hold partial errors & warnings and errors. if any.
        """
        ...
    def UpdateFlows(self, Input: list[Teamcenter.Soa.Client.Model.ModelObject], IsSubHierarchies: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Updates flows between the children of input object(s) based on Find number value.
             Input objects should be an instance of BOM line. This service does not return any
             resulting or affected objects. The client needs to update cache of affected objects
             manually(children of the input object are affected ). If isSubHierarchies parameter
             is true, flows are recursively updated for all children.
             
        :param Input: 
                         Should be a vector of BOM lines. This is a scope of update flow command.
             
        :param IsSubHierarchies: 
                         If isSubHierarchies parameter is true, flows are recursively updated for all children.
             
        :return: Returns error message(s) if any generated during update flow execution. Please note
             service data will not return any resulting objects.
        """
        ...
    def ComputeAppearancePath(self, Input: Teamcenter.Services.Strong.Manufacturing._2013_12.Model.AppearancePathInput) -> Teamcenter.Services.Strong.Manufacturing._2013_12.Model.ComputeAppearancePathResponse:
        """    
             This service computes and returns the values for APNUID and AbsOccUID propertis.
             

             APN - bl_apn_uid_in_topline_context
             
             AbsOccUID - bl_absocc_uid_in_topline_context
             

             Input: parent object and a list of paths.
             
                      Each path starts reletively from
             the parent object.
             
                      In case the parent does not have
             APN, the service will calculate it to the parent as well.
             
             Response : vector of values of the adove propeties according to each path.
             

             If the input is BOMLine (and not Fnd0BOMLineLite) there might be performance issue
             due to the fact that the modified obejct would be put in the serviceData and the
             properties that will be brought for this object would be according to the PolicyFile
             (in this case the best practice is to use Dymanic Policy).
             

             Fnd0BOMLineLite does not have as much properties as BOMLine and therefore even if
             the input is large, not many properties would be calculated in the Policy File.
             



Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         A list of AppearancePathInput that holds parent objects and a list of paths for each
                         one. Each path represents a node for which we would like to get the values of the
                         prorperties.
             
        :return: If there was an error in generating these properties, the return value would be ""
             and the error would be added to the serviceData
        """
        ...
    def ValidateScopeFlowsConsistency(self, RootLines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2014_12.Model.ValidateScopeFlowsConsistencyResponse:
        """    
             This operation will be used to identify scope flows created under the given input
             line are acyclic or not. This operation recieves a list of ImanItemBOPLine
             as an input.  (The type of the BOP line objects can be either Mfg0BvrProcess
             or Mfg0BvrOperation). For each input scope, the operation checks whether the
             scope-flows (defined in this scope), create a cycle of processes or operations.
             

             If a cycle is indentified during this operation, the relevant information for the
             cycle is returned in the response.
             


Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param RootLines: 
                         List of business objects representing BOP line objects (the type of the bop line
                         objects can be either<b> Mfg0BvrProcess</b> or <b>Mfg0BvrOperation</b>)
             
        :return: 
        """
        ...

class ResourceManagementRestBindingStub(ResourceManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetStepP21FileCounts(self, ClassIDs: list[str]) -> Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement.GetStepP21FileCountsResponse: ...
    def GetVendorCatalogInfo(self) -> Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement.GetVendorCatalogInfoResponse: ...
    def ImportStep3DModels(self, IcoIDs: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ImportStepP21Files(self, ClassID: str, ImportOptions: int) -> Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement.ImportStepP21FilesResponse: ...
    def ImportVendorCatalogHierarchy(self, VendorCatalogRootDir: str, ImportOptions: int) -> Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement.ImportVendorCatalogHierarchyResponse: ...
    def UpdateNXToolAssemblies(self, IcoIDs: list[str], IdentifyCutAndNoCut: bool, GenerateSpinning: bool, SetToolJunctions: bool, WritePartAttributes: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CheckToolParameters(self, IcoIds: list[str], CheckLevel: str, CheckTypes: list[str]) -> Teamcenter.Services.Strong.Manufacturing._2014_06.ResourceManagement.CheckToolParametersResponse: ...

class ResourceManagementService:
    """
    
            This service contains all SOA operations that are used in the context of the Resource
            Manager application.
            


Library Reference:

TcSoaManufacturingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ResourceManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetStepP21FileCounts(self, ClassIDs: list[str]) -> Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement.GetStepP21FileCountsResponse:
        """    
             This operation retrieves the count of STEP P21 product files that are available in
             a GTC vendor catalog in and below the specified classes.
             

Teamcenter Component:

             Resource Manager - Resource Manager is application used by process planners; and
             tool designers to store; modify; and retrieve information about the resources they
             use in their processes.
             
        :param ClassIDs: 

        :return: - 300361 Assortment file cannot be found.
        """
        ...
    def GetVendorCatalogInfo(self) -> Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement.GetVendorCatalogInfoResponse:
        """    
             This operation retrieves information about the GTC vendor catalogs that are available
             on the Teamcenter server machine. The multi-value preference "MRMGTCVendorCatalogRootDir"
             allows you to specify one or multiple root directories where those catalogs can be
             stored. This operation scans the given directories for GTC vendor catalogs and returns
             detailed information for each catalog.
             

Teamcenter Component:

             Resource Manager - Resource Manager is application used by process planners; and
             tool designers to store; modify; and retrieve information about the resources they
             use in their processes.
             
        :return: 
        """
        ...
    def ImportStep3DModels(self, IcoIDs: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation imports STEP 3D model files for Generic Tool Catalog (GTC) vendor
             catalog components. The STEP files are converted to NX part and to JT file format
             and imported into Teamcenter. If needed, items are created for the Classification
             objects (ICO). One UGMaster dataset for the NX part file and one DirectModel dataset
             for the JT file is created below the (new) item.
             

Use Cases:

             There are two different use cases:
             
                 A) The specified ICO is classified in a GTC vendor catalog
             class
             
             (the ICO has an attribute -159003 "3D Model file name")
             
                 B) The specified ICO is classified in an MRL MyComponents
             class
             
             (the ICO does not have an attribute -159003 "3D Model file name")
             

             In use case A, this operation retrieves the file name of the 3D model directly from
             GTC attribute
             
             -159003 "3D Model file name".
             
             (Another attribute ID instead of -159003 can be defined in the "MRMGTC3DModelAttributeID"
             preference.)
             

             In use case B, the SOA operation checks if there is an Manufacturing Resource Libraray
             (MRL) attribute -40930 "Vendor Reference Object ID" in the given ICO. This attribute
             is used to store the reference from the MRL MyComponents ICO to the GTC vendor catalog
             ICO. If this attribute exists in the ICO's class and has a valid ICO ID as value,
             the 3D model file name will be retrieved from the referenced ICO. (see use case A)
             
             (Another attribute ID instead of -40930 can be defined in the "MRMGTCReferenceObjectAttributeID"preference.)
             

             The SOA operation retrieves the information about the server-sided directory, where
             all STEP 3D models of the catalog are stored, based on the class of the GTC vendor
             catalog ICO.
             

             If there is a problem during importing one of the 3D models, the operation will continue
             importing the 3D models of the following ICOs.
             

             Note: The Graphics Builder has to be configured properly for this operation to work.
             


Teamcenter Component:

             Resource Manager - Resource Manager is application used by process planners; and
             tool designers to store; modify; and retrieve information about the resources they
             use in their processes.
             
        :param IcoIDs: 
                         The Classification object (ICO) IDs identifying the tool component under which the
                         graphics will be imported.
             
        :return: 
        """
        ...
    def ImportStepP21Files(self, ClassID: str, ImportOptions: int) -> Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement.ImportStepP21FilesResponse:
        """    
             This operation imports STEP P21 files containing the attributes values of manufacturing
             components (vendor product data) into the vendor catalog Classification classes.
             
             It creates Classification objects (ICOs) and associated data. Depending on the available
             data in the input directory, the associated items might be created to store drawing
             files and/or images.
             


Teamcenter Component:

             Resource Manager - Resource Manager is application used by process planners; and
             tool designers to store; modify; and retrieve information about the resources they
             use in their processes.
             
        :param ClassID: 
                         The class ID of a specific vendor catalog class. All catalog products from this class
                         and all child classes of this class will be imported.
             
        :param ImportOptions: 

        :return: 
        """
        ...
    def ImportVendorCatalogHierarchy(self, VendorCatalogRootDir: str, ImportOptions: int) -> Teamcenter.Services.Strong.Manufacturing._2013_12.ResourceManagement.ImportVendorCatalogHierarchyResponse:
        """    
             This operation imports the Classification class hierarchy (including class icons
             and images) of a GTC (Generic Tool Catalog) vendor catalog. The catalog hierarchy
             will be imported below the Manufacturing Resource Library (MRL) "Vendor Catalogs"
             class. The vendor catalog root directory that is needed as input parameter can be
             retrieved using the service operation getVendorCatalogInfo().
             

Teamcenter Component:

             Resource Manager - Resource Manager is application used by process planners; and
             tool designers to store; modify; and retrieve information about the resources they
             use in their processes.
             
        :param VendorCatalogRootDir: 
                         The root directory that contains the GTC vendor catalog
             
        :param ImportOptions: 
                         The import options allow you to control whether the catalog hierarchy will overwrite
                         (1) existing classes or ignore (0) those classes and not import them.
             
        :return: - 327102 Current GTC root directory does not exist
        """
        ...
    def UpdateNXToolAssemblies(self, IcoIDs: list[str], IdentifyCutAndNoCut: bool, GenerateSpinning: bool, SetToolJunctions: bool, WritePartAttributes: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation triggers specific actions on the NX side to update one or mutliple
             tool assemblies for use in NX CAM. The tool assemblies are identified by their Classification
             object (ICO) IDs. Initially, the tool assemblies are created in the Resource Manager
             in Teamcenter. Then this operation uses the Graphics Builder and calls some NX user
             functions. UGMaster datasets and an NX part files are created for the tool assemblies.
             The different input parameters trigger more actions.  To ensure that this operation
             works properly, the "NX Tool Type" (MRL attribute -45110) has to be defined in the
             tool assemblies. Turning tool assemblies have to have a "Tracking Point" (MRL attribute
             -45015) specified. This operation works only for tool assemblies that are classified
             using the Manufacturing Resource Library (MRL).
             
             Note: The Graphics Builder has to be configured properly for this operation to work.
             

Teamcenter Component:

             Resource Manager - Resource Manager is application used by process planners; and
             tool designers to store; modify; and retrieve information about the resources they
             use in their processes.
             
        :param IcoIDs: 
                         The Classification object (ICO) IDs identifying the tool assemblies
             
        :param IdentifyCutAndNoCut: 
                         If true, the "Cut" and "NoCut" information from the different tool components is
                         taken and stored in the assembly itself.
             
        :param GenerateSpinning: 
                         If true, the "Cut" and "NoCut" information from the tool assembly is taken and the
                         "Cut" and "NoCut" rotation spun.
             
        :param SetToolJunctions: 

        :param WritePartAttributes: 

        :return: 
        """
        ...
    def CheckToolParameters(self, IcoIds: list[str], CheckLevel: str, CheckTypes: list[str]) -> Teamcenter.Services.Strong.Manufacturing._2014_06.ResourceManagement.CheckToolParametersResponse:
        """    
             This operation checks for a list of tools if they define the required attribute values
             to create their 3D graphics or use them as cutters in NX CAM.  The list of tools
             is identified by their internal classification object IDs (ICO IDs).   The caller
             can select the level and type of checking that gets performed. The operation will
             return a check result consisting of a status and report for each tool  being checked.
             

Teamcenter Component:

             Resource Manager - Resource Manager is application used by process planners; and
             tool designers to store; modify; and retrieve information about the resources they
             use in their processes.
             
        :param IcoIds: 
                         A list of  classification object IDs that identify the list of tools to be checked.
             
        :param CheckLevel: 

        :param CheckTypes: 

        :return: 
        """
        ...

class StructureManagementRestBindingStub(StructureManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateOrUpdateAttachments(self, Attachments: list[Teamcenter.Services.Strong.Manufacturing._2009_06.StructureManagement.CreateOrUpdateAttachmentsData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteAttachments(self, Lines: list[Teamcenter.Soa.Client.Model.Strong.CfgAttachmentLine]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetAttachmentLineChildren(self, Attlines: list[Teamcenter.Soa.Client.Model.Strong.CfgAttachmentLine]) -> Teamcenter.Services.Strong.Manufacturing._2009_06.StructureManagement.GetAttachmentLineChildrenResponse: ...
    def CloseAttachmentWindow(self, Lines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetBOMLineActivities(self, BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Services.Strong.Manufacturing._2009_06.StructureManagement.GetBOMLineActivitiesResponse: ...
    def GetBOMLineAttachments(self, Bomlines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], Filter: list[str]) -> Teamcenter.Services.Strong.Manufacturing._2009_06.StructureManagement.GetBOMLineAttachmentsResponse: ...
    def GetStructureContextActivityLines(self, Scs: list[Teamcenter.Soa.Client.Model.Strong.StructureContext]) -> Teamcenter.Services.Strong.Manufacturing._2009_06.StructureManagement.GetStructureContextActivityLinesResponse: ...
    def GetStructureContextTopLines(self, Scs: list[Teamcenter.Soa.Client.Model.Strong.StructureContext]) -> Teamcenter.Services.Strong.Manufacturing._2009_06.StructureManagement.GetStructureContextTopLinesResponse: ...
    @typing.overload
    def PasteDuplicateStructure(self, SrcLines: list[Teamcenter.Soa.Client.Model.ModelObject], TargetLines: list[Teamcenter.Soa.Client.Model.ModelObject], CopyRulesKey: str, CopyFutureEffectivity: bool) -> Teamcenter.Services.Strong.Manufacturing._2009_10.StructureManagement.PasteDuplicateStructureResponse: ...
    @typing.overload
    def PasteDuplicateStructure(self, PasteDuplicateInput: list[Teamcenter.Services.Strong.Manufacturing._2018_11.StructureManagement.PasteDuplicateInput], CopyRulesKey: str, NotifyEvents: bool) -> Teamcenter.Services.Strong.Manufacturing._2018_11.StructureManagement.PasteDuplicateStructureResponse: ...
    def CopyEBOPStructure(self, NewRoot: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject, ConfiguringEBOPWindow: Teamcenter.Soa.Client.Model.ModelObject, WorkingWindow: Teamcenter.Soa.Client.Model.ModelObject, CopyRulesKey: str, CopyFutureEffectivity: bool) -> Teamcenter.Services.Strong.Manufacturing._2009_10.StructureManagement.CopyEBOPStructureResponse: ...
    def GetStructureContextLines(self, ScList: list[Teamcenter.Soa.Client.Model.Strong.StructureContext]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.StructureManagement.GetStructureContextLinesResponse: ...
    def GetReferenceContexts(self, Contexts: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2011_06.StructureManagement.ReferencedContextsResponse: ...
    def SetReferenceContexts(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2011_06.StructureManagement.ReferencedContexts]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def FindAffectedCCs(self, Objects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]) -> Teamcenter.Services.Strong.Manufacturing._2013_05.StructureManagement.FindAffectedCCsResponse: ...
    def MoveAndResequenceNodes(self, InputList: list[Teamcenter.Services.Strong.Manufacturing._2015_03.StructureManagement.MoveAndResequenceParameter]) -> Teamcenter.Services.Strong.Manufacturing._2015_03.StructureManagement.MoveAndResequenceResponse: ...
    def CreateCollabPlanningContext(self, CpcInput: Teamcenter.Services.Strong.Manufacturing._2015_10.StructureManagement.CreateCPCInputInfo) -> Teamcenter.Services.Strong.Manufacturing._2015_10.StructureManagement.CreateCPCResponse: ...
    def CopyRecursively(self, CopyInput: list[Teamcenter.Services.Strong.Manufacturing._2018_11.StructureManagement.CopyRecursivelyInputInfo]) -> Teamcenter.Services.Strong.Manufacturing._2018_11.StructureManagement.CopyRecursivelyResponse: ...

class StructureManagementService:
    """
    
            The StructureManagement service provides operations to create, update or delete
            attachments for BOMLines. The service provides capabilities to create clone of selected
            lines for supplied target lines. In addition, the service provides functionalities
            to get and set reference contexts for input BOMLine contexts, also to find affected
            Collaboration Context ( CC ) objects.
            
            Furthermore, the service enables to align assemblies and create or update Part and
            Design object alignments between Design and Part structures. Also it gives interface
            to synchronize the source and target Collaboration Context, create alternative scope
            for product, and find the one or more broken product views for BOMLine objects.
            

            Use cases supported by the StructureManagement service include:
            

Creating, updating, deleting attachments for given BOMLine.
            
Creating the clone of selected lines to each of the target line supplied.
            
Aligning ID in Context (Top Level) and Absolute Transformation Matrix
            between an Engineering BOM (EBOM) and a Manufacturing BOM (MBOM).
            
Creating a Collaboration Planning Context (CPC) with the given input
            structures that are to be cloned and/or referred to, and establishing a relation
            between input MECollaborationContext (CC) object and newly created CPC.
            
Finding equivalent property values on an ItemRevision for
            a given list of input properties.
            
Pasting pastes an assembly item under a target assembly Item
            or replacing an existing assembly Item with a new assembly Item while
            retaining any in-context edits on the properties and attachments under the target
            assembly.
            
Linking or unlinking the PSBOMView objects of the two input
            structures by the input relation.
            
Copying the Mfg0BvrOperation lines from a Bill of Process
            (BOP) structure and paste them to a PlantBOP.
            
Converting the URL representing a BOMLine to a BOMLine
            instance.
            
Cloning the provided source BOMLine and pasting the cloned
            line under the corresponding target BOMLine.
            




Library Reference:

TcSoaManufacturingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> StructureManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateOrUpdateAttachments(self, Attachments: list[Teamcenter.Services.Strong.Manufacturing._2009_06.StructureManagement.CreateOrUpdateAttachmentsData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             create or update attachments. The following properties are loaded automatically for
             the line:me_cl_object_name,me_cl_object_type,me_cl_object_desc and these for the
             workspaceobject:object_name, object_type, object_desc irrespective of policy files.
             
        :param Attachments: 
                         input either bomline or attachmentline (parent) and the relations and workspace objects
                         to be processed as attachments.
             
        :return: failures returned as partial failures in serviceData
        """
        ...
    def DeleteAttachments(self, Lines: list[Teamcenter.Soa.Client.Model.Strong.CfgAttachmentLine]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             remove the specified attachment lines. Only if these lines have a parent is this
             action performed.
             
        :param Lines: 
                         remove the specified lines from the parent attachment window.
             
        :return: partial errors retuned in the serviceData
        """
        ...
    def GetAttachmentLineChildren(self, Attlines: list[Teamcenter.Soa.Client.Model.Strong.CfgAttachmentLine]) -> Teamcenter.Services.Strong.Manufacturing._2009_06.StructureManagement.GetAttachmentLineChildrenResponse:
        """    
             given a vector of input attachmentlines - for each - get the immediate level of child
             attachment lines. For each attachment line the following properties are available
             on client side automatically:me_cl_object_name, me_cl_object_type, me_cl_object_desc
             
        :param Attlines: 
                         input parent attachment lines
             
        :return: returns the child attachment lines for a given line.
        """
        ...
    def CloseAttachmentWindow(self, Lines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             close any attachment window that got created for the bomline during the soa session.
             This will only close the attachment windows that are created to support the attachment
             line soa calls.
             
        :param Lines: 
                         input bomlines for which the attachmentwindow has to be closed.
             
        :return: any partial errors are returned in the response
        """
        ...
    def GetBOMLineActivities(self, BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Services.Strong.Manufacturing._2009_06.StructureManagement.GetBOMLineActivitiesResponse:
        """    
             given a bomline get it's activities (these activities are really the children of
             the root activity associated with the bomline). This assumes that the bomline is
             a bopline. The following properties are available on client side for each line irrespective
             of policy: al_activity_object_name, al_activity_time. If the actual attachments of
             these activity lines are desired - use the getProperties method of DataManagementService
             with al_object as the property name.
             
        :param BomLines: 
                         input vector of bomlines for which activities are needed.
             
        :return: returns a vector of a map of bomline to it's activities.
        """
        ...
    def GetBOMLineAttachments(self, Bomlines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], Filter: list[str]) -> Teamcenter.Services.Strong.Manufacturing._2009_06.StructureManagement.GetBOMLineAttachmentsResponse:
        """    
             given a bomline get it's attachments. The follow properties are available on client
             side irrespective of policy: me_cl_object_name, me_cl_object_type, me_cl_object_desc
             
        :param Bomlines: 
                         list of input BOMLines
             
        :param Filter: 
                         optional relation filter to be used for attachments. The relation names specified
                         here are used as a filter on the attachmentwindow
             
        :return: returns a  map of bomline to attachments
        """
        ...
    def GetStructureContextActivityLines(self, Scs: list[Teamcenter.Soa.Client.Model.Strong.StructureContext]) -> Teamcenter.Services.Strong.Manufacturing._2009_06.StructureManagement.GetStructureContextActivityLinesResponse:
        """    
             Given a vector of StructureContext objects, for each - get the activitylines that
             are attached to the SC by the relation - TC_SC_activities. Currently, this is only
             created during a population of WorkInstruction page by selecting an activity. The
             following properties are available to the client irrespective of policy: al_activity_object_name,
             al_activity_time
             
        :param Scs: 
                         list of input structurecontext objects
             
        :return: lines has the map of sc to activitylines, and serviceData has partial errors.
        """
        ...
    def GetStructureContextTopLines(self, Scs: list[Teamcenter.Soa.Client.Model.Strong.StructureContext]) -> Teamcenter.Services.Strong.Manufacturing._2009_06.StructureManagement.GetStructureContextTopLinesResponse:
        """    
             method to get the toplines of specified StructureContext. Client is responsible for
             closing any windows that are returned during this call. The following properties
             are available irrespective of policy:bl_line_name
             
        :param Scs: 
                         input list of SC's
             
        :return: returns the response structure containing the map of StructureContext to it's lines
             and the response.
        """
        ...
    @typing.overload
    def PasteDuplicateStructure(self, SrcLines: list[Teamcenter.Soa.Client.Model.ModelObject], TargetLines: list[Teamcenter.Soa.Client.Model.ModelObject], CopyRulesKey: str, CopyFutureEffectivity: bool) -> Teamcenter.Services.Strong.Manufacturing._2009_10.StructureManagement.PasteDuplicateStructureResponse: ...
    @typing.overload
    def PasteDuplicateStructure(self, PasteDuplicateInput: list[Teamcenter.Services.Strong.Manufacturing._2018_11.StructureManagement.PasteDuplicateInput], CopyRulesKey: str, NotifyEvents: bool) -> Teamcenter.Services.Strong.Manufacturing._2018_11.StructureManagement.PasteDuplicateStructureResponse: ...
    def CopyEBOPStructure(self, NewRoot: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject, ConfiguringEBOPWindow: Teamcenter.Soa.Client.Model.ModelObject, WorkingWindow: Teamcenter.Soa.Client.Model.ModelObject, CopyRulesKey: str, CopyFutureEffectivity: bool) -> Teamcenter.Services.Strong.Manufacturing._2009_10.StructureManagement.CopyEBOPStructureResponse:
        """    
             Creates a clone of the supplied root of the configuringEBOPWindow under the rootObject
             specified.
             
        :param NewRoot: 
                         The newly created rootobject under which the structure will be cloned.
             
        :param ConfiguringEBOPWindow: 
                         The window with source BOP(GBOP/PBOP) item as root.
             
        :param WorkingWindow: 
                         optional window (the actual source window), from which the IncrementalChange Rev
                         is picked up. In addition the window settings like show unconfigured etc. are also
                         picked up.
             
        :param CopyRulesKey: 
                         The name of the preference which will be used for cloning rule to be used.
             
        :param CopyFutureEffectivity: 
                         if true, future ICRevs will be created appropriately, instead of all ICEs being cloned
                         to the currently active ICRev. Note that if this is true - it is expected that there
                         is an currently selected ICRev in the working window.
             
        :return: returns the input rootobject whose structure will be updated along with any created
             IC revs.
        """
        ...
    def GetStructureContextLines(self, ScList: list[Teamcenter.Soa.Client.Model.Strong.StructureContext]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.StructureManagement.GetStructureContextLinesResponse:
        """    Return the top lines and any selected lines if present.
        :param ScList: 
                         The list of StructureContexts for which toplines and selected lines are needed.
             
        :return: Return a map of Structure Context to Top Line and a map of Structure Context to selected
             child lines.
        """
        ...
    def GetReferenceContexts(self, Contexts: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2011_06.StructureManagement.ReferencedContextsResponse:
        """    return referenced contexts of input context.
        :param Contexts: 
                         vector of input contexts
             
        :return: return ReferenceContextResponse structure
        """
        ...
    def SetReferenceContexts(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2011_06.StructureManagement.ReferencedContexts]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    set Reference context according to user choice.
        :param Input: 
                         includes ReferencedContexts structure
             
        :return: service data will return errors only and no data.
        """
        ...
    def FindAffectedCCs(self, Objects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]) -> Teamcenter.Services.Strong.Manufacturing._2013_05.StructureManagement.FindAffectedCCsResponse:
        """    
             This operation finds all of the Collaboration Contexts which contain a process structure,
             which contains the input objects (e.g. Item, MEWorkArea, METool, MEProcess or MEOperation).
             The input objects must be of type Item or ItemRevision (BOMLine objects are not valid
             input objects).
             

Dependencies:

             whereReferenced
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Objects: 
                         The items to find their Collaboration Contexts (as a reference).
             
        :return: 300070: If Where Referenced operation fails for the input object.
        """
        ...
    def MoveAndResequenceNodes(self, InputList: list[Teamcenter.Services.Strong.Manufacturing._2015_03.StructureManagement.MoveAndResequenceParameter]) -> Teamcenter.Services.Strong.Manufacturing._2015_03.StructureManagement.MoveAndResequenceResponse:
        """    
             This operation moves and/or re-sequences the nodes in the structure.
             

Use Cases:

             Use Case 1: Re-sequencin g nodes within parent in a structure.
             
             This operation can be used in M anufacturing Process Planning (MPP) application to
             resequence a node in a struct ure. For example, in a product structure an Item
             or  BOMLine can be reseqenced within the parent by dragging and dropping t
             he Item in between the siblings. Same could be done in proces s structure
             by dragging and dropping a process or operation BOMLine. As a result of drop,
             the find number of the node and its subsequent sibling are modified.
             
             Use Case 2: Re-parent and re-sequence of nodes.
             
             This operation can be used in MPP application to move the nodes from one parent to
             another and sequenced them among the siblings of new parent. For example, in a process
             structure a process or operation BOMLine objects can be dragged and dropped
             in between the child nodes of another process BOMLine. The dragged processes
             or operations are moved as children of the new process BOMLine and sequenced
             among the sibling as per dropped location. While drag and drop, UI presents an option
             whether to clone the nodes. If selected then the nodes are cloned instead of re-parent.
             
             Use Case 3: Moving the processes or operations to process resource in Plant Bill
             of Processes (BOP).
             
             This operation can be used to allocate the process or operation BOMLine of
             type Mfg0BvrProcess or Mfg0BvrOperation to a process resource of type
             Mfg0BvrProcessResource in a Plant BOP structure. The find number of dropped
             BOMLine objects could be calculated either in the context of the process station
             of type Mfg0BvrProcessStation to which process resource is a child object,
             or process resource is itself. If the context is process station of type Mfg0BvrProcessStation
             then the find numbers of the dropped BOMLine objects are calculated based
             on the existing processes or operations that are a child object of process station.
             If the context is process resource then the calculation is based on the processes
             or operations allocated to that process resource. In Teamcenter MPP application,
             the context is always a process station BOMLine.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param InputList: 
                         The list of moveAndResequenceParameter structure. Each structure specifies the nodes
                         to be moved, their target, whether dropped on the target, context based on which
                         find number to be decided and whether to clone or move the nodes to the new target.
             
        :return: 
        """
        ...
    def CreateCollabPlanningContext(self, CpcInput: Teamcenter.Services.Strong.Manufacturing._2015_10.StructureManagement.CreateCPCInputInfo) -> Teamcenter.Services.Strong.Manufacturing._2015_10.StructureManagement.CreateCPCResponse:
        """    
             This service operation creates a Collaboration Planning Context (CPC) with the given
             input  structures that are to be cloned and/or referred to, and establishes a relation
             between input MECollaborationContext (CC) object and newly created CPC.
             
             CPC is a CC object itself, it is a term used for mix production.
             

Use Cases:

             A user creates a CPC object in Manufacturing Process Planner (MPP) application using
             an existing opened CC structure. Subsequently a relation Mfg0MEAlternatePlanningRel
             is created between newly created CPC and the orginal CC.
             

             Use Case 1: The user opens a CC structure, select some structures available in the
             CC and creates a CPC.
             

             Use Case 2: A user opens a CC structure, select some of the scopes in that structure
             and create a CPC.
             

             Use Case 3: A user opens a CC structure, select some structures/scopes, provide whether
             they need to be referred or cloned and provide cloning parameters such as Clone Suppressed
             Lines, Carry Over ICs etc. to create a CPC.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param CpcInput: 
                         The input to the service is a structure which contains a list of BOMLine objects
                         that are to be cloned and\or referred, cloning information, name and description
                         of new CPC.
             
        :return: 
        """
        ...
    def CopyRecursively(self, CopyInput: list[Teamcenter.Services.Strong.Manufacturing._2018_11.StructureManagement.CopyRecursivelyInputInfo]) -> Teamcenter.Services.Strong.Manufacturing._2018_11.StructureManagement.CopyRecursivelyResponse: ...

class StructureSearchRestBindingStub(StructureSearchService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def NextSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Manufacturing._2009_10.StructureSearch.StructureSearchResultResponse: ...
    def StartSearch(self, Scope: list[Teamcenter.Soa.Client.Model.ModelObject], SearchExpression: Teamcenter.Services.Strong.Manufacturing._2009_10.StructureSearch.SearchExpressionSet, MfgSearchCriteria: Teamcenter.Services.Strong.Manufacturing._2009_10.StructureSearch.MFGSearchCriteria) -> Teamcenter.Services.Strong.Manufacturing._2009_10.StructureSearch.StructureSearchResultResponse: ...
    def StopSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Manufacturing._2009_10.StructureSearch.StructureSearchResultResponse: ...
    def FindStudies(self, InputNodes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2013_05.StructureSearch.FindStudiesResponse: ...
    def SearchConnectedLines(self, InputConnLines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2014_06.StructureSearch.SrchConnectedLinesResponse: ...
    def CreateOrUpdateAssignmentRecipe(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch.CreateOrUpdateAssignmentRecipeInputElem]) -> Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch.CreateOrUpdateAssignmentRecipeResp: ...
    def DeleteAssignmentRecipes(self, Recipes: list[Teamcenter.Soa.Client.Model.ModelObject], RecipeAnchors: list[Teamcenter.Soa.Client.Model.ModelObject], ContextForRemovingResolvedObjs: Teamcenter.Soa.Client.Model.ModelObject, AppKey: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetAssignmentRecipes(self, RecipeAnchors: list[Teamcenter.Soa.Client.Model.ModelObject], RecipeNames: list[str], AppKey: str) -> Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch.GetAssignmentRecipesResp: ...
    def ResolveAssignmentRecipe(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch.ResolveAssignmentRecipeInputElement]) -> Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch.ResolveAssignmentRecipeResp: ...

class StructureSearchService:
    """
    
            The StructureSearch service provides operations to perform search functionality
            on a given input.
            

            Use cases supported by the StructureSearch service include:
            

Searching on given input BOMLine objects for the input search
            criteria.
            
Searching for connected BOMLine objects for the input connection
            BOMLine objects.
            
Interpreting the search criteria objects and return saved BOMLine
            occurrences.
            
Finding study objects referencing the input process/operation object.
            




Library Reference:

TcSoaManufacturingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> StructureSearchService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def NextSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Manufacturing._2009_10.StructureSearch.StructureSearchResultResponse:
        """    Process one additional step of the search identified by the cursor.
        :param SearchCursor: 
                         searchCursor
             
        :return: - result of next search step
        """
        ...
    def StartSearch(self, Scope: list[Teamcenter.Soa.Client.Model.ModelObject], SearchExpression: Teamcenter.Services.Strong.Manufacturing._2009_10.StructureSearch.SearchExpressionSet, MfgSearchCriteria: Teamcenter.Services.Strong.Manufacturing._2009_10.StructureSearch.MFGSearchCriteria) -> Teamcenter.Services.Strong.Manufacturing._2009_10.StructureSearch.StructureSearchResultResponse:
        """    
             Start searching a structure for a given search expression within the scope specified.
             search can also be narrowed to a specific object type, item name, and logical designator
             
        :param Scope: 
                         scope lines within which to search
             
        :param SearchExpression: 
                         generic search expression
             
        :param MfgSearchCriteria: 
                         The MFG addition search criteria
             
        :return: - result of search startup
        """
        ...
    def StopSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Manufacturing._2009_10.StructureSearch.StructureSearchResultResponse:
        """    
             Stop and close down a search identified by a cursor. Throws SearchAlreadyStoppedException
             if the search has already been stopped.
             
        :param SearchCursor: 
                         the search identifier
             
        :return: StructureSearchResultResponse
        """
        ...
    def FindStudies(self, InputNodes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2013_05.StructureSearch.FindStudiesResponse:
        """    
             This operation finds all study objects that reference a given process/operation business
             object.
             
        :param InputNodes: 
                         A list of business objects for which referencing studies should be searced (objects
                         of type Mfg0BvrProcess or Mfg0BvrOperation).
             
        :return: The Mfg0BvrStudy objects that refer to the input business objects.
        """
        ...
    def SearchConnectedLines(self, InputConnLines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2014_06.StructureSearch.SrchConnectedLinesResponse:
        """    
             This operation searches and returns the connected BOMLine objects for the
             input connection BOMLine objects.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param InputConnLines: 
                         Input <b>BOMLine</b> objects whose connected to information needs to be found.
             
        :return: 
        """
        ...
    def CreateOrUpdateAssignmentRecipe(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch.CreateOrUpdateAssignmentRecipeInputElem]) -> Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch.CreateOrUpdateAssignmentRecipeResp:
        """    
             This operation creates or updates the search recipe on a Manufacturing BOM (MBOM)
             node. The recipe is used to automatically resolve Engineering BOM (EBOM) lines under
             the MBOM node with the recipe. If recipe is updated after a prior resolve there must
             be a subsequent call to resolve the new recipe using the resolveAssignmentRecipe.
             The operation will throw an ServiceException if the Teamcenter database schema does
             not have the recipe constructs. It requires the recipe to be provided as a SearchStructureContext
             object (capturing structure search parameters) and/or key-value pairs of AbsOccurrence
             attributes.
             

Use Cases:

             There is a need to automatically consume Engineering BOM (EBOM) nodes under a phantom
             Manufacturing BOM (MBOM) node based on search criteria provided by Structure Search.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         A list of input elements specifying the details of the recipe to be created and attached
                         to a given node.
             
        :return: 
        """
        ...
    def DeleteAssignmentRecipes(self, Recipes: list[Teamcenter.Soa.Client.Model.ModelObject], RecipeAnchors: list[Teamcenter.Soa.Client.Model.ModelObject], ContextForRemovingResolvedObjs: Teamcenter.Soa.Client.Model.ModelObject, AppKey: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes the given explit recipe (Mfg0MEMBOMRecipe) objects.
             Optionally, can delete all recipe objects attached to the recipeAnchors ( BOMLine
             Objects). If the contextForRemovingResolvedObjs is provided, the resolved lines will
             be removed unless those are resolved by other recipes too. Pass NULL for this parameter
             if resolved lines are not to be cleaned up.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Recipes: 
                         A list of <b>Mfg0MEMBOMRecipe</b> objects to be deleted.
             
        :param RecipeAnchors: 
                         A list of  <b>BOMLine</b> objects for which recipes are to be deleted.
             
        :param ContextForRemovingResolvedObjs: 
                         An optional BOMWindow object to indicate resolved lines are to be deleted too.
             
        :param AppKey: 
                         The name of the Application to identify the resolver in the server. Currently, only
                         allowed value is Mfg0AssignmentRecipe.
             
        :return: 
        """
        ...
    def GetAssignmentRecipes(self, RecipeAnchors: list[Teamcenter.Soa.Client.Model.ModelObject], RecipeNames: list[str], AppKey: str) -> Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch.GetAssignmentRecipesResp:
        """    
             This operation get the recipe (Mfg0MEMBOMRecipe) objects attached to the underlying
             ItemRevisions of the recipeAnchors. Currently, only BOMLine objects can be
             specified as recipeAnchors.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param RecipeAnchors: 
                         A list of  <b>BOMLine</b> Objects for which recipes are to be obtained.
             
        :param RecipeNames: 
                         An optional list of recipeNames to search for recipes under the specified recipeAnchors.
             
        :param AppKey: 
                         The name of the Application to identify the resolved in the server. Currently, only
                         allowed value is Mfg0AssignmentRecipe.
             
        :return: 
        """
        ...
    def ResolveAssignmentRecipe(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch.ResolveAssignmentRecipeInputElement]) -> Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch.ResolveAssignmentRecipeResp:
        """    
             This operation resolves the saved search recipe on a Manufacturing BOM (MBOM) node.
             The recipe is used to automatically resolve Engineering BOM (EBOM) lines under the
             MBOM node with the recipe. The operation will throw an ServiceException if the Teamcenter
             database schema does not have the recipe constructs.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         A list of ResolveAssignmentRecipeInputElement structures each detailing the node
                         on which the recipe is to be resolved.
             
        :return: 
        """
        ...

class TimeManagementRestBindingStub(TimeManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def AllocatedTimeRollUp(self, Object: Teamcenter.Services.Strong.Manufacturing._2008_06.TimeManagement.AllocatedTime) -> Teamcenter.Services.Strong.Manufacturing._2008_06.TimeManagement.AllocatedTimeResponse: ...
    def TimeAnalysisRollup(self, Inputs: Teamcenter.Services.Strong.Manufacturing._2008_06.TimeManagement.TimeAnalysisInputs) -> Teamcenter.Services.Strong.Manufacturing._2008_06.TimeManagement.TimeAnalysisRollupResponse: ...
    def CalculateCriticalPathEx(self, Roots: list[Teamcenter.Soa.Client.Model.ModelObject], ProcessLeafNodes: bool) -> Teamcenter.Services.Strong.Manufacturing._2010_09.TimeManagement.CalculateCriticalPathResponseEx: ...
    def GetActivityTimes(self, RootNodes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2010_09.TimeManagement.GetActivityTimesResponse: ...
    def PopulateAllocatedTimeProperties(self, RootNodes: list[Teamcenter.Soa.Client.Model.ModelObject], PropagateZeroValues: bool, StopLevel: int, Precedence: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UpdateTimeManagementProperties(self, RootNodes: list[Teamcenter.Soa.Client.Model.ModelObject], FieldNames: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class TimeManagementService:
    """
    
            Contains TimeManagement Services
            


Library Reference:

TcSoaManufacturingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> TimeManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def AllocatedTimeRollUp(self, Object: Teamcenter.Services.Strong.Manufacturing._2008_06.TimeManagement.AllocatedTime) -> Teamcenter.Services.Strong.Manufacturing._2008_06.TimeManagement.AllocatedTimeResponse:
        """    Calculates the allocated time for each requested bop line.
        :param Object: 
                         TODO
             
        :return: structure containing the results of the allocated time calculation.
        """
        ...
    def TimeAnalysisRollup(self, Inputs: Teamcenter.Services.Strong.Manufacturing._2008_06.TimeManagement.TimeAnalysisInputs) -> Teamcenter.Services.Strong.Manufacturing._2008_06.TimeManagement.TimeAnalysisRollupResponse:
        """    
             Calculates the total time for each activity category under a requested bop line.
             An additional calculation is all the run time propertie related to the bop line time
             calculations such as total time and duration time.
             
        :param Inputs: 
                         a Time Analysis Input structure, required
             
        :return: structure containing the results of the time analysis calculation.
        """
        ...
    def CalculateCriticalPathEx(self, Roots: list[Teamcenter.Soa.Client.Model.ModelObject], ProcessLeafNodes: bool) -> Teamcenter.Services.Strong.Manufacturing._2010_09.TimeManagement.CalculateCriticalPathResponseEx:
        """    
             This operation computes the critical paths for processes or operations. The critical
             path is the sequence of processes or operations that determine the minimum duration
             of a specific object.  If the processLeafNodes flag is set, the algorithm will traverse
             down the structure until it finds all leaf nodes that make up the path. Otherwise
             only the direct children will be taken into account.
             
        :param Roots: 
                         The list of MFG process or operation objects the critical path is to be calculated
                         for.
             
        :param ProcessLeafNodes: 
                         A flag that determines whether to compute the path from the leave nodes of the process/operation
                         structure or from the direct children of a root object.
             
        :return: For each object in the 'roots' vector the list of critical paths. There may be more
             than one per object if multiple paths of the same length exist.
        """
        ...
    def GetActivityTimes(self, RootNodes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Manufacturing._2010_09.TimeManagement.GetActivityTimesResponse:
        """    
             Traverses a set of process or operation trees and computes the effective accumulated
             times of all leaf activities, ignoring any flows between processes, operations or
             activities.  For each activity category that is encountered, a distinct value is
             returned.
             
        :param RootNodes: 
                         The root nodes of the tree structures for which the activity times are to be computed.
             
        :return: The list of activity times indexed by category for each root node in a GetActivityTimesResponse
             structure.
        """
        ...
    def PopulateAllocatedTimeProperties(self, RootNodes: list[Teamcenter.Soa.Client.Model.ModelObject], PropagateZeroValues: bool, StopLevel: int, Precedence: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Updates the allocated time property recursively for all nodes of a list of process
             or operation trees.
             
        :param RootNodes: 
                         Defines the root nodes of the trees to be updated.
             
        :param PropagateZeroValues: 
                         If this parameter is false, the allocated time of a specific node is only overwritten
                         if more detailed information is available at a lower level.  This means that if a
                         given node is not further detailed by any sub node, or if all of the computed times
                         of the sub nodes are 0, the allocated time property of the parent will remain unchanged.
             
        :param StopLevel: 
                         If this parameter is greater than 0, the update will stop that number of levels below
                         the root node. This means that the root node itself will be excluded from the update
                         if the value is 1; if it is 2, all child nodes with exception of the root's direct
                         children will be updated and so forth.
             
        :param Precedence: 
                         The precedence vector defines how the allocated time of a leaf node is to be determined.
                         Each entry must consist of one of the values 'estimated_time', 'simulated_time',
                         'allocated_time' or 'analysis'.  In the case of 'estimated_time' or 'simulated_time'
                         the value is retrieved from the respective property of the TimeAnalysis form.  In
                         case of 'allocated_time' the previous value of the property will be reused.  The
                         value 'analysis' specifies that the allocated time of an operation is to be recursively
                         computed from its activity structure; for processes the result will always be 0.
                         In case the evaluation of the first entry of the 'precedence' vector leads to a 0
                         value, the algorithm will proceed with the next entry until the end of the vector
                         is reached. If no suitable value is found, the resulting value will be 0.
             
        :return: The ServiceData structure containing error information for this service request.
        """
        ...
    def UpdateTimeManagementProperties(self, RootNodes: list[Teamcenter.Soa.Client.Model.ModelObject], FieldNames: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Recomputes the cached values of the runtime properties related to TimeManagement
             for one or more process or operation trees. This will affect the properties of all
             nodes of the tree structures defined by the rootNodes parameter.
             
        :param RootNodes: 
                         The root nodes of the tree structures for which the runtime properties are to be
                         calculated.
             
        :param FieldNames: 
                         The names of the calculated fields to recompute. Currently the following fieldnames
                         are accepted: Mfg0calc_duration, Mfg0calc_start_time, Mfg0calc_dur_start_time, bl_me_work_time
                         and bl_me_duration. If the fieldName vector is empty, all of the properties will
                         be updated.
             
        :return: A ServiceData structure that contains the computed property values in the DataObject
             member. The structure also informs about errors that occurred during the course of
             the operation.
        """
        ...

class TimeWayPlanRestBindingStub(TimeWayPlanService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetTWPInformation(self, Input: Teamcenter.Services.Strong.Manufacturing._2013_05.TimeWayPlan.TwpInfoInput) -> Teamcenter.Services.Strong.Manufacturing._2013_05.TimeWayPlan.TwpResponse: ...
    def SetProductImage(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2013_05.TimeWayPlan.ProductImageInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class TimeWayPlanService:
    """
    
            This service exposes operations that are used to populate and fetch the Time Way
            Plan (TWP) information of the business objects such as process stations, process
            lines, process areas or plant BOP.
            
            Â Â Â Â 
            
            Use Cases:
            
            This service provides following use cases for the specified set of business objects
            such as process stations, process lines, process area, or product BOP.
            

Use Case 1: Fetching TWP information for the business objects
            such as Process Stations. The operation getTWPInformation can be used for fetching
            the Time Way Plan information that are used to display the Time Way Plan. The user
            can request either part of or full TWP data.
            
Use Case 2: Setting product Image for the Process Station.
            The operation setProductImage sets the product image associated with the Process
            Station. This image is used in TWP view for that station.
            
Use Case 3: Setting location information for the process station.
            The operation setTWPLocationInfo sets the location information of process station
            such as station length, station width, X-Y coordinates indicating its location in
            plant and orientation.
            


            This information is used to display the station in TWP view.
            


Library Reference:

TcSoaManufacturingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> TimeWayPlanService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetTWPInformation(self, Input: Teamcenter.Services.Strong.Manufacturing._2013_05.TimeWayPlan.TwpInfoInput) -> Teamcenter.Services.Strong.Manufacturing._2013_05.TimeWayPlan.TwpResponse:
        """    
             This service operation fetches the Time Way Plan (TWP) information. The operation
             takes objects from the plant Bill of Processes (BOP) for which TWP information is
             required, the list of strings specifying what information is required and the context
             product BOP. The object can be process station(s), process line(s), process area(s),
             or plant BOP. The list of string will have values "OperationDetails", "ExecutionPositions",
             "ProductDiagram", and "PlantCarpet" based on which response will contain the information.
             These values will be applicable to all the objects for which TWP information is required.
             

             This information is used to display the Time Way Plan view.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         The input structure contains object(s) for which information is required, the list
                         of string specifying what information is required and the product Bill Of Process
                         (BOP) context. The object can be process station(s), process line(s), process area(s),
                         or plant BOP.
             
        :return: Â Â Â Â 251050 - No Product Bill Of Process (BOP) is associated with
             the Plant BOP.
        """
        ...
    def SetProductImage(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2013_05.TimeWayPlan.ProductImageInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service operation sets a product image for the given input object. The operation
             takes objects from the plant Bill Of Processes (BOP) for which the product image
             is to be set, the business object of the context product BOP, and the business object
             of the dataset representing the product image. The object   from the plant BOP for
             which product image is to be set can be process station(s), process line(s), process
             area(s), or plant BOP.
             
             This operation will create a relation between the object from the plant BOP input
             object and  the dataset business object in context of the input product BOP.
             
             The specified product image is displayed on the station in the Time Way Plan (TWP)
             view.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         The input structure contains object(s) for which product image is to be set, the
                         business object of the dataset  representing the image and the product Bill Of Processes
                         (BOP) context. The object can be process station(s), process line(s), process area(s),
                         or plant BOP.
             
        :return: 
        """
        ...

class ValidationRestBindingStub(ValidationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ExecuteValidations(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2012_09.Validation.ValidationCheckExecutionParam], FailAllOnError: bool) -> Teamcenter.Services.Strong.Manufacturing._2012_09.Validation.ValidationsChecksExecutionResponse: ...
    def GetAllValidations(self) -> Teamcenter.Services.Strong.Manufacturing._2012_09.Validation.ValidationsChecksObjectsResponse: ...
    def GetMaturityReport(self, MaturityReportRequest: Teamcenter.Services.Strong.Manufacturing._2014_12.Validation.MaturityReportRequest) -> Teamcenter.Services.Strong.Manufacturing._2014_12.Validation.MaturityReportResponse: ...
    def GetAllRegisteredCallbacks(self, CallbackType: str) -> Teamcenter.Services.Strong.Manufacturing._2017_05.Validation.RegisteredCallbackObjectsResponse: ...

class ValidationService:
    """
    
            Validation Service
            


Library Reference:

TcSoaManufacturingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ValidationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ExecuteValidations(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2012_09.Validation.ValidationCheckExecutionParam], FailAllOnError: bool) -> Teamcenter.Services.Strong.Manufacturing._2012_09.Validation.ValidationsChecksExecutionResponse:
        """    
             This SOA function is to execute the validation checks by the user choice from the
             UI.
             
        :param Input: 
                         Validation Check Execution Param
             
        :param FailAllOnError: 
                         whether or not to fail all tests when error occurs on a specific validation check
                         for a specific line or to continue.
             
        :return: Validations Checks Execution Response
        """
        ...
    def GetAllValidations(self) -> Teamcenter.Services.Strong.Manufacturing._2012_09.Validation.ValidationsChecksObjectsResponse:
        """    
             This SOA function is to get all the customized registered callback to show the user
             in the UI.
             
        :return: 
        """
        ...
    def GetMaturityReport(self, MaturityReportRequest: Teamcenter.Services.Strong.Manufacturing._2014_12.Validation.MaturityReportRequest) -> Teamcenter.Services.Strong.Manufacturing._2014_12.Validation.MaturityReportResponse:
        """    
             This service operation evaluates the maturity of the structure based on certain rules.
             The operation executes  specified rules on objects of the structure and returns if
             the rules are fulfilled or not. The operation takes  BOMLine as a scope to evaluate
             the maturity of objects under it, the list of rules to evaluate the maturity, and
             supporting information. In response the operation returns the objects and their maturity
             status along with other relevant information.
             

Use Cases:

             Use Case 1 - User checks maturity of a structure.
             
                 User can check the maturity of structure by right clicking
             on root or topline of the structure. Consider a Logistic structure consisting of
             logistics bill of process (LBOP), part family, parts under the part family and in-plant
             supply chain. User needs to know if all part families have part specified or if all
             part families have at least one in-plant supply chain or if all parts have at least
             one in-bound supply chain. User can choose the predefined rules and use this operation
             to evaluate the rules on part family and in response see a maturity report.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param MaturityReportRequest: 
                         supportingInformation -Â Â Â Â Additional supporting information
                         that could be used to evaluate the maturity. Currently this input is not used by
                         the operation.
             
        :return: 
        """
        ...
    def GetAllRegisteredCallbacks(self, CallbackType: str) -> Teamcenter.Services.Strong.Manufacturing._2017_05.Validation.RegisteredCallbackObjectsResponse:
        """    
             This operation returns all the registered customized callbacks for the given callback
             type.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param CallbackType: 
                         The type of customized registered callback functions to retrieve.
             
        :return: The response is the object containing callback function details and the service data
        """
        ...

