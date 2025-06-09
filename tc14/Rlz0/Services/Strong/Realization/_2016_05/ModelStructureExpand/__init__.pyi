import Rlz0.Services.Strong.Realization._2015_07.ModelStructureExpand
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ModelExpandControls2:
    """
    A set of controls for clients to stipulate the output of the expand processing.
    """
    def __init__(self, ) -> None: ...
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            Reference to the configuration context object (ConfigurationContext). It is
            used to configure the expanded model elements (Mdl0ModelElement) or model
            artifacts (Mdl0ModelArtifact) under the composition (Rlz0Composition).
            """
    ExpandSubsetAsSaved: bool
    """Reserved for future use."""
    IncludeCopyStableIDMaps: bool
    """
            If true, copy stable ID maps(copyStableIDMap)
            will be returned in the response.
            """
    IncludeSourceObjectForSubsets: bool
    """
            Specifies if source objects are to be returned with or without encoded in-context
            data for Sparse operations.
            
            If true, source objects are returned with encoded in-context data.
            
            If false, source objects are returned without encoded in-context data.
            """
    LevelsToExpand: int
    """
            The number of levels to expand, where 0 signifies to expand all levels, 1 signifies
            to expand the next level only. Values other than 0 or 1 are not supported.
            """
    PreLoadVisualizationDatasets: bool
    """
            If true, pre loads the Dataset used by visualization into the server so that
            they may be returned via property references on any Mdl0PositionedModelElement
            object. The default value is false.
            """
    ContextObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The context object under which the expansion starts, this could be either an object
            of type Mdl0ApplicationModel or Rlz0Subset.
            """
    ObjectToExpand: Teamcenter.Soa.Client.Model.ModelObject
    """
            Object to expand, which could be an instance of subclass of Rlz0Composition
            class or an instance of Rlz0Subset.
            """
    ExpandOptions: System.Collections.Hashtable
    """
            Flags to be used during expand.
            
            Supported keys:
            

            1. sourceModel - Only the model content that belongs to the specified sourceModel
            (Mdl0ApplicationModel) will be expanded.
            
            2. Purpose - Only the sparse model content (Mdl0ModelElement) that satisfies
            the input purpose will be expanded.
            

            Supported values:
            
            For souceModel - The ID of Source application Model. ( Mdl0ApplicationModel
            )
            
            For Purpose - The rlz0Purpose value of Rlz0Subset.
            

            Example key-value pairs:-
            
            Key:                        Value:
            
            sourceModel         sourceModel ID1
            
            sourceModel         sourceModel ID2
            
            Purpose                   Consumed
            
            Purpose                   WorkArea
            """
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify returned sparse
            elements and Partial Errors associated with this input operation. This is an optional
            argument.
            """
    EffectivityFormulaOverlayMap: System.Collections.Hashtable
    """
            A map of (BusinessObject, string)
            
            Key: Source application model(Mdl0ApplicationModel).
            
            Value: The effectivity overlay information (string)which will be combined with effectivity
            configuration information criteria defined on the Rlz0Subset to further narrow
            the scope of content returned by the expand.
            """
    VariantFormulaOverlayMap: System.Collections.Hashtable
    """
            A map of (BusinessObject, string)
            
            Key: Source application model(Mdl0ApplicationModel).
            

            Value:The variant overlay information (string)which will be combined with variant
            configuration information criteria defined on the Rlz0Subset to further narrow
            the scope of content returned by the expand.
            """

class ModelStructureExpand:
    """
    Interface ModelStructureExpand
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExpandModelStructure2(self, Input: list[ModelExpandControls2]) -> Rlz0.Services.Strong.Realization._2015_07.ModelStructureExpand.ModelStructureExpandResponse:
        """    
             This is a generic operation to expand instances of Mdl0ConditionalElement
             or Mdl0ConditionalArtifact. Currently, this operation supports expansion of
             objects which are instances of subclass of Rlz0Composition or instances of
             Rlz0Subset Class. Objects are expanded in the order of the input list and
             results are paged back to the client.
             

             Pre-Conditions:
             
             1. The source application model has some pre-existing model content.
             
             2. Target application model already exists and has composition and subsets.
             

             Limitations:
             
             Current expansion support is available only for the following classes:-
             
             1. Subclasses of Rlz0Composition.(Rlz0Composition is an abstract class)
             
             2. Rlz0Subset.
             

Use Cases:

             This API supports the navigation of contents of Rlz0Composition object or
             Rlz0Subset object with effectivity and variant overlays.
             

             General use cases are:-
             
             1. Expansion of an Rlz0Composition object: - Expansion of an Rlz0Composition
             object returns all the Rlz0Subset objects that it contains.
             
             2. Expansion of an Rlz0Subset object: - Expansion of an Rlz0Subset
             object returns sparsely or dynamically realized model elements (Mdl0ModelElement)
             from source application model (Mdl0ApplicationModel). Unlike the concept of
             Full or Static Realization, model elements (Mdl0ModelElement) in the target
             application model (Mdl0ApplicationModel) are not new copies rather simple
             references to objects in source application model.
             

             This API provides the support to expand appropriate sparse elements by applying filters
             like Purpose (rlz0purpose on Rlz0Subset object) and SourceModel (Mdl0ApplicationModel)
             that are used during the expansion of composition (Rlz0Composition) or subset
             (Rlz0Subset).
             

             Also,this API provides the support to expand appropriate sparse elements by applying
             effectivity and variant overlay strings for input Mdl0ApplicationModel that
             are used during the expansion of composition (Rlz0Composition) or subset (Rlz0Subset).
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Input: 
                         List of controls (<font face="courier" height="10">ModelExpandControls2</font>) which
                         govern the expansion of objects.
             
        :return: 2. 279055 - The provided number of levels to expand is invalid. Valid values are
             0 or 1 for this operation.
        """
        ...

