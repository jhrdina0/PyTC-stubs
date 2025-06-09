import System
import System.Collections
import Teamcenter.Services.Strong.Visualization._2011_02.DataManagement
import Teamcenter.Services.Strong.Visualization._2011_02.StructureManagement
import Teamcenter.Services.Strong.Visualization._2013_05.DataManagement
import Teamcenter.Services.Strong.Visualization._2013_12.StructureManagement
import Teamcenter.Services.Strong.Visualization._2016_03.DataManagement
import Teamcenter.Soa.Client
import typing

class DataManagementRestBindingStub(DataManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateLaunchFile(self, IdInfos: list[Teamcenter.Services.Strong.Visualization._2011_02.DataManagement.IdInfo], ServerInfo: Teamcenter.Services.Strong.Visualization._2011_02.DataManagement.ServerInfo, UserDataAgentInfo: Teamcenter.Services.Strong.Visualization._2011_02.DataManagement.UserAgentDataInfo, SessionInfo: Teamcenter.Services.Strong.Visualization._2011_02.DataManagement.SessionInfo) -> Teamcenter.Services.Strong.Visualization._2011_02.DataManagement.VVITicketsResponse: ...
    def CreateLaunchInfo(self, IdInfos: list[Teamcenter.Services.Strong.Visualization._2013_05.DataManagement.IdInfo2], ServerInfo: Teamcenter.Services.Strong.Visualization._2011_02.DataManagement.ServerInfo, UserDataAgentInfo: Teamcenter.Services.Strong.Visualization._2011_02.DataManagement.UserAgentDataInfo, SessionInfo: Teamcenter.Services.Strong.Visualization._2013_05.DataManagement.SessionInfo2) -> Teamcenter.Services.Strong.Visualization._2013_05.DataManagement.LaunchInfoResponse: ...
    def GetMetaDataStampWithContext(self, MetaDataStampInfos: list[Teamcenter.Services.Strong.Visualization._2016_03.DataManagement.MetaDataStampInputInfo]) -> Teamcenter.Services.Strong.Visualization._2016_03.DataManagement.MetaDataStampOutputResponse: ...

class DataManagementService:
    """
    
            This library contains a set of service operations that perform
server side business
            logic for the visualization integrations.  These operations help
interrogate and
            manipulate the Teamcenter data model for visualization data, and aid
with integrating
            visualization enabled client applications with Teamcenter in a
consistent way.  There
            are operations that help launch visualization given an object
reference (e.g. createLaunchFile).  There are operations that help
            load and save Product Views (e.g. getSnapshot3DInfo,
            createSnapshot3D, etc).  There are operations
            for creating and updating markups and visualization sessions.
There are operations
            for handling product structure and configuration recipes (the
StructureManagement operations).

            Nearly all of these are internal operations, used by the various
internal PLM client
            applications and visualization integrations (embedded and
standalone).  However,
            there are 3 exceptions to this, the following visualization
operations were made
            public:

createLaunchFile

createBOMSFromRecipes

createVisSC

            These operations can be used by customers to integrate an external
visualization
            application or custom PLMVis based viewer with data stored and
maintained in Teamcenter.
            The most common use case where this is needed is shop floor
visualization.

            These operations are used by all the visualization integrations
provided today, for
            example: 1) integrated standalone visualization, 2) visualization
embedded in the
            RAC, and 3) visualization embedded in the Thin Client.  Use of these
services ensures
            consistent behavior and code reuse across the various visualization
enabled client
            applications of Teamcenter.

Dependencies:

            SpatialStructureManagement, StructureManagement, DataManagement,
StructureManagement

Library Reference:

TcSoaVisualizationStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DataManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateLaunchFile(self, IdInfos: list[Teamcenter.Services.Strong.Visualization._2011_02.DataManagement.IdInfo], ServerInfo: Teamcenter.Services.Strong.Visualization._2011_02.DataManagement.ServerInfo, UserDataAgentInfo: Teamcenter.Services.Strong.Visualization._2011_02.DataManagement.UserAgentDataInfo, SessionInfo: Teamcenter.Services.Strong.Visualization._2011_02.DataManagement.SessionInfo) -> Teamcenter.Services.Strong.Visualization._2011_02.DataManagement.VVITicketsResponse:
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
    def CreateLaunchInfo(self, IdInfos: list[Teamcenter.Services.Strong.Visualization._2013_05.DataManagement.IdInfo2], ServerInfo: Teamcenter.Services.Strong.Visualization._2011_02.DataManagement.ServerInfo, UserDataAgentInfo: Teamcenter.Services.Strong.Visualization._2011_02.DataManagement.UserAgentDataInfo, SessionInfo: Teamcenter.Services.Strong.Visualization._2013_05.DataManagement.SessionInfo2) -> Teamcenter.Services.Strong.Visualization._2013_05.DataManagement.LaunchInfoResponse:
        """    
             This service generates a VVI file which is used to launch Teamcenter Visualization
             viewers with selected objects from Teamcenter and preserve a two way communication
             link between the viewer and the server.  This operation can return the VVI type information
             as a string buffer or as a read file ticket to a vvi/vfz file in the FMS transient
             file volume. NOTE: VVI and VFZ files are not intended to be persisted and should
             be generated with each launch of visualization. For example, the VVI format is not
             guaranteed to be supported if the server or viewer is updated. VFZ files are used
             if more than one object is launched at a time, while VVI files are used for single
             objects. The client can retrieve the VVI/VFZ launch file information via string buffer
             or through the transient file volume. This is controlled by setting the hasTransientVolume
             flag of the SessionInfo2 input structure.  With the hasTransientVolume flag set to
             false, the launch info returns a vvi string buffer for each launch object or as a
             stream of vvi string buffers for multiple launch objects.  Using the API in this
             way can avoid setup and use of the FMS system directly by the calling client.  It
             is the responsibility of the client to decipher the response data structure.  For
             example, the vvi string buffer(s) can be written out as a vvi or vfz file on the
             client and passed to visualization, or the string buffer can be passed directly to
             embedded visualization if using the PLMVis toolkit.  With the hasTransientVolume
             flag set to true, the operation requires the Teamcenter File Management System (FMS)
             to be installed (including FCC and transient volumes) for retrieval of the VVI file
             from the transient file volume. This operation generates the launch file (VFZ or
             VVI), stores it in the FMS transient volume, and returns the FMS ticket. The client
             that initiated this operation is responsible for downloading the transient file (VVI
             or VFZ) with the transient ticket from transient volume to a local file system. The
             transient (VVI or VFZ) file is consumed by the Teamcenter Visualization client. The
             viewer will then establish the server connection and load the object(s) specified
             in the VVI file.  Launch on multiple objects will generate a VFZ file (zip of all
             the vvi files) and transient ticket of VFZ file would be sent to client. This service
             supports launch on Teamcenter persistent objects like Dataset, Item, ItemRevision,
             BOMViewRevision, BOMView. It also supports launch of selected BOMLines of a configured
             structure from Structure Manager or BOPLines from Manufacturing Process Planner,
             but in this case the caller must first create a VisStructureContext object. Valid
             launch object types and behavior such as priority order can be configured with the
             Teamcenter Preferences VMU_Datasets, VMU_FileSearchOrder and VMU_RelationSearchOrder.
             

Teamcenter Component:

             Teamcenter Visualization - Application to allow view and markup of multicad product
             structure that has a jt representation.
             
        :param IdInfos: 
                         A list of Teamcenter objects and related information that need to be visualized in
                         Teamcenter Visualization. For example, if a Dataset is launched, then information
                         about its Item, ItemRevision and type of operation, including any additional information
                         can be provided.
             
        :param ServerInfo: 
                         Server information for the viewer to connect to the server. Contains protocol, server
                         URL, connection mode of the server and any other additional server relevant key value
                         pair.
             
        :param UserDataAgentInfo: 
                         The information about the client that initiated the launch (e.g., application name,
                         application version, and any other additional client application relevant key value
                         pair).
             
        :param SessionInfo: 
                         The session information for the viewer to connect to the session. Includes the session
                         discriminator and any other additional session relevant key value pair.
             
        :return: VVI file data as a string buffer or FMS file ticket for the request objects. The
             following partial errors may be returned: 208031: Launch request is not valid. 208013:
             The selected object is invalid for the launch operation; 208012: Launch file generation
             failed.
        """
        ...
    def GetMetaDataStampWithContext(self, MetaDataStampInfos: list[Teamcenter.Services.Strong.Visualization._2016_03.DataManagement.MetaDataStampInputInfo]) -> Teamcenter.Services.Strong.Visualization._2016_03.DataManagement.MetaDataStampOutputResponse:
        """    
             This operation retrieves metadata stamp files for Teamcenter objects based on the
             context within which these objects are being displayed.  For example, when a user
             prints a model view, the stamp will vary based on the context within which this model
             view is printed.  Printing the model view in owning model context provides one stamp,
             while printing the same view from within a disclosure context produces another stamp.
             

             The metadata stamp is generated based on the list of objects and the context of those
             objects using the metaDataStampInfos list. The transient ticket for the generated
             *.mds file is returned. The ticket can then be used to retrieve the file using a
             FMS method like FccProxy::downloadFiles.
             

             The Teamcenter default implementation uses a Metadatastamp template containing an
             MDS file with Teamcenter property names and default values. The Teamcenter site preference
             MetaDataStamp_template is used to find the item where the template files is stored.
             This file is processed and each Attribute specified will be replaced with the matching
             object property values if found. The output mds file will be written to the transient
             volume and the transient ticket of the file is sent to client in the response data.
             The customization hook provided with this interface may wish to use the same template
             mds file as a starting point.
             

             This operation requires the Teamcenter File Management System (FMS) to be installed
             (including FCC and transient volumes).
             

Use Cases:

             This method is called by visualization when integrating with Teamcenter for printing
             objects like Fnd0ModelViewProxy and SnaphotViewData datasets that are loaded into
             some higher level product context. The user loads a configured product structure,
             or some high level object that sets context in Teamcenter. Within this structure
             or context, the user finds objects they wish to print, and invokes a print action,
             The stamping context is the higher level context within which the stamping metadata
             is retrieved from (e.g. the root node of the product structure), and the stamped
             objects are the individual objects that are to be printed (e.g. model views or product
             Views). Stamp files (tickets) are returned to the caller, and these files are used
             by visualization to place metadata markings on views printed. The stamp file represents
             a metadata stamp overlay on top of the printed image and often contains control information
             for printed detailed design data.
             

             The MDS file created by this service can also be used by the VisView Convert and
             Print utilities.
             

             This service may also be useful for customizations that leverage Siemens Embedded
             visualization toolkits, and thus it is a public service.
             

Teamcenter Component:

             Teamcenter Visualization - Application to allow view and markup of multicad product
             structure that has a jt representation.
             
        :param MetaDataStampInfos: 
                         A list of MetaStampInputInfo structures. Each of the structure elements is identified
                         by a unique identifier enabling the caller to map the input to the output. The input
                         structure holds information including the list of objects to stamps and the stamping
                         context object.
             
        :return: 
        """
        ...

class StructureManagementRestBindingStub(StructureManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateVisSC(self, Info: list[Teamcenter.Services.Strong.Visualization._2011_02.StructureManagement.CreateVisSCInfo]) -> Teamcenter.Services.Strong.Visualization._2011_02.StructureManagement.CreateVisSCResponse: ...
    @typing.overload
    def CreateVisSCsFromBOMs(self, Info: list[Teamcenter.Services.Strong.Visualization._2011_02.StructureManagement.CreateVisSCsFromBOMsInfo]) -> Teamcenter.Services.Strong.Visualization._2011_02.StructureManagement.CreateVisSCsFromBOMsResponse: ...
    @typing.overload
    def CreateVisSCsFromBOMs(self, Info: list[Teamcenter.Services.Strong.Visualization._2011_02.StructureManagement.CreateVisSCsFromBOMsInfo], Options: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Visualization._2011_02.StructureManagement.CreateVisSCsFromBOMsResponse: ...
    def CreateVisSCsFromBOMsWithOptions(self, Info: list[Teamcenter.Services.Strong.Visualization._2013_12.StructureManagement.CreateVisSCsFromBOMsInfo], GlobalOptions: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Visualization._2011_02.StructureManagement.CreateVisSCsFromBOMsResponse: ...

class StructureManagementService:
    """
    
            This service provides operations that abstract the complexities of
BOM system structure
            configuration from the visualization client integrations.  Launching
of selected
            occurrences from a configured structure into visualization is an
example use case
            that is enabled by these services.  Another example is storage of a
visualization
            session that records what configured structure needs to be opened in
order to restore
            the session to its previous state.

Dependencies:

            DataManagement

Library Reference:

TcSoaVisualizationStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> StructureManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateVisSC(self, Info: list[Teamcenter.Services.Strong.Visualization._2011_02.StructureManagement.CreateVisSCInfo]) -> Teamcenter.Services.Strong.Visualization._2011_02.StructureManagement.CreateVisSCResponse:
        """    
             This operation takes a list of ConfigurationContext/top line object pairs
             and creates a VisStructureContext object based on that input. The user may
             optionally supply a list of occurrences in the form of UID chains and a file reference
             for the static PLMXML representation of the configuration. If an occurrence list
             or a static structure file are supplied they will be set as properties on the VisStructureContext
             object. The list of occurrences can be used to populate/expand any BOMWindows
             that are subsequently created using the output VisStructureContext object.
             

Use Cases:

             When the user desires to create a single persistent object that records a particular
             configuration recipe and the caller already has the component objects that make up
             the configuration. This case might occur if the configuration elements of a BOMWindow
             were captured but the BOMWindow was then deleted. This is often the case when
             using the Teamcenter Thin Client.
             


             The createVisSC operation requires input configuration objects and their top lines.
             Therefore, these objects must have been obtained based on some previous configuration
             scenario.
             


Teamcenter Component:

             Teamcenter Visualization - Application to allow view and markup of multicad product
             structure that has a jt representation.
             
        :param Info: 

        :return: object that records the
             configuration recipe.
        """
        ...
    @typing.overload
    def CreateVisSCsFromBOMs(self, Info: list[Teamcenter.Services.Strong.Visualization._2011_02.StructureManagement.CreateVisSCsFromBOMsInfo]) -> Teamcenter.Services.Strong.Visualization._2011_02.StructureManagement.CreateVisSCsFromBOMsResponse: ...
    @typing.overload
    def CreateVisSCsFromBOMs(self, Info: list[Teamcenter.Services.Strong.Visualization._2011_02.StructureManagement.CreateVisSCsFromBOMsInfo], Options: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Visualization._2011_02.StructureManagement.CreateVisSCsFromBOMsResponse: ...
    def CreateVisSCsFromBOMsWithOptions(self, Info: list[Teamcenter.Services.Strong.Visualization._2013_12.StructureManagement.CreateVisSCsFromBOMsInfo], GlobalOptions: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Visualization._2011_02.StructureManagement.CreateVisSCsFromBOMsResponse:
        """    
             This operation takes a list of BOMLines (the occurrences list) and returns
             the VisStructureContext objects representing the configuration state of the
             BOMWindow (referred to as the configuration recipe). This configuration includes:
             

The occurrence UID chains for the input/selected BOMLines
             up to but not including the top line.
             
Optional IMANFile reference to the PLMXML static representation
             of the BOMWindow.
             



             This service supports both the interoperation of selected BOMLines from the
             Teamcenter Rich Client to Teamcenter Visualization and also the capture/persistence
             of the configuration recipe for a particular BOMWindow. The occurrence list
             records the selected BOMLines at the time of interoperation and can be used
             in later operations to populate/expand a BOMWindow with those same occurrences.
             

Use Cases:

             When the user desires to create a persistent object that records the configuration
             recipe of a particular BOMWindow. The resulting VisStructureContext
             object would assumedly be used to later reconstruct a BOMWindow with the same
             configuration recipe and the recorded UID occurrence chains would be used to populate/expand
             the constructed BOMWindow with specific BOMLines. For example, this
             operation is used when sending selected BOMLines from the Structure Manager
             to Teamcenter Visualization and also to capture the configuration recipe for storage
             in Vis Sessions.
             

             Visualization pruned launch use case
             

User opens a structure in Structure Manager (SM)/Multi Structure
             Manager (MSM)/Manufacturing Process Planner (MPP), and configures it
             
User selects some lines they want to send to visualization as a pruned
             structure
             
System calls createVisSCsFromBOMsWithOptions to record the selected
             lines and the configuration of the BOM to send
             



             Visualization session save use case
             

1.    User performs Visualization pruned launch
             use case and loads occurrences into visualization
             
2.    User creates some authored visualization
             content (e.g. snapshots, motions, etc)
             
3.    User saves session to Teamcenter
             
4.    System calls createRecipesFromBOMs operation
             to capture the configuration and any pruning information as a VisStructureContext
             object.  UID of object returned.
             
5.    System writes the VisStructureContext
             object reference into the visualization session data
             
6.    System saves the visualiation session dataset
             to Teamcenter, and relates it to the VisStructureContext object created by
             the service
             



             Visualization Technical Illustration and 3D Markup save use cases
             
             Similar to session save use case, except saving a different data type.  Uses this
             service to create the recipe for the authored visualization data in the Teamcenter
             data model.
             

             Use Case Dependencies:
             
             The createVisSCsFromBOMsWithOptions operation is called with input BOMLines
             from an existing BOM Window. Therefore, the BOMWindow must have already been
             created and populated with at least a top line.
             

Teamcenter Component:

             Teamcenter Visualization - Application to allow view and markup of multicad product
             structure that has a jt representation.
             
        :param Info: 

        :param GlobalOptions: 
                         The list of global options the caller wishes to provide to the operation. These options
                         apply to each <b>VisStructureContext</b> object that is created as a result of this
                         operation (as opposed to the options present in the <i>info</i> input parameter that
                         only apply to that given <b>VisStructureContext</b>). This list of options is represented
                         by a map of string option names to string option values. The values are represented
                         as a list of strings. The size of this list is dependent on the particular option
                         being defined.
             
        :return: 
        """
        ...

