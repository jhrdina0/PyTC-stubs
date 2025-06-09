import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class VolumeInfoResponse:
    def __init__(self, ) -> None: ...
    AccessibleVolumes: list[Teamcenter.Soa.Client.Model.Strong.ImanVolume]
    DefaultVolume: Teamcenter.Soa.Client.Model.Strong.ImanVolume
    DefaultLocalVolume: Teamcenter.Soa.Client.Model.Strong.ImanVolume
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class VolumeManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAccessibleVolumes(self, User: Teamcenter.Soa.Client.Model.Strong.User, Group: Teamcenter.Soa.Client.Model.Strong.Group) -> VolumeInfoResponse: ...

