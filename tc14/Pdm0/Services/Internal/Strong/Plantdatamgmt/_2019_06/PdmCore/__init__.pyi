import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class IsMilestoneActivityInProgressRes:
    def __init__(self, ) -> None: ...
    IsMileStoneActivityInProgress: list[bool]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PdmCore:
    def __init__(self , *args: typing.Any) -> None: ...
    def IsMilestoneActivityInProgress(self, Plants: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel]) -> IsMilestoneActivityInProgressRes: ...

