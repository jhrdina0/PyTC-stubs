import Cfg0.Services.Internal.Strong.Configurator._2014_06.ConfiguratorManagement
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AvailableProductVariabilityInput:
    def __init__(self, ) -> None: ...
    CriteriaExpression: Cfg0.Services.Internal.Strong.Configurator._2014_06.ConfiguratorManagement.BusinessObjectConfigExpression
    FamiliesToTest: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamily]
    Context: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective
    ApplyConstraints: int

class AvailableProductVariabilityOutput:
    def __init__(self, ) -> None: ...
    AvailabilityExpressions: list[AvailableVariability]
    Voilations: list[Cfg0.Services.Internal.Strong.Configurator._2014_06.ConfiguratorManagement.Violation]
    SuggestedSatisfyingExpr: Cfg0.Services.Internal.Strong.Configurator._2014_06.ConfiguratorManagement.ConfigExpression
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class AvailableVariability:
    def __init__(self, ) -> None: ...
    DefaultValue: Cfg0.Services.Internal.Strong.Configurator._2014_06.ConfiguratorManagement.ConfigExpressionTerm
    Availability: list[Cfg0.Services.Internal.Strong.Configurator._2014_06.ConfiguratorManagement.ConfigExpressionTerm]

class ConfiguratorManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAvailableProductVariability(self, Input: AvailableProductVariabilityInput) -> AvailableProductVariabilityOutput: ...

