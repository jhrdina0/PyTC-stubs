import System
import Teamcenter.Soa.Client.Model
import typing

class ExportToApplicationInputData:
    """
    
            The ExportToApplicationInputData structure represents all of the data necessary to
            export selected objects to Word/Excel.
            
    """
    def __init__(self, ) -> None: ...
    ObjectsToExport: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The list of Teamcenter business objects to export."""
    AttributesToExport: list[str]
    """The list of attributes to export."""
    ApplicationFormat: str
    """
            The application format such as "MSWordXML",
            "MSExcel" and "MSExcelLive".
            

            Supported application format for this operation
            


MSWordXML     This format is used for
            exporting WorkspaceObject to static MSWord application.
            
MSExcel    This format is used for exporting
            Teamcenter objects to static MSExcel  application.
            
MSExcelLive    This format is used for
            exporting Teamcenter objects to Live MSExcel  application.
            

"""
    TemplateId: str
    """The name of the Word/Excel template."""

class ExportToApplicationResponse:
    """
    
            ExportToApplicationResponse structure represents the output of export to application
            operation.
            
            It has information about file ticket for the exported file generated at the server.
            
    """
    def __init__(self, ) -> None: ...
    TransientFileReadTickets: list[str]
    """The transient file read tickets for the exported file."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class ImportFromApplicationInputData:
    """
    This holds the data necessary to import an MSWord document into Teamcenter.
    """
    def __init__(self, ) -> None: ...
    TransientFileWriteTicket: str
    """The file ticket of the. docx file to be imported into Teamcenter."""
    ApplicationFormat: str
    """
            The supported application format is MSWordXML


            Supported application format for this operation
            


MSWordXML     This format is used for
            exporting WorkspaceObjects business objects to static MSWord application.
            

"""
    CreateSpecElementType: str
    """The subtype of SpecElement to be created."""

class ImportFromApplicationResponse:
    """
    
            ImportFromApplicationResponse structure represents the output of import from application
            operation. It contains the UID of the BOMWindow after the document is imported to
            Teamcenter.
            
    """
    def __init__(self, ) -> None: ...
    ResultObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The resultant objects which contains the UID of the BOMWindow created after the document
            is imported.  In case of importing templates, it contains the tag of the template.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class FileImportExport:
    """
    Interface FileImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExportToApplication(self, Inputs: list[ExportToApplicationInputData]) -> ExportToApplicationResponse:
        """    
             This operation is used for exporting Teamcenter objects (WorkspaceObject)
             to applications like MSWord and MSExcel. Teamcenter business objects
             should already be created so that the objects can be exported to Word and Excel using
             the service operation.
             
             An MSExcel (.mhtml) or a MSWord (.docx) file is generated at the server
             as a result of this operation.  The generated file will contain Teamcenter objects
             and their properties. Depending upon the application format that is being passed
             as input parameter, the generated file can be opened in Word or Excel.  If the application
             format is "MSWordXML" then the generated
             document is a Word document.  If the application format is "MSExcel" then the generated sheet is a static Excel spreadsheet.
             If the application format is "MSExcelLive"
             then the generated sheet is a Live Excel spreadsheet. "Live" sheet means that modifications
             can be done to the data in Excel which will reflect to Teamcenter.
             



Use Cases:

             User can create Teamcenter objects in RAC and then export those objects and their
             properties to Word or Excel. If "Live" option is selected then User can create "Live"
             spreadsheet after export to Excel.
             

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
                         to Word /Excel.
             
        :return: 
        """
        ...
    def ImportFromApplication(self, Inputs: list[ImportFromApplicationInputData]) -> ImportFromApplicationResponse:
        """    
             This operation imports the contents of the given MSWord document to create
             objects of type SpecElement.  The MSWord document to be imported to
             Teamcenter should have .docx file format. If the application format is MSWordXML
             then the operation parses the given MSWord document to creates a structure of chosen
             subtype of SpecElement.  The parsing of dcoument involves parsing of individual
             paragraphs in the document. Each paragraph in the document with a Heading becomes
             a SpecElement. After the BOM structure is created at the server, a BOMWIndow
             is constructed at the server and returned returned to the caller. Objects of type
             Requirement/Paragraph are created at the server after importing the document.
             This operation supports Word documents in MSOffice Open XML format (.docx
             format) only. If the application format is not set then the operation does not do
             anything.
             

Use Cases:

             User can create an MSWord document and import it using this operation to create
             a structure. Each paragraph in MSWord document represents a Requirement/Paragraph
             in the structure. When this operation is called from Teamcenter rich client, a structure
             is created and is opened in the Requirements Management application.  The structure
             and indentation of the child Requirements is driven by the MSWord outline
             level in the document.  Each Paragraph that is formatted in an outline level
             style produces a separate Requirement. This file may be located in a local
             file system folder or a network folder.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Inputs: 
                         A list of <b>MSWord</b> files to be imported into Teamcenter.
             
        :return: document.
        """
        ...

