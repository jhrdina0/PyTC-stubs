import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class FetchOdsResults:
    def __init__(self, ) -> None: ...
    SystemLogFiles: list[str]
    FmsTickets: list[str]
    FailedObjects: list[str]
    OdsSessionOutput: System.Collections.Hashtable

class FetchOdsResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    Results: FetchOdsResults

class Search:
    def __init__(self , *args: typing.Any) -> None: ...
    def FetchOdsRecords(self, OdsSiteName: str, SearchMode: int, StartDate: str, EndDate: str, PubrList: list[str], OdsSessionInfo: System.Collections.Hashtable) -> FetchOdsResponse: ...

