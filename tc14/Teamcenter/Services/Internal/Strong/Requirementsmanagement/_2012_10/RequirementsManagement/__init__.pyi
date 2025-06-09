import System
import Teamcenter.Services.Internal.Strong.Requirementsmanagement._2012_02.RequirementsManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class MatchedLineData:
    def __init__(self, ) -> None: ...
    MatchedLine: Teamcenter.Soa.Client.Model.ModelObject
    TopLine: Teamcenter.Soa.Client.Model.ModelObject

class MatchedLineOutput:
    def __init__(self, ) -> None: ...
    RevObject: Teamcenter.Soa.Client.Model.ModelObject
    MatchedLineData: list[MatchedLineData]

class MatchedLineResponse:
    def __init__(self, ) -> None: ...
    MatchedOutput: list[MatchedLineOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MatchLineInputData:
    def __init__(self, ) -> None: ...
    RevObject: Teamcenter.Soa.Client.Model.ModelObject
    ScopeTopLines: list[Teamcenter.Soa.Client.Model.ModelObject]

class TraceabilityMatrixInfo1:
    def __init__(self, ) -> None: ...
    ClientId: str
    SourceLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    TargetLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    FilterFormat: str
    FilterTypes: list[str]

class RequirementsManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetMatchingLines(self, Inputs: list[MatchLineInputData]) -> MatchedLineResponse: ...
    def GetTraceabilityMatrix(self, Inputs: list[TraceabilityMatrixInfo1]) -> Teamcenter.Services.Internal.Strong.Requirementsmanagement._2012_02.RequirementsManagement.TraceabilityMatrixResponse: ...

