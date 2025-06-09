import Cae0.Services.Strong.Simproc._2017_05.SimStructureManagement
import System
import Teamcenter.Soa.Client.Model.Strong
import typing

class StructureMapInputsInfo2:
    def __init__(self, ) -> None: ...
    RootBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    SelectedBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    Domain: str
    StructureMapIR: Teamcenter.Soa.Client.Model.Strong.StructureMapRevision

class SimStructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteStructureMapOnSelection(self, StructureMapInputs: StructureMapInputsInfo2) -> Cae0.Services.Strong.Simproc._2017_05.SimStructureManagement.StructureMapExecutionResponse: ...

