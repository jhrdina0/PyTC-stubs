import System
import Teamcenter.Services.Strong.Reports._2007_01.CrfReports
import Teamcenter.Soa.Client.Model
import typing

class ReportsCriteria2:
    """
    
Criteria needed to retrieve report definitions. At least one of the optional
parameters
must be included.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client identifier for routing purposes (required)"""
    ReportDefinitionId: str
    """Report definition ID (optional)"""
    ReportDefinitionName: str
    """Report definition name (optional)"""
    Category: str
    """Designates report category, e.g. item, summary or custom (optional)"""
    Source: str
    """Solution source of report definition, e.g. Teamcenter, TcRA (optional)"""
    Status: str
    """For future use, may be null"""
    ContextObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A vector of ID's representing context object(s) (required for item reports)."""

class CrfReports:
    """
    Interface CrfReports
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetReportDefinitions(self, InputCriteria: list[ReportsCriteria2]) -> Teamcenter.Services.Strong.Reports._2007_01.CrfReports.GetReportDefinitionsResponse:
        """    
             Retrieves a set of report definitions that meet the specified criteria.
             

Use Cases:

             Document set of user level use cases, should describe how user interacts with this
             operation to accomplish the goal.
             

Teamcenter Component:

             Business Intelligence - Capability to create and manage report definitions and generate
             reports
             
        :param InputCriteria: 
                         A vector of ReportsCriteria structures
             
        :return: A vector of ReportDefinitionObjects containing report definition ID's.
        """
        ...

