import System
import System.Collections
import Teamcenter.Services.Strong.Classification._2009_10.Classification
import Teamcenter.Soa.Client.Model
import typing

class ClassAttribute3:
    """
    The structure representing class attributes.
    """
    def __init__(self, ) -> None: ...
    ClassAttributeProperty: Teamcenter.Services.Strong.Classification._2009_10.Classification.ClassAttribute2
    """A structure representing Class attribute details."""
    DependencyAttribute: str
    """The dependency attribute property of this attribute."""
    DependencyConfiguration: str
    """The dependency configuration property of this attribute."""

class ClassAttributesDefinition:
    """
    
            The structure containing list of Classification class attributes definition and configured
            KeyLOV (Stxt) definition.
            
    """
    def __init__(self, ) -> None: ...
    AttributeDefinitionMap: System.Collections.Hashtable
    """A map of attribute ID and attribute definition pairs (int/ClassAttribute3)."""
    ConfiguredKeyLOVDefinitionMap: System.Collections.Hashtable
    """
            A map of attribute ID and KeyLOV definition pairs (int/KeyLOVDefinition2), based
            on dependency configuration of an attribute.
            """

class GetClassDefinitionsResponse:
    """
    Holds the values returned by getClassDefinitions operation.
    """
    def __init__(self, ) -> None: ...
    ClassDefinitionMap: System.Collections.Hashtable
    """A map of Classification class or view ID and its corresponding definition pairs (string/ClassDef)."""
    ClassAttributesDefinitionMap: System.Collections.Hashtable
    """A map of Classification class or view ID and its definition pairs (string/ClassAttributesDefinition)."""
    KeyLOVDefinitionMap: System.Collections.Hashtable
    """A map containing the used Classification KeyLOVs and its definitions (string ID/KeyLOVDefinition2)."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Any failures will be returned in the service data list of partial errors."""

class Classification:
    """
    Interface Classification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetClassDefinitions(self, ClassIDs: list[str]) -> GetClassDefinitionsResponse:
        """    
             This operation returns Classification class definition, its attribute definitions
             including the details of associated Classification KeyLOV (Stxt) objects.
             

Use Cases:

             User wants to get details of classification class along with all associated class
             attributes. This operation is combination of getClassDescriptions and getAttributesForClasses2,
             but provides information in a different format to cater additional information like
             extended properties, attribute dependency and KeyLOVs (Stxt)  associated to
             class attributes.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClassIDs: 
                         A list of Classification class IDs.
             
        :return: 
        """
        ...

