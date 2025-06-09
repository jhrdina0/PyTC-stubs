import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExecuteSavedQueriesResponse:
    """
    Holds the response for executeSavedQueries.
    """
    def __init__(self, ) -> None: ...
    ArrayOfResults: list[SavedQueryResults]
    """A set of SavedQueryResults data structures"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""

class RetrieveSearchCriteriaResponse:
    """
    
Holds a vector of SavedSearchCriteriaInfo and a ServiceData.   To be used as a
response
for operation "retrieveSearchCriteria"
    """
    def __init__(self, ) -> None: ...
    Output: list[SaveSearchCriteriaInfo]
    """A vector of SavedSearchCriteriaInfo"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData"""

class SavedQueryInput:
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
    LimitListCount: int
    """The size of the limitList."""
    MaxNumToReturn: int
    """A specified maximum number of matches to be returned, 0 means no limit."""
    ResultsType: int
    """
            The type of results expected from this operation: 0 (top-level objects only), 1 (top-level
            objects plus children: Hierarchical/Indented results), 2 (default value as specified
            on the query object).
            """
    MaxNumToInflate: int
    """
            The number of objects in the returned result that must  include properties: (-1)(all),
            n (any positive integer less than or equal to the maxNumToReturn).
            """

class SavedQueryResults:
    """
    
Results of Saved Query execution, number of objects returned and hierarchy
information
in a relation map for Hierarchical/Indented execution.  Hierarchical/Indented
execution
example1: If the query is: Find all Items where the Item Revisions have a
Specification
Dataset with name = "xyz1", then results will be comprised of subsets, each
containing:
an Item, a qualifying Item Revision and a qualifying Dataset. For each result
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
    NumOfObjects: int
    """The number of objects returned."""
    ObjectsRelMap: list[int]
    """
            Used only for Hierarchical/Indented execution. An integer array containing the hierarchy
            level information which maps 1-to-1 to the the returned list of objects which is
            ordered as subsets. The integer code in the relation map indicates if the corresponding
            object in the results set is a root object (=0), or a first-level child (=1), or
            a second-level child (=2) and so on. In the case of child levels, the level information
            is with respect to the immediately preceding root object entry in the mapping. The
            order of returns is relevant.
            """
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The objects returned from the search."""

class SaveSearchCriteriaInfo:
    """
    
Holds the criteria information to be saved or retrieved for a  saved search, a
collection
of which is known as "My Saved Searches".  A saved search stores the user's
entries
for a particular saved query  execution so that it can be recalled and rerun in
the
future.
    """
    def __init__(self, ) -> None: ...
    SearchName: str
    """A unique name for the saved search"""
    QueryName: str
    """The name of the saved query associated with the saved search"""
    Keys: list[str]
    """Unique keys associated with the "values" below - each key represents a criteria field"""
    Values: list[str]
    """The values associated with the "keys" above"""
    ResultsType: str
    """The results type associated with the saved search"""
    VirtualFolderPath: str
    """The virtual folder the saved search belongs to"""

class SavedQuery:
    """
    Interface SavedQuery
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteSavedQueries(self, Input: list[SavedQueryInput]) -> ExecuteSavedQueriesResponse:
        """    
             Executes a set of saved queries of following type:
             


QRY_RUN_BY_TC ( 0 )
             
QRY_RUN_BY_USER_EXIT ( 8 )
             
QRY_RUN_BY_KEYWORD_SEARCH ( 24 )
             
QRY_RUN_BY_EINT_EXIT ( 32 )
             
QRY_RUN_BY_TC_PLUS_PROCESS ( 56 )
             



             The saved queries can be executed to yield results in 2 modes:
             


Flat mode: In this traditional execution mode, only the first-level
             objects (corresponding to         the queried
             class) satisfying the query  are returned
             
Hierarchical/Indented mode: This mode is only applicable for saved
             queries that allow         Hierarchical/Indented
             results. In this execution mode, the first-level objects as well as any         sub-level
             objects satisfying the query criteria are returned. The hierarchy level information
             is         also returned so that result subsets
             can be  re-constructed using the resulting objects.
             


                     This service will return the matched
             object UIDs.   After fetching UIDs, client needs to call         DataManagementService.loadObjects
             operation to load objects by pages.  See the         QueryInput
             and QueryResults data structures for usage details.
             

Use Cases:

             Execute a set of saved queries of following types: QRY_RUN_BY_TC,  QRY_RUN_BY_KEYWORD_SEARCH
             and QRY_RUN_BY_TC_PLUS_PROCESS etc.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param Input: 
                         A set of QueryInput data structures.
             
        :return: 
        """
        ...
    def RetrieveSearchCriteria(self, SearchNames: list[str]) -> RetrieveSearchCriteriaResponse:
        """    
             Retrieve the corresponding search criteria for the given saved search names.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param SearchNames: 
                         A set of saved search names for which their  corresponding search criteria are to
                         be retrieved.
             
        :return: RetrieveSearchCriteriaResponse contains (1) a set of SaveSearchCriteriaInfo data
             structures and (2) a ServiceData. Partial errors are stored and referenced by search
             names.
        """
        ...
    def SaveSearchCriteria(self, SearchCriteria: list[SaveSearchCriteriaInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Save a set of search criteria.  Each search criteria pertains to   a saved search,
             a collection of which is known as "My Saved Searches".
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param SearchCriteria: 
                         A set of SaveSearchCriteriaInfo to be saved.
             
        :return: ServiceData     Partial errors are stored and referenced by search names.
        """
        ...

