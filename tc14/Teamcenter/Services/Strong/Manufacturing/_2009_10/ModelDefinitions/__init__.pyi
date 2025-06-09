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

class GetValidRelationTypesResponse:
    """
    Response of the getValidRelationTypes SOA.
    """
    def __init__(self, ) -> None: ...
    RelationTypesResults: list[RelationTypesOutput]
    """Array of relation types results"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Exceptions from internal processing returned as PartialErrors"""

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
    NamingPatterns: list[str]
    """Naming patterns for property, can be null"""

class PropDescInfo:
    """
    Property Description Information
    """
    def __init__(self, ) -> None: ...
    TypeName: str
    """The name of the Teamcenter Engineering type to which property belongs"""
    PropNames: list[str]
    """List of Property names for which PropDesc needs to be fetched"""

class PropDescOutput:
    """
    Property Description Output
    """
    def __init__(self, ) -> None: ...
    PropName: str
    """Input Property name for which PropDesc needs to be fetched"""
    PropertyDesc: PropDesc
    """The PropDescriptor struct describes information about the Teamcenter property"""

class RelationTypeInfo:
    """
    RelationType information
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Name of the relation type."""
    DisplayName: str
    """Display name of the relation type (localized)."""

class RelationTypesInput:
    """
    Input structure for the getValidRelationTypes SOA.
    """
    def __init__(self, ) -> None: ...
    SourceType: Teamcenter.Soa.Client.Model.ModelObject
    """Type of the source for assignment (part, tool, etc.)"""
    TargetType: Teamcenter.Soa.Client.Model.ModelObject
    """Type of the target for assignment (process, operation, etc.)"""

class RelationTypesOutput:
    """
    Output structure for the getValidRelationTypes SOA.
    """
    def __init__(self, ) -> None: ...
    SourceType: Teamcenter.Soa.Client.Model.ModelObject
    """Type of the source for assignment (part, tool, etc.)"""
    TargetType: Teamcenter.Soa.Client.Model.ModelObject
    """Type of the target for assignment (process, operation, etc.)"""
    ValidRelationTypes: list[RelationTypeInfo]
    """Array of PSOccurrenceType names"""

class ModelDefinitions:
    """
    Interface ModelDefinitions
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetManufacturingPropretyDescs(self, Inputs: list[PropDescInfo]) -> AttachedPropDescsResponse:
        """    
             Get the attached property descriptor based on input type name and property names
             structure.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Inputs: 
                         - vector of structure of PropDescInfo with type name and property names vector.
             
        :return: 300401: The input property is NULL.
        """
        ...
    def GetValidRelationTypes(self, RelationTypesInput: list[RelationTypesInput]) -> GetValidRelationTypesResponse:
        """    
             This service returns a list of occurrence types that are valid for assignment between
             two received object types.
             
        :param RelationTypesInput: 
                         Vector of source and target types pairs.
             
        :return: List of valid occurrence types.
        """
        ...

