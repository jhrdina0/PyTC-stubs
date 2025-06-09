import System
import System.Collections
import Teamcenter.Services.Strong.Core._2008_06.DataManagement
import Teamcenter.Services.Strong.Core._2010_04.DataManagement
import Teamcenter.Services.Strong.Core._2013_05.DataManagement
import Teamcenter.Services.Strong.Core._2014_10.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreatableBusinessObjectsOut:
    """
    
            This structure contains a list of creatable business object names under a given business
            object (hierarchy of creatable sub business objects).
            
    """
    def __init__(self, ) -> None: ...
    BoName: str
    """Name of the business object"""
    CreatableBONames: list[Teamcenter.Services.Strong.Core._2010_04.DataManagement.BusinessObjectHierarchy]
    """Creatable business object hierarchy"""

class CreatableSubBONamesInput:
    """
    
            Represents the parent business object name, exclusion preference and/or exclusion
            business object names, and the context using which the sub business object names
            are to be retrieved.
            
    """
    def __init__(self, ) -> None: ...
    BoName: str
    """
            The primary business object name for which creatable sub business object names are
            to be returned. If all creatable sub business object names are needed, then "BusinessObject"
            should be passed as input.
            """
    ExclusionPreference: str
    """
            Name of the preference to be used to exclude the sub business object names from the
            output. Preference needs to be a multi-valued to specify the names of the business
            objects to be excluded. This parameter is optional.
            """
    ExclusionBONames: list[str]
    """
            List of business object namess (and their secondary business objects) to be excluded
            from returned list. This parameter is optional.
            """
    Context: str
    """
            Context based on which server returns the creatable business object names. If there
            is no value specified for the context, all the creatable sub business objects for
            the business object will be returned.
            
            Supported contexts:
            
legacy: Returns sub business object names from sub classes of the given primary
            business object, if the primary business object name is listed in the TYPE_DISPLAY_RULES_list_types_of_subclasses
            site preference.
            
            Please see the Preferences and Environment Variables Reference documentation for
            more information on preference TYPE_DISPLAY_RULES_list_types_of_subclasses.
            """

class CreatableSubBONamesResponse:
    """
    This structure holds the list of creatable business objects and their display names
    """
    def __init__(self, ) -> None: ...
    Output: list[CreatableBusinessObjectsOut]
    """
            List of output objects representing the creatable business objects displayable in
            the Create dialog
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data including the partial errors that are mapped to the input primary business
            objects
            """

class CreateInput2:
    """
    
CreateInput2 is a structure used to capture the inputs required for creation
            of a business object. This is a recursive structure containing the CreateInput2
            (s) for any secondary (compounded) objects that might be created (e.g Item
            also creates ItemRevision and ItemMasterForm etc.).
            
    """
    def __init__(self, ) -> None: ...
    BoName: str
    """Business Object type name."""
    PropertyNameValues: System.Collections.Hashtable
    """
            Map (string/list of strings)  of property name (key) and to property values (values)
            in string format, to be set on new object being created. Note: The calling client
            is responsible for converting the different property types (int, float, date .etc)
            to a string using the appropriate function(s) in the client framework Property class
            (i.e. Property.toDateString).
            """
    CompoundCreateInput: System.Collections.Hashtable
    """CreateInput2 (s) for compounded objects."""

class CreateIn2:
    """
    This is an input structure for create operation including unique client identifier.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique client identifier."""
    CreateData: CreateInput2
    """Input data for create operation."""
    DataToBeRelated: System.Collections.Hashtable
    """
            Additional input data. This data (string/list of strings) will be related to the
            created object by the given property.
            """
    WorkflowData: System.Collections.Hashtable
    """
            Input data (string/list of strings) required for workflow creation.
            
submitToWorkflow - true/false
            
            NOTE: If the above option is "true" then workflow process template to be used for
            workflow creation should be specified in the preference (<TypeName>_default_workflow_template)
            defined for the created object type.
            """
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """Target to which the created object will be pasted."""
    PasteProp: str
    """Property to be used to paste the created object to the target."""

class DeepCopyDataInput:
    """
    Input structure for getDeepCopyData operation
    """
    def __init__(self, ) -> None: ...
    Operation: str
    """
            This is the one of the operation types
            

SaveAs
            
Revise
            

"""
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """The target business object which user wants to do save-as/or revise."""
    DeepCopyDatas: list[Teamcenter.Services.Strong.Core._2014_10.DataManagement.DeepCopyData]
    """
            This contains the list of DeepCopyData for targetObject
            which is the object User wants to do "saveAs"/"revise".
            """
    ParentDeepCopyData: Teamcenter.Services.Strong.Core._2014_10.DataManagement.DeepCopyData
    """
            This contains parent DeepCopyData of selctedBO.
            It also stores the nested deep copy data at the next level.
            """
    SelectedBO: Teamcenter.Soa.Client.Model.ModelObject
    """This is the business object which User wants to change copy action."""

class DomainOfObjectOrTypeResponse:
    """
    The identified domain information for the design artifact or type name will be returned.
    """
    def __init__(self, ) -> None: ...
    Output: list[DomainOutput]
    """The domain information output."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation."""

class DomainOutput:
    """
    The identified domain information for input object or type name.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input."""
    Domain: str
    """The application domain information identified for the input object or type."""

class GetDeepCopyDataResponse:
    """
    
            Structure that contains the DeepCopyData embedded within which is a recursive data
            structure. The DeepCopyData contains information about how the secondary objects
            (related and referenced objects) are to be copied (reference, copy as object, no
            copy).
            
    """
    def __init__(self, ) -> None: ...
    SelectedBOIsDuplicated: bool
    """
            This indicates whether the selectedBO from
            the method input already has DeepCopyData in deepCopyDatas from the method
            input or not.
            """
    DeepCopyDatas: list[Teamcenter.Services.Strong.Core._2014_10.DataManagement.DeepCopyData]
    """
            A list of DeepCopyData for the selectedBO
            from the method input. The DeepCopyData object contains all the information about
            how the attached objects are to be copied (Copy as Object, Copy as Reference, NoCopy,
            etc.). DeepCopyData is a recursive data structure that contains the details for the
            attached objects at the next level.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data containing errors, etc. The plain object list of the Service data is
            populated with the target objects which are to be copied as part of the saveAs/revise
            operation. If there is an error retrieving Business Object for the business object
            name corresponding to the target object, it is added to the error stack of the ServiceData
            as a partial error.
            """

class GetDomainInput:
    """
    Input structure for getDomainOfObjectOrType operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    InputDesignArtifact: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            Design artifact for which domain information is to be identified and returned. Design
            artifact is of type WorkspaceObject.
            """
    TypName: str
    """
            Type name  of BusinessObject for which domain information is to be identified and
            returned. If inputDesignArtifact is empty then only  typName will be processed.
            """

class LocalizedPropertyValuesInfo2:
    """
    This data structure contains business object tag and a list of NameValueLocaleStruct
    """
    def __init__(self, ) -> None: ...
    BusinessObject: Teamcenter.Soa.Client.Model.ModelObject
    """The business object"""
    PropertyValues: list[NameValueLocaleStruct2]
    """A list of NameValueLocaleStruct that holds property name, value and locale information."""

class LocalizedPropertyValuesResponse:
    """
    
            This structure contains a list of output localized property value info and partial
            error.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[LocalizedPropertyValuesInfo2]
    """
            A list of structure LocalizedPropertyValuesInfo2 to keep the localized property values
            info.
            """
    PartialErrors: Teamcenter.Soa.Client.Model.ServiceData
    """Used for storing partial error and standard service data."""

class NameValueLocaleStruct2:
    """
    This data structure contains localization related information for property values.
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
            A list of localization status values.
            
            The status must be one of the following values:
            

            For the approved status: "A", "Approved" or the version of the "Approved" string
            for the client/server log-in locale.
            
            For the in-review status: "R", "In Review", "In-Review", "InReview" or the version
            of the "In Review" string for the client/server log-in locale.
            
            For the pending status: "P", "Pending" or the version of the "Pending" string for
            the client/server log-in locale.
            
            For the invalid status: "I", "Invalid" or the version of the "Invalid" string for
            the client/server log-in locale.
            
            For the master status: "M", "Master" or the version of the "Master" string for the
            client/server log-in locale.
            """
    InternalStatus: list[str]
    """
            A list of internal values of the status.
            
            The status must be one of the following values:
            
            "approved" for the approved status: "A"
            
            "in review" for the in-review status: "R"
            
            "pending" for the pending status: "P"
            
            "invalid" for the invalid status: "I"
            
            "master" for the master status: "M"
            """
    StatusDesc: list[str]
    """A list of descriptions of statuses used for tooltip on the user interface."""
    Master: bool
    """Master value indication"""

class PropertyNamingruleInfo:
    """
    
            This operation generates values for the given properties of an object(s) during create/revise/save
            as action based on the user exits or naming rules configured on those properties.Customer
            user exits are given priority over the naming rules if both of them are configured
            on the same property. The counter has to be set active on the naming rule in order
            to generate the next value for a property. This operation also performs naming rule
            and multi field key validation on the generated values and return appropriate partial
            errors if the validation fails.
            

            For user exit support, an existing user exit will be called to generate values. Right
            now we support below given user exits for corrosponding Objest type.
            

            Object: Item
            
            User exit name: USER_new_item_id
            
            Property: item_id
            

            Object: ItemRevision
            
            User exit name: USER_new_revision_id, USER_new_revision_id_from_alt_rule(Baseline)
            
            Property: item_revision_id
            

            Object: Dataset
            
            User exit name: USER_new_dataset_id
            
            Property: pubr_object_id
            

            Object: Dataset
            
            User exit name: USER_new_dataset_rev
            
            Property: rev
            

            Object: Identifier
            
            User exit name: IDFR_new_alt_id, IDFR_new_rev_id(In Revise case)
            
            Property: idfr_id
            

            Object: CPD Objects
            
            User exit name: USER_new_cpd_id
            
            Property: CPD Objects related property
            

            These each user exits need some specific inputs which are required by them to generate
            ids. These inputs are part of "generateNextValuesIn" structure and are described
            in details in its description.
            

    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the PropertyNamingruleInfo. This can be used by the caller
            to identify this data structure with the source input data.
            

"""
    OperationType: int
    """
            The type of the operation for which the values are to be generated.
            
            1-CREATE
            
            2-REVISE
            
            3-SAVEAS.
            

            An error 74007 is returned by the generateNextValues operation if the operationType
            value is not in any of the above.
            
"""
    BusinessObjectTypeName: str
    """
            The business object type name (for e.g. Item, Dataset or Form etc)   for which unique
            ID generation is required.
            """
    PropertyNameAttachedPattern: System.Collections.Hashtable
    """
            A map of property name and naming rule pattern pairs( string/string ).The key is
            the property name for which the value is to be generated and the value is the naming
            rule pattern string selected for that property. If no pattern is selected for the
            property the pattern string should be empty string. The caller should only pass the
            properties that are autoassignable.
            """
    PropertyValuesMap: System.Collections.Hashtable
    """
            A map of property name and values list(string/vector) of all the properties that
            are provided as inputs to create/revise/save as action of an object excluding the
            properties whose values are needed to be generated.If a multi field key is configured
            on the object ,the values of the constituent properties of the multi field key other
            than the ones for which the values are currently being generated are obtained from
            this map in order to perform the validation.
            
            The entries in this map are also used to generate values for the autoassignable properties
            of some business objects.
            

            Eg:
            
            Identifier: "idContext" value is needed to generate "idfr_id" property value
            

            An error 74032 is returned if any of the above property values are not provided .
            

            The values of the properties are to be provided as strings. For non string type properties
            use the Property.toXXXString functions (ie. toDateString) to covert the actual values
            to a string.
            
"""
    AdditionalInputMap: System.Collections.Hashtable
    """
            A map of extra information which is required by user exits to generate values.
            
            A map where the key (string) is a parameter name and the value (string) is the parameter
            value.
            

            Valid parameters are:
            

            "ruleSuffix":
            
            This is only used when Baseline action to be performed. 'PDR' should be passed as
            ruleSuffix in case of Baseline action. An error 74030 is returned if invalid ruleSuffix
            is supplied.
            

            "sourceObject":
            
            The object that is being revised/saved or the parent object during Dataset creation
            . Its value should be passed as the object UID. An error 74031 is returned if this
            parameter is not provided during revise/save as action. It is optional in case of
            Dataset creation .
            

            Object Name        |        Operation                |            Value
            |
            
            ============================================|
            
            ITEM                |        Create                    |        NULLTAG
            |
            
            |        SaveAs                    |        Source tag
            |
            
            |                                    |
            |
            
            ITEM Revision    |        Create/SaveAs            |        NULLTAG
            |
            
            |        Revise                    |        Source tag
            |
            
            |        Baseline                    |        Source tag
            |
            
            |                                    |
            |
            
            Identifier            |            Create                |            NULLTAG
            |
            
            |        Revise/SaveAs            |         Source tag
            |
            
            |                                    |
            |
            
            Dataset            |         Create                    |         Source tag
            |
            
            |         SaveAs                |            NULLTAG
            |
            
            |                                    |
            |
            
            CPD Objects    |    Create/Revise/SaveAs    |         Source tag
            |
            
            |                                    |
            |
            
            ============================================|
            

            Any parameter other than the above will not be considered.
            
"""
    CompoundObjectInput: System.Collections.Hashtable
    """
            Map for compound property.
            
            A map where the key (string) is a compound property name and the value (vector) is
            vector of PropertyNamingruleInfo type.
            

            By using this map user can generate values for its own properties and also values
            for any of its compound objects's propert. Provided property is autoassignable.
            

            For example user can generate value for "item_id" on item Object and value for "item_revision_id"
            property also using its compound pbject ItemRevision using this map.
            
"""
    PropertyNameContextListMap: System.Collections.Hashtable
    """This contains key as property name and value as a list of substituted context list."""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetLocalizedProperties2(self, PropertyInfo: list[Teamcenter.Services.Strong.Core._2010_04.DataManagement.PropertyInfo]) -> LocalizedPropertyValuesResponse:
        """    
             Typically business object property values are returned in the locale of the current
             session, this operation returns desired property values in any of the supported locales
             of the Teamcenter server. String type properties may be localized with values for
             each supported locale, this operation will return the translated values for one or
             more desired locales.
             

Use Cases:

             Retrieve the localized values for localizable property
             

             When running Teamcenter in language environment other than the English, user wants
             to see the localized property value to be displayed in corresponding language in
             the UI. This operation can be used to fulfill this requirement. By providing the
             desired business object, internal name of the properties, and specific locale name(s),
             this operation will return the localized property value(s) in that particular locale(s)
             and the internal value(s) of the status corresponding to localized value(s) in that
             locale(s).
             

Teamcenter Component:

             Core Model L10N framework - The framework to provide a user interface in the locale
             of users as well as manage the product information (metadata, operation data and
             file content) in multiple languages.
             
        :param PropertyInfo: 
                         A list of desired business objects, property names, and locales to retrieve those
                         properties in.
             
        :return: 38044: The property value is not set.
        """
        ...
    def GetCreatbleSubBuisnessObjectNames(self, Input: list[CreatableSubBONamesInput]) -> CreatableSubBONamesResponse:
        """    
             This operation returns sub business object  names that are displayable to the login
             user in the object creation dialog and their display names for each primary business
             object given as the input, based on specified context. Returned business object lists
             have exclusions of business objects and their secondary business objects as per the
             exclusion preference and/or exlusion business object names specified in the input.
             If the context is specified as legacy, the sub business objects of the primary business
             object are returned only if the primary business object is listed in the site preference
             TYPE_DISPLAY_RULES_list_types_of_subclasses. If the context is left blank, then all
             creatable sub business objects are returned. This operation returns the hierarchy
             of creatable objects for each business object it returns.
             

Use Cases:

Use Case 1: Get all Creatable sub business object names for a given business object

             While creating an object of a business object, user needs to know all the sub business
             objects that can be created. To get all creatable sub business objects for a given
             business object for the logged in user, this operation should be invoked by providing
             empty value for context. Any specific sub business objects that need to be excluded
             from the returned list, can be specified through exclusionPreference and/or exclusionBONames
             parameters.
             

Use Case 2: Get Creatable sub business objects for a given primary business object,
             excluding sub business objects from its sub classes

             While creating an object of a primary business object, user needs to know only the
             sub business objects that can be created for the primary business object, excluding
             the business objects from its sub classes, for example, in the legacy Create wizards
             from Teamcenter Rich Application Client. To get only the creatable direct sub business
             objects for a given primary business object for the logged in user, this operation
             should be invoked by providing legacy as the value for context parameter.
             

Teamcenter Component:

             Core Model Types - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Types
             framework.
             
        :param Input: 
                         A list of primary business object names and the exclusion preferences and/or types,
                         along with context, for which the creatable sub business object names are to be retrieved
             
        :return: 
        """
        ...
    def GenerateNextValuesForProperties(self, PropertyNamingRuleInfo: list[PropertyNamingruleInfo]) -> Teamcenter.Services.Strong.Core._2013_05.DataManagement.GenerateNextValuesResponse: ...
    def GetDomainOfObjectOrType(self, Inputs: list[GetDomainInput]) -> DomainOfObjectOrTypeResponse: ...
    def CreateRelateAndSubmitObjects2(self, CreateInputs: list[CreateIn2]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateResponse: ...
    def GetDeepCopyData(self, DeepCopyDataInput: DeepCopyDataInput) -> GetDeepCopyDataResponse:
        """    
             This operation returns information required to perform save-as/revise after user
             changes the default copy action to one of the following copy actions for one of the
             secondary objects:
             

Copy As Object
             
Revise Object
             
Revise and Relate to Latest
             

             .
             

Use Cases:

             After a user changes the copy action for one of the secondary objects in the DeepCopy
             panels, Client will need to call this operation to construct the DeepCopy panels
             in save-as wizard for user input for that secondary object. Once the user input is
             received, client can make subsequent invocation to the DataManagement.saveAsObjectsAndRelate
             operation to execute SaveAs on the object.
             

Dependencies:

             saveAsObjectsAndRelate
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param DeepCopyDataInput: 
                         The information about the business object (which save-as and revise will be performed
                         ), its DeepCopyData, the business object for which the user changed the copy action
                         and its parent DeepCopyData.
             
        :return: 
        """
        ...

