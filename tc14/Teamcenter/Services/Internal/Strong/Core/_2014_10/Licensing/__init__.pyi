import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class LicenseServerInput:
    def __init__(self, ) -> None: ...
    LicenseServer: Teamcenter.Soa.Client.Model.Strong.Fnd0LicenseServer
    LicenseServerName: str
    FailoverLicenseServers: list[Teamcenter.Soa.Client.Model.Strong.Fnd0LicenseServer]
    HostName: str
    PortNumber: int
    Protocol: int

class Licensing:
    def __init__(self , *args: typing.Any) -> None: ...
    def UpdateLicenseServer(self, InputObjects: list[LicenseServerInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

