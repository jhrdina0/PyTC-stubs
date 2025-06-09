import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class WhereUsedOutputOccGroup:
    def __init__(self, ) -> None: ...
    InputObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    Info: list[WhereUsedParentInfoOccGroup]

class WhereUsedParentInfoOccGroup:
    def __init__(self, ) -> None: ...
    ParentOccGroup: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    Level: int

class WhereUsedResponseOccGroup:
    def __init__(self, ) -> None: ...
    Output: list[WhereUsedOutputOccGroup]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def WhereUsedOccGroup(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], NumLevels: int, WhereUsedPrecise: bool, Rule: Teamcenter.Soa.Client.Model.ModelObject) -> WhereUsedResponseOccGroup: ...

