import Ptn0.Services.Strong.Partition._2011_06.PartitionManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetParentBulkInputInfo:
    """
    
            Contains an object of ConfigurationContext , list of child Ptn0Partition
            objects for which parent Ptn0Partition objects are to be found.It also represents
            the desired maximum level count and maximum parent Ptn0Partition objects that
            are to be returned. The Ptn0Partition objects provided should be from same Model
            Object and same Partition Scheme.
            
    """
    def __init__(self, ) -> None: ...
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            A ConfigurationContext to be used for configuring the output parent Ptn0Partition
            objects with the effectivity condition or revision rule attached to it.
            """
    ChildPartitions: list[Teamcenter.Soa.Client.Model.Strong.Ptn0Partition]
    """
            A list of child Ptn0Partition objects for which the parent Ptn0Partition
            objects are to be found.
            """
    MaxLevelCount: int
    """
            The number of levels of parent Ptn0Partition objects that have to be fetched.
            When this count is set to 0, all levels of parent Ptn0Partition objects in
            that Partition Rollup for a given child Ptn0Partition objects are returned.
            """
    MaxParentCount: int
    """
            The number of parent Ptn0Partition objects to be found. When this count is
            set to 0, all parent Ptn0Partition objects in that Partition Breakdown for
            a given parent Ptn0Partition objects are returned.
            """
    ClientId: str
    """
            A unique string sent by the calling function, so that the output Search Expression
            object could be mapped back to the input.
            """

class GetParentsBulkOutputInfo:
    """
    
GetParentsBulkOutputInfo structure represents the map of the child Partition
            and vector of its parent Partitions, number of parent Partition levels traversed
            in the operation and also a Boolean indicating if parent list is truncated as per
            the input maxParentCount.
            
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
    ClientId: str
    """
            A unique string sent by the calling function, so that the output Search Expression
            object could be mapped back to the input.
            """

class GetParentsBulkResponse:
    """
    
GetParentsBulkResponse structure represents vector of GetParentsBulkOutputInfo
            consisting the parent Partitions, their corresponding child Partition ( i.e., a Map
            of child Partition and vector of its parent Partitions ), number of parent Partition
            levels traversed in the breakdown, total number of parent Partitions found in the
            operation and also the errors via serviceData if invalid input parameters are supplied.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetParentsBulkOutputInfo]
    """
            Vector of GetParentsBulkOutputInfo structures for corresponding vector of
            input GetParentsInputInfo structure.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Consists the errors returned if any."""

class WherePartitionedMemberInfo:
    """
    
            Returned as part of the response for the operation wherePartitioned2. Contains a
            Ptn0Partition that contains an object provided as input to this operation.
            
    """
    def __init__(self, ) -> None: ...
    Partition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """A Ptn0Partition containing an input object."""
    IsPseudoMember: bool
    """If true, the input object is a pseudo-member of the Ptn0Partition."""

class WherePartitionedOutputInfo2:
    """
    
            Returned as part of the response for the operation wherePartitioned2. Contains the
            input objects to the operation and the Ptn0Partitions containing the input
            objects.
            
    """
    def __init__(self, ) -> None: ...
    Partitionable: Teamcenter.Soa.Client.Model.Strong.POM_object
    """An input object that is contained in a Ptn0Partition object."""
    MemberInfo: list[WherePartitionedMemberInfo]
    """A list of Ptn0Partitions containing the input objects."""

class WherePartitionedResponse2:
    """
    
            The response for the operation wherePartitioned2. Contains the objects provided as
            input to the operation and the Ptn0Partitions containing the input objects.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[WherePartitionedOutputInfo2]
    """A list of input objects and the Ptn0Partitions containing the input objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data for any error information."""

class PartitionManagement:
    """
    Interface PartitionManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetParents(self, Inputs: list[GetParentBulkInputInfo]) -> GetParentsBulkResponse:
        """    
             This operation gets configured or un configured parent Partitions of the input child
             Partitions. Desired level of parent Partitions and desired number of Parents can
             be found by specifying the input parameters maximum level of parents and maximum
             number of parents respectively.
             

Use Cases:

             When user creates a Partition Breakdown with parent Partitions and child Partitions,
             they can select a single or multiple child Partitions within this breakdown and try
             to find their parent Partitions. The maximum number of parent Partitions and level
             of parent Partitions can be given as an optional input. User can get all or desired
             number of configured or un configured parents of input child Partitions at all levels
             or desired levels in a Partition breakdown by supplying ConfigurationContext
             object as input.
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Inputs: 
                         A list of <b>GetParentBulkInputInfo</b> objects containing the details of child <b>Ptn0Partition</b>
                         objects, number and level of parent <b>Ptn0Partition</b> objects to be found. Configured
                         parent <b>Ptn0Partition</b> objects can be obtained by specifying the <b>ConfigurationContext</b>
                         object. Each input should contain <b>Ptn0Partition</b> objects from Same <b>Model
                         Object </b>and Same <b>Partition Scheme</b>. Otherwise exception will be thrown.
             
        :return: 280065: One or more selected Partition objects cannot be processed because they are
             either from different Model or different Partition Schemes. Only Partitions From
             Same Model and Same Scheme are allowed.
        """
        ...
    def WherePartitioned2(self, Inputs: list[Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.WherePartitionedInputInfo]) -> WherePartitionedResponse2: ...

