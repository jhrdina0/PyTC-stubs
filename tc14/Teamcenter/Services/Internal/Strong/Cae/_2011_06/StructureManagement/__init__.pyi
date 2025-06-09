import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExecuteRuleResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    ActivityLog: str

class StructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteDatamap(self, RootBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine) -> ExecuteRuleResponse: ...

