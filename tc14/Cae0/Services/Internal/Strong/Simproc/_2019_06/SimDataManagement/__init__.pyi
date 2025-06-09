import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class SimDataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ImportCAEData(self, ZipFileTickets: list[str], SelectedFolder: Teamcenter.Soa.Client.Model.Strong.Folder, IsAsync: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

