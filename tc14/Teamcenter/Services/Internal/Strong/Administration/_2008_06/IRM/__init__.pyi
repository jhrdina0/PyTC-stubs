import Teamcenter.Soa.Client.Model
import typing

class ACLInfoResponse:
    def __init__(self, ) -> None: ...
    AclNameInfos: list[ACLNameInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ACLNameInfo:
    def __init__(self, ) -> None: ...
    AclObject: Teamcenter.Soa.Client.Model.ModelObject
    AclName: str

class IRM:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetACLsByType(self, AclsType: int) -> ACLInfoResponse: ...

