import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class TeamcenterConfiguratorInfo:
    """
    
            Contains additional information about variant data that is only available when using
            Teamcenter configurators. For any non Teamcenter configurator, this structure may
            contain null elements.
            
            The TeamcenterConfiguratorInfo structure
            is interoperated as "NULL" if it has following values set for its parameters:
            
            variant : NULLTAG
            
            optionValue : NULLTAG
            

    """
    def __init__(self, ) -> None: ...
    Variant: Teamcenter.Soa.Client.Model.Strong.Variant
    """
            Teamcenter family business object of type Variant. It can be null if information
            is retrieved from non Teamcenter configurator.
            """
    OptionValue: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            Workspace representation of option value code. This parameter can be null if information
            is being retrieved from non Teamcenter configurator.
            """

class ConfigOption:
    """
    
            Represents a configuration option that is unique in the context of a ConfigurationFamily.
            
            The ConfigOption structure is interpreted as "NULL" if it has the following values
            set for its parameters:  family: NULLTAG
            
            valueCode: empty string ("")
            
            description: empty string ("")
            
            additionalInfo : Null Structure
            

    """
    def __init__(self, ) -> None: ...
    Family: Teamcenter.Soa.Client.Model.Strong.ConfigurationFamily
    """A ConfigurationFamily object which represents a configuration option."""
    ValueCode: str
    """
            Name of the option value. "" is treated as NO VALUE SELECTED, i.e. it does not match
            any non-empty name.
            """
    Description: str
    """Description of the option value."""
    AdditionalInfo: TeamcenterConfiguratorInfo
    """
            A TeamcenterConfiguratorInfo struct having
            additional information about Teamcenter configurator objects.
            """

class ConfigFormula:
    """
    
            Represents a formula string associated with a configuration expression in configurator
            syntax.  A formula of the form "[OptionNamespace]FamilyName = UniqueValue" is called
            "explicit" because no product context is required to determine the family name for
            the value, or the option namespace for the family name. OptionNamespace and FamilyName
            are explicitly spelled out. A variant formula is in "explicit Teamcenter language"
            if its form is explicit and comprised of the lexemes documented for the Variant Formula
            property. A formula of the form "UniqueValue" is called "stenographic" because a
            parser has to infer OptionNamespace and FamilyName. This is possible if there is
            only one value with that name throughout the entire product. If lexemes other than
            those documented for the Variant Formula property are used the formula is in "external
            variant language" and a custom configurator is required to decode the formula. If
            a formula is explicit Teamcenter language, productName and productNameSpace can be
            empty (""). The ConfigFormula structure is considered "NULL" if it has following
            values set for its parameters: - formula: empty string ("") - productName: empty
            string ("") - productNameSpace: empty string ("")
            
    """
    def __init__(self, ) -> None: ...
    Formula: str
    """Formula string in configurator syntax."""
    ProductName: str
    """
            Name of the product(e.g.ItemID). Used in conjunction with productNameSpace parameter
            to resolve any ambiguity in variant option value names.
            """
    ProductNameSpace: str
    """
            Namespace of the product in which the "product" has unique semantics, e.g., ItemRevID,
            model_year or product_type. Used in conjunction with productName parameter to resolve
            any ambiguity in variant option value names.
            """

class ConfigExpression:
    """
    
            Represents a configuration expression. The ConfigExpression
            structure is interpreted as "NULL" when it
            has following values set for its parameters:
            
subExpressions : An empty vector of ConfigExpression structure
            
value : A "NULL" ConfigOption
            structure
            
opCode : -1
            
formula : A "NULL" ConfigFormula
            structure
            
tnf : An empty vector of ConfixExpression structures.
            
            A ConfigExpression that is equivalent to
            the Boolean constant TRUE returns a TNF parameter
            comprising one expression with an opcode
            value of 39.
            
            A ConfigExpression that is equivalent to
            the Boolean constant FALSE returns a TNF
            parameter comprising one expression with an opcode
            value of 40.
            
    """
    def __init__(self, ) -> None: ...
    SubExpressions: list[ConfigExpression]
    """
            A vector of ConfigExpression. If this parameter
            is present the enclosing expression represents a compound expression combining this
            set of subexpressions with the operator specified in the opCode parameter. If the
            enclosing expression is non-NULL either this parameter or the "value" parameter must be present.
            """
    Value: ConfigOption
    """
            It is a ConfigOption struct. If this parameter
            is present the enclosing expression represents an elemental expression literal. The
            parameter specifies the value to which opCode
            compares. If the enclosing expression is non-NULL either this parameter or the subExpressions parameter must be present. subExpressions and
            value must not both be present.
            """
    OpCode: int
    """Operation code such as "and" and "or", see ps/ps_tokens.h."""
    Formula: ConfigFormula
    """
            It is a ConfigFormula struct. If present,
            contains the configuration expression in string format (courtesy info).
            """
    Tnf: list[ConfigExpression]
    """
            If present, this parameter provides a representation of the enclosing expression
            in Teamcenter Normal Form (TNF).
            
            The parameter is intended as "courtesy information" so to make additional SOA calls
            unnecessary by providing information that is expected to be of value if performance
            permits it. Based on the assumption that the vast majority of ConfigExpression structs
            can be converted to TNF very efficiently the server can afford to convert them to
            TNF as a "free gift". If this becomes a performance bottleneck the server may return
            a response with an empty tnf member, in which case the application can explicitly
            request a tnf representation using operation convertVariantExpressions,
            if need be. Preference TC_tnf_timeout_period
            controls the timeout mechanism. If TNF generation takes more time than specified
            in preference TC_tnf_timeout_period, server
            returns an empty tnf member.
            
            If combined with OR the list of tnf expressions is logically equivalent to the enclosing
            expression. Each TNF is provided as a conjunction of Disjunctive Normal Forms (DNF)
            where all DNFs reference a single variant option family. Each clause in the outermost
            conjunction can reference a different variant option family.
            
Example 1:

            Formula: (ENG = V6 | ENG = V8) & (D = 2.6L | D >= 3L & D <= 3.6L)
            
            TNF: Yes
            
            Note: DNF1 references family ENG and DNF2 references family D
            
Example 2:

            Formula: (ENG = V6 | TRANS = AUTO) & (TRANS = M5 | ENG = V8)
            
            TNF: No
            
            Note: DNF1 references family ENG as well as TRANS and  DNF2 references family ENG
            as well as TRANS
            """

class ConfigRuleViolation:
    """
    
            Represents a violated rule along with the message and severity associated with rule
            violation.  The ConfigRuleViolation structure
            is interpreted to be "NULL" if following values are set to its parameters:
            
            - message: empty string ("")
            
            - severity: ConstraintSeverityInformation
            
            - violatedCondition: a "NULL" ConfigExpression structure
            
    """
    def __init__(self, ) -> None: ...
    Message: str
    """The message to display if this rule is violated."""
    Severity: str
    """
            The severity code for the message. Valid values are:
            
            - ConstraintSeverityInformation : Classifies information associated with this constraint
            as additional information, such as hints, which are of interest if configuration
            criteria satisfy this constraint.
            
            - ConstraintSeverityWarning : Classifies information associated with this constraint
            as considerations, such as recommendations, which are important to review if configuration
            criteria satisfy this constraint.
            
            - ConstraintSeverityError : Configuration criteria that satisfy this constraint
            are classified as invalid.
            """
    ViolatedCondition: ConfigExpression
    """The rule that was found to be violated."""

class DefaultRule:
    """
    
            A rule to determine the default value, or value range, for a variant option family.
            The DefaultRule structure is interpreted
            to be "NULL" if it has following values set to its parameters:
            
            - partiallyApplicable: false
            
            - restrictiveCondition: a "NULL" ConfigExpression
            
            - appliedDefault: "NULL" ConfigExpression
            structure
            
            - appliedTo: "NULL" ConfigExpression structure
            
    """
    def __init__(self, ) -> None: ...
    PartiallyApplicable: bool
    """If "true", the default is only applicable to a subset of the criteria (courtesy info)."""
    RestrictiveCondition: ConfigExpression
    """The condition under which the default is applicable. Can be NULL."""
    AppliedDefault: ConfigExpression
    """
            The default condition that was applied, indicating that "restrictiveCondition"
            was met.
            """
    AppliedTo: ConfigExpression
    """The config condition before applying the default."appliedDefault"."""

class VariantCriteria:
    """
    
            The VariantCriteria structure represents
            a criteria object along with its variant criteria and associated validation records.
            The VariantCriteria structure is interpreted
            to be "NULL" if the following values are set for its parameters: - variantCriteriaObject: NULLTAG - primaryVariantScope:
            a "NULL" ConfigFormula structure - solveType:
            -1 - validationRecords: empty vector
            
    """
    def __init__(self, ) -> None: ...
    VariantCriteriaObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """The VariantRule with which the criteria defines in this structure is associated."""
    PrimaryVariantScope: ConfigExpression
    """Nominal variant criteria before applying constraints and defaults."""
    SolveType: int
    """
            Indicates how the variant criteria need to be solved. For possible values see preference
            TC_Default_Solve_Type.
            """
    ValidationRecords: list[VariantValidationRecord]
    """Validation records related to the variant criteria."""

class VariantCriteriaResponse:
    """
    
            Returns variant configuration criteria along with default and constraint processing
            results.
            
    """
    def __init__(self, ) -> None: ...
    VariantCriteria: list[VariantCriteria]
    """Vector of variant criteria structures"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Teamcenter ServiceData"""

class VariantValidationRecord:
    """
    
            Represents validation results for variant criteria associated with a variant criteria
            object (VariantRule ). The VariantValidationRecord
            structure is interpreted to be "NULL" if the following values are set to its parameters:
            
-validationDate: a NULLDATE as defined for
            the SOA client side binding in use.
            
-validationResult: a "NULL" ConfigFormula
            structure
            
-undeterminedFamilies: an empty vector
            
-violations: an empty vector
            
-appliedDefaults: an empty vector
            
    """
    def __init__(self, ) -> None: ...
    ValidationDate: System.DateTime
    """Date of validation."""
    ValidationResult: ConfigExpression
    """Validation result reflecting constraints and defaults."""
    UndeterminedFamilies: list[Teamcenter.Soa.Client.Model.Strong.ConfigurationFamily]
    """Families that are not set to a unique value. If empty, the criteria are complete."""
    Violations: list[ConfigRuleViolation]
    """Violation records. If empty, the variant criteria are valid."""
    AppliedDefaults: list[DefaultRule]
    """One record for each applied default in the sequence they were applied."""

class VariantManagement:
    """
    Interface VariantManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetProductConfigurations(self, ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> VariantCriteriaResponse:
        """    
             This operation returns a set of product configurations managed at the configurator
             level, say for product tracking or reporting purposes.
             
             Teamcenter variant configurators manage product configurations as VariantRules
             which are attached to an ItemRevision representing the product using any relationship
             type (see also preference TC_Default_SVR_Relationship).
             The product is identified by productName
             and productNameSpace parameters. Teamcenter
             configurators use a Multiple Field Key (MFK) stable identifier (see property Item::fnd0VariantNamespace) of the product item
             for productName, and the revision ID for
             productNameSpace. The identifiers of the
             product associated with a Collaborative Design (Cpd0CollaborativeDesign) can
             be obtained from properties Mdl0ApplicationModel::mdl0config_product_name,
             and Mdl0ApplicationModel::mdl0config_prod_namespace.
             

Use Cases:

             An engineering project administrator has created a product ItemRevision. A
             manufacturing engineering user creates and maintains VariantRules that represent
             a set of configurations for prototype builds. The project administrator attaches
             these VariantRules to the product ItemRevision. Product engineering
             users can use operation getProductConfigurations
             to review existing prototype configurations. The user can then chose one of the configurations
             to initialize variant configuration criteria with operation setVariantCriteria.
             

Dependencies:

             setVariantCriteria
             

Teamcenter Component:

             Configuration Management - Capability to configure structured data based on revsion
             rules; effectivities; Status etc.
             
        :param ProductName: 
                         Identifies the product. It is used in conjunction with parameter <font face="courier" height="10">productNameSpace</font> to resolve potential ambiguity in variant option
                         value names, and to identify product context specific constraints. Teamcenter configurators
                         use a Multiple Field Key (MFK) stable identifier (see property <font face="courier" height="10">Item::fnd0VariantNamespace</font>) of the product item for <font face="courier" height="10">productName</font>. The <font face="courier" height="10">productName</font>
                         value for a Collaborative Design (<b>Cpd0CollaborativeDesign</b>) can be obtained
                         from property <font face="courier" height="10">Mdl0ApplicationModel::mdl0config_product_name</font>.
             
        :param ProductNameSpace: 
                         Specifies the namespace for the product identifier. It is used in conjunction with
                         parameter <font face="courier" height="10">productName</font> to resolve potential
                         ambiguity in variant option value names, and to identify product context specific
                         constraints. Teamcenter configurators use the Revision ID of the product <b>ItemRevision</b>
                         for <font face="courier" height="10">productNameSpace</font>. The <font face="courier" height="10">productNameSpace</font> value for a Collaborative Design (<b>Cpd0CollaborativeDesign</b>)
                         can be obtained from property <font face="courier" height="10">Mdl0ApplicationModel::mdl0config_prod_namespace</font>.
             
        :param ConfiguratorURL: 
                         The service end point for the variant configurator service. If empty the local Teamcenter
                         configurator is used. Tc10.1 only supports local Teamcenter configurators. In Tc10.1
                         a non-empty <font face="courier" height="10">configuratorURL</font> parameter will
                         cause an error.
             
        :return: Response object containing variant criateria list.
        """
        ...

