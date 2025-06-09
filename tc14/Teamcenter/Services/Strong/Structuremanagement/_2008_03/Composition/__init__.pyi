import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AssignChildLineOccTypes:
    """
    
This structure defines child lines to be assigned with its occurrence type and
client
id.
    """
    def __init__(self, ) -> None: ...
    LineToAssign: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """lineToAssign"""
    OccType: str
    """occurrence type for new assigned line. it can be empty."""

class AssignChildLinesOutput:
    """
    Holds the response from assignChildLines
    """
    def __init__(self, ) -> None: ...
    NewLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """new BOMLines created as a result of assign operation under newParentLine"""
    LinesWithoutPreds: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """a subset new bomlines that do have incoming flows."""

class AssignChildLinesParameter:
    """
    This structure provides a set of input values for assignLines operation.
    """
    def __init__(self, ) -> None: ...
    NewParentLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """new parent line under which the bomlines need to be assigned"""
    LinesToAssign: list[AssignChildLineOccTypes]
    """Array of AssignChildLineOccType"""
    CopyPreds: bool
    """should predecessor relationship be copied over from old parent?"""
    CopyOccTypeFromSource: bool
    """occurrence type to be used for newly assigned lines."""

class AssignChildLinesResponse:
    """
    Holds the response from assignChildLines
    """
    def __init__(self, ) -> None: ...
    AssignOutput: list[AssignChildLinesOutput]
    """array of AssignChildLinesOutput"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Exceptions from internal processing returned as PartialErrors"""

class Composition:
    """
    Interface Composition
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AssignChildLines(self, Input: list[AssignChildLinesParameter]) -> AssignChildLinesResponse:
        """    Assign lines from one or more parent to a new parent line.
        :param Input: 
                         BomLines to be assigned from one or more parent  to new parent line
             
        :return: including newLines, lines without predecessors and exceptions.
        """
        ...

