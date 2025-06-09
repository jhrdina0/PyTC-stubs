import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AdditionalInfo2:
    def __init__(self, ) -> None: ...
    StrToDateMap: System.Collections.Hashtable
    StrToDoubleMap: System.Collections.Hashtable
    StrToStrMap: System.Collections.Hashtable
    StrToIntMap: System.Collections.Hashtable
    StrToObjMap: System.Collections.Hashtable

class SearchScopedStructureInputInfo:
    def __init__(self, ) -> None: ...
    ProcessScopeForSearch: list[Teamcenter.Soa.Client.Model.Strong.ImanItemBOPLine]
    ObjectType: Teamcenter.Soa.Client.Model.ModelObject
    QueryType: str
    ClosureRuleName: str
    ReturnAssignedObjects: bool
    AdditionalInfo: AdditionalInfo2

class SearchScopedStructureResponse:
    def __init__(self, ) -> None: ...
    QueryOutput: list[Teamcenter.Soa.Client.Model.ModelObject]
    OutOfScopeObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    AssignedObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class StructureSearch:
    def __init__(self , *args: typing.Any) -> None: ...
    def SearchScopedStructure(self, SearchScopedStructureInput: SearchScopedStructureInputInfo) -> SearchScopedStructureResponse: ...

