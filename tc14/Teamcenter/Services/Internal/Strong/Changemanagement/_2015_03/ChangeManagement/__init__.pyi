import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class AdditionalInfo:
    def __init__(self, ) -> None: ...
    IntMap: System.Collections.Hashtable
    DblMap: System.Collections.Hashtable
    StrMap: System.Collections.Hashtable
    ObjMap: System.Collections.Hashtable
    DateMap: System.Collections.Hashtable

class ConnectChangeNoticeToContextInElem:
    def __init__(self, ) -> None: ...
    ChangeObject: Teamcenter.Soa.Client.Model.ModelObject
    Context: Teamcenter.Soa.Client.Model.ModelObject
    ShareMode: str
    Info: AdditionalInfo

class ConnectChangeNoticeToContextResp:
    def __init__(self, ) -> None: ...
    Info: AdditionalInfo
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class CreateOrUpdatePreviousEffResp:
    def __init__(self, ) -> None: ...
    Info: list[AdditionalInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PreviousEffectivity:
    def __init__(self, ) -> None: ...
    ChangeObject: Teamcenter.Soa.Client.Model.ModelObject
    EndItem: Teamcenter.Soa.Client.Model.ModelObject
    Unit: str
    Date: System.DateTime
    Info: AdditionalInfo

class UpdateChangeNoticeRelationsIn:
    def __init__(self, ) -> None: ...
    SelectedLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    Action: str
    IsRecursive: bool
    AdditionalInfo: AdditionalInfo

class UpdateChangeNoticeRelationsResp:
    def __init__(self, ) -> None: ...
    Info: list[AdditionalInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ChangeManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ConnectChangeNoticeToContext(self, Input: list[ConnectChangeNoticeToContextInElem]) -> ConnectChangeNoticeToContextResp: ...
    def CreateOrUpdatePreviousEffectivity(self, Input: list[PreviousEffectivity]) -> CreateOrUpdatePreviousEffResp: ...
    def DisconnectChangeNoticeFromContext(self, Input: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RemovePrevEffectivityFromChgNotice(self, Input: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UpdateChangeNoticeRelations(self, Inputs: list[UpdateChangeNoticeRelationsIn]) -> UpdateChangeNoticeRelationsResp: ...

