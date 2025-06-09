import Cfg0.Services.Internal.Strong.Configurator._2015_10.ConfiguratorManagement
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AvailabilityInput:
    def __init__(self, ) -> None: ...
    CriteriaExpression: list[Cfg0.Services.Internal.Strong.Configurator._2015_10.ConfiguratorManagement.BusinessObjectConfigExpression]
    FamiliesToTest: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamily]
    ValuesToTest: list[Cfg0.Services.Internal.Strong.Configurator._2015_10.ConfiguratorManagement.ConfigExpressionTerm]
    Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective
    ApplyConstraints: int

class AvailabilityOutput:
    def __init__(self, ) -> None: ...
    AvailabilityStruct: list[AvailableFamilyVariabilityStruct]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class AvailableFamilyVariability:
    def __init__(self, ) -> None: ...
    Availability: list[Cfg0.Services.Internal.Strong.Configurator._2015_10.ConfiguratorManagement.ConfigExpressionTerm]
    AvailibilityStatus: list[str]

class AvailableFamilyVariabilityStruct:
    def __init__(self, ) -> None: ...
    AvailabilityExpressions: list[AvailableFamilyVariability]

class ConfiguratorManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetOptionValueAvailability(self, Input: AvailabilityInput) -> AvailabilityOutput: ...

