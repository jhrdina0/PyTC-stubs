import Cfg0.Services.Internal.Strong.Configurator._2015_10.ConfiguratorManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ConfigurationProfile:
    def __init__(self, ) -> None: ...
    IntMap: System.Collections.Hashtable
    BoolMap: System.Collections.Hashtable
    StringMap: System.Collections.Hashtable
    DoubleMap: System.Collections.Hashtable
    ObjectMap: System.Collections.Hashtable
    DateMap: System.Collections.Hashtable

class ConfigurationSessionInfoInput:
    def __init__(self, ) -> None: ...
    Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective
    ConfigProfile: ConfigurationProfile
    TargetObjects: list[Teamcenter.Soa.Client.Model.ModelObject]

class GetContextBasedVariantExprsResponse:
    def __init__(self, ) -> None: ...
    ConfigObjectExpressions: list[Cfg0.Services.Internal.Strong.Configurator._2015_10.ConfiguratorManagement.BusinessObjectConfigExpression]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ConfiguratorManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetContextBasedVariantExpressions(self, TargetObjects: list[Teamcenter.Soa.Client.Model.ModelObject], Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective) -> GetContextBasedVariantExprsResponse: ...
    def SetConfigurationSessionInfo(self, Inputs: list[ConfigurationSessionInfoInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

