import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetVerificationRulesResponse:
    """
    The response information returned by getVerificationRules.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData object  which contains generic information like error number
            and error information.
            """
    Outputs: list[VerificationRulesInfo]
    """The list of VerificationRule objects information."""

class VerificationRuleInput:
    """
    The criteria to get VerificationRule objects.
    """
    def __init__(self, ) -> None: ...
    Functionality: str
    """
            The desired value of the functionality property of the VerificationRule
            objects.
            """
    ConditionName: str
    """
            The desired value of the condition_reference property of the VerificationRule
            objects.
            """
    TypeName: str
    """
            The desired value (business object type name) of the type property of the
            VerificationRule objects.
            """
    SubGroup: str
    """
            The desired value of the subGroup property of the VerificationRule
            objects. It should be the value of LOV in subGroupLOV  property of FunctionalityRule
            object associated with the VerificationRule object.
            """

class VerificationRulesInfo:
    """
    
            The returned VerificationRule objects and it associated VerificationRuleInput
            index.
            
    """
    def __init__(self, ) -> None: ...
    Index: int
    """
            The index of VerificationRuleInput in parameter vector that this list of rules
            is associated with.
            """
    VerificationRules: list[Teamcenter.Soa.Client.Model.Strong.VerificationRule]
    """The list of VerificationRule objects which match the desired criteria."""

class BusinessRules:
    """
    Interface BusinessRules
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetVerificationRules(self, Input: list[VerificationRuleInput]) -> GetVerificationRulesResponse:
        """    
             This operation gets a list of VerificationRule objects which match the given
             criteria each VerificationRuleInput supplied and its context_filter
             attribute which refers to a Condition object defined in Business Modeler
             IDE equals to true; Wild cards can be specified in strings using * in VerificationRuleInput
             which mean to match all cases for the criteria strings. This operation not only returns
             all VerificationRule objects which full match criteria in VerificationRuleInput,
             it also returns VerificationRule objects whose type attribute is the
             parent of the typeName defined in the VerificationRuleInput, meanwhile
             other criteria are matched.
             

Use Cases:

             4 samples Verification Rules created in Business Modeler IDE

             {Functionality= Fnd0BOMGrading, Business Object=Item, Context Filter =isTrue, Condition
             Rule=Condition1, Sub Group=*}
             
             {Functionality= Fnd0BOMGrading, Business Object=Part, Context Filter = isEngineeringGroup,
             Condition Rule=Condition1, Sub Group=*}
             
             {Functionality= Fnd0BOMGrading, Business Object= CommericalPart, Context Filter =isTrue,
             Condition Rule=Condition2, Sub Group= Americas}
             
             {Functionality= Fnd0APS, Business Object=Item, Context Filter =isTrue, Condition
             Rule=Condition1, Sub Group= *}
             
             Login Teamcenter as dba group and get VerificationRule objects by setting
             functionality as Fnd0BOMGrading and typeName as CommericalPart. Following
             VerificationRule objects in will be returned.
             
             {Functionality= Fnd0BOMGrading, Business Object=Item, Context Filter =isTrue, Condition
             Rule=Condition1, Sub Group=*}
             
             {Functionality= Fnd0BOMGrading, Business Object= CommericalPart, Context Filter =isTrue,
             Condition Rule=Condition2, Sub Group=Americas}
             
             The first rule applies to Item, if Condition1 could check Item, it
             could check CommericalPart, since CommericalPart is a sub type of Item
             and it is sure that CommericalPart contains all properties checked in Condition1,
             so it is valid. The second rule applies to all CommericalPart, so it is also
             valid. The other VerificationRule objects either do not match functionality
             or typeName, or else context_filter equals to false.
             

Teamcenter Component:

             BMIDE (Server) - Set of services provided by BMIDE that allow efficiently underyling
             capabilities to develop/modify business objects
             
        :param Input: 
                         The criteria for filtering the list of <b>VericationRule</b> objects.
             
        :return: objects.
        """
        ...

