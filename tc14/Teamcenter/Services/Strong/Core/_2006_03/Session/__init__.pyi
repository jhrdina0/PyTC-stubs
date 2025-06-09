import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetAvailableServicesResponse:
    """
    List of available services and operations.
    """
    def __init__(self, ) -> None: ...
    ServiceNames: list[str]
    """List of available services"""

class GetGroupMembershipResponse:
    """
    Info from getGroupMembership operation.
    """
    def __init__(self, ) -> None: ...
    GroupMembers: list[Teamcenter.Soa.Client.Model.Strong.GroupMember]
    """
            A list of all the valid GroupMember objects for the current session`s User.
            A GroupMember holds identifiers for a User, Group, and Role
            and represents that the user belongs to a group with the particular role.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The plain list has all the GroupMembers, Groups and Roles for
            this User
"""

class GetSessionGroupMemberResponse:
    """
    
            Information returned from the getSessionGroupMember
            service operation.
            
    """
    def __init__(self, ) -> None: ...
    GroupMember: Teamcenter.Soa.Client.Model.Strong.GroupMember
    """
            The GroupMember object which represents the logged in user's, Group,
            and Role for the current session.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The GroupMember object is included in the plain list."""

class LoginResponse:
    """
    
            The  User and GroupMember objects for the user of this session. Partial
            errors are returned in the ServiceData when
            the authentication is successful but requested role is not supported.
            
    """
    def __init__(self, ) -> None: ...
    User: Teamcenter.Soa.Client.Model.Strong.User
    """The User of this session."""
    GroupMember: Teamcenter.Soa.Client.Model.Strong.GroupMember
    """The GroupMember of this session."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The GroupMember and User are added to the plain object list."""

class PreferencesResponse:
    """
    Info from get/setPreferences
    """
    def __init__(self, ) -> None: ...
    Preferences: Teamcenter.Soa.Client.Model.Preferences
    """The requested preference name/values."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Any partial errors that may occur when filling this request."""

class PrefSetting:
    """
    Info for setting preferences
    """
    def __init__(self, ) -> None: ...
    PrefScope: str
    """
            The scope in which the preferences are to be set, "all", "site", "user", "group",
            or "role".
            """
    PrefName: str
    """The name of the preference."""
    PrefValues: list[str]
    """The array of values for this perference."""

class Session:
    """
    Interface Session
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPreferences(self, PrefScope: str, PrefNames: list[str]) -> PreferencesResponse:
        """    
             Get preference values.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param PrefScope: 
                         The scope in which the preferences are to be searched,                     "all",
                         "site", "user", "group", or "role".
             
        :param PrefNames: 
                         A vector of the names of the desired preferences.
             
        :return: A PreferencesResponse structure. The preference names and values are returned in
             the preferences element. If no preference with the given name exists, no error is
             raised and no value is returned. Any other errors are returned in the serviceData
             element.
        """
        ...
    def SetPreferences(self, Settings: list[PrefSetting]) -> PreferencesResponse:
        """    
             Set preference values.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param Settings: 
                         vector of PrefSetting structures, which specify the scope, name, and value(s) for
                         each of the preferences to be set.
             
        :return: A PreferencesResponse structure. The preferences element returns the new values of
             preferences which were successfully set. The serviceData element returns any partial
             errors encountered while setting specific preference values.
        """
        ...
    def GetAvailableServices(self) -> GetAvailableServicesResponse:
        """    
             This operation returns a list of services and service operations that this Teamcenter
             server instance supports. This is useful for client applications that expose different
             functionality based on the version of the Teamcenter server it is connecting to.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :return: 
        """
        ...
    def GetGroupMembership(self) -> GetGroupMembershipResponse:
        """    
             Get the valid groups and roles for the current user.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :return: 
        """
        ...
    def GetSessionGroupMember(self) -> GetSessionGroupMemberResponse:
        """    
             Get the Group and Role for the current session. The group and role
             are set at login, either to default values or as specified by the input arguments
             to the login operation. The group and role can be changed at any time throughout
             the session through the setSessionGroupMember
             or setUserSessionState operations.
             

Dependencies:

             setSessionGroupMember
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :return: 
        """
        ...
    def Login(self, Username: str, Password: str, Group: str, Role: str, SessionDiscriminator: str) -> LoginResponse:
        """    
             Authenticates the user's credentials and initialize a Teamcenter session for this
             client. The operation will throw an InvalidCredentialsException
             if the username, password
             or group is not valid.
             
             When the client application is deployed to a 4Tier environment (communication through
             HTTP or TCCS) the login operation also contributes to the assignment of a Teamcenter
             server instance to the client session. The Teamcenter architecture varies from other
             client server architectures in that there is a dedicated instance of the Teamcenter
             server per client application. However, there are use cases where it is desirable
             for a single user to have multiple desktop applications running and each sharing
             a single instance of a Teamcenter server. This is controlled through the following
             elements:
             

hostPath    From
             the Connection class constructor, this specifies  the address (URI) the Teamcenter
             server is hosted on.
             
username    From
             this login operation, this specifies the user's Teamcenter user name.
             
sessionDiscriminator    From
             this login operation, this identifies the client session.
             



             The hostPath argument determines the server
             machine that the client connects to. Once there, the pool manager on that host uses
             the username and sessionDiscriminator
             arguments of the logon request to determine which Teamcenter server instance to assign
             the client to. If the pool manager has an existing Teamcenter server instance with
             the username/sessionDiscriminator
             key, the client is assigned to that existing instance of the Teamcenter server, and
             therefore sharing the server with another client; otherwise, a new instance of the
             Teamcenter server is used. There are a few general scenarios for the sessionDiscriminator argument:
             


Blank     If the user jdoe logs on to
             Teamcenter using two or more client applications using a blank sessionDiscriminator argument (for example, jdoe/ ), all
             of those clients are assigned to the same Teamcenter server instance. These client
             applications can be running on the same or different client hosts.
             
Constant     If the user jdoe logs on
             to Teamcenter using two or more client applications using a constant or fixed sessionDiscriminator argument (for example, jdoe/MyApp
             ), those clients are assigned to the same Teamcenter server instance. This is similar
             to the blank sessionDiscriminator argument;
             the difference is that only multiple instances of the client application using myApp
             started by jdoe share the same Teamcenter server instance.
             
Unique     If the user jdoe logs on using
             a unique random-generated string (for example, jdoe/akdk938lakc), the
             client application will be assigned to a dedicated instance of the Teamcenter server.
             



             The scenario you use depends on how your client application is used in the integrated
             environment. The most common case is the unique sessionDiscriminator
             value.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Username: 
                         The user's Teamcenter user name.
             
        :param Password: 
                         The user's Teamcenter password.
             
        :param Group: 
                         The group ID for this session. If empty (""), the user's default group is assumed.
             
        :param Role: 
                         The role the user is performing in the group. If empty (""), the user's default role
                         in the group is assumed.
             
        :param SessionDiscriminator: 
                         Client defined identifier for this session. This argument is ignored when the client
                         application is deployed in a 2Tier environment (IIOP communication).
             
        :return: 
        """
        ...
    def LoginSSO(self, Username: str, SsoCredentials: str, Group: str, Role: str, SessionDiscriminator: str) -> LoginResponse:
        """    
             Authenticates the user using Single-Sign-On (SSO) credentials and initialize a Teamcenter
             session for this client. The username and
             ssoCredentials arguments must be obtained
             from Teamcenter's Security Services. The SsoCredentials
             class offers a simple API to get these values. The operation will throw an InvalidCredentialsException if the username, ssoCredentials
             or group is not valid.
             
             When the client application is deployed to a 4Tier environment (communication through
             HTTP or TCCS) the login operation also contributes to the assignment of a Teamcenter
             server instance to the client session. The Teamcenter architecture varies from other
             client server architectures in that there is a dedicated instance of the Teamcenter
             server per client application. However, there are use cases where it is desirable
             for a single user to have multiple desktop applications running and each sharing
             a single instance of a Teamcenter server. This is controlled through the following
             elements:
             

hostPath    From
             the Connection class constructor, this specifies  the address (URI) the Teamcenter
             server is hosted on.
             
username    From
             this login operation, this specifies the user's Teamcenter user name.
             
sessionDiscriminator    From
             this login operation, this identifies the client session.
             



             The hostPath argument determines the server
             machine that the client connects to. Once there, the pool manager on that host uses
             the username and sessionDiscriminator
             arguments of the logon request to determine which Teamcenter server instance to assign
             the client to. If the pool manager has an existing Teamcenter server instance with
             the username/sessionDiscriminator
             key, the client is assigned to that existing instance of the Teamcenter server, and
             therefore sharing the server with another client; otherwise, a new instance of the
             Teamcenter server is used. There are a few general scenarios for the sessionDiscriminator
             argument:
             


Blank     If the user jdoe logs on to Teamcenter
             using two or more client applications using a blank sessionDiscriminator
             argument (for example, jdoe/ ), all of those clients are assigned to the same
             Teamcenter server instance. These client applications can be running on the same
             or different client hosts.
             
Constant     If the user jdoe logs on to Teamcenter
             using two or more client applications using a constant or fixed sessionDiscriminator argument (for example, jdoe/MyApp
             ), those clients are assigned to the same Teamcenter server
             instance. This is similar to the blank sessionDiscriminator argument; the difference
             is that only multiple instances of the client application using myApp started by
             jdoe share the same Teamcenter server instance.
             
Unique     If the user jdoe logs on using a unique
             random-generated string (for example, jdoe/akdk938lakc), the client
             application will be assigned to a dedicated instance of the Teamcenter server.
             



             The scenario you use depends on how your client application is used in the integrated
             environment. The most common case is the unique sessionDiscriminator
             value.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Username: 
                         The user's Teamcenter username.
             
        :param SsoCredentials: 
                         The user's Teamcenter SSO credentials. This should have been obtained from Teamcenter
                         Security Services.
             
        :param Group: 
                         The group id for this session. If blank (""), the user's default group is assumed.
             
        :param Role: 
                         The role the user is performing in the group. If blank (""), the user's default role
                         in the group is assumed.
             
        :param SessionDiscriminator: 
                         Client defined identifier for this session. This argument is ignored when the client
                         application is deployed in a 2Tier environment (IIOP communication).
             
        :return: 
        """
        ...
    def Logout(self) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Logout and terminate the Teamcenter session. If the Teamcenter server is being shared
             with multiple client applications, it will not be terminated until each client has
             issued the logout.
             


Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :return: 
        """
        ...
    def SetSessionGroupMember(self, GroupMember: Teamcenter.Soa.Client.Model.Strong.GroupMember) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Set the Group and Role for the current session. The group and role
             are set at login, either to default values or as specified by the input arguments
             to the login operation. The group and role can be changed at any time throughout
             the session through this operation or the setUserSessionState
             operations. The getSessionGroupMember will
             return the current group and roll.
             

Dependencies:

             getSessionGroupMember
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param GroupMember: 
                         The desired <b>GroupMember</b> for the current session.  The <b>GroupMember</b> defines
                         the <b>Group</b> and <b>Role</b> for the session.
             
        :return: property
             values returned in addition to any properties defined in the object property policy.
        """
        ...

