import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class GetDatabaseKeysForPlantsResponse:
    def __init__(self, ) -> None: ...
    PlantDatabaseInfo: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MeasurementDatabaseDetailsResponse:
    def __init__(self, ) -> None: ...
    MeasurementDatabaseSet: list[MeasurementDatabaseInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MeasurementDatabaseInfo:
    def __init__(self, ) -> None: ...
    DatabaseKey: str
    DatabaseName: str
    DatabaseType: str
    HostName: str
    DatabaseUsername: str

class MeasurementDataQuery:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDatabaseKeysForPlants(self, Plantids: list[str]) -> GetDatabaseKeysForPlantsResponse: ...
    def GetMeasurementDatabaseDetails(self) -> MeasurementDatabaseDetailsResponse: ...

