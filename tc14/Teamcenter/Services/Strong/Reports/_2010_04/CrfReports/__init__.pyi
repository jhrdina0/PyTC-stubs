import System
import Teamcenter.Services.Strong.Reports._2008_12.CrfReports
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GenerateReportsCriteria2:
    """
    The criteria object needed to generate report.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """The client identifier for routing purposes (required)."""
    RdTag: Teamcenter.Soa.Client.Model.Strong.ReportDefinition
    """The Report Definition ID."""
    ReportName: str
    """Designates the name of the report given the rdTag is not supplied."""
    StylesheetTag: Teamcenter.Soa.Client.Model.ModelObject
    """The report style ID (optional)."""
    StylesheetName: str
    """The name of the report style if known"""
    ContextObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of ID's representing context object(s) (required for item reports)."""
    ContextObjectUIDs: list[str]
    """A list of uids representing context objects."""
    DatasetName: str
    """The name of containing DataSet (optional)."""
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
    """The uid for the context Dataset."""
    DatasetCtxObj: Teamcenter.Soa.Client.Model.ModelObject
    """The Dataset context ID."""
    RelationName: str
    """The relation name to be used."""
    DatasetType: str
    """The Dataset type to be used."""
    ReportOptionsNames: list[str]
    """
            A list of strings containing the Names in a series of Name/Value pairs used to specify
            additional criteria (optional).
            """
    ReportOptionsValues: list[str]
    """
            A list of strings containing the Names in a series of Name/Value pairs used to specify
            additional criteria (optional).
            """

class CrfReports:
    """
    Interface CrfReports
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GenerateReports(self, Inputs: list[GenerateReportsCriteria2]) -> Teamcenter.Services.Strong.Reports._2008_12.CrfReports.GenerateReportsResponse:
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
                         The Criteria to generate the report(s) which contains the report definition id, the
                         report style information, the context objects, the query criteria, and the <b>Dataset</b>
                         name, etc.
             
        :return: The GenerateReportsResponse object which contains the ticket for the report created.
             Failure will be returned in the ServiceData.
        """
        ...

