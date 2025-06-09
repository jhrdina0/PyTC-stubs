import System
import Teamcenter.Services.Strong.Query._2006_03.SavedQuery
import Teamcenter.Services.Strong.Query._2007_01.SavedQuery
import Teamcenter.Services.Strong.Query._2007_06.Finder
import Teamcenter.Services.Strong.Query._2007_06.SavedQuery
import Teamcenter.Services.Strong.Query._2007_09.SavedQuery
import Teamcenter.Services.Strong.Query._2008_06.SavedQuery
import Teamcenter.Services.Strong.Query._2010_04.SavedQuery
import Teamcenter.Services.Strong.Query._2010_09.SavedQuery
import Teamcenter.Services.Strong.Query._2012_10.Finder
import Teamcenter.Services.Strong.Query._2013_05.SavedQuery
import Teamcenter.Services.Strong.Query._2014_11.Finder
import Teamcenter.Services.Strong.Query._2018_11.SavedQuery
import Teamcenter.Services.Strong.Query._2019_06.SavedQuery
import Teamcenter.Services.Strong.Query._2020_04.SavedQuery
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FinderRestBindingStub(FinderService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def FindWorkspaceObjects(self, FindList: list[Teamcenter.Services.Strong.Query._2007_06.Finder.WSOFindSet]) -> Teamcenter.Services.Strong.Query._2007_06.Finder.FindWorkspaceObjectsResponse: ...
    @typing.overload
    def PerformSearch(self, SearchInput: Teamcenter.Services.Strong.Query._2012_10.Finder.SearchInput) -> Teamcenter.Services.Strong.Query._2012_10.Finder.SearchResponse: ...
    @typing.overload
    def PerformSearch(self, SearchInput: Teamcenter.Services.Strong.Query._2014_11.Finder.SearchInput2) -> Teamcenter.Services.Strong.Query._2014_11.Finder.SearchResponse2: ...
    def GroupObjectsByProperties(self, ObjectPropertyGroupInputList: list[Teamcenter.Services.Strong.Query._2014_11.Finder.ObjectPropertyGroupInput]) -> Teamcenter.Services.Strong.Query._2014_11.Finder.ObjectsGroupedByPropertyResponse: ...

class FinderService:
    """
    
            The Finder service provides operations to find objects by given type
name, attribute
            names and values or a set of criteria against workspace objects.

Library Reference:

TcSoaQueryStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> FinderService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def FindWorkspaceObjects(self, FindList: list[Teamcenter.Services.Strong.Query._2007_06.Finder.WSOFindSet]) -> Teamcenter.Services.Strong.Query._2007_06.Finder.FindWorkspaceObjectsResponse:
        """    
             Query the database for WorkspaceObjects. A collection of WSOFindSets are used
             to do the queries. For each WSOFindSet , a FindWorkspaceObjectsOutput will be generated
             if any WorkspaceObjects are found that meet all the criteria.  Each FindWorkspaceObjectsOutput
             will contain the tags of the WorkspaceObjects that meet all the criteria and
             the index of the WSOFindSet in the findList that generated the output.  If an error
             is encountered, then no FindWorkspaceObjectsOutput will be generated for that WSOFindSet
             (no partial data returned) and the index for the WSOFindSet in the findList will
             be the client ID in the partial error.  If no WSOFindSet generates any output, a
             null outputList is returned.
             

Use Cases:

             Find workspace object using basic attributes such as object type, object name, owner,
             group, created before, created after etc.
             

Teamcenter Component:

             Business Intelligence - Capability to create and manage report definitions and generate
             reports
             
        :param FindList: 
                         A list of WSOFindSet used to find workspace objects.
             
        :return: Contains a list of FindWorkspaceObjectsOutput structures (which contain the found
             workspace objects). Any found workspace objects will be sent back in the standard
             ServiceData list of plain objects. Any failure will be returned as partial errors
             in ServiceData with index for the WSOFindSet in the findList.
        """
        ...
    @typing.overload
    def PerformSearch(self, SearchInput: Teamcenter.Services.Strong.Query._2012_10.Finder.SearchInput) -> Teamcenter.Services.Strong.Query._2012_10.Finder.SearchResponse: ...
    @typing.overload
    def PerformSearch(self, SearchInput: Teamcenter.Services.Strong.Query._2014_11.Finder.SearchInput2) -> Teamcenter.Services.Strong.Query._2014_11.Finder.SearchResponse2: ...
    def GroupObjectsByProperties(self, ObjectPropertyGroupInputList: list[Teamcenter.Services.Strong.Query._2014_11.Finder.ObjectPropertyGroupInput]) -> Teamcenter.Services.Strong.Query._2014_11.Finder.ObjectsGroupedByPropertyResponse:
        """    
             This operation classifies business objects into groups. In the list of ObjectPropertyGroupInput
             objects, each object containing an internal property name, list of PropertyGroupingValue
             objects identifying groups and a list of business objects to be classified into the
             groups. Each PropertyGroupingValue object contains a start and an end value. The
             end value is used for range values if populated. Unclassified business objects are
             retuned back in a list.
             

Use Cases:

             In Active Workspace client, a user navigates to a new filter category on the filter
             panel. The cells in the visible view for the search results (e.g. list view or table
             view) need to be colored to match the colors on the bar chart for the objects in
             the search results. The client invokes this operation, which identifies the property
             group (or bar on the chart) the objects belong to. The client can then color the
             cells corresponding to the objects appropriately based on the grouping information
             that is returned.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param ObjectPropertyGroupInputList: 
                         A list containing ObjectPropertyGroupInput objects that represents property name
                         and property value information to group a list of input business objects
             
        :return: A structure containing a vector of ObjectPropertyGrouping object and  service data.
        """
        ...

class SavedQueryRestBindingStub(SavedQueryService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetSavedQueries(self) -> Teamcenter.Services.Strong.Query._2006_03.SavedQuery.GetSavedQueriesResponse: ...
    def DescribeSavedQueries(self, Queries: list[Teamcenter.Soa.Client.Model.Strong.ImanQuery]) -> Teamcenter.Services.Strong.Query._2006_03.SavedQuery.DescribeSavedQueriesResponse: ...
    def ExecuteSavedQuery(self, Query: Teamcenter.Soa.Client.Model.Strong.ImanQuery, Entries: list[str], Values: list[str], Limit: int) -> Teamcenter.Services.Strong.Query._2006_03.SavedQuery.ExecuteSavedQueryResponse: ...
    def DeleteQueryCriterias(self, QueryCriteriaNames: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ReorderSavedQueryCriterias(self, QueryCriteriaNames: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RetrieveQueryCriterias(self, QueryCriteriaNames: list[str]) -> Teamcenter.Services.Strong.Query._2007_01.SavedQuery.RetrieveQueryCriteriaResponse: ...
    def SaveQueryCriterias(self, QueryCriterias: list[Teamcenter.Services.Strong.Query._2007_01.SavedQuery.SaveQueryCriteriaInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def ExecuteSavedQueries(self, Input: list[Teamcenter.Services.Strong.Query._2007_06.SavedQuery.SavedQueryInput]) -> Teamcenter.Services.Strong.Query._2007_06.SavedQuery.ExecuteSavedQueriesResponse: ...
    @typing.overload
    def ExecuteSavedQueries(self, Input: list[Teamcenter.Services.Strong.Query._2007_09.SavedQuery.QueryInput]) -> Teamcenter.Services.Strong.Query._2007_09.SavedQuery.SavedQueriesResponse: ...
    @typing.overload
    def ExecuteSavedQueries(self, Input: list[Teamcenter.Services.Strong.Query._2008_06.SavedQuery.QueryInput]) -> Teamcenter.Services.Strong.Query._2007_09.SavedQuery.SavedQueriesResponse: ...
    def RetrieveSearchCriteria(self, SearchNames: list[str]) -> Teamcenter.Services.Strong.Query._2007_06.SavedQuery.RetrieveSearchCriteriaResponse: ...
    def SaveSearchCriteria(self, SearchCriteria: list[Teamcenter.Services.Strong.Query._2007_06.SavedQuery.SaveSearchCriteriaInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def FindSavedQueries(self, InputCriteria: list[Teamcenter.Services.Strong.Query._2010_04.SavedQuery.FindSavedQueriesCriteriaInput]) -> Teamcenter.Services.Strong.Query._2010_04.SavedQuery.FindSavedQueriesResponse: ...
    def ExecuteBusinessObjectQueries(self, Inputs: list[Teamcenter.Services.Strong.Query._2010_09.SavedQuery.BusinessObjectQueryInput]) -> Teamcenter.Services.Strong.Query._2007_09.SavedQuery.SavedQueriesResponse: ...
    def CreateSavedQueries(self, Inputs: list[Teamcenter.Services.Strong.Query._2013_05.SavedQuery.SavedQueryProperties]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ExecuteBOQueriesWithContext(self, Inputs: list[Teamcenter.Services.Strong.Query._2018_11.SavedQuery.BusinessObjectQueryInput2]) -> Teamcenter.Services.Strong.Query._2007_09.SavedQuery.SavedQueriesResponse: ...
    def ExecuteBOQueriesWithSort(self, Inputs: list[Teamcenter.Services.Strong.Query._2019_06.SavedQuery.BusinessObjectQueryInput3]) -> Teamcenter.Services.Strong.Query._2007_09.SavedQuery.SavedQueriesResponse: ...
    def ExecuteBOQueriesWithSortAndContext(self, Inputs: list[Teamcenter.Services.Strong.Query._2020_04.SavedQuery.BusinessObjectQueryInput4]) -> Teamcenter.Services.Strong.Query._2007_09.SavedQuery.SavedQueriesResponse: ...

class SavedQueryService:
    """
    
            The SavedQuery service provides operations to operate saved queries
such as create
            a set of saved queries, find saved query, execute a set of saved
queries and execute
            a Business Object Search (Simple Search).

Library Reference:

TcSoaQueryStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SavedQueryService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetSavedQueries(self) -> Teamcenter.Services.Strong.Query._2006_03.SavedQuery.GetSavedQueriesResponse:
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
    def DescribeSavedQueries(self, Queries: list[Teamcenter.Soa.Client.Model.Strong.ImanQuery]) -> Teamcenter.Services.Strong.Query._2006_03.SavedQuery.DescribeSavedQueriesResponse:
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
    def ExecuteSavedQuery(self, Query: Teamcenter.Soa.Client.Model.Strong.ImanQuery, Entries: list[str], Values: list[str], Limit: int) -> Teamcenter.Services.Strong.Query._2006_03.SavedQuery.ExecuteSavedQueryResponse:
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
    def DeleteQueryCriterias(self, QueryCriteriaNames: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Delete saved searches with given names.
             

Use Cases:

             Delete specified saved searches.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param QueryCriteriaNames: 
                         A list of saved search names to delete.
             
        :return: 
        """
        ...
    def ReorderSavedQueryCriterias(self, QueryCriteriaNames: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Reorder the saved Query Criterias in the MySavedSearches List:   The new order of
             query criteria names specified in the input list will be stored in the MySavedSearches
             list.    The input list should contain only existing query criteria names    If a
             query criteria name in the list is not located, it will not be stored in the list.
             The number of entries in the input list should match the number entries in the
             MySavedSearches list.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param QueryCriteriaNames: 
                         - vector of query criteria names with the new order.
             
        :return: ServiceData - The client id of the partial error   is the name of the Query Criteria
             which are either missing from or   not present in the "MySavedSearches" list.
        """
        ...
    def RetrieveQueryCriterias(self, QueryCriteriaNames: list[str]) -> Teamcenter.Services.Strong.Query._2007_01.SavedQuery.RetrieveQueryCriteriaResponse:
        """    
             Retrieve the information on the saved search by the search name.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param QueryCriteriaNames: 
                         A vector of search names for which to retrieve the information.
             
        :return: RetrieveQueryCriteriaResponse - contains a vector of SaveQueryCriteriaInfo where
             each member corresponds an input queryCriteriaName.  The response also contains
             a standard ServiceData member.  Partial errors contain a client id which is the queryCriteriaName
             mapped to the error message.
        """
        ...
    def SaveQueryCriterias(self, QueryCriterias: list[Teamcenter.Services.Strong.Query._2007_01.SavedQuery.SaveQueryCriteriaInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Saves a saved search with search name, query name, entry names, and entry values.
             If search name is not provided, the criteria keys or the criteria values size is
             0, or the criteria keys size does not equal to the criteria values size, or if error
             happens while creating the saved search, the related error information will be added
             to the error stack. If the search criteria size is no more than 0, ServiceException
             will throw out of this service. The created saved search objects will be returned.
             

Use Cases:

             User selects a query and fills in some criterias, and then save the search from thin
             client with a search name.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param QueryCriterias: 
                         A list of SaveQueryCriteriaInfo representing saved searches to be saved to the database.
             
        :return: ServiceData - The created saved search objects will be returned by service data,
             the related error information will also be returned from the error stack. If search
             name is not provided, the criteria keys or the criteria values size is 0, or the
             criteria keys size does not equal to the criteria values size, or if error happens
             while creating the saved search, the related error information will be added to the
             error stack.
        """
        ...
    @typing.overload
    def ExecuteSavedQueries(self, Input: list[Teamcenter.Services.Strong.Query._2007_06.SavedQuery.SavedQueryInput]) -> Teamcenter.Services.Strong.Query._2007_06.SavedQuery.ExecuteSavedQueriesResponse: ...
    @typing.overload
    def ExecuteSavedQueries(self, Input: list[Teamcenter.Services.Strong.Query._2007_09.SavedQuery.QueryInput]) -> Teamcenter.Services.Strong.Query._2007_09.SavedQuery.SavedQueriesResponse: ...
    @typing.overload
    def ExecuteSavedQueries(self, Input: list[Teamcenter.Services.Strong.Query._2008_06.SavedQuery.QueryInput]) -> Teamcenter.Services.Strong.Query._2007_09.SavedQuery.SavedQueriesResponse: ...
    def RetrieveSearchCriteria(self, SearchNames: list[str]) -> Teamcenter.Services.Strong.Query._2007_06.SavedQuery.RetrieveSearchCriteriaResponse:
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
    def SaveSearchCriteria(self, SearchCriteria: list[Teamcenter.Services.Strong.Query._2007_06.SavedQuery.SaveSearchCriteriaInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def FindSavedQueries(self, InputCriteria: list[Teamcenter.Services.Strong.Query._2010_04.SavedQuery.FindSavedQueriesCriteriaInput]) -> Teamcenter.Services.Strong.Query._2010_04.SavedQuery.FindSavedQueriesResponse:
        """    
             The user can find the saved queries of interest by passing in the criteria such as
             query name and description. The queries that are matching the input criteria will
             be returned back to the user.  This operation can be sued to find the queries with
             a given name(s) or description(s) or combination of name(s) and description(s). This
             operation returns the queries matching the input criteria names and descriptions.
             

Use Cases:

             Find saved queries by given saved query name(s) and description(s).
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param InputCriteria: 
                         Structure that contains the input criteria required to find the saved queries.
             
        :return: Returns the saved queries found matching the given input criteria.
        """
        ...
    def ExecuteBusinessObjectQueries(self, Inputs: list[Teamcenter.Services.Strong.Query._2010_09.SavedQuery.BusinessObjectQueryInput]) -> Teamcenter.Services.Strong.Query._2007_09.SavedQuery.SavedQueriesResponse:
        """    
             Execute business object searches (Simple Search) and return search results.
             

Use Cases:

             Execute business object searches (Simple Search).
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param Inputs: 
                         Business object query inputs
             
        :return: Contains (1) a set of QueryResults data structures and (2) a ServiceData. Partial
             errors are stored and referenced by input vector indexes.
        """
        ...
    def CreateSavedQueries(self, Inputs: list[Teamcenter.Services.Strong.Query._2013_05.SavedQuery.SavedQueryProperties]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    Creates a list of saved queries based on the input properties structure.
        :param Inputs: 
                         A saved query is created for each <font face="courier" height="10">SavedQueryProperties</font>
                         in the list.
             
        :return: 
        """
        ...
    def ExecuteBOQueriesWithContext(self, Inputs: list[Teamcenter.Services.Strong.Query._2018_11.SavedQuery.BusinessObjectQueryInput2]) -> Teamcenter.Services.Strong.Query._2007_09.SavedQuery.SavedQueriesResponse: ...
    def ExecuteBOQueriesWithSort(self, Inputs: list[Teamcenter.Services.Strong.Query._2019_06.SavedQuery.BusinessObjectQueryInput3]) -> Teamcenter.Services.Strong.Query._2007_09.SavedQuery.SavedQueriesResponse:
        """    
             This operation executes business object queries with sorting options.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param Inputs: 
                         Business object query inputs.
             
        :return: 
        """
        ...
    def ExecuteBOQueriesWithSortAndContext(self, Inputs: list[Teamcenter.Services.Strong.Query._2020_04.SavedQuery.BusinessObjectQueryInput4]) -> Teamcenter.Services.Strong.Query._2007_09.SavedQuery.SavedQueriesResponse: ...

