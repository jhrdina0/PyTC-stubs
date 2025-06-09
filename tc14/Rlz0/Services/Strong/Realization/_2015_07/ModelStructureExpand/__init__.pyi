import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CopyStableIDInfo:
    """
    
            This structure contains a map of copystableID (a unique identifier which is restored
            across all the revisions and copies of the object) information for sparse model elements(Mdl0ModelElement)
            and realization artifacts(Rlz0Subset).
            
    """
    def __init__(self, ) -> None: ...
    CopyStableIDMap: System.Collections.Hashtable
    Subset: Teamcenter.Soa.Client.Model.Strong.Rlz0Subset
    """The subset object (Rlz0Subset) which is the context for the copy stable ID"""

class ModelExpandControls:
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
    """Reserved for future use."""
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
            
            Supported keys:
            
            1.sourceModel - Only the model content that belongs to the specified sourceModel
            (Mdl0ApplicationModel) will be expanded.
            
            2. Purpose - Only the sparse model content (Mdl0ModelElement) that satisfies
            the input purpose will be expanded.
            

            Supported values:
            
            For souceModel - The ID of Source application Model. ( Mdl0ApplicationModel
            )
            
            For Purpose - The rlz0Purpose value of Rlz0Subset.
            

            Example key-value pairs:-
            
Key                    
            Value

            sourceModel            sourceModel ID1
            
            sourceModel            sourceModel ID2
            
            Purpose                    Consumed
            
            Purpose                    WorkArea
            

"""
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify returned sparse
            elements and Partial Errors associated with this input operation. This is an optional
            argument.
            """

class ModelExpandResponse:
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string sent by the calling function, so that the output response could be
            mapped back to the input.
            """
    CopyStableIDData: list[CopyStableIDInfo]
    """
            A list of copy stable ID data (CopyStableIDInfo).
            

            Data about the Copy stable IDs of sparse model elements of each Rlz0Subset
            object in a composition object(subclass of Rlz0Composition).  This ID will
            remain constant across revise and save-as (copy) of a Composition revision.
            
"""
    ElementContent: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of expanded objects."""

class ModelStructureExpandResponse:
    """
    
            List of ModelExpandResponse structures which are mapped to the source input structures
            using the clientId. Each structure contains the result of the expansion for the input
            composition ( subclass of Rlz0Composition) object or for subset object (Rlz0Subset).
            The service data contains any additional error related information.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[ModelExpandResponse]
    """This structure contains the expand response for given set of ModelExpandControls."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains error related information."""

class ModelStructureExpand:
    """
    Interface ModelStructureExpand
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExpandModelStructure(self, Input: list[ModelExpandControls]) -> ModelStructureExpandResponse:
        """    
             This is a generic operation to expand instances of Mdl0ConditionalElement
             or Mdl0ConditionalArtifact. Currently, this operation supports expand of objects
             which are instances of subclass of Rlz0Composition or  instances of Rlz0Subset
             Class. Objects are expanded in the order of the input list and results are paged
             back to the client.
             

             Pre-Conditions:
             
             1. The source application model has some pre-existing model content.
             
             2. Target application model already exists and has composition and subsets.
             

             Limitations:
             
             Current expansion support is available only for the following classes:-
             
             1. Subclasses of Rlz0Composition.(Rlz0Composition is an abstract class)
             
             2. Rlz0Subset.
             


Use Cases:

             This API supports the navigation of contents of Rlz0Composition object or
             Rlz0Subset object.
             

             General use cases are:-
             
             1. Expansion of an Rlz0Composition object: - Expansion of an Rlz0Composition
             object returns all the Rlz0Subset objects that it contains.
             
             2. Expansion of an Rlz0Subset object: - Expansion of an Rlz0Subset
             object returns sparsely or dynamically realized model elements (Mdl0ModelElement)
             from source application model (Mdl0ApplicationModel). Unlike the concept of
             Full or Static Realization, model elements (Mdl0ModelElement) in the target
             application model (Mdl0ApplicationModel) are not new copies rather simple
             references to objects in source application model.
             

             Also, this API provides the support to expand appropriate sparse elements by applying
             filters like Purpose (rlz0purpose on Rlz0Subset object) and SourceModel
             (Mdl0ApplicationModel)   that are used during the expansion of composition
             (Rlz0Composition) or subset (Rlz0Subset).
             



Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Input: 
                         List of controls (<font face="courier" height="10">ModelExpandControls</font>) which
                         govern the expansion of objects.
             
        :return: 
        """
        ...

