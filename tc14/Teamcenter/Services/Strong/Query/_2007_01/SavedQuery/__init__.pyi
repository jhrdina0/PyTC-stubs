import System
import Teamcenter.Soa.Client.Model
import typing

class RetrieveQueryCriteriaResponse:
    """
    RetrieveQueryCriteriaResponse
    """
    def __init__(self, ) -> None: ...
    Output: list[SaveQueryCriteriaInfo]
    """vector of SaveQueryCriteriaInfo"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """standard ServiceData member"""

class SaveQueryCriteriaInfo:
    """
    SaveQueryCriteriaInfo
    """
    def __init__(self, ) -> None: ...
    SearchName: str
    """The name of the saved search."""
    QueryName: str
    """The name of the query associated with this search."""
    Keys: list[str]
    """The attribute names for the query."""
    Values: list[str]
    """The attribute values for the query."""

class SavedQuery:
    """
    Interface SavedQuery
    """
    def __init__(self , *args: typing.Any) -> None: ...
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
    def RetrieveQueryCriterias(self, QueryCriteriaNames: list[str]) -> RetrieveQueryCriteriaResponse:
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
    def SaveQueryCriterias(self, QueryCriterias: list[SaveQueryCriteriaInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
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

