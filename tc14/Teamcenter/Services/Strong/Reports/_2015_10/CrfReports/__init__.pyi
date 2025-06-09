import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetOfficeStyleSheetResponse:
    """
    The list of Office template stylesheets attached to the ReportDefinition.
    """
    def __init__(self, ) -> None: ...
    Officetemplates: list[str]
    """
            The names of the office template stylesheets attached to the ReportDefinition object
            via the GRM relationship.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The standard ServiceData"""

class CrfReports:
    """
    Interface CrfReports
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetOfficeStylesheets(self, ReportDefinition: Teamcenter.Soa.Client.Model.Strong.ReportDefinition) -> GetOfficeStyleSheetResponse:
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

