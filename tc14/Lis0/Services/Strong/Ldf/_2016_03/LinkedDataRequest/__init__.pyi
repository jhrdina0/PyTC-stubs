import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class LDFResponseInfoVec:
    """
    List of LDF delegated UI Services or Factory Services.
    """
    def __init__(self, ) -> None: ...
    ResponseInfoVec: list[LDFServiceResponseInfo]
    """List of services definition."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """service data for partial errors"""

class LDFServiceResponseInfo:
    """
    Service response information.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Name of the delegated dialog or factory service."""
    Url: str
    """URL of the delegated dialog or the factory service."""
    HintHeight: str
    """Hint height of the delegated dialog."""
    HintWidth: str
    """Hint width of the delegated dialog."""
    IsDefault: bool
    """Flag if it is primary or default."""
    ServiceType: str
    """Type of the service."""
    IsUIService: bool
    """Is this UI Service?"""
    SvcUid: str
    """Uid of Delegated Dialog or Factory Service."""

class PropertiesValueStructure:
    """
    Map Properties Name & Value Pair.
    """
    def __init__(self, ) -> None: ...
    PropMap: System.Collections.Hashtable
    """Map Properties Name & Value Pair."""

class LinkedDataRequest:
    """
    Interface LinkedDataRequest
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetLDFPropertyValues(self, Url: str, UidServiceProvider: str) -> PropertiesValueStructure:
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
    def GetLDFServices(self, ServiceProviderUid: str, FactoryOrUIService: int) -> LDFResponseInfoVec:
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

