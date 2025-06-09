import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetVolumeTargetsInputInfo:
    def __init__(self, ) -> None: ...
    ProductLine: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsProductLine
    ProductModels: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsProductModel]
    RevisionRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule

class GetVolumeTargetsResponse:
    def __init__(self, ) -> None: ...
    VolumeTargets: list[VolumeTarget]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MixRateTarget:
    def __init__(self, ) -> None: ...
    ProductModelLevelTarget: Teamcenter.Soa.Client.Model.Strong.Prg1AbsVolumeTargetElement
    ProductModel: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsProductModel
    DistributionFactor: float
    Goal: float
    TakeRates: list[TakeRateTarget]

class TakeRateTarget:
    def __init__(self, ) -> None: ...
    FeatureLevelTarget: Teamcenter.Soa.Client.Model.Strong.Prg1AbsTakeRateTargtElement
    Feature: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsConfiguratorWSO
    DistributionFactor: float
    Goal: float

class VolumeTarget:
    def __init__(self, ) -> None: ...
    PlanLevelTarget: Teamcenter.Soa.Client.Model.Strong.Prg1AbsVolumeTargetElement
    ProductLine: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsProductLine
    Goal: float
    MixRates: list[MixRateTarget]

class AdvancedProgramManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetVolumeTargets(self, InputInfo: list[GetVolumeTargetsInputInfo]) -> GetVolumeTargetsResponse: ...

