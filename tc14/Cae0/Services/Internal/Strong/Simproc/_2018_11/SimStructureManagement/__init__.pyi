import Cae0.Services.Internal.Strong.Simproc._2017_11.SimStructureManagement
import Cae0.Services.Strong.Simproc._2017_05.SimStructureManagement
import Teamcenter.Soa.Client.Model
import typing

class StructureMapFilterInclusionRuleInfo:
    def __init__(self, ) -> None: ...
    InclusionRuleFileTicket: str
    InclusionRuleFileItemRevName: str
    InclusionRuleFileItemRevDesc: str
    SelectedInclusionRuleItemRev: Teamcenter.Soa.Client.Model.ModelObject

class SimStructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteStructMapWithInclusionRule(self, StructureMapInputs: Cae0.Services.Internal.Strong.Simproc._2017_11.SimStructureManagement.StructureMapInputsInfo2, InclusionRuleInputs: StructureMapFilterInclusionRuleInfo) -> Cae0.Services.Strong.Simproc._2017_05.SimStructureManagement.StructureMapExecutionResponse: ...

