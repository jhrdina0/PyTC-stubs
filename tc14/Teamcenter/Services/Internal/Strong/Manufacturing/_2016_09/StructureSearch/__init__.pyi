import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class SearchBOEInputInfo:
    def __init__(self, ) -> None: ...
    InputScopes: list[Teamcenter.Soa.Client.Model.ModelObject]
    SearchCriteria: System.Collections.Hashtable

class SearchBOEResponse:
    def __init__(self, ) -> None: ...
    ResultObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class StructureSearch:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetBOEForPlantBOPScope(self, SearchInput: SearchBOEInputInfo) -> SearchBOEResponse: ...

