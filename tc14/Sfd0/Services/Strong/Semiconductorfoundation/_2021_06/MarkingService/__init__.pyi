import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class MarkingService:
    """
    Interface MarkingService
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ValidateAndUpdatePanelContent(self, MarkingPanelRev: Teamcenter.Soa.Client.Model.Strong.Sfd0MrkgPanelRevision, DesignType: str, MarkingPattern: str, MarkingValue: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...

