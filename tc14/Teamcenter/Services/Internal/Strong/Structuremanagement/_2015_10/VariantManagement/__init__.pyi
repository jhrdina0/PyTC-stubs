import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class VariantConfigurationCriteria:
    def __init__(self, ) -> None: ...
    VariantConfiguratorFormula: str
    SavedVariantRules: list[Teamcenter.Soa.Client.Model.ModelObject]

class VariantManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ApplyVariantConfiguration(self, Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow, VariantConfigurationCriteria: VariantConfigurationCriteria) -> Teamcenter.Soa.Client.Model.ServiceData: ...

