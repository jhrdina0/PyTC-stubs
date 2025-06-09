import System
import System.Collections
import Teamcenter.Schemas.Soa._2011_06.Metamodel
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Common
import typing

class ClientCacheInfo:
    """
    Data for the requested cached features.
    """
    def __init__(self, ) -> None: ...
    Features: list[Feature]
    """The list of  features."""
    PartialErrors: Teamcenter.Soa.Client.Model.PartialErrors
    """
            Errors are return for features that do not exist or if there are other errors in
            getting data for a given service. The client ID in the partial error will be that
            of the feature name.
            """

class Credentials:
    """
    The credentials needed to authenticate a user.
    """
    def __init__(self, ) -> None: ...
    User: str
    """The user's Teamcenter user name."""
    Password: str
    """The user's Teamcenter password or SSO token."""
    Group: str
    """The group ID for this session. If blank (""), the user's default group is assumed."""
    Role: str
    """
            The role the user is performing in the group. If blank (""), the user's default role
            in the group is assumed.
            """
    Locale: str
    """
            The locale to be used by the Teamcenter server process for this session. If blank
            (""), the server's default locale will be used.
            """
    Descrimator: str
    """
            Client defined identifier for this session. This argument is ignored when the client
            application is deployed in a 2Tier environment (IIOP communication).
            """

class Feature:
    """
    Information for a single client cache feature.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Name of the feature,  ClientMetaModel or TextData."""
    CacheTickets: System.Collections.Hashtable
    """
            A map of Dataset names and FMS tickets (string/string) for each Dataset
            that makes up the client cache feature.
            """

class LoginResponse:
    """
    
            Basic information about the server and  partial errors are returned when the authentication
            is successful but requested role or locale is not supported.
            
    """
    def __init__(self, ) -> None: ...
    ServerInfo: System.Collections.Hashtable
    """
            Name/Value pairs (string/string) of data related to the server. The following keys
            are valid:
            

Version         The version of the Teamcenter server.
            
HostName     The name of the Teamcenter server's host machine.
            
LogFile         The full path of the Teamcenter server's log
            file.
            
Locale          The locale of this session.
            
TcServerID    The unique ID of this instance of the Teamcenter
            server.
            

"""
    PartialErrors: Teamcenter.Soa.Client.Model.PartialErrors
    """Partial errors or warnings resulting from the login attempt."""

class Session:
    """
    Interface Session
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetClientCacheData(self, Features: list[str]) -> ClientCacheInfo:
        """    
             This operation returns information required to maintain a client cache. The Teamcneter
             server maintains a set of Datasets with static or near static data that is
             pertainant to a client application.  This static data can be downloaded through FMS
             to the cleint host one time, and available for each subsequent client session, thus
             improving the overall performance of the client application. These Datasets are updated
             as part of the deploy process from the BMIDE. The cleint cache consits of serveral
             features, each of these features can be used independnatly of each other. The following
             features are available:
             


ClientMetaModel :The is the client side version of the server`s Meta
             Model. This includes type descriptions, property descriptions, List Of Values data,
             and Dataset tool data. The use of the ClientMetaModel cache replaces the need to
             use the getTypeDescriptions  service calls. By setting the Connection.setOption(OPT_USE_CLIENT_META_MODEL_CACHE,
             true), the SOA client framework will use the cache for Client  Meta Model
             data. The SOA client framework takes care of calling this service opeation and FMS
             to populate the cache. This feature includes the Dataset:Types, Lov, ToolsData,
             types_local (one for each locale i.e types_en_US), lov_local (one for
             each locale i.e lov_en_US).
             
TextData: This contains the localized string available in the Teamcenter
             server's Text Server. Using the localized data from this cache replaces the need
             to call the getDisplayStrings service operation.
             



Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Features: 
                         Names of features to return<i>, All</i> to return data for all features. Available
                         features are <i>ClientMetaModel</i> and <i>TextData</i>.
             
        :return: Feature descriptions
        """
        ...
    def GetTypeDescriptions(self, TypeNames: list[str]) -> Teamcenter.Schemas.Soa._2011_06.Metamodel.TypeSchema:
        """    
             Get the Meta data for the named Business Model object types. This includes type and
             property descriptions and LOV information.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param TypeNames: 
                         List of Business Model Object type names.
             
        :return: The Meta data for the named types.
        """
        ...
    def Login(self, Credentials: Credentials) -> LoginResponse:
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
             

hostPath    From the Connection class constructor,
             this specifies  the address (URI) the Teamcenter server is hosted on.
             
username    From this login operation, this specifies
             the user's Teamcenter user name.
             
sessionDiscriminator    From this login operation,
             this identifies the client session.
             



             The hostPath argument determines the server
             machine that the client connects to. Once there, the pool manager on that host uses
             the username and sessionDiscriminator
             arguments of the login request to determine which Teamcenter server instance to assign
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
             
        :param Credentials: 
                         The user's Teamcenter credentials
             
        :return: 
        """
        ...
    def LoginSSO(self, Credentials: Credentials) -> LoginResponse:
        """    
             Authenticates the user using Single-Sign-On (SSO) credentials and initialize a Teamcenter
             session for this client. The username and
             password arguments must be obtained from
             Teamcenter's Security Services. The SsoCredentials
             class offers a simple API to get these values. The operation will throw an InvalidCredentialsException if the user, password or group is not valid.
             
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
             
        :param Credentials: 
                         The user's Teamcenter credentials.
             
        :return: 
        """
        ...
    def UpdateObjectPropertyPolicy(self, PolicyID: str, AddProperties: list[Teamcenter.Soa.Common.PolicyType], RemoveProperties: list[Teamcenter.Soa.Common.PolicyType]) -> str:
        """    
             Update the named policy, adding and removing the named properties. This operation
             only applies to object property policies that have been defined on the client side.
             

Dependencies:

             setObjectPropertyPolicy
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param PolicyID: 
                         The ID of the policy to update. This is the ID that is returned from the <font face="courier" height="10">setObjectPropetyPolicy</font> operation.
             
        :param AddProperties: 
                         List of properties to add to the named policy.  If the property already exists in
                         the policy, the flags (i.e. <font face="courier" height="10">excludeUiValues</font>)
                         from the input will take precedence over the flags on the existing property.
             
        :param RemoveProperties: 
                         List of properties to remove from the named policy. If a source <font face="courier" height="10">PolicyType</font> defines a type without properties, the whole type is
                         removed.
             
        :return: The policy ID, will be the same as the input ID.
        """
        ...

