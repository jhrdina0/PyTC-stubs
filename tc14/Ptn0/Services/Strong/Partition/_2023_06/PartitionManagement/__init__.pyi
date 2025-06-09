import Ptn0.Services.Strong.Partition._2020_12.PartitionManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetMembersInBOMWindowBulkInputInfo2:
    """
    
            GetMembersInBOMWindowBulkInputInfo2 structure represents the details of expansion
            context object, PartitionInfo structure and expandOptions.
            
    """
    def __init__(self, ) -> None: ...
    ScopeLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
BOMLine object that will provide the scope for expansion of input Partitions.
            The BOMLine provided can be the top line of a BOMWindow (when an Assembly or Product
            is opened) or a Subset line (when a Workset is opened).
            """
    PartitionInfo: list[Ptn0.Services.Strong.Partition._2020_12.PartitionManagement.PartitionInfo]
    """
            A list of PartitionInfo structure containing clientID and Ptn0Partition
            objects.
            """
    ExpandOptions: System.Collections.Hashtable
    """
            A map (string, string) of expand options and its value. It is used to provide additional
            options for expanding Partitions (e.g., additionally return members for all child
            Partitions)
            
            key = "includeChildrenPartition" possible values = "oneLevel", "allLevels"
            """

class GetMembersInBOMWindowOutputInfo2:
    """
    
            GetMembersInBOMWindowOutputInfo2 structure contains the following two maps to return
            children partitions and members of the input partitions.
            

A map (Ptn0Partition, Ptn0Partition) of input partition
            and its children partitions.
            
A map (Ptn0Partition, BOMLine) of input partition and
            its member BOM lines.
            


    """
    def __init__(self, ) -> None: ...
    ChildrenPartitions: System.Collections.Hashtable
    """
            A map (Ptn0Partition, Ptn0Partition) of input partition and its children
            partitions.
            """
    PtnToMembers: System.Collections.Hashtable
    """
            A map (Ptn0Partition, BOMLine) of input partition and its member BOM
            lines.
            """

class GetMembersInBOMWindowResponse2:
    """
    
            Contains a list of GetMembersInBOMWindowOutputInfo2 object and serviceData structures.
            Input Ptn0Partition object information along with their children partitions
            and members are returned via GetMembersInBOMWindowOutputInfo2 object. If the input
            parameters are invalid, the errors are returned in the serviceData.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: list[str]
    """A list of Identifiers that helps the client track the Ptn0artition objects."""
    Output: list[GetMembersInBOMWindowOutputInfo2]
    """
            A list of GetMembersInBOMWindowOutputInfo2 objects for corresponding list of input
            GetMembersInBOMWindowInputInfo2 object.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains the list of all BusinessObject objects that make up the output, as well
            as any errors that might have occurred as part of the service invocation.
            """

class PartitionManagement:
    """
    Interface PartitionManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetMembersInBOMWindow2(self, Input: list[GetMembersInBOMWindowBulkInputInfo2]) -> GetMembersInBOMWindowResponse2: ...

