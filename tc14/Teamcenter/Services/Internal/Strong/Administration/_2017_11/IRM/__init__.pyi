import System
import Teamcenter.Soa.Client.Model
import typing

class AccessorInformation:
    def __init__(self, ) -> None: ...
    AccessorType: str
    AccessorName: str
    AccessorObject: Teamcenter.Soa.Client.Model.ModelObject

class AccessorsInfoResponse:
    def __init__(self, ) -> None: ...
    AccessorInformations: list[AccessorInformation]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class IRM:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAccessorsInfo(self, AccessorObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> AccessorsInfoResponse: ...

