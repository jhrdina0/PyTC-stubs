import System
import Teamcenter.Services.Internal.Strong.Cadbomalignment._2013_05.QueryManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class Column:
    def __init__(self, ) -> None: ...
    Name: str
    Datatype: str
    Table: str
    LogicalName: str
    Width: int

class ColumnSet:
    def __init__(self, ) -> None: ...
    Column: list[Column]
    Table: str

class MultilevelACTBreakdownResponse:
    def __init__(self, ) -> None: ...
    ActWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class RowSet:
    def __init__(self, ) -> None: ...
    Row: list[Row]

class RowColumn:
    def __init__(self, ) -> None: ...
    ColumnSet: ColumnSet
    RowSet: RowSet

class PMMComponentInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    RowColumn: RowColumn

class PMMProxyObjectInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    Proxies: list[Teamcenter.Soa.Client.Model.Strong.Cba0PersistentProxy]

class PMMProxyObjectResponse:
    def __init__(self, ) -> None: ...
    Output: list[PMMProxyObjectInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Row:
    def __init__(self, ) -> None: ...
    Value: list[str]

class QueryManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPMMProxyObjectFromPMMComponent(self, Input: list[PMMComponentInfo]) -> PMMProxyObjectResponse: ...
    def PerformMultilevelACTBreakdown(self, InputBreakDownCriteria: Teamcenter.Services.Internal.Strong.Cadbomalignment._2013_05.QueryManagement.BreakDownCriteria) -> MultilevelACTBreakdownResponse: ...

