import System
import System.Collections
import Teamcenter.Services.Internal.Strong.Core._2009_10.Thumbnail
import Teamcenter.Soa.Client.Model
import typing

class ThumbnailFileTicketsResponse2:
    def __init__(self, ) -> None: ...
    ThumbnailFileTicketsMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Thumbnail:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetThumbnailFileTickets2(self, BusinessObjects: list[Teamcenter.Soa.Client.Model.ModelObject], SearchOrders: Teamcenter.Services.Internal.Strong.Core._2009_10.Thumbnail.SearchOrders) -> ThumbnailFileTicketsResponse2: ...

