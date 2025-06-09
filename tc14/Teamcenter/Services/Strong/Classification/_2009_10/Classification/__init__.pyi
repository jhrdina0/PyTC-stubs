import System
import System.Collections
import Teamcenter.Services.Strong.Classification._2007_01.Classification
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttributeConfiguration:
    """
    Holds the configuration attached to an attibute
    """
    def __init__(self, ) -> None: ...
    PreConfig: str
    """Preconfiguration attached to the attribute"""
    Config: str
    """Base configuration attached to the attribute."""
    PostConfig: str
    """
            Post configuration attached to the attribute.Configurations could be any combinations
            of the following individual configurations:
            

multifield
            
horizontal
            
vertical
            
separator
            
arrow
            
button
            
wide
            
mandatory flag
            
protected flag
            
unique flag
            

"""

class AutoComputeAttribute:
    """
    Contains the attributes that are used for the auto compute operation.
    """
    def __init__(self, ) -> None: ...
    Values: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.ClassificationPropertyValue]
    """
            List of references to the ClassificationPropertyValue
            structures that will hold the values (single or multiple values) for the Attribute
            represented by this AutoComputeAttribute.
            """
    UnitName: str
    """Display unit name for this attribute."""
    Length: int
    """
            Length of an Attribute. This field will hold the number of values for this Attribute.
            

For a single valued attribute, length = 1
            
For an array type of attribute, length = n [where n is the size of
            the array.]
            

"""
    AttributeProperties: int
    """
            Represents the Attribute property flags concatenated into a single Integer value.
            
            To access  individual flag, a bitwise operation will need to be performed by the
            Client.
            
            Valid values are as specified in the enum AutoComputeAttrPropertyFlags.
            """
    IsModified: bool
    """
            Flag to indicate whether the attribute referenced by this AutoComputerAttribute
            structure is modified by the client. It is only used when AutoComputeAttribute
            structure is used as an Input parameter to the autoComputeAttributes
            operation. This parameter is should not be used by clients when reading the AutoComputeAttribute structure as part of
            the  returned AutoComputeAttributesResponse.
            """

class AutoComputeAttributesResponse:
    """
    
            Contains the attribute values for the corresponding autocomputed attributes after
            the autocompute operation is called. The structure element is a key,value pair of
            attribute IDs and their corresponding attribute properties. The attribute properties
            of type AutoComputeAttribute  contains the following information:
            

values : This structure element of type ClassificationPropertyValue
            holds the classification properties for the classification object
            
length : the number of attributes computed
            
unitName : the unit of measure for the attribute
            
attributeProperties : Properties of the attributes
            
isModified : Boolean value to check if attribute is modified
            


    """
    def __init__(self, ) -> None: ...
    AutoComputedAttrs: System.Collections.Hashtable
    """
            Map containing references of the AutoComputeAttribute
            structures with their respective attribute IDs.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failures with classification object ID mapped to the error message in the ServiceData
            list of partial errors.
            """

class FormatProperties:
    """
    Structure representing format details
    """
    def __init__(self, ) -> None: ...
    Format: Teamcenter.Services.Strong.Classification._2007_01.Classification.AttributeFormat
    """
            References the AttributeFormat structure
            holding the format definition for this attribute.
            """
    UnitName: str
    """Unit display name associated with this attribute in this unit system."""
    DefaultValue: str
    """
            Default value of this Class attribute. This can be an empty string indicating no
            default value.
            """
    MinimumValue: str
    """
            Minimum value constraint of this Class attribute. This can be an empty string indicating
            no minimum value constraint.
            
Note: Only applicable to numerical formats of attributes
            """
    MaximumValue: str
    """
            Maximum value contraint of this Class attribute. This can be an empty string indicating
            no maximum value constraint.
            
Note: Only applicable to numerical formats of attributes
            """

class ClassAttribute2:
    """
    Structure representing class attribute details.
    """
    def __init__(self, ) -> None: ...
    Id: int
    """ID for this attribute."""
    Name: str
    """Name for this attribute."""
    ShortName: str
    """Short name defined for this attribute."""
    Description: str
    """Description added for this attribute."""
    MetricFormat: FormatProperties
    """
            References the FormatProperties structure
            defining the metric format of this attribute.
            """
    NonMetricFormat: FormatProperties
    """
            References the FormatProperties structure
            defining the nonmetric format of this attribute.
            """
    Annotation: str
    """Annotation information added to this attribute."""
    AttributeConfiguration: AttributeConfiguration
    """
            Reference the AttributeConfiguration
            structure that defines any additional configuration for this attribute.
            """
    ArraySize: int
    """
            Array size or the number of values for this attribute.
            

If single valued (nonarray), then arraySize
            = 1
            
If multi valued (array), then arraySize
            >= 1 corresponding to the size of the array defined in the attribute definition.
            

"""
    Options: int
    """
            Attribute property flags represented as a single integer. To access individual property
            flags, a bitwise operation will be required by the client.Valid values are:
            

ATTR_vla         
            = (1 << 0)
            
ATTR_external_vla      = (1 << 1)
            
ATTR_mandatory         = (1 << 2)
            
ATTR_protected             = (1 << 3)
            
ATTR_unique        
            = (1 << 4)
            
ATTR_propagated         = (1 << 5)
            
ATTR_localValue             = (1 << 6)
            
ATTR_reference             = (1 << 7)
            
ATTR_auto_computed = (1 << 15)
            
ATTR_hidden        
            = (1 << 20)
            
ATTR_localizable         = (1
            

"""
    ExtendedProperties: list[ExtendedProeprty]
    """
            List of references to the ExtendedProeprty structure holding the extended metadata
            properties of this attribute.
            """

class ExtendedProeprty:
    """
    This Structure represents extended metadata property.
    """
    def __init__(self, ) -> None: ...
    PropertyName: str
    """Name of the extended metadata property associated to the given attribute."""
    Values: list[ExtendedPropertyValues]
    """
            List of references to the ExtendedPropertyValues
            structure holding actual values of the Extended metadata properties.
            """

class ExtendedPropertyValues:
    """
    This structure is used to hold extended metadata property values
    """
    def __init__(self, ) -> None: ...
    Value: str
    """Values of the Extended metadata property associated to a Classification Attribute."""

class GetAttributesForClassesResponse2:
    """
    Holds the values returned by getAttributesForClass2()
    """
    def __init__(self, ) -> None: ...
    Attributes: System.Collections.Hashtable
    """Map of Class IDs and the Class attributes found for each of those classes."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failure will be returned with Class ID mapped to the error message in the ServiceData
            list of partial errors.
            """

class GetKeyLOVsResponse2:
    """
    
            Holds the keylovs returned by the getKeyLOVs2() method.
            
    """
    def __init__(self, ) -> None: ...
    KeyLOVs: System.Collections.Hashtable
    """Map of KeyLOV definitions details."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failure will be returned with Key-LOV ID mapped to the error message in the ServiceData list of partial errors
            """

class KeyLOVDefinition2:
    """
    Structure representing KeyLOVDefinition
    """
    def __init__(self, ) -> None: ...
    Id: str
    """
            Unique Key-LOV ID. This is a negative number.This can be found in the Key/ID field
            of a Key-LOV definition in the Key-LOV tab of Classification Administration.
            """
    Name: str
    """Name of the Key-LOV."""
    KeyLovtag: Teamcenter.Soa.Client.Model.ModelObject
    """Unused parameter. Reserved for future use"""
    Options: int
    """
            Key-LOV options to Show/Hide keys.Valid values are:
            

0 = Show key
            
1 = Hide key
            

"""
    KeyLovEntries: list[KeyLOVEntry]
    """List of Key-LOV entries."""
    OwningSite: Teamcenter.Soa.Client.Model.ModelObject
    """Owning Site (POM_imc)."""
    SharedSites: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            List of sites (POM_imc) where this Key-LOV is to be shared using Multisite
            operations.
            """

class KeyLOVEntry:
    """
    Structure representing KeyLOVEntry
    """
    def __init__(self, ) -> None: ...
    LovKey: str
    """String representing a Key of a Key-LOV entry."""
    LovValue: str
    """String representing a Value  of the Key-LOV  entry."""
    DeprecatedSatus: bool
    """Flag indicating whether this particular Key-LOV entry is deprecated or not."""

class Classification:
    """
    Interface Classification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateKeyLOVs(self, KeyLOVsInput: list[KeyLOVDefinition2]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation creates or updates  the key-LOV objects based on the input such as
             name, id etc., if the input ID matches that of an existing key-LOV, it will be updated.
             Else new key-LOV object will be created. A key-LOV is a list of values used in classification.
             The key-LOVs are used to define one or more values that can be set for classification
             dictionary attributes
             

             Typical format of a Key-LOV



                 <key-LOV ID>:<key-LOV Name>
             
                 <Key10>:<Value10>
             
                 <Key20>:<Value20>
             

             Example of a Key-LOV:



             -33381 : Design Categories
             
                 Des1 : Bearing
             
                 Des2 : Bracket
             
                 Des3 : Frame
             
                 Des4 : LeadBox
             


Use Cases:

             User wants to create new key-LOVs to be used with classification or need to update
             the existing ones in classification.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param KeyLOVsInput: 
                         List of structure that contains information of the key-LOV that needs to be updated
                         or created.
             
        :return: list of partial errors.
        """
        ...
    def GetAttributesForClasses2(self, ClassIds: list[str]) -> GetAttributesForClassesResponse2:
        """    
             Provides information on class attributes for the classification classes based on
             input classification class ids. Detailed information about class attributes is provided
             & includes class attribute name, description, format, unit system, minimum/maximum
             value, configuration set & extended properties.
             

Use Cases:

             When user wants to view details of all class attributes associated with a classification
             class. The method is similar to getAttributesForClasses()
             method, but provides information in a slightly different format. Also additional
             information like that on the extended properties of class attributes is provided
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClassIds: 
                         Identifier for the classification class whose attribute information is requested.
             
        :return: 
        """
        ...
    def GetKeyLOVs2(self, KeyLOVIds: list[str]) -> GetKeyLOVsResponse2:
        """    
             Gets the information for classification key-LOVs  based on given ID(s). Information
             such as key-LOV's name, display options, owning site, shared sites, deprecation status
             and key and value entries can be obtained. A key-LOV is a list of values used in
             classification. The key-LOVs are used to define one or more values that can be set
             for classification dictionary attributes
             

             Typical format of a Key-LOV -
             

                 <key-LOV ID>:<key-LOV Name>
             
                 <Key10>:<Value10>
             
                 <Key20>:<Value20>
             

             Example of a KeyLOV:
             

             - 33381:Design Categories
             
                 Des1:Bearing
             
                 Des2:Bracket
             
                 Des3:Frame
             
                 Des4:LeadBox
             

Use Cases:

             User wants to retrieve the information for an existing key-LOV using the key-LOV's
             unique identifier. This operation is similar to getKeyLOVs()operation, but provides more detailed information
             about the required key-LOV.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param KeyLOVIds: 
                         List of IDs of classification key-LOV, for which information is required. The key-LOV
                         ID is a unique negative integer that identifies a key-LOV. In the Teamcenter rich
                         client, key-LOVs can be accessed in the "Key LOVs" tab of the Classification Administration
                         application. The key-LOV ID can be found in the "Key/ID" field of a key-LOV definition
                         there.
             
        :return: 
        """
        ...
    def AutoComputeAttributes(self, IcoId: str, Wso: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject, ClassId: str, ViewId: str, InputAttrs: System.Collections.Hashtable, UnitSystem: int, Mode: int) -> AutoComputeAttributesResponse:
        """    
             Computes the attribute values  of classification object based on other attribute
             values within the same object or an associated classification view. Or the value
             can be computed based on attribute values of the object being classified. A classification
             object is also called ICO.
             

Use Cases:

             User need to automatically compute classification attribute values for attributes
             marked as 'AutoComputed'. The values can be computed based on - other attribute values
             belonging to same classification object or an associated classification view or attribute
             values of the object being classified.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param IcoId: 
                         Unique ID of classification objects (ICOs) whose attributes are being computed.
             
        :param Wso: 
                         The workspace object  that is being classified. This input is optional and a NULL
                         value can be specified. A NULL value indicates that there is no workspace object
                         associated with classification object corresponding to input icoId
             
        :param ClassId: 
                         Unique Id of classification class, in which classification object(ICO) is created/workspace
                         object is classified.
             
        :param ViewId: 
                         Unique ID of a classification view that is associated to a classification class,
                         under which input ICO is created/input workspace object is classified.
             
        :param InputAttrs: 
                         Input attributes map with values and properties along with a flag indicating whether
                         the attribute value has changed.
             
        :param UnitSystem: 
<ul>
<li type="disc">0 = Metric
                         </li>
<li type="disc">1 = Nonmetric
                         </li>
</ul>

        :param Mode: 
                         If the mode is specified as load mode, then attribute properties (mandatory, read-only,
                         unique, propogated or hidden) are computed. Else both the attribute properties &amp;
                         values are computed
             
        :return: 
        """
        ...

