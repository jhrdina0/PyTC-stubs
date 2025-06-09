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

class GetAITypesResponse:
    def __init__(self, ) -> None: ...
    AdditionalInfo: AdditionalInfo
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Ai:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetApplicationInterfaceTypes(self, SpecificTypeNames: list[str]) -> GetAITypesResponse: ...

