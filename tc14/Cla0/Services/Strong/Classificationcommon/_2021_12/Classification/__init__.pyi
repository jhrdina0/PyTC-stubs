import Teamcenter.Soa.Client.Model
import typing

class Classification:
    """
    Interface Classification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ImportClassificationData(self, FileTicket: str, RelativePathToClsDataFile: str, ProcessAsAsync: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

