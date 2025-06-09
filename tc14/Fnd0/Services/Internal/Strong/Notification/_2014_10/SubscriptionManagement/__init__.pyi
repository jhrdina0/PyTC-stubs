import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetSubscriptionConditionsResponse:
    def __init__(self, ) -> None: ...
    Conditions: list[Teamcenter.Soa.Client.Model.Strong.Condition]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SubscriptionManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetSubscriptionConditions(self) -> GetSubscriptionConditionsResponse: ...

