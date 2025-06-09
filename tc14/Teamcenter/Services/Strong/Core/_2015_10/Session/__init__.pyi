import System
import System.Collections
import Teamcenter.Schemas.Soa._2011_06.Metamodel
import Teamcenter.Services.Strong.Core._2006_03.Session
import Teamcenter.Services.Strong.Core._2007_12.Session
import Teamcenter.Soa.Client.Model
import typing

class Session:
    """
    Interface Session
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetTypeDescriptions2(self, TypeNames: list[str], Options: System.Collections.Hashtable) -> Teamcenter.Schemas.Soa._2011_06.Metamodel.TypeSchema:
        """    
             Gets the Meta data for the named Business Model object types based on the configurations
             specified by the client.  To improve performance, clients can specify to exclude
             certain Meta data such as LOV References and Naming Rule References for the given
             types.
             
             If options are not provided this operation returns all meta data associated with
             given types.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param TypeNames: 
                         List of Business Model Object type names.
             
        :param Options: 
                         A list of property constant names to be fetched. If the list of property constant
                         names is empty this operation does not return any constant values. If the PropertyConstants
                         option is not provided then it will return all constants that can server can return.
             
        :return: The Meta data for the named types as requested  . There are no errors returned, invalid
             input types names are ignored and no type information will be returned for those
             types.
        """
        ...
    def SetUserSessionStateAndUpdateDefaults(self, Pairs: list[Teamcenter.Services.Strong.Core._2007_12.Session.StateNameValue]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation sets the desired user session state values. This operation also updates
             the default value of the Group, Role and Project when these session states are changed.
             

             To clear a field's value, client needs to pass an empty string "" as the value.
             

             Failure to set a particular state value will result in a Partial Error with the clientId
             set to the name of the state property. State values can be per client session or
             per server session. Client session state is kept separate for each client application
             sharing the same Teamcenter server session, while server session state is shared
             with all client application sharing the Teamcenter server session.
             

             Valid keys for the session state pairs are:
             


currentChangeNotice - The UID of the ChangeNotice business
             object for this session (client session).This is deprecated from release Teamcenter
             11.5.
             
refreshPOM - If true the business objects in the POM are refreshed
             before returning property values.  This ensures property data is up-to-date, but
             is a performance hit (client session).
             
objectPropertyPolicy - The name of the current object property
             policy. This can also be controlled through the ObjectPropertyPolicyManager in the
             SOA client framework  (client session).
             
maxOperationBracketTime - Time (seconds) to bracket to limit
             a  POM refresh (client session).
             
maxOperationBracketInactiveTime - Time (seconds) to bracket
             to limit a  POM refresh (client session).
             
usePolicyOnly - If true, only properties defined in the current
             Object Property Policy will be returned. Objects that are added to the updated list
             of the ServiceData without named properties by default are returned with all properties
             currently loaded in the POM.
             
formatProperties - If true, the display value of the property
             will be formatted, if there is an active property formatter is attached to it. If
             false, the display value of the property will not be formatted, even if there is
             an active property formatter attached to it (client session).
             
currentProject - The UID of the Project object (server
             session).
             
workContex - The UID of the WorkContext object (server
             session).
             
volume - The UID of the Volume object (server session).
             
local_volume - The UID of the LocalVolume object (server
             session).
             
groupMember - The UID of the GroupMember object (server
             session).
             
currentDisplayRule - The UID of the DisplayRule object
             (server session).
             
currentOrganization - The UID of the Organization object
             (server session).
             
locationCodePref - The CAGE/Location Code preference. This
             value is set on the Item attribute fnd0OriginalLocationCode
             when Item objects are created (client session).
             
currentChangeItem - The UID of the Change Item Revision business
             object for this session. This functionality is supported from Teamcenter 11.5.
             



Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Pairs: 
                         A list of name/value pairs (string/string) of state properties to set.
             
        :return: 
        """
        ...
    def SponsoredLogin(self, SponsoringUser: str, Password: str, SponsoredUser: str, SponsoredGroup: str, SponsoredRole: str, Locale: str, SessionDiscriminator: str) -> Teamcenter.Services.Strong.Core._2006_03.Session.LoginResponse:
        """    
             Authenticates the sponsoring user`s credentials and initialize a Teamcenter session
             for the sponsored user. The operation will throw an InvalidCredentialsException as
             described below.
             

             When the client application is deployed to a 4Tier environment the login operation
             also contributes to the assignment of a Teamcenter server instance to the client
             session. The sponsoring user, sponsored users and sessionDiscriminator are considered
             in server assignment.
             
             Note: The sessionDiscriminator could be blank ("") or have some value (e.g. "session1"
             or "session2")
             

             Example with blank ("") sessionDiscriminator:
             
             - Sponsor1/User1 and Sponsor1/User2 will be assigned to different servers since their
             access controls are based on User1 and User2
             
             - Sponsor1/User1 and Sponsor2/User1 will be assigned to different servers.
             
             - Sponsor1/User1 and User1 will be assigned to different servers.
             

             Example with "session1" and "session2" sessionDiscriminator:
             
             - Sponsor1/User1(session1) and Sponsor1/User1(session1) will be assigned to same
             servers
             
             - Sponsor1/User1(session1) and Sponsor1/User1(session2) will be assigned to different
             servers
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param SponsoringUser: 
                         The sponsoring user`s Teamcenter user name. This is case insensitive (jdoe or JDOE)
             
        :param Password: 
                         The sponsoring user`s Teamcenter password.
             
        :param SponsoredUser: 
                         Sponsored user`s user name. This is case insensitive (jdoe or JDOE)
             
        :param SponsoredGroup: 
                         The group ID for the sponsored user.
             
        :param SponsoredRole: 
                         The role of the sponsored user.
             
        :param Locale: 
                         The locale to be used by the Teamcenter server process for this session. If null,
                         the server`s default locale will be used.
             
        :param SessionDiscriminator: 
                         Client defined identifier for this session. This argument is ignored when the client
                         application is deployed in a 2Tier environment (IIOP communication).
             
        :return: 128004:  The logon is accepted. However, data entry should only contain characters
             that belong to the encoding of the database instance. The information is in the error
             message.
        """
        ...
    def SponsoredLoginSSO(self, SponsoringUser: str, SsoCredentials: str, SponsoredUser: str, SponsoredGroup: str, SponsoredRole: str, Locale: str, SessionDiscriminator: str) -> Teamcenter.Services.Strong.Core._2006_03.Session.LoginResponse:
        """    
             Authenticates the sponsoring user using Single-Sign-On (SSO) credentials and initialize
             a Teamcenter session for the sponsored user client. The username and ssoCredentials
             arguments are for the sponsoring user and must be obtained from Teamcenter's Security
             Services. The SsoCredentials class offers a simple API to get these values. The operation
             will throw an InvalidCredentialsException as described below.
             

             When the client application is deployed to a 4Tier environment the login operation
             also contributes to the assignment of a Teamcenter server instance to the client
             session. The sponsoring user, sponsored users and sessionDiscriminator are considered
             in server assignment.
             
             Note: The sessionDiscriminator could be blank ("") or have some value (e.g. "session1"
             or "session2")
             

             Example with blank ("") sessionDiscriminator:
             
             - Sponsor1/User1 and Sponsor1/User2 will be assigned to different servers since their
             access controls are based on User1 and User2
             
             - Sponsor1/User1 and Sponsor2/User1 will be assigned to different servers.
             
             - Sponsor1/User1 and User1 will be assigned to different servers.
             

             Example with "session1" and "session2" sessionDiscriminator:
             
             - Sponsor1/User1(session1) and Sponsor1/User1(session1) will be assigned to same
             servers
             
             - Sponsor1/User1(session1) and Sponsor1/User1(session2) will be assigned to different
             servers
             

             Example with "session1" and "session2" sessionDiscriminator:
             
             - Sponsor1/User1(session1) and Sponsor1/User1(session1) will be assigned to same
             servers
             
             - Sponsor1/User1(session1) and Sponsor1/User1(session2) will be assigned to different
             servers
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param SponsoringUser: 
                         The sponsoring user`s Teamcenter user name. This is case insensitive (jdoe or JDOE)
             
        :param SsoCredentials: 
                         The sponsoring user's Teamcenter SSO credentials. This should have been obtained
                         from Teamcenter Security Services.
             
        :param SponsoredUser: 
                         Sponsored user`s user name. This is case insensitive (jdoe or JDOE)
             
        :param SponsoredGroup: 
                         The group ID for the sponsored user.
             
        :param SponsoredRole: 
                         The role of the sponsored user.
             
        :param Locale: 
                         The locale to be used by the Teamcenter server process for this session. If null,
                         the server`s default locale will be used.
             
        :param SessionDiscriminator: 
                         Client defined identifier for this session. This argument is ignored when the client
                         application is deployed in a 2Tier environment (IIOP communication).
             
        :return: 128004: The logon is accepted. However, data entry should only contain characters
             that belong to the encoding of the database instance. The information is in the error
             message.
        """
        ...

