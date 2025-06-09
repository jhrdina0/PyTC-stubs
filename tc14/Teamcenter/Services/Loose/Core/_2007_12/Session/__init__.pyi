import System
import Teamcenter.Soa.Client.Model
import typing

class StateNameValue:
    def __init__(self, ) -> None: ...
    Name: str
    Value: str

class Session:
    def __init__(self , *args: typing.Any) -> None: ...
    def SetUserSessionState(self, Pairs: list[StateNameValue]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetAndEvaluateIdDisplayRule(self, IdentifiableObjects: list[Teamcenter.Soa.Client.Model.ModelObject], DisplayRule: Teamcenter.Soa.Client.Model.ModelObject, SetRuleAsCurrentInDB: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

