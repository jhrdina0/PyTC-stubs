import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateDesc:
    """
    Create Descriptor definition
    """
    def __init__(self, ) -> None: ...
    BusinessObjectTypeName: str
    """Business Object Type Name"""
    PropDescs: list[PropDesc]
    """Vector of Property Descriptors"""
    SecondaryCreateDescs: System.Collections.Hashtable
    """Map of property name to secondary object's create descriptors"""

class CreateDescResponse:
    """
    
            Structure containing Create Descriptor information representing the metadata about
            the properties relevant to a Create Operation
            
    """
    def __init__(self, ) -> None: ...
    CreateDescs: list[CreateDesc]
    """
            List of Teamcenter::Soa::Core::_2008_06::PropDescriptor::CreateDesc
            objects. Each element in the list is a Create Descriptor for a business object which
            contains metadata information about the properties necessary to create the business
            object i.e, property is mandatory, property is visible, etc. It is a recursive data
            structure which may point to secondary CreateDesc
            objects e.g Item CreateDesc contains
            references to ItemRevision and Item Master CreateDesc
            objects
            """
    SrvData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data containing partial errors. If there is any error in retrieving the Create
            Descriptor for any Business Object in the input vector, it is returned as part of
            the error stack. The service data also contains LOV objects for the properties in
            the plain objects vector in the service data
            """

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

class SecCreateDesc:
    """
    
            Secondary Create Descriptor definition. This is the secondary create descriptor data
            type for secondary objects that get created during object creation. For example,
            ItemRevision and Item Master are the secondary objects that get created
            during creation of Item. Note that this is a recursive data structure which
            can itself point to other Secondary Create Descriptors (ItemRevision pointing
            to ItemRevision Master)
            
    """
    def __init__(self, ) -> None: ...
    BusinessObjectTypeName: str
    """Business Object Type Name of the secondary object"""
    IsRequired: bool
    """
            Boolean field indicating if creation of secondary object is required (non optional)
            or not
            """
    IsArray: bool
    """
            true indicates the secondary descriptor is part of an array of secondary descriptors
            (The relation or reference property on the primary create descriptor could potentially
            point to several secondary descriptors i.e Create several secondary objects for the
            same reference or relation property. This is the usecase for which the field will
            be true for each Secondary Descriptor in the array)
            """
    CompoundingCtxt: str
    """
            enum indicating if the secondary object is a relation (in which case value is CompoundRelation) or a regular business object
            (in which case value is CompoundObject)
            """
    PropDescs: list[PropDesc]
    """List of Property Descriptors for the Secondary Object"""
    SecondaryCreateDescs: System.Collections.Hashtable
    """
            Map (string, Teamcenter::Soa::Core::_2008_06::PropDescriptor::SecCreateDesc)
            of the secondary descriptor objects. For example, an ItemRevision is the Secondary
            CreateDescriptor for Item. The ItemRevision Secondary Create Descriptor
            itself will contain SecCreateDesc objects for ItemRevision Master which is
            also created when the ItemRevision is created. The map contains the reference
            property or relation property name on the Parent Secondary Business Object as the
            key and the SecCreateDesc as the value. If
            there are no secondary objects to be created, the map will be empty (For example,
            the secondary create descriptor for Item Master  which is created when Item
            is created has an empty map)
            """

class PropDescriptor:
    """
    Interface PropDescriptor
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetCreateDesc(self, BusinessObjectTypeNames: list[str]) -> CreateDescResponse:
        """    
             The operation returns information required to create a Business Object. The Create
             Descriptor (CreateDesc object) includes the metadata information for the properties
             required when creating a business object  i.e, property is mandatory, property is
             visible, etc. The CreateDesc is a recursive data structure. The CreateDesc object
             can also reference CreateDesc on secondary objects through a reference or relation
             property. For example, the CreateDesc for Item points to CreateDesc on its
             related secondary objects, ItemRevison and Item Master. The CreateDesc
             for ItemRevision in turn points to the CreateDesc for ItemRevision Master.
             

             NOTE:  The operation will be deprecated as of Teamcenter 10. All the metadata information
             necessary for the Create operation can be retrieved from the SOA client metamodel.
             


Use Cases:

             Get Create Descriptor information for the Create wizard for an object.
             
             This call is made to populate the Create dialog for any Business Object. After obtaining
             the user input on the fields of the create dialog, a call is made to the Teamcenter::Soa::Core::_2008_06::DataManagement::createObjects
             operation to create the object
             


Dependencies:

             createObjects
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param BusinessObjectTypeNames: 
                         list of business object names for which Create Descriptor is needed.
             
        :return: 214133  No type was found for the given name
        """
        ...

