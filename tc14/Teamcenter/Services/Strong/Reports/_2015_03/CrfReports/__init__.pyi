import System
import System.Collections
import Teamcenter.Services.Strong.Reports._2007_01.CrfReports
import Teamcenter.Services.Strong.Reports._2008_12.CrfReports
import Teamcenter.Services.Strong.Reports._2010_04.CrfReports
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GeneratePrintReportsOutput:
    """
    A structure that contains information about the generated print reports.
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            The unmodified client id from the input PrintReportsCriteria structure to be used
            to identify the source input data.
            """
    TransientFileReadTickets: list[str]
    """The transient file tickets. This is for future use."""
    TransientFileTicketInfos: list[Teamcenter.Services.Strong.Reports._2008_12.CrfReports.TransientFileTicketInfo]
    """
            The list of TransientFileTicketInfo objects
            for retrieving generated report file. A TransientFileTicketInfo
            object contains the file name, and the transient ticket information for the generated
            report file.
            """

class GeneratePrintReportsResponse:
    """
    
A structure that contains list of print report outputs, and error information,
if
any.
    """
    def __init__(self, ) -> None: ...
    Outputs: list[GeneratePrintReportsOutput]
    """The list of output structure elements."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data including partial errors that are mapped to the client id from the input."""
    ExecutedAsynchronously: bool
    """True value indicates that the operation was executed asynchronously."""

class GenerateReportsCriteria2Async:
    """
    Data needed to generate a report.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """The client identifier for routing purposes."""
    ReportDefinition: Teamcenter.Soa.Client.Model.Strong.ReportDefinition
    """The ReportDefinition object."""
    ReportName: str
    """The name of the report if reportDefinition is null."""
    Stylesheet: Teamcenter.Soa.Client.Model.ModelObject
    """
            The report style sheet. The stylesheet is selectable from a list of already defined
            stylesheets on the ReportDefinition object. It is typically an XSL (saved
            in the DB as a Dataset )(optional).
            """
    StylesheetName: str
    """
            The name of the report style if stylesheet is not supplied. If neither stylesheet
            nor stylesheetName is specified, a raw xml file is generated as report.
            """
    ContextObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of context object(s) (required for item reports)."""
    DatasetName: str
    """
            The name of containing DataSet (optional).If supplied, the generated report
            will be saved as Dataset in Teamcenter,otherwise no dataset created for the
            report.
            """
    CriteriaNames: list[str]
    """
            A list of strings containing the Names in a series of Name/Value pairs used to specify
            criteria for saved queries(optional).
            """
    CriteriaValues: list[str]
    """
            A list of strings containing the Values in a series of Name/Value pairs used to specify
            criteria for saved queries(optional).
            """
    DatasetCtxUID: str
    """The uid for the context Dataset if datasetCtxObj is not supplied."""
    DatasetCtxObj: Teamcenter.Soa.Client.Model.ModelObject
    """The context Dataset where generated report Dataset will be attached to."""
    RelationName: str
    """
            The relation name to be used to attach generated report Dataset to context
            Dataset.
            """
    DatasetType: str
    """The Dataset type to be used to store the report."""
    ReportOptionsNames: list[str]
    """
            A list of option names in a series of Name/Value pairs used to specify additional
            criteria (optional).
            """
    ReportOptionsValues: list[str]
    """
            A list of option values in a series of Name/Value pairs used to specify additional
            criteria (optional).
            """

class GenerateReportsResponse2:
    """
    
Contains file ticket of generated report and synchronize flag as well as service
data.
    """
    def __init__(self, ) -> None: ...
    TransientFileReadTickets: list[str]
    """
            File ticket returned to client to download and the file stored in FMS via this file
            read ticket
            
"""
    TransientFileTicketInfos: list[Teamcenter.Services.Strong.Reports._2008_12.CrfReports.TransientFileTicketInfo]
    """
            A list of TransientFileTicketInfo object(s) for retrieving generated report file.
            The TransientFileTicketInfo object includes the file name, ticket information.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""
    AsyncFlagInfo: bool
    """Asynchronous flag,if true  pop up notification on client will be displayed."""

class PrintReportsCriteria:
    """
    This structure contains the input details for the generation of the print
report.
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    InputObject: Teamcenter.Soa.Client.Model.ModelObject
    """The input object for which the print report is to be generated."""
    IsBatchPrint: bool
    """True value indicates to also send the report to physical printer for printing."""
    PrintInfos: list[PrintSubmitRequestInfo]
    """
            The list of structures containing print configuration info. This info will be used
            only when the isBatchPrint is set to true.
            """

class PrintReportsCriteriaAsync:
    """
    This structure contains the input details for the generation of the print
report.
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    InputObject: Teamcenter.Soa.Client.Model.ModelObject
    """The input object for which the print report is to be generated."""
    IsBatchPrint: bool
    """True value indicates to also send the generated report to physical printer for printing."""
    PrintInfos: list[PrintSubmitRequestInfo]
    """
            The list of structures containing print configuration info. This info will be used
            only when the isBatchPrint is set to true.
            """

class PrintSubmitRequestInfo:
    """
    The structure containing the info needed to submit the print request.
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    PrintObjs: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of Teamcenter business objects (ItemRevision, Item, Dataset)
            that will be printed.
            """
    PrinterConfigurationName: str
    """The PrintConfiguration object name."""
    PrinterName: str
    """The printer name."""
    ColorMode: str
    """The print color mode. The possible values are "Color" or "Monochrome"."""
    UserStamp: str
    """Text for a user stamp to be applied in addition to any existing system stamp configuration."""
    PaperSize: str
    """The print paper size. The sample values are "Legal", "Letter", "11x17" etc."""
    PrintStamp: str
    """Where the print stamp is applied: "first page", "the banner page", or "all pages"."""
    PageRange: str
    """The range of pages to print. Empty value indicates to print all pages."""
    NumberCopies: str
    """The number of copies."""
    Collate: bool
    """
            When two or more copies are printed, this specifies whether the printed pages are
            collated.
            """
    PrintToScale: str
    """
            The scaling factor. Specifies the scaling factor from 0.000001 to 100.0, applied
            to an image when its printed.
            """
    Orientation: str
    """The paper orientation of "best fit", "portrait" or "landscape"."""
    BannerPage: str
    """
            Specifies whether to print a page including the defined stamps and listing additional
            data as specified by the VVCP setup(i.e. the Lifecycle Visualization print configuration)
            The following values can be specified: "Off", "Single", or "All Files".
            """
    ExtraInfo: System.Collections.Hashtable
    """The placeholder for extra name value pair (string, string) information."""

class CrfReports:
    """
    Interface CrfReports
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GenerateReport(self, Inputs: list[Teamcenter.Services.Strong.Reports._2010_04.CrfReports.GenerateReportsCriteria2]) -> GenerateReportsResponse2:
        """    
             Generates reports (Summary Report/Custom Report/Item Report) using the specified
             criteria and the selected report style. The report will be displayed by the selected
             report style at the end. If no report style is selected, then the report will be
             displayed in xml file to the end user. If user would like to save the report as a
             Dataset, it will use the provided Dataset name to save the report to Teamcenter.
             After the report is generated, the report file will be uploaded to the transient
             volumes, user can get it from the transient volumes. Multiple reports generation
             is not supported currently.
             

Use Cases:

             User can generate one report (Summary Report/Custom Report/Item Report) by selecting
             one report definition and then inputs criteria for the report query, selects one
             report style, and inputs the Dataset name for the report if user would like to save
             the report as a Dataset in Teamcenter.
             

Teamcenter Component:

             Business Intelligence - Capability to create and manage report definitions and generate
             reports
             
        :param Inputs: 
                         The Criteria to generate the report(s) which contains the report definition id, the
                         report style information, the context objects, the query criteria, and the Dataset
                         name, etc.
             
        :return: 3083 : Report definition tag provided as input is invalid.
        """
        ...
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
    def GeneratePrintReports(self, ReportDefObj: Teamcenter.Soa.Client.Model.Strong.ReportDefinition, Inputs: list[PrintReportsCriteria]) -> GeneratePrintReportsResponse:
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

