import Fnd0.Services.Strong.Uiconfig._2014_11.UiConfig
import System
import Teamcenter.Soa.Client.Model
import typing

class ResetUIConfigInput:
    def __init__(self, ) -> None: ...
    Scope: Fnd0.Services.Strong.Uiconfig._2014_11.UiConfig.ScopeInput
    ColumnConfigIds: list[str]

class ResetUIConfigResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    ColumnConfigurations: list[Fnd0.Services.Strong.Uiconfig._2014_11.UiConfig.ColumnConfig]

class UiConfig:
    def __init__(self , *args: typing.Any) -> None: ...
    def ResetUIConfigs(self, ResetUiConfigsIn: list[ResetUIConfigInput]) -> ResetUIConfigResponse: ...

