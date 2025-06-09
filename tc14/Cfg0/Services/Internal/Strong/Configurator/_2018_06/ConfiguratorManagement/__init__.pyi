import Cfg0.Services.Internal.Strong.Configurator._2015_10.ConfiguratorManagement
import Cfg0.Services.Internal.Strong.Configurator._2017_11.ConfiguratorManagement
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CellReference:
    def __init__(self, ) -> None: ...
    ExpressionToValidateClientID: str
    ScopeExpressionClientID: str

class ValidateProductConditionOutptStruct:
    def __init__(self, ) -> None: ...
    CriteriaStatus: str
    Conflicts: list[ViolationList]

class CellValidationResult:
    def __init__(self, ) -> None: ...
    CellClientIDs: CellReference
    VerdictStruct: ValidateProductConditionOutptStruct

class ConfigurationSessionInfoOutput:
    def __init__(self, ) -> None: ...
    SessionConfigObject: Teamcenter.Soa.Client.Model.ModelObject
    Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective
    ConfigProfile: Cfg0.Services.Internal.Strong.Configurator._2017_11.ConfiguratorManagement.ConfigurationProfile

class ExpressionMatrix:
    def __init__(self, ) -> None: ...
    ExpressionsToValidate: list[Cfg0.Services.Internal.Strong.Configurator._2015_10.ConfiguratorManagement.BusinessObjectConfigExpression]
    ScopeExpressions: list[Cfg0.Services.Internal.Strong.Configurator._2015_10.ConfiguratorManagement.BusinessObjectConfigExpression]

class FamilyInfo:
    def __init__(self, ) -> None: ...
    Family: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamily
    Values: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsConfiguratorWSO]

class GetConfigurationSessionInfoResponse:
    def __init__(self, ) -> None: ...
    ConfigSessionInfos: list[ConfigurationSessionInfoOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetVariabilityResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    VariabilityList: list[Variability]

class GroupInfo:
    def __init__(self, ) -> None: ...
    FamilyGroup: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamilyGroup
    Families: list[FamilyInfo]

class MatrixCell:
    def __init__(self, ) -> None: ...
    RowIndex: int
    ColumnIndex: int

class ValidateProductConditionResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    ValidationResults: list[CellValidationResult]

class Variability:
    def __init__(self, ) -> None: ...
    Models: list[FamilyInfo]
    GroupedVariability: list[GroupInfo]
    UngroupedVariability: list[FamilyInfo]

class ViolationList:
    def __init__(self, ) -> None: ...
    StatusCode: int
    StatusMessage: str
    Violations: list[Cfg0.Services.Internal.Strong.Configurator._2015_10.ConfiguratorManagement.Violation]

class ConfiguratorManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetConfigurationSessionInfo(self, SessionConfigObjs: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetConfigurationSessionInfoResponse: ...
    def GetVariability(self, ConfiguratorPerspectives: list[Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective]) -> GetVariabilityResponse: ...
    def ValidateProductConditions(self, SessionConfigObj: Teamcenter.Soa.Client.Model.ModelObject, ExpressionMatrix: ExpressionMatrix, MatrixSubset: list[MatrixCell]) -> ValidateProductConditionResponse: ...

