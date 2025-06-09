import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BomWindowInfo:
    """
    input
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique identifier of the object."""
    RevisionRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """Revision Rule"""

class BomWindowResponse:
    """
    Response
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique identifier that helps the client to track the object created."""
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """The Ctm0BOMWindow object that was created."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the Service, plain objects, and error information.
            """

class ComposedData:
    """
    This data structure contains information about the composed data.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique identifier."""
    ComposedTransientFileReadTicket: str
    """
            Transient file read ticket to the compose content. The client will use the ticket
            to download the file using FMS. Multiple files or single file will be returned as
            a zip file.
            """
    ComposedMetaDataReadTicket: str
    """
            The composed meta data xml transient file read ticket. The file contains information
            about the schema dataset, graphics dataset, compose version log transient FMS read
            ticket, compose error log FMS read ticket, and etc.
            """

class ComposeInput:
    """
    Input for the compose operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique Identifier of the object."""
    ComposableBO: Teamcenter.Soa.Client.Model.ModelObject
    """
            This object could be the following: DC_Publication, DC_PublicationRevision,
            DC_Topic, DC_TopicRevision, or Ctm0BOMLine.
            """
    RevisionRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """The revision rule that configures the publication or topic structure."""
    KeyValueArgs: System.Collections.Hashtable
    """
            The name value pairs containing the compose parameters.
            
            Typical key value pairs:
            

language                     English,
            Japanese, etc
            
styleType                     The
            defined style type name that user chooses
            
translateVersion             MatchTopic
            or Latest Received
            
composedRefVariant     The defined composable
            reference variant name that user chooses
            
resultingFileFolder         The
            folder path that user chooses to store the publish document
            
resultingFileName         The
            file name user chooses
            
registerResult                true
            or false
            
publishToFileSystem     true or false
            
createClassName         The
            publish document class name to create for the composed output.  For example: DC_ComposedDoc
            or DC_ReviewerDoc.
            

"""
    ProcessingDataVars: System.Collections.Hashtable
    """Processing data variables (currently not used)."""

class ComposeResponse:
    """
    Vector of compose output objects
    """
    def __init__(self, ) -> None: ...
    ComposedData: list[ComposedData]
    """A list of composed documents."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the Service, plain objects, and error information.
            """

class DecomposeInput:
    """
    
            Input for the decompose operation. This holds the XML file to be decomposed and the
            arguments in keyValueArgs that define how the XML file is decomposed. See keyValueArgs
            for more details.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique client identifier."""
    TransientFileWriteTicket: str
    """Transient file write ticket of the content to be decomposed."""
    KeyValueArgs: System.Collections.Hashtable

class DecomposeOutput:
    """
    
            The DecomposeOutput struct is used to hold the data returned by the decomposeContent
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique client identifier"""
    TopicRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The root topic or publication revision of decomposed content."""

class DecomposeResponse:
    """
    
            Return value for the decompose operation. It contains decompose output as well as
            ServiceData which contains partial errors.
            
    """
    def __init__(self, ) -> None: ...
    DescomposeOutput: list[DecomposeOutput]
    """A vector of Decomposed Output structs."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data."""

class GraphicNameAndSize:
    """
    This structure contains Graphic Name and Size information.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Graphic file name."""
    Size: str
    """Size in bytes of graphic file specified by name."""
    TransientFileWriteTicket: str
    """Transient file write ticked of the content."""

class ImportGraphicInput:
    """
    
            Import Graphic Structure, contains: Graphic Name/Path and Size, Graphic Attribute
            Mapping name, Graphic Usage, Graphic Class name and Language.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id"""
    GraphicAttrMapping: str
    """Name of the Graphic Attribute Mapping in the database."""
    GraphicUsages: str
    """List of Graphic usages, separated by comma."""
    GraphicClassName: str
    """Graphic Class Name.  Either Graphic or S1000D Graphic."""
    Language: str
    """Name of the DCt_Language object in the database."""
    NameAndSize: list[GraphicNameAndSize]
    """Path, graphic name and size of the graphic imported."""
    OverwriteMode: str
    """Define Overwrite mode.  Either Skip, keep, merge or overwrite."""

class ImportGraphicOutput:
    """
    Structure of Import Graphic Output.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id"""
    ErrorMessage: str
    """Error message if there was a problem."""

class ImportGraphicResponse:
    """
    Structure of Import Graphic Response.
    """
    def __init__(self, ) -> None: ...
    OutPut: list[ImportGraphicOutput]
    """Return output response"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data"""

class LanguageTableRow:
    """
    
            This table contains the DCt_Language object and a Boolean indicating whether a review
            is requested.
            
    """
    def __init__(self, ) -> None: ...
    LanguageRef: Teamcenter.Soa.Client.Model.ModelObject
    """DCt_Language objects to be related to TranslationOrder."""
    ReviewOrder: bool
    """
            Review order flag which indicates a review of the TranslationOrder is requested.
            If true, the user is expected to request a review of the translation.
            """

class PreparePublishRequestArgs:
    """
    
            The PreparePublishRequestArgs structure is used to capture the information required
            to prepare the data for publishing.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """A unique string supplied by the caller."""
    PrimaryObject: Teamcenter.Soa.Client.Model.ModelObject
    """The publication or topic revision to be published."""
    PublishTool: Teamcenter.Soa.Client.Model.ModelObject
    """The publish tool used to publish."""
    Priority: int
    """
            The priority of the request.  This only applies to the server side publishing request.
            Note: This is currently not implemented.
            """
    StartTime: System.DateTime
    """
            The start time to start the request.  This only applies to the server side publishing
            request.  Note: This is currently not implemented.
            """
    EndTime: System.DateTime
    """
            The end time at which no new requests will be created based on interval setting.
            If request is still processing, the request WILL be completed and will not be stopped.
            This only applies to the server-side publishing request.
            """
    KeyValueArgs: System.Collections.Hashtable
    """
            The name value pairs (string/string) that contain the publishing parameters.  The
            following are out of the box name value pairs.  Extra name value pairs can be passed
            in for customization if needed.
            

compVerSel: compose version selection that is a valid revision rule
            (Any Status; No Working, Latest Working, Working; Any Status, etc)
            
language: name of the language to be published (English US, German,
            Japanese, etc)
            
styleType: the defined style type name that user chooses
            
registerResult: saves the published output back to Teamcenter to
            either a Composed Document or Reviewer Document
            
transVerSel: the translation version of the topic (Latest Received,
            Match Topic, or Received)
            
resultingFileFolder: the folder path that user chooses to store the
            published output (for client side publishing, must be a valid path)
            
resultingFileName: the file name user chooses (for client side publishing,
            can be any string)
            
publishToFileSystem: whether or not the published output will be
            saved to a file system (true or false)
            
ditaFilterValues: the name(s) of DITA value filter(s)
            

"""

class PreparePublishResponse:
    """
    The response structure for preparePublish method.
    """
    def __init__(self, ) -> None: ...
    DataResult: list[PreparePublishResult]
    """The Prepare Publish Result data."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The SOA Service Data."""

class PreparePublishResult:
    """
    The structure for preparePublish result data.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """A unique string supplied by the caller."""
    ClientSidePublishing: bool
    """
            A flag to indicate whether or not this is client side publishing.  Acceptable values
            are true or false.
            """
    PublishMetaDataReadTicket: str
    """
            The publish meta data xml transient file read ticket.  This file contains information
            about the tool, schema dataset, stylesheet dataset and graphics dataset.  This only
            applies to client side publishing
            """
    ComposedFileReadTicket: str
    """
            The composed xml transient file read ticket.  The client will use the ticket to download
            the file using FMS.  File(s) will be returned as a zip file.  This only applies to
            client side publishing.
            """
    RequestCreated: Teamcenter.Soa.Client.Model.ModelObject
    """The Dispatcher Request objects created.  This only applies to server side publishing."""

class SavePublishInput:
    """
    
            The SavePublishInput structure contains the information needed to save the output
            of the published as a Dataset in Teamcenter and relate it to the DC_ComposedDocRevision
            or DC_ReviewerDocRevision.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """A unique string supplied by the caller."""
    ComposedOrReviewerDocRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            The DC_ComposedDocRevision or DC_ReviewerDocRevision the published
            file is to be attached to.
            """
    UploadInfos: list[SavePublishNamedRefUploadInfo]
    """A vector containing the upload information."""

class SavePublishNamedRefUploadInfo:
    """
    
            The SavePublishNamedRefUploadInfo structure for the upload information needed to
            create or update a dataset on a Composed Document or Reviewer Document Revision.
            
    """
    def __init__(self, ) -> None: ...
    FileName: str
    """The file name of the published output."""
    RefName: str
    """
            A string to indicate the format of the published output (i.e. PDF_Reference,
            ZIPFILE, Text, or MSWordXPart) which is appended to the Dataset
            name.
            """
    FileWriteTicket: str
    """The FMS file write ticket."""
    DatasetTypeName: str
    """The Dataset type."""

class SavePublishOutputResponse:
    """
    The response structure for savePublishOutput method.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The SOA service data."""

class SetBomWindowTopLineInfo:
    """
    Sets the top line of the Ctm0BOMWindow.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique identifier of the object."""
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """The Ctm0BOMWindow to set."""
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """The DC_Publication or DC_Topic."""
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The DC_PublicationRevision or DC_TopicRevision."""

class SetBomWindowTopLineResponse:
    """
    response
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique identifier that helps the client to track the object created."""
    TopLine: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """The top Ctm0BOMLine."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the Service, plain objects, and error information.
            """

class TranslationDeliveryInput:
    """
    Input for the prepareTranslationDelivery Operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique identifier of the object."""
    TranslationOrderRev: Teamcenter.Soa.Client.Model.Strong.TranslationOrderRevision
    """TranslationOrderRevision object."""
    BooleanProps: System.Collections.Hashtable
    """
            Boolean properties for translation delivery. Keys are: Include Graphics, Include
            Supporting Data, Deliver Composed Topic, Deliver Decomposed Topic, Include Published
            Content.
            """
    LanguageRow: list[LanguageTableRow]
    """
            A list of LanguageTableRow objects that containt the language that the document will
            be translated into.
            """

class TranslationDeliveryOut:
    """
    Vector of output objects representing objects that were created
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique identifier."""
    TranlationDeliveryRev: Teamcenter.Soa.Client.Model.Strong.TranslatnDelvryRevision
    """The created TranslatnDelvry."""

class TranslationDeliveryResponse:
    """
    Vector of output objects representing objects that were created.
    """
    def __init__(self, ) -> None: ...
    Output: list[TranslationDeliveryOut]
    """A list of created objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the Service, plain objects, and error information.
            """

class ContentManagement:
    """
    Interface ContentManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ComposeContent(self, Input: list[ComposeInput]) -> ComposeResponse:
        """    
             Create composed XML, and also get the Schemas/DTDs, graphics and other information.
             During the composition, if it is determined a property needs to be mapped from the
             topic to the content, the function uses the applicable attribute mapping object to
             insert the topic property into the xml element or attribute.  Specific functions
             within the xml attribute mapping are performed against the applicable attribute.
             The xml attribute map also provides namespace prefixes that are used in the attributes
             defined in the map.  This allows the attribute mapping to be defined with prefixes
             that do not need to be the same as those defined for the topic itself. If the requesting
             function uses a tool that requires processing instruction, the compose function inserts
             the processing instruction into the content.  The format of the instruction conforms
             to the current xml standard for processing instructions.
             

Use Cases:

Use case 1: Open for View, Edit, or Publish

             This document can be used by many different functions such as, preview, edit, publish,
             or just a snapshot in time.  These functions determine which revision rule to pass
             to the compose function.  The resulting content, when applicable, is validated against
             an xml schema or DTD.  Multiple DTDs and xml schemas are available in the system
             at any time.  The compose function provides all the applicable schema files along
             with the composed content for the function requesting the content.
             

Use case 2: Export Document

             The user may export a document from the database.
             


Dependencies:

             decomposeContent
             

Teamcenter Component:

             Content Management - New Content Management module that provides the capability to
             create/reuse/manage compound documents based on SGML/XML in Tc.
             
        :param Input: 
                         Compose input structure.
             
        :return: 
        """
        ...
    def CreateBomWindow(self, Inputs: list[BomWindowInfo]) -> BomWindowResponse:
        """    
             The operation creates a Ctm0BOMWindow used in the publication structure editor.
             

Use Cases:

             The user wants to create a BOM window to hold a Content Management topic.
             

Teamcenter Component:

             Content Management - New Content Management module that provides the capability to
             create/reuse/manage compound documents based on SGML/XML in Tc.
             
        :param Inputs: 
                         A list of BomWindowInfo structures.
             
        :return: 
        """
        ...
    def DecomposeContent(self, Inputs: list[DecomposeInput]) -> DecomposeResponse:
        """    
             The decompose operation breaks up the XML based on its schema into smaller XML segments.
             The XML segments are then stored as Datasets that are attached to DC_Topic
             or DC_Publication objects in Teamcenter. If an XML is decomposed for the first
             time, for example through the import operation, then new DC_Topic or DC_Publication
             objects are created to hold the Datasets. Otherwise the Datasets attached
             to existing objects are updated with any new content.
             

Use Cases:

Use case 1: Edit and Save

             After the user finishes editing a document created with a composeContent call, user
             can save the changes back into Teamcenter Content Management.
             
             To save the changes they can call decomposeContent with a keyValueArgs entry Type
             = Save_from_edit.This will decompose the edited document, compare it with the original
             composed document and update the database with any changes.
             
Use case 2:  Import or receive a translation

             After a topic has been translated, user can import the translation in to Teamcenter
             Content Management.
             
             To import a translation the user can call this operation with a keyValueArgs entry
             Type = Translation_receive.  This will add or update a translation in the entered
             language for the Topic that was translated.
             
Use case 3:  Import an XML Document

             Users can import a new Topic or Publication into Teamcenter Content Management.
             
             To import a new Topic or Publication into the database, the user can call decomposeContent
             with a keyValueArgs entry Type = Import.
             
Use case 4: Import DITA map

             Users can import a DITA Map into Teamcenter Content Management.
             
             To import a new DITA map into the database, the user can call decomposeContent with
             a keyValueArgs entry Type = ImportDitaMap.
             


Dependencies:

             composeContent
             

Teamcenter Component:

             Content Management - New Content Management module that provides the capability to
             create/reuse/manage compound documents based on SGML/XML in Tc.
             
        :param Inputs: 
                         A vector of DecomposeInput structs. Each item in the vector represents an XML file
                         that will be decomposed. See DecomposeInput for more details.
             
        :return: that are returned. The ServiceData element
             is used to hold the status of the operation and any errors encountered during the
             operation.
        """
        ...
    def ImportGraphicOption(self, Inputs: list[ImportGraphicInput]) -> ImportGraphicResponse:
        """    
             This operation creates a GraphicOption, DCt_GrphcTrnsltn, Graphic
             and Image Dataset for the input image so the user can use these to reference
             graphics in xml content in Teamcenter Content Management.
             

Use Cases:

             The user can import images to be used by Teamcenter Content Management.  This operation
             will import an image, create a GraphicOption, a DCt_GrphcTrnsltn and
             a Graphic for the image.
             

Teamcenter Component:

             Content Management - New Content Management module that provides the capability to
             create/reuse/manage compound documents based on SGML/XML in Tc.
             
        :param Inputs: 
                         A vector of ImportGraphicInput structs.
             
        :return: An ImportGraphicResponse object holding a list of ImportGraphicOutput objects containing
             any status or error messages from the operation along with a ServiceData object is
             returned.
        """
        ...
    def PreparePublish(self, Inputs: list[PreparePublishRequestArgs]) -> PreparePublishResponse:
        """    
             For client side publishing, this operation prepares data for publishing.  The client
             is required to download the returned file (zip file includes the composed XML, schemas,
             style sheet, and\or graphics) and then invoke the publishing tool.   For server side
             publishing, a Dispatcher Request will be created to publish the data.
             

Use Cases:

             Users can use the preparePublish operation to create their own client side publishing.
             

Teamcenter Component:

             Content Management - New Content Management module that provides the capability to
             create/reuse/manage compound documents based on SGML/XML in Tc.
             
        :param Inputs: 
                         A vector of PreparePublishRequestArgs containing the publish input information.
             
        :return: 
        """
        ...
    def PrepareTranslationDelivery(self, Input: list[TranslationDeliveryInput]) -> TranslationDeliveryResponse:
        """    
             Perform operations specific to preparing translations for delivery.  Allows a user
             to create a TranslatnDelvry and relate it to TranslationOrder.  Creates
             the DCt_Translation object and relate to DC_TopicRevision or DC_PublicationRevision.
             If multiple languages are chosen, then multiple translations are generated, each
             with a one to one relation with a DC_TopicRevision or DC_PublicationRevision.
             A folder structure is created to save the composed and decomposed xml files for
             each language.  Zip the folder structure and save as Dataset.
             

Use Cases:

             The user wants to setup a topic and it's children to be translated.
             

Teamcenter Component:

             Content Management - New Content Management module that provides the capability to
             create/reuse/manage compound documents based on SGML/XML in Tc.
             
        :param Input: 
                         A list of Translation Delivery input structures.
             
        :return: 
        """
        ...
    def SavePublishOutput(self, Inputs: list[SavePublishInput]) -> SavePublishOutputResponse:
        """    
             This operation saves the published output to Teamcenter as a Dataset attached
             to either a DC_ComposedDocRevision or a DC_ReviewerDocRevision.  The
             published output file must be uploaded to Teamcenter volume first in order to obtain
             the FMS write ticket for the input for this operation.
             

Use Cases:

             Users can use the savePublishOutput operation to save their own published files to
             Teamcenter.
             

Teamcenter Component:

             Content Management - New Content Management module that provides the capability to
             create/reuse/manage compound documents based on SGML/XML in Tc.
             
        :param Inputs: 
                         A vector of SavedPublishInput containing the input information.
             
        :return: 
        """
        ...
    def SetBomWindowTopLine(self, Inputs: list[SetBomWindowTopLineInfo]) -> SetBomWindowTopLineResponse:
        """    
             This operation creates a Ctm0BOMLine and set the top line of the Ctm0BOMWindow
             to the newly created Ctm0BOMLine. It is used by the publication structure
             editor.
             

Use Cases:

             The user wants to populate the window created with createBomWindow with a topic.
             

Teamcenter Component:

             Content Management - New Content Management module that provides the capability to
             create/reuse/manage compound documents based on SGML/XML in Tc.
             
        :param Inputs: 
                         SetBomWindowTopLineInfo structure
             
        :return: 
        """
        ...

