import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class EmailInfo:
    def __init__(self, ) -> None: ...
    Subject: str
    MessageBody: str
    ListOfRecipients: list[Teamcenter.Soa.Client.Model.ModelObject]
    ListOfCcRecipients: list[Teamcenter.Soa.Client.Model.ModelObject]
    ListOfExtRecipients: list[str]
    ListOfExtCcRecipients: list[str]
    FmsReadTickets: list[str]
    Sender: Teamcenter.Soa.Client.Model.Strong.User
    ClientID: str

class Envelope:
    def __init__(self , *args: typing.Any) -> None: ...
    def SendEmail(self, Emailinfos: list[EmailInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

