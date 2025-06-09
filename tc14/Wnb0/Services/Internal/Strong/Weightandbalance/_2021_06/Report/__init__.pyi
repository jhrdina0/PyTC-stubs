import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CurveInfo:
    def __init__(self, ) -> None: ...
    CurveName: str
    CurvePoints: str

class GetPayloadExcursionPlotInfoResp:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    CurveInfos: list[CurveInfo]
    EnvelopeInfo: CurveInfo

class Report:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPayloadExcursionPlotInfo(self, RollupDataset: Teamcenter.Soa.Client.Model.Strong.Dataset) -> GetPayloadExcursionPlotInfoResp: ...

