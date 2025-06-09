import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BudgetDataInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    LineObj: Teamcenter.Soa.Client.Model.Strong.BOMLine

class BudgetDataOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    BudgetObjs: list[Teamcenter.Soa.Client.Model.ModelObject]

class BudgetDataResponse:
    def __init__(self, ) -> None: ...
    Output: list[BudgetDataOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class EditBudgetInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    LineObj: Teamcenter.Soa.Client.Model.Strong.BOMLine
    BudgetObj: Teamcenter.Soa.Client.Model.ModelObject
    ExcelTemplateObj: Teamcenter.Soa.Client.Model.Strong.Item

class EditBudgetOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    TransientFileReadTicket: str

class EditBudgetResponse:
    def __init__(self, ) -> None: ...
    Output: list[EditBudgetOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class RemoveBudgetInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    LineObj: Teamcenter.Soa.Client.Model.Strong.BOMLine
    BudgetDefObj: Teamcenter.Soa.Client.Model.ModelObject

class Budget:
    def __init__(self , *args: typing.Any) -> None: ...
    def EditBudget(self, EditBudgetInfo: list[EditBudgetInfo]) -> EditBudgetResponse: ...
    def GetBudgetData(self, InputInfo: list[BudgetDataInfo]) -> BudgetDataResponse: ...
    def RemoveBudget(self, RemoveBudgetInfo: list[RemoveBudgetInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

