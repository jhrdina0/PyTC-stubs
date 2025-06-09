import System
import Teamcenter.Services.Strong.Reports._2007_01.CrfReports
import Teamcenter.Services.Strong.Reports._2007_06.CubeReports
import Teamcenter.Services.Strong.Reports._2008_06.CrfReports
import Teamcenter.Services.Strong.Reports._2008_12.CrfReports
import Teamcenter.Services.Strong.Reports._2010_04.CrfReports
import Teamcenter.Services.Strong.Reports._2015_03.CrfReports
import Teamcenter.Services.Strong.Reports._2015_10.CrfReports
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CrfReportsRestBindingStub(CrfReportsService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateReportDefinition(self, ReportProperties: Teamcenter.Services.Strong.Reports._2007_01.CrfReports.ReportProperties) -> Teamcenter.Services.Strong.Reports._2007_01.CrfReports.CreateReportDefinitionResponse: ...
    @typing.overload
    def GenerateReport(self, InputCriteria: Teamcenter.Services.Strong.Reports._2007_01.CrfReports.GenerateReportCriteria, ApplicationId: str) -> Teamcenter.Services.Strong.Reports._2007_01.CrfReports.GenerateReportResponse: ...
    @typing.overload
    def GenerateReport(self, Inputs: list[Teamcenter.Services.Strong.Reports._2010_04.CrfReports.GenerateReportsCriteria2]) -> Teamcenter.Services.Strong.Reports._2015_03.CrfReports.GenerateReportsResponse2: ...
    def GenerateReportDefintionIds(self, InputCriteria: list[Teamcenter.Services.Strong.Reports._2007_01.CrfReports.ReportsCriteria]) -> Teamcenter.Services.Strong.Reports._2007_01.CrfReports.GenerateReportDefintionIdsResponse: ...
    @typing.overload
    def GetReportDefinitions(self, InputCriteria: list[Teamcenter.Services.Strong.Reports._2007_01.CrfReports.ReportsCriteria]) -> Teamcenter.Services.Strong.Reports._2007_01.CrfReports.GetReportDefinitionsResponse: ...
    @typing.overload
    def GetReportDefinitions(self, InputCriteria: list[Teamcenter.Services.Strong.Reports._2008_06.CrfReports.ReportsCriteria2]) -> Teamcenter.Services.Strong.Reports._2007_01.CrfReports.GetReportDefinitionsResponse: ...
    @typing.overload
    def GenerateReports(self, Inputs: list[Teamcenter.Services.Strong.Reports._2008_12.CrfReports.GenerateReportsCriteria]) -> Teamcenter.Services.Strong.Reports._2008_12.CrfReports.GenerateReportsResponse: ...
    @typing.overload
    def GenerateReports(self, Inputs: list[Teamcenter.Services.Strong.Reports._2010_04.CrfReports.GenerateReportsCriteria2]) -> Teamcenter.Services.Strong.Reports._2008_12.CrfReports.GenerateReportsResponse: ...
    def GetPrintTemplates(self, ContextObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Reports._2007_01.CrfReports.GetReportDefinitionsResponse: ...
    def GeneratePrintReports(self, ReportDefObj: Teamcenter.Soa.Client.Model.Strong.ReportDefinition, Inputs: list[Teamcenter.Services.Strong.Reports._2015_03.CrfReports.PrintReportsCriteria]) -> Teamcenter.Services.Strong.Reports._2015_03.CrfReports.GeneratePrintReportsResponse: ...
    def GetOfficeStylesheets(self, ReportDefinition: Teamcenter.Soa.Client.Model.Strong.ReportDefinition) -> Teamcenter.Services.Strong.Reports._2015_10.CrfReports.GetOfficeStyleSheetResponse: ...

class CrfReportsService:
    """
    
            The CrfReports service provides operations
            to manage the Summary reports/Item reports/Custom reports . CRF
stands for Common
            Report Framework. The operations in this service allow creating
report definition,
            loading report definition, generating reports by user inputs,
generating report definition
            id for new report definition, generate URL for TcRA
            operations. Teamcenter provides three types reports based on the
queries. User can
            create Summary Report, Custom Report, and Item Report by CrfReports
service.

            The CrfReports service can be used for supporting following use-
cases:

Create Summary Report/Custom Report/Item Report.

Load the report definition by input criteria.

Generate Summary Report/Custom Report/Item Report.

Library Reference:

TcSoaReportsStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> CrfReportsService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateReportDefinition(self, ReportProperties: Teamcenter.Services.Strong.Reports._2007_01.CrfReports.ReportProperties) -> Teamcenter.Services.Strong.Reports._2007_01.CrfReports.CreateReportDefinitionResponse:
        """    
             Creates a report definition with the specified properties.
             

Teamcenter Component:

             Business Intelligence - Capability to create and manage report definitions and generate
             reports
             
        :param ReportProperties: 
                         The report properties for the report definition.
             
        :return: The report definition and the ServiceData.
        """
        ...
    @typing.overload
    def GenerateReport(self, InputCriteria: Teamcenter.Services.Strong.Reports._2007_01.CrfReports.GenerateReportCriteria, ApplicationId: str) -> Teamcenter.Services.Strong.Reports._2007_01.CrfReports.GenerateReportResponse: ...
    @typing.overload
    def GenerateReport(self, Inputs: list[Teamcenter.Services.Strong.Reports._2010_04.CrfReports.GenerateReportsCriteria2]) -> Teamcenter.Services.Strong.Reports._2015_03.CrfReports.GenerateReportsResponse2: ...
    def GenerateReportDefintionIds(self, InputCriteria: list[Teamcenter.Services.Strong.Reports._2007_01.CrfReports.ReportsCriteria]) -> Teamcenter.Services.Strong.Reports._2007_01.CrfReports.GenerateReportDefintionIdsResponse:
        """    
             Generates new report definition id(s) based upon the specified report criteria. This
             operation is used when user creates new report definition; the report definition
             id is generated by this operation. Multiple report definition id generation is not
             supported currently.
             

Use Cases:

             User creates a new report definition from the New Report wizard. User presses the
             button to generate the report definition id for the new report definition. This operation
             will be triggered to generate the report definition id and assign to the new report
             definition.
             

Teamcenter Component:

             Business Intelligence - Capability to create and manage report definitions and generate
             reports
             
        :param InputCriteria: 
                         A list of ReportsCriteria structures which includes the report category information.
             
        :return: Failure will be returned in the ServiceData.
        """
        ...
    @typing.overload
    def GetReportDefinitions(self, InputCriteria: list[Teamcenter.Services.Strong.Reports._2007_01.CrfReports.ReportsCriteria]) -> Teamcenter.Services.Strong.Reports._2007_01.CrfReports.GetReportDefinitionsResponse: ...
    @typing.overload
    def GetReportDefinitions(self, InputCriteria: list[Teamcenter.Services.Strong.Reports._2008_06.CrfReports.ReportsCriteria2]) -> Teamcenter.Services.Strong.Reports._2007_01.CrfReports.GetReportDefinitionsResponse: ...
    @typing.overload
    def GenerateReports(self, Inputs: list[Teamcenter.Services.Strong.Reports._2008_12.CrfReports.GenerateReportsCriteria]) -> Teamcenter.Services.Strong.Reports._2008_12.CrfReports.GenerateReportsResponse: ...
    @typing.overload
    def GenerateReports(self, Inputs: list[Teamcenter.Services.Strong.Reports._2010_04.CrfReports.GenerateReportsCriteria2]) -> Teamcenter.Services.Strong.Reports._2008_12.CrfReports.GenerateReportsResponse: ...
    def GetPrintTemplates(self, ContextObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Reports._2007_01.CrfReports.GetReportDefinitionsResponse:
        """    
             This operation returns the list of associated ReportDefinition Objects to the current
             selected object.
             

Teamcenter Component:

             Business Intelligence - Capability to create and manage report definitions and generate
             reports
             
        :param ContextObjects: 
                         Selected Object(s)
             
        :return: 3103 No report definitions found for the given business object.
        """
        ...
    def GeneratePrintReports(self, ReportDefObj: Teamcenter.Soa.Client.Model.Strong.ReportDefinition, Inputs: list[Teamcenter.Services.Strong.Reports._2015_03.CrfReports.PrintReportsCriteria]) -> Teamcenter.Services.Strong.Reports._2015_03.CrfReports.GeneratePrintReportsResponse:
        """    
             This operation generates the report based on the selected object and the report definition
             template.
             
             Optionally, it also sends the generated report to the physical printer for printing.
             


Teamcenter Component:

             Business Intelligence - Capability to create and manage report definitions and generate
             reports
             
        :param ReportDefObj: 
                         A report definition template object based on which the print report is to be generated.
             
        :param Inputs: 
                         A list of inputs containing the details of the object and the template, based on
                         which the report is to be generated.
             
        :return: 
        """
        ...
    def GetOfficeStylesheets(self, ReportDefinition: Teamcenter.Soa.Client.Model.Strong.ReportDefinition) -> Teamcenter.Services.Strong.Reports._2015_10.CrfReports.GetOfficeStyleSheetResponse:
        """    
             The operation returns the list of associated Office stylesheets.
             

Teamcenter Component:

             Business Intelligence - Capability to create and manage report definitions and generate
             reports
             
        :param ReportDefinition: 
                         The Report Definition object for which the Office Stylesheets are requested.
             
        :return: The list of Office styleshets attached to the ReportDefinition
        """
        ...

class CubeReportsRestBindingStub(CubeReportsService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ConstructReportURL(self, InputCriteria: Teamcenter.Services.Strong.Reports._2007_06.CubeReports.TcRAReportsCriteria) -> Teamcenter.Services.Strong.Reports._2007_06.CubeReports.ConstructReportURLResponse: ...

class CubeReportsService:
    """
    
            The CubeReports Service provides operation to support for TcRA
reports. Currently
            only one service operation is provided. The operation constructs the
servlet URL
            required by clients to process the TcRA report definition operation
(retrieve, view,
            edit, delete or set permission) specified.

Library Reference:

TcSoaReportsStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> CubeReportsService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ConstructReportURL(self, InputCriteria: Teamcenter.Services.Strong.Reports._2007_06.CubeReports.TcRAReportsCriteria) -> Teamcenter.Services.Strong.Reports._2007_06.CubeReports.ConstructReportURLResponse:
        """    
             Constructs the servlet URL required by clients to process the TcRA report definition
             operation (retrieve, view, edit, delete or set permission) specified. The report
             definition ID, context objects, message name is required to get this URL.
             

Use Cases:

             User retrieves/views/edits/deletes/sets permission for one TcRA report, this operation
             will generate the corresponding URL for the TcRA operation.
             

Teamcenter Component:

             Business Intelligence - Capability to create and manage report definitions and generate
             reports
             
        :param InputCriteria: 
                         A TcRAReportsCriteria structure which includes the report definition ID info, the
                         context objects, the number of the context objects, the message name.
             
        :return: Contains the URL string for the eQube servlet. Failure will be returned in the ServiceData.
        """
        ...

