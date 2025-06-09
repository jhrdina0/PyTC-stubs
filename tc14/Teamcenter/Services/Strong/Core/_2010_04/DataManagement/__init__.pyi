import System
import System.Collections
import Teamcenter.Services.Strong.Core._2007_06.DataManagement
import Teamcenter.Services.Strong.Core._2008_06.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttributeInfo:
    """
    This structure contains the name value pairs.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Name of the attribute that needs to be set."""
    Values: list[str]
    """Values to be set"""

class AvailableBusinessObjectTypeInfo:
    """
    This structure represents Business Object name, display name, and its hierarchy.
    """
    def __init__(self, ) -> None: ...
    Type: str
    """Name of the Business Object"""
    DisplayType: str
    """Display name of the Business Object"""
    Hierarchies: list[str]
    """
            Bottom up hierarchy of the Business Object going up to the input Business
            Object
"""

class BusinessObjectHierarchy:
    """
    
            This structure contains information about a bottom up hierarchy starting with a Business
            Object name and going up the hierarchy of parents up to the primary Business
            Object.
            
    """
    def __init__(self, ) -> None: ...
    BoName: str
    """Name of the Business Object"""
    BoDisplayName: str
    """Display Name of the Business Object"""
    BoParents: list[str]
    """
            Names of Business Objects going up the hierarchy of parents up to the primary
            Business Object
"""

class CommitDatasetFileInfo:
    """
    This structure contains the basic info for a file to be uploaded to a dataset.
    """
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Dataset object reference."""
    CreateNewVersion: bool
    """Flag to create new version ( TRUE ) or not ( FALSE )."""
    DatasetFileTicketInfos: list[DatasetFileTicketInfo]
    """A list of DatasetFileTicketInfos."""

class CreateDatasetsResponse:
    """
    Return structure for createDatasets operation
    """
    def __init__(self, ) -> None: ...
    DatasetOutput: list[DatasetOutput]
    """
            List of output structure for creatDatasets operation. Each element in the list contains
            a client Id and the related Dataset object created.
            """
    ServData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member"""

class DatasetFileInfo:
    """
    Holds the basic info for a file to be uploaded to a Dataset.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string used to identify return data elements and partial errors associated
            with this input structure.
            """
    FileName: str
    """Name of file to be uploaded.  Filename only, should not contain path to filename."""
    NamedReferenceName: str
    """Named Reference relation to file."""
    IsText: bool
    """Flag to indicate if file is text ( TRUE ) or binary (FALSE )."""
    AllowReplace: bool
    """Flag to indicate if file can be overwritten ( TRUE ) or not ( FALSE )."""

class DatasetFileTicketInfo:
    """
    This structure contains the basic info for a file to be uploaded to a dataset.
    """
    def __init__(self, ) -> None: ...
    DatasetFileInfo: DatasetFileInfo
    """Member of type DatasetFileInfo."""
    Ticket: str
    """ID of ticket."""

class DatasetInfo:
    """
    
            The DatasetInfo struct represents all of the data necessary to construct the Dataset
            object.  The basic attributes that required are passed as named elements in the struct.
            All other attributes are passed as name/value pairs in the AttributeInfo struct.
            The nrObjectInfos field allows for the attachment of an object that will be related
            to this newly created Dataset.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string used to identify return data elements and partial errors associated
            with this input structure.
            """
    Name: str
    """Name attribute value"""
    Description: str
    """Description attribute value"""
    Type: str
    """Type attribute value"""
    DatasetId: str
    """ID attribute value"""
    DatasetRev: str
    """Revision attribute value"""
    ToolUsed: str
    """
            Name of the Tool used to open the created Dataset, may be an empty
            string.
            """
    Attrs: list[AttributeInfo]
    """List of attribute name values pairs to be set"""
    DatasetFileInfos: list[DatasetFileInfo]
    """List of  info of the files to be uploaded"""
    NrObjectInfos: list[NamedReferenceObjectInfo]
    """list of info of named references of the Dataset"""
    Container: Teamcenter.Soa.Client.Model.ModelObject
    """Object reference of the container used to hold the created Dataset"""
    RelationType: str
    """Name of the relation type for the Dataset to be created"""

class DatasetOutput:
    """
    
            This structure contains return data from createDatasets
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the input criteria."""
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Dataset object reference of the created dataset"""
    CommitInfo: list[CommitDatasetFileInfo]
    """List of CommitDatasetFileInfos"""

class DisplayableBusinessObjectsOut:
    """
    
            This structure contains a list of displayable business objects (BO) under a given
            BO(displayable sub-BO hierarchy).
            
    """
    def __init__(self, ) -> None: ...
    BoTypeName: str
    """The Business Object name for which displayable Hierarchy is returned."""
    DisplayableBOTypeNames: list[BusinessObjectHierarchy]
    """Displayable BO hierarchy"""

class DisplayableSubBusinessObjectsResponse:
    """
    Structure to hold list of Business Objects and its displayable names.
    """
    def __init__(self, ) -> None: ...
    Output: list[DisplayableBusinessObjectsOut]
    """List of displayable Business Objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service data."""

class GetAvailableBusinessObjectTypesResponse:
    """
    
            Returned service response structure to represents the displayable Business Objects
            information.
            
    """
    def __init__(self, ) -> None: ...
    InputClassToTypes: System.Collections.Hashtable
    """
            A map of Business Object names and associated descendant Business Objects
            (string, vector<AvailableBusinessObjectTypeInfo>>)
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData."""

class GetDatasetCreationRelatedInfoResponse2:
    """
    Holds the Response data from getDatasetCreationRelatedInfo2
    """
    def __init__(self, ) -> None: ...
    ToolNames: list[str]
    """List of Tool names"""
    ToolDisplayNames: list[str]
    """List of Tool display names."""
    NewDatasetName: str
    """The name of the new Dataset, can be an empty string"""
    NameCanBeModified: bool
    """If true, the name of the Dataset can be modified"""
    InitValuePropertyRules: list[str]
    """List of properties have the initialized values from property constant attachments"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member"""

class LocalizableResults:
    """
    
            This data structure contains property names and boolean value to indicate whether
            this property is localizable.
            
    """
    def __init__(self, ) -> None: ...
    PropName: str
    """Internal property name."""
    Islocalizable: bool
    """boolean value to indicate localizability of this property."""

class LocalizableStatusInput:
    """
    
            This data structure contains the type of the business object and its internal property
            names.
            
    """
    def __init__(self, ) -> None: ...
    ObjTypeName: str
    """String Object Type Name"""
    PropNames: list[str]
    """A list of the internal property names of the object."""

class LocalizableStatusOutput:
    """
    This structure contains object type name and localizable information.
    """
    def __init__(self, ) -> None: ...
    ObjTypeName: str
    """Object Type Name"""
    Results: list[LocalizableResults]
    """Result containing localizable information."""

class LocalizableStatusResponse:
    """
    
            This data structure contains a list of localized results and ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Results: list[LocalizableStatusOutput]
    """
            A list of LocalizableResults structure to
            hold the localizable information for all properties.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""

class LocalizedPropertyValuesInfo:
    """
    
            This data structure contains business object tag and a list of of NameValueLocaleStruct

    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The business object."""
    PropertyValues: list[NameValueLocaleStruct]
    """
            A list of NameValueLocaleStruct that holds
            property name, value and locale information.
            """

class LocalizedPropertyValuesList:
    """
    
            This structure contains  a list of output localized property value info and  partial
            error.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[LocalizedPropertyValuesInfo]
    """
            A list of structure LocalizedPropertyValuesInfo to keep the localized property values
            info.
            """
    PartialErrors: Teamcenter.Soa.Client.Model.ServiceData
    """Used for storing partial error and standard service data."""

class NamedReferenceObjectInfo:
    """
    
            This structure contains information regarding named reference type value, object
            reference, object type name and list of attribute information to set on the object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """An identifier is defined by the user to track the related object."""
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """BusinessObject to attach to the Dataset as a named reference."""
    NamedReferenceName: str
    """The name of the named reference object."""
    ReferenceType: str
    """Reference Type. It is either AE_PART_OF or AE_ASSOCIATION."""

class NameLocaleStruct:
    """
    This structure contains a property name and list of possible locales.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """A property name string"""
    Locales: list[str]
    """A list of language locales."""

class NameValueLocaleStruct:
    """
    This structure contains localization related information for property values.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Property name (internal)"""
    Values: list[str]
    """A list of property values"""
    Locale: str
    """The name of the locale"""
    SeqNum: int
    """Sequence number"""
    Status: list[str]
    """
            The name of the localization status.
            
            The status must be one of the following values:
            

for the approved status: "A", "Approved" or the version
            of the "Approved" string for the client/server log-in locale.
            
for the in-review status: "R", "In Review", "In-Review",
            "InReview" or the version of the "In Review" string for the client/server
            log-in locale.
            
for the pending status: "P", "Pending" or the version
            of the "Pending" string for the client/server log-in locale.
            
for the invalid status: "I", "Invalid" or the version
            of the "Invalid" string for the client/server log-in locale.
            
for the master status: "M", "Master" or the version
            of the "Master" string for the client/server log-in locale.
            

"""
    StatusDesc: list[str]
    """Description of statuses used for tooltip on the user interface"""
    Master: bool
    """Master value indication"""

class PropertyInfo:
    """
    This data structure contains business object and a list of properties and locales.
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The desired business object to retrieved localized property values"""
    PropsToget: list[NameLocaleStruct]
    """A list of NameLocaleStruct to hold the desired properties and locales."""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindDisplayableSubBusinessObjectsWithDisplayNames(self, Input: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.BOWithExclusionIn]) -> DisplayableSubBusinessObjectsResponse:
        """    
             This operation returns sub Business Object names that are displayable to the
             login user in the object creation dialog and their display names for each Primary
             Business Object given as the input.  Returned Business Object lists have exclusions
             of Business Objects and their secondary Business Objects as specified in the input.
             This returns the hierarchy of displayable objects for each Business Object it returns.
             
        :param Input: 
                         A list of Business Object names and their exclusion list for which the displayable
                         Business Objects are to be retrieved.
             
        :return: Contains a list of BO type names to be displayed for input
        """
        ...
    def GetAvailableTypesWithDisplayNames(self, Classes: list[Teamcenter.Services.Strong.Core._2007_06.DataManagement.BaseClassInput]) -> GetAvailableBusinessObjectTypesResponse:
        """    
             This operation returns Business Object names and their display names for each
             primary Business Object given as the input.  Returned Business Object lists have
             exclusions of Business Objects and their secondary Business Objects as specified
             in the input. If any of the returned Business Objects is also a primary Business
             Object then this operation may not return its secondary Business Objects by default.
             In order to return its secondary Business Objects also, it is required to add this
             Business Object name to following preference TYPE_DISPLAY_RULES_list_types_of_subclasses.
             
             Please see the Preferences and Environment Variables Reference documentation for
             preference TYPE_DISPLAY_RULES_list_types_of_subclasses for more information.
             
             This is a lightweight way of getting all displayable Business Objects by name rather
             than model object.
             

        :param Classes: 
                         A list of primary Business Object names and their exclusion list.
             
        :return: A map of given base class name and its available instance types. Failure will be
             returned with error messages in service data.
        """
        ...
    def CreateDatasets(self, Input: list[DatasetInfo]) -> CreateDatasetsResponse:
        """    
             This operation creates a list of Dataset objects, sets the requested attribute
             data, adds named references, fetches write tickets for files that will be uploaded
             as named references and creates the specified relation type between created Dataset
             and input container object. The caller needs to convert the structure members from
             the output Core::_2010_04::Datamanagement::CommitDatasetFileInfo to the input Core::_2006_03::Filemanagement::CommitDatasetFileInfo
             if the caller wants to use the 2010_04  version of createDatasets in combination
             with commitDatasetFiles.
             

Teamcenter Component:

             Core Model Dataset - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform.  This component defines class
             'Dataset' behavior.
             
        :param Input: 
                         Input list of DatasetInfo structures
             
        :return: lists
             of created and updated objects respectively.  Any failure will be returned with clientId
             mapped to error message in the ServiceData list of partial errors but no partial
             error will be issued if relation creation fails.
        """
        ...
    def GetDatasetCreationRelatedInfo2(self, TypeName: str, ParentObject: Teamcenter.Soa.Client.Model.ModelObject) -> GetDatasetCreationRelatedInfoResponse2:
        """    
             This operation pre-populates Dataset creation information, default new Dataset
             name and Tool names, for a specified Dataset type.  This operation
             is used to get all the information associates with the specified Dataset prior
             to the creation operation. The returned default new Dataset name may be determined
             by the parent container object.
             

Teamcenter Component:

             Core Model Dataset - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform.  This component defines class
             'Dataset' behavior.
             
        :param TypeName: 
                         The desired <b>Dataset</b> type name
             
        :param ParentObject: 
                         The container object under which the new <b>Dataset</b> object will be created
             
        :return: .
        """
        ...
    def GetLocalizedProperties(self, Info: list[PropertyInfo]) -> LocalizedPropertyValuesList:
        """    
             Typically business object property values are returned in the locale of the current
             session, this operation returns desired property values in any of the supported locales
             of the Teamcenter server.  String type properties may be localized with values for
             each supported locale, this operation will return the translated values for one or
             more desired locales.
             

Use Cases:

Retrieve the localized values for localizable property
             

When running Teamcenter in language environment other than the English, user
             wants to see the localized property value to be displayed in corresponding language
             in the UI.   This operation can be used to fulfill this requirement. By providing
             the desired business object, internal name of the properties, and specific locale
             name(s), this operation will return the localized property value(s) in that particular
             locale(s).
             

Teamcenter Component:

             Core Model L10N framework - The framework to provide a user interface in the locale
             of users as well as manage the product information (metadata, operation data and
             file content) in multiple languages.
             
        :param Info: 
                         A list of desired business objects, property names, and locales to retrieve those
                         properties in.
             
        :return: Â Â Â Â 38044: The property value is not set.
        """
        ...
    def IsPropertyLocalizable(self, InputInfo: list[LocalizableStatusInput]) -> LocalizableStatusResponse:
        """    
             The operation is used to determine if string-type property is localizable or not
             and can retrieve the localizable status for ONE or MORE properties.
             

Use Cases:

Determine whether a string property is marked as localizable property
             

User needs to use this service operation to determine a string property is localizable
             first before he can add the translations to the value of this property.
             


Teamcenter Component:

             Core Model L10N framework - The framework to provide a user interface in the locale
             of users as well as manage the product information (metadata, operation data and
             file content) in multiple languages.
             
        :param InputInfo: 
                         A list of business object type names and internal property names
             
        :return: 
        """
        ...
    def SetLocalizedProperties(self, Info: LocalizedPropertyValuesInfo) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation allows user to set or modify the display values for a localized property
             on a single object. This sets the property values for a single property on an object
             in different locales. With the display values capability, each localized string property
             could have different language translations associated with that.
             

             Please be aware of the following:
             

This operation is only used to set the secondary (not the master)
             values of the localized property. User can still package the master value (with localization
             status marked as "M") in the LocalizedPropertyValuesInfo
             structure, however, the operation will ignore and skip the master value during the
             process.
             
This operation is only used to set the localization values for one
             property. If you want to set the localized values for multiple properties, please
             use operation setLocalizedPropertyValues().
             



Teamcenter Component:

             Core Model L10N framework - The framework to provide a user interface in the locale
             of users as well as manage the product information (metadata, operation data and
             file content) in multiple languages.
             
        :param Info: 
                         The business object and a list of the property name, value and locale of the property
                         value.
             
        :return: 
        """
        ...
    def SetLocalizedPropertyValues(self, Info: list[LocalizedPropertyValuesInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Sets the property values for multiple properties on a single object in different
             locales. With the display values capability, each localized string property could
             have different language translations associated with that. This operation allows
             user to set or modify the display values for the localized properties on a single
             object.
             

             It should be noted that this operation is only used to set the secondary (not the
             master) values of the localized properties. User can still package the master value
             (with localization status marked as "M") in the LocalizedPropertyValuesInfo
             structure, however, the operation will ignore and skip these master values during
             the process.
             


Teamcenter Component:

             Core Model L10N framework - The framework to provide a user interface in the locale
             of users as well as manage the product information (metadata, operation data and
             file content) in multiple languages.
             
        :param Info: 
                         A list of business object, the property name, value and locale of the property value.
             
        :return: 
        """
        ...

