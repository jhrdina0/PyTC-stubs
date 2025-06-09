import System
import System.Collections
import Teamcenter.Services.Strong.Cad._2016_03.StructureManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CandidateModelViewStructNodeInfo:
    """
    
            The structure contains  BOMLine or  Cpd0DesignElement on which the
            candidate Fnd0ModelViewProxy was identified. If a BOMLine is returned
            then also the clone stable occ id  chain which identifies BOMLine in a structure
            is also returned.
            
    """
    def __init__(self, ) -> None: ...
    StructNode: Teamcenter.Soa.Client.Model.ModelObject
    """
            A BOMLine or Cpd0DesignElement object on which the candidate was identified.
            A BOMLine is returned only if a BOMLine is sent as configRecipe
            input.
            """
    CloneStableIdChain: list[str]
    """
            List of strings representing a chain of clone stable ids that lead to the structNode in the product structure.
            
            The clone stable occurrence id values are ordered from the top BOMLine incase
            structNode is a BOMLine with line
            object being ItemRevision. Alternatively, if a the csIdContextOccurrence
            is a subset in the Workset, and only a single cs_id value for the structNode would be needed since a given model element (Mdl0ModelElement)
            in a subset (Cpd0DesignSubsetElement)
            
            can be identified by such a single clone stable id.
            """
    CsIdContextOccurrence: Teamcenter.Soa.Client.Model.ModelObject
    """
            Contains either the subset in which the structure node resides (either Cpd0SubsetLine
            or Cpd0DesignSubsetElement.). This object gives context to the associated
            cloneStableIdChain value(s). In case if the
            structNode is a BOMLine whose line
            object is ItemRevision then this would be empty since the top line gives the
            context for the cloneStableIdChain.
            """

class ConfigurationDisplayInfo:
    """
    
            This structure contains the configuration information that can be displayed to the
            user if there is a mis-match between the configuration found on the Fnd0ModelViewPalette
            and the configuration used for palette reconciliation.
            
Note: The information returned by this structure should be used only to display
            configuration information.
            
    """
    def __init__(self, ) -> None: ...
    ConfigWindow: Teamcenter.Soa.Client.Model.ModelObject
    """
            The configuration window (BOMWindow) that represents the configuration.In
            case when the previous configuration information is returned during reconciliation
            process the BOMWindow is valid until the reconciliation is complete.
            """
    RevisionRule: Teamcenter.Soa.Client.Model.ModelObject
    """The RevisionRule used for the configuration."""
    RevRuleConfigEntriesAsStrings: list[str]
    """A list of strings describing the configuration entries in the RevisionRule."""
    ConfigOptions: list[ConfigurationOptionDisplayInfo]
    """
            A list of options that is being used during configuration such as "hide unconfigured
            lines" etc.
            """
    VariantRules: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of VariantRule objects used for the configuration."""

class ConfigurationOptionDisplayInfo:
    """
    
            A structure to represent the configuration option and its values. Depending upon
            the type of option value the appropriate values member would be populated. Say for
            example for the option "Show Unconfigured Variants" the boolValues would be populated with a single value and the rest
            of the values member would be empty. The caller can determine the type of option
            value by checking the value memberthat has been populated.
            
    """
    def __init__(self, ) -> None: ...
    OptionName: str
    """The name of the option use for configuration."""
    BoolValues: list[bool]
    """A list of boolean values if the option is a boolean."""
    DoubleValues: list[float]
    """A list of double values if the option is a double."""
    IntValues: list[int]
    """A list of integer values if the option is an integer."""
    StrValues: list[str]
    """A list of char or string values if the option is a character or string."""
    DateValues: list[System.DateTime]
    """A list of date values if the option is a date."""
    RefValues: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of objects values if the option is a object."""

class FindModelViewsInput:
    """
    
            The set of inputs needed to start a find operation on a given object (disclosure) or a set of objects (startingScopes)
            which are structured under the disclosure.
            
    """
    def __init__(self, ) -> None: ...
    SearchID: str
    """
            A unique identifier passed by the client in order to identify the find results to
            continue with when calling the continueFindModelViews operation. If a value
            is not provided, the preference MVFindMinNodeCount will be ignored and the
            find will finish and no followup call to continueFindModelViews can be made.
            """
    Disclosure: Teamcenter.Soa.Client.Model.ModelObject
    """
            The structure root of the various startingScopes.
            This structure root must be an ItemRevision or Workset (Cpd0Workset).
            Required if startingScopes contains more
            than one object, otherwise it may be left NULL.
            """
    StartingScopes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of one or more structures to search for model view proxy objects. If a single
            root assembly or workset (Cpd0Workset) is given, the entire structure will
            be searched. If multiple sub-assemblies are given, then only those disclosure children
            under the given sub-assemblies will be searched for proxies. The input objects may
            be any WorkspaceObject sub-type that is expected to own (directly or indirectly)
            model view proxy objects. Most commonly input would be a Workset or WorksetLine,
            but other ItemRevision or ItemLine objects may be given.
            """
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            The configuration context object used to configure the children of the expanding
            structure by revision rules, effectivity, and variants.
            """
    WithDisclosureIntents: list[str]
    """
            A list of string values values (such as "Design Review" or "Quality Check" ) to match
            against candidate model view proxies. Only model view proxies that have any of the
            specified disclosure purpose (fnd0DisclosureIntent) attribute values will
            be returned. If no strings are given or any string is an empty string, then all model
            view proxy objects will be returned.
            """
    Options: System.Collections.Hashtable
    """
            A set of optional flags. Supported options are: "expandStructureScope"
            
expandStructureScope: If true, each startingScope will be expanded and their children
            searched for model views. If false, only model view proxies owned by the startingScope objects will be returned. The default is true.
            """

class FindModelViewsResponse:
    """
    
            The response contains any found model view proxies (FndModelViewProxy) and
            the structure location at which they were found.
            

            Any errors are returned in the serviceData.
            
    """
    def __init__(self, ) -> None: ...
    ModelViewsByStructureNodes: list[Teamcenter.Services.Strong.Cad._2016_03.StructureManagement.StructureNodeResults]
    """
            A list of  proxy objects found for various  nodes in the structure - the structure
            nodes may be bomlines, item revisions or design elements depending on the type of
            structure starting scope and disclosure type.
            """
    Finished: bool
    """
            Flag to indicate if the find operation is complete or if there is more content or
            structure to be searched. If false, then the continueFindModelViews operation
            may be called with the input searchID in
            order to continue to retrieve more model views. If true, the state of the search
            is cleaned up and the given searchID, if
            any, may not be used as input into the continueFindModelViews operation.
            """
    StructureNodesSearched: int
    """
            Total number of structure nodes ( BomLines or Design Elements) which were
            so far searched for model views. This shows how large the structure is as the search
            is progressing over multiple calls to startFindModelViews and continueFindModelViews.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains a list of any errors which occurred during the operation."""

class ModelViewProxyReconcileInfo:
    """
    
            This structure contains the reconcile information for each Fnd0ModelViewProxy
            object found in the Fnd0ModelViewPalette. It contains information about the
            candidate Fnd0ModelViewProxy found, the recommended reconciliation action,
            and a description of the basis on which the candidate Fnd0ModelViewProxy was
            identified.
            
    """
    def __init__(self, ) -> None: ...
    CandidateMVP: Teamcenter.Soa.Client.Model.Strong.Fnd0ModelViewProxy
    """The candidate Fnd0ModelViewProxy identified for reconciliation."""
    ReconcileActionEnum: str
    """
            The recommended action for the user to take. Supported values are:
            

None
            
Replace
            
Remove
            
Resolve Ambiguity
            

"""
    ReconcileAction: str
    """
            The displayable explanation of the action that need to be taken. For example: "Remove
            Model View from Palette"
            """
    ReconcileReason: str
    """
            The displayable message which describes the basis of candidate identification.  For
            example, "Model View deleted from Owning Model"
            """
    CandidateStructNodeInfos: list[CandidateModelViewStructNodeInfo]
    """
            A list of CandidateModelViewStructNodeInfo
            that contains the BOMLine or Cpd0DesignElement  on which the candidate
            Fnd0ModelViewProxy was found.
            """

class NextReconcilePaletteInput:
    """
    
            This structure contains the  information about the  clientID
            that identifies the reconciliation state in the server and list of Fnd0ModelViewProxy
            if they have to be given a higher priority during reconciliation. For example, the
            user may have chosen to apply a Model View on the palette before the palette reconciliation
            that already started was complete.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique clientId passed by the client in order to identify the reconciliation of
            the palette between subsequent calls to startReconcilePalette
            and continueReconcilePalette.
            """
    MvProxiesOrMvGroups: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            List of Fnd0ModelViewProxy  or the  Fnd0ModelViewGroup objects that
            need to be reconciled.  Can be used to do a partial reconciliation or just the ModelViewProxy
            or Group of interest.
            """
    StopReconcile: bool
    """Flag to stop the reconciliation process."""

class PaletteModelViewProxyReconcileInfo:
    """
    
            This structure binds the Fnd0ModelViewProxy in the Fnd0ModelViewPalette
            to its corresponding reconcile information.
            
    """
    def __init__(self, ) -> None: ...
    PaletteMVP: Teamcenter.Soa.Client.Model.Strong.Fnd0ModelViewProxy
    """
            The Fnd0ModelViewProxy on the Fnd0ModelViewPalette that has needs to
            be reconciled.
            """
    ReconcileInfos: list[ModelViewProxyReconcileInfo]
    """
            A list of reconcile information for this Fnd0ModelViewProxy including reasons,
            actions, reconcile candidates, and more. Can be a list if more than one candidate
            identified.
            """

class ReconcilePaletteInput:
    """
    
            This structure contains the  information about the  Fnd0ModelViewPalette or
            the disclosing object that needs to be reconciled. It also contains configuration
            information specified as configRecipe  in
            the form of BOMLine or VisStructureContext object. If BOMLine is specified
            as configRecipe then the BOMWindow
            to which the line belongs will be used for reconciliation. If the configRecipe is not specified then the configuration information
            will be retrieved from the Fnd0ModelViewPalette if present otherwise the default
            configuration is used for reconciliation.
            
            The clientID supplied by the client will
            be used to identify the reconciliation state in the server to continue the reconciliation
            process during the continueReconcilePalette
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique clientId passed by the client in order to identify the reconciliation of
            the palette between subsequent calls to continueReconcilePalette.
            """
    PaletteOrDisclosingObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The Fnd0ModelViewPalette  or the object to which Fnd0ModelViewPalette
            is associated using Fnd0DisclosedViewList relation.
            """
    MvProxiesOrMvGroups: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            List of Fnd0ModelViewProxy  or the  Fnd0ModelViewGroup objects that
            need to be reconciled. Can be used to do a partial reconciliation or just the ModelViewProxy
            or Group of interest.
            """
    DoEntirePalette: bool
    """
            Specify false to indicate whether to reconcile only the Fnd0ModelViewProxy
            or Fnd0ModelViewGroup specified in mvProxiesOrMvGroups,
            or true to continue with reconciliation of the entire palette.
            """
    ConfigRecipe: Teamcenter.Soa.Client.Model.ModelObject
    """
            The top line (BOMLine) of the disclosing object or a VisStructureContext
            which has the product structure configuration information.
            """

class ReconcilePaletteResponse:
    """
    
            This structure contains the reconciliation information reponse for each Fnd0ModelViewProxy
            on the Fnd0ModelViewPalette. The clientID signifies maintains the correlation
            between multiple calls to the the server.  The origConfigInfo
            and reconcileConfigInfo are returned only
            if there is a configuration mis-match between the configuration associated to Fnd0ModelViewPalette
            and the one used for reconciliation.
            
    """
    def __init__(self, ) -> None: ...
    PalMVPReconcileInfos: list[PaletteModelViewProxyReconcileInfo]
    """
            A list of PaletteModelViewProxyReconcileInfo,
            one for each Fnd0ModelViewProxy  on the Fnd0ModelViewPalette  that
            has been reconciled.
            """
    ClientID: str
    """
            A unique clientId passed by the client to correlate multiple subsequent continueReconcilePalette operations .
            """
    Finished: bool
    """True if the reconciliation is complete."""
    ConfigurationMisMatch: bool
    """
            Returned as true during startReconcilePalette
            if there is a configuration mismatch between the product configuration associated
            with the Fnd0ModelViewPalette  and the input product configuration. Used to
            warn the user.
            """
    OrigConfigInfo: ConfigurationDisplayInfo
    """
            The configuration information that is associated to the Fnd0ModelViewPalette,
            presented in a form that can be directly displayed to the user.
            """
    ReconcileConfigInfo: ConfigurationDisplayInfo
    """The configuration information for the current structure that is used for reconciliation."""
    EstimatedMVPsLeft: int
    """The number of Fnd0ModelViewProxy objects remaining to be reconciled."""
    PercentComplete: float
    """
            The percentage of total Fnd0ModelViewProxy objects on the Fnd0ModelViewPalette
            where reconciliation is complete.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
ServiceData is used to communicate partial
            errors to the client.
            """

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ContinueFindModelViews(self, SearchID: str, StopFind: bool) -> FindModelViewsResponse:
        """    
             Continues a search for model views that was started by the startFindModelViews
             operation. The input searchID specifies which
             partial find to continue.
             

Dependencies:

             startFindModelViews
             

Teamcenter Component:

             Disclosure - Component that is used to represent the 3D equivalent of the 2D drawing.
             
        :param SearchID: 
                         A unique identifier passed by the client in order to identify the find partial results
                         to continue searching from where the previous operation (whether <b>startFindModelViews</b>
                         or <b>continueFindModelViews</b> ) left off.
             
        :param StopFind: 
                         If true, the find associated to the input <font face="courier" height="10">searchID</font>
                         will be terminated instead of returning any further results. If false, the state
                         of the find is cleaned up and the given <font face="courier" height="10">searchID</font>
                         may no longer be used as input into the <b>continueFindModelViews</b> operation..
             
        :return: contains
             an invalid value (either never valid or the find has finished or been stopped by
             the client.)
        """
        ...
    def ContinueReconcilePalette(self, ReconcilePaletteInput: NextReconcilePaletteInput) -> ReconcilePaletteResponse:
        """    
             This operation continues the reconciliation of Fnd0ModelViewProxy object references
             in a Fnd0ModelViewPalette object for a given product structure and configuration.
             The Fnd0ModelViewProxy objects are authored and managed by  CAD applications,
             and their lifecycle is delegated to their CAD owning model's lifecycle.  As the CAD
             owning models are updated, so are their Fnd0ModelViewProxy objects.  However,
             the Fnd0ModelViewPalette objects that reference these Fnd0ModelViewProxy
             objects are not automatically updated during CAD model update in all cases, because
             there are times when this update needs to be carefully controlled by users.  Consequently,
             the Fnd0ModelViewPalette can get out of synchronization with the structure
             it is attached to.  This service operation is provided to help reconcile differences
             between the loaded structure configuration and an existing Fnd0ModelViewPalette
             in a user controlled manner.  It provides the caller with information about which
             Fnd0ModelViewProxy objects should be removed and which should be replaced
             by analyzing the current configured structure and comparing it to what was found
             in an existing Fnd0ModelViewPalette.
             
             The Fnd0ModelViewPalette contains Fnd0ModelViewProxy object references
             for  components belonging to the product structure. When the components in the structure
             gets revised, cloned, removed, or a model view is deleted or unpublished, or when
             the structure configuration gets changed, the Fnd0ModelViewPalette needs to
             be reconciled against the current structure in order to get the proper Fnd0ModelViewProxy
             objects corresponding to the updated structure. Using this operation, a list of Fnd0ModelViewProxy
             objects that need to be replaced or removed for a given Fnd0ModelViewPalette
             can be identified, retrieved, and presented to user, so that the user can carefully
             control the update of the Fnd0ModelViewPalette for the various update use
             cases.
             
             This operation is designed in such a way that the caller can use it in a threaded
             operation and display results in batches instead of waiting for the entire reconciliation
             process to be complete which may take a fair amount of time for large structures.
             Before invoking this this operation, the startReconcilePalette
             operation should have been invoked for the same clientID.
             
Note: The reconcile process has to be closed by the caller using the continueReconcilePalette operation with stopReconcile as true. For example the caller calls startReconcilePalette operation followed by continueReconcilePalette operation. Once the finished variable
             is returned as true in the response the caller calls continueReconcilePalette
             with stopReconcile as true so that the resources
             are freed up in the server.
             

Use Cases:

             The operation supports the following use cases.
             
Use Case 1 :  Update a Fnd0ModelViewPalette per informal engineering
             change (i.e. overwrite)
             
             1.An authoring user creates a detailed design in a CAD application.  The user creates
             and publishes Model Views describing the design details. The Model Views are persisted
             in Teamcenter as Fnd0ModelViewProxy objects using the operation createOrUpdateModelViewProxies.
             
             2.The authoring user opens a configured product structure in a visualization enabled
             Teamcenter application and finds the published Fnd0ModelViewProxy objects
             in the product structure using the operation findModelViewsInStructure.
             
             3.The authoring user selects a limited subset of the Fnd0ModelViewProxy objects
             found, adds them to a Palette, organizes them for presentation by re-ordering and
             grouping, and creates a Fnd0ModelViewPalette object in Teamcenter which references
             Fnd0ModelViewProxy objects using the operation createOrUpdateModelViewPalette.
             
             4.A reviewing user opens the product structure configuration along with the Fnd0ModelViewPalette
             into a visualization enabled Teamcenter application, reviews each Model View for
             accuracy, creates review comments for changes that need to be made, and submits those
             changes to the CAD Designer that authored the original detailed design.
             
             5.The authoring user receives the review comments from various reviewing users, and
             uses the CAD application to make changes to the CAD model(s) such as add or remove
             components, reposition or change parts, add, delete, or change model views, publish
             or unpublish model views, etc.  The updated CAD models are saved to Teamcenter along
             with updated Fnd0ModelViewProxy objects using the operation createOrUpdateModelViewProxies.  Since this is informal change,
             the CAD models are typically overwritten as opposed to revised.
             
             6.The authoring user opens the configured product structure with attached Fnd0ModelViewPalette
             created in step 3 in a visualization enabled Teamcenter application, and some of
             the Fnd0ModelViewProxy objects referenced by the Fnd0ModelViewPalette
             are no longer valid relative to the current structure due to the CAD model changes.
             The user invokes the palette reconcile action which triggers the operation startReconcilePalette followed by continueReconcilePalette. The results are displayed to the user
             providing information on which Fnd0ModelViewProxy objects are still valid,
             which need to be replaced, and which need to be removed in order to update the Palette.
             The results are streamed to the client  in batches, so the user is updated on progress
             and can choose to stop the reconcile operation at any time.
             
             7.The authoring user updates the Fnd0ModelViewPalette per the changes suggested
             by this operation, and saves the palette updates using the operation createOrUpdateModelViewPalette.
             

Use Case 2: Update a Fnd0ModelViewPalette to a different structure
             configuration
             
             1.The user opens a structure configuration different from that used to author the
             original Fnd0ModelViewPalette (per use case 1), and sends this to the visualization
             enabled palette authoring tool in Teamcenter.
             
             2.The user opens the Fnd0ModelViewPalette and invokes the palette reconcile
             action which triggers the operation startReconcilePalette
             followed by continueReconcilePalette. The
             results are displayed to the user providing which Fnd0ModelViewProxy objects
             cannot be found, which are still valid, which need to be replaced, and which need
             to be removed in order to reconcile the Palette to the current structure configuration.
             The results are streamed to the client  in batches, so the user is updated on progress
             and can choose to stop the reconcile operation at any time.
             
             3.The authoring user updates the Fnd0ModelViewPalette per the changes suggested
             by the operation, and saves the palette updates using the operation createOrUpdateModelViewPalette. The updated structure configuration
             information used for the updated palette is stored with the palette.
             

Use Case 3 : Update a Fnd0ModelViewPalette per formal engineering change
             (i.e. Revise)
             
             1.The user of a CAD application makes changes to the CAD model(s) representing the
             detailed design such as revising components, add, delete, or change model views,
             publish or unpublish model views, etc during revise of a detailed design.  The revised
             CAD models are saved to Teamcenter, where new and updated Fnd0ModelViewProxy
             objects are published using the operation createOrUpdateModelViewProxies
             and Teamcenter deep copy rules come into play.
             
             2.The user opens the configured product structure with attached Fnd0ModelViewPalette
             (see use case 1) in a visualization enabled Teamcenter application, and some of the
             Fnd0ModelViewProxy objects referenced by the Fnd0ModelViewPalette are
             no longer valid due to the revised CAD model(s).  Some of the Fnd0ModelViewProxy
             objects in the Fnd0ModelViewPalette are from previous revisions of the revised
             components, others cannot be found. The user invokes the palette reconcile action
             which triggers the operation startReconcilePalette
             followed by continueReconcilePalette. The
             results are displayed to the user providing information on which Fnd0ModelViewProxy
             objects are still valid, which need to be replaced with Fnd0ModelViewProxy
             objects on new revisions of the CAD models, and which need to be removed in order
             to update the Palette.  The results are streamed to the client  in batches, so the
             user is updated on progress and can choose to stop and restart the reconcile operation
             at any time.
             
             3.The user updates the Fnd0ModelViewPalette per the changes suggested by this
             operation, and saves the updated palette using the operation createOrUpdateModelViewPalette.
             

Dependencies:

             createOrUpdateModelViewPalette, createOrUpdateModelViewProxies, findModelViewsInStructure,
             startReconcilePalette
             

Teamcenter Component:

             Disclosure - Component that is used to represent the 3D equivalent of the 2D drawing.
             
        :param ReconcilePaletteInput: 
                         Input that contains the reconciliation state identifier and the <b>Fnd0ModelViewProxy</b>
                         if they have to prioritized for reconciliation.
             
        :return: 
        """
        ...
    def StartFindModelViews(self, FindInput: FindModelViewsInput) -> FindModelViewsResponse:
        """    
             Finds Model View Proxy (Fnd0ModelViewProxy) objects associated to any objects
             within the specified structure. This operation is most often used when creating a
             disclosure object.
             

             Objects that act as a disclosure are Items or Worksets that have a relation of Fnd0DisclosingObject
             to the actual design objects being disclosed and hence intend to have a list of disclosed
             Model View Proxy objects.
             

             Used in conjunction with the continueFindModelViews operation. If the preference
             MVFindMinNodeCount has a value, that value is the minimum number of structure
             nodes to search before returning with finished
             as false.
             

Use Cases:

             This API supports the following use cases:
             
             Use Case 1: Creation of a new design disclosure


             The operation can be used for supporting creation of a disclosure object. The disclosure
             object will most commonly be a Workset (Cpd0Workset subtype) but may also
             be a specific type of Item Revision. The actual disclosure object may be pre-existing
             but would not be acting as a disclosure until this operation creates and attaches
             the desired list of disclosed model view references.
             

             The purpose of a design disclosure is to act as a 3D equivalent of a 2D drawing.
             This disclosure object will collect all geometry including background geometry if
             necessary and PMI needed to show all views describing the detailed design for the
             object being disclosed. The disclosure content may be organized into the following
             item revisions or subsets (depending on the disclosure type):
             
             Foreground content - actual installation assembly reference
             
             Background content - context of a product into which the installation assembly is
             used.
             
             Separately collected geometry - such as welds between the foreground and background
             objects.
             

             To create the correct model view list (see the createOrUpdateModelViewPalette
             service operation), the client and user must first find candidate model view proxies
             from which to choose the necessary proxies to disclose.
             

             During the operation, a designer would create a Workset to collect all geometry needed
             to support  installation assembly PMI. It is done to collect assemblies being installed
             and where they are being installed so that PMI and model views associated with this
             combination can be authored and then disclosed. The following types of geometry may
             be collected in a single Workset:
             
             Foreground Subset
             
             Background Subset
             
ItemRevision (Weld Collector)
             

             Multiple CAD Designers will be concurrently authoring PMI and Model Views (MVs) for
             disclosure at multiple levels of the sub-assemblies under the installation assembly.
             All the MVs authored at this time are undisclosed. However, some of them will be
             marked as a candidates for disclosure.
             
             Owning model (ItemRevision) must exist prior to creating the MV proxy in teamcenter
             by a new service operation createOrUpdateModelViewProxies. The owing model
             will be specified as a request parameter for each MV proxy.
             

             A visualization user begins Disclosure authoring by retrieving the above mentioned
             collector workset and making sure it has disclosing object (Fnd0DisclosingObject)
             relations to the actual installation item revisions whose design is being disclosed.
             They will then use the startFindModelViews operation followed by the continueFindModelViews
             operation to find model views that are marked as candidates for disclosure and then
             use a third operation (createOrUpdateModelViewPalette) to create the list
             of actually disclosed model views to be persisted for the Disclosure being updated.
             
             Note:
             
             Candidate Disclosed Model Views will be retrievedfrom all structure nodes that are
             not suppressed or children of suppressed nodes, and then filtered only by any provided
             values in the withDisclosureIntents.
             

Teamcenter Component:

             Disclosure - Component that is used to represent the 3D equivalent of the 2D drawing.
             
        :param FindInput: 
                         The inputs needed to start a find operation on one or more objects that support model
                         views.
             
        :return: 215300 - Invalid request since startingScopes and disclosure are both not provided.
        """
        ...
    def StartReconcilePalette(self, ReconcilePaletteInput: ReconcilePaletteInput) -> ReconcilePaletteResponse:
        """    
             This operation starts the reconciliation of Fnd0ModelViewProxy object references
             in a Fnd0ModelViewPalette object for a given product structure and configuration.
             The Fnd0ModelViewProxy objects are authored and managed by  CAD applications,
             and their lifecycle is delegated to their CAD owning model's lifecycle.  As the CAD
             owning models are updated, so are their Fnd0ModelViewProxy objects.  However,
             the Fnd0ModelViewPalette objects that reference these Fnd0ModelViewProxy
             objects are not automatically updated during CAD model update in all cases, because
             there are times when this update needs to be carefully controlled by users.  Consequently,
             the Fnd0ModelViewPalette can get out of synchronization with the structure
             it is attached to. This service operation is provided to help reconcile differences
             between the loaded structure configuration and an existing Fnd0ModelViewPalette
             in a user controlled manner.  It provides the caller with information about which
             Fnd0ModelViewProxy objects should be removed and which should be replaced
             by analyzing the current configured structure and comparing it to what was found
             in an existing Fnd0ModelViewPalette.
             
             The Fnd0ModelViewPalette contains Fnd0ModelViewProxy object references
             for  components belonging to the product structure. When the components in the structure
             gets revised, cloned, removed, or a model view is deleted or unpublished, or when
             the structure configuration gets changed, the Fnd0ModelViewPalette needs to
             be reconciled against the current structure in order to get the proper Fnd0ModelViewProxy
             objects corresponding to the updated structure.  Using this operation, a list of
             Fnd0ModelViewProxy objects that need to be replace or removed for a given
             Fnd0ModelViewPalette can be identified, retrieved and presented to user, so
             that the user can carefully control the update of the Fnd0ModelViewPalette
             for the various update use cases.
             
             This operation is designed in such a way that the caller can use it in a threaded
             operation and display results in batches instead of waiting for the entire reconciliation
             process to be complete which may take a fair amount of time for large structures.
             This operation is thus supplemented by continueReconcilePalette
             operation.
             
Note: The reconcile process has to be closed by the caller using the continueReconcilePalette operation with stopReconcile as true. For example the caller calls startReconcilePalette operation followed by continueReconcilePalette operation. Once the finished variable
             is returned as true in the response the caller calls continueReconcilePalette
             with stopReconcile as true so that the resources
             are freed up in the server.
             

Use Cases:

             The operation supports the following use cases.
             
Use Case 1 : Update a Fnd0ModelViewPalette per informal engineering
             change (i.e. overwrite)
             
             1. An authoring user creates a detailed design in a CAD application.  The user creates
             and publishes Model Views describing the design details. The Model Views are persisted
             in Teamcenter as Fnd0ModelViewProxy objects using the operation createOrUpdateModelViewProxies.
             
             2. The authoring user opens a configured product structure in a visualization enabled
             Teamcenter application and finds the published Fnd0ModelViewProxy objects
             in the product structure using the operation findModelViewsInStructure.
             
             3. The authoring user selects a limited subset of the Fnd0ModelViewProxy objects
             found, adds them to a Palette, organizes them for presentation by re-ordering and
             grouping, and creates a Fnd0ModelViewPalette object in Teamcenter which references
             Fnd0ModelViewProxy objects using the operation createOrUpdateModelViewPalette.
             
             4. A reviewing user opens the product structure configuration along with the Fnd0ModelViewPalette
             into a visualization enabled Teamcenter application, reviews each Model View for
             accuracy, creates review comments for changes that need to be made, and submits those
             changes to the CAD Designer that authored the original detailed design.
             
             5. The authoring user receives the review comments from various reviewing users,
             and uses the CAD application to make changes to the CAD model(s) such as add or remove
             components, reposition or change parts, add, delete, or change model views, publish
             or unpublish model views, etc.  The updated CAD models are saved to Teamcenter along
             with updated Fnd0ModelViewProxy objects using the operation createOrUpdateModelViewProxies.  Since this is informal change,
             the CAD models are typically overwritten as opposed to revised.
             
             6. The authoring user opens the configured product structure with attached Fnd0ModelViewPalette
             created in step 3 in a visualization enabled Teamcenter application, and some of
             the Fnd0ModelViewProxy objects referenced by the Fnd0ModelViewPalette
             are no longer valid relative to the current structure due to the CAD model changes.
             The user invokes the palette reconcile action which triggers the operation startReconcilePalette followed by continueReconcilePalette. The results are displayed to the user
             providing information on which Fnd0ModelViewProxy objects are still valid, which
             need to be replaced, and which need to be removed in order to update the Palette.
             The results are streamed to the client  in batches, so the user is updated on progress
             and can choose to stop the reconcile operation at any time.
             
             7. The authoring user updates the Fnd0ModelViewPalette per the changes suggested
             by this operation, and saves the palette updates using the operation createOrUpdateModelViewPalette.
             

Use Case 2: Update a Fnd0ModelViewPalette to a different structure
             configuration
             
             1.The user opens a structure configuration different from that used to author the
             original Fnd0ModelViewPalette (per use case 1), and sends this to the visualization
             enabled palette authoring tool in Teamcenter.
             
             2.The user opens the Fnd0ModelViewPalette and invokes the palette reconcile
             action which triggers the operation startReconcilePalette
             followed by continueReconcilePalette. The
             results are displayed to the user providing which Fnd0ModelViewProxy objects
             cannot be found, which are still valid, which need to be replaced, and which need
             to be removed in order to reconcile the Palette to the current structure configuration.
             The results are streamed to the client  in batches, so the user is updated on progress
             and can choose to stop the reconcile operation at any time.
             
             3.The authoring user updates the Fnd0ModelViewPalette per the changes suggested
             by the operation, and saves the palette updates using the operation createOrUpdateModelViewPalette. The updated structure configuration
             information used for the palette update is stored with the palette.


             Use Case 3 : Update a Fnd0ModelViewPalette per formal engineering change
             (i.e. Revise)
             
             1.The user of a CAD application makes changes to the CAD model(s) representing the
             detailed design such as revising components, add, delete, or change model views,
             publish or unpublish model views, etc during revise of a detailed design.  The revised
             CAD models are saved to Teamcenter, where new and updated Fnd0ModelViewProxy
             objects are published using the operation createOrUpdateModelViewProxies
             and Teamcenter deep copy rules come into play.
             
             2.The user opens the configured product structure with attached Fnd0ModelViewPalette
             (see use case 1) in a visualization enabled Teamcenter application, and some of the
             Fnd0ModelViewProxy objects referenced by the Fnd0ModelViewPalette are
             no longer valid due to the revised CAD model(s).  Some of the Fnd0ModelViewProxy
             objects in the Fnd0ModelViewPalette are from previous revisions of the revised
             components, others cannot be found. The user invokes the palette reconcile action
             which triggers the operation startReconcilePalette
             followed by continueReconcilePalette. The
             results are displayed to the user providing information on which Fnd0ModelViewProxy
             objects are still valid, which need to be replaced with Fnd0ModelViewProxy
             objects on new revisions of the CAD models, and which need to be removed in order
             to update the Palette.  The results are streamed to the client  in batches, so the
             user is updated on progress and can choose to stop and restart the reconcile operation
             at any time.
             
             3.The user updates the Fnd0ModelViewPalette per the changes suggested by this
             operation, and saves the updated palette using the operation createOrUpdateModelViewPalette.
             

Dependencies:

             createOrUpdateModelViewPalette, createOrUpdateModelViewProxies, findModelViewsInStructure
             

Teamcenter Component:

             Disclosure - Component that is used to represent the 3D equivalent of the 2D drawing.
             
        :param ReconcilePaletteInput: 
                         Input that contains the <b>Fnd0ModelViewPalette</b> or <b>Fnd0ModelViewProxy</b>
                         that needs to be reconciled and the configuration information.
             
        :return: 
        """
        ...

