import System
import System.Collections
import Teamcenter.Services.Strong.Ai._2012_09.Ai
import typing

class FindRequestsWithDependencyFilter:
    """
    
            structure that captures the filtering options for getting the Request Objects after
            considering dependency. This will include the AppInterface filter options too.
            
    """
    def __init__(self, ) -> None: ...
    AiQryParams: Teamcenter.Services.Strong.Ai._2012_09.Ai.ProjectFilter
    """
            structure to capture the filter option on parent(s) ApplicationInterfaces of the
            RequestObject(s)
            """
    RequestStatus: list[str]
    """
            vector of strings representing the statuses on the request to search for. Currently,
            the valid values are a combination of (case sensitive): Normal, Warning, Severe,
            Abort
            """
    StateDescription: str
    """state description to use for searching for RequestObject."""
    StatusDescription: str
    """status message by which to filter for RequestObjects."""
    CustomStrings: System.Collections.Hashtable
    """map of strings that have the custom key and value pair to search on."""

class Ai:
    """
    Interface Ai
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindRequestsWithDependencies(self, Filter: FindRequestsWithDependencyFilter) -> Teamcenter.Services.Strong.Ai._2012_09.Ai.FindRequestsResponse:
        """    
             This operation is based on dependency between the related  RequestObjects and on
             the input criteria provided to the operation input. The operation will return a list
             of RequestObjects to process. The returned RequestObjects are those whose property
             "type" is of value "Sync" and property "state" is of value "Pending". Further, this
             operation returns only those RequestObjects which are dependent on RequestObjects
             whose state is "Completed".  Dependency of RequestObject is determined by "fnd0pred_list"
             property. This property points to its preceding Request Object.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Filter: 
                         method to find request objects after considering dependency, based on the input criteria.
             
        :return: 203822 (search by request state not allowed)
        """
        ...

