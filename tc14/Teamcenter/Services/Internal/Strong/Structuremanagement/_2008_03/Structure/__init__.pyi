import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ReSequenceParameter:
    def __init__(self, ) -> None: ...
    BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    StartNumber: int
    IncreNumber: int
    Recursive: bool

class Structure:
    def __init__(self , *args: typing.Any) -> None: ...
    def Resequence(self, Input: list[ReSequenceParameter]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

