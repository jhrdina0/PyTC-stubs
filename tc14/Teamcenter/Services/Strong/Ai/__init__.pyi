import System
import Teamcenter.Services.Strong.Ai._2006_03.Ai
import Teamcenter.Services.Strong.Ai._2007_12.Ai
import Teamcenter.Services.Strong.Ai._2008_05.Ai
import Teamcenter.Services.Strong.Ai._2008_06.Ai
import Teamcenter.Services.Strong.Ai._2009_06.Ai
import Teamcenter.Services.Strong.Ai._2009_10.Ai
import Teamcenter.Services.Strong.Ai._2010_09.Ai
import Teamcenter.Services.Strong.Ai._2012_09.Ai
import Teamcenter.Services.Strong.Ai._2013_05.Ai
import Teamcenter.Services.Strong.Ai._2013_12.Ai
import Teamcenter.Services.Strong.Ai._2014_12.Ai
import Teamcenter.Services.Strong.Ai._2018_06.Ai
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AiRestBindingStub(AiService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateProjects(self, ProjectDatas: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ProjectCreationData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GenerateStructure(self, IdsToProcess: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef], TransferModeName: str, Config: Teamcenter.Services.Strong.Ai._2006_03.Ai.Configuration, ServerMode: int) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.GenerateStructureResponse: ...
    def GetFileReadTickets(self, FileIds: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef]) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.GetFileReadTicketsResponse: ...
    def GetFileWriteTickets(self, OriginalFileNames: list[str], FileTypes: list[str]) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.GetFileWriteTicketsResponse: ...
    @typing.overload
    def GetProjects(self, Filter: Teamcenter.Services.Strong.Ai._2006_03.Ai.ProjectFilter) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def GetProjects(self, Filter: Teamcenter.Services.Strong.Ai._2012_09.Ai.ProjectFilter) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetPropertiesOfObjects(self, AppRefs: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef], PropertySetNames: list[str]) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.GetPropertiesOfObjectsResponse: ...
    def GetStructureWriteTicket(self, OriginalFileName: str) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.GetStructureWriteTicketResponse: ...
    def ObjectsExist(self, ObjIds: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef]) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.ObjectsExistResponse: ...
    def ProcessStructure(self, TransferModeName: str, PlmxmlFileId: str, Config: Teamcenter.Services.Strong.Ai._2006_03.Ai.Configuration) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CommitFiles(self, ReqObj: Teamcenter.Soa.Client.Model.Strong.RequestObject, Data: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.CommitFileData]) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.CommitFilesResponse: ...
    def CommitStructureFile(self, Id: Teamcenter.Soa.Client.Model.Strong.RequestObject, Ticket: Teamcenter.Services.Strong.Ai._2006_03.Ai.FileTicket, PUpdate: str) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.CommitStructureFileResponse: ...
    def CreatePublishRequest(self, Id: Teamcenter.Soa.Client.Model.Strong.AppInterface, Detail: Teamcenter.Services.Strong.Ai._2006_03.Ai.RequestDetail, PlmxmlFileName: str) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.CreatePublishRequestResponse: ...
    def DeleteProjects(self, ProjectIds: list[Teamcenter.Soa.Client.Model.Strong.AppInterface]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteRequests(self, RequestIds: list[Teamcenter.Soa.Client.Model.Strong.RequestObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def EndExchange(self, Id: Teamcenter.Soa.Client.Model.Strong.RequestObject, StateMsg: str, Info: Teamcenter.Services.Strong.Ai._2006_03.Ai.StatusInfo) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GenerateFullSyncRequest(self, Id: Teamcenter.Soa.Client.Model.Strong.AppInterface, Name: str, Description: str, BaseRefs: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef]) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.GenerateFullSyncRequestResponse: ...
    def GetNextApprovedRequest(self, ProjectId: Teamcenter.Soa.Client.Model.Strong.AppInterface, CurReq: Teamcenter.Soa.Client.Model.Strong.RequestObject) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.GetNextApprovedRequestResponse: ...
    def GetProjectsInfo(self, AiIds: list[Teamcenter.Soa.Client.Model.Strong.AppInterface]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetRequestsForProject(self, ProjectId: Teamcenter.Soa.Client.Model.Strong.AppInterface, Filter: Teamcenter.Services.Strong.Ai._2006_03.Ai.StateFilter) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetRequestsInfo(self, ReqIds: list[Teamcenter.Soa.Client.Model.Strong.RequestObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetStructureReadTicket(self, Id: Teamcenter.Soa.Client.Model.Strong.RequestObject, Type: str) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.GetStructureReadTicketResponse: ...
    def ProcessPublishRequest(self, Id: Teamcenter.Soa.Client.Model.Strong.RequestObject) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetExchangeMessage(self, Id: Teamcenter.Soa.Client.Model.Strong.RequestObject, StateMsg: str, Info: Teamcenter.Services.Strong.Ai._2006_03.Ai.StatusInfo) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def SetProjectsInfo(self, ProjectIds: list[Teamcenter.Soa.Client.Model.Strong.AppInterface], Infos: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ProjectInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def SetProjectsInfo(self, Infos: list[Teamcenter.Services.Strong.Ai._2012_09.Ai.ProjectInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def StartExchange(self, Id: Teamcenter.Soa.Client.Model.Strong.RequestObject) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GenerateScopedMultipleStructure(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[Teamcenter.Services.Strong.Ai._2007_12.Ai.ObjectsWithConfig], ExportTransferMode: str, ServerMode: int) -> Teamcenter.Services.Strong.Ai._2007_12.Ai.GenerateScopedMultipleStructureResponse: ...
    def GenerateScopedSyncRequest(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[Teamcenter.Services.Strong.Ai._2007_12.Ai.ObjectsWithConfig], RequestDetail: Teamcenter.Services.Strong.Ai._2006_03.Ai.RequestDetail) -> Teamcenter.Services.Strong.Ai._2007_12.Ai.GenerateScopedSyncRequestResponse: ...
    def GenerateArrangements(self, ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision, RevRule: Teamcenter.Services.Strong.Ai._2006_03.Ai.Configuration, BvType: str) -> Teamcenter.Services.Strong.Ai._2008_05.Ai.GenerateArrangementsResponse: ...
    def CompareConfigurationContexts(self, ConfigurationsToCompare: list[Teamcenter.Services.Strong.Ai._2008_06.Ai.ConfigurationContextPair]) -> Teamcenter.Services.Strong.Ai._2008_06.Ai.CompareConfigurationContextsResponse: ...
    def GenerateScopedMultipleStructure2(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[Teamcenter.Services.Strong.Ai._2008_06.Ai.ObjectsWithConfig], ExportTransferMode: str, ServerMode: int) -> Teamcenter.Services.Strong.Ai._2008_06.Ai.GenerateScopedMultipleStructure2Response: ...
    def GenerateScopedSyncRequest2(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[Teamcenter.Services.Strong.Ai._2008_06.Ai.ObjectsWithConfig], RequestDetail: Teamcenter.Services.Strong.Ai._2006_03.Ai.RequestDetail) -> Teamcenter.Services.Strong.Ai._2008_06.Ai.GenerateScopedSyncRequest2Response: ...
    def GetPersistentObjects(self, InputLines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GenerateScopedMultipleStructure3(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[Teamcenter.Services.Strong.Ai._2008_06.Ai.ObjectsWithConfig], ExportTransferMode: str, ServerMode: int) -> Teamcenter.Services.Strong.Ai._2009_06.Ai.GenerateScopedMultipleStructure3Response: ...
    def GetPropertyValues(self, Input: list[Teamcenter.Services.Strong.Ai._2009_10.Ai.GetPropertyValuesData]) -> Teamcenter.Services.Strong.Ai._2009_10.Ai.GetPropertyValuesResponse: ...
    def GenerateAndEvaluateStructure(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[Teamcenter.Services.Strong.Ai._2008_06.Ai.ObjectsWithConfig], ExportTransferMode: str, AbsoluteXmlFileName: str, Xpaths: list[str]) -> Teamcenter.Services.Strong.Ai._2010_09.Ai.GenerateAndEvaluateStructureResponse: ...
    def FindRequests(self, Filter: Teamcenter.Services.Strong.Ai._2012_09.Ai.FindRequestsFilter) -> Teamcenter.Services.Strong.Ai._2012_09.Ai.FindRequestsResponse: ...
    def SetRequestsInfo(self, Infos: list[Teamcenter.Services.Strong.Ai._2012_09.Ai.RequestInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetProjectsInfo2(self, Projects: list[Teamcenter.Soa.Client.Model.Strong.AppInterface]) -> Teamcenter.Services.Strong.Ai._2012_09.Ai.GetProjectsInfo2Response: ...
    def GetRequestsInfo2(self, Robjects: list[Teamcenter.Soa.Client.Model.Strong.RequestObject]) -> Teamcenter.Services.Strong.Ai._2012_09.Ai.GetRequestsInfo2Response: ...
    def FindRequestOnAiWithReferences(self, BaseRef: list[Teamcenter.Soa.Client.Model.ModelObject], RequestType: str) -> Teamcenter.Services.Strong.Ai._2013_05.Ai.FindRequestOnAiWithReferencesResponse: ...
    def FindRequestsWithDependencies(self, Filter: Teamcenter.Services.Strong.Ai._2013_12.Ai.FindRequestsWithDependencyFilter) -> Teamcenter.Services.Strong.Ai._2012_09.Ai.FindRequestsResponse: ...
    def CreateApplicationInterfaceRecords(self, Input: list[Teamcenter.Services.Strong.Ai._2014_12.Ai.CreateAppInterfaceRecordInput]) -> Teamcenter.Services.Strong.Ai._2014_12.Ai.CreateAppInterfaceRecordsResponse: ...
    def GetMappedApplicationRefs(self, AppRefs: list[Teamcenter.Services.Strong.Ai._2014_12.Ai.GetMappedAppRefsInput]) -> Teamcenter.Services.Strong.Ai._2014_12.Ai.GetMappedAppRefsResponse: ...
    def GetObjectsByApplicationRefs(self, Input: list[Teamcenter.Services.Strong.Ai._2018_06.Ai.ConfigurationInfo]) -> Teamcenter.Services.Strong.Ai._2018_06.Ai.GetObjectsByApplicationRefsResponse: ...

class AiService:
    """
    
            Contains Ai Services
            


Library Reference:

TcSoaAiStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> AiService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateProjects(self, ProjectDatas: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ProjectCreationData]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def GenerateStructure(self, IdsToProcess: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef], TransferModeName: str, Config: Teamcenter.Services.Strong.Ai._2006_03.Ai.Configuration, ServerMode: int) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.GenerateStructureResponse:
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
    def GetFileReadTickets(self, FileIds: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef]) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.GetFileReadTicketsResponse:
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
    def GetFileWriteTickets(self, OriginalFileNames: list[str], FileTypes: list[str]) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.GetFileWriteTicketsResponse:
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
    @typing.overload
    def GetProjects(self, Filter: Teamcenter.Services.Strong.Ai._2006_03.Ai.ProjectFilter) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def GetProjects(self, Filter: Teamcenter.Services.Strong.Ai._2012_09.Ai.ProjectFilter) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetPropertiesOfObjects(self, AppRefs: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef], PropertySetNames: list[str]) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.GetPropertiesOfObjectsResponse:
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
    def GetStructureWriteTicket(self, OriginalFileName: str) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.GetStructureWriteTicketResponse:
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
    def ObjectsExist(self, ObjIds: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef]) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.ObjectsExistResponse:
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
    def ProcessStructure(self, TransferModeName: str, PlmxmlFileId: str, Config: Teamcenter.Services.Strong.Ai._2006_03.Ai.Configuration) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def CommitFiles(self, ReqObj: Teamcenter.Soa.Client.Model.Strong.RequestObject, Data: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.CommitFileData]) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.CommitFilesResponse:
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
    def CommitStructureFile(self, Id: Teamcenter.Soa.Client.Model.Strong.RequestObject, Ticket: Teamcenter.Services.Strong.Ai._2006_03.Ai.FileTicket, PUpdate: str) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.CommitStructureFileResponse:
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
    def CreatePublishRequest(self, Id: Teamcenter.Soa.Client.Model.Strong.AppInterface, Detail: Teamcenter.Services.Strong.Ai._2006_03.Ai.RequestDetail, PlmxmlFileName: str) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.CreatePublishRequestResponse:
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
    def EndExchange(self, Id: Teamcenter.Soa.Client.Model.Strong.RequestObject, StateMsg: str, Info: Teamcenter.Services.Strong.Ai._2006_03.Ai.StatusInfo) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def GenerateFullSyncRequest(self, Id: Teamcenter.Soa.Client.Model.Strong.AppInterface, Name: str, Description: str, BaseRefs: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef]) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.GenerateFullSyncRequestResponse:
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
    def GetNextApprovedRequest(self, ProjectId: Teamcenter.Soa.Client.Model.Strong.AppInterface, CurReq: Teamcenter.Soa.Client.Model.Strong.RequestObject) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.GetNextApprovedRequestResponse:
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
    def GetRequestsForProject(self, ProjectId: Teamcenter.Soa.Client.Model.Strong.AppInterface, Filter: Teamcenter.Services.Strong.Ai._2006_03.Ai.StateFilter) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def GetStructureReadTicket(self, Id: Teamcenter.Soa.Client.Model.Strong.RequestObject, Type: str) -> Teamcenter.Services.Strong.Ai._2006_03.Ai.GetStructureReadTicketResponse:
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
    def SetExchangeMessage(self, Id: Teamcenter.Soa.Client.Model.Strong.RequestObject, StateMsg: str, Info: Teamcenter.Services.Strong.Ai._2006_03.Ai.StatusInfo) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    @typing.overload
    def SetProjectsInfo(self, ProjectIds: list[Teamcenter.Soa.Client.Model.Strong.AppInterface], Infos: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ProjectInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def SetProjectsInfo(self, Infos: list[Teamcenter.Services.Strong.Ai._2012_09.Ai.ProjectInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
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
    def GenerateScopedMultipleStructure(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[Teamcenter.Services.Strong.Ai._2007_12.Ai.ObjectsWithConfig], ExportTransferMode: str, ServerMode: int) -> Teamcenter.Services.Strong.Ai._2007_12.Ai.GenerateScopedMultipleStructureResponse:
        """    
             GenerateScopedMultipleStructure: Same as GenerateScopedSyncRequest - except no aiObject
             is needed. If specified - it is only used to get the TransferMode (in case the exportTransferMode
             is not specified). objects or occurrence group objects - specified as application
             refs. The configuration is optional if the ids consist of StructureContexts. ApplicationRefs
             can be ids of occurrence from a previous export from TC, or APNs or AbsOccs, or OccurrenceGroup
             or an Item/Itemrev(only one in that last case). If the Appref is custom (non TcEng
             AppRef), occurrence appref must resolve to AbsOccurrence or APN ), or they can be
             ids of structure context/occurrence group objects. The return is the transient file
             ticket for the plmxml file generated. In case any of the input apprefs cannot be
             processed they will be returned in the data member of response. Errors during plmxml
             processing will be returned in partialerror as xml string, based on TcError.xsd in
             iman_data folder. Configuration structure can be used to specify default revrule
             (if true) all other fields are ignored. Basically, they are declared in the order
             of precedence (where duplication is possible).
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param AiObject: 
                         The Application Interface object under which the new sync request is to be created.
             
        :param ObjectsToProcess: 
                         The list of objects for which a single plmxml will be generated. The configuration
                         for each of the                             object is also specified here.
             
        :param ExportTransferMode: 
                         Name of the transfermode for exporting plmxml.
             
        :param ServerMode: 
                         values are 2 or 4 (2-tier or 4-tier). Used in the generation of transient ticket.
             
        :return: partial failures are returned in data.
        """
        ...
    def GenerateScopedSyncRequest(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[Teamcenter.Services.Strong.Ai._2007_12.Ai.ObjectsWithConfig], RequestDetail: Teamcenter.Services.Strong.Ai._2006_03.Ai.RequestDetail) -> Teamcenter.Services.Strong.Ai._2007_12.Ai.GenerateScopedSyncRequestResponse:
        """    
             Generates a new Sync Request for the given occurrences (from any context) or Structure
             Context objects or occurrence group objects - specified as application refs. The
             configuration is optional if the ids consist of StructureContexts. ApplicationRefs
             can be ids of occurrence from a previous export from TC, or APNs or AbsOccs, or OccurrenceGroup
             or an Item/Itemrev(only one in that last case). If the Appref is custom (non TcEng
             AppRef), occurrence appref must resolve to AbsOccurrence or APN ), or they can be
             ids of structure context/occurrence group objects. The return will be the details
             of the newly created Sync Request. Note that the name, desc, scope, updateType of
             this request are based on the passed in requestDetail. The other fields of the RequestDetail
             are not used during input. In case any of the input apprefs cannot be processed they
             will be returned in the failedIndices structure. Errors during plmxml processing
             will be returned in partialerror , based on TcError.xsd in iman_data folder.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param AiObject: 
                         The Application Interface object under which the new sync request is to be created.
             
        :param ObjectsToProcess: 
                         The list of objects for which a single plmxml will be generated. The configuration
                         for each of the                             object is also specified here.
             
        :param RequestDetail: 
                         The details (name, description, scope, updateType(incremental)) are used in the creation
                         of the sync request. Set the scope type to RequestScope_Whole and updatetype to UpdateType_Full
                         if this structure is not to be used.
             
        :return: partial failures are returned in data.
        """
        ...
    def GenerateArrangements(self, ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision, RevRule: Teamcenter.Services.Strong.Ai._2006_03.Ai.Configuration, BvType: str) -> Teamcenter.Services.Strong.Ai._2008_05.Ai.GenerateArrangementsResponse:
        """    
             The generateArrangements operation will generate a PLMXML file with arrangements
             for an Item Revision. This operation will find out the BOMView Revision with input
             BOMView Type associated to the Item Revision at first and then do generating process.
             An Item Revision and a BOMView Type can specify an unique BOMView Revision. If input
             BOMView Type is NULL, the default BOMView Type will be picked up. A revision rule
             can be applied to the BOMView Revision while generating. The output is struct GenerateArrangementsResponse
             with generated PLMXML file ticket and soa service data.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param ItemRev: 
                         The Item Revision object to generate arrangements from.
             
        :param RevRule: 
                         The revision rule to be applied to BOMView Revision of input Item Revision.
             
        :param BvType: 
                         The BOMView Type name to be used to specify the BOMView Revision of the input Item
                         Revision. There may be more than one BOMView Revision associated to an Item Revision
                         with different BOMView Types. If the input BOMView Type name is NULL, the default
                         BOMView Type will be used to pick up the BOMView Revision.
             
        :return: The FMS ticket to generated PLMXML file and any partial failures.
        """
        ...
    def CompareConfigurationContexts(self, ConfigurationsToCompare: list[Teamcenter.Services.Strong.Ai._2008_06.Ai.ConfigurationContextPair]) -> Teamcenter.Services.Strong.Ai._2008_06.Ai.CompareConfigurationContextsResponse:
        """    
             compareConfigurationContexts: allows clients to check if configurationcontext with
             different uids are equivalent or not. This is because a configurationcontext is used
             to capture runtime revisionrules and there might be 2 configurationcontext created
             with same set of runtime rules. This interface is for backward compatibility with
             Ai. configurationsToCompare pairs of configurationContexts to compare with one other.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param ConfigurationsToCompare: 
                         vector of configurations to compare.
             
        :return: a bool vector which has the results for successful comparisions - either true or
             false. Any pair that gives an error - the index of such a failed error is returned
             in the serviceData member.
        """
        ...
    def GenerateScopedMultipleStructure2(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[Teamcenter.Services.Strong.Ai._2008_06.Ai.ObjectsWithConfig], ExportTransferMode: str, ServerMode: int) -> Teamcenter.Services.Strong.Ai._2008_06.Ai.GenerateScopedMultipleStructure2Response:
        """    
             GenerateScopedMultiple2Structure: Same as GenerateScopedSyncRequest2 - except no
             aiObject is needed. If specified - it is only used to get the TransferMode (in case
             the exportTransferMode is not specified). objects or occurrence group objects - specified
             as application refs. The configuration is optional if the ids consist of StructureContexts.
             ApplicationRefs can be ids of occurrence from a previous export from TC, or APNs
             or AbsOccs, or OccurrenceGroup or an Item/Itemrev(only one in that last case). If
             the Appref is custom (non TcEng AppRef), occurrence appref must resolve to AbsOccurrence
             or APN ), or they can be ids of structure context/occurrence group objects. The return
             is the transient file ticket for the plmxml file generated. In case any of the input
             apprefs cannot be processed they will be returned in the data member of response.
             Errors during plmxml processing will be returned in partialerror as xml string, based
             on TcError.xsd in iman_data folder. Configuration structure can be used to specify
             default revrule (if true) all other fields are ignored. Basically, they are declared
             in the order of precedence (where duplication is possible).
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param AiObject: 
                         The Application Interface object under which the new sync request is to be created.
             
        :param ObjectsToProcess: 
                         The list of objects for which a single plmxml will be generated. The configuration
                         for each of the                             object is also specified here.
             
        :param ExportTransferMode: 
                         Name of the transfermode for exporting plmxml.
             
        :param ServerMode: 
                         values are 2 or 4 (2-tier or 4-tier). Used in the generation of transient ticket.
             
        :return: partial failures are returned in data.
        """
        ...
    def GenerateScopedSyncRequest2(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[Teamcenter.Services.Strong.Ai._2008_06.Ai.ObjectsWithConfig], RequestDetail: Teamcenter.Services.Strong.Ai._2006_03.Ai.RequestDetail) -> Teamcenter.Services.Strong.Ai._2008_06.Ai.GenerateScopedSyncRequest2Response:
        """    
             generateScopedSyncRequest2: Generates a new Sync Request for the given occurrences
             (from any context) or Structure Context objects or occurrence group objects - specified
             as application refs. The configuration is optional if the ids consist of StructureContexts.
             ApplicationRefs can be ids of occurrence from a previous export from TC, or APNs
             or AbsOccs, or OccurrenceGroup or an Item/Itemrev(only one in that last case). If
             the Appref is custom (non TcEng AppRef), occurrence appref must resolve to AbsOccurrence
             or APN ), or they can be ids of structure context/occurrence group objects. The return
             will be the details of the newly created Sync Request. Note that the name, desc,
             scope, updateType of this request are based on the passed in requestDetail. The other
             fields of the RequestDetail are not used during input. In case any of the input apprefs
             cannot be processed they will be returned in the failedIndices structure. Errors
             during plmxml processing will be returned in partialerror , based on TcError.xsd
             in iman_data folder. This differs from generateScopedSyncRequest, in that it allows
             you to specify the reference structures for process.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param AiObject: 
                         The Application Interface object under which the new sync request is to be created.
             
        :param ObjectsToProcess: 
                         The list of objects for which a single plmxml will be generated. The configuration
                         for each of the                             object is also specified here.
             
        :param RequestDetail: 
                         The details (name, description, scope, updateType(incremental)) are used in the creation
                         of the sync request. Set the scope type to RequestScope_Whole and updatetype to UpdateType_Full
                         if this structure is not to be used.
             
        :return: partial failures are returned in data.
        """
        ...
    def GetPersistentObjects(self, InputLines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Given a set of bomlines from the same window, create a private structure context
             and return that. If the input contains any persistent objects like a workspaceobject
             - those will be returned as is.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param InputLines: 
                         list of bomlines from the same bomwindow, for which a StructureContext needs to be
                         created. Note that if input has persistent objects - they will be returned as is.
             
        :return: The serviceData willl have any newly created StructureContext object and partialErrors.
             In addition - if any persistent objects are passed in - they will be returned as
             objects.
        """
        ...
    def GenerateScopedMultipleStructure3(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[Teamcenter.Services.Strong.Ai._2008_06.Ai.ObjectsWithConfig], ExportTransferMode: str, ServerMode: int) -> Teamcenter.Services.Strong.Ai._2009_06.Ai.GenerateScopedMultipleStructure3Response:
        """    
             GenerateScopedMultipleStructure3: Same as GenerateScopedMultipleStructure2 - except
             filetickets are returned. If aiObject is specified - it is only used to get the TransferMode
             (in case the exportTransferMode is not specified). objects or occurrence group objects
             - specified as application refs. The configuration is optional if the ids consist
             of StructureContexts. ApplicationRefs can be ids of occurrence from a previous export
             from TC, or APNs or AbsOccs, or OccurrenceGroup or an Item/Itemrev(only one in that
             last case). If the Appref is custom (non TcEng AppRef), occurrence appref must resolve
             to AbsOccurrence or APN ), or they can be ids of structure context/occurrence group
             objects. The return is the transient file ticket for the plmxml file generated. In
             case any of the input apprefs cannot be processed they will be returned in the data
             member of response. Errors during plmxml processing will be returned in partialerror
             as xml string, based on TcError.xsd in iman_data folder. Configuration structure
             can be used to specify default revrule (if true) all other fields are ignored. Basically,
             they are declared in the order of precedence (where duplication is possible).
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param AiObject: 
                         The Application Interface object under which the new sync request is to be created.
             
        :param ObjectsToProcess: 
                         The list of objects for which a single plmxml will be generated. The configuration
                         for each of the                             object is also specified here.
             
        :param ExportTransferMode: 
                         Name of the transfermode for exporting plmxml.
             
        :param ServerMode: 
                         values are 2 or 4 (2-tier or 4-tier). Used in the generation of transient ticket.
             
        :return: partial failures are returned in data.
        """
        ...
    def GetPropertyValues(self, Input: list[Teamcenter.Services.Strong.Ai._2009_10.Ai.GetPropertyValuesData]) -> Teamcenter.Services.Strong.Ai._2009_10.Ai.GetPropertyValuesResponse:
        """    
             get the property values for the object supplied as ApplicationReferences and configuration.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Input: 
                         array of input structure - each of which specifies the object and configuration,
                         along with properties.
             
        :return: return the property values for the input properties and objects.
        """
        ...
    def GenerateAndEvaluateStructure(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[Teamcenter.Services.Strong.Ai._2008_06.Ai.ObjectsWithConfig], ExportTransferMode: str, AbsoluteXmlFileName: str, Xpaths: list[str]) -> Teamcenter.Services.Strong.Ai._2010_09.Ai.GenerateAndEvaluateStructureResponse:
        """    
             Service to generate a plmxml based on the input objects, configuration, transfermode
             provided and  evaluate the specified xpaths 1.0 expressions against that plmxml.
             Optionally - a pre-existing xml file can be specified (via a full path accessible
             in tc server environment). In that case, only the xpaths argument is used along with
             the absoluteXmlFile argument.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param AiObject: 
                         This parameter is optional (specify NULL if not used). If specified, will be used
                         to get the export transfermode name to be used for plmxml generation.
             
        :param ObjectsToProcess: 
                         A mandatory parameter. If not specified an exception will be thrown. The list of
                         objects for which a single plmxml will be generated. The configuration for each of
                         the object is also specified here.
             
        :param ExportTransferMode: 
                         The transfermode to use for generating the plmxml file. If not specified, the aiObject's
                         transfermode is used. If neither is specified - an exception will be thrown.
             
        :param AbsoluteXmlFileName: 
                         In case there is already a plmxml file generated and available on the tcserver environment,
                         then instead of passing objectsToProcess - this argument can be passed with the absolute
                         path name of such a file. If this is specified -  only the xpaths argument is used,
                         unless the file does not exist - in which case it will be created using the other
                         arguments.
             
        :param Xpaths: 
                         The list of xpath 1.0 expressions to be used for evaluation on top of the generated
                         plmxml.
             
        :return: return the map of xpath expression to it's evaluations and any errors in serviceData.
             If an xml file is generated - the transient ticket for that file is also returned.
        """
        ...
    def FindRequests(self, Filter: Teamcenter.Services.Strong.Ai._2012_09.Ai.FindRequestsFilter) -> Teamcenter.Services.Strong.Ai._2012_09.Ai.FindRequestsResponse:
        """    
             method to find request objects based on the input criteria.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Filter: 
                         Mandatory input field for filtering Request objects as per the input criteria.
             
        :return: list of found requests and any  partial errors.
        """
        ...
    def SetRequestsInfo(self, Infos: list[Teamcenter.Services.Strong.Ai._2012_09.Ai.RequestInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             method to allow caller to set the fields on the RequestObject.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Infos: 
                         vector of info elements to set data on respective RequestObject.
             
        :return: ServiceData that captures partial failures, and also list of updated objects if data
             is set successfully.
        """
        ...
    def GetProjectsInfo2(self, Projects: list[Teamcenter.Soa.Client.Model.Strong.AppInterface]) -> Teamcenter.Services.Strong.Ai._2012_09.Ai.GetProjectsInfo2Response:
        """    
             return the projectInfo information for each of the supplied ApplicationInterface
             Objects.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Projects: 
                         list of Application Interface objects for which the details are needed.
             
        :return: return the info for the provided Application Interface Objects, and any partial errors
             - the Application Interface Objects position in the passed in vector will be used
             as the clientId for errors
        """
        ...
    def GetRequestsInfo2(self, Robjects: list[Teamcenter.Soa.Client.Model.Strong.RequestObject]) -> Teamcenter.Services.Strong.Ai._2012_09.Ai.GetRequestsInfo2Response:
        """    
             get details about specific RequestObjects. These include state desc,status info,
             custom key value pairs.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Robjects: 
                         input vector of RequestObjects for which details are needed.
             
        :return: vector or RequestDetails. The size of this vector may not be same as input vector.
             Partial errors are recorded in serviceData.
        """
        ...
    def FindRequestOnAiWithReferences(self, BaseRef: list[Teamcenter.Soa.Client.Model.ModelObject], RequestType: str) -> Teamcenter.Services.Strong.Ai._2013_05.Ai.FindRequestOnAiWithReferencesResponse:
        """    
             The operation queries for the latest RequestObjects (by creation date and
             type) on the latest ApplicationInterface Object ( by creation date) that references
             the input object in the base_refs member. Additional filtering based on type of RequestObject
             is also possible.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param BaseRef: 
                         The input is set based.
             
        :param RequestType: 
<ul>
<li type="disc">Sync
                         </li>
<li type="disc">Publish
                         </li>
<li type="disc">All (default if value is not one of Sync or Publish including NULL)
                         </li>
</ul>

        :return: 
        """
        ...
    def FindRequestsWithDependencies(self, Filter: Teamcenter.Services.Strong.Ai._2013_12.Ai.FindRequestsWithDependencyFilter) -> Teamcenter.Services.Strong.Ai._2012_09.Ai.FindRequestsResponse:
        """    
             This operation is based on dependency between the related  RequestObjects and on
             the input criteria provided to the operation input. The operation will return a list
             of RequestObjects to process. The returned RequestObjects are those whose property
             "type" is of value "Sync" and property "state" is of value "Pending". Further, this
             operation returns only those RequestObjects which are dependent on RequestObjects
             whose state is "Completed".  Dependency of RequestObject is determined by "fnd0pred_list"
             property. This property points to its preceding Request Object.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Filter: 
                         method to find request objects after considering dependency, based on the input criteria.
             
        :return: 203822 (search by request state not allowed)
        """
        ...
    def CreateApplicationInterfaceRecords(self, Input: list[Teamcenter.Services.Strong.Ai._2014_12.Ai.CreateAppInterfaceRecordInput]) -> Teamcenter.Services.Strong.Ai._2014_12.Ai.CreateAppInterfaceRecordsResponse:
        """    
             This operation creates RecordObjects for the specified labels in the MasterRecord
             associated with the input AppInterface object. Input labels are PLMXML style
             label strings of ApplicationRef element related to Application type "Teamcenter".
             

Use Cases:

Use Case 1: Creating RecordObjects for specified PLMXML labels.

             This operation should be used to create RecordObjects for  Teamcenter Application
             References which were not exported via PLMXML. Typical case would be Light Weight
             BOM APIs are used to get the data, but, later there is a need to do a PLMXML import
             using AppInterface object.
             



Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Input: 
                         The details of <b>AppInterface</b> and set of labels for which <b>RecordObjects</b>
                         are to be created
             
        :return: 
        """
        ...
    def GetMappedApplicationRefs(self, AppRefs: list[Teamcenter.Services.Strong.Ai._2014_12.Ai.GetMappedAppRefsInput]) -> Teamcenter.Services.Strong.Ai._2014_12.Ai.GetMappedAppRefsResponse:
        """    
             This operation searches for objects with specified Application References and returns
             the matching Application References with specified Application names. Application
             Reference is a 3-tuple construct with name, label and version strings. This is used
             in PLMXML exchange between Teamcenter and target applications to uniquely identity
             Teamcenter entities like Item, ItemRevision, Form objects etc.
             

Use Cases:

Use Case 1: Getting Teamcenter Application References for non Teamcenter Application
             References.
             
             This operation can be used to fetch the Application References of Teamcenter given
             non Teamcenter Application References. These are typically used in PLMXML interchange.
             
Use Case 2: Getting non Teamcenter Application References for Teamcenter Application
             References.
             
             This operation can be used to fetch the Application References of non Teamcenter
             Application References given Teamcenter Application References. These are typically
             used in PLMXML interchange.
             


Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param AppRefs: 
                         The details of Application References for which correponding Application References
                         with different Application names are required.
             
        :return: 
        """
        ...
    def GetObjectsByApplicationRefs(self, Input: list[Teamcenter.Services.Strong.Ai._2018_06.Ai.ConfigurationInfo]) -> Teamcenter.Services.Strong.Ai._2018_06.Ai.GetObjectsByApplicationRefsResponse:
        """    
             This operation finds business objects associated with the list of input ApplicationRef
             objects. The ApplicationRef can be associated with either persisent or runtime
             business objects. One business object is returned for each ApplicationRef.
             If no associated business object can be found for an ApplicationRef then a
             NULL  is returned for that entry.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         A list of <i>ConfigurationInformation</i> objects specifying the configuration and
                         <b>ApplicationRef</b> objects for which the associated business objects are needed.
             
        :return: 
        """
        ...

