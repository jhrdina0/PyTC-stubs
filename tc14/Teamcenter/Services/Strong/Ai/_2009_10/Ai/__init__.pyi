import System
import Teamcenter.Services.Strong.Ai._2006_03.Ai
import Teamcenter.Services.Strong.Ai._2008_06.Ai
import typing

class ErrorMap:
    """
    
            capture the index of the input array, and the indices for the objects within that
            array.
            
    """
    def __init__(self, ) -> None: ...
    Index: int
    """index of the input array with the list of objects and configurations."""
    Indices: list[int]
    """Within the index specified by "index" the location of failed indices."""

class GetPropertyValuesData:
    """
    
            Used to input the list of objects with related configuration (used to setup bomwindows
            if needed on server), and the properties.
            
    """
    def __init__(self, ) -> None: ...
    Objs: list[Teamcenter.Services.Strong.Ai._2008_06.Ai.ObjectsWithConfig]
    """list of objects along with configuration."""
    Properties: list[str]
    """list of  properties to be queried for on the object."""

class GetPropertyValuesResponse:
    """
    
            capture the property values for the specified object and specified properties and
            any failures.
            
    """
    def __init__(self, ) -> None: ...
    ObjProps: list[ObjPropDetail]
    """the properties of the object"""
    FailedSetIndices: list[ErrorMap]
    """
            array of failed indices. The index is the position in the input array. And the indices
            member is the list of failed objects (invalid tags) at each such index.
            """

class ObjPropDetail:
    """
    capture the object ApplicationRef and it's property details.
    """
    def __init__(self, ) -> None: ...
    Obj: Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef
    """the ApplicationReference of the obj (uid/appname/version)"""
    Properties: list[PropertyDetails]
    """array or property details per"""
    FailedPropIndices: list[int]
    """
            index of the failed property for the object - the index maps to the input property
            array.
            """
    FailedPropMessages: list[str]
    """the error string corresponding to the error id in failedPropIndices."""

class PropertyDetails:
    """
    details of a property
    """
    def __init__(self, ) -> None: ...
    Name: str
    """display name of the property"""
    Values: list[str]
    """
            values in string form. Array - if the property has multiple values. These values
            can be decoded/parsed using the Property SOA client class if needed.
            """
    MaxStrLen: int
    """in case the property value is  a string - the maximum possible length."""
    Type: str
    """
            the type of the property as a string. integer = "int", short="short", float="float",
            double="double", char="char", logical="logical",note="note", string="string", date="date",
            any reference="reference"
            """
    Access: int
    """will be set to 0 if write access is allowed, 1 - for read."""
    Usage: str
    """if lov - the usage type of that lov."""
    LovValues: list[str]
    """the lovValues as strings."""
    NullElement: list[int]
    """for each value in an array - is the value Null."""
    EmptyElement: list[int]
    """Used to indicate if each element in an array(each value) is empty."""

class Ai:
    """
    Interface Ai
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPropertyValues(self, Input: list[GetPropertyValuesData]) -> GetPropertyValuesResponse:
        """    
             get the property values for the object supplied as ApplicationReferences and configuration.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Input: 
                         array of input structure - each of which specifies the object and configuration,
                         along with properties.
             
        :return: return the property values for the input properties and objects.
        """
        ...

