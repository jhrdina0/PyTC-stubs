import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BoxZoneExpression:
    """
    Expression to search in Box Zone
    """
    def __init__(self, ) -> None: ...
    SearchBoxes: list[SearchBox]
    """
            A list of 3D box coordinate definitions. Even though the structure is specifying
            a list of boxes, the current implementation processes only one Box (first one) and
            the list is just for future expansion purposes.
            """
    BoxOperator: str
    """specifies the search operation i.e. inside or outside or intersecting the box."""

class BoxZoneExpressionInput:
    """
    Box Zone Expression Input Structure
    """
    def __init__(self, ) -> None: ...
    BoxZoneExpression: BoxZoneExpression
    """Box zone expression, contains the definition of the coordinates to a spatial 3D box."""
    Clientid: str
    """
            A unique string sent by the calling function, so that the output Search Expression
            object could be mapped back to the input.
            """

class ClosureQueryExpression:
    """
    Elemental Closure Query Expression - No Implementation in Tc9
    """
    def __init__(self, ) -> None: ...
    ClosureRule: Teamcenter.Soa.Client.Model.Strong.ClosureRule
    """Reference to the ClosureRule object."""
    SearchCriteria: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchDef
    """The Mdl0SearchDef object that represents the rest of the search expression."""

class ClosureQueryExpressionInput:
    """
    Closure Query Expression Input Data Structure - NO IMPLEMENTATION in Tc9
    """
    def __init__(self, ) -> None: ...
    ClosureExpression: ClosureQueryExpression
    """Search Expression representing the closure rule."""
    Clientid: str
    """
            A unique string sent by the calling function, so that the output Search Expression
            object could be mapped back to the input.
            """

class ConfigOutput:
    """
    Output Data Structure for Configuration Data
    """
    def __init__(self, ) -> None: ...
    ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """Configuration Context Object Reference"""
    Clientid: str
    """Client ID to track response with request"""

class ConfigResponse:
    """
    
            Response for a createOrUpdateConfigurations
            operation. Returns runtime configuration objects
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data for any error information. Following are possible partial errors in
            the ServicData structure:
            

MDL0MODEL_invalid_revision_rule_clause
            (278030)  The revision rule used to create a ConfigurationContext object
            has invalid clauses (clauses not valid for CPD application).
            

"""
    ConfigContext: list[ConfigOutput]
    """
            Configuration Context output structure. Contains the reference to the Configuration
            Context object reference and the corresponding client id to match up the input.
            """

class ConfigurationData:
    """
    
            Configuration Input Data structure that is used to create or modify a configuration
            context object
            
    """
    def __init__(self, ) -> None: ...
    ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """Run time Config object that carries the configuration data"""
    RevisionRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """Revision Rule that carries revision and effectivity configuration"""
    VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule
    """Variant Rule (Tc9 -  No Operation) for future use"""
    Clientid: str
    """Client ID for tracking configuration response"""

class ConfigurationDetail:
    """
    Configuration mapping for various configuration object types.
    """
    def __init__(self, ) -> None: ...
    ConfigurationFor: str
    """
            Configuration type. If the value is "Universal",
            the configContext applies to all objects.
            If the value is "Partition", the configContext is applied to partitions only.
            """
    ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
ConfigurationContext having configuration data (RevisionRule and optional
            effectivity and variant configuration).
            """

class ExpressionResponse:
    """
    
            Expression Response structure that carries the search expressions created in the
            server
            
    """
    def __init__(self, ) -> None: ...
    SearchDef: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchDef
    """
            Reference to the Mdl0SearchDef object which is the search expression object
            created based on the input expression type information.
            """
    Clientid: str
    """
            A unique string sent by the calling function, so that the output Search Expression
            object could be mapped back to the input.t
            """

class ModelElementInput:
    """
    
            Model Element Input Data Structure. Special case for ModelElement input is the creation
            of Empty Expression. If the set of Model Elements is empty then createSearchExpressions
            will create an Empty Expression (Mdl0SearchDef object)
            
    """
    def __init__(self, ) -> None: ...
    ModelElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """
            A list of Mdl0ModelElement objects used to create the select content search
            expression.
            """
    Clientid: str
    """
            A unique string sent by the calling function, so that the output Search Expression
            object could be mapped back to the input.
            """

class PlaneZone:
    """
    Coordinates for a Plane Zone
    """
    def __init__(self, ) -> None: ...
    Xvalue: float
    """X-Value"""
    Yvalue: float
    """Y-Value"""
    Zvalue: float
    """Z-Value"""
    Displacement: float
    """distance vector normal to the plane."""

class PlaneZoneExpression:
    """
    Expression to model Plane Zone Search
    """
    def __init__(self, ) -> None: ...
    PlaneZone: PlaneZone
    """Definition of the 3D plane."""
    PlaneZoneOperator: str
    """
            The operation type i.e. Search above the plane or below the plane or intersecting
            the plane.
            """

class PlaneZoneExpressionInput:
    """
    Plane Zone Input Structure
    """
    def __init__(self, ) -> None: ...
    PlaneZoneExpression: PlaneZoneExpression
    """3D plane expression around which the spatial search is performed."""
    Clientid: str
    """
            A unique string sent by the calling function, so that the output Search Expression
            object could be mapped back to the input.
            """

class ProximityExpression:
    """
    search expression structure for proximity search
    """
    def __init__(self, ) -> None: ...
    TargetElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """List of target Mdl0ModelElement whose proximity is searched."""
    Distance: float
    TargetElement: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchDef
    """
            A select content search expression that references a set of target Mdl0ModelElement.
            This is an alternative way of specifying the target. Either of targetElements
            list or the targetElement object is expected to be populated in this structure.
            """

class ProximitySearchExpressionInput:
    """
    Proximity Expression Input - Request Structure
    """
    def __init__(self, ) -> None: ...
    ProximityExpression: ProximityExpression
    """
            Proximity Search Expression. Contains reference to the target elements whose proximity
            is searched and the distance to search.
            """
    Clientid: str
    """
            A unique string sent by the calling function, so that the output Search Expression
            object could be mapped back to the input.
            """

class SearchScope:
    """
    Scope for this Search (Model and type of Search)
    """
    def __init__(self, ) -> None: ...
    Model: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """Application Model that scopes this search"""
    SearchType: list[str]
    """
            List of object types to allow in search results. Objects which are not of these types
            will be silently discarded.
            

            Valid values include "Mdl0ModelElement", and the names of classes derived from Mdl0ModelElement.
            

            If the list is empty, and object that matches the search recipe will be included
            in the search results.
            """
    RecipeContainer: Teamcenter.Soa.Client.Model.ModelObject
    """
Mdl0SubsetDefinition or Cpd0DesignSubsetInstance or Ptn0Partition
            or Mdl0BaselineDefinition for which the search needs to be executed. When
            the recipe container is specified, there is no need to specify the recipe (search
            expression set) separately. Note: if used in the input to setRecipes, this means
            this container will be used as the source recipe, i.e. the recipe from this container
            will be copied to the target recipe container.
            """

class SearchExpression:
    """
    Group of search expressions (or Mdl0SearchDef objects) used in a search recipe
    """
    def __init__(self, ) -> None: ...
    SearchExpressions: list[Teamcenter.Soa.Client.Model.Strong.Mdl0SearchDef]
    """
            A list of leaf node search expressions. Leaf nodes include spatial nodes (such as
            Mdl0SearchBoxZone expressions or Mdl0SearchProximity expressions) or
            non-spatial nodes (such as Mdl0SearchSavedQuery expressions or  Mdl0SearchSlctContent
            expressions).
            
            The list may be combined using a SearchOperator.
            See SearchExpressionSet2.
            
"""
    DoTrushapeRefinement: bool
    """
            If true, use any true shape data to further refine the results of spatial tests (box
            zone, plane zone and proximity expressions only).
            """

class SearchExpressionSet:
    """
    Building block to build complex search expressions
    """
    def __init__(self, ) -> None: ...
    SearchOperator: str
    """List of search expressions combined by the search operator."""
    SearchExpression: SearchExpression
    """
            Search Expressions to be executed. In case of more than one a OR operator is assumed
            between these expressions.Either one of the properties  will be populated i.e. searchOperator and searchExpressionSets
            or the searchExpression, in a structure.
            """
    SearchExpressionSets: list[SearchExpressionSet]
    """List of search expressions combined by the search operator."""

class SearchRecipe:
    """
    Recipe for executing the Search
    """
    def __init__(self, ) -> None: ...
    Scope: SearchScope
    """Scope of Search  Model, search types"""
    ConfigDetails: list[ConfigurationDetail]
    """Configuration Information  Revision Rule, Effectivity Rule"""
    SearchExpression: SearchExpressionSet
    """Expression set to be evaluated  search criteria"""

class RecipeData:
    """
    
            This data structure associates a search recipe to its recipe container. It is used
            to save search recipes against a recipe container.
            
    """
    def __init__(self, ) -> None: ...
    RecipeContainer: Teamcenter.Soa.Client.Model.ModelObject
    """
            Object reference to a recipe container. This object could be either of
            

Mdl0SubsetDefinition

Cpd0DesignSubsetInstance

Ptn0Partition


"""
    Recipe: SearchRecipe
    """
            Associated Search Recipe. The Search Recipe is defined by the SearchRecipe data structure,
            which has the following contents:
            

scope   Scope of the Search
            (Application Model, search types).
            
configDetails   Configuration
            information used in the search (Revision Rule and Effectivity Rule).
            
searchExpression   Top level
            SearchExpressionSet that could be any level
            deep and defines a complex search recipe by combining the elemental Search Expressions
            created by createSearchExpressions operation.
            

"""

class RecipeResponse:
    """
    Response for a Get Recipe Call. Returns the search recipe attached to a RecipeContainer.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service Data for error information. The following are errors thrown by the getRecipes operation in the ServiceData structure:
            
Mdl0Model_invalid_recipe_container (278017)
            The recipe container object passed as input is not a valid recipe container object.
            The recipe container has to be one of Mdl0SubsetDefinition, Ptn0Partition
            or Cpd0DesignSubsetInstance.
            
MDL0MODEL_invalid_recipe_to_load (278027)
            The recipe container object has a search recipe that is not a valid object. The
            search criteria objects are of class ApprSearchCriteria (and its subtypes)
            and if these are combined in a fashion that is not readable by the CPD application
            then this error would be thrown
            
"""
    SearchRecipes: list[RecipeData]
    """
            Recipe Data for the given RecipeContainer objects. The RecipeData structure returns the following information:
            

recipeContainer  The reference
            to the RecipeContainer object from which the recipe is retrieved .
            
recipe   The SearchRecipe data structure that returns the scope, configuration
            details and the search expression set that represents the stored search recipe.
            

"""

class SavedQueryExpression:
    """
    Expression for searching with a Saved Query
    """
    def __init__(self, ) -> None: ...
    SavedQuery: Teamcenter.Soa.Client.Model.Strong.ImanQuery
    """Reference to a ImanQuery object that represents a saved query."""
    Entries: list[str]
    """
            List of entries  specified in the saved query for which the values are populated.
            Each entry in the list represents a property of the type for which ImanQuery
            has been created for.
            """
    Values: list[str]
    """
            List of values for the specified entries and the values may have wild card entries
            as well.
            """

class SavedQueryExpressionInput:
    """
    Saved query Expression Input Data Structure
    """
    def __init__(self, ) -> None: ...
    SavedQueryExpression: SavedQueryExpression
    """Search expression for a saved query search."""
    Clientid: str
    """
            A unique string sent by the calling function, so that the output Search Expression
            object could be mapped back to the input.
            """

class SearchBox:
    """
    Search Box data strcture
    """
    def __init__(self, ) -> None: ...
    Xmin: float
    """X Minimum"""
    Ymin: float
    """Y Minimum"""
    Zmin: float
    """Z Minimum"""
    Xmax: float
    """X Maximum"""
    Ymax: float
    """Y Maximum"""
    Zmax: float
    """Z Maximum"""
    Transform: list[float]
    """NOT Implemented as of now. For future use to define rotated 3D boxes."""

class SearchCursor:
    """
    Search Cursor data structure for getting the next set of search results.
    """
    def __init__(self, ) -> None: ...
    Cursor: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchCursor
    """Search Cursor Object Reference"""
    LoadCount: int
    """Count of Next set of objects to be loaded"""

class SearchExpressionInput:
    """
    Input Data Structure to create the Group of Elemental Search Expressions
    """
    def __init__(self, ) -> None: ...
    ProximitySearchExpressions: list[ProximitySearchExpressionInput]
    """
            Input for creating Proximity Search Expressions. Contains reference to a set of ModelElements (that are targets) and the proximity
            distance.
            """
    BoxZoneExpressions: list[BoxZoneExpressionInput]
    """
            input for creating box zone search expressions. Contains the Min and Max coordinated
            of a test Box definition.
            """
    PlaneZoneExpressions: list[PlaneZoneExpressionInput]
    """
            input for creating plane zone search expressions. Contains a point in the plane and
            the normal vector definition.
            """
    SavedQueryExpressions: list[SavedQueryExpressionInput]
    """
            input for creating saved query search expressions. Contains reference to a stored
            saved query object and a coordinated list of entries and values to be used in the
            saved query. Some queries may contain empty list for entries and values (depends
            on the definition of the Saved Query). Wildcards are accepted for values in the Saved
            Query.
            """
    ClosureQueryExpression: list[ClosureQueryExpressionInput]
    """
            Closure Query Expression  that traverses results using a closure rule  Not implemented
            in Tc9.1.0.
            """
    IncludeElements: list[ModelElementInput]
    """
            References to elements to be included into the search results. The server creates
            a Search Expression for this input as well, so that it could be combined with other
            search expressions in a search recipe.
            """
    ExcludeElements: list[ModelElementInput]
    """
            Reference to elements that should be explicitly excluded in the search results. Again
            a search expression is returned for the exclude elements so that it could be combined
            with other search expressions in a search recipe.
            """

class SearchExpressionResponse:
    """
    
            Response data structure that returns the Search Expression objects created for the
            given Search Expression Input data structures.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service Data for any error information. Any malformed input expressions will result
            in an ITK error being returned in the service data. Following errors are possible
            partial errors returned in the ServiceData:
            

278010 - Invalid box zone operator in the box zone expression input
            structure.
            
278015 - Invalid plane zone operator in the plane zone expression
            input structure.
            
278034 - The following selected proximity targets are missing their
            TrueShape information: %1$.
            
278044 - The proximity search distance exceeds the maximum allowed
            limit of "1000000000000000.0" meters
            
278090 - The proximity search node could not be created, because
            the proximity search does not return the same number of target elements and their
            corresponding offsets
            
2780104 - Invalid Composite Search Type value compositeSearchType
            specified in the composite search expression input structure
            

"""
    Expressions: list[ExpressionResponse]
    """
            A list of ExpressionResponse structures that
            has the search expression object embedded. Each ExpressionResponse
            structure consists of a reference to an Mdl0SearchDef object and the corresponding
            clientid (based on the clientid of input data).
            """

class SearchOptions:
    """
    Search Options for a given Search (loadcount and sorting)
    """
    def __init__(self, ) -> None: ...
    SortAttributes: list[str]
    """
            List of persistent properties of the class being searched based on which the results
            will be sorted
            """
    DefaultLoadCount: int
    """
            Number of objects returned by this search. The rest of them could be retrieved by
            calling fetchNextSearchResults. A defaultLoadCount of zero will return all the results found.
            """
    SortOrder: str
    """order in which results are sorted   Ascending or Descending."""

class SearchResponse:
    """
    Response SOA Structure for results
    """
    def __init__(self, ) -> None: ...
    ModelElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """
            The next list of objects returned by the fetchNextSearchResults
            operation.
            """
    Finished: bool
    """
            This flag will be true if there are no more search results for this executeSearch operation.
            """
    ElementsDone: int
    """
            An integer value specifying the number of objects returned so far for this executeSearch operation
            """
    EstimatedElementsLeft: int
    """
            An integer value specifying the estimated number of objects that still are potentially
            results of this search.
            """
    SearchCursor: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchCursor
    """
            Search cursor object that tracks the search results. This object is used to get the
            next set of results for this executeSearch
            operation.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service Data for any error information. Typically this will contain errors about
            any malformed search recipes. E.g. an invalid proximity target (an object without
            geometrical information)
            
            Following are some of the error codes that may be populated as partial errors in
            the ServiceData object:
            

MDL0MODEL_invalid_proximity_target
            (278033)   A spatial proximity search recipe that has no valid proximity targets.
            The target element has no bounding box populated in the database.
            
MDL0MODEL_invalid_trueshape_object
            (278034)  A spatial proximity search recipe that has targets without a valid
            trueshape object. This error is thrown when the tso_flag is set to true in the input
            SearchExpressionSet.
            
MDL0MODEL_invalid_revision_rule_clause
            (278030)  The revision rule used to create a ConfigurationContext object
            has invalid clauses (clauses not valid for CPD application).
            
MDL0MODEL_invalid_set_of_sort_attributes
            (278028)  The Sort options has a sort attribute that is not valid for the
            current search. The sort attribute should be an attribute of the objects found in
            the search. The database query does not support runtime or compound properties as
            sort attributes.
            

"""

class StopSearchResponse:
    """
    Response Data for StopSearch Operation
    """
    def __init__(self, ) -> None: ...
    Finished: bool
    """
            A Boolean flag with true value indicating the successful deletion of the search cursor
            and removal of server memory allocated by the search operation.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data for any error information"""

class Search:
    """
    Interface Search
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateConfigurations(self, ConfigData: list[ConfigurationData]) -> ConfigResponse:
        """    
             This operation creates a configuration context (ConfigurationContext) object
             (or updates a configuration context object). In CPD, the configuration information
             is kept track using a Configuration Context object. This object is not persisted
             in the Database. It is just created and kept alive until the session is active and
             destroyed when the user logs out.
             
             A configuration context keeps track of the Revision Rule (with any attached Effectivity
             Conditions) (and in the future would keep track of variant rule as well) created/used
             by a client session. In Teamcenter 9.1.0, minor revisioning is not supported in CPD.
             When minor revisioning is introduced in Teamcenter 10.1.0, then the configuration
             context will also serve the purpose of allocating a cparam for the corresponding
             Revision Rule used by the client session.
             
             cparam is an object used by the POM revisioning framework to configure the correct
             minor revision of a reviseable object being used.
             
             A configuration context created could be used by the caller during executeSearch or any other operation that requires the revision
             and effectivity configuration settings.
             


Use Cases:

             This operation supports the use case of creating and maintaining configuration context
             objects with different Revision and Effectivity configurations. Also in the future,
             this will be extended to keep track of cparam objects to pick the correct minor revision
             (historical revision) of the object.  The configuration context objects thus created
             are used during execution of a CPD search operation or other operations such getMembers on a partition.
             

Dependencies:

             createOrUpdateConfigurations
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param ConfigData: 
                         Input data structure to create configuration context objects with associated Revision
                         Rule and other configuration conditions.
             
        :return: Returns ConfigResponse data structure.This operation returns runtime configuration
             context objects.
        """
        ...
    def CreateSearchExpressions(self, SearchExpInput: SearchExpressionInput) -> SearchExpressionResponse:
        """    
             This operation creates the elemental search expressions that could be combined using
             logical operators to build up a complex search recipe in CPD application. The createSearchExpressions
             operation could be used to create multiple search expressions at the same time. The
             following types of expressions could be created by this operation
             

Bounding Box Expression (Mdl0SearchBoxZone)
             
Plane Zone Expression (Mdl0SearchPlaneZone)
             
Proximity Expression (Mdl0SearchProximity)
             
Saved Query Expression (Mdl0SearchSavedQuery)
             
Include Content Expression (Mdl0SearchSlctContent)
             
Exclude Content Expression (Mdl0SearchGroup)
             



             These search expressions can be build for various types of Business Object types.
             Information about how to traverse from one type to another type is embedded within
             a search expression input.
             

Use Cases:

             The createSearchExpressions is a required
             operation before an executeSearch or setRecipes call is made. This operation creates
             the runtime Search Definition objects based on the input search expression data structures.
             The intent of this operation is to create all the individual elemental search expressions
             so that they could be combined using logical operators (AND/OR/NOT) to create a complex
             search recipe.
             

Dependencies:

             createSearchExpressions
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param SearchExpInput: 
                         Search Expression Input Structure
             
        :return: SearchExpressionResponse data structure that returns the Search Expression objects
             created for the given Search Expression Input data structures.
        """
        ...
    def ExecuteSearch(self, Recipe: SearchRecipe, Options: SearchOptions) -> SearchResponse:
        """    
             Operation that executes a search based on an input Search Recipe and returns the
             list of Model Elements (Mdl0ModelElement) back to the caller. Search Recipe
             could be a complex expression set that combines multiple simpler search terms (both
             spatial and non spatial) in a logical sequence.
             
             Search is always executed within the scope of an Application Model and all the Model
             Elements returned belong to the given Application Model. executeSearch
             operation uses the configuration information given in the recipe to configure the
             results of a search (Both Revision and Effectivity Configurations).
             
             The results of a search are returned one set at a time based on the defaultLoadCount specified in the SearchOptions.
             The SearchResponse also contains a Search
             Cursor object that the caller could use to fetch the next set of results by invoking
             the fetchNextSearchResults call. Search options
             also gives the caller the ability to sort the results of a search using any (one
             or more) of the attributes of the returned objects.
             

Use Cases:

             This API provides the ability for searching Model Content in a given Application
             Model. Application Model is a construct in AppModel template that defines an abstract
             boundary in which content could be populated. The populated model content is called
             Model Element which again is an abstract object which has some basic attributes such
             as an ID, revision Id, name and description.
             
             CPD has specialized the Application Model to be a Product Design and the Model Element
             to be a Design Component. In this context, the executeSearch
             API provides the ability to Search for Design Components in a Product Design using
             various Search terms (combined together as a Search Recipe).
             
             The Search term could be spatial (searching for objects in a 3d space specified by
             a bounding box or a 3d plane or proximity to another Design Component) or an attribute
             term (Saved Query searching for Design Components with specific attribute values/patterns)
             or a partition term (Searching for membership in specific segments of a Product Design).
             
             The results of the execute search operation could be constrained by the search scope
             which is part of the search recipe and organized by the search options.
             


Dependencies:

             getConfigurableProducts, getEffectivityConditions, fetchNextSearchResults, stopSearch
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Recipe: 
                         Recipe for executing the search
             
        :param Options: 
                         Search Options for a given Search (load count and sorting)
             
        :return: object
        """
        ...
    def FetchNextSearchResults(self, SearchCursor: SearchCursor) -> SearchResponse:
        """    
             This operation gets the next set of Model Elements from a previously executed search
             results. The results returned will be based on the load count specified in the SearchCursor input structure. This API returns
             the same response structure as that of executeSearch.
             

Use Cases:

             This API is used in conjunction with executeSearch
             operation. executeSearch operation is a prerequisite for invoking fetchNextSearchResults. The search cursor returned by the executeSearch is used to call fetchNextSearchResults operation. This operation could be called
             repeatedly by the caller, until all the search results are returned.
             

Dependencies:

             fetchNextSearchResults
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param SearchCursor: 
<ul>
<li type="disc"><font face="courier" height="10">cursor</font>  A runtime object
                         identifier that keeps track of the Search results and the corresponding indexes as
                         of where the caller has consumed the results
                         </li>
<li type="disc"><font face="courier" height="10">loadCount</font>  An integer number
                         that specifies the number of objects to be fetched from the Search result set. If
                         the <font face="courier" height="10">loadCount</font> is zero (or more than the number
                         of objects left in the result set) then all the remaining objects in the result set
                         is returned.
                         </li>
</ul>

        :return: structure
        """
        ...
    def GetRecipes(self, RecipeContainers: list[Teamcenter.Soa.Client.Model.ModelObject]) -> RecipeResponse:
        """    
             This operation retrieves the stored recipe against a set of recipe container objects.
             The persistent objects used to store the search recipe in Teamcenter are objects
             that do not have lifecycle by itself, so they are always associated to objects that
             exhibit the RecipeContainer behavior. In the current CPD application there
             are three objects that exhibit RecipeContainer behavior. They are
             

Mdl0SubsetDefinition:  object to store a search recipe (without
             the results)
             
Ptn0Partition:   A dynamic partition that executes the search
             recipe to find its members
             
Cpd0DesignSubsetInstance:  A realization object that takes
             a subset of a Product Design and instantiates into a Workset.
             


             The retrieved recipe from the recipe container is translated to the data structures
             defined in the Search SOA service and then it is presented back to the caller.
             

Use Cases:

             This operation supports the use case of retrieving a stored search recipe from Teamcenter
             DB against a recipe container object. The retrieved recipe could be reexecuted by
             calling executeSearch operation.
             

Dependencies:

             getRecipes
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param RecipeContainers: 
                         reference to <b>RecipeContainer</b> Objects. The input vector could contain any Teamcenter
                         object that exhibits a <b>RecipeContainer</b> behavior.
             
        :return: data structure
        """
        ...
    def SetRecipes(self, RecipeInputs: list[RecipeData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation saves a search recipe as persistent objects in Teamcenter. The stored
             recipe could be retrieved using getRecipes operation. This is a bulk operation, i.e.
             it can store multiple complex search recipes in a single call.
             
             The persistent objects used to store the search recipe in Teamcenter are objects
             that do not have lifecycle by itself, so they are always associated to objects that
             exhibit the RecipeContainer behavior. In the current CPD application there
             are three objects that exhibit RecipeContainer behavior. They are
             

Mdl0SubsetDefinition  object to store a search recipe (without
             the results)
             
Ptn0Partition   A dynamic partition that executes the search
             recipe to find its members
             
Cpd0DesignSubsetInstance   A realization object that takes
             a subset of a Product Design and instantiates into a Workset.
             


             Note that the recipe is deleted when its container object is deleted.
             

Use Cases:

             The setRecipes operation is used to save
             search recipes against a Recipe Container object. Apart from capturing the logical
             combination of search expressions, the setRecipes
             also stores the current configuration conditions against the RecipeContainer
             object (Revision Rule and Effectivity Rule), except in the case of Ptn0Partition
             object. Ptn0Partition object does not provide a persistence mechanism for
             the configuration conditions and it uses the configuration set in the current CPD
             application.
             
             The search recipes are stored as ApprSearchCriteria objects in Teamcenter
             and ApprSearchCriteria object hierarchy has a subclass to store each Search
             expression separately.
             


Dependencies:

             convertEffectivityExpressions, createOrUpdateConfigurations, createSearchExpressions
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param RecipeInputs: 
                         Recipe Data that should be set for specific Container Objects
             
        :return: data structure.
        """
        ...
    def StopSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchCursor) -> StopSearchResponse:
        """    
             This operation stops further loading of objects from a previously executed search
             and clears all the memory allocated for the search operation. It deletes the search
             cursor and the list of Model Elements that are kept track by the Search cursor from
             the Server Memory.
             
             The stopSearch does not unload any previously
             loaded Model Elements. Also there is no locking or unlocking performed by the stopSearch operation.
             


Use Cases:

             When a search is executed in CPD and the search returns a large set of objects. The
             server process keeps the results of a search using a search cursor object. At each
             fetchNextSearchResults operation, the results
             are further filtered and returned in batches specified by the load count. However
             if the caller is not interested in consuming the search results further, then a stopSearch could be called to release all the resources
             allocated for that search operation. This includes dropping the runtime search cursor
             object and the list of Model Elements kept track by the cursor.
             

Dependencies:

             executeSearch, fetchNextSearchResults
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param SearchCursor: 
                         Search Cursor for stopping the search
             
        :return: data structure.
        """
        ...

