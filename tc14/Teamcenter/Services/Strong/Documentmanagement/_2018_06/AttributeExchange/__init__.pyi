import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttributeExchange:
    """
    Interface AttributeExchange
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def UpdateDocumentProperties(self, InputObjects: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision], CheckConfiguration: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

