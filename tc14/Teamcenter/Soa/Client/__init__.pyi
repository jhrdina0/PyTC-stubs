import System
import System.Collections
import System.Collections.Generic
import System.IO
import System.Net
import System.Runtime.Serialization
import Teamcenter.Net.TcServerProxy.Admin
import Teamcenter.Net.TcServerProxy.Client
import Teamcenter.Schemas.Soa._2006_03.Exceptions
import Teamcenter.Services.Loose.Core._2006_03.FileManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Common
import Teamcenter.Soa.Exceptions
import Teamcenter.Soa.Internal.Client
import typing

class AbstractCredentialManager:
    CLIENT_CREDENTIAL_TYPE_SSO: int
    """Client credential type for SSO is set to 1."""
    CLIENT_CREDENTIAL_TYPE_STD: int
    """CLIENT credentail type for std is set to 2."""
    CredentialType: int
    """Get the CredentialType."""
    def get_CredentialType(self) -> int: ...
    @typing.overload
    def GetCredentials(self, invalidCredentials: Teamcenter.Schemas.Soa._2006_03.Exceptions.InvalidCredentialsException) -> list[str]: ...
    @typing.overload
    def GetCredentials(self, invalidUser: Teamcenter.Schemas.Soa._2006_03.Exceptions.InvalidUserException) -> list[str]: ...
    def SetUserPassword(self, user: str, password: str, discriminator: str) -> None:
        """    
            Set username,password and the session discriminator.
            
        :param user: Username
        :param password: Password.
        :param discriminator: Session Discriminator.
        :return: 
        """
        ...
    def SetGroupRole(self, group: str, role: str) -> None:
        """    
            Set the group and role.
            
        :param group: group of the current user.
        :param role: role of the current user.
        :return: 
        """
        ...

class Connection:
    """
    
The Connection class is used to store all the information used to connect
a client application to the Teamcenter Server. This class also manages the
client's
session with the Teamcenter server.
    """
    @typing.overload
    def __init__(self, hostPath: str, cookieCollection: System.Net.CookieCollection, credentialManager: CredentialManager, binding: str, protocol: str, useCompression: bool) -> None: ...
    @typing.overload
    def __init__(self, credentialManager: CredentialManager, fileName: str) -> None: ...
    OPT_USE_COMPRESSION: str
    """Use GZip compression on the service HTTP response"""
    OPT_READ_WRITE_TIMEOUT: str
    """The number of milliseconds before the writing or reading to the HTTP stream times out"""
    OPT_TIMEOUT: str
    """The number of milliseconds to wait for the HTTP response"""
    OPT_SERVER_REASSIGNMENT: str
    """Enable server reassignment notification"""
    OPT_CACHE_MODEL_OBJECTS: str
    """Cache Client Data Model objects"""
    WEBSEAL_FORM_URL: str
    """* WebSeal URL."""
    OPT_SSO_LOGIN_URL: str
    """* SSO Login URL."""
    TCCS_ENV_NAME: str
    """The TCCS environment name to which the client application wants to connect"""
    TCCS_HOST_URL: str
    """Teamcenter server URL specified by client application"""
    TCCS_USE_CALLBACK: str
    """Specify whether calllback to client is needed for forward proxy with TCCS"""
    TCCS_SESSION_ID: str
    """Member TCCS_SESSION_ID"""
    OPT_SHARED_EVENTS: str
    """Share events when sharing a server."""
    OPT_SHARED_DISCRIMINATOR: str
    """Use shared discriminator to share a server."""
    OPT_USE_CLIENT_META_MODEL_CACHE: str
    """Retrieve Meta Model information from cached files in FMS """
    JSON_TUNNEL_BINDING: str
    """Identify an alternate sender implementation which may be obtained. """
    ExceptionHandler: ExceptionHandler
    """The handler for processing Exceptions."""
    Binding: str
    """The binding"""
    Cookies: System.Net.CookieCollection
    """The Cookie Manager"""
    HostPath: str
    """The host path"""
    EventSharer: EventSharer
    """The EventSharer"""
    ModelManager: Teamcenter.Soa.Client.Model.ModelManager
    """The ModelManager"""
    ClientDataModel: Teamcenter.Soa.Client.Model.ClientDataModel
    """The Client Data Model"""
    ClientMetaModel: Teamcenter.Soa.Client.Model.ClientMetaModel
    """The Client Meta Model"""
    CredentialManager: CredentialManager
    """ The CredentialManager."""
    Protocol: str
    """ The protocol"""
    Sender: Teamcenter.Soa.Internal.Client.Sender
    """ The sender."""
    ObjectPropertyPolicyManager: ObjectPropertyPolicyManager
    """  
            The Object Property Policy Manager.
            """
    CurrentObjectPropertyPolicy: str
    """  
            The current Object Property Policy.
            """
    PreviousObjectPropertyPolicy: str
    """
            The previous Object Property Policy.
            """
    ClientVersion: Teamcenter.Soa.Common.Version
    """ The version of the client libraries """
    ServerVersion: Teamcenter.Soa.Common.Version
    """The server version"""
    Locale: str
    """The session locale"""
    SiteLocale: str
    """The site locale"""
    def Serialize(self, fileName: str) -> None:
        """    
             Serialize and output connection object values to a named file.
            
        :param fileName:  NName of the output file name with directory path. 
        :return: 
        """
        ...
    def get_ExceptionHandler(self) -> ExceptionHandler: ...
    def set_ExceptionHandler(self, value: ExceptionHandler) -> None: ...
    @staticmethod
    def AddRequestListener(listener: RequestListener) -> None:
        """    
            Add a RequestListener to the service call stack.
            Each listener that is added, will recieve a callback for each service 
            request send and recieved. The callback will have inforatmion about the 
            service request, name of the service and operation, the XML document .etc.
            
        :param listener: Instance of the RequestListener interface.
        :return: 
        """
        ...
    @staticmethod
    def RemoveRequestListener(listener: RequestListener) -> None:
        """     
            Remove the RequestListener from the service call stack
            
        :param listener: Instance of the RequestListner to remove.
        :return: 
        """
        ...
    def get_Binding(self) -> str: ...
    def get_Cookies(self) -> System.Net.CookieCollection: ...
    def get_HostPath(self) -> str: ...
    def get_EventSharer(self) -> EventSharer: ...
    def get_ModelManager(self) -> Teamcenter.Soa.Client.Model.ModelManager: ...
    def get_ClientDataModel(self) -> Teamcenter.Soa.Client.Model.ClientDataModel: ...
    def get_ClientMetaModel(self) -> Teamcenter.Soa.Client.Model.ClientMetaModel: ...
    def get_CredentialManager(self) -> CredentialManager: ...
    def set_CredentialManager(self, value: CredentialManager) -> None: ...
    def get_Protocol(self) -> str: ...
    def get_Sender(self) -> Teamcenter.Soa.Internal.Client.Sender: ...
    def GetAlternateSender(self, altBinding: str) -> Teamcenter.Soa.Internal.Client.Sender:
        """    
            Method to provide access to an alternate sender implmentation.
            
        :param altBinding: Which alternate binding to request.
        :return: Sender implementation or null if not able to satisfy the request.
        """
        ...
    def getServerAddress(self) -> str:
        """    
            The server's URL address as defined in HostPath when in HTTP mode or from the TCCS environment definition
            
        :return: 
        """
        ...
    def get_ObjectPropertyPolicyManager(self) -> ObjectPropertyPolicyManager: ...
    def get_CurrentObjectPropertyPolicy(self) -> str: ...
    def get_PreviousObjectPropertyPolicy(self) -> str: ...
    def GetObjectPropertyPolicy(self, name: str) -> Teamcenter.Soa.Common.ObjectPropertyPolicy:
        """    
            Get the dynamic Property Policy.
            
        :param name: Name of the policy which needs to retrived
        :return: Dynamic property policy if the named policy exists.Else Null
        """
        ...
    def get_ClientVersion(self) -> Teamcenter.Soa.Common.Version: ...
    def get_ServerVersion(self) -> Teamcenter.Soa.Common.Version: ...
    def get_Locale(self) -> str: ...
    def get_SiteLocale(self) -> str: ...
    def SetObjectPropertyPolicy(self, policyName: str) -> None:
        """    
            Sets the Object Property Policy. 
            
        :param policyName: Name of the policy. 
        :return: 
        """
        ...
    def SetObjectPropertyPolicyPerThread(self, policyName: str) -> None:
        """    
             Sets the Object Property Policy for service request made on this thread.
            
        :param policyName: Name of the policy. 
        :return: 
        """
        ...
    def ClearObjectPropertyPolicyPerThread(self) -> None:
        """    
             Clears the Object Property Policy set for this thread.
            
        :return: 
        """
        ...
    def SetOption(self, optionName: str, value: str) -> None: ...
    def GetOption(self, optionName: str) -> str:
        """    
            Get the value of a connection option.
            
        :param optionName: Name of the option 
        :return: The value of the option
        """
        ...
    def SetApplicationName(self, appName: str) -> None:
        """    
             Sets the application name to be passed to the TcServer in the request envelope.
             This value is reported by software analytics if enabled
            
        :param appName: The name of the application that will be reported to the analytics server
        :return: 
        """
        ...
    def SetApplicationVesrion(self, appVersion: str) -> None:
        """    
             Sets the application version to be passed to the TcServer in the request envelope.
             This value is reported by software analytics if enabled
            
        :param appVersion: The version of the application that will be reported to the analytics server
        :return: 
        """
        ...
    def getSessionState(self) -> System.Collections.Hashtable:
        """    
             Gets map<string,string> with client's session state data.
            
        :return: 
        """
        ...
    def SetProxyCredentialProvider(self, credProvider: Teamcenter.Net.TcServerProxy.Client.CredentialProvider) -> None:
        """    
            Set the Credential Provider for Forward Proxy Challenges
            
        :param credProvider: Credential Provider
        :return: 
        """
        ...
    def GetProxyCredentialProvider(self) -> Teamcenter.Net.TcServerProxy.Client.CredentialProvider:
        """    
            Retrieve the Credential Provider for Forward Proxy Challenges
            
        :return: 
        """
        ...
    def GetTSPSession(self) -> Teamcenter.Net.TcServerProxy.Client.TSPSession:
        """    
            Get Instance Of TSP Session
            
        :return: 
        """
        ...
    @staticmethod
    def getEnvironments() -> System.Collections.ArrayList:
        """    
             Returns an ArrayList  containg list of all environments defined in TCCS configuration.
             
        :return: 
        """
        ...
    @staticmethod
    def getEnvsForVersion(expression: str) -> System.Collections.ArrayList:
        """    
             Gets list of  TCCS environment matching the version expression.
             
        :param expression: corresponds to version defined in TCCS environment. Mutliple versions can be specified
             in the expression using OR separator for example '8.3|9.0'. Wild card '*' can be specified at the end of
             input string.
        :return: list of TCCS Environments matching the input expression.    ArrayList<Environment>
        """
        ...
    @staticmethod
    def getEnvironment(envName: str) -> Teamcenter.Net.TcServerProxy.Admin.Environment:
        """    
             Get TCCS environment based on environment Name
             
        :param envName: TCCS environment object corresponding to environment Name
        :return: TCCS environment based on environment Name
        """
        ...
    @staticmethod
    def getEnvironmentsForURL(URL: str) -> System.Collections.ArrayList:
        """    
              Gets list of  TCCS environment matching the input URL.
             
        :param URL: corresponds to server URL defined in TCCS environment.
        :return: Environment List
        """
        ...
    def TccsShutdownServer(self) -> None:
        """    
              Shuts down tcservers launched by TCCS. Works in 2Tier TCCS mode.
             
        :return: 
        """
        ...
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """    
            This method is invoked internally when binary serialization is executed.
            
        :param info: Adds the information to be get serialized.
        :param context: StreamingContext, not useful for current work but 
            need to keep as an argument for function signature
        :return: 
        """
        ...
    def OnDeserialization(self, sender: typing.Any) -> None:
        """    
            This method is invoked internally when binary deserialization is executed.
            
        :param sender: 
        :return: 
        """
        ...

class CredentialManager:
    """
    
This interface is used by the SOA Client Framework to get the authentication
credentials from the client application.
    """
    def __init__(self , *args: typing.Any) -> None: ...
    CredentialType: int
    """
            Returns the type of credentials supplied by this Credential Manager.
            Valid types are SSO (1), Standard (2), Sponsored (3) and Sponsored SSO (4). 
            """
    def get_CredentialType(self) -> int: ...
    @typing.overload
    def GetCredentials(self, invalidCredentials: Teamcenter.Schemas.Soa._2006_03.Exceptions.InvalidCredentialsException) -> list[str]: ...
    @typing.overload
    def GetCredentials(self, invalidUser: Teamcenter.Schemas.Soa._2006_03.Exceptions.InvalidUserException) -> list[str]: ...
    def SetUserPassword(self, user: str, password: str, discriminator: str) -> None:
        """     
            This method is called by the SOA client framework when a login service
            request is issued to the server. This gives the implementing class the
            option to cache the Username and Password, so a latter re-authentication
            attempts can be made silently.
            
        :param user: login user
        :param password: login password
        :param discriminator: optional sessionDiscriminator to discriminate one session from another in server
        :return: 
        """
        ...
    def SetGroupRole(self, group: str, role: str) -> None:
        """     
            This method is called by the SOA client framework when a login or
            change group/role service request is issued to the server. This gives
            the implementing class the option to cache the Group and Role, so  latter
            re-authentication attempts can be made silently.
            
        :param group: Login Group
        :param role: Login Role 
        :return: 
        """
        ...

class SponsoredCredentials:
    def __init__(self , *args: typing.Any) -> None: ...
    def SetSponsoredUser(self, spndUser: str) -> None:
        """     
            This method is called by the SOA client to set the sponsored user for
            login in sponsored mode. This provides the implementing class the option to set sponsored user id.
            
        :param spndUser: sponsored user id
        :return: 
        """
        ...
    def SetLocale(self, locale: str) -> None:
        """     
            This method is called by the SOA client to set the locale to be used. This provides
            the implementing class the option to set the locale used in login.
            
        :param locale: Locale
        :return: 
        """
        ...

class DefaultExceptionHandler:
    """
    
Default implementation of the ExceptionHandler interface.
    """
    def __init__(self, ) -> None: ...
    @typing.overload
    def HandleException(self, ise: Teamcenter.Schemas.Soa._2006_03.Exceptions.InternalServerException) -> None: ...
    @typing.overload
    def HandleException(self, coe: Teamcenter.Soa.Exceptions.CanceledOperationException) -> None: ...

class EventSharer:
    """
    
This interface is used by the SOA Client Framework to invoking methods involving
shared events.
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def IsEventSharingFunctioning(self) -> bool:
        """    
            This method contacts TCCS to determine if event sharing is functioning.
            was previously not working (e.g. TCCS down), this method will retry and if
            event sharing is now available, it will (re)establish this user with it.
            If this attempt to (re)establish fails, SessionHandler.handleException will be invoked,
            It can be called even if the user has not yet logged in.  If event sharing
            was previously not working (e.g. TCCS down), this method will retry and if
            event sharing is now available, it will (re)establish this user with it.
             assuming the application has registered one with the Connection.
            
        :return: 
        """
        ...
    def IsServerShared(self) -> bool:
        """    Check if the server is Shared by clients.
        :return: 
        """
        ...
    def ProcessSharedEvents(self) -> None:
        """    
            This method can be called by application clients that wish to "poll"
            for shared events rather than wait for next service call to obtain them.
            If there are problems accessing the TCCS event sharing system,
            SessionHandler.handleException will be invoked,
            assuming the application has registered one with the Connection.
            
        :return: 
        """
        ...

class ExceptionHandler:
    """
    
This interface is used by the SOA Client Framework to to provide a common means
of handling exceptions.
    """
    def __init__(self , *args: typing.Any) -> None: ...
    @typing.overload
    def HandleException(self, ise: Teamcenter.Schemas.Soa._2006_03.Exceptions.InternalServerException) -> None: ...
    @typing.overload
    def HandleException(self, coe: Teamcenter.Soa.Exceptions.CanceledOperationException) -> None: ...

class FMS_Progress_Callback(System.MulticastDelegate):
    def __init__(self, object: typing.Any, method: System.IntPtr) -> None: ...
    def Invoke(self, uid: str, args: typing.Any, bytesDownloaded: int, bytesFileSize: int, continueDownload: bool) -> int: ...
    def BeginInvoke(self, uid: str, args: typing.Any, bytesDownloaded: int, bytesFileSize: int, continueDownload: bool, callback: System.AsyncCallback, object: typing.Any) -> System.IAsyncResult: ...
    def EndInvoke(self, continueDownload: bool, result: System.IAsyncResult) -> int: ...

class FileManagementUtility:
    """
    
Provide for integration with FMS upload/download for files,
making FMS as transparent as possible to the caller.
    """
    @typing.overload
    def __init__(self, connection: Connection) -> None: ...
    @typing.overload
    def __init__(self, connection: Connection, clientIPAddress: str, assignedFSCURIs: list[str], bootstrapFSCURIs: list[str], cacheDir: str) -> None: ...
    def Term(self) -> None:
        """    
            When finished using this utility class, the Term() method should be
            called to allow FMS to close unused connections.
            
        :return: 
        """
        ...
    @typing.overload
    def GetFiles(self, files: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetFileResponse: ...
    @typing.overload
    def GetFiles(self, files: list[Teamcenter.Soa.Client.Model.ModelObject], cb: FMS_Progress_Callback, callbackContext: typing.Any) -> GetFileResponse: ...
    @typing.overload
    def GetFiles(self, fmsTickets: list[str]) -> list[System.IO.FileInfo]: ...
    @typing.overload
    def GetFiles(self, fmsTickets: list[str], cb: FMS_Progress_Callback, callbackContext: typing.Any) -> list[System.IO.FileInfo]: ...
    @typing.overload
    def GetFile(self, fmsTicket: str) -> System.IO.FileInfo: ...
    @typing.overload
    def GetFile(self, fmsTicket: str, cb: FMS_Progress_Callback, callbackContext: typing.Any) -> System.IO.FileInfo: ...
    def GetFileToLocation(self, file: Teamcenter.Soa.Client.Model.ModelObject, destinationFilePath: str, cb: FMS_Progress_Callback, callbackContext: typing.Any) -> GetFileResponse:
        """    
            Combination of the GetFiles and GetTransientFile logic.  Allows the caller
            to provide the destination file path (directory and file name) for the downloaded
            file.  This is limited to a single file at a time due to specification of the destination.
            
        :param file: namedReference model object
        :param destinationFilePath: local filesystem destination for the file.
        :param cb: FMS Progress callback delegate
        :param callbackContext: callback context - passthru
        :return: response object with file information
        """
        ...
    @typing.overload
    def PutFiles(self, inputs: list[Teamcenter.Services.Loose.Core._2006_03.FileManagement.GetDatasetWriteTicketsInputData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def PutFiles(self, inputs: list[Teamcenter.Services.Loose.Core._2006_03.FileManagement.GetDatasetWriteTicketsInputData], cb: FMS_Progress_Callback, callbackContext: typing.Any) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def PutFileViaTicket(self, writeTicket: str, localFile: System.IO.FileInfo) -> Teamcenter.Soa.Client.Model.ErrorStack: ...
    @typing.overload
    def PutFileViaTicket(self, writeTicket: str, localFile: System.IO.FileInfo, cb: FMS_Progress_Callback, callbackContext: typing.Any) -> Teamcenter.Soa.Client.Model.ErrorStack: ...
    @typing.overload
    def GetTransientFile(self, fmsTicket: str, destinationFilePath: str) -> System.IO.FileInfo: ...
    @typing.overload
    def GetTransientFile(self, fmsTicket: str, destinationFilePath: str, cb: FMS_Progress_Callback, callbackContext: typing.Any) -> System.IO.FileInfo: ...

class GetFileResponse:
    """
    
Data structure for use with FileManagementUtility methods
    """
    def __init__(self, ) -> None: ...
    def SetFiles(self, files: list[System.IO.FileInfo]) -> None:
        """    
            initialize file info.
            
        :param files: files
        :return: 
        """
        ...
    def AddPartialError(self, partialError: Teamcenter.Soa.Client.Model.ErrorStack) -> None:
        """    
            Add the partial errors.
            
        :param partialError: contains partial errors
        :return: 
        """
        ...
    def SizeOfPartialErrors(self) -> int:
        """    
            Get the size of partial errors.
            
        :return: 
        """
        ...
    def GetPartialError(self, index: int) -> Teamcenter.Soa.Client.Model.ErrorStack:
        """    
            Get the partial errors
            
        :param index: index to return appropriate ErrorStack
        :return: ErrorStack for the given index
        """
        ...
    def SizeOfFiles(self) -> int:
        """    
            Get the size of files
            
        :return: 
        """
        ...
    def GetFiles(self) -> list[System.IO.FileInfo]:
        """    
            Get the files
            
        :return: 
        """
        ...
    def GetFile(self, index: int) -> System.IO.FileInfo:
        """    
            Get the file
            
        :param index: index to get file information
        :return: information about perticular file
        """
        ...

class FSCStreamingUtility:
    """
    
Provide for integration with FMS upload/download for files,
making FMS as transparent as possible to the caller.
    """
    def __init__(self, connection: Connection, clientIPAddress: str, assignedFSCURIs: list[str], bootstrapFSCURIs: list[str]) -> None: ...
    def Term(self) -> None:
        """    
            When finished using this utility class, the Term() method should be
            called to allow FMS to close unused connections.
            
        :return: 
        """
        ...
    def Download(self, files: list[Teamcenter.Soa.Client.Model.ModelObject], downloadStreams: list[System.IO.Stream]) -> None:
        """    
             DownLoads the files from volume    
             Limit the array of downloadStreams to 10 to avoid potential problems
             
        :param files: Array  of file objects.
        :param downloadStreams: Array of OutputStream of all the files being down loaded.
        :return: 
        """
        ...
    def Upload(self, inputs: list[Teamcenter.Services.Loose.Core._2006_03.FileManagement.GetDatasetWriteTicketsInputData], uploadStreams: list[System.IO.Stream], streamLength: list[int]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             UpLoads the files to volume
             Limit the array of uploadStreams to 10 to avoid potential problems
             
        :param inputs: Array of Write tickets to files being uploaded.
        :param uploadStreams: Array of InputStream to all the files being uploaded.
        :param streamLength:  Array of file sizes if all the files being uploaded..
        :return: ServiceData.
        """
        ...

class PolicyStyle(System.Enum, int):
    """
    Determines if and how a policy may be updated.
    """
    Fixed: PolicyStyle = ...
    Dyanmic: PolicyStyle = ...
    RefCounted: PolicyStyle = ...

class ObjectPropertyPolicyManager:
    """
    
This interface manages all Object Property Policies used throughout the client
session.
    """
    def __init__(self , *args: typing.Any) -> None: ...
    AvailablePolices: list[str]
    """
             Gets a list of all policies added via the AddPolicy(String, PolicyStyle) method.
             The list will always include the 'Default' and 'Empty' policies.
            """
    CurrentPolicy: str
    """The name of the current policy."""
    PreviousPolicy: str
    """The name of the previous policy."""
    Active: str
    """
            The name of the ative policy.
            If the current thread has set policy through  SetPolicyPerThread(String), then that policy name is  returned,
            otherwise, the policy for the session ( SetPolicy(String) ) is returned.
            """
    @typing.overload
    def AddPolicy(self, policyName: str, style: PolicyStyle) -> str: ...
    @typing.overload
    def AddPolicy(self, policy: Teamcenter.Soa.Common.ObjectPropertyPolicy, useRefCounting: bool) -> str: ...
    @typing.overload
    def AddPolicies(self, policyNames: list[str]) -> list[str]: ...
    @typing.overload
    def AddPolicies(self, policies: list[Teamcenter.Soa.Common.ObjectPropertyPolicy]) -> list[str]: ...
    @typing.overload
    def AddPolicies(self, policyNames: list[str], policies: list[Teamcenter.Soa.Common.ObjectPropertyPolicy]) -> list[str]: ...
    def SetPolicy(self, policyName: str) -> None:
        """    
             Sets the Object Property Policy.
             This policy is applied to all subsequent service operation calls.
            
        :param policyName: The name of the desired policy. This can either be a named policy on the Teamcenter server,
                                     the reserved policies of  'Default' or' Empty', or the ID of a policy defined on the client.
            
        :return: 
        """
        ...
    def SetPolicyPerThread(self, policyName: str) -> None:
        """    
             Sets the Object Property Policy for service operations made on this thread.
            
        :param policyName: The name of the desired policy. This can either be a named policy on the Teamcenter server,
                                     the reserved policies of  'Default' or' Empty', or the ID of a policy defined on the client.
            
        :return: 
        """
        ...
    def ClearPolicyPerThread(self) -> None:
        """    
             Clears the Object Property Policy set for this thread.
             Once this method is called the policy applied to service requests on this thread will revert to the
             policy defined for the session.
            
        :return: 
        """
        ...
    def UpdatePolicy(self, policyName: str, applyToRootTypes: bool, addProperties: list[Teamcenter.Soa.Common.PolicyType], removeProperties: list[Teamcenter.Soa.Common.PolicyType]) -> None:
        """    
             Update the named policy, adding and removing the named properties.
            
        :param policyName: The name of the policy to update. This can either be a named policy on the
                                     Teamcenter server or the ID of a policy defined on the client.
            
        :param applyToRootTypes: If true, the properties are added or removed from the type they are defined on
                                           in the Client Meta Model. For example, the addProperties has the
                                           <b>ItemRevision/checked_out property</b>, will result in the policy being
                                           updated with the <b>WorkspaceObject/checed_out property</b>, as <b>ItemRevision</b>
                                           inherits the <b>checked_out property</b> from <b>WorkspaceObject</b>.
            
        :param addProperties: List of properties to add to the named policy. If the property already exists in
                                        the policy, all flags (excludeUiValues) on that property will be lost and only the
                                        flags from the input will be applied.
            
        :param removeProperties: List of properties to remove from the named policy. If a source <a href="T_Teamcenter_Soa_Common_PolicyType.htm">PolicyType</a>
                                           defines a type without properties, the whole type is removed. If the name policy was
                                           created with reference counting enabled, the property will only be removed if the
                                           reference count goes to zero (matching number of adds and removes).
            
        :return: 
        """
        ...
    def GetPolicy(self, policyName: str) -> Teamcenter.Soa.Common.ObjectPropertyPolicy:
        """    
             Gets the named policy, or null if the policy only has a server side definition or has not been added via
             the AddPolicy(ObjectPropertyPolicy, Boolean)  method.
            
        :param policyName: The ID of the desired policy, as returned from <a href="M_Teamcenter_Soa_Client_ObjectPropertyPolicyManager_AddPolicy_2_a564e6bc.htm">AddPolicy(ObjectPropertyPolicy, Boolean)</a>.
        :return: The named policy.
        """
        ...
    def get_AvailablePolices(self) -> list[str]: ...
    def get_CurrentPolicy(self) -> str: ...
    def get_PreviousPolicy(self) -> str: ...
    def get_Active(self) -> str: ...

class PKCS7:
    """
    
            This class implements partial PKCS7 functionalities.
            List of implemented functionalities

Generate digital signature

    """
    @staticmethod
    @typing.overload
    def sign(message: str) -> str: ...
    @staticmethod
    @typing.overload
    def sign(messages: list[str]) -> list[typing.Any]: ...
    @staticmethod
    @typing.overload
    def sign(message: list[System.Byte]) -> str: ...
    @staticmethod
    @typing.overload
    def sign(messages: list[list[System.Byte]]) -> list[typing.Any]: ...

class ServiceInfo:
    """
    
Data structure used in RequestListener methods
    """
    def __init__(self, id: str, service: str, operation: str, xmlDocument: str) -> None: ...
    Id: str
    """
              String that uniquely identifies the service request.
            """
    Service: str
    """
             The name of the service, the port defined in the WSDL.
            """
    Operation: str
    """
             The name of the service operation
            """
    XmlDocument: str
    """
             The XML document making up the service reqeust or response.
            """

class RequestListener:
    """
    
This interface is used by the SOA Client Framework to notify the client
application when
a service request is sent or its response received.
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ServiceRequest(self, info: ServiceInfo) -> None:
        """    
             This method is called before every service request.
            
        :param info: Information describing the service operation
        :return: 
        """
        ...
    def ServiceResponse(self, info: ServiceInfo) -> None:
        """    
             The method is called after the service response is received.
            
        :param info: Information describing the service response
        :return: 
        """
        ...

class SessionHandler:
    """
    
The SessionHandler is used by the ModelManager to notify the client application
of changes to the session state.
    """
    def LocalSessionChange(self, userSession: Teamcenter.Soa.Client.Model.ModelObject) -> None:
        """    
            This method is called by the SOA Framework when this client application
            has changed one of the shared session variables.
            
        :param userSession: UserSession containing latest values for group, role, etc. 
        :return: 
        """
        ...
    def SharedSessionChange(self, userSession: Teamcenter.Soa.Client.Model.ModelObject) -> None:
        """    
            This method is called by the SOA Framework when a sibling client application
            has changed one of the shared session variables.
            
        :param userSession: UserSession containing latest values for group, role, etc. 
        :return: 
        """
        ...
    def HandleException(self, e: Teamcenter.Schemas.Soa._2006_03.Exceptions.InternalServerException) -> None:
        """    
            This method is called by the SOA Framework when InternalServerException
            is received from TcMEM while processing the shared events.
            
        :param e:  InternalServerException.
        :return: 
        """
        ...

class SsoCredentials:
    """
    
This is the implementation of the CredentialManager interface used to get the
SSO credentials from the SSO server.
    """
    def __init__(self, ssoServerUrl: str, ssoAppID: str) -> None: ...
    CredentialType: int
    """
            Return the SSO as the type of credentials supplied by this Credential Manager.
            """
    SSOUrl: str
    """
             Get SSO URL.
            """
    def get_CredentialType(self) -> int: ...
    @typing.overload
    def GetCredentials(self, invalidCredentials: Teamcenter.Schemas.Soa._2006_03.Exceptions.InvalidCredentialsException) -> list[str]: ...
    @typing.overload
    def GetCredentials(self, invalidUser: Teamcenter.Schemas.Soa._2006_03.Exceptions.InvalidUserException) -> list[str]: ...
    def SetUserPassword(self, user: str, password: str, discriminator: str) -> None:
        """    
            The SSO tokens are not valid for re-authentication, but may want discriminator
            
        :param user: name of user
        :param password: password of user
        :param discriminator: optional;sessionDiscriminator to discriminate one session from another in server
            
        :return: 
        """
        ...
    def SetGroupRole(self, group: str, role: str) -> None:
        """    
            Save for relogin attempt if user expires on server
            
        :param group: group to set
        :param role: role to set
        :return: 
        """
        ...
    def get_SSOUrl(self) -> str: ...

class SponsoredSsoCredentials:
    """
    
This is the implementation of the SponsoredCredentials interface used to get the
SSO credentials from the SSO server for sponsored login
    """
    def __init__(self, ssoServerUrl: str, ssoAppID: str) -> None: ...
    CredentialType: int
    """
            Return the SSO as the type of credentials supplied by this Credential Manager for sponsored login.
            """
    SSOUrl: str
    """
             Get SSO URL.
            """
    def get_CredentialType(self) -> int: ...
    @typing.overload
    def GetCredentials(self, invalidCredentials: Teamcenter.Schemas.Soa._2006_03.Exceptions.InvalidCredentialsException) -> list[str]: ...
    @typing.overload
    def GetCredentials(self, invalidUser: Teamcenter.Schemas.Soa._2006_03.Exceptions.InvalidUserException) -> list[str]: ...
    def SetUserPassword(self, user: str, password: str, discriminator: str) -> None:
        """    
            The SSO tokens are not valid for re-authentication, but may want discriminator
            
        :param user: name of user
        :param password: password of user
        :param discriminator: optional;sessionDiscriminator to discriminate one session from another in server
            
        :return: 
        """
        ...
    def SetGroupRole(self, group: str, role: str) -> None:
        """    
            Save for relogin attempt if user expires on server
            
        :param group: group to set
        :param role: role to set
        :return: 
        """
        ...
    def get_SSOUrl(self) -> str: ...
    def SetLocale(self, loc: str) -> None:
        """    
            Set the locale to be used for sponsored SSO login.
            
        :param loc: locale to set
        :return: 
        """
        ...
    def SetSponsoredUser(self, spndUser: str) -> None:
        """    
            Set the sponsored user to be used for sponsored SSO login.
            
        :param spndUser: sponsored user to set
        :return: 
        """
        ...

class ListenerNotifier:
    def __init__(self, ) -> None: ...
    def NotifyRequestListeners(self, requestInfo: ServiceInfo) -> None: ...
    def NotifyResponseListeners(self, responseInfo: ServiceInfo) -> None: ...

class FmsServiceData:
    def __init__(self, manager: Teamcenter.Soa.Client.Model.ModelManager) -> None: ...
    def sizeOfCreatedObjects(self) -> int: ...
    def sizeOfDeletedObjects(self) -> int: ...
    def sizeOfUpdatedObjects(self) -> int: ...
    def sizeOfPlainObjects(self) -> int: ...
    def sizeOfPartialErrors(self) -> int: ...
    def GetCreatedObject(self, index: int) -> Teamcenter.Soa.Client.Model.ModelObject: ...
    def GetDeletedObject(self, index: int) -> str: ...
    def GetUpdatedObject(self, index: int) -> Teamcenter.Soa.Client.Model.ModelObject: ...
    def GetPlainObject(self, index: int) -> Teamcenter.Soa.Client.Model.ModelObject: ...
    def GetPartialError(self, index: int) -> Teamcenter.Soa.Client.Model.ErrorStack: ...

class FmsServiceData:
    def __init__(self, manager: Teamcenter.Soa.Client.Model.ModelManager) -> None: ...
    def sizeOfCreatedObjects(self) -> int: ...
    def sizeOfDeletedObjects(self) -> int: ...
    def sizeOfUpdatedObjects(self) -> int: ...
    def sizeOfPlainObjects(self) -> int: ...
    def sizeOfPartialErrors(self) -> int: ...
    def GetCreatedObject(self, index: int) -> Teamcenter.Soa.Client.Model.ModelObject: ...
    def GetDeletedObject(self, index: int) -> str: ...
    def GetUpdatedObject(self, index: int) -> Teamcenter.Soa.Client.Model.ModelObject: ...
    def GetPlainObject(self, index: int) -> Teamcenter.Soa.Client.Model.ModelObject: ...
    def GetPartialError(self, index: int) -> Teamcenter.Soa.Client.Model.ErrorStack: ...

class ValidationResult:
    def __init__(self, ) -> None: ...
    fileNameToPhysicalPath: dict[str, str]
    inputs: list[Teamcenter.Services.Loose.Core._2006_03.FileManagement.GetDatasetWriteTicketsInputData]
    partialErrors: System.Collections.ArrayList

