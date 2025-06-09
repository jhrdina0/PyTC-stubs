import Cfg0.Services.Internal.Strong.Configurator._2015_10.ConfiguratorManagement
import Cfg0.Services.Strong.Configurator._2014_12.ConfiguratorManagement
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetModelOptionCondInput:
    def __init__(self, ) -> None: ...
    ConfigPerspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective
    InputExpressions: list[Cfg0.Services.Internal.Strong.Configurator._2015_10.ConfiguratorManagement.ApplicationConfigExpression]

class GetModelOptionCondOutput:
    def __init__(self, ) -> None: ...
    Index: int
    ModelOptionCondList: list[ModelOptionCondStruct]

class GetModelOptionCondResponse:
    def __init__(self, ) -> None: ...
    ModelOptionCondOutputList: list[GetModelOptionCondOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ModelOptionCondStruct:
    def __init__(self, ) -> None: ...
    ModelExpressions: list[Cfg0.Services.Internal.Strong.Configurator._2015_10.ConfiguratorManagement.ApplicationConfigExpression]
    OptionConditions: list[Cfg0.Services.Internal.Strong.Configurator._2015_10.ConfiguratorManagement.ApplicationConfigExpression]

class OverlapStateInfo:
    def __init__(self, ) -> None: ...
    Index: int
    OverlapStates: list[str]

class OverlapStateInput:
    def __init__(self, ) -> None: ...
    ReferenceExpression: Cfg0.Services.Internal.Strong.Configurator._2015_10.ConfiguratorManagement.ApplicationConfigExpression
    Expressions: list[Cfg0.Services.Internal.Strong.Configurator._2015_10.ConfiguratorManagement.ApplicationConfigExpression]

class OverlapStateResponse:
    def __init__(self, ) -> None: ...
    OverlapInfo: list[OverlapStateInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class UpdateAdmissibilityData:
    def __init__(self, ) -> None: ...
    AdmissibilityObject: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsAdmissibility
    AdmissibilityState: str

class UpdateAdmissibilityInputList:
    def __init__(self, ) -> None: ...
    UpdateAdmissibilityInputs: list[UpdateAdmissibilityInputStruct]

class UpdateAdmissibilityInputStruct:
    def __init__(self, ) -> None: ...
    ContextObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    UpdateAdmissibilityData: list[UpdateAdmissibilityData]

class ConfiguratorManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetModelAndOptionConditions(self, OperationConfigPerspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, InputStructs: list[GetModelOptionCondInput]) -> GetModelOptionCondResponse: ...
    def GetOverlapStates(self, Context: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, OverlapStateInputs: list[OverlapStateInput]) -> OverlapStateResponse: ...
    def UpdateAdmissibility(self, UpdateAdmissibilityInputList: list[UpdateAdmissibilityInputList]) -> Cfg0.Services.Strong.Configurator._2014_12.ConfiguratorManagement.GetAdmissibilityResponse: ...

