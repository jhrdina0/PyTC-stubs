import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class DatasetInfo:
    def __init__(self, ) -> None: ...
    LastModDate: System.DateTime
    FileTickets: list[str]

class GetSharedCommonClientFilesResponse:
    def __init__(self, ) -> None: ...
    DatasetInfoMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetStylesheetPref:
    def __init__(self, ) -> None: ...
    ReturnThumbnailTickets: bool
    StylesheetFormat: str

class GetStylesheetResponse:
    def __init__(self, ) -> None: ...
    Outputs: list[StylesheetOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class StylesheetInputData:
    def __init__(self, ) -> None: ...
    ClientId: str
    BoName: str
    BoReference: Teamcenter.Soa.Client.Model.ModelObject
    StylesheetType: str

class StylesheetOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    XrtStylesheet: str
    HtmlStylesheet: str
    ChildrenMap: System.Collections.Hashtable
    ThumbnailFileTicketMap: System.Collections.Hashtable

class PresentationManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetSharedCommonClientFiles(self, PrefNames: list[str]) -> GetSharedCommonClientFilesResponse: ...
    def GetStylesheet(self, Pref: GetStylesheetPref, InputData: list[StylesheetInputData]) -> GetStylesheetResponse: ...

