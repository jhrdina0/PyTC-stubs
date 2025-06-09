import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttributeInfo:
    """
    
This structure allows the caller to create or update named attributes. This
structure
must contain the name of the attribute and the value of the attribute to set.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the attribute to set."""
    Value: str
    """The value of the attribute to set."""

class AttributeInfoCAD:
    """
    
This structure allows the caller to create or update named attributes. This
structure
must contain the name of the attribute and the value of the attribute to set.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the attribute to set."""
    Value: str
    """The value of the attribute to set."""

class CommitDatasetFileInfoCAD:
    """
    
This structure has information to commit named reference files to input Dataset.
This structure contains the necessary  information like the file ticket and if a
new version of Dataset is to be created.
    """
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """A tag of the Dataset to be updated with the named reference file."""
    CreateNewVersion: bool
    """
            The value of true means that a new Dataset to be created, value of false means
            that the existing Dataset to be updated with the named reference file.
            """
    DatasetFileTicketInfos: list[DatasetFileTicketInfoCAD]
    """The information about the Dataset file tickets."""

class CreateOrUpdateOutput:
    """
    
This structure is defined to store information about the newly created Dataset
or updates to the existing Dataset. It contains all the information about
the related objects that user needs to pass during the creation or update of
Dataset.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """The tag of the Item that is created or updated."""
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The tag of the ItemRevision that is created or updated."""
    DatasetOutput: list[DatasetOutput]
    """The tag of the Dataset that is created or updated."""
    ExtraItemObjs: list[ExtraObjectOutput]
    """The structure containing information about the additional Item objects created."""
    ExtraItemRevObjs: list[ExtraObjectOutputCAD]
    """
            The structure containing information about the additional ItemRevision objects
            created.
            """

class CreateOrUpdateResponse:
    """
    
This structure represents the output of createOrUpdate operation.  It has the
information
about the newly created Dataset or update to existing Dataset.
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateOrUpdateOutput]
    """
            The list of structures containing information about the Item,
            
ItemRevision or the Dataset to be created or updated.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The serviceData."""

class DatasetFileInfoCAD:
    """
    
This structure allows the user to create or update the dataset with the named
attributes
information. This structure must contain either an "AttributesToSet" element or
an
"AttributesToUnset" element, but not both.

    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    FileName: str
    """The name of the named reference file to be updated."""
    NamedReferencedName: str
    """The named references string for that object."""
    IsText: bool
    """
            Flag to indicate if it is text data. Value of true indicates it is text data. Value
            of false indicates binary data.
            """
    AllowReplace: bool
    """
            Flag to indicate whether to replace the data. Value of true indicates data to be
            overwritten. Value of false indicates data will not be overwritten.
            """

class DatasetFileTicketInfoCAD:
    """
    This structure has Dataset FMS file ticket information.
    """
    def __init__(self, ) -> None: ...
    DatasetFileInfo: DatasetFileInfoCAD
    """The Dataset file ticket information."""
    Ticket: str
    """The name of the ticket."""

class DatasetInfo:
    """
    
The DatasetInfo structure represents all of the data necessary to construct the
Dataset
object. All the attributes required to be set on the Dataset are passed as
name/value pairs in the AttributeInfo structure.
The extraObject field allows for the creation of an object(s) that will be
related
to this newly created Dataset.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """The tag of Dataset."""
    Name: str
    """The name of Dataset."""
    Description: str
    """The description for Dataset."""
    Type: str
    """The real type name of Dataset."""
    Id: str
    """The id of Dataset."""
    DatasetRev: str
    """The name of Dataset revision."""
    ItemRevRelationName: str
    """The relation name of the revision to Dataset."""
    CreateNewVersion: bool
    """
            The flag to create new version. Value of true indicates new revision to be created,
            value of false indicates no new revision to be created.
            """
    AttrList: list[AttributeInfo]
    """The attributes to be set on the Dataset."""
    MappingAttributes: list[AttributeInfoCAD]
    """The mapping attributes to be set on the Dataset."""
    ExtraObject: list[ExtraObjectInfo]
    """Additional objects to be created and related to the Dataset."""
    DatasetFileInfos: list[DatasetFileInfoCAD]
    """The information about files attached to the Dataset."""
    NamedReferenceObjectInfos: list[NamedReferenceObjectInfo]
    """The information about objects attached to the Dataset."""

class DatasetOutput:
    """
    
This structure is defined to store information about the output Dataset objects.
It also contains information about the additional objects that are related to
the
Dataset.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """The tag of the Dataset."""
    CommitInfo: list[CommitDatasetFileInfoCAD]
    """The structure containing information to commit named reference files."""
    ExtraObjs: list[ExtraObjectOutput]
    """The structure containing information about the objects that are related to the Dataset."""
    NamedRefObjs: list[ExtraObjectOutputCAD]
    """The structure containing information about the additional named reference objects"""

class ExportToApplicationInputData:
    """
    
The ExportToApplicationInputData structure represents all of the data necessary
to
export selected objects to Word/Excel.
    """
    def __init__(self, ) -> None: ...
    ObjectsToExport: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The list of Teamcenter business objects to export."""
    AttributesToExport: list[str]
    """The list of attributes to export."""
    ApplicationFormat: str
    """
            The application format such as MSWordXML, MSExcel and MSExcelLive.
            
            Supported application formats for this operation
            

MSWordXML    This format is used for exporting
            Workspace objects to static MSWord application.
            
MSExcel    This format is used for exporting
            Teamcenter objects to static MSExcel  application.    
            
MSExcelLive    This format is used for
            exporting Teamcenter objects to Live MSExcel  application.
            

"""
    TemplateId: str
    """The name of the MSWord/MSExcel template"""

class ExportToApplicationResponse:
    """
    
ExportToApplicationResponse structure represents the output of export to
application
operation. It contains the read ticket to the exported MSWord/MSExcel
file.
    """
    def __init__(self, ) -> None: ...
    TransientFileReadTickets: list[str]
    """The transient file read tickets for the exported file."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The serviceData."""

class ExtraObjectInfo:
    """
    
The ExtraObjectInfo structure represents
additional object information that may be required to complete an operation.
Example
- It may be required by the client application to pass additional information
about
the relation (GRM) and properties on the relation to the server. This structure
can
be used to store the information about any relation objects.
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The tag of the Teamcenter Business object."""
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    RelationTypeName: str
    """The real type name of the relation."""
    TypeName: str
    """The real type name of the object."""
    AttrNameValuePairs: list[AttributeInfo]
    """The vector of attributes names and its values to be set on the object."""

class ExtraObjectOutput:
    """
    
This structure is defined to store information about the additional objects that
are updated during the createOrUpdate operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The tag of the Business object."""

class ExtraObjectOutputCAD:
    """
    This structure is defined to add additional objects as part of the response
structure.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The tag of the Business object."""

class GetContentInput:
    """
    The parameters required to open requirement in word.
    """
    def __init__(self, ) -> None: ...
    ObjectToProcess: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """Fulltext object, whose content to be  viewed."""
    ApplicationFormat: str
    """The viewing application format. Only MSWordXML is supported."""
    TemplateId: str
    """This parameter is not used currently."""

class GetRichContentResponse:
    """
    
This structure holds FMS ticket of MSWord file generated as part of
getRichContent
operation.
    """
    def __init__(self, ) -> None: ...
    TransientFileReadTickets: list[str]
    """FMS ticket of word file that is generated as part of getRichContent operation."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData."""

class ImportFromApplicationInputData:
    """
    
The ImportFromApplicationInputData structure represents all of the data
necessary
to import an MSWord document into Teamcenter.
    """
    def __init__(self, ) -> None: ...
    TransientFileWriteTicket: str
    """The file ticket of the. docx file to be imported into Teamcenter."""
    ApplicationFormat: str
    """The supported application format is "MSWordXML""""
    CreateSpecElementType: str
    """The subtype of SpecElement to be created."""

class ImportFromApplicationResponse:
    """
    
ImportFromApplicationResponse structure represents the output of import from
application
operation. It contains the UID of the BOMWindow after the document is imported
to
Teamcenter.
    """
    def __init__(self, ) -> None: ...
    ResultObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The resultant objects which contains the UID of the BOMWindow created after the document
            is imported.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class ItemInfo:
    """
    
The ItemInfo structure represents all of
the data necessary to construct the Item object. It contains the information
about the attributes that are set on the Item object. All attributes are passed
as name/value pairs in the AttributeInfo
structure. The extraObject field contains information about the objects that are
related to the newly created Item.
    """
    def __init__(self, ) -> None: ...
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """
            The object tag of the object to be updated. If it is NULL then a new object will
            be created.
            """
    ItemId: str
    """
            The object Id (item_id) of the object to be updated. If it is NULL then a new ID
            is created.
            """
    ItemType: str
    """The object Type (object_type) of the object to be created or updated."""
    Name: str
    """The Name (object_name) of the object."""
    Description: str
    """The Description (object_desc) of the object."""
    AttrList: list[AttributeInfo]
    """
            The attributes to be set on the object. This is in the form of map that stores attribute
            name and attribute value.
            """
    ExtraObject: list[ExtraObjectInfo]
    """The structure containing information about the objects that are related to the Item."""
    Folder: Teamcenter.Soa.Client.Model.Strong.Folder
    """The tag of the Folder under which newly created Item is to be pasted."""

class ItemRevInfo:
    """
    
The ItemRevInfo structure represents all
of the data necessary to construct the ItemRevision object. It contains
information
about the attributes to be set on the revision object. All attributes are passed
as name/value pairs in the AttributeInfo
structure. The extraObject field allows for the creation of an objects that will
be related to this newly created ItemRevision.
    """
    def __init__(self, ) -> None: ...
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            A tag of the ItemRevision to be created or updated. It is NULL for newly created
            Item.
            """
    RevId: str
    """The Id of the ItemRevision. It is NULL for new ItemRevision object."""
    AttrList: list[AttributeInfo]
    """The attribute name and attribute value to be set on the ItemRevision."""
    ExtraObject: list[ExtraObjectInfo]
    """The information about the objects that are related to the ItemRevision."""

class NamedReferenceObjectInfo:
    """
    
The NamedReferenceObjectInfo structure represents
all of the data necessary to construct the named reference file attached to a
Dataset.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify
            
            return data element and partial errors associated with this input structure.
            
"""
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The reference to the named reference file for Dataset."""
    RelationTypeName: str
    """
            The real type name of the relation between the revision and the Dataset.
            
"""
    TypeName: str
    """The real type name of the Dataset."""
    AttrNameValuePairs: list[AttributeInfo]
    """The attribute name-value pair to set on the Dataset."""
    NamedReferenceName: str
    """The real Dataset type."""

class PartInfo:
    """
    
The data required to create an Item, ItemRevision and one or more Dataset.
If the Item already exists then it also has the information required to be
updated
for that Item.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return
            
            data elements and partial errors associated with this input structure.
            """
    ItemInput: ItemInfo
    """The information required to create or update an Item."""
    ItemRevInput: ItemRevInfo
    """The information required to create or update an ItemRevision."""
    DatasetInput: list[DatasetInfo]
    """The information required to create or update one or more Dataset objects."""

class SetContentInput:
    """
    
SetContentInput structure represents the
            parameters required to set the contents to Fulltext object.
    """
    def __init__(self, ) -> None: ...
    ObjectToProcess: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """Fulltext object."""
    TransientFileWriteTicket: str
    """FMS ticket of Word file."""

class SetRichContentResponse:
    """
    
SetRichContentResponse - structure represents
            response parameters of setRichContent SOA.
    """
    def __init__(self, ) -> None: ...
    ResultObjects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """This parameter is not used."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class RequirementsManagement:
    """
    Interface RequirementsManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdate(self, Info: list[PartInfo]) -> CreateOrUpdateResponse:
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
    def ExportToApplication(self, Inputs: list[ExportToApplicationInputData]) -> ExportToApplicationResponse:
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
    def GetRichContent(self, Inputs: list[GetContentInput]) -> GetRichContentResponse:
        """    
             getRichContent operation is used to retrieve rich text contents of SpecElement
             type of objects which is a subclass of WorkspaceObject.  A .docm file
             is generated as a result of getRichContent operation which can be opened in MSWord.
             

Use Cases:

             User can open content (body text) in word for view and edit purpose.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Inputs: 
                         A list of structures containing the required information to open requirement content
                         in word.
             
        :return: A list of FMS transient file tickets for each requested requirement. Each ticket
             is for MSWord file containing rich text generated at the server.
        """
        ...
    def ImportFromApplication(self, Inputs: list[ImportFromApplicationInputData]) -> ImportFromApplicationResponse:
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
    def SetRichContent(self, Inputs: list[SetContentInput]) -> SetRichContentResponse:
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

