import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Common
import typing

class AddPoliciesResponse:
    def __init__(self, ) -> None: ...
    PolicyIDs: list[str]
    PartialErrors: Teamcenter.Soa.Client.Model.PartialErrors

class Session:
    def __init__(self , *args: typing.Any) -> None: ...
    def AddObjectPropertyPolicies(self, ClientPolicies: list[Teamcenter.Soa.Common.ObjectPropertyPolicy], NamedPolicies: list[str]) -> AddPoliciesResponse: ...

