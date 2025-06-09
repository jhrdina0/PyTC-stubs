import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class LaunchDefinitionResponse:
    """
    Return data for the laucnh definition.
    """
    def __init__(self, ) -> None: ...
    XmlLaunchDef: str
    """
            For the ViewMarkup and OfficeOpen operations, the launch definition xml string.
            
            For the AWOfficeOpen operation, the launch definition file ticket string.
            """
    SvcData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The Service Data. Partial errors and failures are updated and returned through this
            object
            """

class LDSelectedInputInfo:
    """
    Launch definition selected input information.
    """
    def __init__(self, ) -> None: ...
    Id: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The id can be an Item, an ItemRevision business object, a Dataset
            business object or a markup control object.  It is required.  If empty, invalid object
            error is returned
            """
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """Related item to input id."""
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Related ItemRevision to the input id."""
    ControlObj: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            Related markup control object (related to the markup through MarkupContextRelation).
            The control object is determined based on the business object constant Fnd0MarkupControlObject
            set to true.
            """
    RequestMode: str
    """
            There are 3 possible values for this element. MARKUP, VIEW, EDIT.  Example, MARKUP
            is for View/Markup action.  VIEW and EDIT is for View/Open action on an office dataset
            business object.
            """
    AdditionalInfo: System.Collections.Hashtable
    """
            This is the map of additional information in the form of key value pair strings.
            This can be empty.
            """

class SsoInfo:
    """
    The information for SSO.
    """
    def __init__(self, ) -> None: ...
    LoginServiceUrl: str
    """The login service Uniform resource locator (Url)."""
    AppId: str
    """The application Id of the Teamcenter server in this Single Sign On(SSO) environment."""

class ServerInfo:
    """
    Server Information.
    """
    def __init__(self, ) -> None: ...
    Protocol: str
    """
            http or iiop (Protocol type for connection to the server). http is for four tier
            and iiop is for two tier deployment
            """
    HostPath: str
    """The host path"""
    ServerMode: str
    """
            Single character. 2 for two tier. 4 for four tier.  This is to support the VIS legacy
            ITK
            """
    UseTccs: bool
    """
            If client uses Single Sign On(SSO) to connect to server, then this should be set
            to true. Otherwise, false
            """
    UseSso: bool
    """
            If client uses SSO to connect to server, then this should be set to true. Otherwise,
            false
            """
    TccsEnvironment: str
    """Teamcenter client communication system (TCCS) environment name"""
    SsoInfo: SsoInfo
    """SSO information"""
    AdditionalInfo: System.Collections.Hashtable
    """This is the map of additional information in the form of key value pair strings"""

class SessionInfo:
    """
    Session information.
    """
    def __init__(self, ) -> None: ...
    Descriminator: str
    """Client Server session discriminator to connect existing specified session."""
    AdditionalInfo: System.Collections.Hashtable
    """This is the map of additional information in the form of key value pair strings."""

class UserAgentDataInfo:
    """
    User application information.
    """
    def __init__(self, ) -> None: ...
    UserApplication: str
    """
            Client who initiates the VVI launch. The VVI file contains the information necessary
            for the stand alone viewer to open the file.
            """
    UserAppVersion: str
    """Version of the client."""
    AdditionalInfo: System.Collections.Hashtable
    """This is the map of additional information in the form of key value pair strings."""

class LaunchDefinition:
    """
    Interface LaunchDefinition
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetLaunchDefinition(self, Operation: str, SelectedInputs: list[LDSelectedInputInfo], ServerInfo: ServerInfo, SessionInfo: SessionInfo, UserAgentData: UserAgentDataInfo) -> LaunchDefinitionResponse:
        """    
             The Application Launcher (AppLauncher) uses a launch definition XML as input to launch
             appropriate external applications. This operation gathers the data and builds the
             launch definition XML string. It contains information for list of supported tools,
             business data and tool preferences. The definition XML is based on the list of LDSelectedInputInfo structure ( contains WorkspaceObject,
             related Item, related ItemRevision, related control WorkspaceObject
             business object, request mode and additional information in the form of key value
             pair strings), structure of server information ServerInfo
             where the operation is initiated, structure of the session information SessionInfo of the client from where the operation is initiated,
             and structure of client information UserAgentDataInfo
             from where the operation is initiated.
             
             The required input data from the LDSelectedInputInfo
             structure is the WorkspaceObject business object (normally this input is the
             subtype of WorkspaceObject business object such as Item business object
             or ItemRevision business object or Dataset business object).    The
             input structures for server, session, and client information can be empty.
             

Use Cases:

             Use case1:  View/Markup action from client

             When a user selects an Item or an ItemRevision or a Dataset
             and performs View/Markup action in the client, the system will invoke the getLaunchDefinition
             operation.
             
             Use case2:  Office client open

             When a user performs open action on an MSWord Dataset and the client is configured
             to use AppLauncher for open, the system will invoke the getLaunchDefinition operation.
             
             Use case3: Active Workspace Office client open

             When a user performs open and edit in office client action on an MSWord Dataset
             and the client is configured to use AppLauncher for open, the system will invoke
             the getLaunchDefinition operation.
             



Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param Operation: 
                         Operation keys such as View/Markup, OfficeOpen, AWOfficeOpen
             
        :param SelectedInputs: 
                         The input list of structures of  <b>Item</b>/<b>ItemRevision</b>/<b>Dataset</b>/Control
                         Object. Gathering the launch data and building launch definition XML are based on
                         it
             
        :param ServerInfo: 
                         The server information where the operation is inititated.  This structure can be
                         empty
             
        :param SessionInfo: 
                         The current session information where the operation is initiated.  This structure
                         can be empty
             
        :param UserAgentData: 
                         The client information from where the operation is initiated.  This structure can
                         be empty
             
        :return: 
        """
        ...

