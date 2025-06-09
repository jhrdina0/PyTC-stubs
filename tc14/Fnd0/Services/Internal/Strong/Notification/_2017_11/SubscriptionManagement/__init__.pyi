import System
import Teamcenter.Soa.Client.Model
import typing

class CriteriaPropertyStructure:
    def __init__(self, ) -> None: ...
    SubscribableObjectType: Teamcenter.Soa.Client.Model.ModelObject
    PropInternalNames: list[str]
    PropDisplayNames: list[str]

class GetSubscribablePropertiesResponse:
    def __init__(self, ) -> None: ...
    CriteriaProperties: list[CriteriaPropertyStructure]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SubscriptionManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetSubscribableProperties(self, SubscribableObjectTypes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetSubscribablePropertiesResponse: ...

