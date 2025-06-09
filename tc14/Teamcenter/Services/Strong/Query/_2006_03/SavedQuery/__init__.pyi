import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DescribeSavedQueriesResponse:
    """
    Holds the field data for each saved query.
    """
    def __init__(self, ) -> None: ...
    FieldLists: list[SavedQueryFieldListObject]
    """A list of fields for each input query."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The standard ServiceData."""

class ExecuteSavedQueryResponse:
    """
    
Holds the response for ExecuteSavedQuery. The number of objects found is the
total
number found and may be greater than the number return in the vector of
objects
if a limit was specified on executing the query.
    """
    def __init__(self, ) -> None: ...
    NFound: int
    """The number of objects found by the query."""
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The objects returned."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The standard service data which includes the returned objects."""

class GetSavedQueriesResponse:
    """
    Holds the response for GetSavedQueries
    """
    def __init__(self, ) -> None: ...
    Queries: list[SavedQueryObject]
    """
            A list of SavedQueryObjects each of which contains the query, query name, and query
            description for a saved query.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData"""

class SavedQueryFieldListObject:
    """
    A  list of saved query fields for a saved query.
    """
    def __init__(self, ) -> None: ...
    Fields: list[SavedQueryFieldObject]
    """Holds one entry per clause"""

class SavedQueryFieldObject:
    """
    The data for a field of a saved query.
    """
    def __init__(self, ) -> None: ...
    AttributeName: str
    """The attribute name for the clause."""
    EntryName: str
    """User entry name for clause."""
    LogicalOperation: str
    """Logical operator for clause"""
    MathOperation: str
    """Math operator for clause"""
    Value: str
    """Default value for clause"""
    Lov: Teamcenter.Soa.Client.Model.ModelObject
    """LOV for the clause"""
    AttributeType: int
    """Attribute type for clause"""

class SavedQueryObject:
    """
    The data for each saved query found.
    """
    def __init__(self, ) -> None: ...
    Query: Teamcenter.Soa.Client.Model.Strong.ImanQuery
    """The saved query."""
    Name: str
    """The name of the saved query."""
    Description: str
    """The description of the saved query."""

class SavedQuery:
    """
    Interface SavedQuery
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetSavedQueries(self) -> GetSavedQueriesResponse:
        """    
             Gets a list of all saved queries with query, query name, and query description information.
             

Use Cases:

             The user can open the search view and can select a query from the Change Search dialog
             which shows all available saved queries.
             
             The user can open the Query Builder to load all the saved queries, and then do the
             modification, deletion, and creation.
             


Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :return: 
        """
        ...
    def DescribeSavedQueries(self, Queries: list[Teamcenter.Soa.Client.Model.Strong.ImanQuery]) -> DescribeSavedQueriesResponse:
        """    
             Returns the description of each of the input saved queries.The description for each
             query includes all the clause information (the attribute name, entry name, operation
             for each clause, the math operation for each clause, the ListOfValues for related
             clause if it has, and the attribute type).
             

Use Cases:

             User can get the description for queries by this service and then can show the details
             in search view so that user can execute the query.
             

             User can get the description for queries by this service and then show the details
             in query builder so that user can see the definition for the query or update the
             query.
             

             User can get the description for queries by this service and then use it to get the
             saved searches.
             

             User can get the description for queries by this service and then use it to get the
             search history.
             


Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param Queries: 
                         A list of ImanQuery objects for which the description is requested.
             
        :return: object attached to the partial
             error.
        """
        ...
    def ExecuteSavedQuery(self, Query: Teamcenter.Soa.Client.Model.Strong.ImanQuery, Entries: list[str], Values: list[str], Limit: int) -> ExecuteSavedQueryResponse:
        """    
             Executes a single saved query by input query with entries and values. If the returned
             result number is larger than the input limit(when limit > 0), then only the input
             limit result number objects will be returned; otherwise all results will be returned.
             The number of objects found is also returned; it may be larger than the limit number.
             

Use Cases:

             The user opens the search view, selects a query from the system defined queries or
             user defined queries, then fills in some input criteria, clicks the Execute button
             to run this query. The result objects will be returned in the search result view.
             If the total result objects number is larger than the limit number which is used
             to prevent loading too many objects in memory considering the performance issue(when
             limit > 0), then only return the limit number result objects for the query. The total
             search result objects number is displayed in the search result view.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param Query: 
                         The saved query to be executed which includes the query tag for the query.
             
        :param Entries: 
                         The user entries.
             
        :param Values: 
                         Values for the user entries
             
        :param Limit: 
                         The maximum number of objects to be returned. If limit &lt;=0, then it means no limit
                         for the results.
             
        :return: The ExecuteSavedQueryResponse object contains the number objects found, the objects
             found, and serviceData.
        """
        ...

