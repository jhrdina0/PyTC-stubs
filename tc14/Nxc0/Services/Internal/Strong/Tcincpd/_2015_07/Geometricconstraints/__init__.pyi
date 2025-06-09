import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ConstraintContainerInfo:
    def __init__(self, ) -> None: ...
    Owner: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    Iteration: int
    LatestIteration: int
    IsLatestIterationWorking: bool
    MemberList: list[Membership]
    ConstraintData: Teamcenter.Soa.Client.Model.Strong.Dataset
    NameReferenceTicketMap: System.Collections.Hashtable
    AreConstraintsFullySolved: bool
    SystemManaged: bool

class ContainerToCheckInputInfo:
    def __init__(self, ) -> None: ...
    Owner: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    Iteration: int

class ElementToCheckInputInfo:
    def __init__(self, ) -> None: ...
    InputElement: Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement
    PendingChecksum: list[str]
    PendingTransform: list[float]

class GetContainersUpToDateStatusResponse:
    def __init__(self, ) -> None: ...
    ContainerUpToDate: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetUpToDateStatusResponse:
    def __init__(self, ) -> None: ...
    UpToDate: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Membership:
    def __init__(self, ) -> None: ...
    Member: Teamcenter.Soa.Client.Model.Strong.POM_object
    Csid: str
    IsForeground: bool

class NavigationOptions:
    def __init__(self, ) -> None: ...
    Mode: str
    ConfigContextObject: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext

class UpToDateResult:
    def __init__(self, ) -> None: ...
    ElementStatus: bool
    OutOfDateGeometricConstraintContainers: list[ConstraintContainerInfo]

class Geometricconstraints:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetContainersUpToDateStatus(self, Containers: list[ContainerToCheckInputInfo], NavOptions: NavigationOptions, LinearTolerance: float, AngularTolerance: float) -> GetContainersUpToDateStatusResponse: ...
    def GetUpToDateStatus(self, Inputs: list[ElementToCheckInputInfo], NavOptions: NavigationOptions, LinearTolerance: float, AngularTolerance: float) -> GetUpToDateStatusResponse: ...

