import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class GetProductScopeForProcessResponse:
    def __init__(self, ) -> None: ...
    ScopedProductBOMLine: list[System.Collections.Hashtable]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetProductScopeForProcess(self, ProcessLine: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetProductScopeForProcessResponse: ...

