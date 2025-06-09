import System
import System.Collections
import Teamcenter.Services.Strong.Core._2007_06.PropDescriptor
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttachedPropDescsResponse:
    """
    
            AttachedPropDescsResponse  structure contains a map of PropDescOutput2 lists mapped
            to the input type name  and the serviceData with possible errors.
            
    """
    def __init__(self, ) -> None: ...
    InputTypeNameToPropDescOutput: System.Collections.Hashtable
    """A map of property descriptor lists and the associated input type name."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

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
    LovAttachmentsCategory: int
    """LOV attachments Category"""
    InterdependentProps: list[str]
    """interdependentProps"""

class PropDescOutput2:
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
    def GetAttachedPropDescs2(self, Inputs: list[Teamcenter.Services.Strong.Core._2007_06.PropDescriptor.PropDescInfo]) -> AttachedPropDescsResponse:
        """    
             Returns a list of Property Descriptors based on the input structure.  The Property
             Descriptors contain the Display Name, Description and other information about the
             input property.
             

Use Cases:

             This operation provides following use case for retrieving a set of Property Descriptors
             given a type name and list of property names for that type.
             

             Use Case 1:Retrieve a set of Property Descriptors for a list of property names.


Create a new PropDescInfo input structure.
             
Populate the type name and input list of property names.
             
Call getAttachedPropDescs2 with the newly created input structure.
             



Teamcenter Component:

             Core Model Property Layer - A set of capabilities/functionality (data model and behaviours)
             that form the very core of our PLM platform.  This component defines properties.
             
        :param Inputs: 
                         An input Type Name and a list of property names on the input type.  A Property Descriptor
                         is returned for each Property Name in the list.
             
        :return: 
        """
        ...

