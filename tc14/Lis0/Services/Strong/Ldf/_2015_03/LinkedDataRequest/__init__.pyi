import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class LinkedResourceOutput:
    """
    
            Linked Data Framework (LDF) resource request output. It contains the response output
            data
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """The unmodified string from the input that this data structure is associated with."""
    Status: int
    """
            HTTP Code for Request Output status. The status values are the standard HTTP status
            codes. Some of the common status are as below:
            

200: OK
            
401: Object Not Found.
            
500: Internal Server Error
            

"""
    HeaderMap: System.Collections.Hashtable
    """HTTP response header pairs (string, string)."""
    Body: str
    """HTTP Response Body."""

class LinkedResourceRequest:
    """
    
            Linked Data Framework (LDF) resource request. It contains linked data request parameters
            for a given REST action
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    ResourceUri: str
    """Request URI, the POST domain URL."""
    HttpMethod: str
    """HTTP request type. "HttpGet", "HttpPut", "HttpPost", "HttpDelete"."""
    HeaderMap: System.Collections.Hashtable
    """HTTP request header pairs(string, string)."""
    Body: str
    """HTTP Request Body."""

class LinkedResourceResponse:
    """
    
            Linked Data Framework (LDF) resource response. It contains the linked data response
            output.
            
            For REST GET action, it contains string in Resource Description Framework (RDF) format
            containing resource details and HTTP response code.
            
            For REST PUT action, it contains ETAG and HTTP response code.
            
            For REST POST action, it contains Linked data URI, ETAG and HTTP response code.
            
            For REST DELETE action, it contains HTTP response code.
            

    """
    def __init__(self, ) -> None: ...
    Outputs: list[LinkedResourceOutput]
    """
            A list of request outputs for returning back to Web Tier. The clientID element will
            be blank, as it does not corespond to a specific input element.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Serivce data."""

class LinkedDataRequest:
    """
    Interface LinkedDataRequest
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteLinkedDataRequests(self, Requests: list[LinkedResourceRequest]) -> LinkedResourceResponse:
        """    
             This operation takes HTTP request URL as input and invokes the appropriate component
             for that linked data consumer request. The request is primarily for delegated UI
             or for factory invocation, apart from the catalog listing. In case of delegated UI,
             this operation returns the delegated UI URL back to the web tier, which would then
             render the corresponding web page for the consumer to use. In case of factory invocation,
             this linked data request invokes the operation from the given library, inside the
             Teamcenter server. For catalog listing or resource shape listing, this operation
             presents processed RDF content as output.
             

Use Cases:

             Execute Linked Data Framework (LDF) resource requests, including:
             

Get registered services' description
             
Post requests using the Creation Factory API
             
Get business objects using the Query Factory API
             



Teamcenter Component:

             Linked Data Framework - Component for Linked Data Framework (LDF)
             
        :param Requests: 

        :return: 
        """
        ...
    def GenerateLinkedDataURI(self, ServiceURI: str, Puid: str) -> LinkedResourceResponse:
        """    
             This operation takes HTTP request URL and uid of the Teamcenter business object to
             be linked as inputs. It generates the URI for that business object which can be stored
             in remote linked data system for linking to this Teamcenter business object. It returns
             the type of the business object as output.
             

Use Cases:

             Validate the input serviceURI
             
             Get the valid BO Service
             
             Generate the URI
             

Teamcenter Component:

             Linked Data Framework - Component for Linked Data Framework (LDF)
             
        :param ServiceURI: 

        :param Puid: 

        :return: 
        """
        ...

