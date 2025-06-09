import Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement
import System
import Teamcenter.Soa.Client.Model
import typing

class EffectivityDisplayStringResponse:
    """
    
            A list of localized string representations for effectivity expressions. The format
            is a pure output format intended to increase ease of reading. It cannot be used as
            input because its format allows ambiguous syntax.
            
    """
    def __init__(self, ) -> None: ...
    DisplayString: list[str]
    """
            Vector of effectivity display strings. This format is the same as for effectivity
            formula properties mdl0effectivity_formula and mdl0allowed_eff_formula.
"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Teamcenter service data."""

class EffectivityOverlapStateResponse:
    """
    Indicates the degreee of overlap for pairs of effectivity expressions.
    """
    def __init__(self, ) -> None: ...
    OverlapStates: list[OverlapStateList]
    """A vector of overlap enumeration values."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Teamcenter service data."""

class OverlapStateList:
    """
    A list of indicators for the degree of overlap between two effectivity expressions.
    """
    def __init__(self, ) -> None: ...
    OverlapStates: list[str]
    """
            A vector of overlap enumeration values. Valid values for an overlap enumeration are:
            
            -    OverlapStateNone : The two expressions have no overlap.
            There is no satisfing solution common to both expressions. A conjunction (AND combination)
            of the two is unsatisfiable.
            
            -    OverlapStateSubset : The two expressions overlap. The expression's
            solution set is a subset of the reference expression's solution set. The conjunction
            (AND combination) of the expression with the negated reference expression is unsatisfiable.
            
            -    OverlapStateMatch : The two expressions are logically equivalent.
            Every solution that satifies one expression also satifies the other, and vice versa.
            
            -    OverlapStateSuperset : The two expressions overlap. The
            expression's solution set is a superset of the reference expression's solution set.
            The conjunction (AND combination) of the negated expression with the reference expression
            is unsatisfiable.
            
            -    OverlapStateIntersect : The two expressions overlap. The
            expression's solution set has some overlap with the refernce expression's solution
            set.
            
"""

class EffectivityManagement:
    """
    Interface EffectivityManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetEffectivityDisplayString(self, Expressions: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> EffectivityDisplayStringResponse:
        """    
             This operation returns a localized string representation for effectivity expressions.
             This string representation is the same that is used for display values of effectivity
             formula properties mdl0effectivity_formula and mdl0allowed_eff_formula.
             Applications can use this API to display effectivity conditions for objects that
             have not yet been saved with this effectivity, e.g. if multiple effectivity modifications
             are accumulated in a client session before they are saved. In this scenario effectivity
             properties are not (yet) available prior to saving modified objects.
             
             This operation connects to the effectivity configurator service whose service endpoint
             is specified by the configuratorURL parameter.
             The actual conversion to formula strings is performed by this configurator service.
             Depending on the (configurator specific) encoding the operation might require the
             specification of a product context using parameters productName
             and productNameSpace. For example, a given
             configurator might use  shorthand representations for formulae if these are unique
             in the context of the specified product. Teamcenter 10.1 only supports local built
             in Teamcenter configurators where parameter configuratorURL
             can be set to an empty string. Teamcenter configurators don't require a product context
             if the formulae are in Explicit Teamcenter Language. The encoding is explicit
             if all lexemes are uniquely identified, e.g. [OptionNamespace]FamilyName
             = UniqueValue, where no product context is required to determine the family
             name for a value, or the option namespace for the family. A configuration condition
             formula is in Explicit Teamcenter Language if its form is explicit and comprised
             of the lexemes documented for the Teamcenter Variant Formula property. Teamcenter
             configurators support shorthand encodings like FamilyName = UniqueValue
             or UniqueValue if the lexemes used in the shorthand encoding are unique in
             the specified product context.
             

Use Cases:

             An application prepares several effectivity conditions with the intent to save them
             to a set of objects using operation setEffectivityConditions. The application
             wants to display the effectivity display string that would get saved with setEffectivityConditions
             before actually saving them.
             

Dependencies:

             setEffectivityConditions
             

Teamcenter Component:

             Configuration Management - Capability to configure structured data based on revsion
             rules; effectivities; Status etc.
             
        :param Expressions: 
                         Configuration expressions for which the effectivity display string is requested.
             
        :param ProductName: 
                         Identifies the product. It is used in conjunction with parameter <font face="courier" height="10">productNameSpace</font> to resolve potential ambiguity in variant option
                         value names, and to identify product context specific constraints. Teamcenter configurators
                         use a Multiple Field Key (MFK) stable identifier (see property <font face="courier" height="10">Item::fnd0VariantNamespace</font>) of the product item for <font face="courier" height="10">productName</font>. The <font face="courier" height="10">productName</font>
                         value for a Collaborative Design (<b>Cpd0CollaborativeDesign</b>) can be obtained
                         from property <font face="courier" height="10">Mdl0ApplicationModel::mdl0config_product_name.</font>

        :param ProductNameSpace: 
                         Specifies the namespace for the product identifier. It is used in conjunction with
                         parameter <font face="courier" height="10">productName</font> to resolve potential
                         ambiguity in variant option value names, and to identify product context specific
                         constraints. Teamcenter configurators use the Revision ID of the product ItemRevision
                         for <font face="courier" height="10">productNameSpace</font>. The productNameSpace
                         value for a Collaborative Design (<b>Cpd0CollaborativeDesign</b>) can be obtained
                         from property <font face="courier" height="10">Mdl0ApplicationModel::mdl0config_prod_namespace.</font>

        :param ConfiguratorURL: 

        :return: Response object containing effectivity display values.
        """
        ...
    def GetEffectivityOverlapStates(self, ReferenceExpressions: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression], Expressions: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> EffectivityOverlapStateResponse:
        """    
             This operation determines and returns the degree of overlap between a set of effectivity
             expressions and a set of reference effectivity criteria expressions. When applications
             create or update DesignElements (DE) and assign effectivity, the UI may want to qualify
             the degree of overlap between the effectivity of the DE and the currently active
             RevRule effectivity criteria.
             
             The following example illustrates the overlap states for a set of expressions:
             
RevisionRule:     |---------------|
             
             Object 0:  |----|                            : OverlapStateNone
             
             Object 1:     |------|                       : OverlapStateIntersect
             
             Object 2:                |----|              : OverlapStateSubset
             
             Object 3:                    |------|        : OverlapStateIntersect
             
             Object 4:  |-----------------------------|   : OverlapStateSuperset
             
             Object 5:         |---------------|          : OverlapStateMatch
             
             Object 6:         |-------------------|      : OverlapStateSuperset
             
             Object 7:     |-------------------|          :
             OverlapStateSuperset

             This operation connects to the effectivity configurator service whose service endpoint
             is specified by the configuratorURL parameter.
             Any conversion from formula strings is performed by this configurator service. Depending
             on the (configurator specific) encoding the operation might require the specification
             of a product context using parameters productName
             and productNameSpace. For example, a given
             configurator might recognize shorthand representations for formulae if these are
             unique in the context of the specified product. Teamcenter 10.1 only supports local
             built in Teamcenter configurators where parameter configuratorURL
             can be set to an empty string. Teamcenter configurators don't require a product context
             if the formulae are in Explicit Teamcenter Language. The encoding is explicit
             if all lexemes are uniquely identified, e.g. [OptionNamespace]FamilyName
             = UniqueValue, where no product context is required to determine the family
             name for a value, or the option namespace for the family. A configuration expression
             formula is in Explicit Teamcenter Language if its form is explicit and comprised
             of the lexemes documented for the Teamcenter Variant Formula property. Teamcenter
             configurators support shorthand encodings like FamilyName = UniqueValue or
             UniqueValue if the lexemes used in the shorthand encoding are unique in the
             specified product context.
             

Use Cases:

             An application wants to qualify effectivity conditions that were retrieved with getEffectivityConditions
             as to whether the condition is equal to, intersects with, or is a subset or superset
             of the effectivity criteria associated with one or more RevisionRules. This
             cannot be achieved with properties on effectivity conditions or RevisionRules because
             the result depends on the combination of an effectivity condition and the effectivity
             configuration criteria on a RevisionRule. One and the same condition may have
             different overlap states with different RevisionRules.
             
             The application calls getEffectivityOverlapStates and passes the effectivity
             criteria (as obtained from a RevisionRule using getRevRuleEffectivityCriteria)
             as referenceExpressions, and the effectivity
             conditions (as obtained from a set of product data elements using getEffectivityConditions)
             as expressions.
             


Dependencies:

             getEffectivityConditions, getRevRuleEffectivityCriteria
             

Teamcenter Component:

             Configuration Management - Capability to configure structured data based on revsion
             rules; effectivities; Status etc.
             
        :param ReferenceExpressions: 
                         The vector of reference effectivity criteria expressions.
             
        :param Expressions: 
                         Vector of effectivity expressions. The response returns the overlap state of each
                         expression in this vector, with each of the reference effectivity criteria expressions
                         given in the <font face="courier" height="10">referenceExpressions</font> parameter.
             
        :param ProductName: 
                         Identifies the product. It is used in conjunction with parameter <font face="courier" height="10">productNameSpace</font> to resolve potential ambiguity in variant option
                         value names, and to identify product context specific constraints. Teamcenter configurators
                         use a Multiple Field Key (MFK) stable identifier (see property <font face="courier" height="10">Item::fnd0VariantNamespace</font>) of the product item for <font face="courier" height="10">productName</font>. The <font face="courier" height="10">productName</font>
                         value for a Collaborative Design (<b>Cpd0CollaborativeDesign</b>) can be obtained
                         from property <font face="courier" height="10">Mdl0ApplicationModel::mdl0config_product_name.</font>

        :param ProductNameSpace: 
                         Specifies the namespace for the product identifier. It is used in conjunction with
                         parameter <font face="courier" height="10">productName</font> to resolve potential
                         ambiguity in variant option value names, and to identify product context specific
                         constraints. Teamcenter configurators use the Revision ID of the product <b>ItemRevision</b>
                         for <font face="courier" height="10">productNameSpace</font>. The <font face="courier" height="10">productNameSpace</font> value for a Collaborative Design (<b>Cpd0CollaborativeDesign</b>)
                         can be obtained from property <font face="courier" height="10">Mdl0ApplicationModel::mdl0config_prod_namespace.</font>

        :param ConfiguratorURL: 
                         The service end point for the effectivity configurator service. If empty the local
                         Teamcenter configurator is used. Tc10.1 only supports local Teamcenter configurators.
                         In Tc10.1 a non-empty <font face="courier" height="10">configuratorURL</font> parameter
                         will cause an error.
             
        :return: Compares each effectivity expressions with each reference expression and returns
             the degreee of overlap
        """
        ...

