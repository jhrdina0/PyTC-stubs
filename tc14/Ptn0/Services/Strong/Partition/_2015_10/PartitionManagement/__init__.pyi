import Ptn0.Services.Strong.Partition._2013_05.PartitionManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetMappedPartitionsInputData:
    """
    
            Contains the list of Ptn0Partition objects, list of Ptn0PartitionScheme
            objects, input options, an object of ConfigurationContext and the Mdl0ApplicationModel
            object.
            
    """
    def __init__(self, ) -> None: ...
    Partitions: list[Teamcenter.Soa.Client.Model.Strong.Ptn0Partition]
    """
            The list of Ptn0Partition objects for which the mapped Ptn0Partition
            objects  has to be retrieved.
            """
    PartitionSchemes: list[Teamcenter.Soa.Client.Model.Strong.Ptn0PartitionScheme]
    """
            The list of Ptn0PartitionScheme objects from which the mapped Partitions has
            to be retrieved.
            """
    AppModelReference: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """Mdl0ApplicationModel object from which the mapped Partitions has to be retrieved."""
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
ConfigurationContext object to be applied for configuring the mapped Ptn0Partition
            objects.
            """
    Options: Ptn0.Services.Strong.Partition._2013_05.PartitionManagement.StringBoolMapStruct
    """
            A  map of option names and flag values (String/Boolean).
            
            Valid option names are:
            
includeChildPartitions - if true, the child
            Partitions of the mapped Partitions are retruned.
            """

class GetMappedPartitionsResponse:
    """
    
            Contains the list of MappedPartitionStruct
            objects and an object of ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    MappedPartitions: list[MappedPartitionStruct]
    """
            The list of MappedPartitionStruct objects
            containing the map of input Ptn0Partition objects and their corresponding
            mapped Ptn0Partition objects. Only those input Ptn0Partition objects
            which has at least one mapped Ptn0Partition object will be returned in the
            map.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """An object of ServiceData for any error information."""

class GetOwningPartitionsInputData:
    """
    
            Contains the list of Ptn0Partition objects, object of ConfigurationContext
            and the Mdl0ApplicationModel object.
            
    """
    def __init__(self, ) -> None: ...
    InputPartitions: list[Teamcenter.Soa.Client.Model.Strong.Ptn0Partition]
    """
            The list of Ptn0Partition objects for which the owning Ptn0Partition
            objects has to be retrieved.
            """
    AppModelReference: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """Mdl0ApplicationModel object from which the owning Partitions has to be retrieved."""
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
ConfigurationContext to be applied for configuring the owning Ptn0Partition
            objects.
            """

class GetOwningPartitionsResponse:
    """
    
            Contains the list of OwningPartitionStruct
            objects and an object of ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    OwningPartitions: list[OwningPartitionStruct]
    """
            The list of OwningPartitionStruct objects
            containing the map of input Ptn0Partition objects and their corresponding
            owning Ptn0Partition objects. Only those input Ptn0Partition objects
            which has at least one owning Ptn0Partition object will be returned in the
            map.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """An object of ServiceData for any error information."""

class MappedPartitionStruct:
    """
    
            The structure contains the map between input Ptn0Partition objects and their
            corresponding mapped Ptn0Partition objects.
            
    """
    def __init__(self, ) -> None: ...
    OwningPartitionToMappedPartitionsMap: System.Collections.Hashtable
    """
            The map (Ptn0Partition/list of Ptn0Partition) of input Ptn0Partition
            objects and corresponding mapped Ptn0Partition objects.
            """

class OwningPartitionStruct:
    """
    
            The structure contains the map between input Ptn0Partition objects and their
            corresponding owning Ptn0Partitions objects.
            
    """
    def __init__(self, ) -> None: ...
    TargetPartitionToOwningPartitionsMap: System.Collections.Hashtable
    """
            The map (Ptn0Partition/list of Ptn0Partition) of input Ptn0Partition
            objects and corresponding owning Ptn0Partition  objects.
            """

class UnmapPartitionsInputData:
    """
    
            Contains the list of owning Ptn0Partition objects, target Ptn0Partition
            objects and an Mdl0ApplicationModel object.
            
    """
    def __init__(self, ) -> None: ...
    OwningPartitions: list[Teamcenter.Soa.Client.Model.Strong.Ptn0Partition]
    """The list of owning Ptn0Partitions objects for which mappings needs to be removed."""
    TargetPartitions: list[Teamcenter.Soa.Client.Model.Strong.Ptn0Partition]
    """
            The list of target Ptn0Partitions objects to be unmapped from the corresponding
            owning Ptn0Partition object.
            """
    AppModelReference: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """
Mdl0ApplicationModel object containing the owning and target Ptn0Partition
            objects.
            """

class PartitionManagement:
    """
    Interface PartitionManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetMappedPartitions(self, OperationInput: list[GetMappedPartitionsInputData]) -> GetMappedPartitionsResponse:
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
    def GetOwningPartitions(self, OperationInput: list[GetOwningPartitionsInputData]) -> GetOwningPartitionsResponse:
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
    def UnmapPartitions(self, OperationInput: list[UnmapPartitionsInputData]) -> Teamcenter.Soa.Client.Model.ServiceData:
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

