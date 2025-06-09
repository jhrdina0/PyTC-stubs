import System
import Teamcenter.Soa.Client.Model
import typing

class CheckinInput:
    def __init__(self, ) -> None: ...
    CiProcess: bool
    IsRecursive: bool

class CheckoutInput:
    def __init__(self, ) -> None: ...
    CoProcess: bool
    IsRecursive: bool
    CoTools: bool
    CoPlant: bool
    CoAssembly: bool
    ChangeId: str
    Reason: str

class Core:
    def __init__(self , *args: typing.Any) -> None: ...
    def CheckinForProcessSimulate(self, RootLines: list[Teamcenter.Soa.Client.Model.ModelObject], Params: CheckinInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CheckoutForProcessSimulate(self, RootLines: list[Teamcenter.Soa.Client.Model.ModelObject], Params: CheckoutInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...

