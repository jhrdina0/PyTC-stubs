import System
import Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement
import Teamcenter.Services.Strong.Contmgmtbase._2016_10.ContentManagement
import Teamcenter.Soa.Client

class ContentManagementRestBindingStub(ContentManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ComposeContent(self, Input: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.ComposeInput]) -> Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.ComposeResponse: ...
    def CreateBomWindow(self, Inputs: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.BomWindowInfo]) -> Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.BomWindowResponse: ...
    def DecomposeContent(self, Inputs: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.DecomposeInput]) -> Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.DecomposeResponse: ...
    def ImportGraphicOption(self, Inputs: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.ImportGraphicInput]) -> Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.ImportGraphicResponse: ...
    def PreparePublish(self, Inputs: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.PreparePublishRequestArgs]) -> Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.PreparePublishResponse: ...
    def PrepareTranslationDelivery(self, Input: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.TranslationDeliveryInput]) -> Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.TranslationDeliveryResponse: ...
    def SavePublishOutput(self, Inputs: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.SavePublishInput]) -> Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.SavePublishOutputResponse: ...
    def SetBomWindowTopLine(self, Inputs: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.SetBomWindowTopLineInfo]) -> Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.SetBomWindowTopLineResponse: ...
    def DecomposeContentWithMetaData(self, Inputs: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.DecomposeInput]) -> Teamcenter.Services.Strong.Contmgmtbase._2016_10.ContentManagement.DecomposeResponse2: ...

class ContentManagementService:
    """
    
            This service adds operations required by content management to perform operations
            specific to content management.  These operations allow the user to perform some
            of the basic functions of content management: compose, decompose, translation import/export
            and import graphics.
            
            These SOAs would allow a user to:
            

Import a set of graphics.
            
Import an XML document that references these graphics
            
Compose the XML document for editing
            
Decompose the edited XML document which updates the content management
            items in the database
            




Library Reference:

TcSoaContMgmtBaseStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ContentManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ComposeContent(self, Input: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.ComposeInput]) -> Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.ComposeResponse:
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
    def CreateBomWindow(self, Inputs: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.BomWindowInfo]) -> Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.BomWindowResponse:
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
    def DecomposeContent(self, Inputs: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.DecomposeInput]) -> Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.DecomposeResponse:
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
    def ImportGraphicOption(self, Inputs: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.ImportGraphicInput]) -> Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.ImportGraphicResponse:
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
    def PreparePublish(self, Inputs: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.PreparePublishRequestArgs]) -> Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.PreparePublishResponse:
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
    def PrepareTranslationDelivery(self, Input: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.TranslationDeliveryInput]) -> Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.TranslationDeliveryResponse:
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
    def SavePublishOutput(self, Inputs: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.SavePublishInput]) -> Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.SavePublishOutputResponse:
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
    def SetBomWindowTopLine(self, Inputs: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.SetBomWindowTopLineInfo]) -> Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.SetBomWindowTopLineResponse:
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
    def DecomposeContentWithMetaData(self, Inputs: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.DecomposeInput]) -> Teamcenter.Services.Strong.Contmgmtbase._2016_10.ContentManagement.DecomposeResponse2:
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
             can save the changes back into Teamcenter Content Management. To save the changes
             they can call decomposeContent with a keyValueArgs entry Type = Save_from_edit.This
             will decompose the edited document, compare it with the original composed document
             and update the database with any changes.
             
Use case 2: Import or receive a translation

             After a topic has been translated, user can import the translation in to Teamcenter
             Content Management. To import a translation the user can call this operation with
             a keyValueArgs entry Type = Translation_receive. This will add or update a translation
             in the entered language for the Topic that was translated.
             
Use case 3: Import an XML Document

             Users can import a new Topic or Publication into Teamcenter Content Management. To
             import a new Topic or Publication into the database, the user can call decomposeContent
             with a keyValueArgs entry Type = Import.
             
Use case 4: Import DITA map

             Users can import a DITA Map into Teamcenter Content Management. To import a new DITA
             map into the database, the user can call decomposeContent with a keyValueArgs entry
             Type = ImportDitaMap.
             

Dependencies:

             composeContent
             

Teamcenter Component:

             Content Management - New Content Management module that provides the capability to
             create/reuse/manage compound documents based on SGML/XML in Tc.
             
        :param Inputs: 
                         A vector of DecomposeInput structs. Each item in the vector represents an XML file
                         that will be decomposed. See DecomposeInput for more details.
             
        :return: 239175: A reference cannot be created to a topic that doesn't exist
        """
        ...

