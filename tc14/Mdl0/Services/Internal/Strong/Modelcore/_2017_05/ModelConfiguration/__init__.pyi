import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CalculatedEffectivityResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    Result: list[CalculatedObjectEffectivityExpr]

class ConfigOption:
    def __init__(self, ) -> None: ...
    Family: Teamcenter.Soa.Client.Model.Strong.ConfigurationFamily
    Name: str
    Description: str

class ConfigFormula:
    def __init__(self, ) -> None: ...
    Formula: str
    ProductName: str
    ProductNameSpace: str

class ConfigExpression:
    def __init__(self, ) -> None: ...
    SubExpressions: list[ConfigExpression]
    OptionValue: ConfigOption
    OpCode: int
    Formula: ConfigFormula
    EffectivityTable: list[EffectivityTableRow]

class CalculatedObjectEffectivityExpr:
    def __init__(self, ) -> None: ...
    ClientId: str
    EffectivityExpression: ConfigExpression
    ConfiguredOutState: str

class EffectivityTableRow:
    def __init__(self, ) -> None: ...
    UnitIn: int
    UnitOut: int
    DateIn: System.DateTime
    DateOut: System.DateTime
    Rest: ConfigFormula

class ModelConfiguration:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetCalculatedEffectivity(self, RevisionRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule, InputObjects: System.Collections.Hashtable, ProductName: str, ProductNamespace: str, ConfiguratorURL: str) -> CalculatedEffectivityResponse: ...

