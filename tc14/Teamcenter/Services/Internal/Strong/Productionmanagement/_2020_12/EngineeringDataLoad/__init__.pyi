import System
import Teamcenter.Services.Internal.Strong.Productionmanagement._2020_01.EngineeringDataLoad
import Teamcenter.Soa.Client.Model
import typing

class CommitFeatData:
    def __init__(self, ) -> None: ...
    CommitFeatureLabel: str
    CommitFeatureID: str
    IsCommitted: bool
    Message: str

class ExcelFeatData:
    def __init__(self, ) -> None: ...
    ExcelFeatureName: str
    ExcelFeatureID: str

class UpdateEngineeringWorkbookResponse:
    def __init__(self, ) -> None: ...
    CommittedFeatures: list[CommitFeatData]
    ExcelFeatures: list[ExcelFeatData]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class EngineeringDataLoad:
    def __init__(self , *args: typing.Any) -> None: ...
    def UpdateEngineeringWorkbook(self, RoutineID: str, RoutineRev: str, FeatureRows: list[Teamcenter.Services.Internal.Strong.Productionmanagement._2020_01.EngineeringDataLoad.Features]) -> UpdateEngineeringWorkbookResponse: ...

