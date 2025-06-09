import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetCAEPropertyComparisonDetailsResponse:
    def __init__(self, ) -> None: ...
    Result: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class StructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetCAEPropertyComparisonDetails(self, TargetBomline: Teamcenter.Soa.Client.Model.Strong.BOMLine) -> GetCAEPropertyComparisonDetailsResponse: ...

