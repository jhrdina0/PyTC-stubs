import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class VariantExprXOChartData:
    def __init__(self, ) -> None: ...
    NoOfColHeaders: int
    ColHeaderExprs: list[Teamcenter.Soa.Client.Model.ModelObject]
    NoOfRows: int
    NoOfCols: int
    NoOfTableChars: int
    TableChars: str
    ColHeaderExprStrs: list[str]

class VariantExprAllData:
    def __init__(self, ) -> None: ...
    VarExprXOData: VariantExprXOChartData
    CodeDescData: list[VariantExprCodeDescData]

class GetVariantExprAllDataResponse:
    def __init__(self, ) -> None: ...
    NveData: VariantExprAllData
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class VariantExprCodeDescData:
    def __init__(self, ) -> None: ...
    Nve: Teamcenter.Soa.Client.Model.Strong.NamedVariantExpression
    Code: str
    Desc: str

class VariantManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetVariantExprXOChartData(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.NamedVariantExpression]) -> GetVariantExprAllDataResponse: ...

