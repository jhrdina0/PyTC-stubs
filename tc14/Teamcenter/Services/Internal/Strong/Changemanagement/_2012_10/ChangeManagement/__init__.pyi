import System
import Teamcenter.Soa.Client.Model
import typing

class ChangeTypeInfo:
    def __init__(self, ) -> None: ...
    TypeName: str
    TypeDisplayName: str

class ContextDataInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Object: str
    BaseTypeName: str
    ExclusionTypeNames: list[str]

class CreatableChangeTypesOut:
    def __init__(self, ) -> None: ...
    ClientId: str
    AllowedChangeTypes: list[ChangeTypeInfo]

class CreatableChangeTypesResponse:
    def __init__(self, ) -> None: ...
    Output: list[CreatableChangeTypesOut]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ChangeManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetCreatableChangeTypes(self, Inputs: list[ContextDataInput]) -> CreatableChangeTypesResponse: ...

