import Ptn0.Services.Strong.Partition._2011_06.PartitionManagement
import Ptn0.Services.Strong.Partition._2011_06.Search
import Ptn0.Services.Strong.Partition._2012_09.Search
import Ptn0.Services.Strong.Partition._2013_05.PartitionManagement
import Ptn0.Services.Strong.Partition._2014_12.PartitionManagement
import Ptn0.Services.Strong.Partition._2015_10.PartitionManagement
import Ptn0.Services.Strong.Partition._2018_06.PartitionManagement
import Ptn0.Services.Strong.Partition._2018_11.Search
import Ptn0.Services.Strong.Partition._2019_06.Search
import Ptn0.Services.Strong.Partition._2020_12.PartitionManagement
import Ptn0.Services.Strong.Partition._2021_06.PartitionManagement
import Ptn0.Services.Strong.Partition._2021_12.PartitionManagement
import Ptn0.Services.Strong.Partition._2023_06.PartitionManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class PartitionManagementRestBindingStub(PartitionManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    @typing.overload
    def GetChildren(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetChildrenInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetChildrenResponse: ...
    @typing.overload
    def GetChildren(self, Inputs: list[Ptn0.Services.Strong.Partition._2014_12.PartitionManagement.GetChildrenBulkInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetChildrenResponse: ...
    @typing.overload
    def GetMembers(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetMembersInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetMembersResponse: ...
    @typing.overload
    def GetMembers(self, Inputs: list[Ptn0.Services.Strong.Partition._2014_12.PartitionManagement.GetMembersBulkInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetMembersResponse: ...
    @typing.overload
    def GetParents(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetParentsInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetParentsResponse: ...
    @typing.overload
    def GetParents(self, Inputs: list[Ptn0.Services.Strong.Partition._2018_06.PartitionManagement.GetParentBulkInputInfo]) -> Ptn0.Services.Strong.Partition._2018_06.PartitionManagement.GetParentsBulkResponse: ...
    def GetPartitions(self, Input: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetPartitionsInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetPartitionsResponse: ...
    def GetSchemesInModel(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetSchemesInModelResponse: ...
    def GetTopLevelPartitions(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetTopLevelPartitionsInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetTopLevelPartitionsResponse: ...
    def PersistDynamicMembers(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.PersistDynamicMembersInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UpdateChildrenOrParents(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.UpdateChildrenOrParentsInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UpdateMembers(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.UpdateMembersInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.UpdateMembersResponse: ...
    def WherePartitioned(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.WherePartitionedInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.WherePartitionedResponse: ...
    @typing.overload
    def ClonePartitions(self, Inputs: list[Ptn0.Services.Strong.Partition._2013_05.PartitionManagement.ClonePartitionsInputInfo]) -> Ptn0.Services.Strong.Partition._2013_05.PartitionManagement.ClonePartitionsResponse: ...
    @typing.overload
    def ClonePartitions(self, InputVector: list[Ptn0.Services.Strong.Partition._2013_05.PartitionManagement.CreateOrUpdateRealizedPartitionsInputInfo]) -> Ptn0.Services.Strong.Partition._2013_05.PartitionManagement.ClonePartitionsResponse: ...
    def CreateOrUpdateRealizedPartitions(self, Inputs: list[Ptn0.Services.Strong.Partition._2013_05.PartitionManagement.CreateOrUpdateRealizedPartitionsInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetRealizedPartitions(self, OperationInput: list[Ptn0.Services.Strong.Partition._2014_12.PartitionManagement.GetRealizedPartitionsInputData]) -> Ptn0.Services.Strong.Partition._2014_12.PartitionManagement.GetRealizedPartitionsResponse: ...
    def ReparentPartition(self, Inputs: list[Ptn0.Services.Strong.Partition._2014_12.PartitionManagement.PartitionReparentingInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.UpdateMembersResponse: ...
    def GetMappedPartitions(self, OperationInput: list[Ptn0.Services.Strong.Partition._2015_10.PartitionManagement.GetMappedPartitionsInputData]) -> Ptn0.Services.Strong.Partition._2015_10.PartitionManagement.GetMappedPartitionsResponse: ...
    def GetOwningPartitions(self, OperationInput: list[Ptn0.Services.Strong.Partition._2015_10.PartitionManagement.GetOwningPartitionsInputData]) -> Ptn0.Services.Strong.Partition._2015_10.PartitionManagement.GetOwningPartitionsResponse: ...
    def UnmapPartitions(self, OperationInput: list[Ptn0.Services.Strong.Partition._2015_10.PartitionManagement.UnmapPartitionsInputData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def WherePartitioned2(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.WherePartitionedInputInfo]) -> Ptn0.Services.Strong.Partition._2018_06.PartitionManagement.WherePartitionedResponse2: ...
    def GetMembersInBOMWindow(self, Inputs: list[Ptn0.Services.Strong.Partition._2020_12.PartitionManagement.GetMembersInBOMWindowBulkInputInfo]) -> Ptn0.Services.Strong.Partition._2020_12.PartitionManagement.GetMembersInBOMWindowResponse: ...
    def GetPartitionsForBOMLine(self, Inputs: list[Ptn0.Services.Strong.Partition._2020_12.PartitionManagement.GetPartitionsForBOMLineIpInfo]) -> Ptn0.Services.Strong.Partition._2020_12.PartitionManagement.GetPartitionsForBOMLineResponse: ...
    def GetSchemesInBOMView(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.PSBOMView]) -> Ptn0.Services.Strong.Partition._2020_12.PartitionManagement.GetSchemesInBOMViewResponse: ...
    def GetTopLevelPartitionsInBOMView(self, Inputs: list[Ptn0.Services.Strong.Partition._2020_12.PartitionManagement.GetTopLevelPtnsInBOMViewInputInfo]) -> Ptn0.Services.Strong.Partition._2020_12.PartitionManagement.GetTopLevelPtnsInBOMViewResponse: ...
    def GetAllChildPtnInAppModel(self, Inputs: list[Ptn0.Services.Strong.Partition._2021_06.PartitionManagement.GetAllChildPtnInAppModelInInfo]) -> Ptn0.Services.Strong.Partition._2021_06.PartitionManagement.GetAllChildPtnInAppModelResponse: ...
    def GetNextChildPtnInAppModel(self, Inputs: list[Ptn0.Services.Strong.Partition._2021_06.PartitionManagement.GetNextChildPtnInAppModelInInfo]) -> Ptn0.Services.Strong.Partition._2021_06.PartitionManagement.GetNextChildPtnInAppModelResponse: ...
    def StopGetChildren(self, Cursor: Ptn0.Services.Strong.Partition._2021_06.PartitionManagement.FetchNextChildrenCursor) -> Ptn0.Services.Strong.Partition._2021_06.PartitionManagement.StopGetChildrenResponse: ...
    def IsPartitionable(self, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision, BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView, IsPartitionableInputInfo: list[Ptn0.Services.Strong.Partition._2021_12.PartitionManagement.IsPartitionableInputInfo]) -> Ptn0.Services.Strong.Partition._2021_12.PartitionManagement.IsPartitionableResponse: ...
    def UpdateMembersInBOMWindow(self, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision, BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView, UpdateMembersInBOMWindowInputInfo: list[Ptn0.Services.Strong.Partition._2021_12.PartitionManagement.UpdateMembersInBOMWindowInputInfo]) -> Ptn0.Services.Strong.Partition._2021_12.PartitionManagement.UpdateMembersInBOMWindowResponse: ...
    def GetMembersInBOMWindow2(self, Input: list[Ptn0.Services.Strong.Partition._2023_06.PartitionManagement.GetMembersInBOMWindowBulkInputInfo2]) -> Ptn0.Services.Strong.Partition._2023_06.PartitionManagement.GetMembersInBOMWindowResponse2: ...

class PartitionManagementService:
    """
    
            This service exposes operations related to partitions in Teamcenter.  Partitions
            logically organize large sets of design components into a hierarchy that permits
            the CAD users to easily find their assigned data. Customers can represent functional
            divisions of the product (for example, propulsion systems or avionics), or they can
            represent physical divisions (for example, engine room or electronics bay). The nodes
            in a physical partition breakdown represent placeholders that may be populated
            by actual product content obtained from part releasing systems, CAD systems, or manufacturing
            planning systems.
            
            Partitions can be added to other partitions, typically to build a default
            manufacturing process. For example, you can paste partition P1 into partition
            P2, where the content of partition P1 represents a set of expected components
            and the containing partition P2 represents a generic manufacturing process
            step. Pasting the generic physical partition P1 into the generic process partition
            P2 implies that the components will be attached to P1 with the manufacturing
            process represented by P2.
            

            Partitions can be organized hierarchically into breakdowns. Partitions reference
            a scheme that defines constraints for the partitions in this scheme, for example,
            the list of partition types that you can arrange into a partition breakdown in
            this scheme. The nodes in a physical partition breakdown represent placeholders
            that may be populated by actual product content obtained from part releasing systems,CAD
            systems or manufacturing planning systems. These hierarchies are built using child
            parent links, where the child chooses the parent.
            


Library Reference:

Ptn0SoaPartitionStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> PartitionManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    @typing.overload
    def GetChildren(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetChildrenInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetChildrenResponse: ...
    @typing.overload
    def GetChildren(self, Inputs: list[Ptn0.Services.Strong.Partition._2014_12.PartitionManagement.GetChildrenBulkInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetChildrenResponse: ...
    @typing.overload
    def GetMembers(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetMembersInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetMembersResponse: ...
    @typing.overload
    def GetMembers(self, Inputs: list[Ptn0.Services.Strong.Partition._2014_12.PartitionManagement.GetMembersBulkInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetMembersResponse: ...
    @typing.overload
    def GetParents(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetParentsInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetParentsResponse: ...
    @typing.overload
    def GetParents(self, Inputs: list[Ptn0.Services.Strong.Partition._2018_06.PartitionManagement.GetParentBulkInputInfo]) -> Ptn0.Services.Strong.Partition._2018_06.PartitionManagement.GetParentsBulkResponse: ...
    def GetPartitions(self, Input: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetPartitionsInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetPartitionsResponse:
        """    
getPartitions SOA operation is
             used for getting all the Partitions from the Partition Scheme and Application Model
             given by user. User can limit the number of Partitions in output by giving maxpartitionCount in GetPartitionsInputInfo
             input structure.
             

Use Cases:

             Use Case 1: Get All partitions from Application Model and Partition Scheme.
             
             User can give Partition scheme and application model to find out partition lying
             under it.
             
             User has following structure created.
             
             To get Partitions under the Partition Scheme and Application Model execute the getPartitions SOA.
             
             ModelA
             
                 |
             
                 SchemeA
             
                     |_Partition1
             
                     |_Partition2
             
                     |_Partition3
             

             After performing SOA operation with ModelA and SchemeA as input it returns Partition1,
             Partition2 and Partition3 as output, provided maxPartitionCount
             is set to 0 which mean all the results will be returned without truncating partition
             list.
             

             Use Case 2: Get N Number of partition from Application Model and Scheme.
             
             Consider structure in use case 1 but the only the difference is maxPartitionCount set to 2 in this case. So performing same operation
             as above with this maxPartitionCount truncates
             output result and gives only Partition1 and Partition2 in output.
             



Dependencies:

             createObjects
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Input: 
                         Vector of the structure <font face="courier" height="10">GetPartitionsInputInfo</font>.
             
        :return: 
        """
        ...
    def GetSchemesInModel(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetSchemesInModelResponse:
        """    
             This operation is used to get all the Partition Schemes which are defined
             under specified Application Model. Application Model object is provided as
             the input parameter for this SOA.
             

Use Cases:

             User creates multiple Partition Schemes under the Application
             Model.


             Application Model (Model A)
             
                         | _ _ Partition
             Scheme A

                         |
             _ _ Partition Scheme B



             To getSchemesInModel SOA user gives ModelA as input and SOA will return the list
             containing values Partition Scheme A and Partition Scheme B.



Dependencies:

             createObjects
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Inputs: 
                         Application Model object is supplied as input to SOA.
             
        :return: 
        """
        ...
    def GetTopLevelPartitions(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetTopLevelPartitionsInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.GetTopLevelPartitionsResponse:
        """    
             This operation can be used to fetch top level partitions(Ptn0Partition) for
             a Partition Schemes(Ptn0PartitionScheme) within an Application Model
             e.g., a Product Design (Cpd0CollaborativeDesign). This operation can be used
             to get top level Partitions in bulk from multiple Partition Schemes in multiple Application
             Models. Top level Partitions in a Partition scheme are the Partitions which are not
             children of any other Partitions. Hence, there can be more than one top level Partition
             in a scheme.
             

Use Cases:

Use Case :  Get Top Level Partitions in a Partition Scheme

             In CPD Application, users can create Partition Breakdowns in a partition scheme
             and may want to browse through this breakdown from top to down. In such cases, user
             may start with top level Partition in a scheme and then can browse through its children.
             

             Users can query for all the top level Partitions in a set of Partition Schemes within
             corresponding  Application Models by specifying both the Partition Schemes and their
             Application models as input parameters. Based on input Configuration Context , Configured
             top level partitions are returned in response and a NULL Configuration Context
returns unconfigured  top level Partitions.
             


Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Inputs: 
                         Vector of Structures containing the details of  Partition scheme and  Application
                         model
             
        :return: .
        """
        ...
    def PersistDynamicMembers(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.PersistDynamicMembersInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service operation is used to create the snapshot of the members which are attached
             to the input Partition dynamically. Inputs Partition and configuration context, are
             used to get all the existing Members  of Partition. The members which are added in
             dynamic mode are persisted by creating static Membership objects for them.
             

Use Cases:

             Use Case : Persist Dynamic Members of input partition.
             

Create Collaborative design in given
             application model.
             
Create Partition Scheme and configuration context in above
             product design.
             
Create Partition and Design Components in Partition Scheme and product
             design
             


                       respectively.
             

Update Partition with Members in dynamic mode by updating recipe.
             
Call persist dynamic SOA using above Partition and configuration
             context
             


                       This use case will execute in following
             sequence, to persist the dynamic members of given partition.
             
                                 1.
             Use input Partition and the configuration context to get all the existing memberships
             for this Partition.
             
                                 2.
             Delete all the memberships got from step no. 1.
             
                                 3.
             Get dynamic members for input Partition.
             
                                 4.
             Create static memberships in bulk for all the dynamic members (from step 3) to
             input Partition.
             


This will convert all the dynamic members in static ones by creating
             a static Membership for all members updated in dynamic mode.
             



             All the dynamic Members of input Partition are now static after creating membership
             objects in database.
             

Dependencies:

             createObjects
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Inputs: 
                         Partition whose dynamic members need to be persisted as static memberships with isFromRecipe
                         set to TRUE.
             
        :return: If user does not have the required access privileges for performing operation it
             will return error.
        """
        ...
    def UpdateChildrenOrParents(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.UpdateChildrenOrParentsInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation updates the given input Partition with the supplied input Partitions
             list. Partitions can be added as children or parents for a given input Partition.
             
             User performing this operation need update privileges ( ADD_CONTENT/ REMOVE_CONTENT
             ) on Partitions or Model.
             


Use Cases:

Update Parents/Children to Partitions

             To organize the design components, user may want to partition these design components.
             In doing so, the Partitions can also be arranged in a hierarchies. This could be
             done by adding children to a given partition or parent Partitions can be added for
             an existing partition. User can also modify an existing Partition breakdown by removing/
             replacing existing child or parent partitions.
             


Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Inputs: 
                         Object of UpdateChildrenOrParentsInputInfo structure.
             
        :return: The exception occurred during the operation are returned in ServiceData
        """
        ...
    def UpdateMembers(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.UpdateMembersInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.UpdateMembersResponse:
        """    
             This operation updates the given input Partition with the Members supplied in a members
             list. Members can be added/removed/replaced for a given  Partition.
             
             User performing this operation needs privileges on partition or members as ADD/REMOVE_CONTENT
             or WRITE respectively, depending upon ownership of Membership object. If user does
             not have required privileges or any of the validation fails it returns error in serviceData along with failed members and error
             code for each failed member in UpdateMemberRespose
             structure.
             


Use Cases:

             Use Case 1: Add members to Partition


             User can add members to the partition as follows.
             
             1.    Creates the Product Design in a given application model.
             
             2.    Creates Partition Scheme under the product design created
             in step1.
             
             3.    Creates Partition under Partition Scheme created in step2.
             
             4.    Creates Design Components directly under Partition created
             in step3.
             
             5.    User can also configure the revision rule while performing
             this operation and this rule will be passed to the SOA.
             

             Operation code ADD will be used for this use case, user can define the way
             memberships will be created in data base by selecting proper predefined value in
             contentPersistenceMode parameter. That is
             STATIC / DYNAMIC /AUTO /ALL_MODE.
             

             Use Case 2: Replace members of the input partition list

             Members of the existing Partition can be replaced with the new set of input members
             list as follows.
             
             1.    User has Partition and Design Components under it as created
             in use case 1.
             
             2.    Now Design Component under the Partition need to be replaced
             with different Design Components.
             
             3.    User selects set of new design components and paste it
             under the existing partition.
             
             4.    This operation will remove all the existing design components
             from the partition and replace with new design components.
             
             5.    User can also configure the revision rule and pass it to
             this SOA.
             
             Operation code REPLACE will be used for this use case, user can define the
             way new membership objects will be created in database using contentPersistenceMode parameter. That is user can select any
             of the modes from STATIC/ DYNAMIC/ AUTO/ ALL_MODE.
             

             Use Case 3: Remove members of the input partition list

             Members of the existing Partition can be removed with the set of input members list.
             
             1.    User has created Partition with few design components under
             it same as use case1.
             
             2.    Design Components are selected and deleted.
             
             3.    This operation will remove the links between Partition
             and Design Components by deleting  membership object or recipe.
             
             Operation code REMOVE will be used in this use case.
             


Dependencies:

             createObjects
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Inputs: 
<ul>
<li type="disc"><font face="courier" height="10">inputPartition</font>
</li>
<li type="disc"><font face="courier" height="10">membersList</font>
</li>
<li type="disc"><font face="courier" height="10">opCode</font>
</li>
<li type="disc"><font face="courier" height="10">contentPersistenceMode</font>
</li>
<li type="disc"><font face="courier" height="10">configurationContext</font>
</li>
</ul>

        :return: .It also returns failed member and corresponding error
             related to that failed member.
        """
        ...
    def WherePartitioned(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.WherePartitionedInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.WherePartitionedResponse:
        """    
             This operation is used to find the Partitions related to the given input Partitionable.
             Operation performs a search on Membership object to find if any Partitions are attached
             to input partitionable.It also requires  Application model object and Partition Scheme
             object to limit the search scope within specified Application model and partition
             scheme.
             


Use Cases:

             Find partition for a member in given application model and partition scheme.


User creates Partition scheme as SchemeA and ModelA as application
             model.
             
Partition1 is created under SchemeA and ModelA.
             
User has a Design Component Member1 as a partitionable under Partition1(it
             creates   membership object)
             


             Execute wherePartitioned SOA with following details for above use case.
             
                   WherePartitionedInputInfo.configurationContext = Revision
             rule.
             
                   WherePartitionedInputInfo.modelContext = ModelA.
             
                   WherePartitionedInputInfo.partitionScheme = SchemeA.
             
                   WherePartitionedInputInfo.partitionable = Member1.
             

             After executing SOA with above details output will contain Partition1 and Member1
             partitionable object.
             

Dependencies:

             createObjects
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Inputs: 
                         Vector of a structure <font face="courier" height="10">WherePartitionedInputInfo</font>
                         containing input application model, partition scheme, partition, revision rule and
                         partitionable object.
             
        :return: 
        """
        ...
    @typing.overload
    def ClonePartitions(self, Inputs: list[Ptn0.Services.Strong.Partition._2013_05.PartitionManagement.ClonePartitionsInputInfo]) -> Ptn0.Services.Strong.Partition._2013_05.PartitionManagement.ClonePartitionsResponse: ...
    @typing.overload
    def ClonePartitions(self, InputVector: list[Ptn0.Services.Strong.Partition._2013_05.PartitionManagement.CreateOrUpdateRealizedPartitionsInputInfo]) -> Ptn0.Services.Strong.Partition._2013_05.PartitionManagement.ClonePartitionsResponse: ...
    def CreateOrUpdateRealizedPartitions(self, Inputs: list[Ptn0.Services.Strong.Partition._2013_05.PartitionManagement.CreateOrUpdateRealizedPartitionsInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation realizes partition breakdowns (Ptn0Partition) from Partition
             Template (Ptn0PartitionTemplateModel) to a target Application Model (Mdl0ApplicationModel)
             and updates partition breakdowns from source Partition Templates. This operation
             can optionally carry forward variant expressions (Fnd0VariantExpression),
             effectivity expressions (Fnd0EffectivityExpression), attribute groups (Mdl0AttributeGroup)
             and child Partitions from source Application Model to target Application Model. Realized
             partitions in the target Application Model can be updated to reflect the changes
             from source partitions. During this operation realization/update of realized Partitions
             the associated mappings are carried forward from source Applciation Model to target
             Application Model.
             

             Instantiated or realized partition breakdowns maintains reference to source partitions
             in Partition Template. User can add a new partition to realized partition structure
             in target application model. However, deleting an instantiated partition after realization
             is allowed in target application model. Realization of a Partition maintains a strict
             child parent hierarchy and will be same as that of its source Partition parent hierarchy.
             Realization of Partition also maintains the mappings relationships and will be same
             as that of its source Partition in parent hierarchy. During update of realized partitions
             Child-parent links and Partition mappings are automatically established in target
             application model wherever possible. Duplicate partitions will not be created during
             update of realized partitions. But the partitions are updated with Variant conditions
             and other related objects (based on Deep copy rules) from the source Partition Template
             to the target application model.
             

             Note: clonePartitions operation should be
             used if one wants to modify the child parent hierarchy of partitions in target Application
             Model.
             

Use Cases:


             Use Case1:
             
             Partition Templates can be used as blue print which can be reused to create partition
             breakdowns in other Application Models (Product Design (Cpd0CollaborativeDesign)
             or Partition Template (Ptn0PartitionTemplateModel)). This enables users to
             reuse Partition Templates and create similar Partition schemes (Ptn0PartitionScheme)
             and partition breakdowns in other Application Models.  This can be done by copy/pasting
             or drag/drop of Partitions from Partition Template to another Application Model in
             RAC. The user may also want to optionally carry over the child Partitions, variant
             expressions, and effectivity expressions and attribute groups.
             

             Variant Expressions are carried forward only when dictionary of options and values
             required for the Variant Expression are available for the target Partition otherwise
             an error message will be thrown.
             

             Use case2:
             
             Once Partitions are realized from a Partition Template to other Application Model,
             Partitions in source Partition Template may undergo changes and user may want to
             bring these updates from Partition Template in to the target model.
             


Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Inputs: 
                         List containing target Application Model, instantiation input options, Revision Rule,
                         Variant Rule and source Application Model or source Partition schemes or source Partitions.
             
        :return: Partial errors are returned in ServiceData when the operation failed to update given
             partitions.
        """
        ...
    def GetRealizedPartitions(self, OperationInput: list[Ptn0.Services.Strong.Partition._2014_12.PartitionManagement.GetRealizedPartitionsInputData]) -> Ptn0.Services.Strong.Partition._2014_12.PartitionManagement.GetRealizedPartitionsResponse:
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
    def ReparentPartition(self, Inputs: list[Ptn0.Services.Strong.Partition._2014_12.PartitionManagement.PartitionReparentingInputInfo]) -> Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.UpdateMembersResponse:
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
    def GetMappedPartitions(self, OperationInput: list[Ptn0.Services.Strong.Partition._2015_10.PartitionManagement.GetMappedPartitionsInputData]) -> Ptn0.Services.Strong.Partition._2015_10.PartitionManagement.GetMappedPartitionsResponse:
        """    
             This operation returns configured mapped Ptn0Partition objects within an Mdl0ApplicationModel.
             Optionally Ptn0Partition objects belonging to specific schemes and child of
             mapped Partitions can be returned.
             

Use Cases:

             User maps Ptn0Partition objects belonging to different Ptn0PartitionScheme
             objects under an Application Model.
             

             Partition Breakdown
             
             ApplicationModel
             
             --------|-------FunctionalScheme
             
             --------------------------|------------------FunctPtn1
             
             --------------------------|------------------FunctPtn2
             
             --------------------------|------------------FunctPtn3
             
             --------|-------PhysicalScheme
             
             --------------------------|------------------PhyPtn1
             
             --------------------------------------------------|------------------PhyPtn3
             
             --------------------------|------------------PhyPtn2
             
             --------|-------SpatialScheme
             
             --------------------------|------------------SpatPtn1
             

             Mapped Partition Details
             
             OwningPartition-------------TargetPartition
             
             FunctPtn1------MappedTo-----PhyPtn1
             
             FunctPtn1------MappedTo-----PhyPtn2
             
             FunctPtn1------MappedTo-----SpatPtn1
             

Use Case 1: Get all mapped Partitions
             
             FunctPtn1 is passed to get mapped Partitions, the operation returns PhyPtn1, PhyPtn2
             and SpatPtn1.
             

Use Case 2: Get mapped Partitions from specified Partition scheme
             
             FunctPtn1 along with SpatialScheme is passed to get mapped Partitions, the operation
             returns SpatPtn1.
             

Use Case 3: Get all mapped Partitions along with their child Partitions
             
             FunctPtn1 is passed to get mapped Partitions along with input option "includeChildPartitions" as true, the operation returns PhyPtn1,
             PhyPtn3, PhyPtn2 and SpatPtn1.
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param OperationInput: 
                         A list of <font face="courier" height="10">GetMappedPartitionsInputData</font> objects,
                         each containing the list of <b>Ptn0Partition</b> objects, list of <b>Ptn0PartitionScheme</b>
                         objects, input options, <b>ConfigurationContext</b> object and the <b>Mdl0ApplicationModel</b>
                         object.
             
        :return: 
        """
        ...
    def GetOwningPartitions(self, OperationInput: list[Ptn0.Services.Strong.Partition._2015_10.PartitionManagement.GetOwningPartitionsInputData]) -> Ptn0.Services.Strong.Partition._2015_10.PartitionManagement.GetOwningPartitionsResponse:
        """    
             This operation returns configured owning Ptn0Partition objects within an Mdl0ApplicationModel.
             Owning Ptn0Partition objects are the objects from where the mapping operation
             was initiated.
             

Use Cases:

             User maps Ptn0Partition objects belonging to different Ptn0PartitionScheme
             objects under an Application Model.
             

             Partition Breakdown
             
             ApplicationModel
             
             --------|-------FunctionalScheme
             
             --------------------------|------------------FunctPtn1
             
             --------------------------|------------------FunctPtn2
             
             --------------------------|------------------FunctPtn3
             
             --------|-------PhysicalScheme
             
             --------------------------|------------------PhyPtn1
             
             --------------------------------------------------|------------------PhyPtn3
             
             --------------------------|------------------PhyPtn2
             
             --------|-------SpatialScheme
             
             --------------------------|------------------SpatPtn1
             

             Mapped Partition Details
             
             OwningPartition----------------TargetPartition
             
             FunctPtn1------MappedTo-----PhyPtn1
             
             FunctPtn2------MappedTo-----PhyPtn1
             
             FunctPtn1------MappedTo-----SpatPtn1
             

Use Case 1: Get all owning Partitions
             
             PhyPtn1 is passed to get owning Partitions, the operation returns FunctPtn1 and FunctPtn2.
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param OperationInput: 
                         A list of <font face="courier" height="10">GetOwningPartitionsInputData</font> objects,
                         each containing the list of <b>Ptn0Partition</b> objects, <b>ConfigurationContext</b>
                         object and the <b>Mdl0ApplicationModel</b> object.
             
        :return: 
        """
        ...
    def UnmapPartitions(self, OperationInput: list[Ptn0.Services.Strong.Partition._2015_10.PartitionManagement.UnmapPartitionsInputData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation unmaps given target Ptn0Partition objects from given owning
             Ptn0Partition objects under an Mdl0ApplicationModel.
             

Use Cases:

             User maps Ptn0Partition objects belonging to different Ptn0PartitionScheme
             objects under an Application Model.
             

             Partition Breakdown
             
             ApplicationModel
             
             --------|-------FunctionalScheme
             
             --------------------------|------------------FunctPtn1
             
             --------------------------|------------------FunctPtn2
             
             --------------------------|------------------FunctPtn3
             
             --------|-------PhysicalScheme
             
             --------------------------|------------------PhyPtn1
             
             --------------------------------------------------|------------------PhyPtn3
             
             --------------------------|------------------PhyPtn2
             
             --------|-------SpatialScheme
             
             --------------------------|------------------SpatPtn1
             

             Mapped Partition Details
             
             OwningPartition----------------TargetPartition
             
             FunctPtn1------MappedTo-----PhyPtn1
             
             FunctPtn2------MappedTo-----PhyPtn2
             
             FunctPtn1------MappedTo-----SpatPtn1
             

Use Case 1: Unmap Partitions for given input pair of owning and target Partitions.
             
             For the input owning Partitions (FunctPtn1, FunctPtn2) and target Partitions (PhyPtn1,
             PhyPtn2), the operation will unmap PhyPtn1 from FunctPtn1 and PhyPtn2 from FunctPtn2.
             

Use Case 2: Unmap Partitions for given input pair of owning and target Partitions
             where multiple target Partitions are mapped to same owning Partition.
             
             For the input owning Partitions (FunctPtn1, FunctPtn1) and target Partitions (PhyPtn1,SpatPtn1),
             the operation will unmap PhyPtn1 from FunctPtn1 and SpatPtn1 from FunctPtn1.
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param OperationInput: 
                         A list of <font face="courier" height="10">UnmapPartitionsInputData</font> objects,
                         each containing the list of owning <b>Ptn0Partition</b> objects, list of target <b>Ptn0Partition</b>
                         objects and the <b>Mdl0ApplicationModel</b> object.
             
        :return: 
        """
        ...
    def WherePartitioned2(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.WherePartitionedInputInfo]) -> Ptn0.Services.Strong.Partition._2018_06.PartitionManagement.WherePartitionedResponse2: ...
    def GetMembersInBOMWindow(self, Inputs: list[Ptn0.Services.Strong.Partition._2020_12.PartitionManagement.GetMembersInBOMWindowBulkInputInfo]) -> Ptn0.Services.Strong.Partition._2020_12.PartitionManagement.GetMembersInBOMWindowResponse: ...
    def GetPartitionsForBOMLine(self, Inputs: list[Ptn0.Services.Strong.Partition._2020_12.PartitionManagement.GetPartitionsForBOMLineIpInfo]) -> Ptn0.Services.Strong.Partition._2020_12.PartitionManagement.GetPartitionsForBOMLineResponse: ...
    def GetSchemesInBOMView(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.PSBOMView]) -> Ptn0.Services.Strong.Partition._2020_12.PartitionManagement.GetSchemesInBOMViewResponse: ...
    def GetTopLevelPartitionsInBOMView(self, Inputs: list[Ptn0.Services.Strong.Partition._2020_12.PartitionManagement.GetTopLevelPtnsInBOMViewInputInfo]) -> Ptn0.Services.Strong.Partition._2020_12.PartitionManagement.GetTopLevelPtnsInBOMViewResponse: ...
    def GetAllChildPtnInAppModel(self, Inputs: list[Ptn0.Services.Strong.Partition._2021_06.PartitionManagement.GetAllChildPtnInAppModelInInfo]) -> Ptn0.Services.Strong.Partition._2021_06.PartitionManagement.GetAllChildPtnInAppModelResponse: ...
    def GetNextChildPtnInAppModel(self, Inputs: list[Ptn0.Services.Strong.Partition._2021_06.PartitionManagement.GetNextChildPtnInAppModelInInfo]) -> Ptn0.Services.Strong.Partition._2021_06.PartitionManagement.GetNextChildPtnInAppModelResponse: ...
    def StopGetChildren(self, Cursor: Ptn0.Services.Strong.Partition._2021_06.PartitionManagement.FetchNextChildrenCursor) -> Ptn0.Services.Strong.Partition._2021_06.PartitionManagement.StopGetChildrenResponse: ...
    def IsPartitionable(self, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision, BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView, IsPartitionableInputInfo: list[Ptn0.Services.Strong.Partition._2021_12.PartitionManagement.IsPartitionableInputInfo]) -> Ptn0.Services.Strong.Partition._2021_12.PartitionManagement.IsPartitionableResponse: ...
    def UpdateMembersInBOMWindow(self, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision, BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView, UpdateMembersInBOMWindowInputInfo: list[Ptn0.Services.Strong.Partition._2021_12.PartitionManagement.UpdateMembersInBOMWindowInputInfo]) -> Ptn0.Services.Strong.Partition._2021_12.PartitionManagement.UpdateMembersInBOMWindowResponse:
        """    
             This operation updates the given input Ptn0Partition with the BOMLine
             objects supplied. BOMLine objects can be added or removed for the given Ptn0Partition.
             The user performing this operation needs ADD_CONTENT or REMOVE_CONTENT access privilege
             on the Ptn0Partition or WRITE access privilege on the BOMLine, depending
             upon ownership of the member. If the user does not have the required privileges or
             if any of the validations fail, then the operation returns an error in ServiceData
             along with the failed BOMLine objects and error code for each of the failed
             BOMLine objects in the UpdateMemberInBomWindowResponse structure.
             

Use Cases:

Use case 1: Add Members to Partition


             User creates a Partition Breakdown with Ptn0Partition objects. The user can
             add single or multiple BOMLine objects to the input Ptn0Partition objects.
             

Use case 2: Remove Members from Partition


             User creates a Partition Breakdown with Ptn0Partition objects. The user can
             remove single or multiple BOMLine objects  from input Ptn0Partition
             objects.
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param ConfigurationContext: 
                         ConfigurationContext used to configure the <b>BOMWindow</b>.
             
        :param ItemRevision: 
                         The <b>ItemRevision</b> for the top line of the <b>BOMWindow</b>.
             
        :param BomView: 
                         The <b>PSBOMView</b> to be used when creating the <b>BOMWindow</b>, or NULL to use
                         the default view.
             
        :param UpdateMembersInBOMWindowInputInfo: 
                         A list of input <b>Ptn0Partition</b> objects, OccThreadPathInformation structure
                         and OpCode.
             
        :return: 
        """
        ...
    def GetMembersInBOMWindow2(self, Input: list[Ptn0.Services.Strong.Partition._2023_06.PartitionManagement.GetMembersInBOMWindowBulkInputInfo2]) -> Ptn0.Services.Strong.Partition._2023_06.PartitionManagement.GetMembersInBOMWindowResponse2: ...

class SearchRestBindingStub(SearchService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    @typing.overload
    def CreatePartitionExpressions(self, PartitionSearchexpInput: Ptn0.Services.Strong.Partition._2011_06.Search.PartitionSearchExpressionInput) -> Ptn0.Services.Strong.Partition._2011_06.Search.SearchExpressionResponse: ...
    @typing.overload
    def CreatePartitionExpressions(self, PartitionSearchexpInput: Ptn0.Services.Strong.Partition._2012_09.Search.PartitionSearchExpressionInput) -> Ptn0.Services.Strong.Partition._2012_09.Search.SearchExpressionResponse: ...
    @typing.overload
    def ExecuteSearch(self, Options: Ptn0.Services.Strong.Partition._2012_09.Search.SearchOptions, Scope: Ptn0.Services.Strong.Partition._2012_09.Search.PartitionScope, Recipe: Ptn0.Services.Strong.Partition._2012_09.Search.SearchRecipe) -> Ptn0.Services.Strong.Partition._2012_09.Search.SearchResponse: ...
    @typing.overload
    def ExecuteSearch(self, SearchOptions: Ptn0.Services.Strong.Partition._2012_09.Search.SearchOptions, Scope: Ptn0.Services.Strong.Partition._2012_09.Search.PartitionScope, Recipe: Ptn0.Services.Strong.Partition._2012_09.Search.SearchRecipe, ExportOption: Ptn0.Services.Strong.Partition._2018_11.Search.ExportOption) -> Ptn0.Services.Strong.Partition._2012_09.Search.SearchResponse: ...
    @typing.overload
    def ExecuteSearch(self, Options: Ptn0.Services.Strong.Partition._2019_06.Search.SearchOptions, Scope: Ptn0.Services.Strong.Partition._2012_09.Search.PartitionScope, Recipe: Ptn0.Services.Strong.Partition._2012_09.Search.SearchRecipe, ExportOption: Ptn0.Services.Strong.Partition._2018_11.Search.ExportOption) -> Ptn0.Services.Strong.Partition._2012_09.Search.SearchResponse: ...
    def FetchNextSearchResults(self, SearchCursor: Ptn0.Services.Strong.Partition._2012_09.Search.SearchCursor, PartitionScope: Ptn0.Services.Strong.Partition._2012_09.Search.PartitionScope) -> Ptn0.Services.Strong.Partition._2012_09.Search.SearchResponse: ...
    def StopSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchCursor) -> Ptn0.Services.Strong.Partition._2012_09.Search.StopSearchResponse: ...

class SearchService:
    """
    
            Contains Search Services to search Model Content in an Application Model (Mdl0ApplicationModel)
            and arranging them by a specific Partition Scheme (Ptn0PartitionScheme). This
            Search Service provides operations that enable searching Conditional Model Elements
            (Mdl0ConditionalElement) in a given Mdl0ApplicationModel such as Product
            Design (Cpd0CollaborativeDesign) or Recipe Container such as subset (Cpd0DesignSubsetElement).
            The search result can be optionally exported to a Microsoft Excel file. Search service
            provides the ability to search for Mdl0ConditionalElement using various search
            recipes (spatial and none spatial). Also this Search Service provides ability to
            create Partition Search expressions (Ptn0SearchPartition and Ptn0SearchUnassigned).
            

Use Cases:

            Search Service is used by the CPD application to implement Searching CPD Design Components
            (Cpd0DesignElement) within a Product Design. However the intent for Partition
            Search is not only to search for Conditional Model Elements, it is also to arrange/group
            the results by Partition, so that the calling application can display the results
            in an organized manner. The search functionality in Partition Search is exactly the
            same compared to the Search functionality offered by AppModel Search Service, except
            for this additional Group by Partition capability. Please refer to the CPD Server
            Functional Specifications for detailed descriptions on Application Model and Model
            Element Data schema.
            
            Partition Search supports searching of Model Elements based on different Search Expressions.
            The Search Expressions could be
            

Spatial



 Box Zone Expression (Mdl0SearchBoxZone) defines a rectangular
            (axis aligned) box, defined in a 3d space, which could be used to find Conditional
            Model Elements that are either inside/outside/intersecting the 3 dimensional box.
            
 Plane Zone Expression (Mdl0SearchPlaneZone) defines a 3d
            plane and the search expression could define to look for Conditional Model Elements
            above/below/intersecting the plane.
            
 Proximity Expression (Mdl0SearchProximity) used to find Conditional
            Model Elements that are spatially nearby a given set of other Conditional Model Elements.
            



Non Spatial



Saved Query Expression (Mdl0SearchSavedQuery) used to search
            Conditional Model Elements with specific attribute values. Accepts wildcards for
            attribute values.
            
Include Expression (Mdl0SearchSlctContent) specific set of
            Model Elements that are included as part of the search result.
            
Exclude Expression (Mdl0SearchGroup) specific set of Model
            Elements that are excluded from the search result.
            
Partition Expression (Ptn0SearchPartition) Model Elements
            that are members of a particular set of Partitions in the given Product Design.
            
Closure Query Expression Not Implemented in Teamcenter 9.1 Out of
            scope for now.
            




            The above search expressions could be joined using AND/OR operators to form complex
            Search Recipes. Also the r esults of the execution of a Search Recipe could be constrained
            to return only a given set of object types. For e.g. the results of a Search Recipe
            could be restricted to return only Cpd0DesignElement objects. The callers
            could also use NOT operator to negate any of the non spatial expressions above and
            combine them in a Search Recipe (Note that NOT is a Unary operator and it accepts
            only one expression to negate unlike AND/OR which combines multiple expressions).
            
            Search Service is typically used to perform the following operations:
            
            Execute a Search Recipe: Executes a complex search recipe formed using the various
            search expression combinations and constrained using the search scope (Application
            Model, Search Types). The results of executing a search could be sorted using one
            or more of the attributes of the returned object type. Also the number of objects
            that should be returned to the caller can be controlled by setting the defaultLoadCount.
            If the default load count is set to zero then all the results are returned in one
            shot.
            
            If the default load count is set to a non zero value, then the caller will be returned
            a search cursor which could be used to get search results as and when it is required.
            Also an active search cursor could be released by calling the stopSearch operation.
            
            Over and above of the process of searching, the results are also grouped by Partition
            objects based on the given input Partition Scheme.
            
            Sample code:
            
            Typically following is the sequence of operations to perform a Search:
            
            1.Â Â Â Â Call createOrUpdateConfigurations and create a Configuration
            Context with a valid Revision Rule (optionally with an Effectivity Rule)
            
            2.Â Â Â Â Call createSearchExpressions and create the elemental search
            expressions
            
            3.Â Â Â Â Create the Search Expression Sets to join the elemental
            search expressions to a complex search recipe
            
            4.Â Â Â Â Call executeSearch with the complex Search Expression Set.
            executeSearch will return a default set of conditional elements (defined by the defaultLoadCount)
            
            5.Â Â Â Â Call fetchNextSearchResults repeatedly to get further results
            based on the search and each time this operation could be called with its own defaultLoadCount
            value.
            
            6.Â Â Â Â Optionally stopSearch could be called to clean up the results
            and this call would indicate that the caller is no longer interested in getting back
            the remaining search results.
            
            Apart from execution of a search query, there are two operations that help the callers
            to save a Search Recipe and enquire the contents of a persisted Search Recipe. The
            setRecipes call saves a Search Recipe and it requires a Search Container object to
            persist the recipe. Currently in CPD application, this could be one of either Cpd0DesignSubsetInstance
            or Ptn0Partition o r Mdl0SubsetDefinition. The getRecipes call returns the search
            expressions and their combinations (as Search Expression Sets) of a stored recipe.
            
            The sample in soa_client.zip, com.teamcenter.cpdsearch.PartitionSearchServiceSOASampleTest.java
            shows the use of Search operations for the following use case:
            


Execute a Search with a complex recipe (Saved Query combined with
            Box Zone and the results restricted to Cpd0DesignElement objects) and return the
            results organized by the functional partition scheme.
            

            .
            

Dependencies:

            Search
            


Library Reference:

Ptn0SoaPartitionStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SearchService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    @typing.overload
    def CreatePartitionExpressions(self, PartitionSearchexpInput: Ptn0.Services.Strong.Partition._2011_06.Search.PartitionSearchExpressionInput) -> Ptn0.Services.Strong.Partition._2011_06.Search.SearchExpressionResponse: ...
    @typing.overload
    def CreatePartitionExpressions(self, PartitionSearchexpInput: Ptn0.Services.Strong.Partition._2012_09.Search.PartitionSearchExpressionInput) -> Ptn0.Services.Strong.Partition._2012_09.Search.SearchExpressionResponse: ...
    @typing.overload
    def ExecuteSearch(self, Options: Ptn0.Services.Strong.Partition._2012_09.Search.SearchOptions, Scope: Ptn0.Services.Strong.Partition._2012_09.Search.PartitionScope, Recipe: Ptn0.Services.Strong.Partition._2012_09.Search.SearchRecipe) -> Ptn0.Services.Strong.Partition._2012_09.Search.SearchResponse: ...
    @typing.overload
    def ExecuteSearch(self, SearchOptions: Ptn0.Services.Strong.Partition._2012_09.Search.SearchOptions, Scope: Ptn0.Services.Strong.Partition._2012_09.Search.PartitionScope, Recipe: Ptn0.Services.Strong.Partition._2012_09.Search.SearchRecipe, ExportOption: Ptn0.Services.Strong.Partition._2018_11.Search.ExportOption) -> Ptn0.Services.Strong.Partition._2012_09.Search.SearchResponse: ...
    @typing.overload
    def ExecuteSearch(self, Options: Ptn0.Services.Strong.Partition._2019_06.Search.SearchOptions, Scope: Ptn0.Services.Strong.Partition._2012_09.Search.PartitionScope, Recipe: Ptn0.Services.Strong.Partition._2012_09.Search.SearchRecipe, ExportOption: Ptn0.Services.Strong.Partition._2018_11.Search.ExportOption) -> Ptn0.Services.Strong.Partition._2012_09.Search.SearchResponse: ...
    def FetchNextSearchResults(self, SearchCursor: Ptn0.Services.Strong.Partition._2012_09.Search.SearchCursor, PartitionScope: Ptn0.Services.Strong.Partition._2012_09.Search.PartitionScope) -> Ptn0.Services.Strong.Partition._2012_09.Search.SearchResponse:
        """    
             This operation gets the next set of Model Elements from a previously executed search
             results. The results returned will be based on the load count specified in the SearchCursor input structure. This API returns
             the same response structure as that of executeSearch.
             
             The results obtained by fetchNextSearchResults
             are again arranged by Partition based on the PartitionScope specified.
             


Use Cases:

             This API is used in conjunction with executeSearch
             operation. executeSearch operation is a prerequisite
             for invoking fetchNextSearchResults. The
             search cursor returned by the executeSearch is used to call fetchNextSearchResults operation. This operation could be called
             repeatedly by the caller, until all the search results are returned. The fetchNextSearchResults in Partition Search Service is introduced
             mainly to organize the search results by Partition over and above of the functionality
             provided in the AppModel Search Service.
             

Dependencies:

             fetchNextSearchResults
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param SearchCursor: 
                         Data structure that keeps track of the list of objects returned by a search.
             
        :param PartitionScope: 
                         Defines Partition scope for the search results arrangement. <i>PartitionScope</i>
                         has a partition scheme name by which the results should be organized by and a flag
                         that indicates whether immediate partitions should be considered or to consider the
                         whole <i>partition breakdown</i> structure while returning back the partition groups
             
        :return: Returns the Search Response structure
        """
        ...
    def StopSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchCursor) -> Ptn0.Services.Strong.Partition._2012_09.Search.StopSearchResponse:
        """    
             This operation stops further loading of objects from a previously executed search
             and clears all the memory allocated for the search operation. It deletes the search
             cursor and the list of Model Elements that are kept track by the Search cursor from
             the Server Memory.
             
             The stopSearch does not unload any previously
             loaded Model Elements. Also there is no locking or unlocking performed by the stopSearch operation.
             


Use Cases:

             When a search is executed in CPD and the search returns a large set of objects. The
             server process keeps the results of a search using a search cursor object. At each
             fetchNextSearchResults operation, the results
             are further filtered and returned in batches specified by the load count. However
             if the caller is not interested in consuming the search results further, then a stopSearch could be called to release all the resources
             allocated for that search operation. This includes dropping the runtime search cursor
             object and the list of Model Elements kept track by the cursor.
             

Dependencies:

             fetchNextSearchResults
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param SearchCursor: 
                         A runtime object identifier that keeps track of the Search results and the corresponding
                         indexes as of where the caller has consumed the results. Invoking stopSearch on this
                         object deletes this object.
             
        :return: Returns stopSearchResponse data structure
        """
        ...

