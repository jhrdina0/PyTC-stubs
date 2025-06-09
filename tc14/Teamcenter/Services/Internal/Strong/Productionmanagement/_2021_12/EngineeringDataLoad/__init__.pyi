import System
import Teamcenter.Services.Internal.Strong.Productionmanagement._2020_01.EngineeringDataLoad
import Teamcenter.Services.Internal.Strong.Productionmanagement._2020_12.EngineeringDataLoad
import Teamcenter.Soa.Client.Model
import typing

class GetFNPFieldsSheetInfoResponse:
    def __init__(self, ) -> None: ...
    PFeatureLabelData: list[SheetColumn]
    MFeatureParamData: list[SheetColumn]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SheetColumn:
    def __init__(self, ) -> None: ...
    ColValue: list[str]

class SheetRow:
    def __init__(self, ) -> None: ...
    RowValue: list[str]

class EngineeringDataLoad:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetFNPFieldsSheetInfo(self, RoutineID: str, RoutineRev: str) -> GetFNPFieldsSheetInfoResponse: ...
    def UpdateEngineeringWorkbook2(self, RoutineID: str, RoutineRev: str, FeatureRows: list[Teamcenter.Services.Internal.Strong.Productionmanagement._2020_01.EngineeringDataLoad.Features], FeatureParamSheetData: list[SheetRow]) -> Teamcenter.Services.Internal.Strong.Productionmanagement._2020_12.EngineeringDataLoad.UpdateEngineeringWorkbookResponse: ...

