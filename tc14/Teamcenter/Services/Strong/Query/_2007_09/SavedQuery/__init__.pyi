import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class QueryInput:
    """
    
The information about each Saved Query to be processed is provided  by way of
the
SavedQueryInput data structure.
    """
    def __init__(self, ) -> None: ...
    Query: Teamcenter.Soa.Client.Model.Strong.ImanQuery
    """The saved query object to be executed."""
    Entries: list[str]
    """Names of search criteria relevant to the query object."""
    Values: list[str]
    """Values for the criteria."""
    LimitList: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of objects (optional) against which the search is conducted, if the list is
            empty, search will be conducted against the database.
            """
    MaxNumToReturn: int
    """A specified maximum number of matches to be returned, 0 means no limit."""
    ResultsType: int
    """
            The type of results expected from this operation: 0 (top-level objects only), 1 (top-level
            objects plus children: Hierarchical/Indented results), 2 (default value as specified
            on the query object).
            """

class QueryResults:
    """
    
Results of saved query  execution, including hierarchy information in a relation
map for Hierarchical/Indented execution.  Hierarchical/Indented execution
example1:
If the query is: Find all Items where the Item Revisions have a Specification
Dataset
with name = "xyz1", then results will be comprised of subsets, each containing:
an
Item, a qualifying Item Revision and a qualifying Dataset. For each result
subset,
the corresponding entries in the relation map would be 0 (for root Item), 1 (for
first-level Item Revision), 2 (for second-level Dataset).
Hierarchical/Indented
execution example2: If the query is: Find all Item Revisions that have a
Specification
Dataset with name = "xyz1" AND Form of type Item Revision Master with
user_data_1
= "xyz2", then the results will comprise of subsets, each containing: an Item
Revision,
a qualifying Dataset, a qualifying Form and a qualifying Item Revision Master.
For
each result subset, the corresponding entries in the relation map would be 0
(for
root Item Revision), 1 (for first-level Dataset), 1 (for first-level Form) and 2
(for second-level Item Revision Master).
    """
    def __init__(self, ) -> None: ...
    ObjectsRelMap: list[int]
    """
            Used only for Hierarchical/Indented execution. An integer array containing the hierarchy
            level information which maps 1-to-1 to the returned list of objects which is ordered
            as subsets. The integer code in the relation map indicates if the corresponding object
            in the results set is a root object (=0), or a first-level child (=1), or a second-level
            child (=2) and so on. In the case of child levels, the level information is with
            respect to the immediately preceding root object entry in the mapping. The order
            of returns is relevant.
            """
    ObjectUIDS: list[str]
    """The object UIDs returned from the search."""

class SavedQueriesResponse:
    """
    Contains a list of business objects found as well as the service data returned.
    """
    def __init__(self, ) -> None: ...
    ArrayOfResults: list[QueryResults]
    """A set of QueryResults data structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class SavedQuery:
    """
    Interface SavedQuery
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteSavedQueries(self, Input: list[QueryInput]) -> SavedQueriesResponse:
        """    
             Executes a set of saved queries of following types: QRY_RUN_BY_TC ( 0 ), QRY_RUN_BY_KEYWORD_SEARCH
             ( 24 ).     The saved queries can be executed to yield results in 2 modes:  (1) Flat
             mode: In this traditional execution mode, only the first-level objects (corresponding
             to the queried class) satisfying the query are returned (2) Hierarchical/Indented
             mode: This mode is only applicable for saved queries that allow Hierarchical/Indented
             results. In this execution mode, the first-level objects as well as any sub-level
             objects satisfying the query criteria are returned. The hierarchy level information
             is also returned so that result subsets can be reconstructed using the resulting
             objects.    This service will retun the matched object UIDs. After fetching UIDs,
             client need to call DataManagementService.loadObjects operation to load objects by
             pages.    See the QueryInput and QueryResults data structures for usage details.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param Input: 
                         A set of QueryInput data structures.
             
        :return: Contains (1) a set of QueryResults data structures and (2) a ServiceData. Partial
             errors are stored and referenced by input vector indexes.
        """
        ...

