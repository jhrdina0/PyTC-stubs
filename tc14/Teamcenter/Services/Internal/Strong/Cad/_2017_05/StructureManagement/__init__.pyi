import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ArrangementID:
    def __init__(self, ) -> None: ...
    ArrangeName: str
    ArrangeSubfileid: str

class ArrJtOverride:
    def __init__(self, ) -> None: ...
    JtDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    JtFile: Teamcenter.Soa.Client.Model.Strong.ImanFile
    JtFileName: str
    FileTicket: str

class ArrAbsOccDataOverride:
    def __init__(self, ) -> None: ...
    OccurrenceThreadPath: list[str]
    OverrideTypes: int
    AbsTransform: list[float]
    Suppression: bool
    UsedArrangement: ArrangementID
    JtOverride: ArrJtOverride

class ArrangementData:
    def __init__(self, ) -> None: ...
    ArrangeType: int
    ArrangeID: ArrangementID
    OccData: list[ArrOccurrenceData]

class ArrOccurrenceData:
    def __init__(self, ) -> None: ...
    OccurrenceThread: str
    OccTransform: list[float]
    AbsOccOverrides: list[ArrAbsOccDataOverride]

class GetProductStructureArrangementsResp:
    def __init__(self, ) -> None: ...
    ArrOutput: list[ProductStructureArrOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class LWBStructureInput:
    def __init__(self, ) -> None: ...
    LwbWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    LwbLines: list[Teamcenter.Soa.Client.Model.Strong.Fnd0BOMLineLite]

class ProductStructureArrangementInput:
    def __init__(self, ) -> None: ...
    Bvrs: list[Teamcenter.Soa.Client.Model.Strong.PSBOMViewRevision]
    LwbStructures: LWBStructureInput

class ProductStructureArrangementsOutput:
    def __init__(self, ) -> None: ...
    Bvr: Teamcenter.Soa.Client.Model.Strong.PSBOMViewRevision
    Line: Teamcenter.Soa.Client.Model.Strong.Fnd0BOMLineLite
    ArrangeData: list[ArrangementData]

class ProductStructureArrOutput:
    def __init__(self, ) -> None: ...
    PsArrOutput: list[ProductStructureArrangementsOutput]

class StructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetProductStructureArrangements(self, PsArrInput: list[ProductStructureArrangementInput]) -> GetProductStructureArrangementsResp: ...

