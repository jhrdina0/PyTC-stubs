import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttachedPropDescsResponse:
    """
    Attached Property Descriptors Response
    """
    def __init__(self, ) -> None: ...
    InputTypeNameToPropDescOutput: System.Collections.Hashtable
    """Map of input type name to PropertyDescriptor"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData which has output tags as plain objects and errors in partialError"""

class PropDesc:
    """
    The PropDesc struct describes information about the Teamcenter property
    """
    def __init__(self, ) -> None: ...
    PropName: str
    """Name of the property"""
    DisplayName: str
    """Display name of the property"""
    DefaultValue: str
    """Default value for the property"""
    PropValueType: int
    """
            Value type for the property, PROP_untyped (0) No Value type PROP_char (1) Value is
            a single character PROP_date (2) Value is a date PROP_double (3) Value is a double
            PROP_float (4) Value is a float PROP_int (5) Value is an integer PROP_logical (6)
            Value is a logical PROP_short (7) Value is a short PROP_string (8) Value is a character
            string PROP_typed_reference (9) Value is a typed reference PROP_untyped_reference
            (10) Value is an untyped reference PROP_external_reference (11) Value is an external
            reference PROP_note (12) Value is a note PROP_typed_relation (13) Value is a typed
            relation PROP_untyped_relation (14) Value is an untyped relation
            """
    PropType: int
    """
            Type for the property PROP_unknown (0) Property type is Unknown PROP_attribute (1)
            Based on a POM Attribute (int, string, ...) PROP_reference (2)  Based on a POM Reference
            PROP_relation (3) Based on an ImanRelation PROP_compound (4) Based on a property
            from another Type PROP_runtime (5) Based on a computed value
            """
    IsDisplayable: bool
    """isDisplayable"""
    IsArray: bool
    """Specifies whether the property is an array or single value"""
    MaxNumElems: int
    """Specifies the max number of elements"""
    Lov: Teamcenter.Soa.Client.Model.Strong.ListOfValues
    """ListOfValues object attached to the property (if any)"""
    IsRequired: bool
    """Specifies whether the property is required"""
    IsEnabled: bool
    """Specifies whether the property is enabled"""
    IsModifiable: bool
    """Specifies whether the property is modifiable"""
    AttachedSpecifier: int
    """attachedSpecifier"""
    MaxLength: int
    """maxLength"""
    InterdependentProps: list[str]
    """interdependentProps"""

class PropDescInfo:
    """
    
            PropDescInfo structure represents all the Property Names and associated type to retrieve
            Property Descriptors.
            
    """
    def __init__(self, ) -> None: ...
    TypeName: str
    """The name of the type associated with the input Property Names."""
    PropNames: list[str]
    """A list of the input Property Names to retrieve Property Descriptors."""

class PropDescOutput:
    """
    Property Description Output
    """
    def __init__(self, ) -> None: ...
    PropName: str
    """Input Property name for which PropDesc needs to be fetched"""
    PropertyDesc: PropDesc
    """The PropDescriptor struct describes information about the Teamcenter property"""

class PropDescriptor:
    """
    Interface PropDescriptor
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAttachedPropDescs(self, Inputs: list[PropDescInfo]) -> AttachedPropDescsResponse:
        """    
             Get the attached property descriptor based on input type name and property names
             structure.
             
        :param Inputs: 
                         - vector of structure of PropDescInfo with type name and property names vector.
             
        :return: AttachedPropDescsResponse - Response structure with Map of input typeName to PropDesc
             structure and serviceData
        """
        ...

