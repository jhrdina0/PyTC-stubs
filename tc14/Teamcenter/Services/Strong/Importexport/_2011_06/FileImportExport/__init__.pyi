import System
import System.Collections
import Teamcenter.Services.Strong.Importexport._2008_06.FileImportExport
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DatasetInfo:
    """
    
            This structure contains the markup dataset information like name, type, tool information
            specified by client.
            
    """
    def __init__(self, ) -> None: ...
    Tool: str
    """The tool used to open the created Dataset."""
    DatasetType: str
    """The type of the Dataset to be created."""
    DatasetName: str
    """The name of the markup Dataset to be created."""
    DatasetDesc: str
    """The description of the markup Dataset to be created."""

class ExportToApplicationInputData2:
    """
    
            The ExportToApplicationInputData2 structure represents all of the data necessary
            to export selected objects to specific application like MSWord and MSExcel.
            
    """
    def __init__(self, ) -> None: ...
    ObjectsToExport: list[Teamcenter.Soa.Client.Model.ModelObject]
    """lThe list of Teamcenter business objects to export."""
    AttributesToExport: list[str]
    """The list of attributes to export."""
    ApplicationFormat: str
    """
            The application format such as "MSWordXML",
            "MSWordXMLLive","MSExcel"
            and "MSExcelLive","MSExcelReimport","StructureOnly","StructureWithContents","MSWordXMLLiveMarkupFN", "MSWordXMLFN","MSWordXMLLiveFN"
            

            Supported application format for this operation
            


MSWordXML     This format is used for
            exporting Workspace objects to static MSWord application.
            
MSExcel    This format is used for exporting
            Teamcenter objects to static MSExcel  application.
            
CSV    This format is used for exporting
            Teamcenter objects in a comma separated file format used for audit purpose.
            
MSExcelLive    This format is used for
            exporting Teamcenter objects to Live MSExcel  application.
            
MSExcelReimport    This format is used
            for exporting Teamcenter objects to MSExcel  application for reimport purpose.
            
MSExcelLiveBulkMode    This format is
            used for exporting Teamcenter objects to MSExcel  application for Bulk Live
            mode so that user can make all the property changes and save all the changes to Teamcenter
            on click of "Save to Teamcenter" button.
            
MSWordXMLLive    This format is used for
            exporting objects of type WorkspaceObject to Live  MSWord application.
            
StructureOnly    This format is used for
            exporting Workspace objects to MSWord without its  contents.(only object_name property
            value exported to MSWord)
            
StructureWithContents    This format is
            used for exporting WorkspaceObject to MSWord Live and so that user
            can modify its contents and save them back to Teamcenter.
            
MSWordXMLLiveMarkupFN    This format is
            used for exporting Markups to MSWord Live using FindNo as sorting key.
            
MSWordXMLLiveMarkup    This format is
            used for exporting Markups to MSWord Live.
            
MSWordXMLFN    This format is used for
            exporting WorkspaceObject to static MSWord using FindNo as sorting
            key.
            
MSWordXMLLiveFN    This format is used
            for exporting WorkspaceObject to Live MSWord application using FindNo
            as sorting key.
            

"""
    TemplateId: str
    """The name of the MSWord/MSExcel template"""
    TemplateType: str
    """Type of export template."""
    ObjectTemplateOverride: list[Teamcenter.Services.Strong.Importexport._2008_06.FileImportExport.TemplateOverride]
    """
            The runtime object template override which is association of objectTemplate for a
            Business object type for a chosen SpecTemplate.
            """
    ExportOptions: list[ImportExportOptions]
    """The options to be considered during the export process like "CheckOutObjects""""

class ExportToApplicationResponse1:
    """
    
            ExportToApplicationResponse structure represents the output of export to application
            operation.  It has information about file ticket for the exported file generated
            at the server and the single markup file sent to the client.
            
    """
    def __init__(self, ) -> None: ...
    TransientFileReadTickets: list[str]
    """The transient file read tickets for the exported file."""
    MarkupXMLReadTickets: list[str]
    """
            The transient file read tickets for the generated markup file during Export to Word
            and when the application format is "MSWordXMLLiveMarkup" or "MSWordXMLLiveMarkupFN"
            
"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class FileMetaData:
    """
    
            This structure contains the information about file path, The key will contain "FilePath"
            and data will contain the physical file path of the file to be used for the purpose
            of import/export.
            

    """
    def __init__(self, ) -> None: ...
    Key: str
    """Placeholder for a string called "FilePath"."""
    Data: str
    """Physical file path of the file for import/export to Teamcenter."""

class GetExportTemplateResponse1:
    """
    
            This structure contains the information about the export templates that are queried
            from database. If there is any error during the querying of export templates from
            the database or if there is any error during the operation, then it is added as part
            of ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""
    OutputTmplNames: System.Collections.Hashtable
    """
            The object type of template as key and a vector of template names as the value.
            
"""
    ConfiguredSpecTemplates: list[Teamcenter.Services.Strong.Importexport._2008_06.FileImportExport.ConfiguredTemplate]
    """This parameter is not being used."""
    ConfiguredObjectTemplates: list[Teamcenter.Services.Strong.Importexport._2008_06.FileImportExport.ConfiguredTemplate]
    """This parameter is not being used."""

class GetTemplateInput:
    """
    
            This structure contains information about the templates to be queried from Teamcenter
            database. It will contain additional information in the form of name-value pair to
            store the information about the application domain.
            
    """
    def __init__(self, ) -> None: ...
    TemplateType: str
    """
            The type of template like "SpecTemplate", "ObjectTemplate" and "ExcelTemplate"
            
"""
    NameValueMap: System.Collections.Hashtable
    """The name value pair to store information about the application domain."""

class ImportExportOptions:
    """
    
            This structure contains additional options required to pass during the Import\Export
            operations. importOptions: This structure is used for providing the import or export
            options depending on the mode of operation. This is key/value pair.
            
            Following are the available options used during importing data to Teamcenter
            

UnCheckOutObjects - Performs uncheckout operation
            
SyncTeamcenter - Synchronize Teamcenter data with document
            
FeedbackRequired - Runs SOA in "feedback" mode, so check conflicting
            objects
            
SyncDocument - Synchronize document with Teamcenter
            
ReviseAllObjects - Revise option (not used)
            
ReviseOverwriteObjects - Revise option for "modified" objects after
            export
            
IgnoreCheckoutObjects - Ignore checked out objects and save remaining
            objects.
            
CheckInObjects - Check in objects
            
UnCheckOutObjects - UnCheckout objects
            


            Following are the available options used during exporting data to Teamcenter
            

ShowTransferModeWarning - to show warning if secondary objects are
            exported to Word Live with structure editing.
            
CheckOutObjects - Checkout objects.
            


    """
    def __init__(self, ) -> None: ...
    Option: str
    """
            The option name can be as below
            

UnCheckOutObjects
            
SyncTeamcenter
            
FeedbackRequired
            
SyncDocument
            
ReviseAllObjects
            
ReviseOverwriteObjects
            
IgnoreCheckoutObjects
            
CheckInObjects
            

"""
    Value: str
    """
            The option's value can be as below
            

UnCheckOutObjects
            
SyncTeamcenter
            
FeedbackRequired
            
SyncDocument
            
ReviseAllObjects
            
ReviseOverwriteObjects
            
IgnoreCheckoutObjects
            
CheckInObjects
            

"""

class ImportFromApplicationInputData2:
    """
    
            The ImportFromApplicationInputData2 structure represents all of the data necessary
            to import a specification into Teamcenter or import templates to Teamcenter.
            
    """
    def __init__(self, ) -> None: ...
    TransientFileWriteTicket: str
    """The file ticket of the. docx file to be imported into Teamcenter."""
    ApplicationFormat: str
    """
            The application format such as "MSWordXML","MSWordXMLLive",
            "MSWordXMLOverWriteCheck", "MSWordSpecTemplate", "MSWordObjTemplate",
            "MSExcelTemplate" and "MSWordSetContent"
            

            Supported application formats for this operation
            


MSWordXML     This format is used for
            importing a MSWord document to Teamcenter.
            
MSWordXMLLive    This format is used for
            importing a Live MSWord document to
            


                                                Teamcenter.
            

MSWordXMLExisting    This format is used
            for importing a  MSWord document and
            


                                                        create
            a Specification within an existing chosen Specification.
            

MSWordSetContent    This format is used
            for importing a  Live MSWord document to
            


                                                    Teamcenter.
            This format is used by the embedded viewer to
            
                                                    set
            the rich text of SpecElement and to set the properties on the
            
                                                    SpecElement.
            

MSWordSpecTemplate    This format is used
            for importing a Specification template to
            


                                                        Teamcenter.
            

MSWordObjectTemplate    This format is
            used for importing a ObjectTemplate to
            


                                                            Teamcenter.
            

MSWordExcelTemplate    This format is
            used for importing a ExcelTemplate to
            


                                                            Teamcenter.
            """
    CreateSpecElementType: str
    """The subtype of SpecElement to be created."""
    SpecificationType: str
    """The subtype of Specification to be created."""
    IsLive: bool
    """Flag to determine static or live option. Default value is non live."""
    SelectedBomLine: Teamcenter.Soa.Client.Model.ModelObject
    """The top BOMLine under which new structure gets imported."""
    FileMetaDatalist: list[FileMetaData]
    """
            The list of structures that contains information about the physical file path of
            the file.
            """
    ImportOptions: list[ImportExportOptions]
    """The additional options that user can pass for import purpose."""
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with the input structure.
            """

class ImportFromApplicationOutputData:
    """
    
            The structure contains the information about the data that is passed back to the
            client after the result of importFromApplication SOA operation. It contains the UID
            of the BOMWindow after the document is imported to Teamcenter.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            
"""
    TransientFileTickets: list[str]
    """The file ticket of the transient file to be imported."""
    ResultObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The objects like the BOMWindow tag if the import is successful.
            
"""

class ImportFromApplicationResponse1:
    """
    
            ImportFromApplicationResponse1 structure represents the output of import from application
            operation. It contains UID of the BOMWindow created after the document is imported.
            In case of import of templates, it contains the business object of the tenplate
            after the import operation.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The Service Data. It holds the error stack which contains information about any errors
            that are generated during importFromApplication operation.
            
"""
    Output: list[ImportFromApplicationOutputData]
    """
            The list of structure containing the resultant objects which contains the UID of
            the BOMWindow created after the document is imported.  In case of importing
            templates, it contains the business object of the template. It also contains the
            file ticket of the xml file containing the details about the generated errors at
            the server during importFromApplication operation.
            """

class MarkupReqInput:
    """
    
            Input structure containing the Single Markup XML info and Markup dataset info to
            be created
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """This is not used."""
    MarkupDataset: DatasetInfo
    """This is not used."""
    ReqObj: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """This is not used."""
    IsLiveMarkup: bool
    """
            This should be always false as we do not support markup in live mode.
            
"""
    TransientFileWriteTickets: list[str]
    """FMS ticket of "mrk" file."""

class MarkupReqOutput:
    """
    
            This structure containing the information about the created markup Dataset
            and the GRM relation on the created markup Dataset to the FullText.
            
    """
    def __init__(self, ) -> None: ...
    MarkupDatset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """The created markup Dataset."""
    Relation: Teamcenter.Soa.Client.Model.Strong.ImanRelation
    """The GRM relation on the created Dataset to the FullText."""

class MarkupReqResponse:
    """
    
            Structure containing markup output with created markup Dataset information
            and ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    MarkupInfo: System.Collections.Hashtable
    """This is not used."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Updated markup Dataset are added to updated object list of ServiceData."""

class MarkupReqUpdateInput:
    """
    Markup dataset sent by the client that needs to be updated
    """
    def __init__(self, ) -> None: ...
    MarkupDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Markup dataset sent by the client that needs to be updated"""
    ReqObj: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """Requirement object ID which has the markups that need an update"""
    IsLiveMarkup: bool
    """Flag indicating whether markup is on live or non live document"""
    TransientFileWriteTickets: list[str]
    """Contains an FMS ticket of the single XML file uploaded"""

class MarkupReqUpdateResponse:
    """
    Structure containing markup dataset update response
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Updated markup dataset will be returned in the ServiceData. Any failure will be returned
            with error message in the ServiceData list of partial errors.
            """

class FileImportExport:
    """
    Interface FileImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def UpdateReqMarkup(self, Inputs: list[MarkupReqUpdateInput]) -> MarkupReqUpdateResponse:
        """    
             This operation creates new markups and updates existing markups in rich text content
             of SpecElement objects that are exported to MSWord using markup option.
             
             This operation will take information about markups in the form of mrk file. User
             needs to have Office Client installed to create and update the markups in Word document.
             

Use Cases:

             User can install Office Client and export SpecElement to MSWord using
             the markup option. Office Client provides a mechainsm to create or update markups
             in a Word document.
             

Teamcenter Component:

             Import/Export - Import / export of Tc data model in a binary format that CMS uses.
             
        :param Inputs: 
                         A list of structures containing the required information to create or update markups
                         for <b>Requirement</b> objects.
             
        :return: information and ServiceData
             with partial errors.
        """
        ...
    def CreateReqMarkup(self, Inputs: list[MarkupReqInput]) -> MarkupReqResponse:
        """    
             This operation will take info for markup datasets to be created for the requirement
             objects and create a markup dataset for each markup data requirement object.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Inputs: 
                         Inputs containing markup dataset info to be created, requirement obj IDs, single
                         markup xml to be uploaded
             
        :return: Response contains created markup dataset info and service data with partial errors
        """
        ...
    def ExportToApplication(self, Inputs: list[ExportToApplicationInputData2]) -> ExportToApplicationResponse1:
        """    
             This operation is used for exporting Teamcenter objects (WorkspaceObject)
             to applications like MSWord and MSExcel. Teamcenter business objects should already
             be created so that the objects can be exported to Word and Excel using the service
             operation.
             
             An MSExcel (.xlsm) or a MSWord (.docx) file or a comma separated file (.csv) file
             is generated at the server as a result of this operation.  The generated file will
             contain Teamcenter objects and their properties. Depending upon the application format
             that is being passed as input parameter, the generated file can be opened in MSWord
             or MSExcel.  If the application format is "CSV"
             then a comma separated file is generated at the server.  If the application format
             is "MSWordXML" then the generated document
             is a Word document.  It traverses the structure for the given SpecElement deep and
             exports all its children to MSWord document. If the application format is "MSExcel" then the generated sheet is a static Excel
             spreadsheet.  If the application format is "MSExcelLive"
             then the generated sheet is a Live Excel spreadsheet. "Live" sheet means that modifications
             can be done to the data will reflect to Teamcenter.  If the application format is
             "MSWordXMLLive" then the generated document
             is a Live Word document.  This mode provides the capability of Live editing the SpecElement
             in the word document.  A "Live" Word document means that the any modifications done
             in the document like changing the rich text or editing of properties will be saved
             to Teamcenter on click of "Save"button in MSWord. If the application format is "MSExcelReimport" then the generated sheet can be
             reimported back to Teamcenter. If the application format is "MSExcelLiveBulkMode" then the sheet is generated in "Bulk Live"
             mode. This mode enables the user to make all the changes to the properties of objectsfrom
             Excel and then commit the changes to Teamcenter on click of "Save to Teamcenter"
             button in Excel.  If the application format is "StructureOnly"
             then the structure can be exported to Word without the contents having only "object_name"
             property in the exported document.  If the application format is "StructureWithContents" then the structure is exported to MSWord
             along with the contents (rich text) of each element in the structure.  This mode
             provides the ability of live editing and structure editing of SpecElements in the
             MSWord document. User can edit the contents or can make structural changes to the
             exported document.  If the application format is "MSWordXMLLiveMarkupFN"
             then Markups will be exported to MSWord using FindNo as sorting key.  If the application
             format is "MSWordXMLFN" then a static structure
             can be exported to MSWord using FindNo as sorting key.  If the application format
             is "MSWordXMLLiveFN" then a "Live" structure
             can be exported to MSWord using FindNo as sorting key.  If the export Option is "CheckOutObjects"
             then the objects can be checked out before exporting to MSWord/Excel.
             

Use Cases:

             User can create Teamcenter objects in RAC and then export those objects and their
             properties to Word or Excel. If "Live" option is selected then user can create "Live"
             documents after export to Word/Excel.  During the export to Word/Excel, Teamcenter
             objects are exported to Word/Excel by applying the appropriate templates. User can
             export Teamcenter objects to Excel which can be imported back to Teamcenter. User
             can create excel sheet in a "Bulk Live" mode so that bulk changes can be committed
             to Teamcenter.  User can export the objects and properties to a comma separated file.
             User can create SpecTemplate, ObjectTemplate and ExcelTemplate in Teamcenter and
             customize these templates as per User need such as adding more properties or adding
             formatting information to the templates.  User can associate different objectTemplate
             for every Business object type at runtime and specify this configuration when using
             this operation. User can export a structure to MSWord without exporting the
             rich text of each SpecElement. User can export a structure for "Live" edit and structure
             edit to MSWord.  User can export a static or a "Live" structure along with the Markups.
             Users can checkout objects during Export to MSWord/MSExcel.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Inputs: 
                         A list of ExportToApplicationInputData2 structures containing the required information
                         to export Teamcenter business objects to Word /Excel.  The set of objects to export,
                         the attributes to export, the application format and the template name to be used
                         for exporting are part of the input structure.
             
        :return: 
        """
        ...
    def GetExportTemplates(self, Filter: list[GetTemplateInput]) -> GetExportTemplateResponse1:
        """    
getExportTemplates is responsible for getting
             various export templates from database based on input filter. Export templates can
             be of type SpecTemplate, ObjectTemplate or ExcelTemplate. Depending
             upon the input filter, the templates of type SpecTemplate or ObjectTemplate
             or ExcelTemplate are retrieved from the database. These templates can be used
             by the application for export purpose.
             

Use Cases:

             User can create Items of type SpecTemplate or ObjectTemplate or ExcelTemplate
             in Teamcenter and use this operation to get the desired template types.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Filter: 
                         A list of GetTemplateInput structures containing the required information to retrieve
                         the type of export templates to get from database.
             
        :return: 
        """
        ...
    def ImportFromApplication(self, Inputs: list[ImportFromApplicationInputData2]) -> ImportFromApplicationResponse1:
        """    
             This operation is used for importing the contents of the given MSWord  document
             (.docx) to create objects of type SpecElement.  Based on the application format,
             this operation can also be used for importing SpecTemplate, ObjectTemplate
             and ExcelTemplate in database.
             
             If the application format is "MSWordXML" then the operation parses the given
             MS Word document to creates a structure of type SpecElement.
             
             If the application format is "MSWordSpecTemplate" or "MSWordObjTemplate"
             or "MSExcelTemplate" then the chosen template can be imported into Teamcenter.
             
             If the application format is "MSWordXMLLive" then a "Live" document can be
             imported to Teamcenter.  To use this application format, a "Live" document should
             be generated from Teamcenter.
             
             If the application format is "MSWordSetContent" then it can set the rich text
             of the SpecElement  by applying the templates at the server.
             
             If the application format is "MSWordXMLExisting" then the given MSWord document
             is imported to Teamcenter to create a Specification within an existing chosen Specification.
             
             If the application format is "MSWordImportUsingKW" then the given MSWord document
             is imported to Teamcenter if user chooses keywords supplied by user. The keywords
             are parsed at the server to create the appropriate SpecElement type when the keyword
             is found.
             
             If the application format is "StructureOnly" then the given MSWord Live document
             is imported to Teamcenter without its  contents.(only object_name property value)
             
             If the application format is "StructureWithContents" then the given MSWord
             Live document is imported to Teamcenter along with its rich text contents.
             
             If the application format is "MSWordXWithFulltext" then this operation can
             be used to create new FullText with provided rich text in given MSWord document
             and this FullText needs to be attached to selected ItemRevision. Currently
             this gets called from Rich client in case of editing rich text for only Systems Engineering
             revision objects,if there is no FullText dataset associated.to selected ItemRevision.
             
             If the application format is "MSWordXWithFulltext"then this operation can
             be used to create FullText object with input rich text in given document.
             The created FullText object will be attached to selected object revision.
             Currently this format is called from Rich client in case of editing rich text for
             only Systems Engineering revision objects and if there is no FullText dataset
             associated.to selected revision.
             
             When Objects objects of type Requirement/Paragraph are created at the server
             after importing the document.  When this operation is called from Teamcenter rich
             client, a structure is created and is opened in the RequirementsManagement
             application.  The structure and indentation of the child Requirement is driven by
             the outline levels in the document.  Each Paragraph that is formatted in an
             outline level style produces a separate Requirement. This file may be located
             in a local file system folder or a network folder.  Import of document to Teamcenter
             supports Word documents in MSOffice Open XML format (.docx format) only. Import
             of templates to Teamcenter supports Word documents in MSOffice Open XML format.
             (.docx and .docm format)
             

             Supported application formats for this operation
             


StructureOnly    This format is used for
             importing MSWord document to Teamcenter without its  contents.(only object_name
             property value).
             
StructureWithContents This format is used for importing WorkspaceObject
             to MSWord Live and so that user can modify its contents and save them back
             to Teamcenter.
             
MSWordImportUsingKW    This format is
             used for importing a MSWord document to Teamcenter using keywords supplied
             by user.
             
MSWordImportExistingUsingKW This format is used for importing
             a MSWord document to create a Specification in Teamcenter into an existing
             Specification when keywords are supplied by user.
             
MSWordXWithFulltext    This format is
             used for importing a MSWord document when user wanted to create new FullText
             with provided rich text in given document and this FullText needs to be attached
             to selected ItemRevision. Currently this gets called from Rich client in case
             of editing rich text for only ItemRevision objects, if there is no FullText
             dataset associated to selected ItemRevision.
             
MSWordXMLPreview This format is used for importing a MSWord
             document to create a Specification from a document previewed by Office client.
             



Use Cases:

             User can create an MSWord document and import it using this operation to create
             a structure. Each paragraph in Word document represents a Requirement/Paragraph in
             the structure. User can import templates (SpecTemplate, ObjectTemplate
             and ExcelTemplate) to Teamcenter. User can import a "Live" document generated
             in Teamcenter and set the properties of Workspace objects. User can set the rich
             text of the SpecElement using the embedded MSWord from RAC. User can prevent
             overwrite of objects which are edited by others.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Inputs: 
                         A list of <font face="courier" height="10">ImportFromApplicationInput2</font> structures
                         containing the required information to import MSWord document to Teamcenter or import
                         templates to teamcenter.
             
        :return: 
        """
        ...

