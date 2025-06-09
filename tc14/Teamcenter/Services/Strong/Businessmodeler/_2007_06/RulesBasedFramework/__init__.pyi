import System
import Teamcenter.Soa.Client.Model
import typing

class ExecuteRbfRulesResponse:
    """
    
            Holds the response for the executeRbfRules
            operation.
            
    """
    def __init__(self, ) -> None: ...
    Outputs: list[RbfNameValue]
    """This is a set of output name/value pairs from the rules engine execution."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """This contains the status of the operation."""

class RbfValue:
    """
    The value for an input or output column on an Application Extension Rule.
    """
    def __init__(self, ) -> None: ...
    DataType: str
    """
            The type of data the structure is holding. It will have one of the following values:
             STRING, BOOLEAN, INTEGER, DOUBLE, FLOAT, DATE,
            or TAG.
            """
    StringValue: str
    """The STRING value for the column."""
    BooleanValue: bool
    """The BOOLEAN value for the column."""
    IntegerValue: int
    """The INTEGER value for the column."""
    DoubleValue: float
    """The DOUBLE value for the column."""
    FloatValue: float
    """The FLOAT value for the column."""
    DateValue: System.DateTime
    """The DATE value for the column."""
    TagValue: Teamcenter.Soa.Client.Model.ModelObject
    """The TAG value for the column."""

class RbfNameValue:
    """
    
            The name of the input or output column along with the data value on a application
            extension rule.
            
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The input or output column name from the application extension rule."""
    Value: RbfValue
    """The value of the named column."""

class RulesBasedFramework:
    """
    Interface RulesBasedFramework
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteRbfRules(self, Id: str, Inputs: list[RbfNameValue]) -> ExecuteRbfRulesResponse:
        """    
             This operation invokes the CLIPS rules engine to apply the set of application extension
             rules that belong to the specified application extension point for the specified
             input name/value pairs.  The result of the execution is returned in the output name/value
             pairs.
             

Teamcenter Component:

             BMIDE (Server) - Set of services provided by BMIDE that allow efficiently underyling
             capabilities to develop/modify business objects
             
        :param Id: 
                         The application extension point ID for which this application extension rule is configured.
             
        :param Inputs: 
                         A set of input name/value pairs for the rules engine execution.
             
        :return: 
        """
        ...

