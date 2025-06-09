import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ProductContextResponse:
    def __init__(self, ) -> None: ...
    ClientIdMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ProductContextSearchInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    SearchObjects: list[Teamcenter.Soa.Client.Model.ModelObject]

class ProductContextSearhData:
    def __init__(self, ) -> None: ...
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    Contents: list[Teamcenter.Soa.Client.Model.Strong.Cpd0DesignElement]

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ProductContextSearch(self, ProductContextSearchInfos: list[ProductContextSearchInfo]) -> ProductContextResponse: ...

