import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateRollupCalculationInputArgument:
    def __init__(self, ) -> None: ...
    Name: str
    Input: str
    Output: str

class CreateRollupCalculationTemplateInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Type: str
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    Arguments: list[CreateRollupCalculationInputArgument]

class CreateRollupCalculationTemplateOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Type: str
    CalcTemplate: Teamcenter.Soa.Client.Model.ModelObject

class CreateRollupCalculationTemplateResponse:
    def __init__(self, ) -> None: ...
    Output: list[CreateRollupCalculationTemplateOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class CreateRollupReportInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Name: str
    Description: str
    Bomline: Teamcenter.Soa.Client.Model.Strong.BOMLine
    Folder: Teamcenter.Soa.Client.Model.Strong.Folder
    RollupTemplate: Teamcenter.Soa.Client.Model.ModelObject

class CreateRollupTemplateInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Name: str
    Desc: str
    Delimiter: str
    ScopeContext: str
    Scope: str

class GetRollupTemplateInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Mode: str

class ReviseRollupReportInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Bomline: Teamcenter.Soa.Client.Model.Strong.BOMLine
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    RollupTemplate: Teamcenter.Soa.Client.Model.ModelObject

class RollupReportOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset

class RollupReportResponse:
    def __init__(self, ) -> None: ...
    Output: list[RollupReportOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class RollupTemplateCalculation:
    def __init__(self, ) -> None: ...
    Type: str
    CalcTemplates: list[Teamcenter.Soa.Client.Model.ModelObject]

class RollupTemplateCalculationOutput:
    def __init__(self, ) -> None: ...
    RollupTemplate: Teamcenter.Soa.Client.Model.ModelObject
    RollupCalcTemplates: list[RollupTemplateCalculation]

class RollupTemplateCalculationResponse:
    def __init__(self, ) -> None: ...
    Output: list[RollupTemplateCalculationOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class RollupTemplateInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    RollupTemplate: Teamcenter.Soa.Client.Model.ModelObject

class RollupTemplateOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    RollupTemplates: list[Teamcenter.Soa.Client.Model.ModelObject]

class RollupTemplateResponse:
    def __init__(self, ) -> None: ...
    Output: list[RollupTemplateOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class BOMRollup:
    def __init__(self , *args: typing.Any) -> None: ...
    def CloneRollupTemplates(self, Input: list[RollupTemplateInput]) -> RollupTemplateResponse: ...
    def CreateRollupCalculationTemplates(self, Input: list[CreateRollupCalculationTemplateInput]) -> CreateRollupCalculationTemplateResponse: ...
    def CreateRollupTemplates(self, Input: list[CreateRollupTemplateInput]) -> RollupTemplateResponse: ...
    def GenerateRollupReports(self, Input: list[CreateRollupReportInput]) -> RollupReportResponse: ...
    def GetRollupTemplateCalculations(self, Input: list[RollupTemplateInput]) -> RollupTemplateCalculationResponse: ...
    def GetRollupTemplates(self, Input: list[GetRollupTemplateInput]) -> RollupTemplateResponse: ...
    def ReviseRollupReports(self, Input: list[ReviseRollupReportInput]) -> RollupReportResponse: ...

