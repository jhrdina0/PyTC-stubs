import System
import System.Collections
import Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement
import Teamcenter.Soa.Client.Model
import typing

class AddOrRemoveContextsInfo:
    """
    
The input parameter to the operation is the target context to associate to, list
of source contexts and the relation name to associate or disassociate with and
the
additional action required for association or disassociation.
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """The target context to associate or disassociate with e.g. Mfg0BvrProductBOP or Mfg0BvrPlantBOP."""
    AddContext: list[Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AssociatedContextInfo]
    """
            The list of source contexts , e.g  Mfg0BvrGenericBOP or Mfg0BvrProductBOP, that should
            be associated with the target context with the specified relation.
            """
    RemoveContext: list[Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.AssociatedContextInfo]
    """
            The list of source contexts, e.g. Mfg0BvrGenericBOP or Mfg0BvrProductBOP, for which
            the association with the target context should be removed with the specified relation.
            """
    ActionMap: System.Collections.Hashtable
    """
            A map (string, list of string) of context and related actions. The data allows additional
            action required for the add or remove context. e.g. the key of the map will be "RemoveContext"
            and "AddContext" and the values for the key such as for the key "RemoveContext" the
            action will be "RemoveLink" and "RemoveAllocation".
            
            "RemoveLink" will remove the link between the allocations.
            
            "RemoveAllocation" will remove the allocations.
            
"""

class CloneAssemblyInputData:
    """
    
Input to the service that is a source object that should be cloned, target
parent
object for the cloned object and additional parameters needed for functionality.

    """
    def __init__(self, ) -> None: ...
    SourceObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Business object of the source structure to be cloned. The expected buisness object
            must be of type Item, ItemRevision or BOMLine.
            """
    ScopeSearchObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Business object of the scope object to search in for parts to be replaced. The expected
            buisness object must be of type Item, ItemRevision or BOMLine.
            If not specified, the source object will be used.
            """
    ParentObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Business object of the parent object for the new created clone object. The expected
            buisness object must be of BOMLine type. If not specified, the parent of the
            sourceObject will be used.
            """
    SourceOccEff: str
    """Occurrence effectivity of the source object."""
    NewCloneOccEff: str
    """Occurrence effectivity of the new cloned object."""
    AdditionalInfo: Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.GeneralInfo
    """
            Additional information needed to create the new cloned object like name, revision,
            description etc.
            """

class CloneAssemblyResponse:
    """
    output structure of cloneAssemblyAndProcessObjects SOA
    """
    def __init__(self, ) -> None: ...
    ClonedObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Business object of new BOMLine object, created as a result of clone operation
            under the new target.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard Service Data"""

class EstablishOriginLinkCandidates:
    """
    Source and targets that are candidates to link
    """
    def __init__(self, ) -> None: ...
    SourceObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The source object is either operation of type Mfg0BvrOperation or process
            of type Mfg0BvrProcess.
            """
    TargetObjects: list[EstablishOriginLinkTargetLinkState]
    """The list of target object and its linked state."""

class EstablishOriginLinkCandidatesInput:
    """
    Source and target candidates to establish origin link.
    """
    def __init__(self, ) -> None: ...
    SourceObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Operation of type Mfg0BvrOperation or process of type Mfg0BvrProcess
            from Generic BOP or Product BOP structure. Same object type from target objects are
            considered to establish the origin link.
            """
    TargetObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            Operation of type Mfg0BvrOperation or process of type Mfg0BvrProcess
            to be linked. The objects are in the context of Product BOP or Plant BOP.
            """

class EstablishOriginLinkInfo:
    """
    Input to the service is a list of a source and targets to be linked.
    """
    def __init__(self, ) -> None: ...
    InputObjects: list[EstablishOriginLinkCandidatesInput]
    """soure and target candidates to establish origin link."""
    Criteria: list[str]
    """
            The list of criteria based on which the origin link established. Currently, the only
            criteria supported is logical designator property. Possible value of parameter is
            "LD" signifying that all source and target objects with matching logical designator
            property are considered for the operation.
            """
    ConsiderHierarchy: bool
    """
            Specifies whether hierarchy of source and target should be considered while establishing
            the origin link. If the value is true then child of source and target are linked
            based on the criteria. If false then child of source and target is not considered.
            """
    Action: str
    """
            Specifies whether origin link should be established between source and target. Possible
            values are "DryRun" and "Link". If value is "DryRun" then candidates are fetched
            without establishing the origin link. If value is "Link" then the source and target
            are linked based on criteria specified.
            """

class EstablishOriginLinkResponse:
    """
    
The response contains service data and list of source and target candidates that
are linked.
    """
    def __init__(self, ) -> None: ...
    Candidates: list[EstablishOriginLinkCandidates]
    """The source and target objects with their linked state."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData contains partial errors if any."""
    LogFileTicket: Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.FileTicket
    """
            The file ticket containing the UID and file name for the log file generated for this
            command.
            """

class EstablishOriginLinkTargetLinkState:
    """
    
This structure contains the target object and its linked state with the provided
source.
    """
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Target object is either operation of type Mfg0BvrOperation or process of type
            Mfg0BvrProcess.
            """
    LinkState: bool
    """Flag specifying whether target is linked with the provided source."""

class ProcResourceResponseInfo:
    """
    
The response contains a structure of the data related to process resource. The
following
partial errors may be returned:

- 253127 - The information for this object cannot be fetched as the object is
not
in the  context of Plant Bill Of Processes (BOP).

    """
    def __init__(self, ) -> None: ...
    InfoMap: System.Collections.Hashtable
    """
            Map of BOMLine objects (business object/list of business objects).
            
            If the key is process area of type Mfg0BvrProcessArea then value is list of process
            resources of type Mfg0BvrProcessResource that are defined under the process area
            and process/operation of type Mfg0BvrProcess/Mfg0BvrOperation that are unallocated
            to process resource. The value may also contain children of the process area such
            as process line or station.
            

            If the key is process resource of type Mfg0BvrProcessResource then values are process/operation
            of type Mfg0BvrProcess/Mfg0BvrOperation that are allocated to process resource.
            

            If the key is process of type Mfg0BvrProcess then values are process/operation of
            type
            
            Mfg0BvrProcess/Mfg0BvrOperation that are child of that process. These childs are
            process/operation that are unallocated to any process resource. If the process itself
            is allocated to process resource then the value is empty list.
            
"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data containing partial errors."""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddOrRemoveAssociatedContexts(self, Input: list[AddOrRemoveContextsInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def EstablishOriginLink(self, Input: EstablishOriginLinkInfo) -> EstablishOriginLinkResponse: ...
    def GetProcessResourceRelatedInfo(self, Input: list[Teamcenter.Soa.Client.Model.ModelObject], ObjectPreference: str) -> ProcResourceResponseInfo:
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
    def CloneAssemblyAndProcessObjects(self, Input: list[CloneAssemblyInputData]) -> CloneAssemblyResponse:
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

