import System
import System.Collections
import Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement
import Teamcenter.Soa.Client.Model
import typing

class CleanDynamicIPALinesResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    LogFileTicket: Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement.FileTicketDetails

class DynamicIPAInputInfo:
    def __init__(self, ) -> None: ...
    InputLine: Teamcenter.Soa.Client.Model.ModelObject
    IsRecursive: bool

class DynamicIPALinesResponse:
    def __init__(self, ) -> None: ...
    BopLineToIPALinesMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    LogFileTicket: Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement.FileTicketDetails

class SaveDynamicIPALinesResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    LogFile: Teamcenter.Services.Strong.Manufacturing._2013_05.IPAManagement.FileTicketDetails

class IPAManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CleanDynamicIPALines(self, InputLines: list[DynamicIPAInputInfo]) -> CleanDynamicIPALinesResponse: ...
    def CreateDynamicIPALines(self, InputLines: list[DynamicIPAInputInfo]) -> DynamicIPALinesResponse: ...
    def SaveContentOfDynamicIPALines(self, InputDIPALines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> SaveDynamicIPALinesResponse: ...
    def UpdateDynamicIPALines(self, InputLines: list[DynamicIPAInputInfo]) -> DynamicIPALinesResponse: ...

