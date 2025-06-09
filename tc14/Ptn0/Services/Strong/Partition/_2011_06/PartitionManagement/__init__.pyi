import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ErrorValuesStruct:
    """
    
            ErrorValuesStruct structure contains the error details which occurred while updating
            member.
            
            For each failed member this structure is populated with details such as error code,
            error message and error level.
            
    """
    def __init__(self, ) -> None: ...
    Code: int
    """integer value representing error code."""
    Message: str
    """string representing error message."""
    Level: str
    """level represents the error crititicality."""

class FailedMemberErrorStruct:
    """
    
            FailedMemberErrorStruct structure contains the member and errorVal structure which
            stores all the information about failed member.
            
    """
    def __init__(self, ) -> None: ...
    Member: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """Member failed to update."""
    ErrorVal: ErrorValuesStruct
    """Stores all the data about error which occurred while updating member."""

class GetChildrenInputInfo:
    """
    
GetChildrenInputInfo structure represents
            the details of ConfigurationContext , Parent Partition for which child Partitions
            are to be fetched.  It also represents the desired maximum level count and maximum
            child Partitions that have to be fetched.
            
    """
    def __init__(self, ) -> None: ...
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            Configuration Context object which configures the output child Partitions with the
            effectivity condition or revision rule attached to it.
            """
    ParentPartition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """parent Partition object  for which the children Partitions are to be fetched."""
    MaxLevelCount: int
    """
            Integer specifying the number of levels of child Partitions that have to be fetched.
            When this count is set to 0, you will get all levels of child Partitions in that
            Partition Breakdown for a given Parent Partition.
            """
    MaxChildCount: int
    """
            Integer specifying the number of  child Partitions that have to be fetched. When
            this count is set to 0, you will get all child Partitions in that Partition Breakdown
            for a given parent Partition.
            """

class GetChildrenOutputInfo:
    """
    
            Contains the map of ChildParentPartitionMap, number of Partition level s traversed
            in the operation and also a Boolean indicating if children list is truncated as per
            the input maxChildCount.
            
    """
    def __init__(self, ) -> None: ...
    ParentChildMap: System.Collections.Hashtable
    """
            A map of parent Ptn0Partition object and list of its child Ptn0Partition
            objects (Ptn0Partition, list of(Ptn0Partition)).
            """
    ExpandedLevelCount: int
    """
            Number of Partition levels that were traversed while executing this operation. This
            value depends up on the maximum level count that is supplied as input parameter.
            """
    ChildPartitionListTruncated: bool
    """
            If true the child Ptn0Partition object list is truncated. This value depends
            up on the input maximum child count that is supplied as input parameter
            """

class GetChildrenResponse:
    """
    
            Contains list of GetChildrenOutputInfo objects consisting the child Ptn0Partition
            objects, their corresponding parent Ptn0Partition object ( i.e., a Map of
            Parent Ptn0Partition and list of its Child  Ptn0Partitions ) , number
            of Partition levels traversed in the breakdown, total number of child Ptn0Partition
            objects found in the operation and also the errors via serviceData if invalid input
            parameters are supplied.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetChildrenOutputInfo]
    """
            List of GetChildrenOutputInfo objects for corresponding list of input GetChildrenInputInfo
            objects.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member."""

class GetMembersInputInfo:
    """
    
GetMembersInputInfo structure represents
            the details of ConfigurationContext, Partition for which members are to be
            fetched.  It also represents content persistence mode and a Boolean flag to indicate
            to load the CAD data or not.
            
    """
    def __init__(self, ) -> None: ...
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
ConfigurationContext object which configures the output members with the effectivity
            condition or revision rule attached to it.
            """
    Partition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """Partition object  for which the members are to be fetched."""
    ContentPersistenceMode: str
    """
            Enumerator indicating the content persistence mode.This parameter can be any one
            of the four following values which can be passed to this enumerator depending on
            the use case.
            


STATIC_MODE         This
            mode can be used when only static members are required.
            
DYNAMIC_MODE     This
            mode can be used when only dynamic members are required.
            
ALL_MODE             This
            mode can be used when both static and dynamic members are required.
            
AUTO_MODE            This
            mode can be used when members are fetched depending on    the
            default persistence mode of the Partition                
            

"""
    IsGraphicDataToBeLoaded: bool
    """
            Boolean flag indicating, whether the graphic data such as JT data has to be loaded
            when members are fetched.
            """

class GetMembersOutputInfo:
    """
    Contains input Ptn0Partition object and vector of its members.
    """
    def __init__(self, ) -> None: ...
    InputPartition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """Input Ptn0Partition object."""
    MembersList: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """List of member objects for the input Ptn0Partition object."""

class GetMembersResponse:
    """
    
            Contains list of GetMembersOutputInfo object and serviceData structures. Ptn0Partition
            objects along with their members are returned via GetMembersOutputInfo object.  If
            the input parameters are invalid, the errors are returned in serviceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetMembersOutputInfo]
    """
            List of GetMembersOutputInfo objects for corresponding list of input GetMembersInputInfo
            object.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member."""

class GetParentsInputInfo:
    """
    
            GetParentsInputInfo structure represents the details of ConfigurationContext,
            child Partition for which parent Partitions are to be fetched.  It also represents
            the desired maximum level count and maximum parent Partitions that have to be fetched
            for the list of Partition Objects in the input.
            
    """
    def __init__(self, ) -> None: ...
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            Configuration Context object which configures the output  parent Partitions
            with the effectivity condition or revision rule attached to it.
            """
    ChildPartition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """child Partition object  for which the parent Partitions are to be fetched."""
    MaxLevelCount: int
    """
            Integer specifying the number of levels of parent Partitions that have to be fetched.
            When this count is set to 0, you will get all levels of parent Partitions in that
            Partition Rollup for a given list of child Partitions. This level will be applicable
            for each Partition from the list of child Partitions specified in the input.
            """
    MaxParentCount: int
    """
            Integer specifying the number of  parent Partitions that have to be fetched. When
            this count is set to 0, you will get all parent Partitions in that Partition Rollup
            for a given list of child Partitions. Parent Partition count will be applicable for
            each child partition in the list of child Partitions in the input.
            """

class GetParentsOutputInfo:
    """
    
GetParentsOutputInfo structure represents
            the map of the child Partition and vector of its parent Partitions, number of parent
            Partition levels traversed in the operation and also a Boolean indicating if parent
            list is truncated as per the input maxParentCount.
            
    """
    def __init__(self, ) -> None: ...
    ChildParentMap: System.Collections.Hashtable
    """
            Map of child Partition and vector of its parent Partitions. Child Partition is the
            key in the map and vector of parent Partitions is its value.
            """
    ExpandedLevelCount: int
    """
            Number of parent Partition levels that are traversed while executing this operation.
            This value depends up on the maximum level count that is supplied as input parameter.
            """
    ParentPartitionListTruncated: bool
    """
            Boolean flag which indicates that the parent Partition list is truncated or not.
            This value depends up on the input maximum parent count that is supplied as input
            parameter.
            """

class GetParentsResponse:
    """
    
GetParentsResponse structure represents vector
            of GetParentsOutputInfo consisting the parent
            Partitions, their corresponding child Partition ( i.e., a Map of child Partition
            and vector of its parent  Partitions ), number of parent Partition levels traversed
            in the breakdown, total number of parent Partitions found in the operation and also
            the errors via serviceData if invalid input
            parameters are supplied.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetParentsOutputInfo]
    """
            Vector of GetParentsOutputInfo structures
            for corresponding vector of input GetParentsInputInfo
            structure.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """consists the errors returned if any."""

class GetPartitionsInputInfo:
    """
    
GetPartitionsInputInfo structure is input
            to the getPartitions SOA.It contains the
            details of configuration context, Application Model,
            Partition Scheme and maxPartitionCount.
            

    """
    def __init__(self, ) -> None: ...
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            The RevisionRule as per the users requirement which will be used for configuring
            output.
            """
    ModelCntxt: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """Application Model object for which partitions to be searched."""
    PartitionScheme: Teamcenter.Soa.Client.Model.Strong.Ptn0PartitionScheme
    """Partition Scheme object  as another search limit for partitions."""
    MaxPartitionCount: int
    """Its a integer variable used to truncate the output list of Partition."""

class GetPartitionsOutputInfo:
    """
    
GetPartitionsOutputInfo Structure contains
            details of output result also partition scheme to which this output belongs to, and
            the Boolean to reflect the value if output list was truncated due to maxPartitionCount.
            
    """
    def __init__(self, ) -> None: ...
    ParitionScheme: Teamcenter.Soa.Client.Model.Strong.Ptn0PartitionScheme
    """Input Partition Scheme for which SOA was operated"""
    Partitions: list[Teamcenter.Soa.Client.Model.Strong.Ptn0Partition]
    """List of partitions result of the SOA operation"""
    IsListTruncated: bool
    """
            Variable set to true if output list of partition was truncated because of maxPartitionCount setting, otherwise its set to false.
            """

class GetPartitionsResponse:
    """
    
GetPartitionsResponse contains result of
            the soa operation and exception data.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetPartitionsOutputInfo]
    """
            Vector of GetpartitionsOutputInfo structure
            which contains the actual result of the SOA operation that is list of partitions
            for given Application Model and Partition Scheme.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any  exception occurred while performing SOA is returned in service data also the
            list of output partitions are added to plain object list of service data.
            """

class GetSchemesInModelOutputInfo:
    """
    
GetSchemesInModelOutputInfo  structure contains
            the list of partition schemes which are output of SOA operation and input application
            model to which schemes belongs.
            
    """
    def __init__(self, ) -> None: ...
    Model: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """Application Model object which was input to the SOA operation."""
    PartitionSchemes: list[Teamcenter.Soa.Client.Model.Strong.Ptn0PartitionScheme]
    """List of Partition schemes result of the SOA operation."""

class GetSchemesInModelResponse:
    """
    
            Output contains list of Partition Scheme and Application Model. Service data is populated
            with any exception occurred while performing operation and partition scheme objects.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetSchemesInModelOutputInfo]
    """
            This is vector of  GetSchemesInModelOutputInfo
            structure which contains the Partition scheme list and Application
            model.
"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains exception occurred while performing operation. Plain object list is populated
            with the resulted partition scheme object.
            """

class GetTopLevelPartitionsInputInfo:
    """
    
GetTopLevelPartitionsInputInfo structure
            represents the details of Application model Context ,  Partition scheme  and Configuration
            context, for which top level Partitions are to be fetched.
            
    """
    def __init__(self, ) -> None: ...
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            Configuration Context object which configures the output top level Partitions
            with the effectivity condition or revision rule attached to it.
            """
    ModelCntxt: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """Application Model object for which the top level Partitions are to be fetched."""
    PartitionScheme: Teamcenter.Soa.Client.Model.Strong.Ptn0PartitionScheme
    """Partition Scheme object for which the top level Partitions are to be fetched."""

class GetTopLevelPartitionsOutputInfo:
    """
    
GetTopLevelPartitionsOutputInfo structure
            represents the list of top level Partitions returned corresponding to a input Partition
            Scheme supplied.
            
    """
    def __init__(self, ) -> None: ...
    ParitionScheme: Teamcenter.Soa.Client.Model.Strong.Ptn0PartitionScheme
    """Input  Partition Scheme to which this structures output partitions belong to."""
    TopLevelPartitions: list[Teamcenter.Soa.Client.Model.Strong.Ptn0Partition]
    """
            Configured top level Partitions as per the Configuration Context and supplied input
            Partition Scheme and Application Model.
            """

class GetTopLevelPartitionsResponse:
    """
    
GetTopLevelPartitionsResponse structure represents
            the list of GetTopLevelPartitionsOutputInfo
            consisting of the top level Partitions, their corresponding scheme structure and
            also the errors via serviceData if invalid input parameters are supplied.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetTopLevelPartitionsOutputInfo]
    """
            List of GetTopLevelPartitionsOutputInfo structures
            for corresponding list of input GetTopLevelPartitionsInputInfo
            structures.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """consists of the errors returned if any."""

class PersistDynamicMembersInputInfo:
    """
    
PersistDynamicMembersInputInfo structure
            is input parameter for the SOA. This structure provides partition for which members
            should be persisted, structure also contains the configuration context representing
            revision rule.
            
    """
    def __init__(self, ) -> None: ...
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            Revision rule or user defined rule. Passing NULLTAG
            in this parameter is not allowed.
            """
    Partition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """Partition to persist Members."""

class UpdateChildrenOrParentsInputInfo:
    """
    
UpdateChildrenOrParentsInputInfo structure
            consists the input of Partition to be updated,  Partitions to be updated as children
            or parents, enumerator to indicate what kind of update is to be performed and a Boolean
            flag to indicate whether adding children or parents to given input Partition.
            
    """
    def __init__(self, ) -> None: ...
    Partition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """Input Partition business object, to which the members wil be updated."""
    PartitionList: list[Teamcenter.Soa.Client.Model.Strong.Ptn0Partition]
    """List of Partitions to  be updated for input  Partition based on the opCodevalue."""
    OpCode: str
    """
            Its a enum variable which will be taking ADD, REMOVE and REPLACE
            as values.As per the value of this parmeter, input partitions  list is added/ removed/
            replaced as children/ parens to the input Partition.
            """
    IsParent: bool
    """
            Boolean flag to indicate whether the input Partition being updated is a parent partition
            or child Partition.
            """

class UpdateMembersInputInfo:
    """
    
UpdateMembersInputInfo structure hold the
            information required to carry out SOA operation.
            
            Vector of this structure is passed as input to SOA operation to do the bulk operation
            for more than one Partition
            

    """
    def __init__(self, ) -> None: ...
    InputPartition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """
            Holds the Partition business object. updateMember SOA will operate on this input
            based on the operation code and partition business object is updated accordingly.
            """
    MembersList: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            List of members to add, remove or replace membership object for a partition based
            on the opCodevalue.
            """
    OpCode: str
    """
            Its a enum variable which will be taking ADD, REMOVE and REPLACE
            as values.As per the value of this parmeter inputPartition is updated with members.
            """
    ContentPersistenceMode: str
    """
            Its Enum variable which has following allowed values.
            

STATIC_MODE:  Updates Partition
            by creating memberships in database for input members.
            
DYNAMIC_MODE: Updates Partition
            Recipe to include the input members
            
AUTO_MODE : Selectes default
            mode set by user from remaining three modes.
            
ALL_MODE: Updates Partition
            by creating static memberships in databse for input members and updates recipe on
            partion.
            

"""
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            Configuration context value by user, this is the business object representing user
            defined revision rule. If user pass the NULLTAG  it will load a default revision
            rule from database and proceed.
            """

class UpdateMembersOutputInfo:
    """
    This structure holds update member failed with failed members and error details.
    """
    def __init__(self, ) -> None: ...
    MemberErrorVector: list[FailedMemberErrorStruct]
    """
            Structure containing information related to failed member and corresponding error
            occurred while performing update member operation.
            """
    InputPartition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """Input partition of which update member operation failed."""

class UpdateMembersResponse:
    """
    
            UpdateMembersResponse structure contains ServiceData for storing the exception occurred
            while performing update member operation and UpdateMembersOutputInfo structure.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data for update member operation it stores the error/ exception if it occurres
            while performing operation. There are no plain object, created object or deleted
            objects returned in servicedata.
            """
    Output: list[UpdateMembersOutputInfo]
    """It returns failed members and errors corresponding to it.."""

class WherePartitionedInputInfo:
    """
    
WherePartitionedInputInfo is input parameter
            to wherePartitioned SOA.
            
    """
    def __init__(self, ) -> None: ...
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
RevisionRule business object or any user defined rule to configure the output
            as per the rule.
            """
    ModelContext: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """
ApplicationModel business object it limits search scope for SOA operation.
            This parameter cannot be NULLTAG.
            """
    PartitionScheme: Teamcenter.Soa.Client.Model.Strong.Ptn0PartitionScheme
    """
            Partition Scheme as another search criteria for the SOA, user can give NULLTAG
            value for this parameter.For NULLTAG search scope will be  application model
            itself.
            """
    Partitionable: Teamcenter.Soa.Client.Model.Strong.POM_object
    """An element for which corresponding partition is searched."""

class WherePartitionedOutputInfo:
    """
    
            SOA operation output that is partition list for the partitionable is returned along
            with the input partitionable in above structure.
            
    """
    def __init__(self, ) -> None: ...
    Partitionable: Teamcenter.Soa.Client.Model.Strong.POM_object
    """Input Partitionable provided while performing operation"""
    Partitions: list[Teamcenter.Soa.Client.Model.Strong.Ptn0Partition]
    """List of output partitions for partitionables."""

class WherePartitionedResponse:
    """
    
WherePartitionedResponse structure is returned
            as the result of the SOA operation.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[WherePartitionedOutputInfo]
    """
            List of a type WherePartitionedOutputInfo
            containing output partition and given input partitionable to SOA.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Exception occurred while performing SOA operation is put into serviceData. Results of SOA that is partition list is added to
            plain object list of serviceData.
            """

class PartitionManagement:
    """
    Interface PartitionManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetChildren(self, Inputs: list[GetChildrenInputInfo]) -> GetChildrenResponse:
        """    
             This operation is used to get configured or unconfigured child Partitions
             of the input parent Partitions. Desired level of children and desired number of children
             can be fetched by specifying the input parameters maximum level of children and maximum
             number of children respectively.
             

Use Cases:

             When user creates a Partition Breakdown with Parent Partitions and
             child Partitions, he can select a single or multiple Partitions within this breakdown
             and try to fetch their child Partitions.The maximum number of child Partitions and
             level of child Partitions can be given as an optional input. User can get all or
             desired number of configured or un configured children of input Partitions at all
             levels or desired levels in a Partition Breakdown by supplying ConfigurationContext
             object as input.
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Inputs: 
                         Vector of Structures containing the details of Parent Partitions, number and level
                         of child Partitions to be fetched. Configured child Partitions can be obtained by
                         specifying the <b>ConfigurationContext</b> object.
             
        :return: .
        """
        ...
    def GetMembers(self, Inputs: list[GetMembersInputInfo]) -> GetMembersResponse:
        """    
             This operation is used to get configured or un configured members of the input Partitions.
             All the members of a single or multiple Partitions can be fetched using this operation.
             

Use Cases:

             When user creates a Partition Breakdown with Partitions and members (e.g., Design
             Components) , user can select a single or multiple Partitions within this breakdown
             and try to fetch their members. User can get all configured or un configured members
             of input Partitions by supplying ConfigurationContext object as input. Depending
             on the use case, the user may get the dynamic members or static members or both or
             depending on the default persistence mode of the Partition. An additional flag can
             also be passed as input to load the graphic data that is associated with each member.
             

             Use case 1:
             
             When user adds members to a static Partition, system creates Membership links to
             this Partition. These members can be fetched by specifying the content persistence
             mode input argument as STATIC_MODE.
             

             Use case 2:
             
             When user adds members to a Partition dynamically, system updates recipe on Partition.
             System will not create any persistent Membership links when Partitions are updated
             dynamically. These dynamic members can be fetched by executing the recipe, by specifying
             the content persistence mode input argument as DYNAMIC_MODE.
             

             Use case 3:
             
             Users can add members to Partitions statically by creating Memberships and dynamically
             by creating the search recipe. Both these static members and dynamic members can
             be fetched by specifying the content persistence mode input argument as ALL_MODE.
             

             Use case 4:
             
             Users can add members to Partitions statically by creating Memberships and also dynamically
             by creating search recipe. The members can be fetched depending on the default persistence
             mode of the Partition also i.e., if Partition is a dynamic Partition like a Spatial Partition, then user can get dynamic members
             and if its a static Partition like a Functional
             Partition, then user can fetch static members by specifying the content
             persistence mode input argument as AUTO_MODE.
             



Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Inputs: 
                         Vector of Structures containing the details of Parent Partitions, number and level
                         of child Partitions to be fetched. Configured child Partitions can be obtained by
                         specifying the Configuration Context object.
             
        :return: .
        """
        ...
    def GetParents(self, Inputs: list[GetParentsInputInfo]) -> GetParentsResponse:
        """    
             This operation is used to get configured or un configured parent Partitions of the
             input child Partitions.Desired level of parent Partitions and desired number of Parents
             can be fetched by specifying the input parameters maximum level of parents and maximum
             number of parents respectively.
             

Use Cases:

             When user creates a Partition Breakdown with parent Partitions and child Partitions,
             he can select a single or multiple child Partitions within this breakdown and try
             to fetch their parent Partitions.  The maximum number of parent Partitions and level
             of parent Partitions can be given as an optional input. User can get all or desired
             number of configured or un configured parents of input child Partitions at all levels
             or desired levels in a Partition breakdown by supplying ConfigurationContext object
             as input.
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Inputs: 
                         Vector of Structures containing the details of child Partitions, number and level
                         of parent Partitions to be fetched. Configured parent Partitions can be obtained
                         by specifying the <b>ConfigurationContext</b> object.
             
        :return: .
        """
        ...
    def GetPartitions(self, Input: list[GetPartitionsInputInfo]) -> GetPartitionsResponse:
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
    def GetSchemesInModel(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel]) -> GetSchemesInModelResponse:
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
    def GetTopLevelPartitions(self, Inputs: list[GetTopLevelPartitionsInputInfo]) -> GetTopLevelPartitionsResponse:
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
    def PersistDynamicMembers(self, Inputs: list[PersistDynamicMembersInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def UpdateChildrenOrParents(self, Inputs: list[UpdateChildrenOrParentsInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def UpdateMembers(self, Inputs: list[UpdateMembersInputInfo]) -> UpdateMembersResponse:
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
    def WherePartitioned(self, Inputs: list[WherePartitionedInputInfo]) -> WherePartitionedResponse:
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

