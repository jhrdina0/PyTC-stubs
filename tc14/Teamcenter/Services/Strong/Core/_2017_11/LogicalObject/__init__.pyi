import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class AttrDescriptor:
    """
    Structure containing map of class attribute descriptors.
    """
    def __init__(self, ) -> None: ...
    AttributeDescMap: System.Collections.Hashtable
    """The map of the attribute descriptors."""

class AttributeValue:
    """
    Structure for each ICO attribute value.
    """
    def __init__(self, ) -> None: ...
    AttrValue: str
    """The value of the attribute."""
    Unit: str
    """The unit of the attribute."""
    Locale: str
    """The locale for this attribute."""

class AttributeValues:
    """
    Contains values for ICO attributes and a boolean to check whether attribute is valid.
    """
    def __init__(self, ) -> None: ...
    IsAttributeValid: bool
    """A flag to indicate whether the attribute is valid."""
    Values: list[AttributeValue]
    """A list of values for this attribute."""

class ClassAttrDescriptor:
    """
    Structure representing Class attribute description.
    """
    def __init__(self, ) -> None: ...
    Id: str
    """An attribute id."""
    Name: str
    """An attribute name."""
    ShortName: str
    """An attribute short name."""
    Descripton: str
    """An attribute description."""
    Annotation: str
    """An attribute annotation."""
    ArraySize: int
    """An attribute array size."""
    Options: int
    """An attribute options."""
    MetricFormat: int
    """An attribute metric format."""
    MetricUnit: str
    """An attribute metric unit."""
    MetricDefaultValue: str
    """An attribute metric default value."""
    MetricMinValue: str
    """An attribute metric min value."""
    MetricMaxValue: str
    """An attribute metric max value."""
    NonMetricFormat: int
    """An attribute non metric format."""
    NonMetricUnit: str
    """An attribute non metric format."""
    NonMetricDefaultValue: str
    """An attribute non metric default value."""
    NonMetricMinValue: str
    """An attribute non metric min value."""
    NonMetricMaxValue: str
    """An attribute non metric max value."""
    ExtendedProps: list[ExtendedProperties]
    """The extended properties."""

class ClassAttributeInfo:
    """
    Structure containing classification object information.
    """
    def __init__(self, ) -> None: ...
    ClassId: str
    """The classification class Id."""
    AttributeValuesMap: System.Collections.Hashtable
    """The class attributes map."""
    UnitBase: str
    """A class unit system of measure."""
    ClassifiedObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Reference of the classified WorkspaceObject object. This can be a NULLTAG if it is
            a standalone ICO.
            """

class ExtendedProperties:
    """
    Extended metadata properties for an attribute.
    """
    def __init__(self, ) -> None: ...
    PropertyName: str
    """An extended property name."""
    PropertyValue: list[str]
    """The extended property values."""

class GetLogicalObjectInput:
    """
    
            Holds the list of the root object instances and the logical type name to retrieve
            the matched logical object instances.
            
    """
    def __init__(self, ) -> None: ...
    RootObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of root object instances. Persistent types are the only supported business
            objects for a root object.
            """
    LoTypeName: str
    """
            Name of the logical object type for which the logical object instances are to be
            searched for. The logical object type name corresponds to the name of any subtype
            of Fnd0LogicalObject.
            """

class GetLogicalObjectOutput:
    """
    Holds the list of the retrieved logical object instances.
    """
    def __init__(self, ) -> None: ...
    LogicalObjects: list[LogicalObjectOutput]
    """A list of the retrieved logical object instances."""

class GetLogicalObjectResponse:
    """
    Holds the list of the retrieved logical object output response and partial errors.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Returned service data."""
    LoOutputs: list[GetLogicalObjectOutput]
    """
            A list of the retrieved logical object output response corresponding to a  logical
            object input.
            """
    ClassificationAttributeDesc: System.Collections.Hashtable
    """A map of classification objects and a list of references to their attribute descriptors."""
    ClassificationObjectInfo: System.Collections.Hashtable
    """A map of the ICO ids and their class attribute info."""

class LogicalObjectOutput:
    """
    
            This structure contains the logical object instance and its related classification
            objects information.
            
    """
    def __init__(self, ) -> None: ...
    Root: Teamcenter.Soa.Client.Model.ModelObject
    """An instance of the root object."""
    LogicalObjectInstances: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of logical object instances. Only one logical object instance is returned
            for a given root object in the current implementation.
            """
    MemberClassificationObjects: list[MemberClassificationObject]
    """A list of  MemberClassificationObject objects."""

class MemberClassificationObject:
    """
    Contains classification object information.
    """
    def __init__(self, ) -> None: ...
    MemberOrRootName: str
    """The internal name of the member or the root."""
    IcoIDs: list[str]
    """A list of ICO ids."""

class LogicalObject:
    """
    Interface LogicalObject
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetLogicalObjects(self, LoInputs: list[GetLogicalObjectInput]) -> GetLogicalObjectResponse: ...

