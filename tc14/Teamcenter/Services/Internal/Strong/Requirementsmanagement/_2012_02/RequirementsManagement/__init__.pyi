import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class TraceabilityMatrixInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    SourceLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    TargetLine: Teamcenter.Soa.Client.Model.Strong.BOMLine

class TraceabilityMatrixOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    TraceabilityMap: System.Collections.Hashtable

class TraceabilityMatrixResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    Output: list[TraceabilityMatrixOutput]

class TraceabilityMatrixStructure:
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    Relations: list[Teamcenter.Soa.Client.Model.Strong.ImanRelation]

class RequirementsManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetTraceabilityMatrix(self, Inputs: list[TraceabilityMatrixInfo]) -> TraceabilityMatrixResponse: ...

