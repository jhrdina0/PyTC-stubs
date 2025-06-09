import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class AttributeValue2:
    """
    Structure for each classification object attribute value.
    """
    def __init__(self, ) -> None: ...
    AttributeID: int
    """ID of the attribute."""
    AttributeName: str
    """Name of the attribute."""
    AttributeValues: list[str]
    """The values of the attribute."""
    Unit: str
    """The unit of the attribute."""

class ClassificationObjectInfo:
    """
    Structure containing classification object information.
    """
    def __init__(self, ) -> None: ...
    IcoClassId: str
    """The classification class Id."""
    IcoID: str
    """The classification object Id."""
    UnitBase: str
    """A class unit system of measure."""
    ClassifiedObjectUID: str
    """Classified WorkspaceObject object UID."""
    IcoAttributeValues: list[AttributeValue2]
    """Attribute list of this classification object."""
    IcoClassName: str
    """The class name in which the ICO is classified."""
    IcoType: int
    """
            The type of the ICO. Possible values are:
            

            0 - default ICO,
            
            1 - generic and
            
            2 - for a need ICO.
            

            Generic and Need type are added to support Piping and Instrumentation diagram application.
            
            Compared to default type, the visibility of these objects to the client is controlled
            by preferences (ICS_hidden_ico_types and ICS_support_generic_and_need).
            """

class GetLogicalObjectInput2:
    """
    
            Holds the list of the root object instances and the logical type name to retrieve
            the matched logical object instances.
            
    """
    def __init__(self, ) -> None: ...
    RootObjects: list[RootObject]
    """A list of root object instances."""
    LoTypeName: str
    """
            Name of the logical object type for which the logical object instances are to be
            searched for. The logical object type name corresponds to the name of any subtype
            of Fnd0LogicalObject.
            """

class GetLogicalObjectOutput2:
    """
    
            Holds the list of the retrieved logical object instances and related classification
            objects. Size of logicalObjectsOutput is equal to the input rootObjects attribute
            of input structure GetLogicalObjectInput2.
            
    """
    def __init__(self, ) -> None: ...
    LogicalObjectsOutput: list[LogicalObjectOutput2]
    """A list of the retrieved logical object instances."""

class GetLogicalObjectResponse2:
    """
    
            Holds the list of the retrieved logical object along with classification object output
            response and partial errors.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Returned service data."""
    LoOutputs: list[GetLogicalObjectOutput2]
    """
            A list of the retrieved logical object output response corresponding to a  logical
            object input.
            """
    ClassificationObjectInfo: System.Collections.Hashtable
    """
            A map (string, classificationObjectInfo) of the ICO Ids and their class attribute
            info.
            """

class LogicalObjectInstance:
    """
    Holds the logical Object instance and its root and member's classification objects.
    """
    def __init__(self, ) -> None: ...
    LoInstance: Teamcenter.Soa.Client.Model.ModelObject
    """An instance of the Fnd0LogicalObject."""
    MemberClassificationObjects: list[MemberClassificationObject2]
    """Logical Object instance's root and member name and its classification object information."""

class LogicalObjectOutput2:
    """
    
            This structure contains the logical object instance for a given root object given
            in input structure RootObject.
            
    """
    def __init__(self, ) -> None: ...
    Root: Teamcenter.Soa.Client.Model.ModelObject
    """
            An instance of the root Object. This is same object which is provided in input structure
            RootObject.
            """
    LogicalObjectInstances: list[LogicalObjectInstance]
    """
            A list of logical object instances. Only one logical object instance is returned
            for a given root object in the current implementation.
            """

class MemberClassificationObject2:
    """
    Contains member or root name and its classification object information.
    """
    def __init__(self, ) -> None: ...
    MemberOrRootName: str
    """The internal name of the member or the root on the Logical Object Type."""
    IcoIDs: list[str]
    """A list of ICO UIDs."""

class RootObject:
    """
    
            Holds the root object instance and its client id to retrieve the matched logical
            object instance.
            
    """
    def __init__(self, ) -> None: ...
    Root: Teamcenter.Soa.Client.Model.ModelObject
    """
            A root object instance. Persistent types are the only supported business objects
            for a root object.
            """
    ClientID: str
    """
            Client Id for the root object. This helps in uniqely mapping the input and output
            data.
            """

class LogicalObject:
    """
    Interface LogicalObject
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetLogicalObjects2(self, LoInputs: list[GetLogicalObjectInput2]) -> GetLogicalObjectResponse2: ...

