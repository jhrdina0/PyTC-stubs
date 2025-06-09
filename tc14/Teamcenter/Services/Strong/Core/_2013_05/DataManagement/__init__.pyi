import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class DeepCopyData:
    """
    
            The DeepCopyData data structure holds the
            relevant information regarding applicable deep copy rules.
            
    """
    def __init__(self, ) -> None: ...
    AttachedObject: Teamcenter.Soa.Client.Model.ModelObject
    """Other side object."""
    PropertyName: str
    """Name of relation type or reference property for which DeepCopy rule is configured."""
    PropertyType: str
    """
            If Relation, it represents Relation type
            property. If Reference, it represents Reference
            property.
            """
    CopyAction: str
    """DeepCopy action [NoCopy, CopyAsReference, CopyAsObject or Select]."""
    IsTargetPrimary: bool
    """
            If true the target object is processed as primary, otherwise it is processed as a
            secondary object.
            """
    IsRequired: bool
    """
            If true, the copy action can not be modified. If false, the copy action can be changed
            different action by the user. In this case, the copy action field in the revise dialog
            is editable.
            """
    CopyRelations: bool
    """
            If true, the custom properties on the source relation object are copied over to the
            newly-created relation. If false, custom properties are not copied.
            """
    OperationInputTypeName: str
    """OperationInput type name."""
    ChildDeepCopyData: list[DeepCopyData]
    """List of DeepCopy data for the secondary objects on the other side."""
    OperationInputs: System.Collections.Hashtable
    """
            OperationInput field to capture property values of attached object, to apply on copied
            object of attached object. Map of property name(key) and property values(values)
            in string format of attached object, to be set on copied object of attached object.
            The calling client is responsible for converting the different property types (int,
            float, date .etc) to a string using the appropriate toXXXString functions in the
            SOA client  framework Property class.
            """

class GeneratedValue:
    """
    
            This structure contains the  generated value for the input property. It also contains
            the information whether or not the generated values can be modified in the user interface.
            
    """
    def __init__(self, ) -> None: ...
    ErrorCode: int
    """The error encountered during the generation of value."""
    NextValue: str
    """
            The  value generated based on the user exit/naming rule configured on the property.If
            the property has multiple naming rule patterns with counters  and if the selected
            pattern is passed as empty string, the value is generated based on the first pattern
            configured on the naming rule. An error 74006 is returned if the generated value
            does not match the naming rule pattern configured on the property and the nextValue
            is set to empty string. An error 74006 is returned if the generated value does not
            match the naming rule pattern configured on the property and the nextValue is set
            to empty string.
            """
    IsModifiable: bool
    """
            True if the user can modify the generated value.If isModifiable is false the attempts
            to change the generated value shall be prevented at the user interface.
            """

class GeneratedValuesOutput:
    """
    
            This structure contains the values generated for each of the properties supplied
            in  the propertyNameWithSelectedPattern map of corresponding PropertyValuesInput
            structure.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifying string from the source GenerateNextValuesInput."""
    GeneratedValues: System.Collections.Hashtable
    """This contains map of property name and its values."""
    GeneratedValuesOfSecondaryObjects: System.Collections.Hashtable
    """Field contains value for generated secondary object property values."""

class GenerateNextValuesIn:
    """
    The input required to generate the next values.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """A unique string supplied by the caller."""
    OperationType: int
    """
            The type of the operation for which the values are to be generated. 1-CREATE
            
            2-REVISE
            
            3-SAVEAS.
            

            An error 74007 is returned by the generateNextValues operation if the operationType
            value is not in any of the above.
            """
    BusinessObjectName: str
    """
            The name of the business object for which the property values are to be generated.
            An error 39007 is returned by the generateNextValues operation if the type name is
            not valid.
            """
    PropertyNameWithSelectedPattern: System.Collections.Hashtable
    """
            A map of  property name and  naming rule pattern  pairs( string/string ).The key
            is the property name for which the value is to be generated and the value is the
            naming rule pattern string selected for  that property. If no pattern is selected
            for the property  the pattern string  should be empty string. The caller should only
            pass the properties that are autoassignable.
            """
    PropValues: System.Collections.Hashtable
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
            

            An error  74032 is returned if any of the above property values are not provided
            .
            

            The values of the properties are to be provided as strings. For non string type properties
            use the Property.toXXXString functions (ie. toDateString) to covert the actual values
            to a string.
            
"""
    AdditionalInputParams: System.Collections.Hashtable
    """
            A map of extra information which is required by user exits to generate values.
            
            A map where the key (string) is a parameter name and the value (string) is the parameter
            value.
            

            Valid parameters are:
            

            "ruleSuffix":
            
            This is only used when Baseline action to be performed. 'PDR'  should be passed
            as ruleSuffix  in case of Baseline action. An error 74030 is returned if invalid
            ruleSuffix is supplied.
            

            "sourceObject":
            
            The object that is being revised/saved  or  the parent object  during  Dataset creation
            . Its value should be passed as the object UID. An error 74031 is returned if this
            parameter is not provided during revise/save as action.  It is optional in case of
            Dataset creation .
            

            Object Name        |        Operation                |            Value                    |
            
            ============================================|
            
                ITEM                |        Create                    |        NULLTAG                |
            
                                    |        SaveAs                    |        Source
            tag                |
            
                                    |                                    |                                    |
            
                ITEM Revision    |        Create/SaveAs            |        NULLTAG                |
            
                                    |        Revise                    |        Source
            tag                |
            
                                    |        Baseline                    |        Source
            tag                |
            
                                    |                                    |                                    
            |
            
                Identifier            |            Create                |            NULLTAG            
            |    
            
                                    |        Revise/SaveAs            |        
            Source tag            
            |
            
                                    |                                    |                                    
            |
            
                Dataset            |        
            Create                    |        
            Source tag            
            |
            
                                    |        
            SaveAs                |            NULLTAG            
            |
            
                                    |                                    |                                    
            |
            
                CPD Objects    |    Create/Revise/SaveAs    |        
            Source tag            
            |
            
                                    |                                    |                                    
            |
            
            ============================================|
            

            Any parameter other than the above will not be considered.
            
"""
    CompoundObjectInput: System.Collections.Hashtable
    """
            Map for compound property.
            
            A map where the key (string) is a compound property name and the value (vector) is
            vector of GenerateNextValuesIn type.
            

            By using this map user can generate values for its own properties and also values
            for any of its   compound objects's propert. Provided property is autoassignable.
            

            For example user can generate value for "item_id" on item Object and value for "item_revision_id"
            property also using its compound pbject ItemRevision using this map.
            """

class GenerateNextValuesResponse:
    """
    
            This output structure contains service data with partial errors and a list of GeneratedValuesOutput
            each for an entry in the generateNextValuesIn input list.
            
    """
    def __init__(self, ) -> None: ...
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            The Service Data with partial errors for each GenerateNextValuesInput and identified
            by  its clientId.
            """
    GeneratedValues: list[GeneratedValuesOutput]
    """
            A list of GeneratedValuesOutput one for each entry in generateNextvaluesIn input
            list and  identified by its clientId.
            """

class GetChildrenInputData:
    """
    
            This structure defines the object for which to retrieve children and optionally the
            propertyNames from which to retrieve those children.  If propertyNames is undefined,
            then the Teamcenter <Type>_DefaultChildProperties preference is used.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            Identifier used to track the input object.  Primarily this is used to identify which
            PartialError corresponds to which input object.
            """
    Obj: Teamcenter.Soa.Client.Model.ModelObject
    """The object for which to retrieve children."""
    PropertyNames: list[str]
    """
            The properties to use to retrieve children.  Only the properties defined in this
            list are used. If this list is empty, then the children are returned based on the
            <Type>_DefaultChildProperties and <Type>_PseudoFolders preferences.  Please
            see the Preferences and Environment Variables Reference and the RichClient
            Interface Guide for information on configuring there preferences
            """

class GetChildrenOutput:
    """
    This structure contains the children output for the defined property name.
    """
    def __init__(self, ) -> None: ...
    Children: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            This is the list of Teamcenter business object children which exist within this property
            name.
            """
    PropertyName: str
    """The property the child belongs to in the parent input object."""

class GetChildrenResponse:
    """
    Output structure for the getChildren operation.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The service data contains any partial errors which may have been encountered during
            processing.  All business objects which are returned are added to the serviceData's
            plain objects list.
            """
    ObjectWithChildren: System.Collections.Hashtable
    """A map of requested objects and a list of children(business object/vector<GetChildrenOutput>)."""

class GetPasteRelationsInputData:
    """
    Object input structure of getPasteRelations operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            Identifier used to track the input object.  Primarily this is used to identify which
            PartialError corresponds to which input object.
            """
    Obj: Teamcenter.Soa.Client.Model.ModelObject
    """The parent object for which to get the paste relations."""
    ChildTypeName: str
    """The child type name for which the paste relations will be retrieved."""

class GetPasteRelationsOutput:
    """
    
            Output structure of getPasteRelations operation.  This structure contains all the
            paste relations for a given business object.
            
    """
    def __init__(self, ) -> None: ...
    PasteRelationsInfo: list[PasteRelationsInfo]
    """This is the list of paste relation names and other info for the given business object."""
    IndexOfPreferred: int
    """
            The zero-based index of the preferred paste relation in the list of paste relation
            names.
            """

class GetPasteRelationsResponse:
    """
    
            Response of getPasteRelations operation.  This structure contains the servicedata
            and the outputMap to look up the paste relations for a given business object.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The service data contains any partial errors which may have been encountered during
            processing.  All business objects which are returned are added to the serviceData's
            plain objects list.
            """
    OutputMap: System.Collections.Hashtable
    """A map of input parent object to a vector of GetPasteRelationsOutput objects."""

class PasteRelationsInfo:
    """
    Object output structure of getPasteRelations operation.
    """
    def __init__(self, ) -> None: ...
    PasteRelationName: str
    """The paste relation name."""
    IsExpandable: bool
    """
            A flag indicating whether the relation will enable the children to be shown under
            the parent when expanded.
            """

class ReviseIn:
    """
    
            Input structure for reviseObjects operation
            of any revisable object.
            
    """
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """Target object being revised"""
    ReviseInputs: System.Collections.Hashtable
    """
            Map of property name(key) and property values(values) in string format, to be set
            on new object being created with revise. The calling client is responsible for converting
            the different property types (int, float, date .etc) to a string using the appropriate
            toXXXString functions in the SOA client framework Property class.
            """
    DeepCopyDatas: list[DeepCopyData]
    """
            Relevant information regarding applicable deep copy rules for the objects attached
            to the targetobject.
            """

class ReviseObjectsResponse:
    """
    
            Output structure of reviseObjects operation
            have information of new resultant objects created and error information if any.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[ReviseOut]
    """The target object and the newly created revised objects."""
    ReviseTrees: list[ReviseTree]
    """
            List corresponding to the input target objects that holds mapping between the original
            objects and the copied objects.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Data containing created objects, errors, etc."""

class ReviseOut:
    """
    
            Member of Output structure of reviseObjects
            operation, having information of original and newly created objects.
            
    """
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """Original object being revised."""
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of newly created objects during revise operation."""

class ReviseTree:
    """
    
            Member of Output structure of reviseObjects
            operation, having information of attached objects and newly created objects from
            them.
            
    """
    def __init__(self, ) -> None: ...
    OriginalObject: Teamcenter.Soa.Client.Model.ModelObject
    """Original object."""
    ObjectCopy: Teamcenter.Soa.Client.Model.ModelObject
    """
            Object copy after Revise. This could be NULL if no copy was made or same as original
            object if the copy is a reference to the original.
            """
    ChildReviseNodes: list[ReviseTree]
    """List of child revise nodes for next level of the tree."""

class SubTypeNamesInput:
    """
    
            The parent business object type name and context for which the sub business object
            type names are to be retrieved.
            
    """
    def __init__(self, ) -> None: ...
    TypeName: str
    """
            The business object type name for which sub business object type names are to be
            returned. If all sub business object type names are needed then pass BusinessObject
            as input.
            """
    ContextName: str
    """
            Context name based on which server returns the business object type names.
            

            Supported contexts:
            

            subtypes: Returns all sub business object type names.
            """
    ExclusionPreference: str
    """
            Name of the preference to be used to exclude the sub business object type names from
            the output. Preference needs to be a multi-valued to specify the names of the business
            object types to be excluded.
            

            This is optional. It could be empty string.
            """

class SubTypeNamesOut:
    """
    
            This is the output structure which holds list of sub business object type names for
            a given business object type based on the context specified.
            
    """
    def __init__(self, ) -> None: ...
    TypeName: str
    """The parent business object type name."""
    ContextName: str
    """Name of the context for which  the typeName represents."""
    ExclusionPreference: str
    """
            Name of the preference to be used to exclude the sub business object type names from
            the output. Preference needs to be a multi-valued to specify the names of the business
            object types to be excluded.
            

            This is optional. It could be empty string.
            """
    SubTypeNames: list[str]
    """List of sub business object type names based on the context name."""
    DisplayableSubTypeNames: list[str]
    """List of sub business object type displayable names based on the context name."""

class SubTypeNamesResponse:
    """
    
            The returned business object type names based on the context for each input business
            object type.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[SubTypeNamesOut]
    """List of  business object type names."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service data."""

class ValidateInput:
    """
    
            This structure contains the necessary input for the validateValues
            operation to support generic property validation while retaining support for some
            existing user exits for specific properties.  The validateValues
            operation details legacy user exit support.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller.  This ID is used to identify return data
            elements and partial errors associated with this input structure.
            """
    OperationType: int
    """
            The operation type for which the input values are to be validated. Valid values are:
            


0 for create
            
1 for revise
            
2 for saveas
            
3 for generic validation
            

"""
    BusinessObjectName: str
    """The name of the business object for which the property values are to be validated."""
    PropValuesMap: System.Collections.Hashtable
    """
            A map where the key (string) is a property name and the value (string) is the property
            value to be validated.  The value input is a list to support multi-value properties.
            The values of the properties are to be provided as strings.
            """
    CompoundObjectInput: System.Collections.Hashtable
    """
            A map where the key (string) is a property name and the value (ValidateInput) is input for the property. This contains the property
            values of the secondary objects.
            """

class ValidateValuesResponse:
    """
    The response from the validateValues operation.
    """
    def __init__(self, ) -> None: ...
    ValidationResults: System.Collections.Hashtable
    """
            A map where the key (string) is the clientId
            and the value (ValidationResults) is a list
            of validation results for the properties.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data containing errors that occurred during the operation."""

class ValidationResults:
    """
    
            This structure holds the property validation results for validateValues
            operation.
            
    """
    def __init__(self, ) -> None: ...
    UniqueID: bool
    """If true, the MFK value is unique.  If false, the MFK value is not unique."""
    ValidationStatus: list[ValidationStatus]
    """
            A list of ValidationStatus, which contains the validation status for each
            input property value.
            """

class ValidationStatus:
    """
    This structure holds the validation status for a property.
    """
    def __init__(self, ) -> None: ...
    PropName: str
    """The property name."""
    ValueStatus: int
    """
            The status of the property value validation. The possible values are:
            


0 for valid - The input value is valid for use as-is.
            
1 for invalid - The input value is not valid and cannot be used.
            
2 for override - The input value cannot be used, but should be replaced
            by the value in the modifiedValue field.
            
3 for duplicate - The input value is not valid because it is considered
            a duplicate and cannot be used.
            

"""
    ModifiedValue: list[str]
    """
            The modified property value if the input value is modified by the user exit or by
            naming rule validation according to naming rule pattern and case specification. The
            modified property value should be used for subsequent create, saveAs and revise operation.
            It will hold value if property value validation status is override i.e.
            valueStatus = 2 otherwise it will be empty.
            
            This is a list to support multi-value properties.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPasteRelations(self, Inputs: list[GetPasteRelationsInputData]) -> GetPasteRelationsResponse:
        """    
             Returns the paste relation names for the given parent types and the child types,
             within which the expandable relations and the preferred paste relation are indicated.
             

Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param Inputs: 
                         The list of  the parent object and the child type.
             
        :return: 39030: No preferred paste relation was found for the type.
        """
        ...
    def ReviseObjects(self, ReviseIn: list[ReviseIn]) -> ReviseObjectsResponse:
        """    
             This operation is generic single revise operation for revisable business objects.
             This operation revises the given objects and copies or creates new objects using
             the data for the property values and deep copy data. Deep copy processing is recursive
             such that relations between secondary objects, or from secondary objects to the revised
             object, are replicated during this revise operation based upon deep copy rule configuration.
             This operation supports codeless configuration of custom properties. The following
             lists of revisable types are supported for this operation:
             

ItemRevision ( foundation template) and its sub-types
             
Identifier ( foundation template ) and its sub-types
             
Mdl0ConditionalElement (CPD solution ) and its sub-types
             



Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param ReviseIn: 
                         Input data containing target object and DeepCopyData of the attached objects
             
        :return: 
        """
        ...
    def ValidateValues(self, Inputs: list[ValidateInput]) -> ValidateValuesResponse: ...
    def GetChildren(self, Inputs: list[GetChildrenInputData]) -> GetChildrenResponse:
        """    
             This operation returns the children for each input object.  The children returned
             is determined by the input propertyNames
             list of strings which defines the properties which are to be processed in order to
             collect the children to be returned  If the propertyNames
             list is empty, then the properties which are processed to object the children is
             based on the <Type>_DefaultChildProperties and <Type>_DefaultPseudoFolder preferences.
             Please see the Preferences and Environment Variables Reference and the
             RichClient Interface Guide for information on configuring these preferences.
             Children for which the user does not have read-access will be excluded from the returned
             list of children. No partial error is given if the propertyNames
             list or the <Type>_DefaultChildProperties preference contains an invalid property
             name for the input object, children for the remaining propertyNames
             will be returned.
             

Use Cases:

             Assume the following data exists in Teamcenter:
             
             Item
             
                 Item Revision
             
                 Item Master Form
             

             The ItemRevision exists in the Item's "revision_list" property.
             
             Item Item Master Form exists in the Item's "IMAN_master_form" property.
             

Use case 1 (Get all children/no filter)

             1.    The user selects the Item in the above data in a tree viewer
             which shows all objects.
             
             2.    The user clicks the "+" to expand the Item.
             
             3.    The client then invokes getChildren with the selected object
             (Item), and no entries in the propertyNames
             argument.
             
             4.    getChildren determines the selected object's type, retrieves
             <Type>_DefaultChildProperties and <Type>_PseudoFolders preferences, and returns
             the Item Revision and Item Master Form, their type objects, and the propertyName
             in which they exist related to the parent.
             
             5.    The client then displays the returned list of children
             as child nodes in the tree.
             

Use case 2 (Get subset of children/with filter)

             1.    The user selects the Item in the above data in a tree viewer
             which only shows object related via the revision_list property.
             
             2.    The user clicks the "+" to expand the Item.
             
             3.    The client then invokes getChildren with the selected object
             (Item), and gives "revision_list" in the propertyNames
             list.
             
             4.    getChildren iterates over the propertyNames list, and returns
             the Item Revision object, its child type object, and the propertyName in which it
             exists related to the parent.
             
             5.    The client then displays the returned list of children
             as child nodes in the tree.
             


Teamcenter Component:

             Core Model Method Layer - A set of capabilities/functionality (data model and behaviours)
             that form the very core of our PLM platform. This component defines basic method
             structure.
             
        :param Inputs: 
                         The list of objects and desired children for which to expand and return children.
             
        :return: The partial error 236027 (error) is returned if there is an error retrieving the
             value for a valid property.
        """
        ...
    def GetSubTypeNames(self, InBOTypeNames: list[SubTypeNamesInput]) -> SubTypeNamesResponse:
        """    
             This operation returns sub business object type names for each business object type
             name given as the input for the specified context.
             

             It returns the input base type in the sub business object type names list too.
             

Teamcenter Component:

             Core Model Types - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Types
             framework.
             
        :param InBOTypeNames: 
                         A list of business object type names with the desired context.
             
        :return: 39031: The requested context is not supported
        """
        ...
    def GenerateNextValues(self, GenerateNextValuesIn: list[GenerateNextValuesIn]) -> GenerateNextValuesResponse:
        """    
             This operation generates values for the given properties of an object(s) during create/revise/save
             as action based on the user exits or naming rules configured on those properties.
             Customer user exits are given priority over the naming rules if both of them are
             configured on the same property. The counter has to be set active on the naming rule
             in order to generate the next value for a property. This operation also performs
             naming rule and multi field key validation on the generated values and return appropriate
             partial errors if the validation fails.
             
             This operation does not support generating values for attached Revision Name Rules
             on an Object type.
             
             For user exit support, an existing user exit will be called to generate values. Right
             now we support below given user exits for corresponding Object type.
             

             Object: Item
             
             User exit name: USER_new_item_id
             
             Property: item_id
             

             Object: ItemRevision
             
             User exit name: USER_new_revision_id, USER_new_revision_id_from_alt_rule (Baseline)
             
             Property: item_revision_id
             

             Object: Dataset
             
             User exit name: USER_new_dataset_id
             
             Property: pubr_object_id
             

             Object: Dataset
             
             User exit name: USER_new_dataset_rev
             
             Property: rev
             

             Object: Identifier
             
             User exit name: IDFR_new_alt_id, IDFR_new_rev_id (In Revise case)
             
             Property: idfr_id
             

             Object: CPD Objects
             
             User exit name: USER_new_cpd_id
             
             Property: CPD Objects related property
             

             Each of these user exits need some specific inputs which are required by them to
             generate IDs. These inputs are part of "generateNextValuesIn" structure and are described
             in details in its description.
             

Use Cases:

             a)    User clicks on assign button in Create/Revise/Saveas dialog:
             

             Autoassignable properties are those that have either a user exit or a naming rule
             with counter configured.A constant "autoassignable" is defined on the PropertyDescription
             class and its value can be obtained using PropertyDescription.getConstant() API.
             "Assign" button is displayed in create/revise/save as dialog to populate their values.
             

             This operation is used  to  generate the values for the autoassignable properties
             when the user clicks on the "Assign" button.The caller should collect the list of
             all autoassignable properties  that do not have any user input and pass them to this
             operation. If  the autoassignable  property has a naming rule , the  naming rule
             pattern selected by the user  for  that property should also be passed as input to
             this operation. In all other cases the naming rule pattern should be passed as empty
             string.
             

             b)    User clicks on finish button in Create/Revise/Saveas dialog:
             

             This operation is also used to generate the values for the autoassignable properties
             when the user clicks "Finish" button in in create/revise/save as dialog. The caller
             should collect the list of  all autoassignable properties that do not have any value
             generated and pass them to this operation. If  the autoassignable  property has a
             naming rule , the  naming rule pattern selected by the user  for  that property should
             also be passed as input to this operation. In all other cases the naming rule pattern
             should be passed as empty string.
             


Teamcenter Component:

             Core Naming Rules - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Naming
             Rules and Revision Naming Rules.
             
        :param GenerateNextValuesIn: 
                         [ 1. CREATE 2. REVISE 3. SAVE-AS ].
             
        :return: 
        """
        ...

