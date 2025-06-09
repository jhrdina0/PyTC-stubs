import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class MultisiteDashboardResponse:
    def __init__(self, ) -> None: ...
    DashboardData: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ReportRecipe:
    def __init__(self, ) -> None: ...
    RecipeId: str
    ReportType: str
    Filters: System.Collections.Hashtable

class ImportExportTCXML:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetMultisiteDashBoardData(self, SessionOptions: System.Collections.Hashtable, ReportRecipe: list[ReportRecipe]) -> MultisiteDashboardResponse: ...

