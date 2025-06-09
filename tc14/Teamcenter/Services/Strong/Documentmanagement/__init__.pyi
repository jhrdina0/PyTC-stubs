import System
import Teamcenter.Services.Strong.Documentmanagement._2007_01.DocumentTemplate
import Teamcenter.Services.Strong.Documentmanagement._2008_06.DocumentControl
import Teamcenter.Services.Strong.Documentmanagement._2010_04.DigitalSignature
import Teamcenter.Services.Strong.Documentmanagement._2010_04.LaunchDefinition
import Teamcenter.Services.Strong.Documentmanagement._2011_06.AttributeExchange
import Teamcenter.Services.Strong.Documentmanagement._2013_12.PrintOrRender
import Teamcenter.Services.Strong.Documentmanagement._2018_11.PrintOrRender
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class AttributeExchangeRestBindingStub(AttributeExchangeService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ResolveAttrMappingsAndGetProperties(self, Info: list[Teamcenter.Services.Strong.Documentmanagement._2011_06.AttributeExchange.ResolveAttrMappingsAndGetPropertiesInfo]) -> Teamcenter.Services.Strong.Documentmanagement._2011_06.AttributeExchange.ResolveAttrMappingsAndGetPropertiesResponse: ...
    def ResolveAttrMappingsAndSetProperties(self, Info: list[Teamcenter.Services.Strong.Documentmanagement._2011_06.AttributeExchange.ResolveAttrMappingsAndSetPropertiesInfo]) -> Teamcenter.Services.Strong.Documentmanagement._2011_06.AttributeExchange.ResolveAttrMappingsAndSetPropertiesResponse: ...
    def UpdateDocumentProperties(self, InputObjects: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision], CheckConfiguration: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class AttributeExchangeService:
    """
    
            This service provides operations for metadata exchange between Teamcenter properties
            and the application client (for example: Microsoft Office Word application).   It
            supports the metadata exchange for the following property types: char, double,
            float, short, int, logical, string, and date.
            


Library Reference:

TcSoaDocumentManagementStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> AttributeExchangeService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ResolveAttrMappingsAndGetProperties(self, Info: list[Teamcenter.Services.Strong.Documentmanagement._2011_06.AttributeExchange.ResolveAttrMappingsAndGetPropertiesInfo]) -> Teamcenter.Services.Strong.Documentmanagement._2011_06.AttributeExchange.ResolveAttrMappingsAndGetPropertiesResponse:
        """    
             This operation processes the metadata exchange mapping information between the client
             application and Teamcenter from the provided input list of ResolveAttrMappingsAndGetPropertiesInfo
             structure (containing the metadata exchange mapping information from the client application).
             The operation then gets and returns the property  values of the corresponding Teamcenter
             object from provided input information.
             

Use Cases:

Metadata exchange between Teamcenter and Microsoft Office Word application

             From the Teamcenter client for Microsoft Office Word 2010, a user opens and checks
             out a WordX Dataset.  User then clicks on the Teamcenter ribbon and clicks on Attribute
             Exchange> Configurations> Create.  From here user can set up the metadata exchange
             between the properties of the Microsoft Office Word file properties and the properties
             of the Teamcenter object.
             

             In the configuration, user can set the direction of the metadata exchange either
             as File to Teamcenter, Teamcenter to File, or Two Way.  In this case, user selects
             Teamcenter to File for the metadata exchange from the client to Teamcenter.  User
             sets up the property mapping by selecting a file property (Comments for example)
             and selecting a Teamcenter object property (object_desc for example), and saves the
             attribute exchange configuration.  User then clicks on Attribute Exchange>Reload
             button.  The Microsoft Office Word initiates this operation and gets Teamcenter object
             property (object_desc for example) value back.  To verify the client file property
             gets updated, from Microsoft Office Word menu File, select Info (in the left panel),
             then select Properties (in the right panel), then select Show Document Panel.
             


Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param Info: 
                         It contains the attribute exchange mappings information.
             
        :return: 
        """
        ...
    def ResolveAttrMappingsAndSetProperties(self, Info: list[Teamcenter.Services.Strong.Documentmanagement._2011_06.AttributeExchange.ResolveAttrMappingsAndSetPropertiesInfo]) -> Teamcenter.Services.Strong.Documentmanagement._2011_06.AttributeExchange.ResolveAttrMappingsAndSetPropertiesResponse:
        """    
             This operation processes the metadata exchange mapping information between the client
             and Teamcenter from the provided input list of ResolveAttrMappingsAndSetPropertiesInfo
             structure (containing the metadata exchange mapping information from the client application).
             The operation sets the Teamcenter property values based on the provided input information.
             


Use Cases:

Metadata exchange between Teamcenter and Microsoft Office Word application


             From the Teamcenter client for Microsoft Office Word 2010, a user opens and checks
             out a WordX Dataset.  User then clicks on the Teamcenter ribbon and clicks on Attribute
             Exchange >Configurations>Create.  From here user can set up the metadata exchange
             between the properties of the Microsoft Office Word file and the properties of the
             Teamcenter object.
             

             In the configuration, user can set the direction of the metadata exchange either
             as File to Teamcenter, Teamcenter to File, or Two Way.  In this case, user selects
             File to Teamcenter for the metadata exchange, pick a file property (Comment for example),
             pick a Teamcenter object property (object_desc for example), and save the attribute
             exchange configuration.  From Microsoft Office Word menu File, select Info (left
             panel), then select Properties (right panel)>Show Document Panel.  Update the Comments
             text box in the Document Properties Panel with some text.  Now select Teamcenter
             ribbon and click on Save.  Save and check in the Dataset.  During this process, the
             Microsoft Office Word initiates this operation and updates Teamcenter object property
             (object_desc for example) value.  User can verify the Teamcenter object property
             (object_desc for example) by login to a Teamcenter client such as Rich Application
             Client (RAC), do a View properties on the Teamcenter object.
             


Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param Info: 
                         It contains information for Resolving the attribute exchange and the value to be
                         set on the Teamcenter attribute.
             
        :return: that has failure along with the corresponding
             list of client properties and error messages).
        """
        ...
    def UpdateDocumentProperties(self, InputObjects: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision], CheckConfiguration: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class DigitalSignatureRestBindingStub(DigitalSignatureService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def DigitalSigningSave(self, SaveInput: Teamcenter.Services.Strong.Documentmanagement._2010_04.DigitalSignature.DigitalSignSaveInput) -> Teamcenter.Services.Strong.Documentmanagement._2010_04.DigitalSignature.DigtalSigningSaveResponse: ...

class DigitalSignatureService:
    """
    
            The DigitalSignature service provides operations for managing the digitally sign
            Dataset object.
            


Library Reference:

TcSoaDocumentManagementStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DigitalSignatureService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def DigitalSigningSave(self, SaveInput: Teamcenter.Services.Strong.Documentmanagement._2010_04.DigitalSignature.DigitalSignSaveInput) -> Teamcenter.Services.Strong.Documentmanagement._2010_04.DigitalSignature.DigtalSigningSaveResponse:
        """    
             The digitalSigningSave function will update an existing dataset that has the name
             referenced uploaded signed file.
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param SaveInput: 
                         Digital signing input
             
        :return: Return based dataset if successful.
        """
        ...

class DocumentControlRestBindingStub(DocumentControlService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetAdditionalFilesForCheckin(self, Inputs: list[Teamcenter.Services.Strong.Documentmanagement._2008_06.DocumentControl.GetAdditionalFilesForCheckinInputs]) -> Teamcenter.Services.Strong.Documentmanagement._2008_06.DocumentControl.GetAdditionalFilesForCheckinOutputsResponse: ...
    def PostCreate(self, Input: list[Teamcenter.Services.Strong.Documentmanagement._2008_06.DocumentControl.PostCreateInputs]) -> Teamcenter.Services.Strong.Documentmanagement._2008_06.DocumentControl.PostCreateResponse: ...
    def GetCheckinModeAndFiles(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> Teamcenter.Services.Strong.Documentmanagement._2008_06.DocumentControl.GetCheckinModeAndFilesOutputsResponse: ...

class DocumentControlService:
    """
    
            This service provides operations that are designed to carry out necessary DocumentManagement
            functions for ItemRevision objects that are under Item Revision Definition Configuration
            (IRDC) control.
            

            The postCreate operation is called after a new ItemRevision has been created, and
            it notifies the server to remove the template files attached to the ItemRevision
            and to attach user selected datasets to the newly created object.
            

            The getCheckinModeAndFiles operation is used prior to performing a Check In operation.
            It determines what files have been checked out and downloaded to the client machine,
            and what the Check In mode is for searching for additional files for the checked
            out files.
            

            The getAdditionalFilesForCheckin operation is used when performing a Check In operation,
            after calling the getCheckinModeAndFiles operation. The client searches for local
            files and sends the list of files to the server using this operation. The server
            returns the subset of those files that need to be checked in.
            


Library Reference:

TcSoaDocumentManagementStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DocumentControlService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetAdditionalFilesForCheckin(self, Inputs: list[Teamcenter.Services.Strong.Documentmanagement._2008_06.DocumentControl.GetAdditionalFilesForCheckinInputs]) -> Teamcenter.Services.Strong.Documentmanagement._2008_06.DocumentControl.GetAdditionalFilesForCheckinOutputsResponse:
        """    
             This operation is used in conjunction with the getCheckinModeAndFiles operation during
             the Check In process. getCheckinModeAndFiles takes a list of ItemRevision objects
             that have been checked out, and returns the list of source files that have been downloaded
             to the client. This operation takes the list of downloaded files returned by getCheckinModeAndFiles,
             and returns the subset of those files that are eligible for Check In.
             

Use Cases:

Check In


             This method is called after the getCheckinModeAndFiles operation, but before the
             files are checked in.
             

Dependencies:

             getCheckinModeAndFiles
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param Inputs: 
                         The input is vector of GetAdditionalFilesForCheckinInputs structure.
             
        :return: 
        """
        ...
    def PostCreate(self, Input: list[Teamcenter.Services.Strong.Documentmanagement._2008_06.DocumentControl.PostCreateInputs]) -> Teamcenter.Services.Strong.Documentmanagement._2008_06.DocumentControl.PostCreateResponse:
        """    
             This operation is to be called by the client after the creation of the ItemRevision
             business object, if there are local files to be attached to the newly created ItemRevision.
             For ItemRevision under Item Revision Definition Control (IRDC) it will
             replace any datasets copied from a template with new datasets for the local files.
             The client will then need to import the local files in the volume based on the return
             information from the SOA.  For ItemRevision not under IRDC control,
             the commitInfos list field from the return PostCreateInfo
             structure for this ItemRevision will be empty.
             

Use Cases:

Create new item from the RAC

             During the new item create on RAC, if the ItemRevision business object is
             under IRDC control,  the Attach Files panel will be enabled in the create
             wizard dialog,  if user choose to attach local files in the Attach Files panel, the
             template files for the IRDC will be replaced for the newly created ItemRevision
             business object, and instead the new datasets will be created for the local files;
             if user choose not to attach any local files in the Attach Files panel, then the
             template files for the IRDC will be used for the newly created ItemRevision.
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param Input: 
                         input is the list of <font face="courier" height="10">PostCreateInput</font> structure,
                         which contains client id, <b>ItemRevision</b> business object and list of file names
             
        :return: 
        """
        ...
    def GetCheckinModeAndFiles(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> Teamcenter.Services.Strong.Documentmanagement._2008_06.DocumentControl.GetCheckinModeAndFilesOutputsResponse:
        """    
             Get the CheckIn mode and files for ItemRevision business objects.  This is
             called before CheckIn to get from the server the source files that are currently
             checked out and downloaded locally and how the system is going to search for translated
             files locally for CheckIn. The information here is going to be used to search additional
             files in the client.  If the ItemRevision business object is under Item Revision
             Definition Configuration (IRDC), the CheckIn mode value is retrieved from
             the IRDC object; otherwise it will be an empty string.
             
             CheckIn mode is used to check in translated files that are already in the directory
             with the source file or the first level subdirectory.
             
             There are three CheckIn modes:
             

Same File Name: Attaches and checks in the derived files only if
             they have the same name as the source dataset.
             
Any File Name: Attaches and checks in the derived files no matter
             what names they have.
             
None: Does not attach and check in any derived files.
             


             Refers to Business Modeler IDE Guide > Creating data model objects to represent objects
             in Teamcenter > Working with document management > Create an Item Revision definition
             configuration (IRDC) for more information, the Checkin mode is defined by
             Derived Visualization Files to Checkin from the IRDC Checkin Page Info tab.
             

Use Cases:

Check in ItemRevision under IRDC control

             When a user checks out an ItemRevision business object under IRDC control,
             the user has the option to download the source files into user local machine.  If
             the user then checks in the ItemRevision, the system will search for the translated
             files in the source file directory according to the specified CheckIn mode. This
             functionality supports client side rendering to provide the derived datasets.
             
             For example, there is case where some AutoCAD file cannot be converted to a certain
             format by the server; user can find the translated files in the local directory to
             check in instead.
             


Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param Inputs: 
                         The vector of <b>ItemRevision</b>s to be checked in
             
        :return: 
        """
        ...

class DocumentTemplateRestBindingStub(DocumentTemplateService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetTemplates(self, Input: Teamcenter.Services.Strong.Documentmanagement._2007_01.DocumentTemplate.GetTemplateInput) -> Teamcenter.Services.Strong.Documentmanagement._2007_01.DocumentTemplate.GetTemplatesResponse: ...

class DocumentTemplateService:
    """
    
            This service provides operations to retrieve names and thumbnail images of available
            DMTemplate business objects from the server for a specific application. It is intended
            to support a Microsoft Office style template system, where after the user chooses
            to create a new document, the user is presented with a selection of different templates
            that are differentiated by name and thumbnail image. Once the user selects a DMTemplate,
            the object can be created using the DMTemplate data.
            

            The getTemplate operation returns a list of DMTemplate objects that match a set of
            given search criteria. Available search criteria are application type (e.g. Microsoft
            Word), application version (optional), unit of length (e.g. inches or metric), template
            type, and item type.
            


Library Reference:

TcSoaDocumentManagementStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DocumentTemplateService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetTemplates(self, Input: Teamcenter.Services.Strong.Documentmanagement._2007_01.DocumentTemplate.GetTemplateInput) -> Teamcenter.Services.Strong.Documentmanagement._2007_01.DocumentTemplate.GetTemplatesResponse:
        """    
             This operation is intended to support applications with a Microsoft Office style
             template system, where the user chooses to create a new document, and the application
             presents the user with a selection of different templates to use to create the document.
             The calling application inputs its search criteria, and getTemplates returns the
             list of DMTemplate objects that match the criteria. The DMTemplate is a business
             object that is used to control the template files provided during Create.
             

             The search criteria are:
             

The name of the calling application. DMTemplate objects are application
             specific.
             
The version number of the calling application. Optional.
             
The desired measurement type; e.g. inches or metric. Used for CAD
             applications.
             
The type of Item that will be created using the DMTemplate file.
             
An application defined type value.
             



             The operation returns a list of DMTemplate names and thumbnail images that can be
             used by the application to present a choice to the user. Once the user selects a
             DMTemplate to use in the creation of the new object, the application can get the
             files for the selected DMTemplate using the expandPrimaryObjects operation.
             

Use Cases:

Get a list of templates for creating a new object.


             The user decides to create a new ItemRevision in a CAD application. The application
             calls this operation and receives a list of template names and thumbnails to display
             to the user. The user selects a template and the application retrieves the template
             files using the expandPrimaryObjects operation. The application then creates the
             new ItemRevision and attaches copies of the template files.
             

Dependencies:

             expandPrimaryObjects
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param Input: 
                         The search parameters for the application specific DMTemplate objects.
             
        :return: 
        """
        ...

class LaunchDefinitionRestBindingStub(LaunchDefinitionService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetLaunchDefinition(self, Operation: str, SelectedInputs: list[Teamcenter.Services.Strong.Documentmanagement._2010_04.LaunchDefinition.LDSelectedInputInfo], ServerInfo: Teamcenter.Services.Strong.Documentmanagement._2010_04.LaunchDefinition.ServerInfo, SessionInfo: Teamcenter.Services.Strong.Documentmanagement._2010_04.LaunchDefinition.SessionInfo, UserAgentData: Teamcenter.Services.Strong.Documentmanagement._2010_04.LaunchDefinition.UserAgentDataInfo) -> Teamcenter.Services.Strong.Documentmanagement._2010_04.LaunchDefinition.LaunchDefinitionResponse: ...

class LaunchDefinitionService:
    """
    
            The Application Launcher (AppLauncher) uses a launch definition XML as input to launch
            appropriate external applications. The LaunchDefinition service provides operations
            to gather the data and build the launch definition XML string in the Teamcenter system.
            The launch definition XML string contains information for list of supported tools,
            business data and tool preferences.
            


Library Reference:

TcSoaDocumentManagementStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> LaunchDefinitionService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetLaunchDefinition(self, Operation: str, SelectedInputs: list[Teamcenter.Services.Strong.Documentmanagement._2010_04.LaunchDefinition.LDSelectedInputInfo], ServerInfo: Teamcenter.Services.Strong.Documentmanagement._2010_04.LaunchDefinition.ServerInfo, SessionInfo: Teamcenter.Services.Strong.Documentmanagement._2010_04.LaunchDefinition.SessionInfo, UserAgentData: Teamcenter.Services.Strong.Documentmanagement._2010_04.LaunchDefinition.UserAgentDataInfo) -> Teamcenter.Services.Strong.Documentmanagement._2010_04.LaunchDefinition.LaunchDefinitionResponse:
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

class PrintOrRenderRestBindingStub(PrintOrRenderService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetPrinterDefinitions(self) -> Teamcenter.Services.Strong.Documentmanagement._2013_12.PrintOrRender.PrinterDefinitionResponse: ...
    def PrintSubmitRequest(self, Input: list[Teamcenter.Services.Strong.Documentmanagement._2013_12.PrintOrRender.PrintSubmitRequestInfo]) -> Teamcenter.Services.Strong.Documentmanagement._2013_12.PrintOrRender.SubmitRequestResponse: ...
    def RenderSubmitRequest(self, Input: list[Teamcenter.Services.Strong.Documentmanagement._2013_12.PrintOrRender.RenderSubmitRequestInfo]) -> Teamcenter.Services.Strong.Documentmanagement._2013_12.PrintOrRender.SubmitRequestResponse: ...
    def ContainsRenderableFiles(self, SelectedObjects: list[Teamcenter.Soa.Client.Model.ModelObject], RenderFormat: str) -> Teamcenter.Services.Strong.Documentmanagement._2018_11.PrintOrRender.ContainsRenderableFilesResponse: ...
    def RenderFilesSubmitRequest(self, SelectedObjects: list[Teamcenter.Soa.Client.Model.ModelObject], RenderFormat: str, SaveRenderedFiles: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class PrintOrRenderService:
    """
    
            The PrintOrRender service provides operations for batch print and document rendering.
            

            The getPrinterDefinition operation gets the printer definition information required
            for the Batch Print operation printSubmitRequest.
            

            The printSubmitRequest operation performs batch printing on ItemRevision objects,
            Item object and Dataset objects.
            

            The renderSubmitRequest operation performs rendering on ItemRevision objects.
            The ItemRevision objects must be under Item Revision Definition Configuration
            (IRDC) control.
            



Library Reference:

TcSoaDocumentManagementStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> PrintOrRenderService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetPrinterDefinitions(self) -> Teamcenter.Services.Strong.Documentmanagement._2013_12.PrintOrRender.PrinterDefinitionResponse:
        """    
             This operation returns Print Definition information from the PrintConfiguration
             objects defined in Teamcenter.
             

Use Cases:

             The client wants to get the information required for the Batch Print operation printSubmitRequest.
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :return: 
        """
        ...
    def PrintSubmitRequest(self, Input: list[Teamcenter.Services.Strong.Documentmanagement._2013_12.PrintOrRender.PrintSubmitRequestInfo]) -> Teamcenter.Services.Strong.Documentmanagement._2013_12.PrintOrRender.SubmitRequestResponse:
        """    
             This operation submits print requests for batch printing.
             

Use Cases:

             The client can call this operation to do batch printing. Batch printing lets you
             select workspace objects, such as Item, ItemRevision, or Dataset
             objects, and print the associated documents with system stamps and watermarks.
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param Input: 
                         The input need to create batch print request.
             
        :return: 
        """
        ...
    def RenderSubmitRequest(self, Input: list[Teamcenter.Services.Strong.Documentmanagement._2013_12.PrintOrRender.RenderSubmitRequestInfo]) -> Teamcenter.Services.Strong.Documentmanagement._2013_12.PrintOrRender.SubmitRequestResponse:
        """    
             This operation submits render requests for rendering.
             

Use Cases:

             The client can call this operation to do the rendering on ItemRevision objects.
             When you render an ItemRevision object containing a dataset, you translate
             the associated file to an alternate format.
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param Input: 
                         The input values needed to submit the render request.
             
        :return: 
        """
        ...
    def ContainsRenderableFiles(self, SelectedObjects: list[Teamcenter.Soa.Client.Model.ModelObject], RenderFormat: str) -> Teamcenter.Services.Strong.Documentmanagement._2018_11.PrintOrRender.ContainsRenderableFilesResponse:
        """    
             Checks to see if selectedObjects contains
             any files that can be rendered to the renderFormat
             using the Dispatcher Render Management translator.
             

Use Cases:

             This operation is intended to be called to determine the visibility of commands such
             as the "Generate PDF" one-step command.
             

             Generate PDF (one-step command): The user selects one or more Dataset or ItemRevision
             (or sub-type) objects in Active Workspace.  The containsRenderableFiles
             operation is called by the Active Workspace client framework to determine if there
             are any files within selectedObjects that
             can be rendered to pdf.  If any renderable files are found, then the "Generate PDF"
             command becomes visible.  If no renderable files are found, then the "Generate PDF"
             command remains hidden.
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param SelectedObjects: 
                         The list of objects selected by the user. Valid selected objects include <b>Dataset</b>
                         and <b>ItemRevision</b> (or sub-type) objects.
             
        :param RenderFormat: 
                         The render file format. The value may be any output file format supported by Teamcenter
                         Visualization Convert and Print (VVCP), such as <i>pdf</i> or <i>tif</i>.
             
        :return: 259010: <render format> is not a supported render format.
        """
        ...
    def RenderFilesSubmitRequest(self, SelectedObjects: list[Teamcenter.Soa.Client.Model.ModelObject], RenderFormat: str, SaveRenderedFiles: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Submits a Render Management Dispatcher request to render the files within the selected
             objects to the specified file format without requiring any Item Revision Document
             Control (IRDC) forms to be defined in Business Modeler Integrated Development Environment
             (BMIDE).
             

Use Cases:

             Generate PDF:
             
             The user selects one or more Dataset or ItemRevision (or sub-type)
             objects in Active Workspace.  The containsRenderableFiles
             operation is called to determine if there are any files in the selected objects that
             can be rendered to pdf.  If any renderable files are found, the "Generate PDF" one-step
             command becomes visible.  If the user clicks on the "Generate PDF" command, the renderFilesSubmitRequest operation is called to
             submit a Render Management Dispatcher request to render the valid files within the
             selected objects to pdf.  When the files have been rendered, an alert notification
             will be sent to inform the user that the rendering is complete.
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param SelectedObjects: 
                         The list of objects selected by the user. Valid selected objects include <b>Dataset</b>
                         and <b>ItemRevision</b> (or sub-type) objects.
             
        :param RenderFormat: 
                         The render file format. The value may be any output file format supported by Teamcenter
                         Visualization Convert and Print (VVCP), such as <i>pdf</i> or <i>tif</i>.
             
        :param SaveRenderedFiles: 
                         Specifies if the rendered files should be saved in <b>Dataset</b> objects.
             
        :return: <Business Object name> cannot be updated
             for released <Business Object type> <Business Object name>.
        """
        ...

