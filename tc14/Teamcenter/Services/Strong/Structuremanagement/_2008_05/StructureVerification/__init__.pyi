import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AlignmentCheckResponse:
    """
    This structure provides response of the call.
    """
    def __init__(self, ) -> None: ...
    PropertyList: list[str]
    """the property list used in this alignment check"""
    Results: list[AlignmentCheckResult]
    """the mismatched BOM lines"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Partial errors"""

class BOMLinePair:
    """
    This structure provides a pair of BOM lines.
    """
    def __init__(self, ) -> None: ...
    Source: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """the source BOM line"""
    Target: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """the target BOM line"""

class AlignmentCheckResult:
    """
    This structure provides information about the alignment check in a given scope.
    """
    def __init__(self, ) -> None: ...
    Scope: BOMLinePair
    """the pair of scope BOM lines"""
    Mismatches: list[AlignmentMismatches]
    """the mismatched BOM lines"""

class AlignmentMismatches:
    """
    This structure provides information about a pair of mismatched lines.
    """
    def __init__(self, ) -> None: ...
    MismatchedAlignment: BOMLinePair
    """the pair of mismatched BOM lines"""
    Mismatchedproperties: list[int]
    """the indices of mismatched properties"""

class StructureVerification:
    """
    Interface StructureVerification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CheckAlignment(self, Input: list[BOMLinePair]) -> AlignmentCheckResponse:
        """    
             An alignment connects two occurrences that are to be considered equivalent. They
             are referred to as source and target. An alignment can connect one source to multiple
             targets. Alignment can be used to transfer data from source to target. An alignment
             check is used to determine if the source and target of an alignment have matching
             data.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         The source ebom and the target mbom structures.
             
        :return: contains ServiceData along with vector of AlignmentCheckResponse
        """
        ...

