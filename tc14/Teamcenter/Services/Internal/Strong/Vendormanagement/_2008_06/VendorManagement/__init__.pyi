import Teamcenter.Soa.Client.Model
import typing

class ConditionData:
    def __init__(self, ) -> None: ...
    CondName: str
    CondExpress: str

class GetVPSRConditionsResponse:
    def __init__(self, ) -> None: ...
    CondData: list[ConditionData]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class VendorManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetVPSRConditions(self) -> GetVPSRConditionsResponse: ...

