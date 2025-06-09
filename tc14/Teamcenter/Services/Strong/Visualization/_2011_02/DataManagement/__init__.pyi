import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class IdInfo:
    """
    
This structure holds the information about the objects that will be launched to
the
viewer.
    """
    def __init__(self, ) -> None: ...
    Id: Teamcenter.Soa.Client.Model.ModelObject
    """
            A required parameter that references the object to be launched. If needed, launched
            object will be resolved by the server to a launch able object.
            """
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """
            An optional object reference of the Item containing launch able object. If this is
            not known, the server will attempt to identify the parent if it can.
            """
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            An optional object reference of the ItemRevision containing launchable object.
            If this is not known, the server will attempt to identify if it can.
            """
    Operation: str
    """
            An optional parameter references the type of launch action. This controls the action
            the viewer will perform when it opens the object. The actions supported are one of
            following: Open, Insert,
            Merge or Interop.
            Open will open the object in a new window.
            Insert will insert the object into the current
            window that has focus.  Merge will attempt
            to merge a pruned product structure with one that is already open if it can.  Interop will present a dialog that lets the user
            select the launch action.
            """
    IdAdditionalInfo: System.Collections.Hashtable
    """
            An optional parameter referencing the additional information of launched objects
            in form of key/value pair (if any).
            """

class ServerInfo:
    """
    
This structure holds the basic information for Teamcenter Visualization to
connect
to the server.
    """
    def __init__(self, ) -> None: ...
    Protocol: str
    """
            A required parameter referencing the protocol type for connection to the server.
            Use http for standard 4 tier connections, and iiop for 2 tier deployments.
            """
    Hostpath: str
    """A required parameter referencing the URL to connect to the server."""
    Servermode: int
    """
            A required parameter referencing the servermode that controls how the connection
            to the server is made: 2 for two tier. 4 for four tier.
            """
    ServerAdditionalInfo: System.Collections.Hashtable
    """
            An optional parameter referencing the additional  information of the server in form
            of key/value pair (if any).
            """

class SessionInfo:
    """
    
This structure holds the information about the session information of the client
application from where the launch operation was initiated.
    """
    def __init__(self, ) -> None: ...
    SessionDescriminator: str
    """
            Client/Server session discriminator to connect to existing specified session.  This
            allows the viewer application to share an existing server process session with the
            client that initiated the launch. If this is not specified, the viewer will present
            a login prompt.
            """
    SessionAdditionalInfo: System.Collections.Hashtable
    """
            An optional parameter referencing the additional information of the session in form
            of key/value pair (if any).
            """

class UserAgentDataInfo:
    """
    
This structure holds the information about the client application that initiated
the launch.
    """
    def __init__(self, ) -> None: ...
    UserApplication: str
    """An optional parameter referencing the client who initiates the launch."""
    UserAppVersion: str
    """An optional parameter referencing the version of the client that initiated launch."""
    UserAdditionalInfo: System.Collections.Hashtable
    """
            An optional parameter referencing the additional information of client application
            in form of key/value pair (if any).
            """

class VVITicketsResponse:
    """
    
Used to return information from the createLaunchFile
operation. The structure holds the serviceData
object and a FMS transient read ticket corresponding to the launch file (VVI or
VFZ).
    """
    def __init__(self, ) -> None: ...
    Ticket: str
    """
            The FMS transient read ticket of the launch file (VVI or VFZ) generated for the objects
            that can be launched. The file will be placed in the transient file volume and the
            caller will need to download it from there with the ticket sent by the service.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            SOA Framework object containing error information. In cases where objects cannot
            be launched, error message, codes will be mapped to respective object id in the list
            of partial errors.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateLaunchFile(self, IdInfos: list[IdInfo], ServerInfo: ServerInfo, UserDataAgentInfo: UserAgentDataInfo, SessionInfo: SessionInfo) -> VVITicketsResponse:
        """    
             This service generates a VVI file which is used to launch Teamcenter Visualization
             viewers with selected objects from Teamcenter and preserve a two way communication
             link between the viewer and the server.  These files are not intended to be permanent
             and should be generated with each launch.  For example, the VVI format is not guaranteed
             to be supported if the server or viewer is updated.  VFZ files are used if more than
             one object is launched at a time.
             

             This operation requires the Teamcenter File Management System (FMS) to be installed
             (including FCC and transient volumes) for retrieval of the VVI file from the transient
             file volume.  This operation generates the launch file (VFZ or VVI), stores it in
             the FMS transient volume, and returns the FMS ticket.  The client that initiated
             this operation is responsible for downloading the transient file (VVI or VFZ) with
             the transient ticket from transient volume to a local file system. Transient (VVI
             or VFZ) file is then consumed by the Teamcenter Visualization client.  The viewer
             will then establish the server connection and load the object(s) specified in the
             VVI file.  Launch on multiple objects will generate a VFZ file (zip of all the vvi
             files) and transient ticket of VFZ file would be sent to client.
             

             This service supports launch on Teamcenter persistent objects like Dataset,
             Item, ItemRevision, BOMViewRevision, BOMView. It also
             supports launch of selected BOMLines of a configured structure from Structure
             Manager or BOPLines from Manufacturing Process Planner, but in this case the
             caller must first create a VisStructureContext object (See Dependency section
             for operation to use).  Valid launch object types and behavior such as priority order
             can be configured with the Teamcenter Preferences VMU_Datasets, VMU_FileSearchOrder
             and VMU_RelationSearchOrder.
             


Use Cases:

             This operation supports the mechanism of visualizing Teamcenter specific objects
             in Teamcenter Visualization client. There are several steps to support this mechanism.
             

             1.    The client application that initiates the launch will provide:
             

             A vector of IdInfo objects that contains one or more pieces of information about
             Teamcenter objects that needs to be visualized in the viewer (e.g., If Dataset
             is launched, then information about its Item, ItemRevision and type
             of operation, including any additional information can be provided). Note: In case
             launch of Teamcenter runtime objects like BOMLines from Structure Manager or BOPLines
             from Manufacturing Process Planner, it is the responsibility of the client to create
             VisStructureContext object and provide VisStructureContext as the object
             to be laud (See Dependency section for operation to use).
             
SessionInfo object contains session relevant information for Teamcenter Visualization
             to connect to the session (e.g., session discriminator and any other additional session
             relevant key value pair)
             
ServerInfo object contains server information for Teamcenter Visualization
             to connect to the server. (e.g., protocol, server URL, connection mode of the server
             and any other additional server relevant key value pair)
             
             UserAgentDataInfo object contains client application information who initiated the
             launch. (e.g., application name, application version, and any other additional client
             application relevant key value pair).
             


             2.    After gathering the necessary information as listed in
             step 1, client application then invokes the DataManagementService::createLaunchFile
             operation to obtain an FMS read ticket for the launch file (VVI or VFZ), that has
             relevant information for visualizing Teamcenter persistent or runtime objects.
             

             See the Dependencies section below for details.
             

             3.    Use a File Management System (FMS) Application Programmatic
             Interface (API) to download the transient file (VVI or VFZ) from transient volume.
             

             Check the documentation for each API to determine how to react to download failures.
             

             Use Case References:
             
             This operation is used in conjunction with other FileManagementService
             service operations, Visualization service
             operations, FccProxy and the FileManagementUtility. Please consult the documentation
             for each of these available operations for details on the requirements, usage, and
             environments in which they should be used.
             

             Visualization operations for creating the VisStructureContext from clients
             that initiate the launch of Teamcenter runtime objects like BOMLines from
             Structure Manager or BOPLines from Manufacturing Process Planner.
             

Teamcenter::Soa::Internal::Visualization::_2011_02::
             StructureManagement::CreateVisSCsFromBOMsResponse createVisSCsFromBOMs




Teamcenter Component:

             Teamcenter Visualization - Application to allow view and markup of multicad product
             structure that has a jt representation.
             
        :param IdInfos: 
                         A vector of <font face="courier" height="10">IdInfo</font> structures which holds
                         information about Teamcenter objects that need to be visualized in Teamcenter Visualization.
                         For example, if a <b>Dataset</b> is launched, then information about its <b>Item</b>,
                         <b>ItemRevision</b> and type of operation, including any additional information can
                         be provided.
             
        :param ServerInfo: 
                         A <font face="courier" height="10">ServerInfo</font> structure object containing
                         server information for the viewer to connect to the server.  Contains protocol, server
                         URL, connection mode of the server and any other additional server relevant key value
                         pair
             
        :param UserDataAgentInfo: 
                         A <font face="courier" height="10">UserAgentDataInfo</font> structure object containing
                         information about client that initiated the launch (e.g., application name, application
                         version , and any other additional client application relevant key value pair)
             
        :param SessionInfo: 
                         A <font face="courier" height="10">SessionInfo</font> structure object containing
                         session information for the viewer to connect to the session.  Includes the session
                         discriminator and any other additional session relevant key value pair.
             
        :return: for those respective objects and an
             FMS transient read ticket, for the launch file, representing the objects that can
             be launched.
        """
        ...

