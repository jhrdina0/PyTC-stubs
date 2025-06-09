import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AppendRemoveElementsInfo:
    """
    
            This structure contains information about the AppendList, RemoveList and configuration
            rules to be applied on those input list of objects. This is an optional parameter.
            AppendList contains objects from the target application model that are to be realized
            under the realization container. Updates on the appended objects is not supported.
            RemoveList contains list of objects that are to be removed from the target application
            model that are under the realization container.
            
    """
    def __init__(self, ) -> None: ...
    AppendList: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """List of elements to be appended from source model into Target Container during Update."""
    RemoveList: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """List of elements to be removed from target realization container during update."""
    ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """Configuration rules to be applied on elements to be appended or removed."""

class AuxObjectInfo:
    """
    
            Any special attributes to be set on to the Target object for a given source object
            can be supplied using this structure.
            
    """
    def __init__(self, ) -> None: ...
    SourceObject: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """
            Business object reference to the source object. Special attribute values will be
            set for its corresponding target object.
            """
    AttrInfo: System.Collections.Hashtable
    """
            Bag of Attributes to be set on the corresponding Target object for the given source
            object
            """

class ErrorValuesStruct:
    """
    
            ErrorValuesStruct structure contains the error details which occurred for the failed
            business objects. For each failed object this structure is populated with details
            such as error code, error message and error level.
            
    """
    def __init__(self, ) -> None: ...
    Code: int
    """integer value representing error code."""
    Message: str
    """string representing error message"""
    Level: str
    """
            level represents the error crititicality. Possible values are: Error_severity_information,
            Error_severity_warning & Error_severity_error.
            """

class FailedObjsErrorStruct:
    """
    
            Error structure that contains information about the source object and the reasons
            for their failure.
            
    """
    def __init__(self, ) -> None: ...
    SourceObject: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """Business Object Reference to the source object that has failed to realize or update."""
    ErrorValue: ErrorValuesStruct
    """
            ErrorValuesStruct structure represents the reasons for the failure to realize a source
            object or update a target object.
            """

class ModelToModelRealizationContentResponse:
    """
    
            This construct contains a list of RealizeModelElementData
            which is one to one correspondence with RealizeModelContentInfo.
            Any created / updated objects including the ReuseModelElement
            which actually holds the objects in the target model will be sent back in the standard
            ServiceData lists of created and updated objects respectively. Any failure will be
            returns with the client id mapped to error message in the Service Data list of partial
            errors. The ReuseModelElement acts as a container
            object as it contains the realized objects in the target model after realization
            
    """
    def __init__(self, ) -> None: ...
    RmeData: list[RealizeModelElementData]
    """
            Represents the list of RealizeModelElement
            data which has one to one correspondence with input RealizeModelContentInfo.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains newly added, updated object data including the error information, if any."""

class SourceModelInfo:
    """
    
            SourceModelInfo is a construct that holds information about the source application
            model, include list, subset definition and configuration rules that are required
            to realize source content in the target application model.
            
    """
    def __init__(self, ) -> None: ...
    SourceModel: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """Business object reference to source application model. This is a mandatory argument"""
    SubsetDef: Teamcenter.Soa.Client.Model.Strong.Mdl0SubsetDefinition
    """
            Business object reference to the source Subset Definition. It can be empty if includeSourceElements
            is supplied as input.
            """
    ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """Configuration rules to be applied on source models i.e. sourceModelObject."""
    IncludeSourceElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """
            Contains a list of business object references of the object to be included from Source
            Model into the Target Model. Applications can supply includeSourceElements instead
            of supplying subset Definition as input argument.
            """

class RealizationContentInfo:
    """
    
            The createInput structure specifies the information about the source application
            model content that has to be realized into the target application model. Additionally,
            it also contains information about the auxInfo ( to carry forward effectivity and
            variant information ) and auxObjectInfo ( to set additional attributes on newly created
            realized content ).
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string supplied by the caller. This ID is used to identify returned elements
            and Partial Errors associated with this input objects.This is an optional argument.
            """
    BoType: str
    """
            Business object Type for the realization Container object to be created in the target
            model. Valid types are only subtypes of Rlz0RealizationContainer.
            If nothing supplied, it will be defaulted to Rlz0RealizationContainer
            type.
            """
    RealizationContainerName: str
    """Display name of the realization container. Cannot be empty."""
    SourceModelInfo: SourceModelInfo
    """
            Information about the source model content that is to be realized into the target
            model.
            """
    TargetModel: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """
            Business object reference to the application model into which the objects are to
            be realized. This argument cannot be NULL.
            """
    AuxInfo: System.Collections.Hashtable
    """
            auxInfo Map is an optional argument that is used to specify name value pairs to specify
            sync flags. All values are specified as strings, the caller is responsible for generating
            the correct string representation of each name and value passed. This is an optional
            argument. Note: The flags supplied will be applicable for all the objects that are
            created using this operation. sync_variant_expressions flag is specified to carry
            over Variant expression from source object, Note: please refer to precondition to
            copy over variants in TDOC ( optional; valid values: true or false). sync_effectivity_expressions
            flag is specified to carry over Effectivity expression from source object ( optional;valid
            values: true or false). fnd0CheckoutOnCreate flag is specified to checkout the realized
            objects in target model ( optional;valid values: true or false).
            """
    AuxObjectInfo: list[AuxObjectInfo]
    """
            Any special attributes to be set on to the newly created target object for a given
            source object can be supplied using this structure. This argument is optional.
            """

class RealizeModelContentInfo:
    """
    
            This construct holds information about the CreateInput structure and the UpdateInput
            structure to perform create realization and update realization operations respectively.
            
    """
    def __init__(self, ) -> None: ...
    CreateInfo: list[RealizationContentInfo]
    """
            Contains information about source application model along with search criteria and
            configuration rules that are to be applied on source model to realize source content
            into target application model.
            """
    UpdateInfo: list[UpdateRealizationContentInfo]
    """
            Contains information about the realization container and updates that are to be performed
            on the realized content.
            """

class RealizeModelElementData:
    """
    
            This is the response structure for create or update realization operation. This structure
            contains information about the realizationContainer, source to target create map
            uids for newly realized objects, source to target update map for the updated objects
            and information about the failed objects. ClientId is populated to map the SOA request
            to response.
            
    """
    def __init__(self, ) -> None: ...
    RealizationContainer: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """Business Object reference to realizationContainer object that is created or updated."""
    SourceToTargetCreatedObject: System.Collections.Hashtable
    """
            source and its corresponding target object uid map, This map is populated for newly
            realized objects.
            """
    SourceToTargetUpdatedObject: System.Collections.Hashtable
    """
            source and its corresponding target objects uid map, this map is created for updated
            objects.
            """
    FailedObjects: list[FailedObjsErrorStruct]
    """
            List of failed objects structure, which specifies the reason for create or update
            realization failure for a specific source object. Each structure contains the source
            object and its error structure.
            """
    ClientID: str
    """
            A unique string sent by the calling function, so that the output response could be
            mapped back to the input.
            """

class SourceModelConfigResponse:
    """
    
            This structure represents the output response to the getSourceModelConfigInfo
            operation.
            
    """
    def __init__(self, ) -> None: ...
    SourceModelsInfo: System.Collections.Hashtable
    """
            A set of name value pairs used to specify source model object configuration information
            that was used during realization or instantiation for the corresponding target model
            object specified as key. Only the data, for which source object information was obtained
            successfully, are present in this set .
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            An object of ServiceData which contains updated data model objects and/or error objects
            with error messages
            """

class SourceModelConfigurationData:
    """
    
            This structure represents the source application model configuration contents that
            are requested by the user for the supplied target model object.
            
    """
    def __init__(self, ) -> None: ...
    SourceModelObject: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """
            Business object reference to the source model object that was used during realization
            or instantiation
            """
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """Revision rule that was applied on source model object during realization or instantiation"""
    VarRule: Teamcenter.Soa.Client.Model.Strong.VariantRule
    """Variant rule that was applied on source model object during realization or instantiation"""
    SourceModelElements: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """
            Represents the list of source model elements that were used while realization or
            instantiation.
            """
    SearchExpr: Teamcenter.Soa.Client.Model.ModelObject
    """Businessobject reference to the search expression"""
    ClosureRule: Teamcenter.Soa.Client.Model.Strong.ClosureRule
    """
            Business object reference to the closure rule that was applied during realization/instantiation
            of the source application model
            """
    SyncVariantExprs: bool
    """
            A boolean value if set to true, indicates whether the sync variant expressions was
            set on the source application model
            """
    EffectivityExprs: bool
    """
            A boolean value if set to true, indicates that effectivity expression was set on
            the source application model
            """
    BaselineInfo: Teamcenter.Soa.Client.Model.ModelObject
    """Reference to the baseline information of the source application model"""

class UpdateRealizationContentInfo:
    """
    
            The UpdateInput structure holds the information about the realization container,
            source model content information and target model content information that will be
            used during realization update. Additionally, it also contains information about
            the sync flags ( to carry forward effectivity and variant information ) and auxiliary
            object information.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string supplied by the caller. This ID is used to identify returned elements
            and Partial Errors associated with this input objects.This is an optional argument.
            """
    RealizationContainer: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            Business Object Reference to an existing realization container object that needs
            to be updated. This is required for Update. This acts as a realization container
            object.
            """
    SourceModelInfo: SourceModelInfo
    """Information about the source model content that has to be updated in the target model."""
    AppendRemoveElementsInfo: AppendRemoveElementsInfo
    """
            Information about the elements that are to be appended or removed from the target
            application model. This structure also holds the configuration rules that are to
            be applied on to the input content before performing update.
            """
    UpdateAuxInfo: System.Collections.Hashtable
    """
            updateAuxInfo is an optional argument that is used to specify name value pairs (string,
            string) to specify synchronization flags. The caller is responsible for generating
            the correct string representation of each name and value passed.
            
            Note: The flags supplied will be applicable for all the objects that are created
            using this operation.
            
            Current possible value pairs are:
            
            1. ( sync_variant_expressions, true/false )
            
            sync_variant_expressions flag is specified to carry over Variant expression from
            source object, Note: please refer to precondition to copy over variants in TDOC (
            optional; valid values: true or false).
            
            2. ( sync_effectivity_expressions, true/false )
            
            sync_effectivity_expressions flag is specified to carry over Effectivity expression
            from source object ( optional;valid values: true or false).
            
            3. ( fnd0CheckoutOnCreate, true/false )
            
            fnd0CheckoutOnCreate flag is specified to checkout the newly realized objects in
            target model ( optional;valid values: true or false).
            """
    UpdateAuxObjectInfo: list[AuxObjectInfo]
    """
            Any special attributes to be set on to the newly created target object for a given
            source object can be supplied using this structure. This argument is optional.
            """

class RealizationManagement:
    """
    Interface RealizationManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateModelToModelRealization(self, Input: RealizeModelContentInfo) -> ModelToModelRealizationContentResponse:
        """    
             This operation creates or updates realization content from an application model (
             referred as source model ) into another application model ( referred as target model
             ). For each realization create operation, a new realizationContainer is created,
             under which the target realized content resides. Internally each Realization will
             remember the search criteria and the configuration rules that were used on source
             model to collect a set of objects that are now being realized into the target model.
             

             The newly created objects in the target model are fully populated meaning they are
             created in persistent or static fashion. The realized model elements in the target
             model will be of same type and category as the source model objects.
             
             For example, if a Design Component (Cpd0DesignElement) of category Shape from a source
             model is realized into a target model, the object type and category of the newly
             created object in the target model will still be the same as the object in the source
             model.
             

             In case the realization content (list of model elements or a subset definition object)
             is not provided for create operation, then an empty realizationContainer object is
             created and populated in the SOA response. This realizationContainer object can be
             updated later to get the realization content.
             

             Note: Internally BMIDE deep copy rules are used to traverse and realize the source
             objects and its corresponding secondary objects. For any special behaviour on object
             traversal and action type existing deep copy rules can be updated or new deep copy
             rules can be created.
             

             Pre-Conditions:
             
             1) The source application model is with some pre-existing model content.
             
             2) Target application model already exists.
             

             Limitations:
             
             1) Partitions (Ptn0Partition) are not supported/Realized using this operation.
             

             Applications/Customers should use existing Partition Template Realization capability
             to realize partitions from one model to another.
             

Use Cases:

             To realize model elements ( coming from a Product definition application model )
             into the manufacturing application model and maintain associations between related
             objects in the source and target models for updating realized content. The cross
             domain realization or Model- Model Realization use case supports different aspects
             of the common content across different domain models. The most typical cross domain
             realization or Model- Model Realization use case supports assignment of model elements
             ( coming from a Product definition ) into the manufacturing model.
             

             The basic idea is that the realized model elements draw on all information from the
             source model elements and then add additional or override information in the realized
             model context. In terms of maturity propagation, the expectation is that this is
             controlled and when the user makes a deliberate decision to move forward to a newer
             maturity status of is source model elements, he will also make a decision to update
             the realization on the realized model elements. This allows both domains to proceed
             on their own path but still be collaborative in nature.
             

             Realizing a reuse design component, will realize all its chain of subordinate design
             components by default. This is controlled by a business object constant called RealizeReuseAndSubordinates.
             If the value of this constant is true, then reuse and its full chain of subordinates
             will be realized together, else reuse or the selected subordinate will be ignored.
             Similarly realizing a subordinate design component will realize its reuse design
             component and full chain of subordinates for that reuse design component by default.
             The same preference can be used to control this behaviour.
             

             Delete on the realization container will delete the container and its content.
             


Dependencies:

             autoAssignValues, getSaveAsDesc
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Input: 
                         Data on <font face="courier" height="10">RealizeModelContentInfo</font> used to create
                         or update Model to Model Realization across different application models
             
        :return: 
        """
        ...
    def GetSourceModelConfigInfo(self, TargetModelObjects: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]) -> SourceModelConfigResponse:
        """    
             This operation gets the configuration information of the source model element that
             was used during realization or instantiation. The input objects could be any of the
             following:
             
             1) Reuse Design Component (Rlz0ReuseDesignModelElement)
             
             2) Subordinate of a Reuse Design Component (Rlz0ReuseDesignModelElement)
             
             3) Realization container object (Rlz0ReuseModelElementInstance)
             
             4) Realized content
             

             The operation returns the list of source model object configuration information as
             a response or fails in case of error condition.
             

Use Cases:

             The getSourceModelConfigInfo operation could
             be called when user wants to fetch the Source Model Configuration information that
             was applicable during realization or instantiation. User can specify the input as
             a list of realized model elements.
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param TargetModelObjects: 
                         List of the target model objects that were realized or instantiated. The operation
                         checks for the sopport of the supplied objects. This parameter is mandatory for the
                         operation and cannot be null.
             
        :return: object and returned as a partial error.
        """
        ...

