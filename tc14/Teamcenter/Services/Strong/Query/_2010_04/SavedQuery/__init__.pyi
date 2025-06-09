import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FindSavedQueriesCriteriaInput:
    """
    Structure that contains the input criteria required to find the saved queries.
    """
    def __init__(self, ) -> None: ...
    QueryNames: list[str]
    """Names of saved queries to be found."""
    QueryDescs: list[str]
    """Descrptions of saved queries to be found."""
    QueryType: int
    """The type of the saved queries."""

class FindSavedQueriesResponse:
    """
    Holds the response for FindSavedQueries.
    """
    def __init__(self, ) -> None: ...
    SavedQueries: list[Teamcenter.Soa.Client.Model.Strong.ImanQuery]
    """A vector of Saved Query objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData"""

class SavedQuery:
    """
    Interface SavedQuery
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindSavedQueries(self, InputCriteria: list[FindSavedQueriesCriteriaInput]) -> FindSavedQueriesResponse:
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

