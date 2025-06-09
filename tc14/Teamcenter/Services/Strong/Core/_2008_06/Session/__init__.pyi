import System
import Teamcenter.Services.Strong.Core._2006_03.Session
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Common
import typing

class GetDisplayStringsOutput:
    """
    The name/value pair of a Text Server key and its corresponding localized value.
    """
    def __init__(self, ) -> None: ...
    Key: str
    """The textserver key."""
    Value: str
    """The localized value for the Text Server key."""

class GetDisplayStringsResponse:
    """
    The response for  the getDisplayStrings operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[GetDisplayStringsOutput]
    """A list Text Server key/localized value pairs."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Partial errors with the key name attached to the partial error."""

class Session:
    """
    Interface Session
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDisplayStrings(self, Info: list[str]) -> GetDisplayStringsResponse:
        """    
             Get the localized text string for each input key from the info array. The input key
             must correspond to a key defined in the Text Server. If the input array is empty,
             the returned array will also be empty.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Info: 
                         A list of Text Server key names.
             
        :return: An array Text Server key/localized value pairs. Any errors encountered while looking
             up a given Text Server key will be returned as a partial error with the key name
             attached to the partial error.
        """
        ...
    def Login(self, Username: str, Password: str, Group: str, Role: str, Locale: str, SessionDiscriminator: str) -> Teamcenter.Services.Strong.Core._2006_03.Session.LoginResponse:
        """    
             Authenticates the user`s credentials and initialize a Teamcenter session for this
             client. The operation will throw an InvalidCredentialsException
             if the username, password
             or group is not valid.
             
             When the client application is deployed to a 4Tier environment (communication through
             HTTP or TCCS) the login operation also contributes
             to the assignment of a Teamcenter server instance to the client session. The Teamcenter
             architecture varies from other client server architectures in that there is a dedicated
             instance of the Teamcenter server per client application. However, there are use
             cases where it is desirable for a single user to have multiple desktop applications
             running and each sharing a single instance of a Teamcenter server. This is controlled
             through the following elements:
             

hostPath    From
             the Connection class constructor, this specifies  the address (URI) the Teamcenter
             server is hosted on.
             
username    From
             this login operation, this specifies the user`s Teamcenter user name.
             
sessionDiscriminator    From
             this login operation, this identifies the client session.
             



             The hostPath argument determines the server
             machine that the client connects to. Once there, the pool manager on that host uses
             the username and sessionDiscriminator
             arguments of the logon request to determine
             which Teamcenter server instance to assign the client to. If the pool manager has
             an existing Teamcenter server instance with the username/sessionDiscriminator key, the client is assigned
             to that existing instance of the Teamcenter server, and therefore sharing the server
             with another client; otherwise, a new instance of the Teamcenter server is used.
             There are a few general scenarios for the sessionDiscriminator
             argument:
             


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
             a unique random generated string (for example, jdoe/akdk938lakc), the
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
                         The user`s Teamcenter user name. This is case insensitive (<i>jdoe</i> or <i>JDOE</i>)
             
        :param Password: 
                         The user`s Teamcenter password.
             
        :param Group: 
                         The group ID for this session. If null, the user`s default group is assumed.
             
        :param Role: 
                         The role the user is performing in the group. If null, the user`s default role in
                         the group is assumed.
             
        :param Locale: 
                         The locale to be used by the Teamcenter server process for this session. If null,
                         the server`s default locale will be used.
             
        :param SessionDiscriminator: 
                         Client defined identifier for this session. This argument is ignored when the client
                         application is deployed in a 2Tier environment (IIOP communication).
             
        :return: 
        """
        ...
    def LoginSSO(self, Username: str, SsoCredentials: str, Group: str, Role: str, Locale: str, SessionDiscriminator: str) -> Teamcenter.Services.Strong.Core._2006_03.Session.LoginResponse:
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
             
hostPath    From the
             Connection class constructor, this specifies  the address (URI) the Teamcenter server
             is hosted on.
             
username    From this
             login operation, this specifies the user's Teamcenter user name.
             
sessionDiscriminator    From
             this login operation, this identifies the client session.
             

             The hostPath argument determines the server
             machine that the client connects to. Once there, the pool manager on that host uses
             the username and sessionDiscriminator
             arguments of the login request to determine which Teamcenter server instance to assign
             the client to. If the pool manager has an existing Teamcenter server instance with
             the username/sessionDiscriminator
             key, the client is assigned to that existing instance of the Teamcenter server, and
             therefore sharing the server with another client; otherwise, a new instance of the
             Teamcenter server is used. There are a few general scenarios for the sessionDiscriminator argument:
             


Blank     If the user jdoe logs on to Teamcenter
             using two or more client applications using a blank sessionDiscriminator argument
             (for example, jdoe/ ), all of those clients are assigned to the same Teamcenter
             server instance. These client applications can be running on the same or different
             client hosts.
             
Constant     If
             the user jdoe logs on to Teamcenter using two or more client applications using a
             constant or fixed sessionDiscriminator argument (for example, jdoe/MyApp
             ), those clients are assigned to the same Teamcenter server instance. This is similar
             to the blank sessionDiscriminator argument;
             the difference is that only multiple instances of the client application using myApp
             started by jdoe share the same Teamcenter server instance.
             
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
                         The group id for this session (optional). If NULL, the user's default group is assumed.
             
        :param Role: 
                         The role the user is performing in the group (optional). If NULL, the user's default
                         role in the group is assumed.
             
        :param Locale: 
                         The locale to be used by the Teamcenter server process for this session (optional).
                         If NULL, the server's default locale will be used.
             
        :param SessionDiscriminator: 
                         Client defined identifier for this session. This argument is ignored when the client
                         application is deployed in a 2Tier environment (IIOP communication).
             
        :return: 
        """
        ...
    def SetObjectPropertyPolicy(self, Policy: Teamcenter.Soa.Common.ObjectPropertyPolicy) -> str:
        """    
             Sets the current object property policy. The business logic of a service operation
             determines what business objects are returned, while the object property policy determines
             which properties are returned on each business object instance.  This allows the
             client application to determine how much or how little data is returned based on
             how the client application uses those returned business objects. The policy is applied
             uniformly to all service operations.
             
             By default, all applications use the Default object property policy, defined
             on the Teamcenter server $TC_DATA/soa/policies/default.xml.
             It is this policy that is applied to all service operation responses until the client
             application changes the policy. Siemens PLM Software strongly recommends that all
             applications change the policy to one applicable to the client early in the session.
             
             The object property policy will stay in affect for this session until changed by
             another call to setObjectPRopertyPolicy.
             The current policy can be modified with calls to updatObjectPropertyPolicy.
             

             Like any other service operation, this operation cannot be called before establishing
             a session with the login serivce operation,
             so if you need a policy other than the Default policy for the business objects
             returned by the login operation, use the
             _2011_06 version of the login/loginSso operation
             to authenticate and establish a session without returning business objects. The setObjectPropertyPolicy operation can then be called
             to establish the policy for the session.
             

Dependencies:

             updateObjectPropertyPolicy
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Policy: 
                         The object property policy.
             
        :return: .
        """
        ...

