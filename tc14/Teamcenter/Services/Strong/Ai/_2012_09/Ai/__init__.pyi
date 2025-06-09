import System
import System.Collections
import Teamcenter.Services.Strong.Ai._2006_03.Ai
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ProjectFilter:
    """
    Structure to specify the filter when using getProjects  method.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """name of the AppliationInterface Object"""
    Description: str
    """description of the ApplicationInterface Object"""
    Type: str
    """type of the ApplicationInterface Object. The type must be a valid type of AI Object."""
    UserId: str
    """userId to filter on (maps to owning user)"""
    GroupName: str
    """filter on AI objects using groupName"""
    CreatedBefore: System.DateTime
    """filtering by Date"""
    CreatedAfter: System.DateTime
    """filtering by Date"""
    ModifiedBefore: System.DateTime
    """filtering by Date"""
    ModifiedAfter: System.DateTime
    """filtering by Date"""
    ReleasedBefore: System.DateTime
    """filtering by Date"""
    ReleasedAfter: System.DateTime
    """filtering by Date"""
    ContextString: str
    """maps to the context string of AI object's Export TransferMode."""
    TargetSiteIds: list[str]
    """valid site names to be used to search for ApplicationInterface objects."""
    TargetAppProjectId: str
    """
            if an application stamps a targetAppProject id using the setProjectsInfo method -
            they can use this for filtering.
            """

class FindRequestsFilter:
    """
    
            structure that captures the filtering options for getting the Request Objects. This
            will include the AppInterface filter options too.
            
    """
    def __init__(self, ) -> None: ...
    AiQryParams: ProjectFilter
    """
            structure to capture the filter options on parent(s) ApplicationInterfaces of the
            RequestObject(s)
            """
    RequestState: list[str]
    """
            vector  representing the requeststates to use for filtering. Currently, the only
            valid values are unique combinations of (case sensitive): Processing, Pending, Communicating,
            Completed, Rejected
            """
    RequestStatus: list[str]
    """
            vector of strings representing the statuses on the request to search for. Currently,
            the valid values are a combination of (case sensitive): Normal,  Warning, Severe,
            Abort
            """
    StateDescription: str
    """state description to use for searching for RequestObject."""
    StatusDescription: str
    """status message by which to filter for RequestObjects."""
    CustomStrings: System.Collections.Hashtable
    """vector of strings that have the custom key and value pair to search on."""
    RequestType: list[str]
    """
            the type of request - valid values:Publish, Sync. Empty vector if this filter option
            is not needed.
            """

class FindRequestsResponse:
    """
    
            structure containing the response from findRequests method. partial failures are
            captured in the serviceData and found Requests are captured in RequestDetails.
            
    """
    def __init__(self, ) -> None: ...
    Requests: list[RequestDetail]
    """list of found requests based on the input query."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Any partial errors are reported in this member."""

class GetProjectsInfo2Response:
    """
    get the ProjectInfo structure for each of the specified ApplicationInterfaceObjects.
    """
    def __init__(self, ) -> None: ...
    Infos: list[ProjectInfo]
    """info about the ApplicationInterface objects"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """partial errors are returned in this structure."""

class GetRequestsInfo2Response:
    """
    get the details on the input RequestObject.
    """
    def __init__(self, ) -> None: ...
    Details: list[RequestDetail]
    """
            details about the input RequestObjects. If there is an error getting info for any
            RequestObject, it will not be in this vector, but failure details will be in the
            serviceData.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            serviceData to capture any partialErrors. client id used will be the position in
            the input vector.
            """

class ProjectInfo:
    """
    Structure to specify ApplicationInterface information.
    """
    def __init__(self, ) -> None: ...
    Ai: Teamcenter.Soa.Client.Model.Strong.AppInterface
    """The ApplicationInterfaceObject for which the info is relevant."""
    TargetAppProjectId: str
    """The projectId string recorded on the ApplicationInterface Object"""
    Name: str
    """name of the AppliationInterface Object"""
    Description: str
    """description of the ApplicationInterface Object"""
    TargetSiteIds: list[str]
    """
            The list of names of targetSiteIds to be set on the ApplicationInterface Object.
            Entries must be valid site names.
            """

class RequestDetail:
    """
    Structure representing the details of the RequestObject
    """
    def __init__(self, ) -> None: ...
    Ro: Teamcenter.Soa.Client.Model.Strong.RequestObject
    """the request object for which the details are being provided."""
    Name: str
    """name of the RequestObject"""
    Description: str
    """description of the RequestObject"""
    StateDesc: str
    """description on the state of the RequestObject."""
    Status: Teamcenter.Services.Strong.Ai._2006_03.Ai.StatusInfo
    """the status fields of the RequestObject"""
    Rscope: int
    """
            2 values are possible:  0(whole)- no ExternalReference elements will be found in
            plmxml. Partial(1) then there will be ExternalReference elements in plmxml.
            """
    Rupdate: int
    """used to specify an incremental update. possible values are 0 (Full), 1 ( delta)."""
    KvPairs: System.Collections.Hashtable
    """
            key value pairs associated with the RequestObject. These would have been populated
            via the setRequestsInfo call.
            """

class RequestInfo:
    """
    
            structure representing gettable/settable information on a RequestObject by clients
            for a given RequestObject.
            
    """
    def __init__(self, ) -> None: ...
    Ro: Teamcenter.Soa.Client.Model.Strong.RequestObject
    """the object for which the data is being or retrieved."""
    StateMessage: str
    """The string to set/get for the RequestObject's state_msg property."""
    StatusInfo: Teamcenter.Services.Strong.Ai._2006_03.Ai.StatusInfo
    """
            Structure to set the status and status_msg attributes of RequestObject. These typically
            are used to provide the TC user information about what happened in the relevant client
            application.
            """
    KvPairs: System.Collections.Hashtable
    """
            key value pairs of strings to allow clients to set custom properties on the RequestObject.
            Limit of 64 bytes on key and 256 bytes on value.
            """

class Ai:
    """
    Interface Ai
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindRequests(self, Filter: FindRequestsFilter) -> FindRequestsResponse:
        """    
             method to find request objects based on the input criteria.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Filter: 
                         Mandatory input field for filtering Request objects as per the input criteria.
             
        :return: list of found requests and any  partial errors.
        """
        ...
    def GetProjects(self, Filter: ProjectFilter) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             get the Application Interface objects based on a optional filter.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Filter: 
                         optional filter used to narrow down the number of ApplicationInterface Objects.
             
        :return: ServiceData object that has the ApplicationInterface objects that were found (returned
             as plain objects).
        """
        ...
    def SetProjectsInfo(self, Infos: list[ProjectInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             set the info on the ApplicationInterface Objects.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Infos: 
                         info to be set on the ApplicationInterface Object. The Ai object is part of the structure.
             
        :return: ServiceData object that returns the objects on which setting the data succeeded,
             and partial failures for those that failed.
        """
        ...
    def SetRequestsInfo(self, Infos: list[RequestInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             method to allow caller to set the fields on the RequestObject.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Infos: 
                         vector of info elements to set data on respective RequestObject.
             
        :return: ServiceData that captures partial failures, and also list of updated objects if data
             is set successfully.
        """
        ...
    def GetProjectsInfo2(self, Projects: list[Teamcenter.Soa.Client.Model.Strong.AppInterface]) -> GetProjectsInfo2Response:
        """    
             return the projectInfo information for each of the supplied ApplicationInterface
             Objects.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Projects: 
                         list of Application Interface objects for which the details are needed.
             
        :return: return the info for the provided Application Interface Objects, and any partial errors
             - the Application Interface Objects position in the passed in vector will be used
             as the clientId for errors
        """
        ...
    def GetRequestsInfo2(self, Robjects: list[Teamcenter.Soa.Client.Model.Strong.RequestObject]) -> GetRequestsInfo2Response:
        """    
             get details about specific RequestObjects. These include state desc,status info,
             custom key value pairs.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Robjects: 
                         input vector of RequestObjects for which details are needed.
             
        :return: vector or RequestDetails. The size of this vector may not be same as input vector.
             Partial errors are recorded in serviceData.
        """
        ...

