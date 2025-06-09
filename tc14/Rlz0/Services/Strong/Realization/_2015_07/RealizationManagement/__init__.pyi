import Rlz0.Services.Strong.Realization._2014_10.RealizationManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AuxiallaryObjectInfo3:
    """
    
            AuxiliaryObjectInfo3 is used as input for creating or updating auxiliary objects
            along with main objects. For example, it can be used to pass information about attribute
            group objects to be created along with source elements(Mdl0ModelElement).
            
    """
    def __init__(self, ) -> None: ...
    AttributeInfo: System.Collections.Hashtable
    BoType: str
    """
            Type of the auxiliary object used for creation. For update of auxiliary object, this
            field is ignored.
            
            Supported types:
            
            All subclassess of Mdl0ManagedAttributeGroup

            All subclassess of Mdl0AttributeGroup

            All subclass of Rlz0Composition
"""
    RelationType: str
    """
            The property name to AuxiliaryObjectInfo3. The property name must be the relation
            property on the main object which will be used to attach the auxiliary objects.
            """
    AuxObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Auxiliary object to be updated. This field is empty when auxiliary object is being
            created.
            
            Supported object types:
            
            All subclassess of Mdl0ManagedAttributeGroup

            All subclassess of Mdl0AttributeGroup

            All subclass of Rlz0Composition
"""
    SubObjects: System.Collections.Hashtable
    """
            Contains information about sub-objects to be created for auxiliary object. This field
            is ignored when auxiliary object is being updated.
            """

class CompositionInfo:
    """
    
            This structure contains information about the composition object(subclass of Rlz0Compostion)
            to which the subset(Rlz0Subset) content would be assigned.This is a mandatory
            argument.composition is a Mdl0ConditionalElement which is already created at the
            target application model and can be empty.The parameters compositionType,compositionName and attrInfo
            contain information required to create a composition
            in the target application model, if the input parameter composition is empty.The
            required input for this structure is either a composition object or a compositionType.
            
    """
    def __init__(self, ) -> None: ...
    Composition: Teamcenter.Soa.Client.Model.Strong.Rlz0Composition
    """
            The composition object (subclass of Rlz0Composition) to which subset (Rlz0Subset)
            content would be assigned. This is an optional parameter.
            """
    CompositionType: str
    """
            The type of the object(Mdl0ModelElement) that will be created in the target
            application model. This is mandatory if the input parameter composition is empty.
            """
    AttrInfo: System.Collections.Hashtable
    TargetModel: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """
            The (Mdl0ApplicationModel)target application model.This argument is mandatory
            if the input parameter composition is null.
            """

class CompositionSubsetContentInfo:
    """
    
            This structure specifies the content from different the source application models
            that have to be sparsely realized as subsets(Rlz0Subset) into a composition(subclass
            of Rlz0Composition) at the target application model. Additionally, it also
            contains information about the auxInfo ( to carry forward effectivity and variant
            information ) and auxObjectInfo ( to set additional attributes on newly created realized
            content ).
            
            Note : auxInfo and auxObjectInfo are for future use.
            

    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string supplied by the caller. This ID is used to identify returned elements
            and Partial Errors associated with this input objects.This is an optional argument.
            """
    CompositionInfo: CompositionInfo
    """
            Information about the composition object (Mdl0ModelElement) at target application
            model into which the objects are to be sparsely realized. This argument cannot be
            NULL or empty.
            """
    SubsetCreateInfos: list[SubsetContentInfo]
    """
            A list that holds information from different source application models whose content
            has to be sparsely realized into the target model under subsets(Rlz0Subset).If
            the list is empty then only a composition(subclass of Rlz0Composition) will
            be created without any subset(Rlz0Subset) and its content.
            """
    AuxInfo: System.Collections.Hashtable
    """
            An optional Map (string, string) that is used to specify name value pairs to specify
            sync flags. All values are specified as strings, the caller is responsible for generating
            the correct string representation of each name and value passed. This is an optional
            argument. Note: The flags supplied will be applicable for all the objects that are
            created using this operation. Optional, Future.
            """
    AuxObjectInfo: list[Rlz0.Services.Strong.Realization._2014_10.RealizationManagement.AuxObjectInfo]
    """
            List of any special attributes that are to be set on the target object for a given
            source object can be specified using this structure. This argument is optional, Future.
            """

class CompositionSubsetModelContentInfo:
    """
    
            This construct holds information required  to create  or update a subset under a
            composition(subclass of Rlz0Composition) with  sparsely realized elements.
            
    """
    def __init__(self, ) -> None: ...
    CreateInfo: list[CompositionSubsetContentInfo]
    """
            Contains information about source application model content and the target application
            model (Mdl0ApplicationModel) into which the content has to be sparsely realized.
            """
    UpdateInfo: list[UpdateCompositionSubsetContentInfo]
    """
            Contains information about the source application model content and target application
            model content that will be processed during update operation.(Future)
            """

class CompositionSubsetModelElementData:
    """
    
            This is the response structure for create or update composition subset operation.
            This structure contains information about subset that is created or an update in
            composition(subclass of Rlz0Composition) along with failed model element if
            any. ClientId is populated to map the service operation request to response.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string sent by the calling function, so that the output response could be
            mapped back to the input.
            """
    Composition: Teamcenter.Soa.Client.Model.Strong.Rlz0Composition
    """The updated composition (subclass of Rlz0Composition) object."""
    SubsetData: list[OutputSubsetData]
    """Information on newly created or updated subset (Rlz0Subset) object."""

class CompoundCreateInfo3:
    """
    Generic CreateInfo construct to support compound object create.
    """
    def __init__(self, ) -> None: ...
    AttributeInfo: System.Collections.Hashtable
    BoType: str
    """
            The name of the Teamcenter Business Object type to be created.This is for future
            use.
            """
    CompoundInfo: System.Collections.Hashtable
    """
            A map (string/list of CompoundCreateInfo3) of  property name to compound object property
            values. The CompondCreateInfo3 describes a different object to be created during
            the creation of an auxiliary object.This is for future use.
            """

class M2MCompositionSubsetContentResponse:
    """
    
            This construct contains a list of CompositionSubsetModelElementData which
            is one to one correspondence with CompositionSubsetModelContentInfo. Any created
            / updated objects such as realization maps which maintain associations between source
            and target models objects or realization objects with subset or baseline information
            in the target model will be returned to the client in the standard ServiceData lists
            of created and updated objects respectively. Any failure will be returned with the
            client id mapped to error message in the Service Data list of partial errors.
            
    """
    def __init__(self, ) -> None: ...
    SrmeData: list[CompositionSubsetModelElementData]
    """
            A list of CompositionSubsetModelElement data which has one to one correspondence
            with input CompositionSubsetModelContentInfo.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains newly added, updated object data including the error information, if any."""

class OutputSubsetData:
    def __init__(self, ) -> None: ...
    SubsetClientId: str
    """
            A unique string sent by the calling function, so that the output subset response
            could be mapped back to the input.
            """
    Subset: Teamcenter.Soa.Client.Model.Strong.Rlz0Subset
    """The newly created or updated subset (Rlz0Subset) object."""
    CsIDMap: System.Collections.Hashtable
    """
            Map (business object/string) of configured source model element to its copy stable
            id.
            """
    SubsetCsId: str
    """Copy stable ID of subset (Rlz0Subset) element."""
    PersistentObjMap: System.Collections.Hashtable
    """This is for override mapping. Not supported currently. Reserved for future development."""
    AppendedSourceElementList: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """Contains list of appended source elements."""
    RemovedSourceElementList: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """Contains list of removed source elements."""

class SubsetContentInfo:
    """
    
            This construct holds information about purpose that has to be assigned to subset
            object (Rlz0Subset) and transforms that are to be applied onto the subset
            and its content along with.
            
            the source application model (Mdl0ApplicationModel) search recipe (Fnd0RecipeContainer),
            baseline revision (Mdl0BaselineRevision), and configuration rules (ConfigurationContext)
            that are to be applied on source model to sparsely realize source content into target
            application model (Mdl0ApplicationModel).
            

    """
    def __init__(self, ) -> None: ...
    SubsetClientId: str
    """
            A unique string sent by the calling function, so that the output subset response
            could be mapped back to the input.
            """
    Purpose: str
    """
            The subset (Rlz0Subset) created under a composition(subclass of Rlz0Composition)
            will have a specific purpose as given in input.
            
            Examples of purpose:
            
            Work Area
            
            Consumed
            """
    Transform: list[float]
    """
            Transform to be applied on the subset (Rlz0Subset) content.This is for future
            use.
            """
    SourceModel: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """
            The source application model (Mdl0ApplicationModel) that contains the data
            to be sparsely realized. This is a mandatory argument.
            """
    RecipeDef: Teamcenter.Soa.Client.Model.Strong.Fnd0RecipeContainer
    """
            The source recipe Definition (Fnd0RecipeContainer). It can be empty if includeSourceElements
            or baseline revision (Mdl0BaselineRevision) is supplied as input.
            """
    BaselineRev: Teamcenter.Soa.Client.Model.Strong.Mdl0BaselineRevision
    """
            The Baseline Revision (Mdl0BaselineRevision). It can be empty if includeSourceElements
            or source recipe (Fnd0RecipeContainer) is supplied as input.
            """
    ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
ConfigurationContext rules to be applied on the source model content.This
            is mandatory when includeSourceElements argument
            is provided as input.
            """
    IncludeSourceElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """
            A list of Mdl0ModelElement objects that are to be included from Source application
            model (Mdl0ApplicationModel) into the target model (Mdl0ApplicationModel).
            It can be empty if recipe definition (Fnd0RecipeContainer) or baseline revision
            (Mdl0BaselineRevision) is provided as input.
            """

class UncoupleModelRealizationInputInfo:
    """
    
            Contains information stored by the caller such as clientId for specific session and
            Mdl0ModelElement only Rlz0RealizationContainer or Cpd0DesignElement
            accepted, or sourceModel and targetModel object which contails realization information
            to uncouple.
            
    """
    def __init__(self, ) -> None: ...
    RealizedElement: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """
            A Mdl0ModelElement which contains information of realization to be uncoupled.
            If this option is selected realizationContainer, source and target model will be
            ignored.
            """
    RealizationContainer: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """
            A Mdl0ModelElement object which contains information of realization to be
            uncoupled. If this option is selected source and target model will be ignored.
            """
    SourceModel: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """Information about the source content that was previously realized to the target model."""
    TargetModel: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """
            Business object reference to the application model containing the objects to be uncoupled.
            
"""
    ClientID: str
    """
            A unique string supplied by the caller. This ID is used to identify the newly deleted
            or updated elements and partial errors associated with the input. This is an optional
            argument.
            
"""

class UpdateCompositionSubsetContentInfo:
    """
    
            This structure holds the information about source model content information and target
            model content information that will be used during realization update.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string supplied by the caller. This ID is used to identify returned elements
            and Partial Errors associated with this input objects.This is an optional argument.
            """
    SubsetElement: Teamcenter.Soa.Client.Model.Strong.Rlz0Subset
    """Reference to the Rlz0Subset business object that has to be updated."""
    ObjLastModifiedDateGuard: System.DateTime
    """
            Modification date guard is used if it is set to a non-null date. Object update will
            abort if the last modified date of the object is greater than objLastModifiedDateGuard.
            """
    Transform: list[float]
    """Transform to be applied on the subset (Rlz0Subset) content."""
    RecipeDef: Teamcenter.Soa.Client.Model.Strong.Fnd0RecipeContainer
    """The source recipe Definition (Fnd0RecipeContainer)."""
    BaselineRev: Teamcenter.Soa.Client.Model.Strong.Mdl0BaselineRevision
    """
            The Baseline Revision (Mdl0BaselineRevision). It can be empty if recipe (Fnd0RecipeContainer)
            is supplied as input.
            """
    AppendList: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """
            A list of Mdl0ModelElement objects that are to be appended from source model
            (Mdl0ApplicationModel) into target during Update.
            """
    RemoveList: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """
            A list Mdl0ModelElement objects that are to be removed from the target model
            (Mdl0ApplicationModel) during Update.
            """
    UpdateAuxInfo: System.Collections.Hashtable
    """
            A set of name value pairs (String, String) used to specify additional property data
            or specify sync flags. All values are specified as strings, the caller is responsible
            for generating the correct string representation of each name and value passed. This
            is an optional argument.
            """
    UpdateAuxObjectInfo: list[AuxiallaryObjectInfo3]
    """
            List of any special attributes that are to be set on the target object for a given
            source object can be supplied using this structure. This argument is optional.
            """
    ReplaceSourceElements: System.Collections.Hashtable
    """
            The model elements (Mdl0ModelElement) in this list will replace the model
            elements (Mdl0ModelElement) from Subset (Rlz0Subset) while retaining
            csId (copy stable ID). If no model element is found corresponding to key csId, a
            case of change in csId is assumed. In case of change in csId, csId of existing model
            element in subset is changed.
            """
    PersistSourceElements: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """
            The model elements (Mdl0ModelElement) in this list will replace the model
            elements (Mdl0ModelElement) from Subset (Rlz0Subset) while retaining
            csId (copy stable ID). If no model element is found corresponding to key csId, a
            case of change in csId is assumed. In case of change in csId, csId of existing model
            element in subset is changed.
            """
    UpdateRecipeForAppendsAndRemoves: bool
    """
            If true, the Rlz0Subset recipe include/exclude elements criteria will be modified
            accordingly based on appendList and removeList in input arguments.If false, the Rlz0Subset
            recipe criteria based on appendList and removeList will not be updated on realization object(Rlz0SubsetInstance).
            """
    RemoveSecondaryObjectsAutomatically: bool
    """
            This flag specifies if the secondary objects for the objects specified in removeSourceElements
            parameter must also be removed from Rlz0Subset. It is set to false by default.
            If false, it is expected that removeList
            in input contains complete hierarchy of model elements(Mdl0ModelElement) to
            be removed. If the value is set to true, the application will collect the secondary
            object hierarchy for the objects specified in removeList
            and will remove them.
            """

class RealizationManagement:
    """
    Interface RealizationManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateCompositionSubset(self, Input: CompositionSubsetModelContentInfo) -> M2MCompositionSubsetContentResponse:
        """    
             Operation to create or update subsets (Rlz0Subset) in a composition ( subclass
             of Rlz0Composition) with sparse elements. Sparse elements are the realized
             objects, the realization of content ( source model content ) from source application
             model to target application model is and done without creating brand new copies,
             the sparse elements refer to the same source model elements.
             
             Internally each Realization operation will remember the search criteria and the configuration
             rules that were used on the source model to collect a set of objects that are now
             being sparsely realized into the target model.
             

             Pre-Conditions:
             
             1) The source application model (Mdl0ApplicationModel) has some pre-existing
             model content.
             
             2) The target application model (Mdl0ApplicationModel) (Ex: Product Design)
             and a Composition (subclass of Rlz0Composition) object already exists.
             
             3) When one of the supplied inputs from the source application model is a baseline
             revision (Mdl0BaselineRevision), the user has to ensure that the supplied
             baseline is a closed baseline for the realization operation to execute.
             

             Limitations:
             
             None
             

Use Cases:

             Ability to sparsely realize model elements from a source application model (Mdl0ApplicationModel)
             into a target application model (Mdl0ApplicationModel) by referencing  to
             objects in source application model. The cross domain realization or Model- Model
             Realization use case supports different aspects of the common content across different
             domain models. The most typical cross domain realization or Model- Model Realization
             use case supports assignment of model elements into a composition in the target application
             model.
             

             The basic idea is that the sparsely realized model elements at the target application
             model are not copies but references of source model elements to which the user can
             add additional or override information in the Realization context.
             

             Realizing a Reuse design model element ( Cpd0DesignModelElement - Category
             - REUSE ) or ModelReuse design component ( Cpd0DesignModelElement - Category
             - MODELREUSE ), will realize all its chain of Subordinate DesignModelElements ( Cpd0DesignModelElement
             - Category - SUBORDINATE ) by default.
             

             Delete operation on a composition(subclass of Rlz0Composition) at the target
             application model will remove the associations between source model elements and
             the Sparse Elements in target model. Remove operation on  sparsely realized model
             elements at the target will only remove the associations between source and target
             but does not remove the original model elements at source.
             


Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Input: 
                         Contains information about create and update inputs to create or update subsets (<b>Rlz0Subset</b>)
                         in a composition (subclass of <b>Rlz0Composition</b>)
             
        :return: 
        """
        ...
    def UncoupleModelRealization(self, Input: list[UncoupleModelRealizationInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation uncouple realized  design model content from an application model
             referred as source model into another application model referred as target model.
             For each input object delete the objects in the following order Rlz0ModelRealizationMap,
             Rlz0RealizationContainer and Rlz0M2MSubsetRealization to uncouple the
             model realization.
             

Use Cases:

             To uncouple realized model elements coming from a Product definition application
             model from manufacturing application model and remove associations between related
             objects in the source and target models to avoide updating realized content.
             

             The basic idea is that the realized model elements draw on all information from the
             source model elements and then add additional or override information in the realized
             model context. In terms of maturity propagation, the expectation is that this is
             controlled and when the user makes a deliberate decision to move forward to a newer
             maturity status of is source model elements, he can also make a decision not to update
             the realization in the realized model elements using decoupling. This allows both
             domains to proceed on their own path.
             


Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Input: 
                         List of UncoupleModelRealizationInputInfo objects containing the <b>Mdl0ModelElement</b>
                         or SourceModel and TargetModel  object and information stored by the caller such
                         as <font face="courier" height="10">clientID</font> for specific session.
             
        :return: 
        """
        ...

