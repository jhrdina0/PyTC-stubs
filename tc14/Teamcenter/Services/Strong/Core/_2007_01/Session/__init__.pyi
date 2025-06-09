import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetTCSessionInfoResponse:
    """
    Data structure representing the different current user's Teamcenter session information.
    """
    def __init__(self, ) -> None: ...
    ServerVersion: str
    """The version of the server."""
    TransientVolRootDir: str
    """Path to the root folder of the transient volume."""
    IsInV7Mode: bool
    """True if the server is operating in V7 mode."""
    ModuleNumber: int
    """This element is not to be used anymore and always returns a -1."""
    User: Teamcenter.Soa.Client.Model.Strong.User
    """The User object for this session."""
    Group: Teamcenter.Soa.Client.Model.Strong.Group
    """The Group object for this session."""
    Role: Teamcenter.Soa.Client.Model.Strong.Role
    """The Role object for this session."""
    TcVolume: Teamcenter.Soa.Client.Model.Strong.ImanVolume
    """The ImanVolume object for this session."""
    Project: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """The Project object for this session."""
    WorkContext: Teamcenter.Soa.Client.Model.Strong.TC_WorkContext
    """The WorkContext object for this session."""
    Site: Teamcenter.Soa.Client.Model.Strong.POM_imc
    """The site object for this session"""
    Bypass: bool
    """True if bypass is enabled."""
    Journaling: bool
    """True if journaling is enabled."""
    AppJournaling: bool
    """True if application journaling is enabled."""
    SecJournaling: bool
    """True if sec journaling is enabled."""
    AdmJournaling: bool
    """True if administration journaling is enabled."""
    Privileged: bool
    """True if the user is privileged."""
    IsPartBOMUsageEnabled: bool
    """True if the Part BOM Usage is enabled."""
    IsSubscriptionMgrEnabled: bool
    """True if the Subscription Manager is enabled."""
    TextInfos: list[TextInfo]
    """textInfos"""
    ExtraInfo: System.Collections.Hashtable
    """
            Map of kev/value pairs (string/string).The following keys are returned:
            

TcServerIDUnique  ID of this Teamcenter server instance.
            
systemTypeType  of server, always 'Teamcenter'.
            
syslogFile  The absolute path of the system log file (.syslog)
            on the server host.
            
Hostname  The host name of the machine hosting the Teamcenter
            server process.
            
TCServerLocale The locale of the Teamcenter server.
            
currentOrganization The UID of the user's current Organization.
            The business object instance is in the ServiceData plain list
            
loginGroupOrganization  The UID of the user's login Organization.
            The business object instance is in the ServiceData plain list
            
currentChangeNotice  The UID of the user's current ChangeNotice
            The business object instance is in the ServiceData plain list
            
locationCodePref  The preferred location code.
            
displayCurrentCountryPage  True if the current country selection
            page is needed.
            

"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""

class MultiPreferencesResponse:
    """
    Multiple Preferences Response
    """
    def __init__(self, ) -> None: ...
    Preferences: list[ReturnedPreferences]
    """List of Returned Preferences"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The successful Object ids, partial errors and failures"""

class ReturnedPreferences:
    """
    Info for one preference
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The preference name."""
    Scope: str
    """The scope of the preference, "all", "site", "user", "group", or "role"."""
    Values: list[str]
    """The values for the perference."""

class ScopedPreferenceNames:
    """
    Info for getPreferences
    """
    def __init__(self, ) -> None: ...
    Scope: str
    """The scope of the preference, "all", "site", "user", "group", or "role"."""
    Names: list[str]
    """The names of the perferences."""

class TextInfo:
    """
    Text Information
    """
    def __init__(self, ) -> None: ...
    RealName: str
    """Real Name"""
    DisplayName: str
    """Display Name"""

class Session:
    """
    Interface Session
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPreferences(self, RequestedPrefs: list[ScopedPreferenceNames]) -> MultiPreferencesResponse:
        """    
             Get preference values.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param RequestedPrefs: 
                         vector of PrefSetting structures, which specify the scope name for each of the preferences
                         to be set.
             
        :return: A PreferencesResponse structure. The preference names and values are returned in
             the preferences element. If no preference with the given name exists, no error is
             raised and no value is returned. Any other errors are returned in the serviceData
             element. ServiceException thrown if the named policy does not exist or if there are
             errors in setting this policy.
        """
        ...
    def GetTCSessionInfo(self) -> GetTCSessionInfoResponse:
        """    
             This operation gets information about the current user's Teamcenter session. This
             will return more detail session information than the login service operation including
             User, Group, Role, Site, Volume, Project, and
             WorkContext.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :return: 
        """
        ...
    def SetObjectPropertyPolicy(self, PolicyName: str) -> bool:
        """    
             Sets the current object property policy. The business logic of a service operation
             determines what business objects are returned, while the object property policy determines
             which properties are returned on each business object instance. This allows the client
             application to determine how much or how little data is returned based on how the
             client application uses those returned business objects. The policy is applied uniformly
             to all service operations.
             
             By default, all applications use the Default object property policy, defined
             on the Teamcenter server $TC_DATA/soa/policies/default.xml.
             It is this policy that is applied to all service operation responses until
             the client application changes the policy. Siemens PLM Software strongly recommends
             that all applications change the policy to one applicable to the client early in
             the session.
             
             The object property policy is set to the policy named in the file $TC_DATA/soa/policies/<policyName>.xml The reserved policy
             name "Empty", will enforce a policy that only returns minimum data required
             for each object (UID and type name).The object property policy will stay in affect
             for this session until changed by another call to setObjectPRopertyPolicy.
             


             Like any other service operation, this operation cannot be called before establishing
             a session with the login serivce operation,
             so if you need a policy other than the Default policy for the business objects
             returned by the login operation, use the
             _2011_06 version of the login/loginSso operation
             to authenticate and establish a session without returning business objects. The setObjectPropertyPolicy operation can then be called
             to establish the policy for the session.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param PolicyName: 
                         The name of the policy file without the <font face="courier" height="10">.xml </font>extension.
                         The file must exist on the Teamcenter server volume at <font face="courier" height="10">$TC_DATA\soa\policies\&lt;policyName&gt;.xml.</font>

        :return: True if the object property policy is successfully set to the named policy.
        """
        ...

