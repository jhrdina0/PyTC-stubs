import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CompAndParentVariabilityInfo:
    def __init__(self, ) -> None: ...
    CompVarInfo: list[VariabilityInfo]
    ParentVarInfo: list[VariabilityInfo]

class GetVariabilityInfoResponse:
    def __init__(self, ) -> None: ...
    CompAndParentVarInfo: list[CompAndParentVariabilityInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class VariabilityInfo:
    def __init__(self, ) -> None: ...
    VariabilityObj: Teamcenter.Soa.Client.Model.ModelObject
    VariantObj: Teamcenter.Soa.Client.Model.Strong.Variant
    Comment: str

class VariantManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetVariabilityInfo(self, Inputs: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetVariabilityInfoResponse: ...

