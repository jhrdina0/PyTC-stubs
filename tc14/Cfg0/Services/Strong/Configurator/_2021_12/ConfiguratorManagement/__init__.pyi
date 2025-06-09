import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ConditionPair:
    """
    
            It contains a Variant Condition pair with intent to validate the configuration with
            each other.
            
    """
    def __init__(self, ) -> None: ...
    LeftConditionExpression: str
    """The Variant Condition as tc_formula with which rightConditionExpression is validated."""
    LeftConditionProductHierarchyPath: str
    """An offset with respect to VariantRule context. This is for future; leave empty."""
    RightConditionExpression: str
    """The Variant Condition as tc_formula with which leftConditionExpression is validated."""
    RightConditionProductHierarchyPath: str
    """An offset with respect to VariantRule context. This is for future; leave empty."""

class ConditionPairCompatibility:
    """
    
            It contains a result from the operation with a list of compatibility for Variant
            Condition pairs and a service data.
            
    """
    def __init__(self, ) -> None: ...
    IsCompatible: list[bool]
    """
            If true, the Variant Condition pair appear in a buildable combinations in the context
            of supplied VariantRule otherwise, Variant Condition pair is not compatible. The
            list of compatibility and  the list of input, that is, Variant Condition pairs will
            be in same sequence.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData containing partial exceptions, if any."""

class ConfiguratorManagement:
    """
    Interface ConfiguratorManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetConditionPairCompatibility(self, VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule, ConditionPairs: list[ConditionPair], ClientCode: str) -> ConditionPairCompatibility: ...

