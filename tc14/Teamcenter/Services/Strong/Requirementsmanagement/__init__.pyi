import System
import Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement
import Teamcenter.Services.Strong.Requirementsmanagement._2008_06.RequirementsManagement
import Teamcenter.Services.Strong.Requirementsmanagement._2009_10.RequirementsManagement
import Teamcenter.Services.Strong.Requirementsmanagement._2010_09.RequirementsManagement
import Teamcenter.Services.Strong.Requirementsmanagement._2011_06.RequirementsManagement
import Teamcenter.Services.Strong.Requirementsmanagement._2012_09.RequirementsManagement
import Teamcenter.Services.Strong.Requirementsmanagement._2022_12.RequirementsManagement
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import typing

class RequirementsManagementRestBindingStub(RequirementsManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateOrUpdate(self, Info: list[Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.PartInfo]) -> Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.CreateOrUpdateResponse: ...
    def ExportToApplication(self, Inputs: list[Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.ExportToApplicationInputData]) -> Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.ExportToApplicationResponse: ...
    @typing.overload
    def GetRichContent(self, Inputs: list[Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.GetContentInput]) -> Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.GetRichContentResponse: ...
    @typing.overload
    def GetRichContent(self, Inputs: list[Teamcenter.Services.Strong.Requirementsmanagement._2008_06.RequirementsManagement.GetContentInput1]) -> Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.GetRichContentResponse: ...
    def ImportFromApplication(self, Inputs: list[Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.ImportFromApplicationInputData]) -> Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.ImportFromApplicationResponse: ...
    def SetRichContent(self, Inputs: list[Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.SetContentInput]) -> Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.SetRichContentResponse: ...
    def OpenStdNote(self, Input: list[Teamcenter.Services.Strong.Requirementsmanagement._2009_10.RequirementsManagement.StdNoteInput]) -> Teamcenter.Services.Strong.Requirementsmanagement._2009_10.RequirementsManagement.OpenStdNoteResponse: ...
    def SetStdNote(self, Input: list[Teamcenter.Services.Strong.Requirementsmanagement._2009_10.RequirementsManagement.SetStdNoteDetails]) -> Teamcenter.Services.Strong.Requirementsmanagement._2009_10.RequirementsManagement.SetStdNoteResponse: ...
    def MoveLine(self, Input: list[Teamcenter.Services.Strong.Requirementsmanagement._2010_09.RequirementsManagement.MoveLineInfo]) -> Teamcenter.Services.Strong.Requirementsmanagement._2010_09.RequirementsManagement.MoveLineResponse: ...
    def PublishColumnConfiguration(self, Input: list[Teamcenter.Services.Strong.Requirementsmanagement._2011_06.RequirementsManagement.PublishColumnConfigInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetBomlineAfterCreate(self, Inputs: list[Teamcenter.Services.Strong.Requirementsmanagement._2012_09.RequirementsManagement.GetBOMLineInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetRichContent2(self, Inputs: list[Teamcenter.Services.Strong.Requirementsmanagement._2022_12.RequirementsManagement.SetContentInput2]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class RequirementsManagementService:
    """
    
            The RequirementsManagement service provides operations to create and
update Item
            objects. This service can create and update the Dataset when
creating the
            Item objects. It can update the related objects such as Dataset and
            Form. It provides a basic support for editing the rich text of
Requirement
            objects.  It also provides support for exporting Teamcenter objects
to MSWord
            and MSExcel.

            The RequirementsManagement service service can be used for
supporting following use
            cases:

Create object of type Item

Update objects of type Item

Create and update Dataset

Get the rich text of Requirement

Set the rich text of Requirement

Export Teamcenter objects to MSWord

Export Teamcenter objects to MSExcel

Create the traceability matrix between two BOM structures based on
            TraceLink relation

Manipulate the BOMLine by moving the BOMLine upwards,
            downwards or to specified Â Â Â Â location

Open objects of type Fnd0ParamReqment

Publish the column configuration that is marked as publishable by
            the user.

Library Reference:

TcSoaRequirementsmanagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> RequirementsManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateOrUpdate(self, Info: list[Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.PartInfo]) -> Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.CreateOrUpdateResponse:
        """    
             This operation creates objects of type Item .  The related objects such as
             ItemRevision, Dataset and Forms are also created during this
             operation.  This operation checks for the existence of the Item, ItemRevision,
             and Dataset.  If the Item and ItemRevision already exists, but
             the Dataset does not exist, then the Dataset is created.  If the Dataset
             exists, a new version will be added to the existing version.  If any of the objects
             exists, but the input attribute values that differ from those already set, attempts
             are made to update the values. There is no attempt to query and update an existing
             object without a reference to that object. This operation has the additional behavior
             to create and update the Dataset along with the creation of Item.
             

Use Cases:

             User can create objects of type Item using this operation.
             
             User can create or update objects of type Dataset using this operation.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Info: 
                         A list of structures containing the required information to create/update objects
                         of type <b>Item</b>.
             
        :return: .
        """
        ...
    def ExportToApplication(self, Inputs: list[Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.ExportToApplicationInputData]) -> Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.ExportToApplicationResponse:
        """    
             This operation is used for exporting Teamcenter objects (WorkspaceObject)
             to applications like MSWord and MSExcel.  Teamcenter business objects
             should already be created so that the objects can be exported to MSWord and
             MSExcel using the service operation.
             

             An Excel (.mhtml) or a Word (.docx) file is generated at the server as a result of
             this operation.  The generated file will contain Teamcenter objects and their properties.
             Depending upon the application format that is being passed as input parameter, the
             generated file can be opened in MSWord or MSExcel.  If the application
             format is MSWordXML then the generated document is a Word document.  If the
             application format is MSExcel then the generated sheet is a static Excel spreadsheet.
             If the application format is MSExcelLive then the generated sheet is a Live
             Excel spreadsheet. "Live" sheet means that modifications can be done to the data
             in MSExcel which will reflect to Teamcenter.
             


Use Cases:

             User can create Teamcenter objects in RAC and then export those objects and their
             properties to MSWord or MSExcel. If "Live" option is selected then
             User can create "Live" spreadsheet after export to MSExcel.
             

             Following usecases are supported in this operation
             


Export of Workspace objects to MSWord (static)
             
Export of Teamcenter objects to MSExcel(static)
             
Export of Teamcenter objects to MSExcel(Live) and edit the properties
             from Excel Live sheet.
             



Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Inputs: 
                         A vector of <font face="courier" height="10">ExportToApplicationInputData</font>
                         structures containing the required information to export Teamcenter business objects
                         to <b>MSWord</b> /<b>MSExcel</b>.
             
        :return: then the appropriate error code and the error message is added to
             the error stack. This error stack is part of serviceData.
        """
        ...
    @typing.overload
    def GetRichContent(self, Inputs: list[Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.GetContentInput]) -> Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.GetRichContentResponse: ...
    @typing.overload
    def GetRichContent(self, Inputs: list[Teamcenter.Services.Strong.Requirementsmanagement._2008_06.RequirementsManagement.GetContentInput1]) -> Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.GetRichContentResponse: ...
    def ImportFromApplication(self, Inputs: list[Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.ImportFromApplicationInputData]) -> Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.ImportFromApplicationResponse:
        """    
             This operation is used for importing the contents of the given MSWord document  to
             create objects of type SpecElement.  The MSWord document to be imported to
             Teamcenter should have .docx file format. If the application format is MSWordXML
             then the operation parses the given MSWord document to creates a structure of chosen
             subtype of SpecElement.
             

             Objects of type Requirement/Paragraph are created at the server after
             importing the document.  When this operation is called from Teamcenter rich client,
             a structure is created and is opened in the RequirementsManagement
             application.  The structure and indentation of the child Requirement is driven
             by the MSWord outline level in the document.  Each Paragraph that is formatted
             in an outline level style produces a separate Requirement. This file may be located
             in a local file system folder or a network folder.  This operation supports MSWord
             documents in MS Office Open XML format (.docx format) only.
             

Use Cases:

             User can create an MSWord document and import it using this operation to create a
             structure. Each Paragraph in MSWord document represents a Requirement/Paragraph
             in the structure.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Inputs: 
                         A list of <font face="courier" height="10">ImportFromApplicationInputData</font>
                         structures containing the information to import MSWord document and create a structure.
                         It contains the file ticket of the document to be imported, the application format
                         "<i>MSWordXML</i>" and the subtype of the <b>SpecElement</b> to be created after
                         import of document to Teamcenter.
             
        :return: 
        """
        ...
    def SetRichContent(self, Inputs: list[Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.SetContentInput]) -> Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.SetRichContentResponse:
        """    
             The SOA operation is responsible for setting rich text contents from Word document
             to a Fulltext object of requirement. This SOA operation will be called when;
             User modified rich content of requirements through word document. This operation
             will basically accept Fulltext object to process in "objectToProcess" variable.
             Along with Fulltext object, this operation will accept transient file tickets
             for MSWord Document which is modified by user. All exceptions are added to
             service data, if occurred.
             

Use Cases:

             User can set rich text contents of SpecElement object by using setRichContent
             SOA.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Inputs: 

        :return: structure is returned.
             It contains information about the failure in ServiceData.
        """
        ...
    def OpenStdNote(self, Input: list[Teamcenter.Services.Strong.Requirementsmanagement._2009_10.RequirementsManagement.StdNoteInput]) -> Teamcenter.Services.Strong.Requirementsmanagement._2009_10.RequirementsManagement.OpenStdNoteResponse:
        """    
             This operation helps to open Fnd0ParamReqment object, or its Revision Fnd0ParamReqmentRevision
             contents in Teamcenter MS Word view. User will get the note text associated with
             the selected Fnd0ParamReqmentRevision allowing editing in that view. Opening
             Fnd0ParamReqment/ Fnd0ParamReqmentRevision happens in two different
             ways:
             
             1.    In context with Fnd0ListsParamReqments
             relation: In this case, operation gives the Parameter/ value pairs selected in context
             for the parent object of Fnd0ListsParamReqments,
             allowing editing the values.
             
             2.    Without context: In this case, it gives note text associated
             for the Fnd0ParamReqmentRevision for view/edit purpose.
             


Use Cases:

             1.    Suppose user created Fnd0ParamReqment object, and
             now wants to see/edit note text of it, then opening Teamcenter MS Word view, user
             will see it, and can edit it.
             
             2.    Suppose user has attached any Fnd0ParamReqment/Fnd0ParamReqmentRevision
             object to any other Item/ItemRevision object with Fnd0ListsParamReqments relation, and now wants to edit/view parameter
             values which are set while attaching this Fnd0ParamReqment/Fnd0ParamReqmentRevision,
             then opening Teamcenter MS Word view will show it.
             


Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Input: 
                         A list of structures containing <b>Fnd0ParamReqmentRevision</b> object with <font face="courier" height="10">Fnd0ListsParamReqments</font> relation object by which
                         <b>Fnd0ParamReqmentRevision</b> is attached to any other object.
             
        :return: 
        """
        ...
    def SetStdNote(self, Input: list[Teamcenter.Services.Strong.Requirementsmanagement._2009_10.RequirementsManagement.SetStdNoteDetails]) -> Teamcenter.Services.Strong.Requirementsmanagement._2009_10.RequirementsManagement.SetStdNoteResponse:
        """    
             Sets the parameters and their values on Standard Note/Parametric Requirement.
             This SOA operation can set values on one or more Standard Note/Parametric
             Requirement in one operation call. When any Standard Note/Parametric
             Requirement attached to any ItemRevision it will get attached with relation
             Fnd0ListsParamRequirements (Parametric Requirements Lists). In that context
             if that Standard Note/Parametric Requirement object is selected, and
             edited in MS Word view, then saving of editing values from this view will
             be set on this Standard Note/Parametric Requirement using this SOA.
             This SOA will set those parameters and their values on given relation object.
             

Use Cases:

             You can edit, and set Standard Note/Parametric Requirement Parameter
             values using MS Word view in Teamcenter. This view can be launched using Window->Show
             view->Other->Teamcenter->MS Word
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Input: 
                         List of standard note input details with their values on parameters to be set.
             
        :return: values will be returned with client id
             mapped to error message in the ServiceData list of partial errors.
        """
        ...
    def MoveLine(self, Input: list[Teamcenter.Services.Strong.Requirementsmanagement._2010_09.RequirementsManagement.MoveLineInfo]) -> Teamcenter.Services.Strong.Requirementsmanagement._2010_09.RequirementsManagement.MoveLineResponse:
        """    
             This operation manipulates the BOMLine Structure (Requirement/ Function/
             SEBlock structure) by moving the selected BOMLine object either Upwards,
             Downwards or to a specific position. A Number property will be updated for
             selected Fnd0BuildingBlockBOMLine object along with its children.
             
             Following operation are supported by this service operation.
             

Move Up - To move up the selected BOM line (Fnd0BuildingBlockBOMLine)
             up in the structure with respect to its sibling. For instance, if a requirement structure
             "Req_01", we have two children "SubReq_01" and "SubReq_02". In move up structure
             modification can be done with respect to the parent. Requirements "SubReq_01" and
             "SubReq_02" can be move up in context of parent "Req_01".
             
Move Down - To move down the selected BOM line (Fnd0BuildingBlockBOMLine)
             up in the structure with respect to its sibling. For instance, if a requirement structure
             "Req_01", we have two children "SubReq_01" and "SubReq_02". In move down structure
             modification can be done with respect to the parent. Requirements "SubReq_01" and
             "SubReq_02" can be move down in context of parent "Req_01".
             
Promote - To indent the selected BOM line (Fnd0BuildingBlockBOMLine)
             up in the structure with respect to its sibling. For instance, promote a requirement
             previously occupying level 2, with number "1.1", moves to the level 1, with number
             "2.0". Children previously occupying level 3 with number "1.1.1", moves to the level
             2, with number "2.1".
             
Demote - To out-dent the selected BOM line (Fnd0BuildingBlockBOMLine)
             up in the structure with respect to its sibling. For instance, demote a requirement
             previously occupying level 2, with number "1.0", moves to the level 3, with number
             "1.1.1". Children previously occupying level 3, with number "1.1.1", moves to the
             level 4, with number "1.1.1.1".
             
Edit Number - To move the selected BOM line (Fnd0BuildingBlockBOMLine)
             up in the structure with respect to its sibling. You can able to move selected BOM
             line object from one level to other and from one parent to other parent.  For instance,
             if a requirement has number "1.1.1" which means it is under parent "1.1". If the
             number changed to "1.1.3", the requirement is repositioned under the parent. If the
             number is changed to "2.1", then requirement will be removed from the parent and
             put under the sibling of the parent.
             



Use Cases:

             You can manipulate the hierarchy for a selected Requirement /Function/
             SEBlockBOMLine object by using the moveLine operation. The given Fnd0BuildingBlockBOMLine
             object will be moved as per the choice along with its children and the Number property
             will be updated with new values.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Input: 
                         A list of <font face="courier" height="10">MoveLineInfo</font> structures which hold
                         the required information to move selected <b>Fnd0BuildingBlockBOMLine</b> object
                         along with its sibling.
             
        :return: 
        """
        ...
    def PublishColumnConfiguration(self, Input: list[Teamcenter.Services.Strong.Requirementsmanagement._2011_06.RequirementsManagement.PublishColumnConfigInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation publishes the Column Configuration that is Mark as Publishable
             by the user. This operation will get the column configuration values from the specified
             Fnd0ColumnConfiguration object and create the site preferences. After creating
             the site preference it will set the "IsPublished" property to true present on the
             specified Fnd0ColumnConfiguration object.  So by creating the site preference
             these column configuration will be visible to all present users in the system. This
             operation converts the user preferences to the site level preferences in Teamcenter
             Context so that all users can use it. When user save the column configuration, applied
             on the BOM structure then it will store all applied column configuration values as
             user protection scope preferences. After that user can mark the same column configuration
             as Mark as Publishable that means user want that column configuration to be
             available to other users in the system. So Administrator privileged user can
             publish the column configuration so it will be available to all other users in the
             system. The user which originally saved the column configuration will see two preferences
             with same name, one with protection scope user and other one with site protection
             scope.
             

Use Cases:

             You can publish the column configuration that is Mark as Publishable by the
             user so that it will be visible to all other users and others users can apply the
             publish column configuration on BOM structure.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Input: 
                         A list of <font face="courier" height="10">PublishColumnConfigInfo</font> structures
                         which hold the required information to publish the column configuration.
             
        :return: object
             is returned in the updated object list of ServiceData. Any failure will be returned
             with client id mapped to error message in the ServiceData list of partial errors.
        """
        ...
    def GetBomlineAfterCreate(self, Inputs: list[Teamcenter.Services.Strong.Requirementsmanagement._2012_09.RequirementsManagement.GetBOMLineInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates a BOMLine for a newly created  Item and adds it to the selected
             parent BOMLine and checks out the latest revision of newly created Item based on
             a check-out preference. The inputs structure for this operation contains selected
             parent BOMLine and newly created Item (e.g. Functionality or Logical Block).
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Inputs: 
                         This argument contains parent BOMLine and newly created business object of the Item.
                         The newly created Item is used to create the BOMLine and to get the latest ItemRevision
                         for the checkout. The parent BOMLine in the input list is used to attach the newly
                         created BOMLine.
             
        :return: A GetBOMLineResponse with ServiceData element containing the newly created BOMLine.
             The following partial error may be returned: 515024  Specified object tag is not
             a valid.
        """
        ...
    def SetRichContent2(self, Inputs: list[Teamcenter.Services.Strong.Requirementsmanagement._2022_12.RequirementsManagement.SetContentInput2]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

