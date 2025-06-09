import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GenerateReportsCriteria:
    """
    
Criteria needed to retrieve report definitions or generate report definition
ids.
At least one of the optional parameters must be included.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """The client identifier for routing purposes."""
    RdTag: Teamcenter.Soa.Client.Model.Strong.ReportDefinition
    """The Report Definition ID."""
    ReportName: str
    """Designates the name of the report given the report definition is not supplied."""
    StylesheetTag: Teamcenter.Soa.Client.Model.ModelObject
    """
            The report style sheet ID (optional). If no report style is provided, then the report
            will be displayed in xml format to the end user.
            """
    StylesheetName: str
    """The name of the stylesheet if known"""
    ContextObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of ID's representing context object(s) (required for item reports)."""
    ContextObjectUIDs: list[str]
    """A list of UIDs representing context objects."""
    DatasetName: str
    """
            The name of containing Dataset (optional). If the dataset name is provided,
            then it will save the generated report as a Dataset in Teamcenter database,
            otherwise will not.
            """
    CriteriaNames: list[str]
    """The names in a series of Name/Value pairs used to specify additional criteria (optional)."""
    CriteriaValues: list[str]
    """The values in a series of Name/Value pairs used to specify additional criteria (optional)."""
    DatasetCtxUID: str
    """The uid for the context Dataset UID."""
    DatasetCtxObj: Teamcenter.Soa.Client.Model.ModelObject
    """The Dataset context id."""
    RelationName: str
    """The relation name to be used."""
    DatasetType: str
    """The Dataset type to be used."""

class GenerateReportsResponse:
    """
    The Response object from generateReports operation.
    """
    def __init__(self, ) -> None: ...
    TransientFileReadTickets: list[str]
    """It is for future use, may be null."""
    TransientFileTicketInfos: list[TransientFileTicketInfo]
    """
            A list of TransientFileTicketInfo object(s) for retrieving generated report file.
            The TransientFileTicketInfo object includes the file name, ticket information.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData which includes the failure information."""

class TransientFileInfo:
    """
    The information required for file upload.
    """
    def __init__(self, ) -> None: ...
    FileName: str
    """Absolute file path to transient volume"""
    IsText: bool
    """true if filetype is text"""

class TransientFileTicketInfo:
    """
    TransientFileInfo with a ticket.
    """
    def __init__(self, ) -> None: ...
    TransientFileInfo: TransientFileInfo
    """file information structure"""
    Ticket: str
    """FMS file ticket"""

class CrfReports:
    """
    Interface CrfReports
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GenerateReports(self, Inputs: list[GenerateReportsCriteria]) -> GenerateReportsResponse:
        """    
             Generates reports (Summary Report/Custom Report/Item Report) using the specified
             criteria and the selected report style. The report will be displayed by the selected
             report style at the end. If no report style is selected, then the report will be
             displayed in xml file to the end user. If user would like to save the report as a
             Dataset, it will use the provided Dataset name to save the report to
             Teamcenter. After the report is generated, the report file will be uploaded to the
             transient volumes, user can get it from the transient volumes. Multiple reports generation
             is not supported currently.
             

Use Cases:

             User can generate one report (Summary Report/Custom Report/Item Report) by selecting
             one report definition and then inputs criteria for the report query, selects one
             report style, and inputs the Dataset name for the report if user would like
             to save the report as a Dataset in Teamcenter.
             

Teamcenter Component:

             Business Intelligence - Capability to create and manage report definitions and generate
             reports
             
        :param Inputs: 
                         A GenerateReportCriteria structure which contains the report definition id, the report
                         style information, the context objects, the query criteria, and the dataset name.
             
        :return: The GenerateReportsResponse object which contains the ticket for the report created.
             Failure will be returned in the ServiceData.
        """
        ...

