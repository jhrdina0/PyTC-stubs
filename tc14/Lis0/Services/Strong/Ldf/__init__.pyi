import Lis0.Services.Strong.Ldf._2015_03.LinkedDataRequest
import Lis0.Services.Strong.Ldf._2016_03.LinkedDataRequest
import Lis0.Services.Strong.Ldf._2018_06.LinkedDataRequest
import System
import System.Collections
import Teamcenter.Soa.Client

class LinkedDataRequestRestBindingStub(LinkedDataRequestService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ExecuteLinkedDataRequests(self, Requests: list[Lis0.Services.Strong.Ldf._2015_03.LinkedDataRequest.LinkedResourceRequest]) -> Lis0.Services.Strong.Ldf._2015_03.LinkedDataRequest.LinkedResourceResponse: ...
    def GenerateLinkedDataURI(self, ServiceURI: str, Puid: str) -> Lis0.Services.Strong.Ldf._2015_03.LinkedDataRequest.LinkedResourceResponse: ...
    def GetLDFPropertyValues(self, Url: str, UidServiceProvider: str) -> Lis0.Services.Strong.Ldf._2016_03.LinkedDataRequest.PropertiesValueStructure: ...
    def GetLDFServices(self, ServiceProviderUid: str, FactoryOrUIService: int) -> Lis0.Services.Strong.Ldf._2016_03.LinkedDataRequest.LDFResponseInfoVec: ...
    def GetLDFPropertiesRelationTypes(self, UidContextObject: str, Url: str, UidServiceProvider: str) -> Lis0.Services.Strong.Ldf._2016_03.LinkedDataRequest.PropertiesValueStructure: ...
    def GetLDFFileSelectionDialogService(self, LdfFileSelectionDialogInputMap: System.Collections.Hashtable) -> Lis0.Services.Strong.Ldf._2018_06.LinkedDataRequest.LdfFileSelectionDialogResponse: ...

class LinkedDataRequestService:
    """
    
            This LinkedDataRequest SOA Service supports implementation of Linked Data Framework.
            This framework allows Teamcenter to work with disparate software systems, which have
            implemented OSLC standard (Open Services for Lifecycle Collaboration). This would
            allow Teamcenter business objects to link via URIs (Unique Resource Identifier) with
            other business objects from remote system. Thereby, end user can invoke CREATE, READ,
            UPDATE, DELETE operations from Teamcenter onto remote system via programmatic interfaces
            or using delegated dialog from remote system.
            
            This service would include following features:
            
            1.Discovery API operation implementation corresponding to given HTTP request.
            
            2.Generate a unique URI for the given Teamcenter business object linked to the remote
            site and return the type of that business object.
            
            3.Generate Json for creating a link, for the given Teamcenter business object, at
            the remote site with modify (REST action: PUT) request for the remote object.
            
            4.Requests server to get request token & request token secret from given Service
            Provider. It returns the request token back to the SOA client.
            
            5.Requests server to get access token & access token secret from given Service
            Provider.
            
            6.Signs the given HTTP request with OAuth header. It encrypts using HMAC SHA1.
            


Library Reference:

Lis0SoaLdfStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> LinkedDataRequestService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ExecuteLinkedDataRequests(self, Requests: list[Lis0.Services.Strong.Ldf._2015_03.LinkedDataRequest.LinkedResourceRequest]) -> Lis0.Services.Strong.Ldf._2015_03.LinkedDataRequest.LinkedResourceResponse:
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
    def GenerateLinkedDataURI(self, ServiceURI: str, Puid: str) -> Lis0.Services.Strong.Ldf._2015_03.LinkedDataRequest.LinkedResourceResponse:
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
    def GetLDFPropertyValues(self, Url: str, UidServiceProvider: str) -> Lis0.Services.Strong.Ldf._2016_03.LinkedDataRequest.PropertiesValueStructure:
        """    
             This operation invokes the GET service to remote site and fetches the property values
             for the remote linked object.
             

Teamcenter Component:

             Linked Data Framework - Component for Linked Data Framework (LDF)
             
        :param Url: 
                         The URL for linked object from remote system.
             
        :param UidServiceProvider: 
                         Service Provider UID.
             
        :return: typedef std::map< std::string, std::string > StringKeyValueMap;
        """
        ...
    def GetLDFServices(self, ServiceProviderUid: str, FactoryOrUIService: int) -> Lis0.Services.Strong.Ldf._2016_03.LinkedDataRequest.LDFResponseInfoVec:
        """    
             This operation gets the details of programmatic or UI services for the given service
             provider.
             

Teamcenter Component:

             Linked Data Framework - Component for Linked Data Framework (LDF)
             
        :param ServiceProviderUid: 
                         The UID for remote system service provider, registered in teamcenter.
             
        :param FactoryOrUIService: 
                         2 - Get both Factory as well as Delegated UI Services.
             
        :return: is UIService     If true, this is a delegated UI Service, otherwise it is factory
             service.
        """
        ...
    def GetLDFPropertiesRelationTypes(self, UidContextObject: str, Url: str, UidServiceProvider: str) -> Lis0.Services.Strong.Ldf._2016_03.LinkedDataRequest.PropertiesValueStructure:
        """    
             This Operation invokes the Rest Get call to remote site and fetches the property
             values for the remote linked object and find all the available relation types that
             the remote system object should be linked with given Teamcenter Context Object.
             

Teamcenter Component:

             Linked Data Framework - Component for Linked Data Framework (LDF)
             
        :param UidContextObject: 
                         The UID for primary Teamcenter Business Object associated to LDF Link, representing
                         remote object via Relation Object.
             
        :param Url: 
                         Example:-http://pnv6s282.net.plm.eds.com:8085/polarion/oslc/services/projects/TcLDFConnectorProject01/changeRequests/TcLDFConnectorProject01-529.
             
        :param UidServiceProvider: 
                         The UID of the Service Provider, (of type <b>Lis0ServiceProvider</b>) representing
                         remote site project container, defined in Teamcenter.
             
        :return: contains map "propMap" (string, string)
             representing property names and their values from the remote linked object.
        """
        ...
    def GetLDFFileSelectionDialogService(self, LdfFileSelectionDialogInputMap: System.Collections.Hashtable) -> Lis0.Services.Strong.Ldf._2018_06.LinkedDataRequest.LdfFileSelectionDialogResponse:
        """    
             This operation creates dataset of given name and type. It will then build the URL
             for associated Remote File Selection Delegated UI with parameters of dataset UID,MIME
             types and the external UID. The remote system should use MIME types for File selection
             Filtering and use the external UID to search for the object to collect the remote
             files from.
             

Teamcenter Component:

             Linked Data Framework - Component for Linked Data Framework (LDF)
             
        :param LdfFileSelectionDialogInputMap: 
                         5.datasetUid
             
        :return: 121012: The URL request cannot be processed successfully.
        """
        ...

