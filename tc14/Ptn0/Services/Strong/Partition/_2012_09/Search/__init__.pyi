import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ConfigurationDetail:
    """
    Configuration mapping for various configuration object types.
    """
    def __init__(self, ) -> None: ...
    ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            Configuration Context having configuration data (RevsionRule and EffectivityRule).
            

"""
    ConfigurationFor: str
    """Input ConfigurationFor structure."""

class ExpressionResponse:
    """
    Expression Response data structure
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
            object could be mapped back to the input.
            """

class PartitionGroup:
    """
    
            Data structure that returns the Partition groups for the members returned by the
            Search
            
    """
    def __init__(self, ) -> None: ...
    IsRootPartition: bool
    """
            Flag to indicate whether the Partition in the structure is a root partition (Partition
            that does not have any parent partitions) or not.
            """
    Members: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """Defines the vector of members (model elements) that have membership in this Partition."""
    Partition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """
            Reference to the Partition object (Ptn0Partition) represented in this PartitionGroup.
            """
    ChildPartitionGroups: list[PartitionGroup]
    """
            Child partition groups (vector of PartitionGroup
            objects) for this Partition object along with their grouped members.
            """

class PartitionQueryExpression:
    """
    search expression structure for proximity search
    """
    def __init__(self, ) -> None: ...
    PartitionObjectExpression: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchDef
    """Search Criteria specifying the specific Partitions"""
    PartitionItemRevExpression: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchDef
    """
            Search Criteria specifying partition item revisions whose partition instances should
            be included
            """
    IncludeChildPartitions: bool
    """Flag to include child partitions in hierarchical partition structure"""
    Clientid: str
    """Client ID to track response with request"""

class PartitionScope:
    """
    
            Defines Partition scope for the search results arrangement. PartitionScope has a partition scheme name by which the results
            should be organized by and a flag that indicates whether immediate partitions should
            be considered or to consider the whole partition breakdown structure while returning
            back the partition groups
            
    """
    def __init__(self, ) -> None: ...
    Scheme: Teamcenter.Soa.Client.Model.Strong.Ptn0PartitionScheme
    """Input partition scheme within which the partition results are required."""
    IsOnlyImmediateGroupsReqd: bool
    """
            Flag to indicate whether only Immediate hierarchy of Partition to members are required.
            If true, all the Ptn0Partition object hierarchy till the root are returned,
            otherwise no Ptn0Partition object hierarchy is returned.
            """

class UnassignedQueryExpression:
    """
    
            Search for unassigned model elements - Elements not assigned to a partition of given
            scheme names.
            
    """
    def __init__(self, ) -> None: ...
    PartitionSchemeNames: list[str]
    """
            list of Ptn0PartitionScheme names in which the unassigned search should be
            performed.
            """
    Clientid: str
    """
            A unique string sent by the calling function, so that the output Search Expression
            object could be mapped back to the input.
            """

class PartitionSearchExpressionInput:
    """
    Input for creating Partition Search Expression Objects
    """
    def __init__(self, ) -> None: ...
    PartitionQueryExpressions: list[PartitionQueryExpression]
    """
PartitionQueryExpression structures that
            define search expressions to search for Partition objects in an Application Model.
            """
    UnassignedQueryExpression: UnassignedQueryExpression
    """
            data structure that defines the list of partition schemes where it is required to
            find the unassigned model elements.
            """

class SearchCursor:
    """
    Data structure that keeps track of the list of objects returned by a search.
    """
    def __init__(self, ) -> None: ...
    Cursor: Teamcenter.Soa.Client.Model.ModelObject
    """
            A runtime object identifier that keeps track of the Search results and the corresponding
            indexes as of where the caller has consumed the results
            """
    LoadCount: int
    """
            An integer number that specifies the number of objects to be fetched from the Search
            result set. If the loadCount is zero (or
            more than the number of objects left in the result set) then all the remaining objects
            in the result set is returned.
            """

class SearchExpression:
    """
    
            Group of search expressions (or Mdl0SearchDef objects) used in the search
            recipe.
            
    """
    def __init__(self, ) -> None: ...
    SearchExpressions: list[Teamcenter.Soa.Client.Model.Strong.Mdl0SearchDef]
    """Reference to the list of Search Expression Objects."""
    DoTrushapeRefinement: bool
    """True shape object flag (true or false)."""

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
            
PTN0PARTITION_search_has_no_valid_criteria (280012)
            When the Partition Search input has neither partition criteria nor an Partition
            Item Revision criteria specified, then this error is thrown.
            
"""
    Expressions: list[ExpressionResponse]
    """
            A list of ExpressionResponse structures that
            has the search expression object embedded. Each ExpressionResponse
            structure consists of a reference to an Mdl0SearchDef object and the corresponding
            clientid (based on the clientid of input data).
            """

class SearchExpressionSet:
    """
    Building block to build complex search expressions.
    """
    def __init__(self, ) -> None: ...
    SearchOperator: str
    """
            Boolean operator to combine multiple search expressions: And,
            Or or Not.
            """
    SearchExpression: SearchExpression
    """
            Search Expressions to be executed. In case of more than one a OR operator is assumed
            between these expressions.
            """
    SearchExpressionSets: list[SearchExpressionSet]
    """A list of search expressions combined by the search operator."""

class SearchOptions:
    """
    Search options for the given search.
    """
    def __init__(self, ) -> None: ...
    SortAttributes: list[str]
    """
            List of persistent attributes of the class being searched based on which the results
            will be sorted
            """
    DefaultLoadCount: int
    """
            Number of objects returned by this search. The rest of them could be retrieved by
            calling fetchNextSearchResults. A defaultLoadCount of zero will return all the results found.
            """
    SortOrder: str
    """Order in which results are sorted Ascending or Descending."""

class SearchScope:
    """
    
            Defines the scope of a given search  Application model, type of objects to be returned
            and optionally the recipe container.
            
    """
    def __init__(self, ) -> None: ...
    Model: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """Application Model that scopes this search"""
    SearchType: list[str]
    """Type of Search  can restrict object types returned in the final search result"""
    RecipeContainer: Teamcenter.Soa.Client.Model.ModelObject
    """
            Subset or Subset Instance or Partition for which the search needs to be executed.
            When the recipe container is specified, there is no need to specify the recipe (search
            expression set) separately.
            """

class SearchRecipe:
    """
    Recipe for performing a Search
    """
    def __init__(self, ) -> None: ...
    Scope: SearchScope
    """Scope of Search: Model, search types"""
    ConfigDetails: list[ConfigurationDetail]
    """A list of configuration information: Revision Rule, Effectivity Rule."""
    SearchExpression: SearchExpressionSet
    """Expression set to be evaluated : search criteria"""

class SearchResponse:
    """
    Response Data Structure for search results.
    """
    def __init__(self, ) -> None: ...
    ModelElements: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of objects returned by the execute search operation."""
    ElementsDone: int
    """
            An integer value specifying the number of objects returned so far for this execute
            search operation
            """
    EstimatedElementsLeft: int
    """
            An integer value specifying the estimated number of objects that still are potentially
            results of this search.
            """
    IsFinished: bool
    """
            This flag will be true if there are no more search results for this execute search
            operation.
            """
    SearchCursor: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchCursor
    """
            Search cursor object that tracks the search results. This object is used to get the
            next set of results for this executeSearch
            operation.
            """
    PartitionGrps: list[PartitionGroup]
    """
            Partition for the members that are returned in the search results. Partition Groups
            may contain complete partition breakdown or just the immediate partitions based on
            the input PartitionScope specification.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service Data for any error information. Typically this will contain errors about
            any malformed search recipes. E.g. an invalid proximity target (an object without
            geometrical information)
            
            Following are some of the error codes that may be populated as partial errors in
            the ServiceData object:
            
MDL0MODEL_invalid_proximity_target (278033)
            A spatial proximity search recipe that has no valid proximity targets. The target
            element has no bounding box populated in the database.
            
MDL0MODEL_invalid_trueshape_object (278034)
            A spatial proximity search recipe that has targets without a valid trueshape object.
            This error is thrown when the tso_flag is set to true in the input SearchExpressionSet.
            
MDL0MODEL_invalid_revision_rule_clause (278030)
            The revision rule used to create a ConfigurationContext object has invalid clauses
            (clauses not valid for CPD application).
            
MDL0MODEL_invalid_set_of_sort_attributes (278028)
             The Sort options has a sort attribute that is not valid for the current search.
            The sort attribute should be an attribute of the objects found in the search. The
            database query does not support runtime or compound properties as sort attributes.
            
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
    """Service Data for any error information  e.g. invalid search cursor object."""

class Search:
    """
    Interface Search
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreatePartitionExpressions(self, PartitionSearchexpInput: PartitionSearchExpressionInput) -> SearchExpressionResponse:
        """    
             This operation creates Partition Search expressions (Ptn0SearchPartition)
             that would be used in a Search Recipe (to perform executeSearch or setRecipes call).
             Since Partition is an optional BMIDE template on top of AppModel template, creating
             Partition Search expressions are provided as part of the Partition Search service.
             
             createPartitionExpressions is a bulk operation that takes multiple Partition search
             expression input data and creates SearchExpressionResponse that is similar to its
             counterpart (createSearchExpressions) in the AppModel Search service.
             


Use Cases:

             There are 2 use cases supported by this operation to create the elemental search
             expressions to find members of Partitions.
             
1.Create Partition Search Expressions   A Partition Search expression is used
             to first find the partition that are specified by the Search recipe and then searching
             for the members of partitions that are of interest.
             
2. Create Unpartitioned Elements Search Expression   Search expression used
             to find unpartitioned elements on a given partition scheme or on all partition schemes
             in that Product Design.
             


Dependencies:

             createPartitionExpressions
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param PartitionSearchexpInput: 
                         Input for the runtime partition expressions
             
        :return: :Response data structure
             that returns the Search Expression objects created for the given Search Expression
             Input data structures.
        """
        ...
    def ExecuteSearch(self, Options: SearchOptions, Scope: PartitionScope, Recipe: SearchRecipe) -> SearchResponse:
        """    
             Operation that executes a search based on an input Search Recipe and returns the
             list of Model Elements (Mdl0ModelElement) back to the caller. Search Recipe
             could be a complex expression set that combines multiple simpler search terms (both
             spatial and non spatial) in a logical sequence.
             
             Search is always executed within the scope of an Application Model and all the Model
             Elements returned belong to the given Application Model. executeSearch
             operation uses the configuration information given in the recipe to configure the
             results of a search (Both Revision and Effectivity Configurations).
             
             The results of a search are returned one set at a time based on the defaultLoadCount specified in the SearchOptions. The SearchResponse also contains a Search Cursor object that the caller
             could use to fetch the next set of results by invoking the fetchNextSearchResults
             call. Search options also gives the caller the ability to sort the results of a search
             using any (one or more) of the attributes proeprties of the returned objects.
             
             The PartitionScope specifies the grouping
             by which the search results should be grouped or organized. It contains a partition
             scheme (Ptn0PartitionScheme) name and a flag that specifies whether the immediate
             partitions are the only ones that need to be considered. The SearchResponse contains the results grouped based on Partitions
             in which the search results have membership, in the given partition scheme.
             


Use Cases:

             This API provides the ability for searching Model Content in a given Application
             Model. Application Model is a construct in AppModel template that defines an abstract
             boundary in which content could be populated. The populated model content is called
             Model Element which again is an abstract object which has some basic properties such
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
             which is part of the search recipe and organized by the search options. Also the
             results of a search are organized by Partitions based on the input Partition Scheme.
             


Dependencies:

             createPartitionExpressions, fetchNextSearchResults, stopSearch
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Options: 
                         defines additional search options.
             
        :param Scope: 
                         Defines Partition scope for the search results arrangement.
             
        :param Recipe: 
                         defines the search recipe
             
        :return: defines the set of objects loaded after search and cursor to load on demand.
        """
        ...
    def FetchNextSearchResults(self, SearchCursor: SearchCursor, PartitionScope: PartitionScope) -> SearchResponse:
        """    
             This operation gets the next set of Model Elements from a previously executed search
             results. The results returned will be based on the load count specified in the SearchCursor input structure. This API returns
             the same response structure as that of executeSearch.
             
             The results obtained by fetchNextSearchResults
             are again arranged by Partition based on the PartitionScope specified.
             


Use Cases:

             This API is used in conjunction with executeSearch
             operation. executeSearch operation is a prerequisite
             for invoking fetchNextSearchResults. The
             search cursor returned by the executeSearch is used to call fetchNextSearchResults operation. This operation could be called
             repeatedly by the caller, until all the search results are returned. The fetchNextSearchResults in Partition Search Service is introduced
             mainly to organize the search results by Partition over and above of the functionality
             provided in the AppModel Search Service.
             

Dependencies:

             fetchNextSearchResults
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param SearchCursor: 
                         Data structure that keeps track of the list of objects returned by a search.
             
        :param PartitionScope: 
                         Defines Partition scope for the search results arrangement. <i>PartitionScope</i>
                         has a partition scheme name by which the results should be organized by and a flag
                         that indicates whether immediate partitions should be considered or to consider the
                         whole <i>partition breakdown</i> structure while returning back the partition groups
             
        :return: Returns the Search Response structure
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

             fetchNextSearchResults
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param SearchCursor: 
                         A runtime object identifier that keeps track of the Search results and the corresponding
                         indexes as of where the caller has consumed the results. Invoking stopSearch on this
                         object deletes this object.
             
        :return: Returns stopSearchResponse data structure
        """
        ...

