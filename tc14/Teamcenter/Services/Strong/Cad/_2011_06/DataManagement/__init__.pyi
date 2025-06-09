import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class PropDescriptor:
    """
    
            The PropDescriptor struct describes information
            about the Teamcenter property
            
    """
    def __init__(self, ) -> None: ...
    PropName: str
    """Name of the property"""
    DisplayName: str
    """Display name of the property. This is the localized name for the property."""
    DefaultValue: str
    """
            Default value for the property. This is also sometimes known as the initial value
            of the property
            """
    PropValueType: int
    """
            Value type for the property in integer form:
            
            PROP_untyped (0) No value
            
            PROP_char (1) Value is a single character
            
            PROP_date (2) Value is a date
            
            PROP_double (3) Value is a double
            
            PROP_float (4) Value is a float
            
            PROP_int (5) Value is an integer
            
            PROP_logical (6) Value is a logical
            
            PROP_short (7) Value is a short
            
            PROP_string (8) Value is a character string
            
            PROP_typed_reference (9) Value is a typed reference
            
            PROP_untyped_reference (10) Value is an untyped reference
            
            PROP_external_reference (11) Value is an external reference
            
            PROP_note (12) Value is a note
            
            PROP_typed_relation (13) Value is a typed relation
            
            PROP_untyped_relation (14) Value is an untyped relation
            """
    PropType: int
    """
            Type for the property in integer form:
            
            PROP_unknown (0) Property type is unknown
            
            PROP_attribute (1)  Based on a POM attribute (int, string, ...)
            
            PROP_reference (2)  Based on a POM reference
            
            PROP_relation (3) Based on an ImanRelation

            PROP_compound (4) Based on a property from another type
            
            PROP_runtime (5) Based on a computed value
            """
    IsDisplayable: bool
    """Boolean property indicating if the property should be displayed (true) or not (false)."""
    IsArray: bool
    """Specifies whether the property is an array or single value"""
    Lov: Teamcenter.Soa.Client.Model.Strong.ListOfValues
    """ListOfValues object attached to the property (if any)"""
    IsRequired: bool
    """Specifies whether the property is required"""
    IsEnabled: bool
    """Specifies whether the property is enabled"""
    IsModifiable: bool
    """Specifies whether the property is modifiable"""
    AttachedSpecifier: int
    """
            Attached specifier holds the following information:
            

Is it a hierarchical LOV attachment? If it is hierarchical LOV attachment,
            the specifier value is 0;  This value can be 0 in following cases:
            
    Standard LOV attachment (Combobox, Range
            etc)
            
    Value Ddescription attachment only ( specifier
            value is 0 for the value attachment )
            
    To check whether it is hierarchical or not,
            one needs to verify the children LOVs (value filters from LOV). If there are children
            LOVs then it could be a hierarchical LOV.
            
 Is it attached with interdependent?
            
bool isInterdependent = ( specifier & (1 << 1) ) != 0;
            
 Is it attached with description attachment?
            
bool  isDescriptionAttach = ( specifier & (1 << 1) )!=
            0;
            


            If attached with interdependent or description attachment what is the order of the
            attachment?
            
            int order = specifier >> 8;
            """
    MaxLength: int
    """Maximum length for a string property."""
    LovAttachmentsCategory: int
    """
            Defines categories of LOVs attached to the property.
            
            0:  No attachments
            
            1:  Only isTrue condition is attached
            
            2:  Only session based conditions are attached
            
            3:  One or more object based conditions are attached
            
"""
    InterdependentProps: list[str]
    """Interdependent properties for interdependent LOVs."""

class AttrMappingInfo:
    """
    Attribute mapping information.
    """
    def __init__(self, ) -> None: ...
    CadAttrMappingDefinition: Teamcenter.Soa.Client.Model.Strong.CadAttrMappingDefinition
    """The CadAttrMappingDefinition object reference representing the mapping definition."""
    PropDesc: PropDescriptor
    """
            The property descriptor structure containing property information for the mapping
            definition property.
            """

class GetAllAttrMappingsResponse:
    """
    
            The response from the getAllAttrMappings2
            operation.
            
    """
    def __init__(self, ) -> None: ...
    AttrMappingInfos: list[AttrMappingInfo]
    """A list of attribute mapping information."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData.  This operation will populate
            the ServiceData plain objects with CadAttrMappingDefinition objects and property descriptor
            LOV objects.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAllAttrMappings2(self) -> GetAllAttrMappingsResponse:
        """    
             This operation retrieves all CAD attribute mapping definitions. If a CadAttributeMappingDefinition object has a path that includes
             a Generic Relationship Manager (GRM) or named reference part, the associated property
             descriptor and any attached ListOfValues
             (LOV) objects will be returned. This operation also returns LOV attachments category
             information to be used in object based conditions.
             

             Since this operation returns existing Teamcenter attribute mappings, please reference
             the Teamcenter help section on creating attribute mappings.
             


Use Cases:

             User needs to have attributes set on an object in Teamcenter.
             

             For this operation, the client application uses the list of returned attribute mapping
             definitions to present the correct CAD attributes to the user that correspond to
             the correct Teamcenter attributes including property descriptor information about
             the Teamcenter attributes.
             


Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :return: 
        """
        ...

