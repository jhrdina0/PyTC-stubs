import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DeriveResponse:
    def __init__(self, ) -> None: ...
    ActivityLog: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class HighlightModelResponse:
    def __init__(self, ) -> None: ...
    HighlightModelMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SimStructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateDerivedStructures(self, RootBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine, SelectedRule: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision, SelectedVarConfig: str, VarConfigDetails: str, NumOfStructs: int, OptionalRootName: str, OptionalIndex: str, UseAutoIndex: bool) -> DeriveResponse: ...
    def HighlightModelStructure(self, ModelRoot: Teamcenter.Soa.Client.Model.Strong.BOMLine) -> HighlightModelResponse: ...

