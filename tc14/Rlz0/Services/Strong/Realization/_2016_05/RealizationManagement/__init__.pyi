import Rlz0.Services.Strong.Realization._2014_10.RealizationManagement
import Rlz0.Services.Strong.Realization._2015_07.RealizationManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model.Strong
import typing

class CompositionSubsetContentInfo:
    """
    
            This structure specifies the content from different source application models  that
            have to be sparsely realized as subsets(Rlz0Subset) into a composition(subclass
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
            and Partial Errors associated with this input objects. This is an optional argument.
            """
    CompositionInfo: Rlz0.Services.Strong.Realization._2015_07.RealizationManagement.CompositionInfo
    """
            Information about the composition object (Mdl0ModelElement) at target application
            model into which the objects are to be sparsely realized. This argument is mandatory
            and cannot be NULL or empty.
            """
    SubsetCreateInfos: list[SubsetContentInfo]
    """
            A list that holds information from different source application models whose content
            has to be sparsely realized into the target model under subsets(Rlz0Subset).If
            the list is empty then only a composition(subclass of Rlz0Composition) will
            be created without any subset(Rlz0Subset) and its content.
            """
    AuxInfo: System.Collections.Hashtable
    AuxObjectInfo: list[Rlz0.Services.Strong.Realization._2014_10.RealizationManagement.AuxObjectInfo]
    """
            List of any special attributes that are to be set on the target object for a given
            source object can be specified using this structure. This argument is optional, Future.
            """

class CompositionSubsetModelContentInfo:
    """
    
            This construct holds information required  to create or update a subset under a composition(subclass
            of Rlz0Composition) with sparsely realized elements.
            
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
            model content that will be processed during update operation.
            """

class ConditionalElementInfo:
    """
    Data structure that holds the information related to a conditional element(Mdl0ConditionalElement).
    """
    def __init__(self, ) -> None: ...
    ConditionalElement: Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement
    """
            The conditional element (Mdl0ConditionalElement) whose members will be sparsely
            realized. Valid conditionalElement types
            are partition (Ptn0Partition) and design subset element (Cpd0DesignSubsetElement).
            """
    IncludeChildren: bool
    """
            If true, the children of given conditional element (Mdl0ConditionalElement)
            will also be sparsely realized.
            
            If false, children of given conditional element (Mdl0ConditionalElement) will
            not be sparsely realized.
            """

class SubsetContentInfo:
    """
    
            This construct holds information about purpose that has to be assigned to subset
            object (Rlz0Subset) and transforms that are to be applied onto the subset
            and its content along with
            
            the source application model (Mdl0ApplicationModel), search recipe (Fnd0RecipeContainer),
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
            A unique string sent by the caller  such that the subset (Rlz0Subset) created
            under a composition (subclass of Rlz0Composition) will have a specific purpose
            as given in input.
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
            The source recipe definition (Fnd0RecipeContainer). It can be empty if includeSourceElements
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
            is mandatory when includeSourceElements argument is provided as input.
            """
    IncludeSourceElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """
            A list of Mdl0ModelElement objects that are to be included from Source application
            model (Mdl0ApplicationModel) into the target model (Mdl0ApplicationModel).
            It can be empty if recipe definition (Fnd0RecipeContainer) or baseline revision
            (Mdl0BaselineRevision) is provided as input.
            """
    ConditionalElementInfo: ConditionalElementInfo
    """
            The conditional element (Mdl0ConditionalElement) information whose members
            will be sparsely realized.
            """

class UpdateCompositionSubsetContentInfo:
    """
    
            This structure holds update specific inputs that will be used during realization
            update.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string supplied by the caller. This ID is used to identify returned elements
            and Partial Errors associated with this input objects. This is an optional argument.
            """
    SubsetElement: Teamcenter.Soa.Client.Model.Strong.Rlz0Subset
    """
            Reference to the Rlz0Subset object that has to be updated.This is a mandatory
            argument for update.
            """
    ObjLastModifiedDateGuard: System.DateTime
    """
            Modification date guard is used if it is set to a non-null date. Object update will
            abort if the last modified date of the object is greater than objLastModifiedDateGuard.
            """
    Transform: list[float]
    """Transform to be applied on the subset (Rlz0Subset) content."""
    RecipeDef: Teamcenter.Soa.Client.Model.Strong.Fnd0RecipeContainer
    """The source recipe definition (Fnd0RecipeContainer)."""
    BaselineRev: Teamcenter.Soa.Client.Model.Strong.Mdl0BaselineRevision
    """
            The Baseline Revision (Mdl0BaselineRevision). It can be empty if recipe (Fnd0RecipeContainer)
            is supplied as input.
            """
    UpdateConditionalElementInfo: ConditionalElementInfo
    """
            The conditional element (Mdl0ConditionalElement) information for update sparse
            realization.
            """
    UpdateConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """Configuration context that is used for update operations."""
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
            A set of name value pairs (string, string) used to specify additional property data
            or specify sync flags. All values are specified as strings, the caller is responsible
            for generating the correct string representation of each name and value passed. This
            is an optional argument.
            
            Supported value pairs are:
            
            1. Key: "append"
            
            Valid values: "true" or "false"
            
            Default value: "false"
            
            If append flag is true, appends the content (valid content objects are Mdl0ModelElement,
            Mdl0SubsetDefinition and Ptn0Partition) to Rlz0Subset without
            replacing or removing the existing realized content. If false, regular update happens.
            

            2. Key: "SMART_UPDATE"
            
            Valid values: "true" or "false"
            
            Default value: "false"
            
            If this flag is true, new revisions of sparse content are identified, which would
            be appended to the Rlz0Subset object and the old sparse revisions will be marked
            as inactive. If false, regular update happens.
            
            Note: The "append" and "SMART_UPDATE" flags are mutually exclusive.
            

            3. Key: "CARRYOVER"
            
            Valid values: "true" or "false"
            
            Default value: "false"
            
            If this flag is true, attached relations to the existing revisions of sparse elements
            are carried over to the new revisions of sparse elements. If false, attached relations
            to existing revisions are not carried forward.
            

            4. Key: "includeSourceObjectForSubsets"
            
            Valid values: "true" or "false"
            
            Default value: "false"
            
            If this flag is true, source objects are returned without encoded in-context data.
            If false, source objects are returned with encoded in-context data.
            """
    UpdateAuxObjectInfo: list[Rlz0.Services.Strong.Realization._2015_07.RealizationManagement.AuxiallaryObjectInfo3]
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
    PersistSourceElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """
            Future support.
            
            Specifies a list of source objects (Mdl0ModelElement) for which there must
            be persistent objects created in the target model (Mdl0ApplicationModel).
            """
    UpdateRecipeForAppendsAndRemoves: bool
    """
            If true, the Rlz0Subset recipe include/exclude elements criteria will be modified
            accordingly based on appendList and removeList in input arguments.If false, the Rlz0Subset
            recipe criteria based on appendList and removeList will not be updated on realization
            object(Rlz0SubsetInstance).
            """
    RemoveSecondaryObjectsAutomatically: bool
    """
            Future support.
            
            This flag specifies if the secondary objects for the objects specified in removeSourceElements parameter must also be removed from Rlz0Subset.
            It is set to false by default. If false, it is expected that removeList in input contains complete hierarchy of model elements
            (Mdl0ModelElement) to be removed. If the value is set to true, the application
            will collect the secondary object hierarchy for the objects specified in removeList and will remove them.
            """

class RealizationManagement:
    """
    Interface RealizationManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateCompositionSubset(self, Input: CompositionSubsetModelContentInfo) -> Rlz0.Services.Strong.Realization._2015_07.RealizationManagement.M2MCompositionSubsetContentResponse:
        """    
             Operation to create or update subsets (Rlz0Subset) in a composition (subclass
             of Rlz0Composition) with sparse elements. Sparse elements are the realized
             objects, the realization of content ( source model content ) from source application
             model to target application model and is done without creating brand new copies,
             the sparse elements refer to the same source model elements.
             
             Internally each Realization operation will remember the search criteria and the configuration
             rules that were used on the source model to collect a set of objects that are now
             being sparsely realized into the target model.
             

Pre-Conditions:

             1) The target application model (Mdl0ApplicationModel) (Ex: Product Design)
             and a Composition (subclass of Rlz0Composition) object already exist.
             
             2) When one of the supplied inputs from the source application model is a baseline
             revision (Mdl0BaselineRevision), the user has to ensure that the supplied
             baseline is a closed baseline for the realization operation to execute.
             

Limitations:

             None
             

Use Cases:

             Ability to sparsely realize model elements from a source application model (Mdl0ApplicationModel)
             into a target application model (Mdl0ApplicationModel) by referencing to objects
             in source application model. The cross domain realization or Model- Model Realization
             use case supports different aspects of the common content across different domain
             models. The most typical cross domain realization or Model- Model Realization use
             case supports assignment of model elements into a composition (subclass of Rlz0Composition)
             in the target application model.
             

             The basic idea is that the sparsely realized model elements at the target application
             model are not copies but references of source model elements to which the user can
             add additional or override information in the Realization context.
             

             Realizing a subclass of conditional element(Mdl0ConditionalElement ) such
             as partition (Ptn0Partition) or design subset element (Cpd0DesignSubsetElement)
             will realize all of its members into a subset (Rlz0Subset) in target application
             model.
             

             Delete operation on a composition (subclass of Rlz0Composition) at the target
             application model will remove the associations between source model elements and
             the Sparse Elements from all its subsets (Rlz0Subset) in target model. Delete
             operation on a subset (Rlz0Subset) will remove the associations between source
             model elements and the Sparse Elements within that subset. Remove operation on sparsely
             realized model elements at the target will only remove the associations between source
             and target but does not remove the original model elements at source.
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Input: 
                         Contains information about create and update inputs to create or update subsets (<b>Rlz0Subset</b>)
                         in a composition ( subclass of <b>Rlz0Composition</b> )
             
        :return: 
        """
        ...

