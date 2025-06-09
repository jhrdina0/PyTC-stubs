import System
import Teamcenter.Soa.Client.Model
import typing

class GetViewableDataResponse:
    def __init__(self, ) -> None: ...
    Output: list[ViewerData]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class TypeToNamedRefPair:
    def __init__(self, ) -> None: ...
    NamedRefType: str
    FileTickets: list[str]

class ViewerData:
    def __init__(self, ) -> None: ...
    InputObj: Teamcenter.Soa.Client.Model.ModelObject
    ViewerID: str
    ViewableObj: Teamcenter.Soa.Client.Model.ModelObject
    Traversal: list[Teamcenter.Soa.Client.Model.ModelObject]
    ViewableNamedRefs: list[TypeToNamedRefPair]

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetViewableData(self, Input: list[Teamcenter.Soa.Client.Model.ModelObject], ConfiguredViewerIDs: list[str], ViewerConfigKey: str) -> GetViewableDataResponse: ...

