import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ConfigInput:
    def __init__(self, ) -> None: ...
    SourceDatasetTypeName: str
    DerivedDatasetTypeName: str
    ServiceAvailable: int

class ConfigOutput:
    def __init__(self, ) -> None: ...
    ConfigOutputData: list[ConfigOutputData]
    SvcData: Teamcenter.Soa.Client.Model.ServiceData

class ConfigOutputData:
    def __init__(self, ) -> None: ...
    SvcConfig: list[Teamcenter.Soa.Client.Model.Strong.DispatcherServiceConfig]

class DispatcherManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetConfigurations(self, SvcConfigInput: list[ConfigInput]) -> ConfigOutput: ...

