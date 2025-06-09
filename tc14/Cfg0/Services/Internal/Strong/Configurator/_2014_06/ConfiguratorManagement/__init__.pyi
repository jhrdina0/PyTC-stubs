import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BusinessObjectConfigExpression:
    def __init__(self, ) -> None: ...
    ClientId: str
    TargetObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    Expressions: list[ConfigExpression]

class ConfigExpression:
    def __init__(self, ) -> None: ...
    ClientId: str
    ExpressionType: int
    Formula: str
    SubExpressions: list[ConfigSubExpression]

class ConfigExpressionDisplayStringInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Expressions: list[ConfigExpression]

class ConfigExpressionDisplayStringOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    ExpressionStrings: list[str]

class ConfigExpressionGroup:
    def __init__(self, ) -> None: ...
    GroupName: str
    Terms: list[ConfigExpressionTerm]

class ConfigExpressionTerm:
    def __init__(self, ) -> None: ...
    FamilyNamespace: str
    FamilyID: str
    OperatorCode: int
    ValueText: str
    RangeExpressions: list[RangeExpression]
    Family: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamily
    Value: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsValue

class ConfigSubExpression:
    def __init__(self, ) -> None: ...
    ExpressionGroups: list[ConfigExpressionGroup]

class Expression:
    def __init__(self, ) -> None: ...
    Id: int
    AsTextExpression: list[str]

class ConfiguratorConstraint:
    def __init__(self, ) -> None: ...
    ModelDesignator: Expression
    Applicability: Expression
    Restriction: Expression
    Comment: str
    ModelOptions: list[VariantOption]
    ApplicabilityOptions: list[VariantOption]
    RestrictionOptions: list[VariantOption]
    RuleOptions: list[VariantOption]
    ConstraintType: str
    ConstraintSeverity: str

class CreateInput:
    def __init__(self, ) -> None: ...
    BoName: str
    StringProps: System.Collections.Hashtable
    StringArrayProps: System.Collections.Hashtable
    BoolProps: System.Collections.Hashtable
    BoolArrayProps: System.Collections.Hashtable
    DateProps: System.Collections.Hashtable
    DateArrayProps: System.Collections.Hashtable
    IntProps: System.Collections.Hashtable
    IntArrayProps: System.Collections.Hashtable
    DoubleProps: System.Collections.Hashtable
    DoubleArrayProps: System.Collections.Hashtable
    FloatProps: System.Collections.Hashtable
    FloatArrayProps: System.Collections.Hashtable
    ObjectProps: System.Collections.Hashtable
    ObjectArrayProps: System.Collections.Hashtable
    CompoundCreateInput: System.Collections.Hashtable

class CreateUpdateVariantRulesResponse:
    def __init__(self, ) -> None: ...
    RuleOutputs: list[VariantRuleOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class VariantOption:
    def __init__(self, ) -> None: ...
    OptionNamespace: str
    Name: str
    Description: str
    Tag: str
    ValueDataType: str
    Uom: str

class DeclaredFamily:
    def __init__(self, ) -> None: ...
    Family: VariantOption
    ValueRange: Expression
    Values: System.Collections.Hashtable
    VariantMode: int

class ExpressionGroupInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    SearchOperator: str
    ExpressionIds: list[str]
    Settings: System.Collections.Hashtable

class ExpressionJoinCondition:
    def __init__(self, ) -> None: ...
    Left: int
    OperatorCode: int
    Right: int

class ExpressionJoinInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    SearchOperator: str
    ExpressionIds: list[str]
    Settings: System.Collections.Hashtable
    JoinConditions: list[ExpressionJoinCondition]

class FamilyFilters:
    def __init__(self, ) -> None: ...
    FamilyIDs: list[str]
    Families: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsOptionFamily]

class GroupFilters:
    def __init__(self, ) -> None: ...
    GroupIDs: list[str]
    Groups: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamilyGroup]

class ValueFilters:
    def __init__(self, ) -> None: ...
    ValueIDs: list[str]
    Values: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsOptionValue]

class FilterCriteria:
    def __init__(self, ) -> None: ...
    GroupFilters: GroupFilters
    FamilyFilters: FamilyFilters
    ValueFilters: ValueFilters
    IncludeUnreferencedRules: bool

class GetDisplayStringResponse:
    def __init__(self, ) -> None: ...
    DisplayStrings: list[ConfigExpressionDisplayStringOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetFamilyGroupResponse:
    def __init__(self, ) -> None: ...
    GroupAndAllocation: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetOptionFamiliesResponse:
    def __init__(self, ) -> None: ...
    GroupAndFamilies: list[GroupAndFamilies]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetOptionValuesResponse:
    def __init__(self, ) -> None: ...
    ValueAndAssocations: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetProductDefaultsResponse:
    def __init__(self, ) -> None: ...
    ExpressionsWithDefaults: list[BusinessObjectConfigExpression]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class VariantInfo:
    def __init__(self, ) -> None: ...
    LastUpdate: System.DateTime
    VariantOption: list[VariantOption]
    ValidValueRanges: list[Expression]
    DefaultConditions: list[Expression]
    DefaultExpressions: list[Expression]
    RuleChecks: list[ConfiguratorConstraint]
    FamilyHash: System.Collections.Hashtable
    FamilyNameHash: System.Collections.Hashtable
    RuleCheckExpressions: Expression

class GetVariantCacheInfoResponse:
    def __init__(self, ) -> None: ...
    VariantInfo: VariantInfo
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GroupAndFamilies:
    def __init__(self, ) -> None: ...
    FamilyGroup: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamilyGroup
    FamilyAndAssociation: System.Collections.Hashtable

class ObjectReferenceInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Objects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    ResultColumns: list[SearchResultTableColumn]

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

class ResultTypeInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    SearchResultObjectTypes: list[str]
    ResultColumns: list[SearchResultTableColumn]
    PredicateClauseParameters: list[SearchPredicateParameters]

class SavedQueryExpressionInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Entries: list[str]
    Values: list[str]
    SavedQuery: Teamcenter.Soa.Client.Model.Strong.ImanQuery
    ResultColumns: list[SearchResultTableColumn]

class SearchExpressionInput:
    def __init__(self, ) -> None: ...
    Traversals: list[TraversalExpressionInput]
    ExcludeObjects: list[ObjectReferenceInput]
    IncludeObjects: list[ObjectReferenceInput]
    SavedQueries: list[SavedQueryExpressionInput]
    ExpressionGroups: list[ExpressionGroupInput]
    ExpressionJoins: list[ExpressionJoinInput]
    ResultTypes: list[ResultTypeInput]

class SearchOptions:
    def __init__(self, ) -> None: ...
    DefaultLoadCount: int
    SortAttributes: list[str]
    SortOrder: list[str]

class SearchPredicateParameters:
    def __init__(self, ) -> None: ...
    Attribute: str
    ValueObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    PredicateOperator: int

class SearchRecipe:
    def __init__(self, ) -> None: ...
    ConfiguratorPerspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective
    Settings: System.Collections.Hashtable
    SearchExpression: SearchExpressionInput
    RootExpressionInputClientId: str
    VariantCriteria: Teamcenter.Soa.Client.Model.ModelObject

class SearchResultTable:
    def __init__(self, ) -> None: ...
    ObjectColumns: System.Collections.Hashtable
    StringColumns: System.Collections.Hashtable
    IntColumns: System.Collections.Hashtable
    DoubleColumns: System.Collections.Hashtable
    LogicalColumns: System.Collections.Hashtable
    DateColumns: System.Collections.Hashtable

class SearchResponse:
    def __init__(self, ) -> None: ...
    ObjectsDone: int
    RowsDone: int
    EstimatedObjectsLeft: int
    EstimatedRowsLeft: int
    FoundObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    SearchResultTable: SearchResultTable
    SearchCursor: Teamcenter.Soa.Client.Model.Strong.Cfg0SearchCursor
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SearchResultTableColumn:
    def __init__(self, ) -> None: ...
    Index: int
    Attribute: str
    Alias: str
    DataType: int

class TraversalExpressionInput:
    def __init__(self, ) -> None: ...
    ClientID: str
    TransferOptionsSet: Teamcenter.Soa.Client.Model.Strong.TransferOptionSet
    OptionNames: list[str]
    OptionValues: list[str]
    ResultColumns: list[SearchResultTableColumn]

class ValidateProductConfigInput:
    def __init__(self, ) -> None: ...
    ApplyConstraints: int
    ExpressionsToValidate: list[BusinessObjectConfigExpression]
    Context: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective

class ValidateProductConfigOutput:
    def __init__(self, ) -> None: ...
    UpdatedExpression: BusinessObjectConfigExpression
    Violations: list[Violation]

class ValidateProductConfigurationResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    Outputs: list[ValidateProductConfigOutput]

class VariantRuleInput:
    def __init__(self, ) -> None: ...
    Expressions: list[ConfigExpression]
    SaveRule: bool
    RuleToUpdate: Teamcenter.Soa.Client.Model.Strong.POM_object
    CreInputs: CreateInput
    RelationName: str
    ReferenceObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject

class VariantRuleOutput:
    def __init__(self, ) -> None: ...
    Index: int
    RuleObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    VariantExpression: list[ConfigExpression]

class Violation:
    def __init__(self, ) -> None: ...
    Message: str
    Severity: str
    ViolatedRule: ConfigExpression

class ConfiguratorManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateUpdateVariantRules(self, Rules: list[VariantRuleInput], RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule) -> CreateUpdateVariantRulesResponse: ...
    def ExecuteSearch(self, SearchRecipe: SearchRecipe, SearchOptions: SearchOptions) -> SearchResponse: ...
    def FetchNextSearchResults(self, SearchCursor: Teamcenter.Soa.Client.Model.Strong.Cfg0SearchCursor, LoadCount: int) -> SearchResponse: ...
    def GetDefaultRules(self, Context: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, FilterCriteria: FilterCriteria) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetExcludeRules(self, Context: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, FilterCriteria: FilterCriteria, Severities: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetFamilyGroups(self, Context: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective) -> GetFamilyGroupResponse: ...
    def GetIncludeRules(self, Context: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, FilterCriteria: FilterCriteria, Severities: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetModelsForProduct(self, Context: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, LeafLevelOnly: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetOptionFamilies(self, Context: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, Groups: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamilyGroup], OtherFamilies: bool, UnavailableFamilies: bool) -> GetOptionFamiliesResponse: ...
    def GetOptionValues(self, Context: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, Groups: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamilyGroup], Families: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsOptionFamily], UnavailableValues: bool) -> GetOptionValuesResponse: ...
    def GetProductDefaults(self, Inputs: list[ProductDefaultsInput]) -> GetProductDefaultsResponse: ...
    def GetVariantCache(self, ProductItem: Teamcenter.Soa.Client.Model.Strong.ItemRevision, RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule, ProductModelUID: str, ProductItemUID: str) -> GetVariantCacheInfoResponse: ...
    def GetVariantExpressionDisplayStrings(self, Inputs: list[ConfigExpressionDisplayStringInput], RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule) -> GetDisplayStringResponse: ...
    def StopSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.Strong.Cfg0SearchCursor) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ValidateProductConfiguration(self, Inputs: list[ValidateProductConfigInput]) -> ValidateProductConfigurationResponse: ...

