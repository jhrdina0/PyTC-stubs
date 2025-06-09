import System
import Teamcenter.Soa.Client.Model
import typing

class DatabaseKeysListResponse:
    def __init__(self, ) -> None: ...
    DatabaseKeysSet: list[str]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MeasurementDataQuery:
    def __init__(self , *args: typing.Any) -> None: ...
    def QueryDatabaseKeysList(self) -> DatabaseKeysListResponse: ...

