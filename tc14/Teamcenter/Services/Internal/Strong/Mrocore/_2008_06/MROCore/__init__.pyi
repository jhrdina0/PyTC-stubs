import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class NameOccurrenceInputInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    SelectedPattern: str
    BomLine: Teamcenter.Soa.Client.Model.Strong.NeutralBOMLine

class NameOccurrenceOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    BomLine: Teamcenter.Soa.Client.Model.Strong.NeutralBOMLine

class NameOccurrenceResponse:
    def __init__(self, ) -> None: ...
    NamedOccurrenceOutput: list[NameOccurrenceOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SetupDeviationOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Relation: Teamcenter.Soa.Client.Model.Strong.AllowedDeviation

class SetupDeviationPhysInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    ParentPhysicalPartImpl: Teamcenter.Soa.Client.Model.Strong.PhysicalPart
    ChildPhysicalPartImpl: Teamcenter.Soa.Client.Model.Strong.PhysicalPart
    SelectedDocument: Teamcenter.Soa.Client.Model.Strong.Item

class SetupDeviationResponse:
    def __init__(self, ) -> None: ...
    Output: list[SetupDeviationOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MROCore:
    def __init__(self , *args: typing.Any) -> None: ...
    def NameOccurrence(self, NameOccurrenceInputInfo: list[NameOccurrenceInputInfo]) -> NameOccurrenceResponse: ...
    def SetupDeviation(self, SetupDeviationPhysInput: list[SetupDeviationPhysInput]) -> SetupDeviationResponse: ...

