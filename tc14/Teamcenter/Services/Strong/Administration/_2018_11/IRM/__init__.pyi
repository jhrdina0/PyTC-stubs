import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class GetSessionInfoFromTicketResponse:
    """
    
            Structure that holds the user, session information and service data. The user and
            session information is captured in the call to the related getSessionInfoTicket and
            will be decoded from the encrypted sessionInfoTicket input string.
            
    """
    def __init__(self, ) -> None: ...
    UserInfo: System.Collections.Hashtable
    """
            User login information, like: userId, userUid, groupName, groupUid, roleName, roleUid,
            projectId, projectUid
            """
    SessionValues: System.Collections.Hashtable
    """sessionValues"""
    SiteId: int
    """Site identifier that generated the ticket."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData  in which the partial errors are communicated to the client."""

class GetSessionInfoTicketResponse:
    """
    
            GetSessionInfoTicketResponse structure contains an encrypted ticket which has to
            be used to retrieve session info.
            
    """
    def __init__(self, ) -> None: ...
    SessionInfoTicket: str
    """
            An encrypted ticket in string format. Client can preserve this ticket and pass this
            ticket to getSessionInfoFromTicket to get the session info back.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData in which the partial errors are communicated to the client."""

class IRM:
    """
    Interface IRM
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetSessionInfoFromTicket(self, SessionInfoTicket: str) -> GetSessionInfoFromTicketResponse:
        """    
             This operation gets all the session information in the form of key values map only
             if valid sessionInfoTicket is provided by client. Each key corresponds to particular
             session attribute like user, roles, groups, project teams, and licenses. For each
             entry in the keys array, the corresponding entry in the values array contains the
             values for that specific session attribute. Session information returned from this
             operation is used during read expression evaluation in external clients to determine
             the READ privilege to the current logged in user on the indexed Teamcenter data.
             

Use Cases:

             VDS (Visualization Data Server) has no user concept or connection authentication
             by design. TC SessionInfo passed to VDS clients after valid Teamcenter login but
             no validation is done by VDS today. Due to this shortcoming VDS is potential for
             spoofing, user session hacking and session reuse. To overcome this issue two new
             service operations are proposed and will be used. Calling client VDS uses getSessionInfoTicket
             operation to get encrypted (tamper proof) data packet and preserves the encrypted
             string. VDS calls SOA GetSessionInfoFromTicket with this ticket to get back the user
             session information. GetSessionInfoFromTicket returns back the session information
             only if the ticket is not expired.
             

Teamcenter Component:

             Entitlement - It Maps IRM SOA services to BMIDE.
             
        :param SessionInfoTicket: 
                         ticket
             
        :return: 
        """
        ...
    def GetSessionInfoTicket(self) -> GetSessionInfoTicketResponse:
        """    
             This operation returns User, Group, Session Info, Site identifier and Ticket Expiry
             Time in the form of an encrypted string. Encrypted string ticket returned from this
             operation is used by getSessionInfoFromTicket operation to retrieve the session info.
             

Use Cases:

             VDS has no user concept or connection authentication by design. Teamcenter session
             information is passed to VDS clients after valid Teamcenter login but no validation
             is done by VDS today. Due to this shortcoming VDS is potential for spoofing, user
             session hacking and session reuse. To overcome this issue 2 new service operations
             are proposed and will be used. Calling client VDS uses getSessionInfoTicket to get
             encrypted (tamper proof) data packet and preserves the encrypted string. VDS client
             calls getSessionInfoFromTicket with this ticket to get back the user session information.
             getSessionInfoFromTicket returns back the session information only if the ticket
             is not expired and valid.
             

Teamcenter Component:

             Entitlement - It Maps IRM SOA services to BMIDE.
             
        :return: 
        """
        ...

