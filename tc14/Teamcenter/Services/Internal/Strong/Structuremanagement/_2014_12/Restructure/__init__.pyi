import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ReplaceItemsParameter:
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    ViewType: Teamcenter.Soa.Client.Model.Strong.PSViewType
    ReplaceOption: int

class Restructure:
    def __init__(self , *args: typing.Any) -> None: ...
    def ReplaceItems(self, ReplaceInputs: list[ReplaceItemsParameter]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

