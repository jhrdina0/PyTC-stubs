import System
import Teamcenter.Soa.Client.Model
import typing

class SearchDynamicIPAsOutput:
    def __init__(self, ) -> None: ...
    BopLine: Teamcenter.Soa.Client.Model.ModelObject
    DipaLines: list[Teamcenter.Soa.Client.Model.ModelObject]

class SearchDynamicIPAsResponse:
    def __init__(self, ) -> None: ...
    Output: list[SearchDynamicIPAsOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class IPAManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def SearchDynamicIPAs(self, SearchScopes: list[Teamcenter.Soa.Client.Model.ModelObject], ReturnOnFirstResult: bool) -> SearchDynamicIPAsResponse: ...

