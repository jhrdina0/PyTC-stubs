import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateOrUpdateHierarchyViewsResponse:
    def __init__(self, ) -> None: ...
    HierarchyObjects: list[Teamcenter.Soa.Client.Model.Strong.Cls0HierarchyView]
    Data: Teamcenter.Soa.Client.Model.ServiceData

class HierarchyViewDetails:
    def __init__(self, ) -> None: ...
    HierarchyViewId: str
    HierarchyViewName: str
    HierarchyViewDescription: str
    Scheme: Teamcenter.Soa.Client.Model.Strong.Cls0ClassificationScheme
    ContextObj: Teamcenter.Soa.Client.Model.Strong.Cls0Context

class Classification:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateHierarchyViews(self, HierarchyViewDetails: list[HierarchyViewDetails]) -> CreateOrUpdateHierarchyViewsResponse: ...

