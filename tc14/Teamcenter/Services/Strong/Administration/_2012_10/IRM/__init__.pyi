import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class AMImpactedObjectsResponse:
    """
    
            Data structure that holds the UIDs of Teamcenter business objects whose READ
            access is impacted by the Access Manager rule tree changes, a Boolean
            flag that indicates if full reindex is needed or not and the service data with any
            partial errors that might happen while finding the impacted objects
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""
    IsImpactGlobal: bool
    """isImpactGlobal"""
    ImpactedUids: list[str]
    """impactedUids"""

class GetSessionValuesResponse:
    """
    
            Structure that holds the SessionValuesMap which contains session keys and corresponding
            session values. Each session key in the SessionValuesMap corresponds to a session
            attribute like groups, roles and project teams.
            
    """
    def __init__(self, ) -> None: ...
    SessionValues: System.Collections.Hashtable
    """
            A map of key-value pairs that holds the session keys and the matching session values
            from Read Expression string.
            """

class IRM:
    """
    Interface IRM
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAMImpactedObjects(self, FilterByIndexedStatus: bool) -> AMImpactedObjectsResponse:
        """    
             This operation lists the business objects whose read access is impacted by the changes
             in Access Manager (AM) rule tree. The rule tree changes considered are limited
             to those made after the previous call to this operation. This operation is usually
             called periodically and the objects whose read access privilege is modified due to
             the changes to AM rule tree between the previous call and the current one
             are determined and returned. Optionally, this operation returns the set of objects
             which is the intersection of objects impacted by AM rule changes and objects
             previously indexed. Previously indexed objects are stored in ACCT_TABLE table.
             
             AM rule configuration changes need re-login to refresh the in memory rule registry
             cache. Hence, until re-login after the AM rule changes, this operation will
             return ZERO objects.
             

Teamcenter Component:

             Entitlement - It Maps IRM SOA services to BMIDE.
             
        :param FilterByIndexedStatus: 
                         If true, only the objects previously indexed are included in the response
             
        :return: 
        """
        ...
    def GetSessionValues(self) -> GetSessionValuesResponse:
        """    
             This operation gets all the session information in the form of key values map.  Each
             key corresponds to particular session attribute like user, roles, groups,
             project teams, and licenses.  For each entry in the keys array, the
             corresponding entry in the values array contains the values for that specific session
             attribute. Session information returned from this SOA operation is used during read
             expression evaluation in external clients to determine the READ privilege
             to the current logged in user on the indexed Teamcenter data.
             

Teamcenter Component:

             Entitlement - It Maps IRM SOA services to BMIDE.
             
        :return: 
        """
        ...

