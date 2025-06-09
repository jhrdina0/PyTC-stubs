import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttributeFormat:
    """
    Structure representing format details of an attribute
    """
    def __init__(self, ) -> None: ...
    FormatType: int
    """
            Integer representing the attribute type, which could be one of the following
            

- 1 => KeyLOV
            
0 => String
            
1 => Integer
            
2 => Real
            
3 => Date
            
4 => Time range
            

"""
    FormatModifier1: int
    """
            Integer to indicate whether the attribute is configured for one of the following
            -
            

0 - Force positive number
            
1 - Accept and display either + or -
            
2 - Accept + or - but display - sign only
            


Note: This field will return 0 if not applicable. Only applicable if the selected
            formatType is 1 or 2
            """
    FormatModifier2: int
    """
            Integer to indicate additional information about the selected formatType from one
            of the following :
            
            If formatType = 0 then:
            

0 = Print characters in upper and lower case
            
1 = Print all characters in upper case
            
2 = Print all characters in lower case
            


            If formatType = 2 then Number of digits after the decimal point
            


            Note: This field will return 0 if not applicable. Only applicable if the selected
            formatType is 0 or 2
            """
    FormatLength: int
    """
            Integer representing the length of the attribute. In case of a Key-LOV, this will
            contain the Key-LOV ID.
            """

class ChildDef:
    """
    Structure representing Child Definition
    """
    def __init__(self, ) -> None: ...
    Id: str
    """Child class ID."""
    Type: str
    """
            Type of Class. Valid values are -
            

Group                 = (1 << 0)
            
Class                  =
            (1 << 1)
            
View               
            = (1 << 2)
            
Storage class     = (1 << 4)
            

"""
    Name: str
    """Name of the child class"""
    Description: str
    """Description of the child class"""
    ChildCount: int
    """Number of children underneath this child class."""
    InstanceCount: int
    """Number of instances of classification objects in this child class and its descendents."""
    ViewCount: int
    """Number of views for this child class."""
    Documents: list[TypedDocument]
    """
            List of references to the TypedDocument
            structure containing Documents attached to this child class.
            """

class ClassAttribute:
    """
    Contains a list of Child Classes found for the given Classes
    """
    def __init__(self, ) -> None: ...
    Id: int
    """Integer ID for this attribute"""
    Name: str
    """Name for this attribute"""
    ShortName: str
    """Short name defined for this attribute"""
    Annotation: str
    """Annotation information added to this attribute"""
    Format: AttributeFormat
    """
            References the FormatProperties structure
            defining the metric format of this attribute.
            """
    AltFormat: AttributeFormat
    """References the FormatProperties structure defining the nonmetric format of this attribute."""
    UnitName: str
    """
            Unit display name associated with this attribute in this unit system.Note: Only
            applicable to numerical formats of attributes.
            """
    DefaultValue: str
    """
            Default value of this Class attribute. This can be an empty string indicating no
            default value.
            """
    MinValue: str
    """
            Minimum value constraint of this Class attribute. This can be an empty string indicating
            no minimum value constraint.
            
Note: Only applicable to numerical formats of attributes.
            """
    MaxValue: str
    """
            Maximum value contraint of this Class attribute. This can be an empty string indicating
            no maximum value constraint.
            
Note: Only applicable to numerical formats of attributes.
            """
    Description: str
    """Description added for this attribute."""
    ArraySize: int
    """
            Array size or the number of values for this attribute
            

If single valued (non array), then arraySize
            = 1
            
If multi valued (array), then arraySize
            >= 1 corresponding to the size of the array defined in the attribute definition.
            

"""
    Options: int
    """
            Attribute property flags represented as a single integer.
            
            To access individual property flags, a bitwise operations will be required by the
            client.
            
            Valid values are:
            

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
            
ATTR_localizable        = (1
            

"""
    PreConfig: str
    """Preconfiguration attached to the attribute."""
    Config: str
    """Base configuration attached to the attribute"""
    PostConfig: str
    """
            Post configuration attached to the attribute.
            
            Configurations could be any combinations of the following individual configurations:
            

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

class ClassFlags:
    """
    Contains a list of child classes found for the given classes.
    """
    def __init__(self, ) -> None: ...
    IsValid: bool
    """

True value indicates that the class is a valid class. The option
            is for future use and currently is set by default to true internally.
            

"""
    IsAbstract: bool
    """True value indicates that the class is abstract class, else storage class."""
    IsGroup: bool
    """True value indicates that the class is a group."""
    IsAssembly: bool
    """True value indicates that the class is an assembly."""

class ClassDef:
    """
    Properties of the given class.
    """
    def __init__(self, ) -> None: ...
    Id: str
    """Class ID"""
    Parent: str
    """Class ID of the parent class."""
    Name: str
    """Class name"""
    ShortName: str
    """Short name"""
    Description: str
    """Class description"""
    UnitBase: str
    """
            Unit system of the class. See enum UnitBase
            for list of valid values
            """
    Options: ClassFlags
    """
            Class options as specified in the enum ClassFlags
            below
            """
    UserData1: str
    """User data 1 added to this class"""
    UserData2: str
    """User data 2 added to this class"""
    ChildCount: int
    """Number of child classes for this class"""
    InstanceCount: int
    """Total number of classification objects instantiated in this class or any of its descendents"""
    ViewCount: int
    """Number of Views defined for this class"""
    Documents: list[TypedDocument]
    """
            List of attached Icons, Images and NamedRefs
            to this class
            """

class ClassificationObject:
    """
    Structure representing Classification Object details
    """
    def __init__(self, ) -> None: ...
    ClsObjTag: Teamcenter.Soa.Client.Model.ModelObject
    """Reference of Classification object."""
    InstanceId: str
    """Alphanumeric ID of the Classification object."""
    ClassId: str
    """Unique Alphanumeric ID of the Classification class where this object was created."""
    UnitBase: str
    """Unit system of measure in which the Classification object is stored in."""
    WsoId: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            Reference of the WorkspaceObject (WSO) that is associated by this Classification
            object. This can be empty. Allowed WSO types will be defined by the preference 'ICS_allowable_types'.
            
"""
    Properties: list[ClassificationProperty]
    """
            Array of Classification attributes references that store the properties of this Classification
            object.
            """

class ClassificationProperty:
    """
    
            Structure representing Classification Property which holds attribute ids  and their
            values
            
    """
    def __init__(self, ) -> None: ...
    AttributeId: int
    """Holds the unique identifier of an attribute."""
    Values: list[ClassificationPropertyValue]
    """
            Holds a array of values for this attribute in the context of a Classification object.
            
            [Note: An array is required as an attribute can be single or multi-valued.]
            

"""

class ClassificationPropertyValue:
    """
    Holds the 'DB value' and  an optional 'Display value' of a property
    """
    def __init__(self, ) -> None: ...
    DbValue: str
    """Value of the Classification attribute as stored in the database."""
    DisplayValue: str
    """
            Value of the Classification attribute as  it should displayed in the client.
            
            [ For example, If the attribute is a Key-LOV then the Key is stored as the 'dbValue',
            while the 'displayValue' can be configured to be either of the following based
            on the Key-Value pairs in the Key-LOV definition:
            

"Value" only.
            
Concatenated "Key" and "Value". ]
            

"""

class CreateClassificationObjectsResponse:
    """
    
            Holds the classification objects returned by the getCreateClassificationObjects()
            method.
            
    """
    def __init__(self, ) -> None: ...
    ClsObjs: list[ClassificationObject]
    """List of created Classification objects."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failure will be returned with Classification object ID mapped to the error message
            in the ServiceData list of partial errors.
            """

class FindClassificationObjectsResponse:
    """
    
            Holds the classfication objects returned by the findClassificationObjects()
            method.
            
    """
    def __init__(self, ) -> None: ...
    Icos: System.Collections.Hashtable
    """Map of classified WorkspaceObjects and their associated Classification objects."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failure will be returned with WorkspaceObject ID mapped to the error message
            in the ServiceData list of partial errors.
            """

class FindClassifiedObjectsResponse:
    """
    
            Holds the classified objects returned by the  getFindClassifiedObjects()
method.
            
    """
    def __init__(self, ) -> None: ...
    Wsos: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """
            List of classified WorkspaceObjects found for the given list of Classification
            objects.
            """
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failure will be returned with WorkspaceObject ID mapped to the error message
            in the ServiceData list of partial errors.
            """

class GetAttributesForClassesResponse:
    """
    Contains a list of Child Classes found for the given Classes
    """
    def __init__(self, ) -> None: ...
    Attributes: System.Collections.Hashtable
    """Map of Class IDs and the Class attributes found for each of those classes"""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failure will be returned with Class ID mapped to the error message in the ServiceData
            list of partial errors.
            """

class GetChildrenResponse:
    """
    Contains a list of Child Classes found for the given Classes
    """
    def __init__(self, ) -> None: ...
    Children: System.Collections.Hashtable
    """Map of Child classes found for input Class IDs."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failures with Class ID mapped to the error message are returned in the ServiceData
            list of partial errors.
            """

class GetClassDescriptionsResponse:
    """
    Contains a list of Child Classes found for the given Classes.
    """
    def __init__(self, ) -> None: ...
    Descriptions: System.Collections.Hashtable
    """Map of Child classes found for input Class IDs."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """Internal errors encounterd during the operation are added to the partial errors."""

class GetClassificationObjectsResponse:
    """
    
            Holds the classification object details returned by the GetClassificationObjects()
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClsObjs: System.Collections.Hashtable
    """TagClsObjMap map of input classification object to its details."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failure will be returned with Classification Object ID mapped to the error message
            in the ServiceData list of partial
            errors.
            """

class GetFileIdAttributes:
    """
    Contains a list of child classes found for the given classes.
    """
    def __init__(self, ) -> None: ...
    Relation: str
    """Name of the relation for attachement."""
    DatasetType: str
    """Internal type of the attached Dataset object."""
    NamedRefs: list[str]
    """List of named references."""

class GetFileIdCriteria:
    """
    Contains a list of child classes found for a class in the classification hierarchy.
    """
    def __init__(self, ) -> None: ...
    Wsos: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """
            List of associated WorkspaceObjects
            to execute the search for File IDs.
            """
    Criteria: GetFileIdAttributes
    """Reference to the search criterion."""

class GetFileIdsResponse:
    """
    Contains a list of child classes found for the given classes
    """
    def __init__(self, ) -> None: ...
    Ids: System.Collections.Hashtable
    """
            References to map of WorkspaceObject objects and attached Document
            objects.
            """
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """Internal errors encounterd during the operation are added to the partial errors."""

class GetKeyLOVsResponse:
    """
    
            Holds the key-LOV returned by the getKeyLOVs()
            method.
            
    """
    def __init__(self, ) -> None: ...
    KeyLOVs: System.Collections.Hashtable
    """Map of Key-LOV definitions details."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failure will be returned with the Key-LOV ID mapped to the error message in the
            ServiceData list of partial errors.
            """

class GetParentsResponse:
    """
    
            Holds the parents returned by the getParents() method.
            
    """
    def __init__(self, ) -> None: ...
    Parents: System.Collections.Hashtable
    """Map contains a list of parents for each of the input Class IDs"""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """Internal errors encounterd during the operation are added to the partial errors."""

class GetPartFamilyTemplatesResponse:
    """
    
            Holds the PartFamilyTemplates returned by the getPartFamilyTemplates() method.
            
    """
    def __init__(self, ) -> None: ...
    Wsos: System.Collections.Hashtable
    """Map of part family templates found for input Class IDs."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            Failures mapped to the error message in the ServiceData
            list of partial errors.
            """

class KeyLOVDefinition:
    """
    Structure representing KeyLOVDefinition
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Name of the Key-LOV."""
    Options: int
    """
            Key-LOV options to Show/Hide keys.
            
            Valid values are
            

0 = Show key
            
1 = Hide key
            

"""
    KeyValuePairs: System.Collections.Hashtable
    """Map of the Key-Value pairs."""

class SearchAttribute:
    """
    Structure SearchAttribute holds the attribute id and expression for attribute search
    """
    def __init__(self, ) -> None: ...
    AttributeId: int
    """Alphanumeric attribute ID of the attribute used in this search."""
    Query: str
    """
            Query expression for this attribute e.g. >= 20.00. Supported Operators are:
            

Equals - "="
            
Less than - "<"
            
Greater than - ">"
            
Greater than or equal to - ">="
            
Less than or equal to - "<=",
            
OR - "|"
            
AND - "&"
            

"""

class SearchByInstanceIdResponse:
    """
    
            Holds the Instance identifier returned by the getSearchByInstanceId()
            method.
            
    """
    def __init__(self, ) -> None: ...
    ClsObjTags: System.Collections.Hashtable
    """Retrieved classification objects."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failure will be returned with classification object IDs mapped to the error message
            in the ServiceData list of partial
            errors.
            """

class SearchClassAttributes:
    """
    SearchClassAttributes holds classIds and expressions to search class attributes
    """
    def __init__(self, ) -> None: ...
    ClassIds: list[str]
    """List of class IDs to perform search"""
    SearchAttributes: list[SearchAttribute]
    """List of references to the search attributes in these classes."""
    SearchOption: int
    """Unused parameter for this operation."""

class SearchForClassesCriteria:
    """
    
            Searches for classes based on the specified class attribute. Also allows sorting
            the results based on a predefined criterion. Search criteria must be specified and
            cannot be empty.
            
    """
    def __init__(self, ) -> None: ...
    SearchAttribute: str
    """
            Class attribute to be searched for. Valid values are as defined in enum ClassSearchAttribute.
            """
    SearchString: str
    """Query string to search the class attribute by."""
    SortOption: str
    """
            Option to sort the returned results. Valid values are as defined in enum ClassSortOption.
            """

class SearchForClassesResponse:
    """
    
            Returns a SearchForClassesResponse
            structure containing:
            

Retrieved classes in the ServiceData
            list of plain objects
            
Any failures with class ID mapped to the error message in the ServiceData list of partial errors.
            


    """
    def __init__(self, ) -> None: ...
    Classes: System.Collections.Hashtable
    """Map of search criteria index and the classes found for each of those searches."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """Internal errors encounterd during the operation are added to the partial errors"""

class SearchResponse:
    """
    SearchResponse holds the response of search details
    """
    def __init__(self, ) -> None: ...
    ClsObjTags: System.Collections.Hashtable
    """Map of the input query strings and references to the retrieved objects."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failure will be returned mapped to the error message in the ServiceData list of partial errors.
            """

class TypedDocument:
    """
    
            Structure holding the attached Icon, Image or NamedRef or this
            child class.
            
    """
    def __init__(self, ) -> None: ...
    DocumentType: str
    """
            Contains type of document attached. Valid values are:
            

icon
            
image
            
NamedRef
            

"""
    Ticket: str
    """Ticket identifier for the attached file"""
    OriginalFileName: str
    """File name for this attachment."""

class UpdateClassificationObjectsResponse:
    """
    UpdateClassificationObjectsResponse
    """
    def __init__(self, ) -> None: ...
    ClsObjs: list[ClassificationObject]
    """List of updated Classification objects."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failure will be returned with Classification object ID mapped to the error message
            in the ServiceData list of partial
            errors.
            """

class Classification:
    """
    Interface Classification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateClassificationObjects(self, ClsObjs: list[ClassificationObject]) -> CreateClassificationObjectsResponse:
        """    
             Creates one or more classification objects and (optionally) attach them to a workspace
             object, thus classifying it. When the Classification objects are not associated with
             any workspace object, they would act as standalone Classification objects. A classification
             object is also called ICO
             

Use Cases:

             User wants to classify a workspace object or create a standalone classification object
             (ICO) in Teamcenter. This operation can be combined with other operations like createItems()
             to create workspace object and then associate the workspace object to the classification
             object. Before creating a classification object, a classification class hierarchy
             should already be created by the classification admin user in Teamcenter. This hierarchy
             should include a storage class (a class that allows instances to be created and associated
             to it) for which the classification objects need to be created. Values of any attributes
             associated with classification objects can also be populated.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClsObjs: 
                         List of structure containing information about the classification object(ICO) that
                         needs to be created including its attribute values. It also includes the classification
                         class information for which classification object will be created &amp; information
                         on workspace object being classified.
             
        :return: 
        """
        ...
    def DeleteClassificationObjects(self, ClsObjTags: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Deletes one or more classification objects permanently. A classification object is
             also called ICO. The classified workspace object associated with the ICO will not
             be deleted
             

Use Cases:

             User needs to delete classification objects. It is typically called when after creating
             or searching the classification objects, user decides that the returned objects are
             not needed anymore
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClsObjTags: 
                         Unique Business Object(s) representing the classification object(s) to be deleted.
             
        :return: 
        """
        ...
    def FindClassifiedObjects(self, IcoTags: list[Teamcenter.Soa.Client.Model.ModelObject]) -> FindClassifiedObjectsResponse:
        """    
             Finds the workspace objects (WSO) associated with input Teamcenter classification
             objects. A classification object is also called ICO. Each ICO can have only one workspace
             object associated with it.
             

Use Cases:

             When user need to find workspace objects based on classification objects (ICO) that
             were created when workspace objects were classified.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param IcoTags: 
                         List of classification object (ICO) Business Objects, whose corresponding   workspace
                         objects need to be found
             
        :return: 
        """
        ...
    def GetAttributesForClasses(self, ClassIds: list[str]) -> GetAttributesForClassesResponse:
        """    
             Provides information on class attributes for the classification classes based on
             input classification class ids. Detailed information about class attributes is provided
             & includes class attribute name, description, format, unit system, minimum/maximum
             value & configuration set
             

Use Cases:

             When user wants to view details of all class attributes associated with a classification
             class. This operation is similar to getAttributesForClasses2(), but provides information
             in a slightly different format. Typically, the information about class attributes
             is used to determine which classification class a workspace object shall be classified
             into
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClassIds: 
                         Identifier for the classification class whose attribute information is requested.
             
        :return: 
        """
        ...
    def GetChildren(self, GroupOrClassIds: list[str]) -> GetChildrenResponse:
        """    
             Gets the information about immediate children in classification hierarchy for given
             group or class identifier(s).
             
             Returns a GetChildrenResponse structure
             containing:
             

Retrieved child classes in the ServiceData
             list of plain objects
             
Any failures with Class ID mapped to the error message in the ServiceData list of partial errors.
             



Use Cases:

             User wants to get details of all groups or classes that lie under a particular group
             or class in a classification class hierarchy.
             

             Returns a GetChildrenResponse structure
             containing:
             

Retrieved child classes in the ServiceData
             list of plain objects
             
Any failures with Class ID mapped to the error message in the ServiceData list of partial errors.
             



Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param GroupOrClassIds: 
                         Unique ID(s) of the classification class or group whose immediate children need to
                         be determined in the classification class hierarchy
             
        :return: 
        """
        ...
    def GetClassDescriptions(self, ClassIds: list[str]) -> GetClassDescriptionsResponse:
        """    
             Gets detailed information about a classification class based on classification class
             ID. This information includes class type, parent, name, description, unit system
             and user data associated with the class.  It also includes a count of children, number
             of classification views & number of instances of classification objects associated
             with the classification class. Information can also be obtained on any documents
             such as images & icons attached to the classification class.
             

Use Cases:

             When user need details of classification classes. These details can help user decide
             whether to classify a workspace object in particular classification classes.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClassIds: 
                         List of unique identifiers for classification classes whose details are needed.
             
        :return: 
        """
        ...
    def GetClassificationObjects(self, ClsObjTags: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetClassificationObjectsResponse:
        """    
             Looks for specified classification objects. If they are found, then detailed information
             about those objects is provided. A classification object is also called ICO
             

Use Cases:

             When user need to find an existing classification object to either view or update
             its details. It can be followed by operations like updateClassificationObjects()
             or deleteClassificationObjects() to
             update or delete the classification objects.
             
             The operation findClassificationObjects()
             can be used to get the list of classification objects, associated with workspace
             objects. Then, this operation getClassificationObjects()
             is used to get the detailed information on the classification objects.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClsObjTags: 
                         The classification object(s) for which detailed information is required.
             
        :return: 
        """
        ...
    def GetFileIds(self, Criteria: list[GetFileIdCriteria]) -> GetFileIdsResponse:
        """    
             Gets the file information from any dataset that is associated with workspace object(s).
             The dataset type can be specified along with the relation used when it is attached
             to a workspace object. Information corresponding to a particular file inside a dataset
             can be retrieved.
             

Use Cases:

             User wants to get information about files inside a dataset that is associated with
             workspace objects (WSO). Typically it will be used to get and view the  image or
             icon files associated with datasets attached to workspace objects.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param Criteria: 
                         List of structures containing information on the workspace objects (WSO) to which
                         the datasets are attached, the type of datasets, relation in which dataset is attached
                         to the WSO, and the named reference inside the dataset. All this information can
                         be used to get to a particular file inside a dataset
             
        :return: 
        """
        ...
    def GetKeyLOVs(self, KeyLOVIds: list[str]) -> GetKeyLOVsResponse:
        """    
             Gets the information for classification key-LOVs  based on given ID(s). Information
             such as key-LOV's name, display options, and key and value entries can be obtained.
             A key-LOV is a list of values used in classification. The key-LOVs are used to define
             one or more values that can be set for classification dictionary attributes
             

             Typical format of a key-LOV -
             

                 <key-LOV ID>:<key-LOV Name>
             
                 <Key10>:<Value10>
             
                 <Key20>:<Value20>
             

             Example of a key-LOV
             

             - 33381:Design Categories
             
                 Des1:Bearing
             
                 Des2:Bracket
             
                 Des3:Frame
             
                 Des4:LeadBox
             


Use Cases:

             User wants to retrieve the information for an existing key-LOV using the key-LOV's
             unique identifier. The operation is similar to getKeyLOVs2().
             But getKeyLOVs2()provides more detailed
             information about any key-LOVs .
             

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
    def GetParents(self, ChildIds: list[str]) -> GetParentsResponse:
        """    
             Gets the classification class ID(s) of all parent classes in a hierarchy, based on
             given classification class ID. The parent class IDs are sorted as immediate parent
             first, toplevel parent last.
             

Use Cases:

             User needs to determine all the parent classes for any given class in a classification
             hierarchy.  If user needs to get the children of the given class ID, then getChildren() operation shall be used.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ChildIds: 
                         The unique identifier IDs for classification classes for which parent class ID information
                         is being requested
             
        :return: 
        """
        ...
    def GetPartFamilyTemplates(self, ClsClassIds: list[str]) -> GetPartFamilyTemplatesResponse:
        """    
             Finds the information for part family templates (PFT) based on the classification
             class IDs. Part family templates can be used to define geometry and certain properties
             of the geometry as variable properties. They can be attached to a classification
             class. For any classification class, user can find out the associated part family
             templates and their information.
             

Use Cases:

             While using graphics builder, users often require information about the part family
             template attached to the classification classes.  Graphics builder is a program used
             by classification administration that communicates with the Teamcenter server to
             generate graphics. The graphics builder uses NX libraries.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClsClassIds: 
                         List of IDs of classification classes for which the associated part family template
                         information is required.
             
        :return: 
        """
        ...
    def Search(self, SearchCriteria: list[SearchClassAttributes]) -> SearchResponse:
        """    
             Finds all the classification objects based on classification class IDs, classification
             attribute ID and an expression for classification attribute value. A classification
             object is also called an ICO.
             

Use Cases:

             User needs to search for classification objects based on the class where they are
             classified and the value of classification attributes.Another related operation for
             searching classification objects is searchByInstanceID(),
             that can search for classification objects based on their IDs
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param SearchCriteria: 
                         List of structures containing classification class ID, classification attribute ID,
                         and an expression for classification attribute value (e.g. &gt;= 20.00 ).
             
        :return: 
        """
        ...
    def SearchByInstanceId(self, InstanceIdQueries: list[str]) -> SearchByInstanceIdResponse:
        """    
             Finds all the classification objects based on their IDs. A classification object
             is also called an ICO. If the ICO classifies a workspace object, then ICO ID would
             be same as the workspace object ID
             

Use Cases:

             User wants to search for classification objects based on their IDs. The returned
             objects can then be used as input for operations like findClassifiedObjects(),
             which is used to search workspace objects associated with the ICOs.
             
             Another related operation for searching classification objects is search(), that can search for classification objects based
             on class ID and attribute values
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param InstanceIdQueries: 
                         List of IDs of classification objects. These can contain wildcards ( e.g. ICO00*
                         ).
             
        :return: 
        """
        ...
    def SearchForClasses(self, Criteria: list[SearchForClassesCriteria]) -> SearchForClassesResponse:
        """    
             Finds the classification classes based on provided search criteria and provides detailed
             information about those classes.  The user can search using a search expression on
             attributes of the class (Class ID, Name, Type etc.)  . For example, the user shall
             be able to search all the classes whose name begins with a particular set of characters
             and where the class ID matches certain pattern. The order of search results can also
             be sorted on various criteria.
             

Use Cases:

             The user needs to search for classification classes using a search criterion based
             on various attributes of a class. The search criterion can be based on one or more
             attributes
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param Criteria: 
                         List of structure containing search expression, search attributes, and sort options
                         for search results
             
        :return: 
        """
        ...
    def UpdateClassificationObjects(self, ClsObjs: list[ClassificationObject]) -> UpdateClassificationObjectsResponse:
        """    
             Updates existing classification objects. A classification object is also called ICO.
             Values of various ICO attributes can be modified
             

Use Cases:

             User wants to update values of the attributes for an existing classification object
             in Teamcenter. E.g. user wants to modify an integer value of a class attribute ("Length")
             for an existing ICO. This operation is typically used after creating the classification
             objects using createClassificationObjects().
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClsObjs: 
                         List of structures containing information about classification objects that needs
                         to be modified,  along with the information that needs to be updated
             
        :return: 
        """
        ...
    def FindClassificationObjects(self, WsoIds: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]) -> FindClassificationObjectsResponse:
        """    
             Finds the classification objects associated with input workspace objects (WSO). A
             classification object is also called ICO. Each workspace object can have one or more
             ICOs associated with it.
             

Use Cases:

             When user need to find classification objects (ICO) based on workspace objects. Each
             time a workspace object is classified in a classification class a classification
             object (ICO) object is created.  After searching for all the classification objects
             corresponding to a workspace object, user can find more information about the classification(s)
             of a workspace object. The operation getClassificationObjects() can be used to get detailed information about
             the classification objects. After getting information on classification objects,
             user can also choose to modify or delete those using operation updateClassificationObjects() or deleteClassificationObjects()


Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param WsoIds: 
                         List of identifiers for classified workspace objects(WSO), for which the associated
                         classification objects(ICO) are required.
             
        :return: 
        """
        ...

