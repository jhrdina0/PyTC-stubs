import Teamcenter.Soa.Client.Model
import typing

class ItemIDData:
    def __init__(self, ) -> None: ...
    ClientId: str
    ItemID: str
    ExistingObject: Teamcenter.Soa.Client.Model.ModelObject

class ItemIDInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    ExternalObjectID: str
    ContextID: str

class ItemIDResponse:
    def __init__(self, ) -> None: ...
    ItemData: list[ItemIDData]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class LineItemPropsWithType:
    def __init__(self, ) -> None: ...
    Name: str
    Description: str
    Liccname: str
    Liccdesc: str
    Partid: str
    Viewtype: str
    Quantity: int
    RevRule: str
    VarRule: str
    ClosureRule: str
    Quote: Teamcenter.Soa.Client.Model.ModelObject
    BpliTypeName: str

class VendorManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateLineItems(self, Properties: list[LineItemPropsWithType], BidPackage: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetItemIDwithContext(self, Input: list[ItemIDInput]) -> ItemIDResponse: ...

