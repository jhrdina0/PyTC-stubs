import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ApplyBOMVariantRulesResponse:
    """
    It contains list of variant rules applied on the window.
    """
    def __init__(self, ) -> None: ...
    Rules: list[BOMVariantRuleContents]
    """List of  BOMVariantRuleContents object associated with the BOMWidow"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Object of service data, that returns partial errors."""
    Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """BOMWindow object on which rules have been applied"""

class BOMVariantOptionValueEntry:
    """
    
It contains details of option, its description and values associated with that
particular
option.
    """
    def __init__(self, ) -> None: ...
    Option: Teamcenter.Soa.Client.Model.Strong.Variant
    """Variant object that contains details of option value."""
    OwningItem: Teamcenter.Soa.Client.Model.Strong.Item
    """Item on which option is set."""
    OptionName: str
    """Name of the option associated with Item"""
    OptionDesc: str
    """Additional information about option"""
    VariantOptionValue: list[VariantOptionValue]
    """
            List containing options and configuration details
            
"""

class BOMVariantRuleContents:
    """
    
BOMVariantRuleContents contains variant rule, the saved variant rules associated
with the window,   list of option value details and a boolean flag for
constraints
evaluation status.

In getBOMVariantRules operation , this structure used as output.

In setBOMVariantRule operation, this structure used as input as well as output.
As input, it contains details of variant rule, saved variant rule, saved variant
rule modification flag and list of options that needs to be set on variant rule.
As output, it contains details of variant rule with set option values.

In applyBOMVariantRules operation, this structure used as input as well as
output. Typically the variantRule, svr, isSVRModified provided as input and
list
of BOMVariantOptionValueEntry and isConstraintsEvaluated are part of output.

Constraints (defaults, derived defaults and rule check) will only be evaluated
for
single variant rule having single option value.

    """
    def __init__(self, ) -> None: ...
    VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule
    """VariantRule with which window has been configured. This cannot be NULL"""
    Svr: Teamcenter.Soa.Client.Model.ModelObject
    """
            Saved variant rule with which  window has been configured. This will be NULL if window
            is not configured with saved variant rule.
            """
    IsSVRModified: bool
    """True, if saved variant rule has been modified."""
    BomVariantOptionValueEntry: list[BOMVariantOptionValueEntry]
    """List of options associated with VariantRule"""
    IsConstraintsEvaluated: bool
    """True, if default, derived default have been evaluated"""

class BOMVariantRuleOutput:
    """
    
BOMVariantRuleOutput contains window and the list of rule associated with
            window. It has the identifier to map input variant rule to output
variant rule.
    """
    def __init__(self, ) -> None: ...
    Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """BOMWindow on which rules are set"""
    Rules: list[BOMVariantRuleContents]
    """List of  BOMVariantRuleContents  objects"""
    ClientId: str
    """Identifier to map input variant rules to output variant rules."""

class BOMVariantRulesResponse:
    """
    List of varaint rule data associated with window.
    """
    def __init__(self, ) -> None: ...
    VariantRuleData: list[BOMVariantRuleOutput]
    """List of  BOMVariantRuleOutput  object"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Object of service data."""

class GetBOMVariantRuleInput:
    """
    
It contains information about window and saved variant rules which user want to
add,
delete, update or override.
    """
    def __init__(self, ) -> None: ...
    Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """BOMWindow object for which variant rule is being requested."""
    VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule
    """The variant rule for which the contents are requested."""
    Svrs: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            List of saved variant rules which user want to add, unset, update or override. It
            is optional.
            """
    ClientId: str
    """
            unique identifier for each window. Output will have same identifier, to let caller
            know, which rule list is associated with which window.
            """
    SvrActionMode: int
    """
            This flag indicates different action mode associated to SVRs which includes  add
            (add new saved variant rule), unset (unset existing saved variant rule), update (update
            configuration using saved variant rule), override (override configuration using saved
            variant rule).
            

0     Set this value, when you want to get variant rule
            from window(default value).
            
1      Set this value, when you want to apply or add new
            saved variant rule in case of multiple rule scenario
            
2      Set this value, when you want to unset existing
            saved variant rule in case of multiple rule scenario.
            
3     Set this mode, if user wants to override existing
            option value in saved variant rule.
            
4     Set this mode, if user wants to update existing
            option value in saved variant rule.
            
"""

class GetVariantExpressionsMatchInfoResponse:
    """
    The response of method getVariantExpressionsMatchInfo.
    """
    def __init__(self, ) -> None: ...
    VariantExpressionsDetails: list[VariantExpressionsDetails]
    """The entries in this list corresponds to each input InputBOMLinesSet."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The partial errors."""

class InputBOMLinesSet:
    """
    The list of roll up BOMLine objects and non-roll up BOMLine objects.
    """
    def __init__(self, ) -> None: ...
    RollUpBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """
            The list of BOMLine objects for which rolled up variant conditions and rolled up
            clause lists  to be calculated. If this list is empty, then this operation will populate
            the variant expressions for the nonRollUPBOMLines and their corresponding clause
            lists in the response.
            """
    NonRollUpBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """
            The list of BOMLine objects for which occurrence variant conditions and clause lists
            to be returned. If this list is empty, , then this operation will populate the rolled
            up variant expressions and corresponding clause lists in the response.
            """
    DoCompare: bool
    """
            If true, the comparison will be peformed between all the input bomLines i.e. rollUpBOMLines
            and nonRollUpBOMLines till a mismatch is found.
            """

class SetBOMVariantRuleData:
    """
    
SetBOMVariantRuleData contains information about window and variant rule that
            needs to be set on the window. This structure will be used as an
input and as an
            output. Input contains details of  window and BOMVariantRuleContents
that needs
            to be set on window . Output contains details of
BOMVariantRuleContents  having information
            about option values set on the variant rule.
    """
    def __init__(self, ) -> None: ...
    Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """BOMWindow object on which variant rules will be set"""
    Rules: list[BOMVariantRuleContents]
    """
            A list of BOMVariantRuleContents  object which contain details of Variant Rule and
            list of options and values.
            """
    ClientId: str
    """Identifier to map input variant rule to output variant rule"""

class SetBOMVariantRulesResponse:
    """
    SetBOMVariantRulesResponse object reference.
    """
    def __init__(self, ) -> None: ...
    SetBOMVariantRuleData: list[SetBOMVariantRuleData]
    """List of  objects containing setBOMVariantRuleData  object"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Object of service data that that returns partial errors"""

class VariantExpressionClauseList:
    """
    Contains clauseList object and corresponding clause list text.
    """
    def __init__(self, ) -> None: ...
    ClauseListText: list[str]
    """
            The text representation of the clauseList. If the line does not have the variant
            condition then this list will be empty.
            """
    ClauseList: Teamcenter.Soa.Client.Model.ModelObject
    """
            The clauseList object of the VarientExpression. If the line does not have the variant
            condition then corresponding entry in this list will be null.
            """

class VariantExpressionsDetails:
    """
    
The VariantExpressionsDetails represents response for each input
InputBOMLinesSet.
It contains clause List and corresponding clause List text for rollUpBOMLines
and
nonRollUpBOMLines.
    """
    def __init__(self, ) -> None: ...
    RollUpClauseList: list[VariantExpressionClauseList]
    """
            The rolled up clause list object and clauseListText for the BOMLine objects in the
            rollUpBomLines list. Each entry in this list corresponds to one BOMLine in rollUpBomLines
            list.
            """
    NonRollUpClauseList: list[VariantExpressionClauseList]
    """The clause lists for the BOMLines objects in the nonRollUpBomLines list."""
    IsDifferent: bool
    """
            True if the input doCompare flag is set and any of the BOMLines of the inputBOMLinesSets
            are different due to variant conditions.
            """

class VariantOptionValue:
    """
    Details of option values.
    """
    def __init__(self, ) -> None: ...
    Value: str
    """Value assigned to option"""
    HowSet: str
    """
            Indicates, how value is set. Possible values are
            

    Unset  value is unset,
            
    Unset (potentially derived)  derivable
            value is unset,
            
    Derived  value is from derived option
            value  ,
            
    Defaulted  value from default option
            value,
            
    Set by User  value is set by user,
            
    Set by Rule  value is set by rule,
            
    Variant Item  value set by variant
            item
            

"""
    HowSetInt: int
    """
            It indicates how value is set. It is integer representation of  howSet.
            
            Valid values are as follows.
            
0  value is unset,
            
1  derivable value is unset,
            
2  value is from derived option value  ,
            
3  value from default option value,
            
4  value is set by user,
            
5  value is set by rule,
            
8  value set by variant item.
            
"""
    WhereSet: str
    """Name of saved variant rule given by user or name of the owningItem"""
    Index: int
    """Position of option value in variant revision"""
    IsConfiguredOptionValue: bool
    """If rule is configured with particular option value."""

class VariantManagement:
    """
    Interface VariantManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetVariantExpressionsMatchInfo(self, InputBOMLinesSets: list[InputBOMLinesSet]) -> GetVariantExpressionsMatchInfoResponse:
        """    
             This operation calculates and returns the rolledup variant expressions and rolledUp
             clause lists for the input rollUpBomLines. For the nonRolledUpBomLines, BOMLine variant
             conditions and clause lists will be returned. . If doCompare parameter is set as
             true, then this operation compares the equivalent lines based on the variant conditions
             and sets the isDifferent variable accordingly. The lines in input rollUpBomLines,
             will be compared using the rolled up variants and the lines in the nonRollUpBomLines
             list will be compared using variant conditions. All the lines in one InputBOMLinesSet
             will be compared with each other till a difference is found.
             

Teamcenter Component:

             Options & Variants - Modular and Legacy - Capability to specify variabilty (options)
             on a product structure and be able to define multiple variants and solve for a specific
             configuration.
             
        :param InputBOMLinesSets: 
                         The list of roll up BOMLine objects and non-roll up BOMLine objects.
             
        :return: A list VariantExpressionsDetails, one for each request input and serviceData for
             partial errors. The following partial errors may be returned: 1. 214506: An error
             has occurred while retrieving the variant expression match information for the input
             BOM Line set "%1$". 2. 46217: An error has occurred while calculating the Rollup
             Variant Condition for the BOM Line.
        """
        ...
    def GetBOMVariantRules(self, VariantRuleInput: list[GetBOMVariantRuleInput]) -> BOMVariantRulesResponse:
        """    
             This operation takes list of window and its identifier and returns variant rules
             and saved variant rules associated with the window. As part of input in this operation
             user can provide saved variant rule along with saved variant rule action mode. This
             action indicates add, remove, update or override actions related to saved variant
             rule. There could be multiple variant rules, associated with window. List of these
             rules will be returned as the output. It also returns list of option and list of
             values associated with each option.  A flag in the value list indicates, if window
             is configured with the particular option value.  There could be multiple values associated
             with a single option and there could be multiple saved variant rules associated with
             a window.
             

Use Cases:

             This operation should be used when user wants to get variant rules associated with
             window. User may also use it to set , unset, override or update saved variant rule
             based on the window mode
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param VariantRuleInput: 
                         List of window for which variant rules are being requested
             
        :return: 
        """
        ...
    def SetBOMVariantRules(self, SetBOMVariantRuleInput: list[SetBOMVariantRuleData]) -> SetBOMVariantRulesResponse:
        """    
             This operation set the input variant rule to the window and returns the list of variant
             rule and respective window.
             

Use Cases:

             This operation should be used when user want to set values of the option on variant
             rule.
             

Dependencies:

             getBOMVariantRules
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param SetBOMVariantRuleInput: 
                         List of input object containing variant rule and window on which rule will be set.
             
        :return: This operation returns variant rule and details of option values that is set to window.
        """
        ...
    def ApplyBOMVariantRules(self, Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow, Rules: list[BOMVariantRuleContents]) -> ApplyBOMVariantRulesResponse:
        """    
             The applyBOMVariantRules operation applies either given BOM variant rules or Saved
             Variant Rules to the window. BOM Variant rules that contain options having multiple
             values can be applied to the window. Output will be the window and list of BOM variant
             rules and Saved Variant Rules have been applied to the window.
             

Use Cases:

             This operation will be used when BOM variant rules or Saved Variant Rules needs to
             be applied on the window.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param Window: 
<b>BOMWindow</b> object on which variant rules will be applied.
             
        :param Rules: 
                         This input has a list of BOMVariantRuleContents which contain details of variant
                         rule and list of options and values
             
        :return: This operation returns list of  BomVariantRuleContents object which contains details
             of option values that is applied to window. If multiple saved variant rules set on
             the window or options having multiple values then constraints  (defaults and derived
             defaults and rule check) will not be evaluated.
        """
        ...

