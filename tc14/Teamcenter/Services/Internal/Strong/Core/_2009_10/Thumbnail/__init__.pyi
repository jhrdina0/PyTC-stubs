import System
import Teamcenter.Soa.Client.Model
import typing

class SearchOrders:
    def __init__(self, ) -> None: ...
    RelationSearchOrder: list[str]
    DatasetTypeSearchOrder: list[str]

class ThumbnailFileTicketsResponse:
    def __init__(self, ) -> None: ...
    ThumbnailFileTickets: list[str]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class UpdateThumbnailInputs:
    def __init__(self, ) -> None: ...
    IsNone: bool
    IsAutoSelect: bool
    ThumbnailSource: Teamcenter.Soa.Client.Model.ModelObject

class Thumbnail:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetThumbnailFileTickets(self, BusinessObjects: list[Teamcenter.Soa.Client.Model.ModelObject], SearchOrders: SearchOrders) -> ThumbnailFileTicketsResponse: ...
    def UpdateThumbnail(self, BusinessObject: list[Teamcenter.Soa.Client.Model.ModelObject], UpdateThumbnailInputs: list[UpdateThumbnailInputs]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

