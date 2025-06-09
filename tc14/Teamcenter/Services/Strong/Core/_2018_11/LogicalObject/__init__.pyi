import System
import System.Collections
import Teamcenter.Services.Strong.Core._2018_06.LogicalObject
import Teamcenter.Soa.Client.Model
import typing

class GetLogicalObjectInput3:
    """
    
            The structure holds:
            
            1.Â Â Â Â A list of RootObject(s) structures which represents client
            id and root object instance pair.
            
            2.Â Â Â Â A logical type name.
            
            3.Â Â Â Â A map containing the included logical object ID, or member
            ID and configuration context UID.
            

            Above input data are used to retrieve the matched logical object instances and their
            configured included logical object instances.
            
    """
    def __init__(self, ) -> None: ...
    RootInstances: list[Teamcenter.Services.Strong.Core._2018_06.LogicalObject.RootObject]
    """A list of root instance structures."""
    LoTypeName: str
    """
            Name of the logical object type for which the logical object instances are to be
            searched for. The logical object type name corresponds to the name of any subtype
            of Fnd0LogicalObject.
            """
    LoQueryNameValues: System.Collections.Hashtable
    """
            A map (string, string) of the Included Logical Object ID, or member ID and its Configuration
            Context UID.
            """

class GetLogicalObjectOutput3:
    """
    
            The structure holds the list of the retrieved logical object instances, related classification
            objects and included logical object instances.
            
    """
    def __init__(self, ) -> None: ...
    LogicalObjectsOutput: list[LogicalObjectOutput3]
    """
            A list of the retrieved logical object instances. The length of this member is equal
            to the length of the input rootInstances member of the input structure GetLogicalObjectInput3.
            """

class GetLogicalObjectResponse3:
    """
    
            The structure holds the list of the retrieved logical object instances along with
            classification object output response and partial errors.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Returned service data."""
    LoOutputs: list[GetLogicalObjectOutput3]
    """
            A list of the retrieved logical object output response corresponding to a  logical
            object input.
            """
    ClassificationObjectInfo: System.Collections.Hashtable
    """
            A map(string, ClassificationObjectInfo)  of the ICO IDs and their classification
            object info.
            """

class LogicalObjectInstance2:
    """
    
            The structure holds the logical object instance, its root, its members and its classification
            objects. The structure also holds the data for included logical object instances.
            
    """
    def __init__(self, ) -> None: ...
    LoInstance: Teamcenter.Soa.Client.Model.ModelObject
    """An instance of the Logical Object Type."""
    MemberClassificationObjects: list[Teamcenter.Services.Strong.Core._2018_06.LogicalObject.MemberClassificationObject2]
    """
            A list of structures containing classification object data for the root or member
            of the Logical Object Type.
            """
    IncludedLOInstances: System.Collections.Hashtable
    """The included Logical Object instances."""

class LogicalObjectOutput3:
    """
    The structure contains the logical object instances for a given root object.
    """
    def __init__(self, ) -> None: ...
    Root: Teamcenter.Soa.Client.Model.ModelObject
    """
            An instance of the root object. This is same object which was provided in input RootObject
            structure.
            """
    LogicalObjectInstances: list[LogicalObjectInstance2]
    """
            A list of logical object instances. Only one logical object instance is returned
            for a given root object in the current implementation.
            """

class LogicalObject:
    """
    Interface LogicalObject
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetLogicalObjectsWithContext(self, LoInputs: list[GetLogicalObjectInput3]) -> GetLogicalObjectResponse3: ...

