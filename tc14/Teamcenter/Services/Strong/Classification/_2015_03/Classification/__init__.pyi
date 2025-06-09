import System
import Teamcenter.Services.Strong.Classification._2009_10.Classification
import Teamcenter.Soa.Client.Model
import typing

class DependencyAttributeStruct:
    """
    
            The structure containing class ID, the changed attribute ID, its value and all other
            UI attribute IDs and corresponding values.
            
    """
    def __init__(self, ) -> None: ...
    ClassID: str
    """The unique ID of Classification class."""
    SelectedAttributeID: int
    """The unique ID of an attribute (from above class) whose UI value is changed."""
    SelectedValue: str
    """
            The user selected value of the attribute (key of the selected entry from the KeyLOV).
            This could be empty if the value has been deselected.
            """
    AttributeValues: list[DependencyAttributeValue]
    """
            A list of DependencyAttributeValue objects containing attribute IDs and their corresponding
            values for all other UI attributes from above class.
            """

class DependencyAttributeValue:
    """
    Structure containing the attribute ID and corresponding value.
    """
    def __init__(self, ) -> None: ...
    AttributeID: int
    """Unique ID of an attribute."""
    Value: str
    """The UI value for above attribute (the key of a KeyLOV entry in case of KeyLOV attribute)."""

class DependencyKeyLOVDescriptor:
    """
    Structure representing dependent attribute IDs and corresponding key-value pairs.
    """
    def __init__(self, ) -> None: ...
    AttributeID: int
    """The unique ID of the changed attribute."""
    SelectedKeys: list[str]
    """A list of unique key of to be selected entry for this attribute (can be empty)."""
    KeyLOVDefinition: Teamcenter.Services.Strong.Classification._2009_10.Classification.KeyLOVDefinition2
    """The structure representing the configured KeyLOV definition for attribute."""

class GetDependencyKeyLOVsResponse:
    """
    Holds the values returned by getKeyLOVsForDependentAttributes operation.
    """
    def __init__(self, ) -> None: ...
    DependencyKeyLOVs: list[DependencyKeyLOVDescriptor]
    """
            A list containing attribute ID, key of to be selected entry from a KeyLOV and its
            KeyLOV definition for each to be changed attribute.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Any failures will be returned in the service data list of partial errors."""

class Classification:
    """
    Interface Classification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetKeyLOVsForDependentAttributes(self, DependencyAttributeStruct: list[DependencyAttributeStruct]) -> GetDependencyKeyLOVsResponse:
        """    
             This operation returns the Classification KeyLOV (stxt) definitions based
             on the dependency settings on class or view attributes.
             

Use Cases:

             If a user changes the value for any attribute in a dependency chain while working
             in a class containing interdependent KeyLOV (stxt) attributes, the other dependent
             attributes should get configured KeyLOV structures and potential auto populated value.
             

             This operation is used to get the value and the KeyLOV definition for the dependent
             KeyLOV attributes.
             
             Consider a class containing two interdependent KeyLOV attributes
             
             Country
             
                 United States
             
                 Canada
             
             State
             
                 Ohio
             
                 California
             
                 Ontario
             
                 Quebec
             

If a user first selects the value for Country attribute say "United
             States" the State attribute will only show states belonging "United States".
             
If a user first selects the value for State attribute say "Ohio";
             value for Country attribute will be auto populated to "United States". Now, if a
             user deselects the value for Country attribute; the value for State attribute gets
             deselected as well.
             



Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param DependencyAttributeStruct: 
                         List of structure containing class ID, the changed attribute ID, its value and all
                         other UI attribute IDs and corresponding values.
             
        :return: 
        """
        ...

