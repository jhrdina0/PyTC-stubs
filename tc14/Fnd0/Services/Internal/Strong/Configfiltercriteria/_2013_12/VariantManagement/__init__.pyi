import Teamcenter.Soa.Client.Model
import typing

class ConfiguratorServiceResponse:
    def __init__(self, ) -> None: ...
    ResponseData: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class VariantManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteConfiguratorService(self, InputXMLString: str, ConfiguratorURL: str) -> ConfiguratorServiceResponse: ...

