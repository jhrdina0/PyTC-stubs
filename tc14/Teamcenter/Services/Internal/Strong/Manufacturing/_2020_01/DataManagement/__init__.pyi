import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class AdditionalInfo:
    def __init__(self, ) -> None: ...
    StrToDateMap: System.Collections.Hashtable
    StrToDoubleMap: System.Collections.Hashtable
    StrToStrMap: System.Collections.Hashtable
    StrToIntMap: System.Collections.Hashtable
    StrToObjVectorMap: System.Collections.Hashtable

class AssociateOrRemoveScopeInput:
    def __init__(self, ) -> None: ...
    ProcessLine: Teamcenter.Soa.Client.Model.ModelObject
    AddScopeLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    RemoveScopeLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    AdditionalInfo: AdditionalInfo

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def AssociateOrRemoveScopesForProcess(self, AssociateOrRemoveInput: list[AssociateOrRemoveScopeInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

