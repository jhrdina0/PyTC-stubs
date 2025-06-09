import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ApplicationConfigExpression:
    def __init__(self, ) -> None: ...
    Formula: str
    ExprID: str
    ExpressionType: int
    ConfigExprSets: list[ConfigExpressionSet]

class ApplConfigExprWithDisplayString:
    def __init__(self, ) -> None: ...
    ApplConfigExpr: ApplicationConfigExpression
    ApplConfigExprDisplayString: str
    ConfigExprSetsInfo: list[ConfigExpressionSetInfo]

class BusinessObjectConfigExpression:
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    Expressions: list[ApplicationConfigExpression]
    ClientId: str

class AvailableProductVariabilityInput:
    def __init__(self, ) -> None: ...
    CriteriaExpression: BusinessObjectConfigExpression
    FamiliesToTest: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamily]
    Context: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective
    ApplyConstraints: int

class AvailableProductVariabilityOutput:
    def __init__(self, ) -> None: ...
    AvailabilityExpressions: list[AvailableVariability]
    Violations: list[Violation]
    SuggestedSatisfyingExpr: ApplicationConfigExpression
    CriteriaStatus: str
    RequiredFamilies: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamily]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class AvailableVariability:
    def __init__(self, ) -> None: ...
    DefaultValues: list[ConfigExpressionTerm]
    Availability: list[ConfigExpressionTerm]

class ConfigExpression:
    def __init__(self, ) -> None: ...
    ClientID: str
    ExpressionType: int
    Formula: str
    SubExpressions: list[ConfigSubExpression]

class ConfigExpressionGroup:
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamily
    GroupName: str
    Terms: list[ConfigExpressionTerm]

class ConfigExpressionSet:
    def __init__(self, ) -> None: ...
    ConfigExpressions: list[ConfigExpression]

class ConfigExpressionSetInfo:
    def __init__(self, ) -> None: ...
    ConfigExprsWithDisplayString: list[ConfigExprWithDisplayString]

class ConfigExpressionTerm:
    def __init__(self, ) -> None: ...
    Family: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamily
    FamilyID: str
    FamilyNamespace: str
    OperatorCode: int
    RangeExpressions: list[RangeExpression]
    Value: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsValue
    ValueText: str
    SelectionClass: str

class ConfigExprWithDisplayString:
    def __init__(self, ) -> None: ...
    ConfigExprDisplayString: str

class ConfigSubExpression:
    def __init__(self, ) -> None: ...
    ExpressionGroups: list[ConfigExpressionGroup]

class ConvertVariantExpressionInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    ExprsToConvert: list[ApplicationConfigExpression]
    Context: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective
    ExpressionFormat: int

class ConvertVariantExpressionOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    ApplConfigExprsWithDisplayString: list[ApplConfigExprWithDisplayString]

class ConvertVariantExpressionsResponse:
    def __init__(self, ) -> None: ...
    Outputs: list[ConvertVariantExpressionOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetProductDefaultsConfigOutput:
    def __init__(self, ) -> None: ...
    ExpressionWithDefaults: BusinessObjectConfigExpression
    CriteriaStatus: str
    RequiredFamilies: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamily]

class GetProductDefaultsResponse:
    def __init__(self, ) -> None: ...
    Outputs: list[GetProductDefaultsConfigOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetRevisionRulesResponse:
    def __init__(self, ) -> None: ...
    ApplicableRevisionRules: list[Teamcenter.Soa.Client.Model.Strong.RevisionRule]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetVariantExpressionsResponse:
    def __init__(self, ) -> None: ...
    ConfigObjectExpressions: list[BusinessObjectConfigExpression]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ProductDefaultsInput:
    def __init__(self, ) -> None: ...
    ApplyDefaults: int
    ExpressionsToUpdate: list[BusinessObjectConfigExpression]
    Families: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamily]
    Context: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective

class RangeExpression:
    def __init__(self, ) -> None: ...
    OperatorCode: int
    ValueText: str
    Feature: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsValue

class SetVariantExpressionInput:
    def __init__(self, ) -> None: ...
    BusinessObjectExpressions: list[BusinessObjectConfigExpression]
    RevisionRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    SaveExpressions: bool

class ValidateProductConfigInput:
    def __init__(self, ) -> None: ...
    ApplyConstraints: int
    ExpressionsToValidate: list[BusinessObjectConfigExpression]
    Context: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective

class ValidateProductConfigOutput:
    def __init__(self, ) -> None: ...
    UpdatedExpression: BusinessObjectConfigExpression
    Violations: list[Violation]
    CriteriaStatus: str
    RequiredFamilies: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamily]

class ValidateProductConfigurationResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    Outputs: list[ValidateProductConfigOutput]

class Violation:
    def __init__(self, ) -> None: ...
    Message: str
    Severity: str
    ViolatedRule: ApplicationConfigExpression
    ConfiguratorWSO: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsConfiguratorWSO

class ConfiguratorManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ConvertVariantExpressions(self, Inputs: list[ConvertVariantExpressionInput]) -> ConvertVariantExpressionsResponse: ...
    def GetAvailableProductVariability(self, Input: AvailableProductVariabilityInput) -> AvailableProductVariabilityOutput: ...
    def GetProductDefaults(self, Inputs: list[ProductDefaultsInput]) -> GetProductDefaultsResponse: ...
    def GetRevRulesForConfiguratorContext(self) -> GetRevisionRulesResponse: ...
    def GetVariantExpressions(self, TargetObjects: list[Teamcenter.Soa.Client.Model.ModelObject], RevisionRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule) -> GetVariantExpressionsResponse: ...
    def SetVariantExpressions(self, Inputs: list[SetVariantExpressionInput], RevisionRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ValidateProductConfiguration(self, Inputs: list[ValidateProductConfigInput]) -> ValidateProductConfigurationResponse: ...

