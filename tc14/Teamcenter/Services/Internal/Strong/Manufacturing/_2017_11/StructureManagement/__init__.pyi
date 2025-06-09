import System
import System.Collections
import Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement
import Teamcenter.Soa.Client.Model
import typing

class AlternativeScopeForProductInputInfo:
    def __init__(self, ) -> None: ...
    ProductNode: Teamcenter.Soa.Client.Model.ModelObject
    NewAlternativeScpName: str
    NewAlternativeScpDesc: str
    ContainerInfo: System.Collections.Hashtable

class AlternativeScopeForProductResponse:
    def __init__(self, ) -> None: ...
    ProductNodeAlternativeScp: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PasteByRuleInfo:
    def __init__(self, ) -> None: ...
    SourceLine: Teamcenter.Soa.Client.Model.ModelObject
    TargetLine: Teamcenter.Soa.Client.Model.ModelObject
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class PasteByRuleInfoInput:
    def __init__(self, ) -> None: ...
    SourceTargetLineInfo: list[PasteByRuleInfo]
    TargetLine: Teamcenter.Soa.Client.Model.ModelObject
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class PasteByRuleResponse:
    def __init__(self, ) -> None: ...
    CreatedLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class StructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateAlternativeScopeForProduct(self, AltenativeScpForProdInfo: list[AlternativeScopeForProductInputInfo]) -> AlternativeScopeForProductResponse: ...
    def PasteByRule(self, InputInfo: PasteByRuleInfoInput) -> PasteByRuleResponse: ...

