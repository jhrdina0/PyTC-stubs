import System
import Teamcenter.Soa.Client.Model
import typing

class CheckBriefcaseLicenseResponse:
    def __init__(self, ) -> None: ...
    LicenseExists: bool
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetBriefcaePreviewDataResponse:
    def __init__(self, ) -> None: ...
    OldBriefcasePreviewDataFMSTicket: str
    NewBriefcasePreviewDataFMSTIcket: str
    DeltaBriefcasePreviewFMSTicket: str
    OldBriefcasePreviewData: list[NamesAndValues]
    NewBriefcasePreviewData: list[NamesAndValues]
    DeltaBriefcasePreviewData: list[NamesAndValues]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class NamesAndValues:
    def __init__(self, ) -> None: ...
    ElementName: str
    ElementValues: list[str]

class Briefcase:
    def __init__(self , *args: typing.Any) -> None: ...
    def CheckBriefcaseLicense(self) -> CheckBriefcaseLicenseResponse: ...
    def GetBriefcasePreviewData(self, OldBriefcaseFMSTicket: str, OldBriefcaseUID: str, NewBriefcaseFMSTicket: str, NewBriefcaseUID: str, OptionNamesAndValues: list[NamesAndValues]) -> GetBriefcaePreviewDataResponse: ...

