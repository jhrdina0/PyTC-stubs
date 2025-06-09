import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class GetStylesheetPerPagePref:
    def __init__(self, ) -> None: ...
    ReturnThumbnailTickets: bool
    StylesheetFormat: str
    ProcessEntireXRT: bool

class GetStylesheetPerPageResponse:
    def __init__(self, ) -> None: ...
    Outputs: list[StylesheetPerPageOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class StylesheetPerPageInputData:
    def __init__(self, ) -> None: ...
    ClientId: str
    BoName: str
    BoReference: Teamcenter.Soa.Client.Model.ModelObject
    StylesheetType: str
    TargetPage: str

class StylesheetPerPageOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    XrtStylesheet: str
    HtmlStylesheet: str
    ChildrenMap: System.Collections.Hashtable
    ThumbnailFileTicketMap: System.Collections.Hashtable
    ProcessedPage: str
    VisiblePages: list[str]

class PresentationManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetStylesheetPerPage(self, Pref: GetStylesheetPerPagePref, InputData: list[StylesheetPerPageInputData]) -> GetStylesheetPerPageResponse: ...

