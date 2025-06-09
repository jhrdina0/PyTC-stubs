import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ConfigurationRosterCoverage:
    def __init__(self, ) -> None: ...
    JsonResponse: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ConfigurationRosterInput:
    def __init__(self, ) -> None: ...
    Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective
    JsonRequest: str

class ConfiguratorManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetConfigurationRosterCoverage(self, ConfigurationRoster: ConfigurationRosterInput) -> ConfigurationRosterCoverage: ...

