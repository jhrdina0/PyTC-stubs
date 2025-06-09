import System
import Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport
import Teamcenter.Services.Strong.Importexport._2008_06.FileImportExport
import Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport
import Teamcenter.Services.Strong.Importexport._2012_09.FileImportExport
import Teamcenter.Services.Strong.Importexport._2017_11.FileImportExport
import Teamcenter.Soa.Client
import typing

class FileImportExportRestBindingStub(FileImportExportService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    @typing.overload
    def ExportToApplication(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport.ExportToApplicationInputData]) -> Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport.ExportToApplicationResponse: ...
    @typing.overload
    def ExportToApplication(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2008_06.FileImportExport.ExportToApplicationInputData1]) -> Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport.ExportToApplicationResponse: ...
    @typing.overload
    def ExportToApplication(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.ExportToApplicationInputData2]) -> Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.ExportToApplicationResponse1: ...
    @typing.overload
    def ExportToApplication(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2017_11.FileImportExport.ExportToApplicationInputData3]) -> Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport.ExportToApplicationResponse: ...
    @typing.overload
    def ImportFromApplication(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport.ImportFromApplicationInputData]) -> Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport.ImportFromApplicationResponse: ...
    @typing.overload
    def ImportFromApplication(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2008_06.FileImportExport.ImportFromApplicationInputData1]) -> Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport.ImportFromApplicationResponse: ...
    @typing.overload
    def ImportFromApplication(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.ImportFromApplicationInputData2]) -> Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.ImportFromApplicationResponse1: ...
    @typing.overload
    def ImportFromApplication(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2012_09.FileImportExport.ImportFromApplicationInputData3]) -> Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.ImportFromApplicationResponse1: ...
    @typing.overload
    def GetExportTemplates(self, Filter: Teamcenter.Services.Strong.Importexport._2008_06.FileImportExport.ExportTemplateInput) -> Teamcenter.Services.Strong.Importexport._2008_06.FileImportExport.GetExportTemplateResponse: ...
    @typing.overload
    def GetExportTemplates(self, Filter: list[Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.GetTemplateInput]) -> Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.GetExportTemplateResponse1: ...
    def UpdateReqMarkup(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.MarkupReqUpdateInput]) -> Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.MarkupReqUpdateResponse: ...
    def CreateReqMarkup(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.MarkupReqInput]) -> Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.MarkupReqResponse: ...

class FileImportExportService:
    """
    
            The FileImportExport service provides operations
            to import and export data from/to Teamcenter.  The operation in this service allows
            to import word documents or import of templates to Teamcenter. The operation in this
            service allows the export of Teamcenter business objects to MSWord/MSExcel.
            
            The FileImportExport service can be used for supporting following use cases:
            

Export Teamcenter business objects to Word using static option.
            
Export Teamcenter business objects to Word using Live option.
            
Export Teamcenter business objects to Word for Markups.
            
Export Teamcenter business objects to Excel using static option.
            
Export Teamcenter business objects to Excel using Live option.
            
Export Teamcenter business objects to Excel using Bulk Live option.
            
Export Teamcenter business objects to Excel using export for reimport
            option.
            
Export Teamcenter business objects to Excel using Checkout option
            
Export Teamcenter business objects to Excel using Excel template.
            
Import a Word document to Teamcenter.
            
Import of SpecTemplate, ObjectTemplate and ExcelTemplate.
            
Import a Word document using keywords.
            
Import a Word Live document to set the properties
            
Import a Word Live document to make structural changes.
            
Import a previewed document from Office client.
            




Library Reference:

TcSoaImportExportStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> FileImportExportService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    @typing.overload
    def ExportToApplication(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport.ExportToApplicationInputData]) -> Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport.ExportToApplicationResponse: ...
    @typing.overload
    def ExportToApplication(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2008_06.FileImportExport.ExportToApplicationInputData1]) -> Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport.ExportToApplicationResponse: ...
    @typing.overload
    def ExportToApplication(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.ExportToApplicationInputData2]) -> Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.ExportToApplicationResponse1: ...
    @typing.overload
    def ExportToApplication(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2017_11.FileImportExport.ExportToApplicationInputData3]) -> Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport.ExportToApplicationResponse: ...
    @typing.overload
    def ImportFromApplication(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport.ImportFromApplicationInputData]) -> Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport.ImportFromApplicationResponse: ...
    @typing.overload
    def ImportFromApplication(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2008_06.FileImportExport.ImportFromApplicationInputData1]) -> Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport.ImportFromApplicationResponse: ...
    @typing.overload
    def ImportFromApplication(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.ImportFromApplicationInputData2]) -> Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.ImportFromApplicationResponse1: ...
    @typing.overload
    def ImportFromApplication(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2012_09.FileImportExport.ImportFromApplicationInputData3]) -> Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.ImportFromApplicationResponse1: ...
    @typing.overload
    def GetExportTemplates(self, Filter: Teamcenter.Services.Strong.Importexport._2008_06.FileImportExport.ExportTemplateInput) -> Teamcenter.Services.Strong.Importexport._2008_06.FileImportExport.GetExportTemplateResponse: ...
    @typing.overload
    def GetExportTemplates(self, Filter: list[Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.GetTemplateInput]) -> Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.GetExportTemplateResponse1: ...
    def UpdateReqMarkup(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.MarkupReqUpdateInput]) -> Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.MarkupReqUpdateResponse:
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
    def CreateReqMarkup(self, Inputs: list[Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.MarkupReqInput]) -> Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.MarkupReqResponse:
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

