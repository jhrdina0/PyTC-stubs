import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class MaturityData:
    """
    Structure containing the result of maturity check and other relevant information
    """
    def __init__(self, ) -> None: ...
    EvaluatedObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The BusinessObject on which rules are evaluated. For example, a BOMLine from the
            structure is a valid object on which certain rules are evaluated.
            """
    RuleResults: System.Collections.Hashtable
    """
            Map containing the result of the evaluation. The key of the map is uid of the rule
            and value of the map is list of PropertyData containing the result of the evaluation
            along with relevant data.
            

            The valid propertyName members of the PropertyData is:
            


status:  Specifies the status of the evaluation. Valid values of
            status are "Pass", "Fail", "Partial" and "NA" (Not Applicable).  "Pass" signifies
            that rule on evaluatedObject is passed, "Fail" signifies failed, "Partial" signifies
            partially passed and "NA" signifies that the rule is not applicable for the evaluated
            object.
            
statusDisplayValue: Display value of the rule evaluated on the object.
            It may not be same as outcome of rule.
            
ruleUID: uid of the rule
            

"""
    ObjectLevelStatus: list[PropertyData]
    """
            Overall result and status of evaluated object.
            

            The valid propertyName member of the PropertyData is:
            


status:  Specifies the status of the evaluation. Valid values of
            status are "Pass", "Fail" and "Partial".  "Pass" signifies that all rules on evaluatedObject
            passed, "Fail" signifies that all rules failed and "Partial" signifies that some
            rule passed. Rules that are not applicable for the evaluated object are ignored for
            determining the overall status of the object.
            

"""

class MaturityReportRequest:
    """
    
The input object to service. It contains below parameters -

inputObjects -Â Â Â Â The input contains the BOMLine which acts as
a scope for maturity check. The objects in the hierarchy of the scope are
candidates
for the check.

ruleList -Â Â Â Â The list of rules for which maturity is to be evaluated.
Some of the rules may not be applicable to all objects in the scope.

supportingInformation -Â Â Â Â Additional supporting information
that could be used to evaluate the maturity. Currently this input is not used by
the operation.

    """
    def __init__(self, ) -> None: ...
    InputObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of BOMLine for which the maturity report is required. All objects in the hierarchy
            of the line are evaluated for the maturity check.
            """
    SelectedRules: System.Collections.Hashtable
    """
            A list of rules to evaluate the maturity. The
            
            key and value (string, list(PropertyData)) of the map are uid of the rule and corresponding
            data respectively. The latter is list of structure PropertyData which has property
            name of the rule and data of that property respectively. The valid property name
            is "ruleUID" with value as UID of the rule.
            

            The rule in the list may be applicable to specific object type. The operation fetches
            those objects for a given scope and evaluates the rule. Both evaluated objects and
            status of the evaluation is reported in the response.
            

            For any two rules from the list, one may evaluate an object type different than that
            of another.
            """
    SupportingInformation: list[PropertyData]
    """
            Additional supporting information required to evaluate the maturity.
            
            Currently this input is not used by operation.
            """

class MaturityReportResponse:
    """
    
The response is  the map containing maturity data and the service data. The map
contains
the evaluated object and its maturity status along with additional information
related
to checks. The evaluated objects type may not be of same type and may not be
applicable
to all the rules specified in input of the operation.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data containing partial errors."""
    MaturityResult: System.Collections.Hashtable
    """
            The result of getMaturityData operation, contains BusinessObjects and their maturity
            data.
            """

class PropertyData:
    """
    The detail information of the data in the form of property and its value.
    """
    def __init__(self, ) -> None: ...
    PropertyName: str
    """Key to identify the data in the collection."""
    Value: list[str]
    """Value of the property."""
    DataType: str
    """
            Type of the data. It can be "boolean", "character", "date", "float", "double", "integer",
            "string" and "businessObject".
            """

class Validation:
    """
    Interface Validation
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetMaturityReport(self, MaturityReportRequest: MaturityReportRequest) -> MaturityReportResponse:
        """    
             This service operation evaluates the maturity of the structure based on certain rules.
             The operation executes  specified rules on objects of the structure and returns if
             the rules are fulfilled or not. The operation takes  BOMLine as a scope to evaluate
             the maturity of objects under it, the list of rules to evaluate the maturity, and
             supporting information. In response the operation returns the objects and their maturity
             status along with other relevant information.
             

Use Cases:

             Use Case 1 - User checks maturity of a structure.
             
                 User can check the maturity of structure by right clicking
             on root or topline of the structure. Consider a Logistic structure consisting of
             logistics bill of process (LBOP), part family, parts under the part family and in-plant
             supply chain. User needs to know if all part families have part specified or if all
             part families have at least one in-plant supply chain or if all parts have at least
             one in-bound supply chain. User can choose the predefined rules and use this operation
             to evaluate the rules on part family and in response see a maturity report.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param MaturityReportRequest: 
                         supportingInformation -Â Â Â Â Additional supporting information
                         that could be used to evaluate the maturity. Currently this input is not used by
                         the operation.
             
        :return: 
        """
        ...

