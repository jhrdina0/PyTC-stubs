import Cae0.Services.Internal.Strong.Simproc._2017_05.SimulationToolLaunch
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExportMaterialResponse:
    def __init__(self, ) -> None: ...
    MaterialExportFile: Teamcenter.Soa.Client.Model.Strong.ImanFile
    MaterialExportLogfile: Teamcenter.Soa.Client.Model.Strong.ImanFile
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ImportObjectsFromPLMXMLResponse2:
    def __init__(self, ) -> None: ...
    LogFileTickets: list[Cae0.Services.Internal.Strong.Simproc._2017_05.SimulationToolLaunch.FileTicket]
    PlmxmlNamedRefPlmdTicketInfoList: list[PLMXMLNamedReferencePlmdTicketInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class NameAndValue:
    def __init__(self, ) -> None: ...
    OptionName: str
    OptionValue: str

class PLMXMLNamedReferencePlmdTicketInfo:
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    AbsoluteFilePath: str
    RefName: str
    PlmdTicket: str

class SimulationToolLaunch:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExportAndCheckoutPLMXMLWithDSM(self, PlmxmlFileName: str, TransferMode: str, ObjectsToExport: list[Teamcenter.Soa.Client.Model.ModelObject], CheckOutOnExport: bool, ToolName: str, LogFileTickets: list[str], SessionOptions: list[NameAndValue]) -> Cae0.Services.Internal.Strong.Simproc._2017_05.SimulationToolLaunch.ExportObjectsToPLMXMLResponse: ...
    def ExportMaterialsForToolLaunch(self, MaterialsObjects: list[Teamcenter.Soa.Client.Model.ModelObject], MaterialExportFileName: str, MaterialExportFilterName: str) -> ExportMaterialResponse: ...
    def ImportAndCheckinPLMXMLwithDSM(self, XmlFileTicket: str, NamedRefFileTickets: list[str], LogFileTickets: list[str], TransferMode: str, CheckInOnImport: bool, PerformCancelCheckOut: bool, SessionOptions: list[NameAndValue]) -> ImportObjectsFromPLMXMLResponse2: ...

