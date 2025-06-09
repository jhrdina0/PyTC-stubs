import System
import Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ApplyBOMVariantRulesResponse2:
    """
    It contains list of variant rules applied to a BOM window.
    """
    def __init__(self, ) -> None: ...
    Rules: list[BOMVariantRuleContents2]
    """A list of BOMVariantRuleContents2 object associated with the BOMWidow"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Object of service data, that returns partial errors."""
    Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """BOMWindow object on which rules have been applied"""

class BOMVariantRuleContents2:
    """
    
Contains variant rule, the saved variant rules associated with the window, list
of
option value details and a boolean flag for constraints evaluation status.

In getBOMVariantRules2 operation, this structure used as output.

In setBOMVariantRule2 operation, this structure used as input as well as output.
As input, it contains details of variant rule, saved variant rule, saved variant
rule modification flag and list of options that needs to be set on variant rule.
As output, it contains details of variant rule with set option values.

In applyBOMVariantRules2 operation, this structure used as input as well as
output.
Typically the variantRule, svr, isSVRModified provide input and list of
BOMVariantOptionValueEntry
and isConstraintsEvaluated are used for output.

Constraints (defaults, derived defaults and rule check) will only be evaluated
for
single variant rule having single option value.
    """
    def __init__(self, ) -> None: ...
    VariantRule: Teamcenter.Soa.Client.Model.ModelObject
    """VariantRule with which window has been configured. This cannot be NULL."""
    Svr: Teamcenter.Soa.Client.Model.ModelObject
    """
            Saved variant rule with which window has been configured. This will be NULL if window
            is not configured with saved variant rule.
            """
    IsSVRModified: bool
    """True, if saved variant rule has been modified."""
    BomVariantOptionValueEntry: list[Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.BOMVariantOptionValueEntry]
    """List of options associated with VariantRule."""
    IsConstraintsEvaluated: bool
    """True, if default, derived default have been evaluated."""

class BOMVariantRuleOutput2:
    """
    
Contains window and the list of rule associated with window. It has the
identifier
to map input variant rule to output variant rule.
    """
    def __init__(self, ) -> None: ...
    Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """The BOMWindow on which rules are set."""
    Rules: list[BOMVariantRuleContents2]
    """A list of BOMVariantRuleContents2 objects."""
    ClientId: str
    """Identifier to map input variant rules to output variant rules."""

class BOMVariantRulesResponse2:
    """
    List of varaint rule data associated with window.
    """
    def __init__(self, ) -> None: ...
    VariantRuleData: list[BOMVariantRuleOutput2]
    """A list of BOMVariantRuleOutput2 object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Object of service data."""

class SetBOMVariantRuleData2:
    """
    
Contains information about window and variant rule that needs to be set on the
window.
This structure will be used as an input and as an output. Input contains details
of window and BOMVariantRuleContents2 that needs to be set on window. Output
contains
details of BOMVariantRuleContents2 having information about option values set on
the variant rule.
    """
    def __init__(self, ) -> None: ...
    Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """A BOMWindow object on which variant rules are to be set."""
    Rules: list[BOMVariantRuleContents2]
    """
            A list of BOMVariantRuleContents2 object which contain details of Variant Rule and
            list of options and values.
            """
    ClientId: str
    """Identifier string to map input variant rule to output variant rule."""

class SetBOMVariantRulesResponse2:
    """
    SetBOMVariantRulesResponse2 object reference.
    """
    def __init__(self, ) -> None: ...
    VariantRuleData: list[SetBOMVariantRuleData2]
    """A list of objects containing SetBOMVariantRuleData2 object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Object of service data that that returns partial errors."""

class VariantManagement:
    """
    Interface VariantManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetBOMVariantRules2(self, VariantRuleInput: list[Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.GetBOMVariantRuleInput]) -> BOMVariantRulesResponse2: ...
    def SetBOMVariantRules2(self, SetBOMVariantRuleInput: list[SetBOMVariantRuleData2]) -> SetBOMVariantRulesResponse2: ...
    def ApplyBOMVariantRules2(self, Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow, Rules: list[BOMVariantRuleContents2]) -> ApplyBOMVariantRulesResponse2: ...

