import System
import Teamcenter.Soa.Client.Model
import typing

class ConditionInput:
    """
    
            Holds the name of the condition to be evaluated along with the set of input parameter
            business object values.
            
    """
    def __init__(self, ) -> None: ...
    ConditionName: str
    """This is the name of the condition to be evaluated."""
    ConditionSignature: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            This is set of condition parameters (tag_t) required by the specified condition
            name.
            """

class ConditionOutput:
    """
    
            Holds the results of a condition evaluation along with any exit code that was captured
            during the condition evaluation.
            
    """
    def __init__(self, ) -> None: ...
    Result: bool
    """This is the result of the rules engine evaluation (True or False)."""
    ExitCode: int
    """
            This is the exit code (zero for success or non zero indicating an error) captured
            during the condition evaluation.
            """

class EvaluateConditionsResponse:
    """
    
            Holds the response for the evaluateConditions
            operation.
            
    """
    def __init__(self, ) -> None: ...
    Outputs: list[ConditionOutput]
    """This is a set of condition evaluation results from the rules engine execution."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """This contains the status of the operation."""

class ConditionEngine:
    """
    Interface ConditionEngine
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def EvaluateConditions(self, Inputs: list[ConditionInput]) -> EvaluateConditionsResponse:
        """    
             This operation tells the CLIPS rules engine to evaluate the expression defined on
             the specified Condition using the specified input parameter(s) defined on
             the ConditionParameter.  This operation takes as input a set of conditions
             along with parameters for each condition and returns a set of outputs containing
             the result (true/false) and exit code of each condition evaluation. There is a one
             to one correspondence between the elements in the input set and the elements in the
             output set.  This allows for evaluation of multiple conditions in one operation call.
             

Teamcenter Component:

             BMIDE (Server) - Set of services provided by BMIDE that allow efficiently underyling
             capabilities to develop/modify business objects
             
        :param Inputs: 
                         This is a set of condition(s) along with the corresponding input parameter value(s)
                         for each condition.
             
        :return: 
        """
        ...

