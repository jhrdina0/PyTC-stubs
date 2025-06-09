import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GlobalAlternateList:
    def __init__(self, ) -> None: ...
    GlobalAlternates: list[Teamcenter.Soa.Client.Model.Strong.Item]

class GlobalAlternateListInput:
    def __init__(self, ) -> None: ...
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    GAltItems: list[Teamcenter.Soa.Client.Model.Strong.Item]

class GlobalAlternateResponse:
    def __init__(self, ) -> None: ...
    GlobalAlternateLists: list[GlobalAlternateList]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PreferredGlobalAlternateInput:
    def __init__(self, ) -> None: ...
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    GAltItem: Teamcenter.Soa.Client.Model.Strong.Item

class GlobalAlternate:
    def __init__(self , *args: typing.Any) -> None: ...
    def AddRelatedGlobalAlternates(self, Input: list[GlobalAlternateListInput]) -> GlobalAlternateResponse: ...
    def RemoveRelatedGlobalAlternates(self, Input: list[GlobalAlternateListInput]) -> GlobalAlternateResponse: ...
    def SetPreferredGlobalAlternate(self, Input: list[PreferredGlobalAlternateInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ListGlobalAlternates(self, Items: list[Teamcenter.Soa.Client.Model.Strong.Item]) -> GlobalAlternateResponse: ...

