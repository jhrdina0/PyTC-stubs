import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExportConfiguredNXAssemblyInfo:
    def __init__(self, ) -> None: ...
    Bomline: Teamcenter.Soa.Client.Model.Strong.BOMLine
    NamingFormat: str

class ExportConfiguredNXAssemblyOutput:
    def __init__(self, ) -> None: ...
    TransientZipFileReadTicket: str
    TransientLogFileReadTicket: str
    Bomline: Teamcenter.Soa.Client.Model.Strong.BOMLine

class ExportConfiguredNXAssemblyResponse:
    def __init__(self, ) -> None: ...
    Output: list[ExportConfiguredNXAssemblyOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExportConfiguredNXAssembly(self, Inputs: list[ExportConfiguredNXAssemblyInfo]) -> ExportConfiguredNXAssemblyResponse: ...

