import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CADOccPublishInfo:
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    ClientId: str

class ItemRevPublishInfo:
    def __init__(self, ) -> None: ...
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    ClientId: str

class PublishManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def PublishCadOccurrences(self, PublishInfo: list[CADOccPublishInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def PublishItems(self, PublishInfo: list[ItemRevPublishInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

