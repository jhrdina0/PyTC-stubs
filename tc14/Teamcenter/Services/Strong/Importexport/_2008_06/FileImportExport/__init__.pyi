import System
import Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport
import Teamcenter.Soa.Client.Model
import typing

class ConfiguredTemplate:
    """
    
            The ConfiguredTemplate structure contains
            the information required to get IRDC configured export templates. BMIDE enables the
            user to configure templates based on the object type using the IRDC configuration.
            
    """
    def __init__(self, ) -> None: ...
    BusinessObjectType: str
    """Type name of business object."""
    TemplateName: str
    """The name of the configured template on business object type."""
    TemplateType: str
    """The type name of configured template."""

class ExportTemplateInput:
    """
    
            The ExportTemplateInput structure contains the flags that are required to filter
            the different type of export templates such as SpecTemplate, ObjectTemplate
            and ExcelTemplate from the database.
            
    """
    def __init__(self, ) -> None: ...
    GetSpecTemplates: bool
    """If set to true then it will query for SpecTemplates in database."""
    GetObjectTemplates: bool
    """If set to true then it will query for ObjectTemplates in database."""
    GetExcelTemplates: bool
    """If set to true then it will query for ExcelTemplates in database."""
    GetConfiguredSpecTemplate: bool
    """This element is not used."""
    GetConfiguredObjectTemplate: bool
    """This element is not used."""

class ExportToApplicationInputData1:
    """
    
            The ExportToApplicationInputData1 structure represents all of the data necessary
            to export selected Teamcenter objects to MSWord/Excel.
            
    """
    def __init__(self, ) -> None: ...
    ObjectsToExport: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The list of Teamcenter business objects to export."""
    AttributesToExport: list[str]
    """The list of attributes to export."""
    ApplicationFormat: str
    """
            The application format such as "MSWordXML",
            "MSExcel", "MSExcelLive",
            "MSExcelReimport", "MSWordXMLLive", "MSExcelLiveBulkMode".
            

            Supported application format for this operation
            


MSWordXML     This format is used for
            exporting Workspace objects to static MSWord application.
            
MSExcel    This format is used for exporting
            Teamcenter objects to static MSExcel  application.
            
MSExcelLive    This format is used for
            exporting Teamcenter objects to Live MSExcel  application.
            
MSExcelReimport    This format is used
            for exporting Teamcenter objects to MSExcel
            


            application for reimport purpose.
            

MSExcelLiveBulkMode    This format is
            used for exporting Teamcenter objects to MSExcel  application for Bulk Live mode
            so that user can make all the property changes and save all the changes to Teamcenter
            on click of "Save to Teamcenter"button.
            
MSWordXMLLive    This format is used for
            exporting Workspace objects to Live MSWord application.
            

"""
    TemplateId: str
    """The name of the Word/Excel template"""
    TemplateType: str
    """The type of the export template."""
    ObjectTemplateOverride: list[TemplateOverride]
    """
            The runtime object template override which is association of objectTemplate for a
            Business object type for a  chosen SpecTemplate.
            """

class GetExportTemplateResponse:
    """
    
            The GetExportTemplateResponse Return represents the output of getExportTemplates
            operation which contains the information about the objects of type SpecTemplate,
            ObjectTemplate and ExcelTemplate that are queried from the database.
            Example- If the input filter flag (getSpecTemplates) is set to true in ExportTemplateInput
            structure, then the GetExportTemplateResponse structure will contain the all the
            objects of type SpecTemplate

    """
    def __init__(self, ) -> None: ...
    SpecTemplates: list[str]
    """The list of objects of type SpecTemplate"""
    ObjectTemplats: list[str]
    """The list of objects of type ObjectTemplate"""
    ExcelTemplates: list[str]
    """The list of objects of type ExcelTemplate"""
    ConfiguredSpecTemplates: list[ConfiguredTemplate]
    """This is not used"""
    ConfiguredObjectTemplates: list[ConfiguredTemplate]
    """This is not used"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class ImportFromApplicationInputData1:
    """
    
            The ImportFromApplicationInputData1 structure represents all of the data necessary
            to import a specification into Teamcenter or import templates to Teamcenter.
            
    """
    def __init__(self, ) -> None: ...
    TransientFileWriteTicket: str
    """The file ticket of the. docx file to be imported into Teamcenter."""
    ApplicationFormat: str
    """
            The application format suchas "MSWordXML",
            "MSWordXMLLive", "MSWordXMLOverWriteCheck",
            "MSWordSpecTemplate","MSWordObjTemplate","MSExcelTemplate"
            and "MSWordSetContent"
            

            Supported application formats for this operation
            


MSWordXML     This format is used for
            importing a MSWord document to Teamcenter.
            
MSWordXMLLive    This format is used for
            importing a Live MSWord document to Teamcenter.
            
MSWordXMLOverwriteCheck    This format
            is used for importing a  Live MSWord document to Teamcenter and check for
            overwrite condition on the object during setting of properties in database.
            
MSWordSetContent    This format is used
            for importing a  Live MSWord document to
            


            Teamcenter. This format is used by the embedded viewer to set the rich text of SpecElement
            and to set the properties on the SpecElement.
            

MSWordSpecTemplate    This format is used
            for importing a SpecificationTemplate to
            


            Teamcenter.
            

MSWordObjectTemplate    This format is
            used for importing a ObjectTemplate to Teamcenter.
            
MSWordExcelTemplate    This format is
            used for importing a ExcelTemplate to Teamcenter.
            

"""
    CreateSpecElementType: str
    """The subtype of SpecElement to be created."""
    SpecificationType: str
    """The subtype of Specification to be created."""
    IsLive: bool
    """
            If the flag is set to true then it indicates "live" option.
            
            If the flag is set to false then it indicates "static" option.
            
"""

class TemplateOverride:
    """
    The structure represents all of the data necessary to override object templates.
    """
    def __init__(self, ) -> None: ...
    BusinessObjectType: str
    """The type of business object."""
    TemplateId: str
    """The name of object template."""
    TemplateType: str
    """The type of object template."""

class FileImportExport:
    """
    Interface FileImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExportToApplication(self, Inputs: list[ExportToApplicationInputData1]) -> Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport.ExportToApplicationResponse:
        """    
             This operation is used for exporting Teamcenter objects (WorkspaceObject) to applications
             like MSWord and MSExcel. Teamcenter business objects should already be created so
             that the objects can be exported to MSWord and MSExcel using the service operation.
             
             An Excel (.mhtml) or a Word (.docx) file or a comma separated file (.csv) file is
             generated at the server as a result of this operation.  The generated file will contain
             Teamcenter objects and their properties. Depending upon the application format that
             is being passed as input parameter, the generated file can be opened in MSWord or
             MXExcel.  If the application format is "MSWordXML" then the generated document
             is a Word document.  It traverses the structure for the given SpecElement deep and
             exports all its children to MSWord document. If the application format is
             "MSExcel" then the generated sheet is a static Excel spreadsheet.  If the
             application format is "MSExcelLive" then the generated sheet is a Live Excel
             spreadsheet. "Live" sheet means that modifications can be done to the data will reflect
             to Teamcenter.  If the application format is "MSWordXMLLive" then the generated
             document is a Live Word document.  A "Live" Word diocument means that the any modifications
             done in the document like changing the rich text or editing of properties will be
             saved to Teamcenter on click of "Save" button in MSWord. If the application
             format is "MSExcelReimport" then the generated sheet can be reimported back
             to Teamcenter. If the application format is "MSExcelLiveBulkMode"then the
             sheet is generated in "Bulk Live" mode. This mode enables the user to make all the
             changes to the properties of objectsfrom Excel and then commit the changes to Teamcenter
             on click of "Save to Teamcenter" button in Excel.
             


Use Cases:

             User can create Teamcenter objects in RAC and then export those objects and their
             properties to Word or Excel. If "Live" option is selected then User can create "Live"
             documents after export to Word/Excel.  During the export to Word/Excel, Teamcenter
             objects are exported to Word/Excel by applying the appropriate templates. User can
             export Teamcenter objects to Excel which can be imported back to Teamcenter. User
             can create excel sheet in a "Bulk Live" mode so that bulk changes can be committed
             to Teamcenter.  User can export the objects and properties to a comma separated file.
             User can create SpecTemplate, ObjectTemplate and ExcelTemplate in Teamcenter and
             customize these templates as per User need such as adding more properties or adding
             formatting information to the templates.  User can associate different objectTemplate
             for every Business object type at runtime and specify this configuration when using
             this operation.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Inputs: 
                         A vector of <font face="courier" height="10">ExportToApplicationInputData1</font>
                         structures containing the required information to export Teamcenter business objects
                         to Word /Excel. The set of objects to export, the attributes to export, the application
                         format and the template name to be used for exporting are part of the input structure.
             
        :return: 
        """
        ...
    def GetExportTemplates(self, Filter: ExportTemplateInput) -> GetExportTemplateResponse:
        """    
             This operation is used for retrieving all the MSWord and MSExcel templates from database.
             An input filter can be applied to get the desired template type from database. All
             the Word and Excel templates are of Item
             type. Depending on the input filter, the Item of type SpecTemplate or ObjectTemplate
             or ExcelTemplate are retrieved from the database. These templates are used
             by the application for export purpose. If the chosen filter is of type SpecTemplate
             or ObjectTemplate then the document to be imported is in .docx or .docm file
             format.  If the chosen filter is of type ExcelTemplate then the spreadsheet
             to be imported is in .xlsx or .xlsm file format.
             

Use Cases:

             User can import MSWord and MSExcel templates to Teamcenter and use these templates
             for export purpose. During this operation, items of type SpecTemplate or ObjectTemplate
             or ExcelTemplate is created after the import operation in Teamcenter.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Filter: 
                         A list of structures containing the flags required to filter the <b>SpecTemplate</b>,
                         <b>ObjectTemplate</b> and <b>ExcelTemplate</b> type of the export templates from
                         database.
             
        :return: 
        """
        ...
    def ImportFromApplication(self, Inputs: list[ImportFromApplicationInputData1]) -> Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport.ImportFromApplicationResponse:
        """    
             This operation is used for importing the contents of the given MSWord document (.docx)
             to create objects of type SpecElement.  Based on the application format, this
             operation can also be used to import objects of type SpecTemplate,ObjectTemplate
             and ExcelTemplate in database. If the application format is "MSWordXML"then the operation parses the given MS Word document
             to creates a structure of type SpecElement.  If the application format is "MSWordSpecTemplate" or "MSWordObjTemplate"or
             "MSExcelTemplate" then the chosen template
             can be imported into Teamcenter.  If the application format is "MSWordXMLLive" then a "Live" document can be imported to Teamcenter.
             To use this application format, a "Live" document should be generated from Teamcenter.
             If the application format is "MSWordSetContent"
             then it can set the rich text of the SpecElement  and the properties on the
             SpecElement by using the SpecficationTemplate and ObjectTemplate at
             the server. If the application format is "MSWordXMLOverWriteCheck"
             then the Teamcenter objects will be checked for overwrite condition at the server.
             
             The objects of type Requirement/Paragraph are created at the server after
             import of the document.  If this operation is called from Teamcenter rich client,
             a structure is created and is opened in the RequirementsManagement application.
             The structure and indentation of the child Requirement is driven by the outline
             levels in the document.  Each Paragraph that is formatted in an outline level
             style produces a separate Requirement. This file may be located in a local
             file system folder or a network folder.  Import of document to Teamcenter supports
             Word documents in MS Office Open XML format (.docx format) only. Import of templates
             to Teamcenter supports MSWord documents in MS Office Open XML format. (.docx and
             .docm format)
             

Use Cases:

             User can create an MSWord document and import it using this operation to create
             a structure. Each paragraph in MSWord document represents a Requirement/Paragraph
             in the structure. User can import templates (SpecTemplate, ObjectTemplate
             and ExcelTemplate) to Teamcenter. User can import a "Live" document generated
             in Teamcenter and set the properties of Workspace objects. User can set the rich
             text of the SpecElement using the embedded Word from RAC. User can prevent overwrite
             of objects which are edited by others.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Inputs: 
                         A vector of <font face="courier" height="10">ImportFromApplicationInputData1</font>
                         containing the required information to import MSWord document to Teamcenter or import
                         templates to Teamcenter.  The transientfile ticket of the file to be imported, application
                         format, the <b>SpecElement</b> type to be imported, the type of <b>Specification</b>
                         and the flag to indicate live import are part of this structure.
             
        :return: 
        """
        ...

