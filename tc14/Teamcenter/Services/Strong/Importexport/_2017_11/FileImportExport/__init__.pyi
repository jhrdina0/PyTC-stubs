import System
import Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport
import Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport
import Teamcenter.Soa.Client.Model
import typing

class ExportPackingInfo:
    """
    
            The structure contains a primary business object and a list of secondary business
            objects.
            
    """
    def __init__(self, ) -> None: ...
    PrimaryObj: Teamcenter.Soa.Client.Model.ModelObject
    """The primary business object. The primary business object can be of any type."""
    SecondaryObjs: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of secondary business objects. The secondary business objects can be of any
            type.
            """

class ExportToApplicationInputData3:
    """
    
            The ExportToApplicationInputData3 structure represents all of the data necessary
            to export selected objects to specific application like MSExcel.
            
    """
    def __init__(self, ) -> None: ...
    ExportPackingInfos: list[ExportPackingInfo]
    """A list of ExportPackingInfo."""
    ColumnAttributes: list[str]
    """The column attributes to export."""
    ApplicationFormat: str
    ExportOptions: list[Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.ImportExportOptions]
    """List of ImportExportOptions to be used during the export process."""

class FileImportExport:
    """
    Interface FileImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExportToApplication(self, Inputs: list[ExportToApplicationInputData3]) -> Teamcenter.Services.Strong.Importexport._2007_06.FileImportExport.ExportToApplicationResponse:
        """    
             This operation is used for exporting Teamcenter objects to MSExcel. Each row in the
             MSExcel sheet can contain multiple Teamcener business objects and its properties.
             Teamcenter business objects should already be created so that the objects can be
             exported to MSExcel using the service operation.
             
             An MSExcel (.xlsm) file is generated at the server as a result of this operation.
             If the application format is "MSExcel" then the generated sheet is a static Excel
             spreadsheet. If the application format is "MSExcelLive" then the generated sheet
             is a Live Excel spreadsheet. "Live" sheet means that modifications done to the excel
             data will reflect to Teamcenter. If the export Option is "CheckOutObjects" then the
             objects will be checked out before exporting to Excel. Right now it only supports
             exporting to MSExcel, but we could support exporting to other application like MSWord
             in the future.
             

Use Cases:

             User can use this service operation to export 4GD objects from content pane to MSExcel.
             In the generated sheet, each row will contain multiple business objects and their
             properties. The properties can be edited from Excel and saved back to Teamcenter
             and vice versa.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Inputs: 
                         A list of ExportToApplicationInputData3 structures containing the required information
                         to export Teamcenter business objects to Excel.
             
        :return: 
        """
        ...

