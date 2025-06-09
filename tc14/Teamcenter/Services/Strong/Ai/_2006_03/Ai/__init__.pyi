import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ApplicationRef:
    """
    Structure representing application neutral identifier
    """
    def __init__(self, ) -> None: ...
    Application: str
    """
            The application where these fields can be resolved. For example - it is Teamcenter
            for TC.
            """
    Label: str
    """The identifier for the object."""
    Version: str
    """The optional version string."""

class CommitFileData:
    """
    commitFileData structure to be used when commiting files to teamcenter.
    """
    def __init__(self, ) -> None: ...
    Ticket: str
    """the write ticket returned from Teamcenter from a prior call to GetWriteFileTickets."""
    Id: ApplicationRef
    """If used with AI object, this represents the id of the RequestObject."""
    Filename: str
    """filename as specified, when getting the write ticket."""

class CommitFilesResponse:
    """
    commit files response.
    """
    def __init__(self, ) -> None: ...
    FailedCommits: list[CommitFileData]
    """failedCommits"""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """data"""

class CommitStructureFileResponse:
    """
    returns the fileIds if the saved plmxml file.
    """
    def __init__(self, ) -> None: ...
    FileId: str
    """fileId"""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """data"""

class Configuration:
    """
    Configuration structure.
    """
    def __init__(self, ) -> None: ...
    Id: Teamcenter.Soa.Client.Model.ModelObject
    """
            Tag of ConfigurationContext or StructureContext or RevRule or VariantRule or storedOptionSetId,or
            TransferMode.
            """
    Rulename: str
    """if id is NULLTAG, then used to specify the revisionrule by name."""
    UseDefaultRevisionRule: bool
    """
            if true - the Teamcenter preferences are used to pick up the rev rule. Overrides
            the above 2 members if true.
            """

class FileTicket:
    """
    FileTicket details
    """
    def __init__(self, ) -> None: ...
    Ticket: str
    """the FMS ticket"""
    OriginalFileName: str
    """name of the file that is displayed in TC UI"""

class CreatePublishRequestResponse:
    """
    response of the createPublishRequest method.
    """
    def __init__(self, ) -> None: ...
    Ticket: FileTicket
    """ticket"""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """data"""

class GenerateFullSyncRequestResponse:
    """
    Used to generate the plmxml for a sync request.
    """
    def __init__(self, ) -> None: ...
    Ticket: FileTicket
    """ticket"""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """data"""

class GenerateStructureResponse:
    """
    generatestructure returns the transient file ticket on success.
    """
    def __init__(self, ) -> None: ...
    Ticket: str
    """ticket"""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """data"""

class GetFileReadTicketsResponse:
    """
    tickets to download files referenced by plmxml.
    """
    def __init__(self, ) -> None: ...
    Tickets: list[FileTicket]
    """tickets"""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """data"""

class GetFileWriteTicketsResponse:
    """
    Tickets to upload files referenced by plmxml.
    """
    def __init__(self, ) -> None: ...
    Tickets: list[str]
    """tickets"""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """data"""

class GetNextApprovedRequestResponse:
    """
    get next approved request. Currently not used.
    """
    def __init__(self, ) -> None: ...
    Ticket: FileTicket
    """ticket"""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """data"""

class GetPropertiesOfObjectsResponse:
    """
    GetPropertiesOfObjectsResponse struct
    """
    def __init__(self, ) -> None: ...
    NameValues: System.Collections.Hashtable
    """nameValues"""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """data"""

class GetStructureReadTicketResponse:
    """
    response of getStructureReadTicket - returns the plmxml file ticket.
    """
    def __init__(self, ) -> None: ...
    Ticket: FileTicket
    """ticket"""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """data"""

class GetStructureWriteTicketResponse:
    """
    
            response of getStructureWriteTicket - returns the ticket to be used for uploading
            a plmxml file.
            
    """
    def __init__(self, ) -> None: ...
    Ticket: str
    """ticket"""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """data"""

class ObjectsExistResponse:
    """
    response of ObjectsExist method
    """
    def __init__(self, ) -> None: ...
    BExist: list[bool]
    """does the object exist in Teamcenter or not."""
    Ids: list[ApplicationRef]
    """All the ApplicationRef registered for the Teamcenter object"""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """used to report any partial failures."""

class ProjectCreationData:
    """
    Project(AI) creation method data
    """
    def __init__(self, ) -> None: ...
    Type: str
    """Type of the Application Interface object to be created."""
    Name: str
    """Name of the AI object to be created."""
    Description: str
    """Description of the AI object to be created."""
    TargetApplicationId: str
    """The application id to be set on the AI object."""

class ProjectFilter:
    """
    Structure to specify the filter when using GetProjects method.
    """
    def __init__(self, ) -> None: ...
    ProjectType: str
    """ProjectType enum. Set it to ProjectType_Any if not needed."""
    Name: str
    """name of the AppliationInterface Object"""
    Description: str
    """description of the ApplicationInterface Object"""
    Type: str
    """type of the ApplicationInterface Object. The type must be a valid type of AI Object."""
    UserId: str
    """userId to filter on"""
    GroupName: str
    """filter on AI objects using groupName"""
    CreatedBefore: System.DateTime
    """filtering by Date"""
    CreatedAfter: System.DateTime
    """filtering by Date"""
    ModifiedBefore: System.DateTime
    """filtering by Date"""
    ModifiedAfter: System.DateTime
    """filtering by Date"""
    ReleasedBefore: System.DateTime
    """filtering by Date"""
    ReleasedAfter: System.DateTime
    """filtering by Date"""
    ApplicationId: str
    """maps to the Export TransferMode's (of the AI) context string"""
    SiteId: str
    """description of the ApplicationInterface Object"""
    TargetAppProjectId: str
    """used only if projectType==ProjectType_Existing"""

class ProjectInfo:
    """
    Structure to specify ApplicationInterface information.
    """
    def __init__(self, ) -> None: ...
    TargetAppProjectId: str
    """The projectId string recorded on the ApplicationInterface Object"""
    Name: str
    """name of the AppliationInterface Object"""
    Description: str
    """description of the ApplicationInterface Object"""

class StatusInfo:
    """
    Structure representing the status fields of the RequestObject
    """
    def __init__(self, ) -> None: ...
    Status: str
    """RequestStatus enum RequestStatus_Normal etc."""
    Description: str
    """status message of the Request."""

class RequestDetail:
    """
    Structure representing the details of the RequestObject
    """
    def __init__(self, ) -> None: ...
    Name: str
    """name of the RequestObject"""
    Description: str
    """description of the RequestObject"""
    StateDesc: str
    """description on the state of the RequestObject."""
    Status: StatusInfo
    """the status fields of the RequestObject"""
    Scope: str
    """
            RequestScope_Whole - no ExternalReference elements will be found in plmxml. If Partial
            then there will be ExternalReference elements in plmxml.
            """
    Update: str
    """used to specify an incremental update."""

class StateFilter:
    """
    Structure to filter RequestObject
    """
    def __init__(self, ) -> None: ...
    States: list[str]
    """vector of RequestState enums"""
    Types: list[str]
    """vector of RequestType enums"""

class Ai:
    """
    Interface Ai
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateProjects(self, ProjectDatas: list[ProjectCreationData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Create ApplicationInterface Objects in Teamcenter based on the input values.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param ProjectDatas: 
                         std::vector of ProjectCreationData, each of which has the name,type, description
                         and optional targetApplicationId.
             
        :return: new objects added to the CreatedObjs member of ServiceData. Partial failures will
             be reported in the service data too. member.
        """
        ...
    def GenerateStructure(self, IdsToProcess: list[ApplicationRef], TransferModeName: str, Config: Configuration, ServerMode: int) -> GenerateStructureResponse:
        """    
             Generate a plmxml for the given set of ids.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param IdsToProcess: 
                         ids for which plmxml will be generated. If multiple ids are specified - the traverse
                         rootRef in plmxml will have these multiple roots.
             
        :param TransferModeName: 
                         The name of the transferMode in TC.
             
        :param Config: 
                         Configuration structure. If the id(Tag) member is specified, it must be the     the
                         tag of ConfigurationContext or StructureContext or RevRule or VariantRule or storedOptionSetId,
                         or TransferMode.     If this is a NULLTAG - then rulename will be used to find
                         RevisionRule. If both are empty, and     useDefaultRevisionRule is true - the Teamcenter
                         preferences are used to pick up the rev rule.     If all 3 are not used - then no
                         revrule will be used in the generation of plmxml.
             
        :param ServerMode: 
                         - 2 or 4 - 2tier or 4-tier. This is used for transient file ticket generation on
                         server.
             
        :return: file path to the FCC Cache location. Any errors during plmxml processing are returned
             in resp struct. severe error would result in an exception being thrown.
        """
        ...
    def GetFileReadTickets(self, FileIds: list[ApplicationRef]) -> GetFileReadTicketsResponse:
        """    
             Used to download the tickets for the files referenced by the plmxml file previously
             exported from Teamcenter. These tickets are then to be used with FCC client Proxy
             to actually download the files.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param FileIds: 
                         Ids for which the files are obtained.
             
        :return: list of successful tickets, successul originalFileNames (which will be the same size)
             and the list of failedIds. Reasons of failure - will be inServiceData struct.
        """
        ...
    def GetFileWriteTickets(self, OriginalFileNames: list[str], FileTypes: list[str]) -> GetFileWriteTicketsResponse:
        """    
             Used to download the tickets for the files referenced by the plmxml file created
             by a client application. These tickets are then to be used with FCC client Proxy
             to actually upload(commit) the files.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param OriginalFileNames: 
                         The original fileName array. If there it a path - it is stripped out.
             
        :param FileTypes: 
                         The fileType for each corresponding element in originalFileNames array. If empty
                         - then default to Binary for all files.
             
        :return: list of successful tickets, failed originalFileNames. Reasons of failure - will be
             in ServiceData struct.
        """
        ...
    def GetProjects(self, Filter: ProjectFilter) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Get a list of projects that are available on this database based on the filter specified.
             Suggest atleast filtering based on type of AppInterface
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Filter: 
                         qualifier to customize the projects returned.
             
        :return: serviceData returned will have the projects added as plainobjects. In case of partial
             failures - they will be reported in ServiceData - errorStack
        """
        ...
    def GetPropertiesOfObjects(self, AppRefs: list[ApplicationRef], PropertySetNames: list[str]) -> GetPropertiesOfObjectsResponse:
        """    
             Get Properties of Teamcenter obects based on a propertyset created using the plmxml
             admin application.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param AppRefs: 
                         The ApplicationRefs of objects on which properties are desired.
             
        :param PropertySetNames: 
                         The name of the property set for each of the corresponding objects in appRefs array.
                         The scope of any propertySetName must be TcEng. Refer to the plmxml admin application
                         documentation for further details.
             
        :return: partial failures are returned in data. The property name and it's values are retuned
             in the nameValues member.
        """
        ...
    def GetStructureWriteTicket(self, OriginalFileName: str) -> GetStructureWriteTicketResponse:
        """    
             Used to download the ticket for the plmxml file that will be uploaded by the client.
             This ticket is then to be used with FCC client Proxy to actually upload the file.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param OriginalFileName: 
                         originalFileName to be used in Teamcenter.
             
        :return: fileticket is returned in the Response struct.
        """
        ...
    def ObjectsExist(self, ObjIds: list[ApplicationRef]) -> ObjectsExistResponse:
        """    
             Given 1 or more ApplicationRef objects - find the corresponding TeamCenter Object(s).
             Typically, the ApplicationRef is obtained from a plmxml file. The ApplicationRef
             for Teamcenter objects is (from a client point of view) - application='TcEng', label=teamcenter_uid,
             version=teamcenter_uid.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param ObjIds: 
                         ApplicationRef's of client domain context id.
             
        :return: structure. If (bExist) is true then the corresponding (id) will have the Teamcenter
             ApplicationRef, else (id) fields will be empty. The failed ids' will be in data member.
        """
        ...
    def ProcessStructure(self, TransferModeName: str, PlmxmlFileId: str, Config: Configuration) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Import a plmxml for a previously uploaded plmxml via getStructureWriteTicket, fcc
             method to upload the file and commitStructureFile (with no associated RequestObject
             - non AI plmxml import)
             

Note:

             For importing plmxml that contains datasets or other attachments you need to use
             importObjectsFromPLMXML from globalmultisite.ImportExportService.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param TransferModeName: 
                         The name of the transferMode in TC. Must be of ImportType.
             
        :param PlmxmlFileId: 
                         The id of the file from a prior call to commitStructureFile.
             
        :param Config: 
                         Configuration structure. If the id(Tag) member is specified, it must be the the tag
                         of ConfigurationContext or StructureContext or RevRule or VariantRule or storedOptionSetId,
                         or TransferMode. If this is a NULLTAG - then rulename will be used to find RevisionRule.
                         If both are empty, and useDefaultRevisionRule is true - the Teamcenter preferences
                         are used to pick up the rev rule. If all 3 are not used - then no revrule will be
                         used in the generation of plmxml.
             
        :return: errors during plmxml processing are returned in the return struct.
        """
        ...
    def CommitFiles(self, ReqObj: Teamcenter.Soa.Client.Model.Strong.RequestObject, Data: list[CommitFileData]) -> CommitFilesResponse:
        """    
             After a call to getFileWriteTickets - this method is to be used to create TeamCenter
             file objects - referencing the files in the volume.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param ReqObj: 
                         The optional id of the Request Object in TeamCenter. Optional if AI
                         is not being used. If RequestObject is not passed then specify NULL for this.
             
        :param Data: 
                         vector of CommitFileData elements - ticket, ApplicationRef and originalFileName combination.
                         The ApplicationRef element for each of the file must be the same as those present
                         in the plmxml file. filename - to be assigned to each of the TC file object. If path
                         is supplied with - it is stripped out.
             
        :return: list of successful tickets, failed originalFileNames. Reasons of failure - will be
             in ServiceData struct. ServiceData will have the list of Teamcenter File uids as
             plain objects, which can be retrieved by client if needed.
        """
        ...
    def CommitStructureFile(self, Id: Teamcenter.Soa.Client.Model.Strong.RequestObject, Ticket: FileTicket, PUpdate: str) -> CommitStructureFileResponse:
        """    
             This method is to be used to save a plmxml file after getting the write ticket using
             the GetStructureWriteTicket method.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Id: 
                         The optional id of the Request Object in TeamCenter. Optional if AI
                         is not being used. If RequestObject is not passed then specify NULL for this
                         parameter.
             
        :param Ticket: 
                         ticket obtained from a prior call to GetStructureWriteTicket method.
             
        :param PUpdate: 
                         If specified (only valid if id param is also specified), must be Full.
             
        :return: teamcenter FileUID. Reasons of failure - will be inServiceData struct.
        """
        ...
    def CreatePublishRequest(self, Id: Teamcenter.Soa.Client.Model.Strong.AppInterface, Detail: RequestDetail, PlmxmlFileName: str) -> CreatePublishRequestResponse:
        """    
             Create a new RequestObject of type Publish on the specified AI Object.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Id: 
                         The id of the AI Object in TeamCenter.
             
        :param Detail: 
                         The details like name,desc etc. to be set on the newly created
                         RequestObject
             
        :param PlmxmlFileName: 
                         optional. Only needed if  plmxml will be uploaded right away.
             
        :return: Failures will be returned in ServiceData. The created object is returned in data
             member. If plmxmlFileName is used as input - the FileTicket will have the FMS file
             write ticket. So, no additional call to getstructureWriteTicket is needed.
        """
        ...
    def DeleteProjects(self, ProjectIds: list[Teamcenter.Soa.Client.Model.Strong.AppInterface]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Delete the specified AI Objects from the Database.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param ProjectIds: 
                         any of the ids returned from a prior call to getProjects, or contructed from uid
             
        :return: Partial Failures will be returned in ServiceData and DeletedObjs will be marked in
             service data.
        """
        ...
    def DeleteRequests(self, RequestIds: list[Teamcenter.Soa.Client.Model.Strong.RequestObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Given 1 or more requestObjects - delete them from the database.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param RequestIds: 
                         The Request object list
             
        :return: partial Failures will be returned in ServiceData and the DeleteObjs list will be
             available.
        """
        ...
    def EndExchange(self, Id: Teamcenter.Soa.Client.Model.Strong.RequestObject, StateMsg: str, Info: StatusInfo) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Set Completed state on the Sync RequestObject or Pending state on a Publish RequestObject.
             StatusInfo and state description can be set by client
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Id: 
                         stateMsg
             
        :param StateMsg: 
                         message to be set as state message.
             
        :param Info: 
                         StatusInfo that is to be set on the RequestObject. For example: some test like Okay,normal.
                         Or, any reason of failure on client side etc.
             
        :return: Failures will be returned in ServiceData.  The updatedObject is available too.
        """
        ...
    def GenerateFullSyncRequest(self, Id: Teamcenter.Soa.Client.Model.Strong.AppInterface, Name: str, Description: str, BaseRefs: list[ApplicationRef]) -> GenerateFullSyncRequestResponse:
        """    
             Generate a Sync Request on a new AI or Existing AI object.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Id: 
                         The id of the Project(AI) object on which to generate the Sync Request Object
             
        :param Name: 
                         name to be given to the newly created Sync RequestObject. If no baseRefs argument
                         is specified                   then, this name is used as a lookup for existing sync
                         requests and that is processed. If no such                   request is found - then
                         the last existing sync request is processed.
             
        :param Description: 
                         description of the newly created Sync RequestObject. Not used if baseRefs is not
                         specified.
             
        :param BaseRefs: 
                         In the case of a newly createdAI object - this parameter specifies the the list of
                         database objects to be exported in the Sync. It is an error to specify this parameter
                         on an AI object having existing baseRefs. In such a case pass an empty vector.
             
        :return: partial Failures will be returned in ServiceData. And the newly created RequestObject
             will be available as createdObject in servicedata
        """
        ...
    def GetNextApprovedRequest(self, ProjectId: Teamcenter.Soa.Client.Model.Strong.AppInterface, CurReq: Teamcenter.Soa.Client.Model.Strong.RequestObject) -> GetNextApprovedRequestResponse:
        """    
             Given a  RequestObject get the next approved pending sync RequestObject.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param ProjectId: 
                         The Id of the AI object for which the next Pending,Sync Request is needed.
             
        :param CurReq: 
                         The current requestId with the client.
             
        :return: partial Failures will be returned in ServiceData(data) member , and the plainObject
             will have the RequestObject. ticket member will have the fms ticket to be used with
             fcc client to download the plmxml.
        """
        ...
    def GetProjectsInfo(self, AiIds: list[Teamcenter.Soa.Client.Model.Strong.AppInterface]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Get details of the specified AI Objects.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param AiIds: 
                         An array of ids obtained for which only uids are available, and data is needed from
                         Team Center.
             
        :return: serviceData will have a  vector of type Application Interface Objects - added as
             PlainObjects Partial failures are also reported in serviceData
        """
        ...
    def GetRequestsForProject(self, ProjectId: Teamcenter.Soa.Client.Model.Strong.AppInterface, Filter: StateFilter) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Given a Project(AI) object, get the RequestObjects based on the optional filter.
             default filter used: RequestType Sync and RequestState - pending.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param ProjectId: 
                         one of the ids returned from a prior call to getProjects.
             
        :param Filter: 
                         optional StateFilter where a combination of RequestStates and/or RequestTypes can
                         be specifed.
             
        :return: Partial Failures will be returned in ServiceData. ServiceData will contain the RequestObject
             Ids as plainObjects - so client Data Model can be used.
        """
        ...
    def GetRequestsInfo(self, ReqIds: list[Teamcenter.Soa.Client.Model.Strong.RequestObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Given a vector of RequestObjects, get details on those. This can be used if the RequestObject
             Ids are known. If not, GetProjectRequests can be used.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param ReqIds: 
                         1 or more RequestObject ids obtained from a prior call getProjectRequests or some
                         newly created ones using createPublishMethod. The reqIds are just wrappers around
                         a stored UID - perhaps obtained from plmxml or a prior call.
             
        :return: Partial Failures will be returned in ServiceData. The requestObjects (filled in)
             are available as plain objects in service data.
        """
        ...
    def GetStructureReadTicket(self, Id: Teamcenter.Soa.Client.Model.Strong.RequestObject, Type: str) -> GetStructureReadTicketResponse:
        """    
             Used to download the ticket for the plmxml file associated with the RequestObject.
             This ticket is then to be used with FCC client Proxy to download the file.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Id: 
                         The id of the Request Object in TeamCenter.
             
        :param Type: 
                         if specified must be Full.
             
        :return: fileticket is returned in the Response struct.
        """
        ...
    def ProcessPublishRequest(self, Id: Teamcenter.Soa.Client.Model.Strong.RequestObject) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Process(import) the plmxml corresponding to the RequestObject.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Id: 
                         The id of the Request Object in TeamCenter.
             
        :return: Failures will be returned in ServiceData.
        """
        ...
    def SetExchangeMessage(self, Id: Teamcenter.Soa.Client.Model.Strong.RequestObject, StateMsg: str, Info: StatusInfo) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Set any StatusInfo on the RequestObject and state description.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Id: 
                         The id of the RequestObject.
             
        :param StateMsg: 
                         The description to be set for the current requestObject state. Note you can't change
                         the state itself
             
        :param Info: 
                         StatusInfo that is to be set on the RequestObject
             
        :return: Failures will be returned in ServiceData.  The updatedObject is available too.
        """
        ...
    def SetProjectsInfo(self, ProjectIds: list[Teamcenter.Soa.Client.Model.Strong.AppInterface], Infos: list[ProjectInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Set details of the specified AI Objects from the supplied vector of ProjectInfo objects.
             You can only set targetAppProjectId, description and name fields.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param ProjectIds: 
                         An id returned from a prior call to GetProjects.
             
        :param Infos: 
                         ProjectInfo object containing the data to be set on AI's in database.
             
        :return: Any partial failures will be returned in ServiceData.
        """
        ...
    def StartExchange(self, Id: Teamcenter.Soa.Client.Model.Strong.RequestObject) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Set Communicating State on the RequestObject. To be called before uploading or downloading
             files to the RequestObject
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Id: 
                         The id of the RequestObject.
             
        :return: Failures will be returned in ServiceData. The createdObject is available in data.
        """
        ...

