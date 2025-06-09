import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CAEConfigDetailResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    XmlConfigList: list[str]

class SimProcessConfigurationManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetCAEConfigDetail(self, ConfigItemList: list[Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision]) -> CAEConfigDetailResponse: ...
    def RetrieveConfigurationList(self, InputCriteria: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData: ...

