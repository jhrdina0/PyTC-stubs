import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class MappingObject:
    """
    
            This is the key structure holding the metadata exchange mapping information.  Only
            one of the three values can be set: nextLevelMappedObject, relationObject,
            or attributeName.
            

If the next level mapping is linked by referenced Teamcenter object,
            then the nextLevelMappedObject is set.
            
If the next level mapping is linked by Teamcenter relation, then
            the relationObject is set.
            
If the current Teamcenter object is where the property is from, then
            the attributeName is set.
            


    """
    def __init__(self, ) -> None: ...
    ObjectType: str
    """the Teamcenter object type name."""
    ReferencedName: str
    """
            the Teamcenter property on the upper level Teamcenter object by which the current
            Teamcenter object is being referenced (For example, an Item Revision relates to a
            Dataset with the References relation, the upper level object is the Item Revision,
            and the current object is the Dataset).  This value is set when Teamcenter property
            type is any other Teamcenter type.
            """
    Path: str
    """
            the indicator of how to find the next level.  If ReferencedObject is the value then
            use referencedObject from the MappingObject.  If Realtion is the value, then use
            relationObject, or if Leaf is the value then use attributeName.
            """
    AttributeName: str
    """the name of the Teamcenter property on the last level object for the exchange."""
    NextLevelMappedObject: list[MappingObject]
    """
            the MappingObject collection which contains mapping information for the next level.
            This will be a vector of single object.  Using a collection since circular references
            are not supported.
            """
    RelationObject: list[Relation]
    """
            the relationship information between the current Teamcenter object and the next level
            object.
            """

class AttrExchangeMapping:
    """
    The metadata exchange mapping information and the client object property name.
    """
    def __init__(self, ) -> None: ...
    ForeignObjectPropertyName: str
    """
            the property name of the client object which the Teamcenter property would be exchanged
            with.
            """
    Mapping: MappingObject
    """the top level MappingObject."""

class AttrExchangeMappingSetValue:
    """
    
            The metadata exchange mapping information and the value to be set on the Teamcenter
            property.
            
    """
    def __init__(self, ) -> None: ...
    AttrExchange: AttrExchangeMapping
    """the attribute exchange mapping information."""
    TcPropertyValue: str
    """the property value to be on the Teamcenter object attribute."""

class FailedObjInfo:
    """
    The failed client object property name and failed error list.
    """
    def __init__(self, ) -> None: ...
    FailedForeignObjectName: str
    """the name of the failed client object property."""
    ErrorStack: list[str]
    """the list of failure errors."""

class Relation:
    """
    The information about relationship between two Teamcenter objects.
    """
    def __init__(self, ) -> None: ...
    RelationName: str
    """the relationship name that exists between two Teamcenter objects."""
    MappedObject: list[MappingObject]
    """
            a next level object which contains mapping information.  This collection will only
            contain one object, using a collection since circular references are not supported.
            """
    RelationType: str
    """
            the information about what the relation is between two Teamcenter objects.  The values
            could be Primary or Secondary. If it is primary, the containing object is the primary
            object in the relation.  If it is secondary, the containing object is the secondary
            object in the relation.
            """

class TcAttributeValue:
    """
    The resolved attribute information.
    """
    def __init__(self, ) -> None: ...
    TcVal: str
    """
            the Teamcenter property value.  The actual value is converted to string before sending
            to the client.
            """
    TypeOfVal: str
    """
            the Teamcenter property type.  The type of the value can be of char, double, float,
            int, logical, short or string.  The client and the server will need to do the conversion
            based on these types.
            """

class ResolveAndGetData:
    """
    
            The Teamcenter object property values based on the given metadata exchange mapping
            information.
            
    """
    def __init__(self, ) -> None: ...
    ForeignObjectPropertyName: str
    """
            the property name of the client object which the Teamcenter object property would
            be exchanged with.
            """
    TcAttrVal: TcAttributeValue
    """the Teamcenter property value to be set on the client object property."""
    IsFailed: bool
    """this value is true if the mapping resolve for this input object failed."""
    ErrorStack: list[str]
    """
            these are the errors return from the server for the particular mapping resolve or
            getting properties.
            """

class ResolveAndGetResult:
    """
    
            The WorkspaceObject (the current implementation in the Microsoft Office client, this
            is the Dataset) object and its corresponding resolved attribute mapping outputs.
            
    """
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            the WorkspaceObject (the current implementation in the Microsoft Office client, this
            is the Dataset) object from which the resolving of the mapping begins.
            """
    ResolveAndGetDataList: list[ResolveAndGetData]
    """the list of resolved attribute structures whether it succeeded or failed."""

class ResolveAndSetResult:
    """
    
            The Teamcenter object and the corresponding failed mapping information about which
            Teamcenter object property setting has failed.
            
    """
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            the WorkspaceObject (the current implementation in the Microsoft Office client, this
            is the Dataset)  object where the attribute mapping start from.
            """
    FailedObjInfos: list[FailedObjInfo]
    """the list of the failed mappping information."""

class ResolveAttrMappingsAndGetPropertiesInfo:
    """
    The input structure for ResolveAttrMappingsAndGetProperties service method.
    """
    def __init__(self, ) -> None: ...
    Locale: str
    """the locale information for the dataset content."""
    DatsetObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            the WorkspaceObject (the current implementation in the Microsoft Office client, this
            is the Dataset) object from which the metadata exchange is initiated.
            """
    AttrExchange: list[AttrExchangeMapping]
    """the list of structures with the metadata exchange mapping information."""

class ResolveAttrMappingsAndGetPropertiesResponse:
    """
    
            The return structure for resolving metadata exchange mappings and the Teamcenter
            object property values.
            
    """
    def __init__(self, ) -> None: ...
    ResolveAndGetResults: list[ResolveAndGetResult]
    """the list of structures that have the Teamcenter object property values."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            the list of errors.  The error would be associated with the property names of the
            client object property for the which the metadata exchange failed.
            """

class ResolveAttrMappingsAndSetPropertiesInfo:
    """
    
            The input structure for resolving metadata exchange mappings and to set the Teamcenter
            object property.
            
    """
    def __init__(self, ) -> None: ...
    Locale: str
    """the locale information for the dataset content."""
    DatasetObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            the WorkspaceObject (normally is Dataset) object from which the metadata exchange
            is initiated.
            """
    AttrExchange: list[AttrExchangeMappingSetValue]
    """the list of structures with the metadata exchange mapping information."""

class ResolveAttrMappingsAndSetPropertiesResponse:
    """
    
            The return structure for resolving metadata exchange mappings, and the Teamcenter
            object property values.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """the list of partial errors returned for failed metadata exchange object."""
    ResolvedAndSetResults: list[ResolveAndSetResult]
    """
            the list of structures that have the client object property name that fails to set
            and the corresponding list of errors.
            """

class AttributeExchange:
    """
    Interface AttributeExchange
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ResolveAttrMappingsAndGetProperties(self, Info: list[ResolveAttrMappingsAndGetPropertiesInfo]) -> ResolveAttrMappingsAndGetPropertiesResponse:
        """    
             This operation processes the metadata exchange mapping information between the client
             application and Teamcenter from the provided input list of ResolveAttrMappingsAndGetPropertiesInfo
             structure (containing the metadata exchange mapping information from the client application).
             The operation then gets and returns the property  values of the corresponding Teamcenter
             object from provided input information.
             

Use Cases:

Metadata exchange between Teamcenter and Microsoft Office Word application

             From the Teamcenter client for Microsoft Office Word 2010, a user opens and checks
             out a WordX Dataset.  User then clicks on the Teamcenter ribbon and clicks on Attribute
             Exchange> Configurations> Create.  From here user can set up the metadata exchange
             between the properties of the Microsoft Office Word file properties and the properties
             of the Teamcenter object.
             

             In the configuration, user can set the direction of the metadata exchange either
             as File to Teamcenter, Teamcenter to File, or Two Way.  In this case, user selects
             Teamcenter to File for the metadata exchange from the client to Teamcenter.  User
             sets up the property mapping by selecting a file property (Comments for example)
             and selecting a Teamcenter object property (object_desc for example), and saves the
             attribute exchange configuration.  User then clicks on Attribute Exchange>Reload
             button.  The Microsoft Office Word initiates this operation and gets Teamcenter object
             property (object_desc for example) value back.  To verify the client file property
             gets updated, from Microsoft Office Word menu File, select Info (in the left panel),
             then select Properties (in the right panel), then select Show Document Panel.
             


Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param Info: 
                         It contains the attribute exchange mappings information.
             
        :return: 
        """
        ...
    def ResolveAttrMappingsAndSetProperties(self, Info: list[ResolveAttrMappingsAndSetPropertiesInfo]) -> ResolveAttrMappingsAndSetPropertiesResponse:
        """    
             This operation processes the metadata exchange mapping information between the client
             and Teamcenter from the provided input list of ResolveAttrMappingsAndSetPropertiesInfo
             structure (containing the metadata exchange mapping information from the client application).
             The operation sets the Teamcenter property values based on the provided input information.
             


Use Cases:

Metadata exchange between Teamcenter and Microsoft Office Word application


             From the Teamcenter client for Microsoft Office Word 2010, a user opens and checks
             out a WordX Dataset.  User then clicks on the Teamcenter ribbon and clicks on Attribute
             Exchange >Configurations>Create.  From here user can set up the metadata exchange
             between the properties of the Microsoft Office Word file and the properties of the
             Teamcenter object.
             

             In the configuration, user can set the direction of the metadata exchange either
             as File to Teamcenter, Teamcenter to File, or Two Way.  In this case, user selects
             File to Teamcenter for the metadata exchange, pick a file property (Comment for example),
             pick a Teamcenter object property (object_desc for example), and save the attribute
             exchange configuration.  From Microsoft Office Word menu File, select Info (left
             panel), then select Properties (right panel)>Show Document Panel.  Update the Comments
             text box in the Document Properties Panel with some text.  Now select Teamcenter
             ribbon and click on Save.  Save and check in the Dataset.  During this process, the
             Microsoft Office Word initiates this operation and updates Teamcenter object property
             (object_desc for example) value.  User can verify the Teamcenter object property
             (object_desc for example) by login to a Teamcenter client such as Rich Application
             Client (RAC), do a View properties on the Teamcenter object.
             


Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param Info: 
                         It contains information for Resolving the attribute exchange and the value to be
                         set on the Teamcenter attribute.
             
        :return: that has failure along with the corresponding
             list of client properties and error messages).
        """
        ...

