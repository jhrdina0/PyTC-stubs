import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class LicenseServerInput2:
    def __init__(self, ) -> None: ...
    LicenseServerName: str
    HostName: str
    LicenseServerType: str
    PortNumber: int
    Protocol: int
    LicenseServer: Teamcenter.Soa.Client.Model.Strong.Fnd0LicenseServer
    FailoverLicenseServers: list[Teamcenter.Soa.Client.Model.Strong.Fnd0LicenseServer]
    MultipleLicenseServers: list[Teamcenter.Soa.Client.Model.Strong.Fnd0LicenseServer]

class Licensing:
    def __init__(self , *args: typing.Any) -> None: ...
    def UpdateLicenseServer2(self, InputObjects: list[LicenseServerInput2]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

