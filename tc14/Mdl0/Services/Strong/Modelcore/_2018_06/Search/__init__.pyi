import Mdl0.Services.Strong.Modelcore._2011_06.Search
import Mdl0.Services.Strong.Modelcore._2013_05.Search
import Mdl0.Services.Strong.Modelcore._2014_10.Search
import Mdl0.Services.Strong.Modelcore._2017_05.Search
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ClassificationExpression:
    """
    
            Search Expression is a part of ClassificationExpressionInput which will be
            used to Find Classified Model Element Objects based on classification attributes
            & their values.
            
    """
    def __init__(self, ) -> None: ...
    InClassClassName: str
    """Name of the Classification class to use for search."""
    AttributeIds: list[int]
    """A list of Classification attribute Ids."""
    AttributeValues: list[str]
    """
            A list of values which is parallel to the Classification attribute id list with the
            operator used for comparison in the criteria and the metric to be used for comparison.
            The value may also include the combination operator (only AND is supported) name
            followed by ':' if there are more than one criteria is specified in the in class
            search expression.E.g. "AND:= a.METRIC".
            """

class ClassificationExpressionInput:
    """
    Classification Expression Input.
    """
    def __init__(self, ) -> None: ...
    RootType: str
    TraversalKey: str
    ClassificationExpression: ClassificationExpression
    """
            ClassificationExpression containing Class, attribute IDs & attribute values based
            on which the search will be performed.
            """
    Clientid: str
    """
            A unique string sent by the calling function, so that the output Search Expression
            object could be mapped back to the input.
            """

class IncludeAllExpressionInput:
    """
    Input Data to create an IncludeAll search expression.
    """
    def __init__(self, ) -> None: ...
    Clientid: str
    """
            A unique string sent by the calling function, so that the output Search Expression
            object could be mapped back to the input.
            """

class SearchScope2:
    """
    Scope for this Search (Model and type of Search)
    """
    def __init__(self, ) -> None: ...
    Model: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """Application Model that scopes this search"""
    SearchType: list[str]
    RecipeContainer: Teamcenter.Soa.Client.Model.ModelObject
    """
Mdl0SubsetDefinition, Cpd0DesignSubsetInstance, Ptn0Partition
            or Mdl0BaselineDefinition for which the search needs to be executed. When
            the recipe container is specified, there is no need to specify the recipe (search
            expression set) separately.
            
            Note: if used in the input to setRecipes3,
            this means this container will be used as the source recipe, i.e. the recipe from
            this container will be copied to the target recipe container.
            """
    DomainViewKeyName: str
    """
            Domain view key is the name of the preference which holds the search filter list
            types.
            
            Either searchType list or domainViewKeyName may be passed to setRecipes3
            operation.
            
            If only a domainViewKeyName was provided
            during the setRecipes3 operation, getRecipes3 operation will return the domainViewKeyName
            and the search type list that was stored from the preference value at the time of
            recipe creation.
            
            If both, searchType list and domainViewKeyName are passed, then the explicit filter list will
            be stored in the recipe and list from the preference will be ignored.
            """

class SearchRecipe3:
    """
    Recipe for executing the Search
    """
    def __init__(self, ) -> None: ...
    Scope: SearchScope2
    """Scope of Search  Model, search types."""
    ConfigDetails: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ConfigurationDetail]
    """
            List of Configuration information to apply. Configuration information specifies the
            RevisionRule and optional effectivity and variant configuration.
            
            Configuration information is required for Universal configuration and optional for
            Partition configuration. If more than one list member specifies Universal configuration,
            the last one is used. If more than one list member specifies Partition configuration,
            the last one is used.
            """
    SearchExpression: Mdl0.Services.Strong.Modelcore._2014_10.Search.SearchExpressionSet2
    """Expression set to be evaluated as search criteria"""

class RecipeData3:
    """
    
            This data structure associates a search recipe to its recipe container. It is used
            to save search recipes against a recipe container.
            
    """
    def __init__(self, ) -> None: ...
    RecipeContainer: Teamcenter.Soa.Client.Model.ModelObject
    """
            Recipe container object. Supported types: Mdl0SubsetDefinition, Cpd0DesignSubsetInstance,
            Ptn0Partition, or Mdl0BaselineDefinition
"""
    Recipe: SearchRecipe3
    """
            Associated Search Recipe. The Search Recipe is defined by the SearchRecipe3 data
            structure, which has the following contents:
            

scope   Scope of the Search
            (Application Model, search types, domain view key).
            
configDetails   Configuration
            information used in the search (RevisionRule and optional effectivity and
            variant configuration).
            
searchExpression   Top level
            SearchExpressionSet2 that could be any level
            deep and defines a complex search recipe by combining the elemental Search Expressions
            created by createSearchExpressions operation.
            

"""

class RecipeResponse3:
    """
    
            Response for a getRecipes3 operation. Returns
            the search recipe attached to a RecipeContainer.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data for error information."""
    SearchRecipes: list[RecipeData3]
    """
            A list of Recipe Data objects for the given RecipeContainer objects. The RecipeData2
            structure returns the following information:
            

recipeContainer  The reference to the RecipeContainer object
            from which the recipe is retrieved .
            
recipe   The SearchRecipe2
            data structure that returns the scope, configuration details and the search expression
            set that represents the stored search recipe.
            

"""

class SearchExpressionInput:
    """
    
            Each one of the input data structure has client id that will track the corresponding
            Search Definition object in the response data structure.
            
    """
    def __init__(self, ) -> None: ...
    ReturnType: str
    """
            Type name of the the Business Objects to be returned. All objects returned will be
            of this type, or sub-type of the this type. For Example: Cpd0DesignElement.
            """
    ProximitySearchExpressions: list[Mdl0.Services.Strong.Modelcore._2017_05.Search.ProximitySearchExpressionInput]
    """
            A list for creating proximity search expressions. Contains reference to a set of
            Objects of type Mdl0ModelElements (that are targets) and the proximity distance.
            """
    BoxZoneExpressions: list[Mdl0.Services.Strong.Modelcore._2017_05.Search.BoxZoneExpressionInput]
    """
            A list for creating box zone search expressions. Contains the minimum and maximum
            coordinates of a test box definition.
            """
    PlaneZoneExpressions: list[Mdl0.Services.Strong.Modelcore._2017_05.Search.PlaneZoneExpressionInput]
    """
            A list for creating plane zone search expressions. Contains a point in the plane
            and the normal vector definition.
            """
    SavedQueryExpressions: list[Mdl0.Services.Strong.Modelcore._2017_05.Search.SavedQueryExpressionInput]
    """
            A list for creating saved query search expressions. Contains reference to a stored
            saved query object and a coordinated list of entries and values to be used in the
            saved query. Some queries may contain empty list for entries and values (depends
            on the definition of the saved query). Wildcards which all are supported in Teamcenter
            Search are accepted for values in the saved query.
            """
    CompositeExpressions: list[Mdl0.Services.Strong.Modelcore._2017_05.Search.CompositeSearchExpressionInput]
    """
            A list of search expressions to be executed as single search term. This will typically
            be used to search for objects based on properties of some other object. The composite
            search terms will be combined together with logical AND operator.
            """
    ClosureQueryExpression: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ClosureQueryExpressionInput]
    """Not implemented."""
    OptionSetExpressions: list[Mdl0.Services.Strong.Modelcore._2013_05.Search.OptionSetExpressionInput]
    """
            Option Set Expression that defines the Transfer Option Set and option values that
            are used traverse the closure defined for the Transfer Option Set.
            """
    GeomConstraintExpressions: list[Mdl0.Services.Strong.Modelcore._2014_10.Search.GeomConstraintExpressionInput]
    """
            Input for creating geometric constraint collection search expressions. Contains
            an integer flag that indicates how the search result is treated to fetch the related
            constraint data and reference to source search criteria on which the constraint search
            term is to be applied.
            """
    ClassificationExpressions: list[ClassificationExpressionInput]
    """
            A list for creating classification search expressions.  Contains Classification objects,
            their respective attributes and values. Some expressions may contain only Classification
            Objects. Classification Attributes and values are not mandatory. The Classification
            search term can be combined with logical AND operator.
            """
    IncludeAllExpressions: list[IncludeAllExpressionInput]
    """
            Input for creating include all search expression. This search expression will return
            all the objects of type ConditionalElements in the context of an application
            model.
            """
    IncludeElements: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ModelElementInput]
    """
            A list of objects to be included into the search results. The server creates a Search
            Expression for this input as well, so that it could be combined with other search
            expressions in a search recipe.
            """
    ExcludeElements: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ModelElementInput]
    """
            A list of objects that should be explicitly excluded in the search results. Again
            a search expression is returned for the exclude elements so that it could be combined
            with other search expressions in a search recipe.
            """

class Search:
    """
    Interface Search
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateSearchExpressions(self, SearchExpressionInput: SearchExpressionInput) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchExpressionResponse:
        """    
             This operation creates the elemental search expressions that could be combined using
             logical operators to build up a complex search recipe. The createSearchExpressions
             operation could be used to create multiple search expressions at the same time. The
             following types of expressions could be created by this operation.
             

             Bounding Box Expression (Mdl0SearchBoxZone)
             
             Plane Zone Expression (Mdl0SearchPlaneZone)
             
             Proximity Expression (Mdl0SearchProximity)
             
             Saved Query Expression (Mdl0SearchSavedQuery)
             
             Composite Search Expression(Mdl0CompositeSearchDef)
             
             Geometric Constraint Expression (Mdl0SearchGeomConstraint)
             
             Classification Search Expression (Mdl0SearchClassification)
             
             Include Content Expression (Mdl0SearchSlctContent)
             
             Exclude Content Expression (Mdl0SearchGroup)
             


             The above search expressions can be build for various types of Business Object types.
             Information about how to traverse from one type to another type is embedded within
             a search expression input.
             

Use Cases:

             The createSearchExpressions is a required operation before an executeSearch or setRecipes2
             call is made. This operation creates the runtime Search Definition objects based
             on the input search expression data structures. The intent of this operation is to
             create all the individual elemental search expressions so that they could be combined
             using logical operators (AND, OR, NOT) to create a complex search recipe.
             

Dependencies:

             executeSearch, setRecipes, setRecipes2
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param SearchExpressionInput: 
                         Search Expression Input Structure
             
        :return: SearchExpressionResponse data structure that returns the Search Expression objects
             created for the given Search Expression Input data structures.
        """
        ...
    def GetRecipes3(self, RecipeContainers: list[Teamcenter.Soa.Client.Model.ModelObject]) -> RecipeResponse3: ...
    def SetRecipes3(self, RecipeInputs: list[RecipeData3]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

