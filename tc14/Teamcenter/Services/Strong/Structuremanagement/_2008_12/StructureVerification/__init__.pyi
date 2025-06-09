import System
import Teamcenter.Soa.Client.Model
import typing

class AccCheckInput:
    """
    This structure provides a set of input values for accountabilityCheck operation.
    """
    def __init__(self, ) -> None: ...
    SourceTags: list[Teamcenter.Soa.Client.Model.ModelObject]
    """the source BOM lines"""
    TargetTags: list[Teamcenter.Soa.Client.Model.ModelObject]
    """the target BOM lines"""
    Option: int
    """options of search"""
    SrcCtxtLineTag: Teamcenter.Soa.Client.Model.ModelObject
    """the possible source context line"""
    TarCtxtLineTag: Teamcenter.Soa.Client.Model.ModelObject
    """the possible target context line"""
    MatchType: int
    """represents user choice in the color display"""

class AccountabilityCheckResponse:
    """
    This structure provides response of the call
    """
    def __init__(self, ) -> None: ...
    ResultSourceTarget: list[AccountabilityCheckResult]
    """Accountabilty Check result"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Partial errors"""

class AccountabilityCheckResult:
    """
    The structure characterizes compare result for each source line
    """
    def __init__(self, ) -> None: ...
    Source: Teamcenter.Soa.Client.Model.ModelObject
    """the sourse BOM line"""
    Targets: list[Teamcenter.Soa.Client.Model.ModelObject]
    """the target BOM lines"""
    CheckResult: int
    """characterized check result"""

class StructureVerification:
    """
    Interface StructureVerification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AccountabilityCheck(self, Input: AccCheckInput) -> AccountabilityCheckResponse:
        """    
             The operation will call the existing accountability check functions,  which will
             generate a check result for report in the colored display.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         a set of input values
             
        :return: return AccountabilityCheckResponse including lines from source and target windows
             and check result
        """
        ...

