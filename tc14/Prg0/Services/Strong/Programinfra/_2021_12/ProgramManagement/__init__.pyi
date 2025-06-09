import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ProgramManagement:
    """
    Interface ProgramManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def MoveEvents(self, Events: list[Teamcenter.Soa.Client.Model.Strong.Prg0AbsEvent], NewEventDate: System.DateTime, UpdateSecondaryEvents: bool, RunInBackground: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

