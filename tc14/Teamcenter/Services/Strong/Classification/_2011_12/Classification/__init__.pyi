import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class AttrDescriptor:
    """
    Structure containing map of class attribute descriptors.
    """
    def __init__(self, ) -> None: ...
    AttrDescMap: System.Collections.Hashtable
    """Map of attribute descriptors."""

class AttributeValues:
    """
    Contains values for ico attributes and boolean to check whether attribute is valid.
    """
    def __init__(self, ) -> None: ...
    IsAttrValid: bool
    """Flag to indicate whethe the attribute is valid"""
    Values: list[Value]
    """List of values for this attribute"""

class ClassAttrDescriptor:
    """
    Structure representing Class attribute description.
    """
    def __init__(self, ) -> None: ...
    Id: int
    """An attribute id."""
    Name: str
    """An attribute name."""
    ShortName: str
    """An attribute shortName."""
    Description: str
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
    """An attribute non metric unit."""
    NonMetricDefaultValue: str
    """An attribute non metric default value."""
    NonMetricMinValue: str
    """An attribute non metric min value."""
    NonMetricMaxValue: str
    """An attribute non metric max value."""
    ExtendedProps: list[ExtendedProperties]
    """Extended properties."""

class ClassAttrInfo:
    """
    Structure containing classification object information.
    """
    def __init__(self, ) -> None: ...
    Cid: str
    """Classification class Id."""
    AttrValuesMap: System.Collections.Hashtable
    """Class attributes map"""
    UnitBase: str
    """Class unit system of measure."""
    IcoId: str
    """
            Reference of the classified WorkspaceObject
            object. This can be a NULLTAG if it is a standalone ICO.
            """
    WsoTag: Teamcenter.Soa.Client.Model.ModelObject
    """The tag of classifying WSO."""

class ClassificationInfoResponse:
    """
    Contains classification objects info returned by getClassificationObjectInfo() method.
    """
    def __init__(self, ) -> None: ...
    ClassificationObjectInfo: System.Collections.Hashtable
    """Map of classification objects and list of references to their class attributes."""
    ClassAttributeDesc: System.Collections.Hashtable
    """Map of classification objects and list of references to their attribute descriptors."""
    SvcData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failures with classification object ID mapped to the error message in the ServiceData list of partial errors.
            """

class ExtendedProperties:
    """
    Extended metadata properties for an attribute.
    """
    def __init__(self, ) -> None: ...
    PropName: str
    """An extended prop name."""
    PropValue: list[str]
    """Extended prop values."""

class Value:
    """
    structure for each ico attribute value.
    """
    def __init__(self, ) -> None: ...
    AttrValue: str
    """Value of the attribute"""
    Unit: str
    """Unit of the attribute."""
    Locale: str
    """Locale for this attribute."""

class Classification:
    """
    Interface Classification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetClassificationObjectInfo(self, IcoUids: list[str], AttributeIds: list[int], GetOptimizedValues: bool, FetchDescriptor: bool, Locale: str) -> ClassificationInfoResponse:
        """    
             Provides detailed information on classification objects based on their unique identifiers
             (UID). A classification object is also called an ICO
             

Use Cases:

             When user needs to get details of a classification object (ICO).  These details include
             the classification class to which ICO belongs, the unit system, ICO ID, various ICO
             attributes and their values and property descriptor for these attributes
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param IcoUids: 
                         Unique IDs of classification objects whose details are required
             
        :param AttributeIds: 
                         Unique Identifiers of classification attribute associated with input classification
                         object,  whose values are to be fetched
             
        :param GetOptimizedValues: 
                         Boolean flag to get optimized classification attribute values. When Teamcenter optimizes
                         an attribute value, it provides the most readable value with the least number of
                         leading or trailing zeros. For example, 1 km is easier to read than 1000 m
             
        :param FetchDescriptor: 
                         Boolean flag to indicate whether  property descriptor for each of class attributes
                         is to be fetched
             
        :param Locale: 
                         Locale in which classification objects attribute  values and properties descriptor
                         are to be fetched.
             
        :return: 
        """
        ...

