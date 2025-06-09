import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AvailableVariability:
    """
    
            The struct defines available features or ranges for a given configuration family
            satisfying the input criteria.
            
    """
    def __init__(self, ) -> None: ...
    Availability: list[ExpressionTerm]
    """
            A list of configuration expressions referencing available values only from the requested
            families. This is a list of discrete values or ranges. Each value has a selection
            severity associated with it denoting whether the feature has been selected by user
            or by constraint evaluation.
            """

class ExpressionInfo:
    """
    This represents an expression which is a collection of variant and effectivity expressions.
    """
    def __init__(self, ) -> None: ...
    VariantFormula: str
    EffectivityFormula: str
    """
            The Effectivity Configuration Expression represented as Teamcenter formula and not
            as display formula. The display formula which could have effect of localization and/or
            customization.
            """
    JsonExpression: str
    """The expression represented as a JSON string. This is reserved for future use."""

class Expression:
    """
    
            This struct represents an expression along with its product hierarchy path. The product
            hierarchy path specifies the complete path to the node in hierarchy to which the
            expression belongs.
            
    """
    def __init__(self, ) -> None: ...
    ProductHierarchyPath: str
    """
            The product hierarchy path which represents an offset of expression with respect
            to the root product context. This is reserved for future use.
            """
    ExpressionInfo: ExpressionInfo
    """The expression consisting of variant expression and effectivity expression."""

class AvailableVariabilityResponse:
    """
    
            The structure represents response for the getAvailableVariability operation
            consisting of available variability for the requested families, expanded expression,
            status of the configuration and a service data.
            
            To get the details of violations for invalid configuration or list of families with
            missing selections for valid and incomplete configuration, the validateAndExpandExpressions
            service operation should be called.
            
    """
    def __init__(self, ) -> None: ...
    AvailableVariability: list[AvailableVariability]
    ExpandedExpression: Expression
    """
            The expanded expression satisfying the given input expression and set of constraint(s)
            for the given configurator context. It will consist of input expression along with
            system suggested features only for the requested families. The expanded expression
            will be present in the response only for a valid configuration.
            """
    IsValid: bool
    """
            True if the configuration is valid. To know the violations for an invalid configuration,
            the validateAndExpandExpressions operation should be called.
            """
    IsComplete: int
    ResponseInfo: list[KeyValuePair]
    """A list of response names and value pairs. This is reserved for future use."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data for errors and returned objects."""

class BatchSolveConditionsResponse:
    """
    
            The response contains solve results of variant conditions validated against VariantRule.
            Service Data contains information about error details for any failures in solving
            the variant conditions.
            
    """
    def __init__(self, ) -> None: ...
    SolveResults: list[ConditionSolveResult]
    """
            A list of conditions solve results validated against each VariantRule. The list of
            solveResults and the list of input, variantRules will be in the same sequence.
            """
    ResponseInfo: list[KeyValuePair]
    """A list of response names and value pairs. This is reserved for future use."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData containing partial exceptions, if any."""

class Conditions:
    """
    
            This represents a list of variant conditions expressions to be validated against
            a VariantRule.
            
    """
    def __init__(self, ) -> None: ...
    ConditionExpressions: list[ExpressionInfo]
    """
            A list of variant conditions that are validated against each VariantRule. ExpressionInfo
            is used to represent a variant condition formula.
            """
    ProductHierarchyPath: str

class ConditionSolveResult:
    def __init__(self, ) -> None: ...
    ConditionsStatus: list[ConditionsStatus]
    """
            A list of Conditions solves status. The list of conditionsStatus and the list of
            input, conditionExpressions of the conditions will be in same sequence.
            """
    IsValid: bool
    """If true, the configuration of the VariantRule is valid otherwise invalid."""
    IsComplete: int
    """
            The completeness status of the configuration of the VariantRule. Valid values are
            as follows:
            
            0 - Unknown; the completeness status of the configuration is unknown. You should
            send the appropriate solve profile as input to the operation to get the completeness
            status.
            
            1 - Incomplete; not all families in the configuration have value selections.
            
            2- Complete; all families in the configuration have value selections.
            """

class ConditionsStatus:
    """
    This represents the status of variant conditions validated against a VariantRule.
    """
    def __init__(self, ) -> None: ...
    IsConfigured: list[int]
    Explanation: list[str]
    """A list of explaination for isConfigured status. This is for future use."""

class ConfigurationInformationOutput:
    """
    The structure for holding configuration session information.
    """
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.Strong.VariantRule
    """VariantRule or its subtype."""
    Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective
    """
            The Cfg0ConfiguratorPerspective instance which provides the product information
            used to select the features and constraints. The product information is a combination
            of Cfg0ProductItem (represented by cfg0ProductItems property), RevisionRule
            (represented by cfg0RevisionRule property), effectivity string (represented by cfg0RuleSetEffectivity
            property) and rule date (represented by cfg0RuleSetCompileDate property).
            """
    SolveProfile: str
    """
            The configuration solve profile as JSON string that consists of attributes governing
            the behavior of configurator constraint evaluation. This string should adhere to
            the JSON schema for solve profile defined in SolveProfile_Schema.json; please refer
            to schema and sample solve profiles defined at %TC_DATA%/json/variabilityadaptor/schema
            for details. Each solve profile key should occur only once in the solve profile JSON
            string.
            """

class ExpressionStatus:
    def __init__(self, ) -> None: ...
    ExpandedExpression: Expression
    """
            The expanded expression satisfying the given input expression and set of constraint(s)
            for the given configurator context. It will consist of input expression along with
            system suggested features only for the requested families. The expanded expression
            will be present in the response only for a valid configuration.
            """
    IsValid: bool
    """
            The flag indicates whether the configuration is valid or invalid. If valid, the value
            in the response will be true else false.
            """
    IsComplete: int
    """
            The completeness status of the configuration. Valid values are as follows:
            
            0 - Unknown; the completeness status of the configuration is unknown. User should
            send the appropriate solve profile as input to the operation to get the completeness
            status.
            
            1 - Incomplete; not all families in the configuration have value selections.
            
            2- Complete; all families in the configuration have value selections.
            """
    OptimizedRuleSet: bool
    """
            The flag indicates whether the configuration was optimized. If set to true, the response
            was computed with an optimized ruleset.
            """
    OptimizationCriteria: Expression
    """The criteria formula used for optimizing the ruleset."""
    Violations: list[ViolationList]
    """List of the unique violations."""
    MissingSelections: list[OptionList]
    """List of the families, for these families there are no selection or no precise selections."""

class ExpressionTerm:
    """
    
            Defines an elemental expression literal for a single feature, or feature range expression
            for a given family.
            
    """
    def __init__(self, ) -> None: ...
    Family: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamily
    """
            The family object instance to be used in a family expression term, or a feature range
            expression.
            """
    FamilyID: str
    """
            The ID of family in the term. It will have a value only if the family is present
            in an expression and family is NULL.
            """
    FamilyNamespace: str
    """
            The family namespace by which the family object is uniquely identified. It will have
            a value only if the family is present in an expression and family is NULL.
            """
    OperatorCode: int
    RangeExpressions: list[RangeExpression]
    """A list of elemental expression literals describing a feature range for a given family."""
    Feature: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsValue
    """The feature object to be used in an elemental expression literal."""
    ValueText: str
    """The ID of the feature or the feature to use for a free form family."""
    SelectionSeverity: str

class Family:
    """
    
            Represents a family (Cfg0AbsOptionFamily) or a Feature Familiy (Cfg0AbsFeatureFamily)
            business object along with the Family Allocation (Cfg0AbsAllocation ) business
            object for the input Configurator context.
            
    """
    def __init__(self, ) -> None: ...
    CfgFamily: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamily
    FamilyAllocation: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsAssociation
    """
            The allocation object (Cfg0AbsAssociation) with respect to the current family
            and input configurator context.
            """
    Features: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsConfiguratorWSO]
    Groups: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamilyGroup]
    """
            The Family Group objects (CfgAbsFamilyGroup) that the current family is member
            of. The subset of Family Group objects (CfgAbsFamilyGroup) that are attached
            to the input perspective and contain the current family.
            """

class FamilyGroup:
    """
    
            Represents a Family Group (Cfg0AbsFamilyGroup) with its allocation business
            object and its member families.
            
    """
    def __init__(self, ) -> None: ...
    FamGroup: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamilyGroup
    """
            The group (Cfg0AbsFamilyGroup ) business object represented by the structure.
            This object identifies the navigation structure in in Guided Variant Configuration
            (active validation). The following characteristics are important in this context:
            
            1.    Family Groups (and Family Group allocations) cannot
            be revised.
            
            2.    The same Family Group may be allocated to multiple
            Configurator Contexts.
            
            3.    Family Groups may contain families across multiple
            products.
            
            4.    Allocating a Family Group does not automatically allocate
            its families. Configurator Contexts may choose to only allocate a subset of the families
            in each Family Group.
            """
    GroupAllocation: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsAssociation
    Families: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamily]
    """
            List of Families (Cfg0AbsOptionFamily) and Feature Families (Cfg0AbsFeatureFamily)
            business objects  in this group. The Revision Rule in the Configurator Perspective
            (Cfg0ConfiguratorPerspective.cfg0ProductItems) must select a valid family
            revision and family allocation revision.
            """

class FamilyList:
    """
    
            The structure represents a list of Cfg0AbsFamily allocated to the same product
            context in product hierarchy. The product hierarchy path specifies the complete path
            to the context in hierarchy to which the families belong.
            
    """
    def __init__(self, ) -> None: ...
    ProductHierarchyPath: str
    """
            The product hierarchy path which represents an offset with respect to the list of
            families. This is reserved for future use.
            """
    Families: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamily]
    """A list of Cfg0AbsFamily allocated to the same product context."""

class FeatureValue:
    """
    
            Represents (Cfg0AbsOptionValue) and Standalone Feature (Cfg0AbsFeature)
            business objects for the given configurator context.
            
    """
    def __init__(self, ) -> None: ...
    Feature: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsConfiguratorWSO
    """
            Feature and Standalone Feature (Cfg0AbsOptionValue and Cfg0AbsFeature)
            which are attached to the current family. It is of type Cfg0AbsConfiguratorWSO
            (common parent) as it may hold either Cfg0AbsOptionValue or Cfg0AbsFeature
            type.
            
            If it is of type Standalone Feature (Cfg0AbsFeature) then it must be a member
            of Feature Family (Cfg0AbsFeatureFamily.cfg0Features).
            
            The Revision Rule in the Configurator Perspective (Cfg0ConfiguratorPerspective.cfg0RevisionRule)
            must select a valid feature revision.
            
            For a revision of a feature to be configured for the given revision rule, the following
            objects must also be configured:
            

Feature revision (Cfg0AbsOptionValue and Cfg0AbsFeature)
            
Feature allocation revision (Cfg0AbsAllocation)
            
Family revision (Cfg0AbsOptionFamily and Cfg0AbsFeatureFamily)
            
Family allocation revision (Cfg0AbsAllocation)
            

"""
    Family: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsFamily
    """
            Family (Cfg0AbsOptionFamily) or Feature Family (Cfg0AbsFeatureFamily)
            business object revision of the current feature.
            """
    Allocation: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsAssociation

class GetConfigurationInformationResponse:
    """
    
            The response structure for retrieving Configuration Information from VariantRule
            objects. The session information is retrieved as a combination of Cfg0ConfiguratorPerspective
            representing the product information and Solve Profile which represents the parameters
            for constraint evaluation. The service data returns partial error encountered in
            retrieving the session information from an input object against the index of the
            object in input list.
            
    """
    def __init__(self, ) -> None: ...
    ConfigInformations: list[ConfigurationInformationOutput]
    """
            A list of configuration information retrieved from input VariantRule objects.
            The session information is retrieved as a combination of Cfg0ConfiguratorPerspective
            representing the product information and Solve Profile which represents the
            parameters for constraint evaluation.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The service data returns partial error encountered in retrieving the session information
            from an input object against the index of the object in input list.
            """

class GetVariablityResponse:
    """
    The response structure for the getVariablity operation
    """
    def __init__(self, ) -> None: ...
    ProductFamilies: list[ProductFamily]
    Groups: list[FamilyGroup]
    GroupedFamilies: list[Family]
    """List of Family structures that are assigned to groups"""
    UngroupedFamilies: list[Family]
    """
            List of Family structures that are not assigned to any groups. Here the groups member
            of the Family->groups member is empty.
            """
    Features: list[FeatureValue]
    """
            List of FeatureValue structs that represent (Cfg0AbsOptionValue) and Standalone
            Feature (Cfg0AbsFeature) business objects for the given configurator context.
            """
    ResponseInfo: list[KeyValuePair]
    """
            For future use. Currently it will be empty in the response. The filter struct allows
            user to filter the output response.  The filter struct has name and values the server
            can use to specify what kind of data was requested. It returns the response key-value
            pairs for the corresponding request key-value pairs.
            

            The valid name-values are
            


Cfg0::response:filter:Groups  - Represents a Boolean value. If true,
            then returns the list of family group (Cfg0AbsFamilyGroup) objects as part
            of the GetVariabilityResponse.groups member. Default is true.
            
Cfg0::response:filter::Products - Represents a Boolean value. If
            true, then returns Product model, Product Line, Summary Models as part of the GetVariablityResponse.productFamilies
            member. Default is true.
            
Cfg0::response:filter:UngroupedFamilies - Represents a Boolean value.
            If true, the operation returns the families that are not part of any group as part
            of the GetVariablityResponse.ungroupedFamilies member. Default is true.
            

"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Teamcenter ServiceData"""

class KeyValuePair:
    def __init__(self, ) -> None: ...
    Key: str
    """The key string."""
    Values: list[str]
    """A list of value strings associated with the key."""

class OptionList:
    """
    
            The structure represents a list of Families associated with the same product context
            in product hierarchy. The product hierarchy path specifies the complete path to the
            context in hierarchy to which the families belong.
            
    """
    def __init__(self, ) -> None: ...
    ProductHierarchyPath: str
    """
            The product hierarchy path which represents an offset with respect to the list of
            families. This is reserved for future use.
            """
    Objects: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsConfiguratorWSO]
    """A list of Families associated with the same product context."""

class ProductFamily:
    def __init__(self, ) -> None: ...
    ModelFamily: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsModelFamily
    Members: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsModel]

class RangeExpression:
    """
    
            An elemental expression literal that is used in a value range expression for a given
            family.
            
    """
    def __init__(self, ) -> None: ...
    OperatorCode: int
    Feature: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsValue
    """The feature object to be used in a range expression."""
    ValueText: str
    """The string value of the feature."""

class ValidateAndExpandExprsResponse:
    """
    
            The structure represents response for the validateAndExpandExpressions
            operation consisting of information expanded expression, status of the configuration,
            families missing selections, violations in case of the invalid configuration foreach
            input expression and a service data.
            
    """
    def __init__(self, ) -> None: ...
    Status: list[ExpressionStatus]
    """
            The status structure holds information about the expanded expression status of the
            configuration, families missing selections, violations in case of the invalid configuration.
            """
    ResponseInfo: list[KeyValuePair]
    """A list of response names and value pairs. This is reserved for future use."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data for errors and returned objects."""

class Violation:
    """
    
            The structure represents a violated rule along with the message and severity associated
            with rule violation.
            
    """
    def __init__(self, ) -> None: ...
    Message: str
    """The message to display if this rule is violated."""
    Severity: str
    """
            The severity associated with the message. Valid values for this parameter are defined
            by the ListOfValues "Cfg0ConstraintSeverity".
            """
    OptimizedRule: bool
    """
            If true, this violated rule was modified while optimizing the ruleset. The constraint
            was modified by the system for performance reasons and the user will not find the
            same rule in the database.
            """
    ViolatedRuleExpresion: Expression
    """The expression that represents the violation."""
    ConfiguratorWSO: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsConfiguratorWSO
    """
            Validation constraint for product variant configurations. It might contain NULL in
            case user is not privileged to read validation constraint rule.
            """

class ViolationList:
    """
    
            The structure represents the violated rules along with the message and severity associated
            with rule violation. It represents independent set of constraint rules which are
            responsible for conflict.
            
    """
    def __init__(self, ) -> None: ...
    StatusMessage: str
    """The message describing the statusCode."""
    StatusCode: int
    Violations: list[Violation]
    """Set of violated rules which together responsible for a conflict."""

class ConfiguratorManagement:
    """
    Interface ConfiguratorManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def BatchSolveConditions(self, VariantRules: list[Teamcenter.Soa.Client.Model.Strong.VariantRule], Conditions: list[Conditions], RequestInfo: list[KeyValuePair]) -> BatchSolveConditionsResponse: ...
    def GetAvailableVariability(self, Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, SolveProfile: str, Expression: Expression, Families: FamilyList, RequestInfo: list[KeyValuePair]) -> AvailableVariabilityResponse: ...
    def GetConfigurationInformation(self, TargetObjects: list[Teamcenter.Soa.Client.Model.Strong.VariantRule]) -> GetConfigurationInformationResponse: ...
    def GetVariability(self, Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, RequestInfo: list[KeyValuePair]) -> GetVariablityResponse: ...
    def SetConfigurationInformation(self, TargetObjects: list[Teamcenter.Soa.Client.Model.Strong.VariantRule], ConfigPerspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, SolveProfile: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ValidateAndExpandExpressions(self, Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, SolveProfile: str, Expressions: list[Expression], RequestInfo: list[KeyValuePair]) -> ValidateAndExpandExprsResponse: ...

