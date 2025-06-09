import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateInput:
    """
    
CreateInput is a structure used to capture
            the inputs required for creation of a business object. This is a recursive structure
            containing the CreateInput(s) for any secondary
            (compounded) objects that might be created (e.g. Item also creates ItemRevision
            and ItemMasterForm).
            
    """
    def __init__(self, ) -> None: ...
    BoName: str
    """Business Object name."""
    PropertyNameValues: System.Collections.Hashtable
    """
            A map (string, PropertyValues) of property
            name and values pairs that need to be part of create input.
            """
    CompoundCreateInput: System.Collections.Hashtable
    """
            Compounded create input in case the business object needs secondary object to be
            created.
            """

class CreateObjectInfo:
    """
    
CreateObjectInfo is a structure which provides
            input to create an object.
            
    """
    def __init__(self, ) -> None: ...
    CreInp: CreateInput
    """The CreateInput to create the object."""
    RelationName: str
    """
            The relation to be used to associate the created object to the relateToObject. If this is not provided and relateToObject is provided then the relation type is determined
            using the preference <Primary>_<Secondary>_default_relation. For example,
            if relateToObject is of type ItemRevision and boName is DirectModel then preference
            
            ItemRevision_DirectModel_default_relation used. If not found, then ItemRevision_default_relation
            will be searched for and used.
            """
    RelateToObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The object to which the created object is to be related with the given relationName.
            
            Special cases -
            
            1. Folder object without relationName
            is passed then the created object is added as a folder content.
            
            2. BOMLine is passed then the system creates an attachment line.
            """

class CreateOrUpdateObjectInfo:
    """
    
CreateOrUpdateObjectInfo is a structure which
            provides input to either create or update an object.
            
Note: If objectToUpdate
            is provided then objectToCreate will be ignored.
            
    """
    def __init__(self, ) -> None: ...
    ObjectToCreate: CreateObjectInfo
    """
            The CreateInput to create the object. In
            case a Dataset is requested to be created then the default values for tool_used, dataset_type
            and format_used will be assumed.
            """
    ObjectToUpdate: Teamcenter.Soa.Client.Model.ModelObject
    """The object to be updated."""
    LmdOfObject: System.DateTime
    """
            Last modified date of the input object. If this input date is different than the
            current last modified date and the overwriteForLastModDate
            preference is false, the input will be ignored, and processing will continue with
            the next input. In this scenario, error 215033 will be returned. If the dates are
            different and the overwriteForLastModDate
            preference is true, processing will continue with the current input. In this scenario,
            error 215034 will be returned.
            """
    OverwriteForLastModDate: bool
    """
            Flag to check whether the object needs to be updated if the input last modified date
            is different from the current last modified date of the object in Teamcenter.
            """
    ObjectPropsToUpdate: System.Collections.Hashtable
    """
            A map (string, PropertyValues)
            of property name and values pairs that need to be set on the created or updated object.
            """

class RevisionRuleConfigInfo:
    """
    
RevisionRuleConfigInfo is a structure which
            enables client to pass configuration information for RevisionRule and configuration
            parameters.
            
    """
    def __init__(self, ) -> None: ...
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """The RevisionRule to be used for configuration."""
    UnitNo: int
    """Unit number. The client must pass -1 if unit number is not used for configuration."""
    Date: System.DateTime
    """Effectivity date."""
    Today: bool
    """Effectivity date to use today as the date."""
    EndItem: Teamcenter.Soa.Client.Model.Strong.Item
    """End Item."""
    EndItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """End ItemRevision."""
    OverrideFolders: list[OverrideInfo]
    """A list of Overriding Folder objects."""

class ConfigurationInfo:
    """
    
ConfigurationInfo is a structure which enables
            client to pass configuration information for product structures.
            
    """
    def __init__(self, ) -> None: ...
    RevRuleConfigInfo: RevisionRuleConfigInfo
    """The RevisionRule and the configuration entry parameters."""
    VariantRulesOrOptionSets: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of VariantRule or StoredOptionSet to be used for configuration."""
    ActiveAssemblyArrangement: Teamcenter.Soa.Client.Model.Strong.AssemblyArrangement
    """AssemblyArrangement to be used for configuration."""
    ConfigContext: Teamcenter.Soa.Client.Model.ModelObject
    """
            Configuration object to be used for configuration. If used then revRuleConfigInfo, variantRulesOrOptionSets
            and activeAssemblyArrangement are ignored.
            """
    BomWinPropFlagMap: System.Collections.Hashtable
    """
            A map (string, PropertyValues)
            of property name and values pairs that need to be set on the BOMWindow. A
            pseudo-property of 'search_filter' may be set with a JSON formatted search filter
            criteria to be applied to the product structure being added or updated for the session.
            For Fnd0Workset as a session, all map values will be saved to the product
            structure subset being attached to the session.
            """
    EffGrpRevList: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    """
            A list of Fnd0EffectivityGrp objects, effGrpRevList
            is used along with BOMWindow  to configure.
            """

class StructureContextIdentifier:
    """
    
StructureContextIdentifier is a structure
            in which the application can provide information about the product
            and its configurations that were opened. Using this structure an existing product
            and configuration is provided in the following forms.
            

product: this could be an Item, ItemRevision, BOMView,
            BOMViewRevision or BOMLine or VisStructureContext or recipe
            object. If a BOMLine or VisStructureContext or any recipe object is
            passed then the configInfo need not be provided.
            


    """
    def __init__(self, ) -> None: ...
    Product: Teamcenter.Soa.Client.Model.ModelObject
    """
            This is either an Item, ItemRevision, BOMView, BOMViewRevision,
            BOMLine or StructureContext. The following is list the behaviour based
            on the type of object
            
BOMLine - configInfo need not be provided.
            If configInfo is provided it will be ignored.
            
Item or BOMView - The BOMWindow will be created using the ItemRevision
            by applying the configInfo if provided otherwise
            by applying global RevisionRule on the Item.
            
BOMViewRevision - The BOMWindow will be created using the ItemRevision
            of the BOMViewRevision.
            
VisStructureContext  or any recipe object- If the object is
            already associated to the session nothing is done otherwise a copy of the recipe
            is created and associated to session.The configInfo
            is ignored.
            """
    BomViewType: Teamcenter.Soa.Client.Model.ModelObject
    """
            The PSBOMView type that is to be used to create the BOMWindow. This
            is used only if Item or ItemRevision is supplied as product. If empty
            the default view type is used.
            """
    ConfigInfo: ConfigurationInfo
    """
            The configuration information for the product. This is used only if Item,
            ItemRevision, BOMView, BOMViewRevision are supplied as product.
            """
    ConfigOptions: System.Collections.Hashtable
    """Ignore."""

class ProductStructureRecipe:
    """
    
ProductStructureRecipe contains product,
            configuration and subset information.
            
Note: During update of existing product structure information associated to
            the session the complete information like occurrenceLists,
            searchRecipe and staticStructureFile
            has to be passed
            
    """
    def __init__(self, ) -> None: ...
    StructureContextIdentifier: StructureContextIdentifier
    """The product and the configuration information."""
    OccurrenceLists: list[StructureSubsetInfo]
    """A list of filtered product structure results."""
    SearchRecipe: Teamcenter.Soa.Client.Model.ModelObject
    """
            This is Fnd0SearchRecipe type BusinessObject which defines the search filters
            that were applied on the product structure
            """
    StaticStructureFile: Teamcenter.Soa.Client.Model.Strong.ImanFile
    """
            The ImanFile object that represents the static product structure as expanded
            during the creation of session.
            """

class BaseObjectAttachInfo:
    """
    
BaseObjectAttachInfo is a structure which
            enables to create or update an object and attach it to the session. If relation is
            used to attach object to the session additional properties that are to be set on
            the relation can be passed as input.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The input clientId sent by the client application
            which will enable the client to map the output with the input.
            """
    BaseObjectToCreateOrUpdate: CreateOrUpdateObjectInfo
    """
            The input that has information to create an object or update an object associated
            to the session.
            """
    RelationName: str
    """
            The relation name used to associate the base object to the session. Typically, the
            ImanRelation name.
            """
    AdditionalProps: System.Collections.Hashtable
    """
            A map (string, PropertyValues) of property
            name and values pairs that need to be set on the ImanRelation specified via
            relationName.
            
Note: Incase the relationName is VisManagedDocument,
            the clientId of BaseObjectAttachInfo
            can be passed as fnd0ParentStableId to indicate
            which document is the parent of this document, if this document was inserted into
            another in the session. The operation would first check if any BaseObjectAttachInfo has the clientId
            value same as the provided as fnd0ParentStableId
            value, if yes then the stableId of the BaseObjectAttachInfo is stored as fnd0ParentStableId otherwise the given string provided is stored
            as fnd0ParentStableId.
            """
    Recipe: ProductStructureRecipe
    """
            In case where the relationName is VisManagedDocument,
            the structure configuration information that need to be set on fnd0Recipe property of the relation.
            """

class BaseObjectAttachInfoOutput:
    """
    
BaseObjectAttachInfoOutput holds information
            about the object that was associated to the session.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The input clientId sent by the client application
            which will enable the client to map the output with the input.
            """
    StableId: str
    """
            The identifier that enables the client to identify the association of the opened
            object with the session.
            """
    BaseObject: Teamcenter.Soa.Client.Model.ModelObject
    """The object that was associated to the session."""

class CompositePathIdentifiers:
    def __init__(self, ) -> None: ...
    PathIdentifiers: list[StructurePathIdentifiers]
    """A list of identifiers that identifies the BOMLine in a structure."""

class CreateOrUpdateSessionOutput:
    """
    
CreateOrUpdateSessionOutput contains the
            session object and a list of objects and product structures that were associated
            to the session.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The input clientId sent by the client application
            which will enable the client to map the output with the input.
            """
    SessionObject: Teamcenter.Soa.Client.Model.ModelObject
    """Fnd0AppSession that represents the session."""
    BaseObjectAttachOutputs: list[BaseObjectAttachInfoOutput]
    """
            A list of BaseObjectAttachInfoOutput which
            has information about the objects that were associated to session.
            """
    RecipeOfOpenedProductOutputs: list[StructureRecipeOfProductOutput]
    """
            A list of StructureRecipeOfProductOutput
            that contains information about the product structures that were associated to session.
            """
    ProductSessionDataAttachOutputs: list[BaseObjectAttachInfoOutput]
    """
            A list of Fnd0ProductSessionData objects that were created or updated and
            attached to the session object.
            """

class CreateOrUpdateSessionResponse:
    """
    
CreateOrUpdateSessionResponse contains a
            list of CreateOrUpdateSessionOutput

            Each of which has the session object along with it are the objects and product structures
            that were associated to it. Stable Id that identifies the associated objects is also
            returned which could be used during opening the session or referencing them from
            within the CAD files.
            
    """
    def __init__(self, ) -> None: ...
    SessionOutputs: list[CreateOrUpdateSessionOutput]
    """A list of objects that were associated to the session."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
ServiceData that contains the partial errors
            if any.
            """

class NamedReferenceInfo:
    """
    
NamedReferenceInfo structure contains the
            reference object corresponding to the named reference. If the referenced object is
            ImanFile then the FMS file ticket for it is returned.
            
    """
    def __init__(self, ) -> None: ...
    NamedReferenceType: str
    """The type of reference object."""
    NamedReferenceName: str
    """The NamedReference name of the object."""
    ReferenceObject: Teamcenter.Soa.Client.Model.ModelObject
    """The object reference corresponding to the named reference."""
    FileTicket: str
    """
            The FMS ticket used to retrieve the file in the cases where referenceObject is a file.
            """

class ProductStructureFilter:
    """
    
            This structure enables the client to control how and what product structures are
            to returned in the response.
            
    """
    def __init__(self, ) -> None: ...
    ProductStructure: str
    OutputFilters: System.Collections.Hashtable
    RelativeToSessionStableIds: list[str]
    """
            A list of stable Ids that identifies the association of  product structures to the
            session. This parameter is applicable only if parameter
            productStructure equals UseList
"""
    AdditionalPropsOnBOMWindow: System.Collections.Hashtable
    """
            A map(string,PropertyValues) that specifies
            additional options that need to be set on the BOMWindow while returning the
            session product structure contents.
            """

class ProductSessionDataFilter:
    """
    
ProductSessionDataFilter is a structure in
            which the application can specify the Fnd0ProductSessionData types that are
            associated to the session. The application can either specify the Fnd0ProductSessionData
            by their stable Ids or by their type names.
            
    """
    def __init__(self, ) -> None: ...
    StableIds: list[str]
    """
            A list of stable Ids that identifies the association of Fnd0ProductSessionData
            to the session.
            """
    ProductSessionDataTypeNames: list[str]
    """
            A list of Fnd0ProductSessionData type names. The instances of the given type
            which are associated to the session that are to be retrieved.
            """

class OpenSavedSessionFilter:
    """
    
OpenSavedSessionFilter enables the client
            application to control the output returned during opening a session.
            
    """
    def __init__(self, ) -> None: ...
    RelAndTypesFilter: list[RelationAndTypesFilter]
    """A list of type filter to be applied on the objects that are associated to the session."""
    ProductStructureFilter: ProductStructureFilter
    """
            The filter to control the product structures returned by the operation. This structure
            can be empty in which case the default values as mentioned in the ProductStructureFilter description will be used.
            """
    ProductSessionDataFilter: ProductSessionDataFilter
    """Product Session Data Filter"""

class OpenSessionOutput:
    """
    
OpenSessionOutput contains the launched session
            object,  the associated product structures and objects.
            
    """
    def __init__(self, ) -> None: ...
    SessionObject: Teamcenter.Soa.Client.Model.ModelObject
    """The session Fnd0AppSession object that was opened from the client."""
    SessionProductStructures: list[SessionProductStructureInfo]
    """
            A list of associated product structures that were associated to the session. Typically,
            it contains the BOMWindow object.
            """
    RelatedObjectInfos: list[RelatedObjectInfo]
    """
            A list of RelatedObjectInfo that contains
            information about the objects that were related to the session object.
            """
    ProductSessionDataObjects: list[ProductSessionDataObjectInfo]
    """A list of Fnd0ProductSessionData that are associated to the session."""

class OpenSessionResponse:
    """
    
OpenSessionResponse contains a list of OpenSessionOutput which has the objects and product
            structures associated to the session. Stable Id that identifies the associated objects
            and product structures are also returned which could be used for further references
            to update the session.
            
    """
    def __init__(self, ) -> None: ...
    SessionOutputs: list[OpenSessionOutput]
    """A list of objects and product structures that were associated to the session."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
ServiceData that contains the partial errors
            if any.
            """

class OverrideInfo:
    """
    This contains information about the override RevisionRule Entry.
    """
    def __init__(self, ) -> None: ...
    RuleEntry: Teamcenter.Soa.Client.Model.Strong.CFMOverrideEntry
    """Refers to the CFMOverrideEntry of RevisionRule object."""
    Folder: Teamcenter.Soa.Client.Model.Strong.Folder
    """
            A Folder containing ItemRevision that are to be considered while evaluating
            the RevisionRule.
            """

class ProductSessionDataAttachInfo:
    """
    
ProductSessionDataAttachInfo is a structure
            which enables to create or update an object of type Fnd0ProductSessionData
            and attach it to the session.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The input clientId sent by the client application
            which will enable the client to map the output with the input.
            """
    SessionData: CreateOrUpdateObjectInfo
    """
Fnd0ProductSessionData that has to be created or updated and attached to the
            session object.
            """

class ProductSessionDataObjectInfo:
    """
    
ProductSessionDataObjectInfo has the information
            about Fnd0ProductSessionData that are associated to the session.
            
    """
    def __init__(self, ) -> None: ...
    StableId: str
    """
            The identifier that enables the client to identify the association of the opened
            object with the session.
            """
    ProductSessionDataObject: Teamcenter.Soa.Client.Model.Strong.Fnd0ProductSessionData
    """Fnd0ProductSessionData object associated to the session."""

class PropertyValues:
    """
    
PropertyValues is a structure using which
            the property values that need to be set on objects are sent. Scalar property values
            are also sent via this structure.
            
            Note: In case to set a char property, populate the stringValues
            as shown in example. Example
            
            To set a single char value say Y- provide stringValues[0][0]
            = Y
            
            To set an array of char values YES - provide stringValues[0]
            = YES
            
    """
    def __init__(self, ) -> None: ...
    IntValues: list[int]
    """List of integer values."""
    BoolValues: list[bool]
    """List of boolean values."""
    DateValues: list[System.DateTime]
    """List of date values."""
    StringValues: list[str]
    """List of string values."""
    FloatValues: list[float]
    """List of float values."""
    DoubleValues: list[float]
    """List of double values."""
    TagValues: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of object values."""

class RelatedObjectInfo:
    """
    
RelatedObjectInfo structure contains an object
            associated to session, named references and reference objects.
            
    """
    def __init__(self, ) -> None: ...
    StableId: str
    """
            The identifier that enables the client to identify the association of the opened
            object with the session.
            """
    RelatedObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The resulting related object by following a relation specified in the OpenSavedSessionFilter.
            """
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """
            This is  only populated when the relatedObject
            is associated with Fnd0AppSession with VisManagedDocument relation.
            The BOMWindow is constructed using fnd0Recipe
            property on the relation.
            """
    RecipeObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The recipe object of the structure which can be opened outside the context of the
            session. Typically it is the a VisStructureContext object but it could be
            any object which is capable of reconstructing the BOMWindow and hence the
            client should not assume the type of object to particular type. This is only populated
            when the relatedObject is associated with
            Fnd0AppSession with VisManagedDocument relation and the relation has
            the fnd0Recipe property populated.
            """
    RelationProperties: System.Collections.Hashtable
    """
            A map(string,PropertyValues) on the relation
            that associated the session and the object. This has information about position,
            order, parent in case a document was inserted into another.
            
            Whe the the relatedObject is associated with
            Fnd0AppSession with VisManagedDocument relation.
            
            The following information is returned.
            
fnd0InsertOrder of type Integer - Indicates
            the order at which the relatedObject was
            inserted into its parent.
            
fnd0ParentStableId of type string - Indicates
            the parent object into whcih the relatedObject
            was inserted.
            
fnd0Xform of type string - Indicates the
            transformation of the  relatedObject in the
            co-ordinate system of parent.
            """
    NamedRefList: list[NamedReferenceInfo]
    """
            A List of named reference and reference object if the relatedObject
            is a Dataset.
            """

class RelatedObjectTypeAndNamedRefs:
    """
    
            This structure contains a related object type and the list of its named references
            to be processed.
            
    """
    def __init__(self, ) -> None: ...
    ObjectTypeName: str
    """Secondary object type based on which the results are to be filtered down."""
    NamedReferenceNames: list[str]
    """
            Name of the named references in case the objectTypeName
            is of Dataset type.
            """

class RelationAndTypesFilter:
    """
    
            This structure contains a relation name and a list of related object types and its
            named references (RelatedObjectTypeAndNamedRefs).
            Together they are used to filter objects passed back in a session open operation.
            
    """
    def __init__(self, ) -> None: ...
    StableId: str
    """Stable ID that associates the object with the session."""
    RelationName: str
    RelatedObjAndNamedRefs: list[RelatedObjectTypeAndNamedRefs]
    """A list of related object types and named references."""
    NamedRefHandler: str

class SessionInfo:
    """
    
SessionInfo is a structure which enables
            to create or update a session. The client can pass information to create a session
            or update a session by passing sessionToCreateOrUpdate
            . During creation of session the client populates attachObjectsToSession,
            productSessionDataAttachInfos with objects
            it has opened and populates productAndConfigsToCreateOrUpdate
            with product structure that were opened. The client can detach the closed documents
            and product structures by populating detachObjectOrProductsFromSession.
            
Note: If an existing product structure which was associated to the session
            is opened in the context of the session, its configuration was changed or recipe
            was changed, and session is saved, the client application has to remove the original
            product and configuration from the session identifying it by stableId and add the changes as new product structure configuration
            with same  or different stableId.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The input clientId sent by the client application
            which will enable the client to map the output with the input.
            """
    SessionToCreateOrUpdate: CreateOrUpdateObjectInfo
    """
            The input that has information to create a session BusinessObject. Since the
            session object is a Fnd0AppSession the required properties for object creation
            like object_name and the BusinessObject
            type name can be passed.  Inorder to update, the object itself is passed.
            """
    AttachObjectsToSession: list[BaseObjectAttachInfo]
    """
            A list of information about the opened objects that are to be attached to the session.
            This would typically include any Dataset or Form that were opened in
            the application session.
            """
    ProductAndConfigsToCreate: list[StructureRecipeOfOpenedProduct]
    """
            A list of information about the opened product structures that are to be attached
            to the session. This would typically include any BOMLine, VisStructureContext
            or Item, ItemRevision, BOMView, BOMViewRevision with
            configuration information.
            """
    ProductAndConfigsToUpdate: list[StructureRecipeRelatedInfo]
    """
            A list of information about the product structures information attached to the session
            that are to be updated.
            
Note: In order to update the configuration and search recipe the client has
            to remove the existing product structure information and re-associate the new product
            structure configuration.
            """
    ProductSessionDataAttachInfos: list[ProductSessionDataAttachInfo]
    """
            A list of Fnd0ProductSessionData objects that are to be created or updated
            and attached to the session.
            """
    DetachObjectOrProductsFromSession: list[str]
    """
            A list of stable Id of the product structure or objects associated with the session
            that must be detached.
            
Note: This is considered only during the update case.
            """

class SessionProductStructureInfo:
    """
    
SessionProductStructureInfo holds information
            about the product structure associated to session.
            
    """
    def __init__(self, ) -> None: ...
    StableId: str
    """
            The identifier that enables the client to identify the association of the opened
            product structure with the session.
            """
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """
            The BOMWindow of the product structure that was associated to the session.
            This is populated only if  ProductStructureFilter.RecipeObjectsOnly is false.
            """
    RecipeObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The recipe object of the structure which can be opened outside the context of the
            session. Typically it is the a VisStructureContext object but it could be
            any object which is capable of reconstructing the BOMWindow and hence the
            client should not assume the type of object to particular type.
            """
    RelationProperties: System.Collections.Hashtable
    """
            A map(string,PropertyValues) on the relation that associated the session
            and the product structure . This has information about position, order and parent
            in case these properties were stored on the IMAN_CCContext relation. This
            map is only populated when the  IMAN_CCContext  relation that associates Fnd0AppSession
            and product structure has this information.
            
            The following information is returned.
            
fnd0InsertOrder of type Integer - Indicates
            the order at which the product structure was inserted into its parent.
            
fnd0ParentStableId of type string - Indicates
            the parent product structure into which the product structure was inserted.
            
fnd0Xform of type string - Indicates the
            transformation of the product structure in the co-ordinate system of parent
            """
    StaticStructureFileTicket: str
    """
            The static structure file ticket if the product structure was represented as a static
            file during the creation of session.
            
Note: This is populated only if  ProductStructureFilter.WantStaticStructureFileTicket
            is true.
            """
    RelatedObjectInfos: list[RelatedObjectInfo]
    """
            A list of RelatedObjectInfo that contains
            information about the objects that were related to the product structure information
            associated to session object.
            """
    ProductSessionDataObjects: list[ProductSessionDataObjectInfo]
    """
            A list of Fnd0ProductSessionData that are associated to product structure
            information present in the session.
            """

class StructurePathIdentifiers:
    """
    
StructurePathIdentifiers is a structure describes
            the information that need to be used to traverse a BOMLine path.
            
    """
    def __init__(self, ) -> None: ...
    IdentifierPropertyName: str
    """The name of the property that is used to identify the BOMLine in the path."""
    ResultPathIdentifiers: list[str]
    """A list of property values to match when the BOMLine path is traversed."""

class StructureRecipeOfOpenedProduct:
    """
    
StructureRecipeOfOpenedProduct is a structure
            in which the application can provide information about the product and its configurations
            that were opened. Using this structure, the subsets or product structures that were
            added, updated or removed to the existing product structure that is associated to
            session can be updated.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The input clientId sent by the client application
            which will enable the client to map the output with the input.
            """
    ObjsAttachInfos: list[BaseObjectAttachInfo]
    """
            A list of information about the opened objects that are to be associated to the products
            opened in the context of the session. This would typically include any Dataset
            or Form that are to associated to the product structure in the context of
            session.
            """
    ProductSessionDataAttachInfos: list[ProductSessionDataAttachInfo]
    """
            A list of Fnd0ProductSessionData objects that are to be created or updated
            and attached to the product structure in the context of the session.
            """
    StructureRecipe: ProductStructureRecipe
    """
            Object of type ProductStructureRecipe which
            contains product, configuration and subset information.
            """
    StructureRecipeProps: System.Collections.Hashtable
    """
            A map (string, PropertyValues)
            of property name and values pairs that need to be set  or updated on the ImanRelation
            that associates the product structure to the session.
            
Note: If the client would like to
            re-use the same stableId of a detached product structure, then it can be accomplished
            by passing the stable id as value for fnd0CopyStableId
            property.
            """

class StructureRecipeOfProductOutput:
    """
    
StructureRecipeOfOpenedOutput holds information
            about the product structure that was associated to the session.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The input clientId sent by the client application
            which will enable the client to map the output with the input.
            """
    RelativeToSessionStableId: str
    """
            The identifier that enables the client to identify the association of the opened
            product structure with the session.
            """
    RecipeObject: Teamcenter.Soa.Client.Model.ModelObject
    BaseObjectAttachOutputs: list[BaseObjectAttachInfoOutput]
    """
            A list of BaseObjectAttachInfoOutput which
            has information about the objects that were associated to product structure information
            in the session.
            """
    ProductSessionDataAttachOutputs: list[BaseObjectAttachInfoOutput]
    """
            A list of Fnd0ProductSessionData objects that were created or updated and
            attached to the product structure information in the session.
            """

class StructureRecipeRelatedInfo:
    """
    
StructureRecipeRelatedInfo contains the product
            structure information that is associated to the session which is to be updated.
            
    """
    def __init__(self, ) -> None: ...
    StableId: str
    """The stableId of existing product structure information."""
    ObjsAttachInfos: list[BaseObjectAttachInfo]
    """
            A list of information about the opened objects that are to be associated to the product
            structures opened in the context of the session. This would typically include any
            Dataset or Form that are to associated to the product structure in
            the context of session.
            """
    ProductSessionDataAttachInfos: list[ProductSessionDataAttachInfo]
    """
            A list of Fnd0ProductSessionData objects that are to be created or updated
            and attached to the product structure information in the context of the session.
            """
    DetachObjects: list[str]
    """
            A list of stable Id of the objects associated with the product structure information
            in the context of the session that must be detached.
            """
    StructureRecipeProps: System.Collections.Hashtable
    """
            A map (string, PropertyValues) of property
            name and values pairs that need to be set or updated on the ImanRelation that
            associates the product structure to the session.
            """

class SubsetLinesInfo:
    """
    
SubsetLinesInfo is a structure using which
            the result lines of a search can be persisted along with the subset. The lines could
            be identified as BOMLine object or using an identifier.
            
    """
    def __init__(self, ) -> None: ...
    Lines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Result BOMLine that are part of the subset."""
    CompositePathIdentifiers: list[CompositePathIdentifiers]
    """Result BOMLine identified by path identifiers."""

class StructureSubsetInfo:
    """
    
StructureSubsetInfo is a structure that has
            the results of product structure filter which needs to be saved in the session.
            
    """
    def __init__(self, ) -> None: ...
    ResultContext: str
    ResultObjects: SubsetLinesInfo
    """Results of the product structure filter."""

class AppSessionManagement:
    """
    Interface AppSessionManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateSavedSession(self, SessionsToCreateOrUpdate: list[SessionInfo]) -> CreateOrUpdateSessionResponse:
        """    
             This operation creates or updates a session data model that captures product structure
             configuration rules, non structure object references (e.g. 2D drawings), and application
             specific data (e.g. markups, snaphsots) from a visualization enabled application.
             The session model is either a Fnd0WorksetRevision Object or a Fnd0AppSession(Session)
             Object referencing objects opened in client applications. The operation returns unique,
             copy stable ids for all the objects referenced by the session for persistence of
             it into CAD session files. Client specific objects can be associated to Fnd0AppSession
             with GRM relations or as sub class Fnd0ProductSessionData where the fnd0OwningObject
             property is referencing Fnd0AppSession.
             

Use Cases:

             The user may have opened multiple product structures, applied search filters on them
             and along with  it  may have opened other objects like Dataset or Form.
             The user then issues a save session command to capture the state of the session so
             that it can be restored for continuation of work or to share it other users with
             review markups.
             

             The mechanism for a client application(CAD) which captures the CAD related session
             setting in a session file and saves the opened products, documents and its state
             in Teamcenter as session, contains steps as below.
             

             User creates a Session
             

User opens product structures, Dataset, creates a review markup
             and saves the session.
             
Client application creates a Dataset that will contain the
             session assets information like Markup, Snapshot etc. using createDatasets or using BaseObjectAttachInfo.baseObjectToCreateOrUpdate.
             
The client application then invokes the createOrUpdateSavedSession
             where the input are the objects that were opened in the session and Dataset
             containing session assets. This step creates the session object and associates the
             input objects to the session with relevant relations as per the data model. Associated
             Dataset and ImanFile objects are then accessible to other authorized
             clients through the PLM system.
             



             User updates a Session
             

User searches for the Fnd0AppSession or Fnd0WorksetRevision
             he has saved.
             
Opens it in the client application that supports opening of Fnd0AppSession
             or Fnd0WorksetRevision.
             
The client application invokes openSavedSession
             operation which returns the objects associated to the session with its corresponding
             stable Ids.
             
The application restores his session as persisted by the Fnd0AppSession
             or Fnd0WorksetRevision.
             
User now closes some documents, opens new documents and/or modifes
             existing objects. For Fnd0WorksetRevision, the only supported updates are
             adding new product structures to the session, removing product structures, or updating
             the desired configuration or filtering of a product structure which is already in
             the session.
             
User now issues a command to save the session
             
The application invokes createOrUpdateSavedSession
             operation to update the object association to the session by identifying the association
             via stable Id.
             



Note: As a best practice, for a Fnd0AppSession but not Fnd0WorksetRevision
             session, if the configuration or search recipe of a product structure in an existing
             session is changed and saved by the user it is recommended that the application removes
             the the product structure from the session and adds the changed product structure
             to the session with the same stableId or using a new stable id.
             

Teamcenter Component:

             Teamcenter Visualization - Application to allow view and markup of multicad product
             structure that has a jt representation.
             
        :param SessionsToCreateOrUpdate: 
                         A list of <font face="courier" height="10">SessionInfo</font> data structures. Each
                         of the struct element is identified by a unique identifier assigned by the client
                         and holds information about the session that needs to be created or updated, list
                         of Teamcenter object information that will be associated to the session.
             
        :return: 
        """
        ...
    def OpenSavedSession(self, SessionsToOpen: list[Teamcenter.Soa.Client.Model.ModelObject], Filter: OpenSavedSessionFilter) -> OpenSessionResponse:
        """    
             This operation is used to open the documents and product structures that were saved
             to a session object using createOrUpdateSavedSession.
             For product structures, the configuration rules persisted with the session are used
             to recreate the correct BOM system configuration in effect when the session was last
             authored.  The client can either open all the documents and product structures associated
             to the session or selectively open by providing OpenSavedSessionFilter.
             The session object type that can be opened by this operation is Fnd0AppSession.
             

Use Cases:

             The user may have opened multiple product structures, applied search filters on them
             and along with  it  may have opened other objects like Dataset or Form.
             The user then issues a save session command to capture the state of the session so
             that it can be restored for continuation of work or share it other users with review
             markups.
             

             The mechanism for a client application(CAD) which captures the CAD related session
             setting in a session file and saves the opened products, documents and its state
             in Teamcenter as session, contains steps as below.
             

             1.    User opens product structures, Dataset, creates
             a review markup and saves the session.
             
             2.    Client application creates a Dataset that will contain
             the session assets information like Markup, Snapshot etc. using createDatasets. The client application then invokes the createOrUpdateSavedSession where the input are
             the objects that were opened in the session and Dataset containing session
             assets. This step creates the session object and associates the input objects to
             the session with relevant relations as per the data model. Associated Dataset
             and ImanFile objects are then accessible to other authorized clients through
             the PLM system.
             
             3.    Another user could search for the session created in step
             2 and issue a command in the application to open the session. The client application
             now invokes this operation to get all the objects and product structures that were
             associated to the session and present it to the user the way he persisted those in
             Teamcenter. The stable Id that uniquely identifies the association of a product structure
             or object to the session is also returned so that it can used to update the session
             when the user modifies the session.
             

Teamcenter Component:

             Teamcenter Visualization - Application to allow view and markup of multicad product
             structure that has a jt representation.
             
        :param SessionsToOpen: 
                         A list of <font face="courier" height="10">Teamcenter::BusinessObject</font> session
                         object that are to be opened. Valid session object is <b>Fnd0AppSession</b>.
             
        :param Filter: 
                         The filter to apply on the type of object and product structures that the client
                         application is interested in opening.
             
        :return: 
        """
        ...

