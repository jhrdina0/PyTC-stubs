import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class CreateProxyLinkInputInfo:
    """
    
            A structure containing uid,owning site of the object for which the ProxyLink object
            is created, primary object to which the proxy link object is related, relation name
            used to relate the primary object and the proxylink and the attributes to be populated
            on the proxy link object.
            
    """
    def __init__(self, ) -> None: ...
    ObjectUID: str
    """The uid of the object for which the ProxyLink is created."""
    OwningSite: str
    """The owning site of the object for which the ProxyLink is created."""
    ProxyLinkType: str
    """The name of the ProxyLink type."""
    Attributes: System.Collections.Hashtable
    """
            A map (string/string) of  property names and initial  value pairs to be populated
            on the ProxyLink object.
            """
    PrimaryObject: Teamcenter.Soa.Client.Model.ModelObject
    """The BusinessObject to attach the ProxyLink object."""
    RelationName: str
    """
            The name of the relation to use while attaching the ProxyLink object to the primaryObject
            .
            """

class ProxyLink:
    """
    Interface ProxyLink
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateProxyLink(self, Input: list[CreateProxyLinkInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates ProxyLink object(s) based on the input information provided
             and relates it to the primary objects at the proxy link site.
             

Use Cases:

             When the user wants to provide information about an object to a site other than the
             owning site of the object, the user can create a proxy link for that object.  From
             the different site, User can access the master object using the proxy link.
             

Teamcenter Component:

             Application Registry - WOLF application registry - includes 'Advanced Links' feature
             used by Remote Inbox.
             
        :param Input: 
                         The uid,owning site of the object(s) for which the ProxyLink object(s) are created,
                         primary objects to which the proxy link objects are related, relation name used to
                         relate the primary object and the proxylink and the attributes to be populated on
                         the proxy link objects.
             
        :return: ServiceData. ServiceData may contain the following errors: 207105 - Property update
             failed, 207106 - A proxy of that kind already exists, 207107 - A few proxies of that
             kind already exist, 207108 - A wrong type application name is provided, 207109 -
             The requested object wasn't found, 207110 - There is a problem with the preference,
             207111 - There is a problem with the preferene and external properties, 207112 -
             There is a problem with the preferene and internal properties, 207113 - Number of
             external/internal property names doesn't match, 207114 - A proxy related type is
             missing, 207115 - The Teamcenter sites registered for linking or Remote Inbox Subscription
             could not be obtained, 207201 - Failed to contact application registry. Either it
             is down or preference TC_external_app_reg_url is not set, 207204 - The application
             couldn't be found in the application registry, 207208 - The "object no longer referenced"
             call failed.
        """
        ...

