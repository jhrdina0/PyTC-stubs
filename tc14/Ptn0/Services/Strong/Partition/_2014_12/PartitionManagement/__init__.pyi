import Ptn0.Services.Strong.Partition._2011_06.PartitionManagement
import Ptn0.Services.Strong.Partition._2013_05.PartitionManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetChildrenBulkInputInfo:
    """
    
            Contains an object of ConfigurationContext , list of Parent Ptn0Partition
            object for which child Ptn0Partition objects are to be fetched.  It also represents
            the desired maximum level count and maximum child Ptn0Partition objects that
            have to be fetched.
            
    """
    def __init__(self, ) -> None: ...
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
ConfigurationContext to be used for configuring the output child Ptn0Partition
            objects with the effectivity condition or revision rule attached to it.
            """
    ParentPartitions: list[Teamcenter.Soa.Client.Model.Strong.Ptn0Partition]
    """
            A list of parent Ptn0Partition object for which the children Ptn0Partition
            objects are to be fetched.
            """
    MaxLevelCount: int
    """
            The number of levels of child Ptn0Partition objects that have to be fetched.
            When this count is set to 0, all levels of child Ptn0Partition objects in
            that Partition Breakdown for a given Parent Ptn0Partition objects are returned.
            """
    MaxChildCount: int
    """
            The number of child Ptn0Partition objects to be fetched. When this count is
            set to 0, all child Ptn0Partition objects in that Partition Breakdown for
            a given parent Ptn0Partition objects are returned.
            """

class GetMembersBulkInputInfo:
    """
    
            Contains an object of ConfigurationContext, list of Ptn0Partition objects
            for which members are to be fetched. It also represents content persistence mode
            and a Boolean flag to indicate to load the CAD data or not.
            
    """
    def __init__(self, ) -> None: ...
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
ConfigurationContext to be used for configuring the output members with the
            effectivity condition or revision rule attached to it.
            """
    Partitions: list[Teamcenter.Soa.Client.Model.Strong.Ptn0Partition]
    """A list of Ptn0Partition objects for which the members are to be fetched."""
    ContentPersistenceMode: str
    """
            The content persistence mode. This parameter can be any one of the four following
            values:
            

MODE_STATIC Used when only static members are required.
            
MODE_DYNAMIC Used when only dynamic members are required.
            
MODE_ALL Used when both static and dynamic members are required.
            
MODE_AUTO Used when members are fetched depending on the default persistence
            mode of the Partition.
            
"""
    IsGraphicDataToBeLoaded: bool
    """If true the graphic data such as JT data must be loaded when members are fetched."""

class GetRealizedPartitionsInputData:
    """
    
            Contains the list of PartitionIdentifier objects, an object of ConfigurationContext
            and the list of allowed Mdl0ApplicationModel types to use for filteration.
            
    """
    def __init__(self, ) -> None: ...
    PartitionIdentifiersList: list[PartitionIdentifier]
    """
            Contains the list of PartitionIdentifier objects used to construct the template
            Ptn0Partition objects.
            """
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            An object of ConfigurationContext to be used for configuring the output Ptn0Partition
            objects.
            """
    AllowedAppModelTypesList: list[str]
    """
            List of allowed Mdl0ApplicationModel types. The realized Ptn0Partition
            objects associated with these types will be returned.
            """

class GetRealizedPartitionsResponse:
    """
    
            Contains the list of PartitionMapStruct objects
            encapsulating PtnToPtnsMap object corresponding
            to the list of input PartitionIdentifier
            objects along with the ServiceData. The PtnToPtnsMap
            object has the template Ptn0Partition objects and their corresponding realized
            Ptn0Partition objects.
            
    """
    def __init__(self, ) -> None: ...
    ListPartitionMapStructs: list[PartitionMapStruct]
    """
            The list of PartitionMapStruct objects containing
            the map of template Ptn0Partition objects and their corresponding realized
            Ptn0Partition objects. Only the template Ptn0Partition objects having
            at least one realized Ptn0Partition objects will be returned in the map.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """An object of ServiceData for any error information."""

class PartitionIdentifier:
    """
    
            Contains the information to identify a Ptn0Partition object. The fields are
            the part of the MFK for Ptn0Partition object.
            
    """
    def __init__(self, ) -> None: ...
    PartitionID: str
    """The ID."""
    PartitionSchemeType: str
    """The PartitionScheme type name e.g. Ptn0SchemeFunctional"""
    ModelID: str
    """The Application Model ID of the Partition."""
    ModelType: str
    """The Application Model type name of the Partition e.g. Ptn0PartitionTemplateModel"""

class PartitionMapStruct:
    """
    
            The structure contains the map between template Ptn0Partition objects and
            their corresponding realized Ptn0Partition objects.
            
    """
    def __init__(self, ) -> None: ...
    TemplatePartitionToRealizedPartitionsMap: System.Collections.Hashtable
    """
            Contains the map of template Ptn0Partition objects and corresponding realized
            Ptn0Partition objects.
            """

class PartitionReparentingInputInfo:
    """
    
PartitionReparentingInputInfo structure contains source, target parent Partition,
            list of child Partitions and operation code. The service operation can handle bulk
            reparenting if inputs are supplied in list.
            
    """
    def __init__(self, ) -> None: ...
    TargetParentPartition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """
Partition business object reference to which the members will be updated.
            This is mandatory argument for reparentPartition operation.
            """
    SourceParentPartition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """
Partition business object reference from which the members will be updated.
            This is mandatory argument for reparentPartition operation.
            """
    ChildPartitions: list[Teamcenter.Soa.Client.Model.Strong.Ptn0Partition]
    """
            List of Partition objects to be reparented to target Partition
            object based on the opCode. This is mandatory argument for reparentPartition
            operation.
            """
    OpCode: str
    """
            This is mandatory argument for reparentPartitoin operation. Valid values are
            MOVE_REPARENTING_PARTITION, REPLACE_REPARENTING_PARTITION.
            """

class PartitionManagement:
    """
    Interface PartitionManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ClonePartitions(self, InputVector: list[Ptn0.Services.Strong.Partition._2013_05.PartitionManagement.CreateOrUpdateRealizedPartitionsInputInfo]) -> Ptn0.Services.Strong.Partition._2013_05.PartitionManagement.ClonePartitionsResponse:
        """    
             This operation clones Partition breakdowns (Ptn0Partition) from a source Application
             Model (Mdl0ApplicationModel) to a target Application Model. Source Application
             Model may be a Partition Template (Ptn0PartitionTemplateModel) or Product
             Design (Cpd0CollaborativeDesign) or a Product Architecture Model (Ptn0ProductArchModel).
             The Target Application Model can also be any one of the three i.e. Partition Template,
             Product Design or Product Architecture Model. The operation supports full Partition
             breakdown cloning as well as partial (selective) breakdown cloning. This operation
             can optionally carry forward variant expressions (Fnd0VariantExpression),
             effectivity expressions (Fnd0EffectivityExpression), associated Ptn0PartitionMapping
             objects and attribute groups (Mdl0AttributeGroup) from source partitions to
             target partitions. The operation allows optional filtering out of local Partitions
             (Partitions which are not realized from a template Partition). When both the Source
             Application Model and Target Application Model are not Partition Template, the option
             to copy realization references (Rlz0RealizationMap) to the source template
             Partition is also available. Such Partitions in the target Application Model can
             be updated to reflect the changes from source template Partitions.
             

             When Partition breakdowns are cloned in to an existing scheme in target model, and
             if there are already Partitions present in this scheme with the same Multi Field
             Key attributes then there will be a MFK uniqueness violation error reported for that
             duplicate Partitions, but this error is presented to the user only after saving of
             all non-duplicate Partitions.
             

             Partition breakdowns from a source Application Model can be used as a template to
             create similar Partition breakdowns in target Application Model. After cloning the
             user could re-orient or modify Partition breakdown in the target Application Model.
             Cloned partitions do not maintain any references to source partitions in source Application
             Model. If the option to copy realization references is used, then a strict child
             parent hierarchy of partitions would be enforced in the target Application Model.
             

             Note: createOrUpdateRealizedPartitions operation
             should be used if one wants to strictly maintain the child parent hierarchy of partitions
             in target Application Model while realizing from a Partition Template.
             

Use Cases:

             Users use the Partition breakdowns from an Application Model to create similar Partition
             Schemes (Ptn0PartitionScheme) and Partition breakdowns in other Application
             Models. This can be achieved by cloning Partitions from selected Partition schemes
             of different Application Models or cloning the entire partition breakdown of the
             given source Application Model.
             

             Partition Template
             
             (Functional Scheme)
             
                 |....Partition1
             
                     |....Partition1_1
             
                     |....Partition1_2
             
                     |....Partition1_3
             
                 |....Partition2
             
                     |....Partition2_1
             
                     |....Partition2_2
             
                 |....Partition3
             
                     |....Partition3_1
             

Use case 1: Full Clone: User wants to clone the entire Partition breakdown
             into target Application Model.
             
             Full cloning from the source Partition Template would result in creation of a Functional
             Partition Scheme and identical Partition breakdown in the target Application model.
             

Use case 2: Partial Clone: User wants to clone only selected Partitions from
             the Partition breakdown in the source Application Model into target Application Model.
             
             User will select the Partitions to copy e.g. Partition1_1, Partition1_2 and Partition2_2
             and paste them onto the target Application Model. As the parent hierarchy is maintained,
             the parent Partitions for the selected Partitions i.e. Partition1 and Partition2
             will also be copied into the target Application Model.
             

             Product Architecture Model
             
             (Functional Scheme)
             
                 |....Partition1
             
                     |....Partition1_1 (Source Partition:
             Partition1_1)
             
                     |....Partition1_2 (Source Partition:
             Partition1_2)
             
                     |....Partition1_local (Source Partition:
             None)
             
Use case 3: Full Clone excluding local Partitions: User wants to clone only
             realized Partitions from the Partition breakdown in the source Application Model
             into the target Application Model.
             
             Full cloning from the source Application Model with the "exclude local Partitions"
             option would result in copying of the Partition1, Partition1_1 and Partition1_2 to
             the target Application Model.
             

             Note: This option is applicable only when the source Application Model is either
             a Product Design or a Product Architecture Model.
             

             In all above operations, the user can optionally carry over the variant expressions,
             effectivity expressions, associated Partition mappings and attribute groups optionally
             from source Application Model to target Application Model. They can be modified after
             cloning, if the realization references are not copied along with them.
             

             Variant Expressions are carried forward only when dictionary of options and values
             required for the Variant Expression are available for the target Partition otherwise
             an error message will be thrown.
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param InputVector: 
                         List containing target Application Model, instantiation input options, Revision Rule,
                         Variant Rule and source Application Model or source Partition schemes or source Partitions.
             
        :return: List of Partitions failed to clone, Partition schemes of the failed Partitions, source
             Application Model of the failed Partitions and the corresponding failure detail will
             be returned. Partial errors are returned in ServiceData.
        """
        ...
    def GetChildren(self, Inputs: list[GetChildrenBulkInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetChildrenResponse:
        """    
             This operation gets configured or unconfigured child Ptn0Partition objects
             of the input list of parent Ptn0Partition objects. Desired level of children
             and desired number of children can be fetched by specifying the input parameters
             maximum level of children and maximum number of children respectively.
             

Use Cases:

             User creates a Partition Breakdown with Parent Ptn0Partition objects and child
             Ptn0Partition objects, he can select a single or multiple Ptn0Partition
             object within this breakdown and try to fetch their child Ptn0Partition objects.The
             maximum number of child Ptn0Partition objects and level of child Ptn0Partition
             objects can be given as an optional input. User can get all or desired number of
             configured or un configured children of input Ptn0Partition objects at all
             levels or desired levels in a Partition Breakdown by supplying ConfigurationContext
             object as input.
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Inputs: 
                         List of GetChildrenBulkInputInfo objects containing the details of Parent <b>Ptn0Partition</b>
                         objects, number and level of child <b>Ptn0Partition</b> objects to be fetched. Configured
                         child <b>Ptn0Partition</b> objects can be obtained by specifying the <b>ConfigurationContext</b>
                         object.
             
        :return: objects.
        """
        ...
    def GetMembers(self, Inputs: list[GetMembersBulkInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetMembersResponse:
        """    
             This operation is used to get configured or un configured members of the input Ptn0Partition
             objects. All the members of a single or multiple Ptn0Partition object can
             be fetched using this operation.
             

Use Cases:

             User creates a Partition Breakdown with Ptn0Partition objects and members
             (e.g., Design Components) , user can select a single or multiple Ptn0Partition
             object within this breakdown and try to fetch their members. User can get all configured
             or un configured members of input Ptn0Partition objects by supplying ConfigurationContext
             object as input. Depending on the use case, the user may get the dynamic members
             or static members or both or depending on the default persistence mode of the Ptn0Partition
             object. An additional flag can also be passed as input to load the graphic data that
             is associated with each member.
             

Use case 1:

             User adds members to a static Ptn0Partition object, system creates Membership
             links to this Ptn0Partition object. These members can be fetched by specifying
             the content persistence mode input argument as MODE_STATIC.
             

Use case 2:

             User adds members to a Ptn0Partition object dynamically, system updates recipe
             on Ptn0Partition object. System will not create any persistent Membership
             links when Ptn0Partition objects are updated dynamically. These dynamic members
             can be fetched by executing the recipe, by specifying the content persistence mode
             input argument as MODE_DYNAMIC.
             

Use case 3:

             Users can add members to Ptn0Partition objects statically by creating Memberships
             and dynamically by creating the search recipe. Both these static members and dynamic
             members can be fetched by specifying the content persistence mode input argument
             as MODE_ALL.
             

Use case 4:

             Users can add members to Ptn0Partition objects statically by creating Memberships
             and also dynamically by creating search recipe. The members can be fetched depending
             on the default persistence mode of the Ptn0Partition object also i.e., if
             Partition is a dynamic Partition like a Spatial Partition, then user can get dynamic
             members and if its a static Partition like a Functional Partition, then user can
             fetch static members by specifying the content persistence mode input argument as
             MODE_AUTO.
             


Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Inputs: 
                         List of GetMembersBulkInputInfo object containing the <b>ConfigurationContext</b>,
                         list of <b>Ptn0Partition</b> object, content persistence mode and a flag to load
                         the graphics data.
             
        :return: objects along with their members are returned.
        """
        ...
    def GetRealizedPartitions(self, OperationInput: list[GetRealizedPartitionsInputData]) -> GetRealizedPartitionsResponse:
        """    
             This operation fetches configured Ptn0Partition objects across the specified
             types of partition breakdowns (Ptn0ProductArchModel and Cpd0CollaborativeDesign)
             that have been realized from a given input set of Ptn0Partition objects in
             a Partition Template (Ptn0PartitionTemplateModel). The types of partition
             breakdowns to select is specified as an input to this operation.
             
             The Inactive Ptn0Partition objects in the partition breakdown may additionally
             be filtered out.
             


Use Cases:

             Users use the Ptn0Partition objects from a generic Partition Template hierarchy
             (e.g. vehicle architecture) to locate their corresponding realized Ptn0Partition
             objects in the derived (product specific) Partition Breakdown hierarchy. The template
             Ptn0Partition objects are identified based on the PartitionIdentifier
             input object.
             

Use case 1: A template Partition is realized into the Partition breakdowns
             under two Application Models. Both the Application Models are Ptn0ProductArchModel
             objects. The allowedAppModelTypesList contains
             Ptn0ProductArchModel.
             
             In this case, a map containing a single row of the template Partition reference and
             the two realized Partition references will be returned.
             

Use case 2: Two different revisions of the template Partition are realized
             into the Partition breakdowns under two Application Models. Both the Application
             Models are Ptn0ProductArchModel objects. The allowedAppModelTypesList
             contains Ptn0ProductArchModel.
             
             In this case, a map containing two rows will be returned. Each row would contain
             one revision of the template Partition reference and the corresponding realized Partition
             reference.
             

Use case 3: A template Partition is realized into the Partition breakdowns
             under two Application Models. One of the Application Models is Ptn0ProductArchModel
             object and the other is Cpd0CollaborativeDesign object. The allowedAppModelTypesList contains Ptn0ProductArchModel.
             
             In this case, a map containing a single row of the template Partition reference and
             the realized Partition reference in the Partition Breakdown under Ptn0ProductArchModel
             will be returned.
             

Use case 4: A template Partition is realized into the Partition breakdowns
             under two Application Models. One of the realized Partition has a Release status
             associated with it. The other realized Partition is in Working state. Both the Application
             Models are Ptn0ProductArchModel objects. The allowedAppModelTypesList contains
             Ptn0ProductArchModel. The ConfigurationContext
             is provided as "Any Status; No Working".
             
             In this case, a map containing a single row of the template Partition reference and
             the realized Partition reference to the Partition with Release status will be returned.
             The Working Partition will not be configured.
             

Use case 5: In the cases where either the template Partition is not realized
             into any Partition Breakdowns, or invalid template Partition input, no specific error
             will be thrown. Instead, an empty map will be returned, indicating that there are
             no realized Partitions available for the input provided.
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param OperationInput: 
                         A vector of <font face="courier" height="10">GetRealizedPartitionsInputData</font>
                         objects, each containing the list of <font face="courier" height="10">PartitionIdentier</font>
                         objects, <b>ConfigurationContext</b> object and the allowed <b>Mdl0ApplicationModel</b>
                         type names.
             
        :return: 
        """
        ...
    def ReparentPartition(self, Inputs: list[PartitionReparentingInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.UpdateMembersResponse:
        """    
             This operation moves child Partition(s) from source parent Partition or top level
             Partition to target parent Partition. Successful execution of this operation will
             remove input childPartitions from existing sourceParentPartition and add them under
             targetParentPartition.
             


childPartitions: These are the Partition (Ptn0Partition) selected
             for reparent operation.
             
sourceParentPartition: Partition whose one or more children are selected
             for reparent operation.
             
targetParentPartition: Selected childPartitions will be moved under
             this Partition.
             



             This operation updates the targetParentPartition with the supplied childPartitions.
             User performing drag and drop operation needs following privileges on Partition,
             Model (Mdl0ApplicationModel)
             

ADD_CONTENT
             
REMOVE_CONTENT
             



Use Cases:

             User may want to reparent Partition to organize them in hierarchical structure. This
             could be done by using drag and drop functionality. User may select single / multiple
             child Partitions and drop them to target Partition. User can select child Partition(s)
             present under same / different parent Partition.
             

             Product Design
             
             |....Partition1
             
             |....Partition1_1
             
             |....Partition1_2
             
             |....Partition1_3
             
             |....Partition_common
             
             |....Partition_common_1
             
             |....Partition2
             
             |....Partition2_1
             
             |....Partition2_2
             
             |....Partition_common
             
             |....Partition_common_1
             
             |....Partition3
             
             |....Partition3_1
             

Use Case 1: Reparent single child Partition
             
             User may want to reparent child Partition1_1 present under Partition1 to target Partition3.
             

Use Case 2: Reparent multiple child Partitions present under
             same source parent Partition
             
             User may want to reparent child Partition1_1, Partition1_2 present under Partition1
             to target Partition3.
             

Use Case 3: Reparent multiple child Partitions present under
             different source parent Partitions
             
             User may want to reparent child Partition1_1, Partition2_1 present under different
             parent Partition1, Partition2 to target Partition3.
             

Use Case 4: Reparent multiple child Partitions present under
             different source parent Partitions
             
             User may want to reparent child Partition_common which is present under different
             parent Partitions Partition1, Partition2 to target Partition3.
             



Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Inputs: 
<ul>
<li type="disc">targetParentPartition
                         </li>
<li type="disc">sourceParentPartition
                         </li>
<li type="disc">childPartitions
                         </li>
<li type="disc">opCode
                         </li>
</ul>

        :return: The exception occurred during the operation are returned in ServiceData.It also returns
             failed member and corresponding error related to that failed member.
        """
        ...

