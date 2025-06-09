import System
import Teamcenter.Services.Strong.Documentmanagement._2010_04.DigitalSignature
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CheckOutForSignResponse:
    def __init__(self, ) -> None: ...
    Verdict: list[bool]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DigitalSignature:
    def __init__(self , *args: typing.Any) -> None: ...
    def DigitalSigningSaveTool(self, SaveInput: Teamcenter.Services.Strong.Documentmanagement._2010_04.DigitalSignature.DigitalSignSaveInput) -> Teamcenter.Services.Strong.Documentmanagement._2010_04.DigitalSignature.DigtalSigningSaveResponse: ...
    def CancelSign(self, InputDatasets: list[Teamcenter.Soa.Client.Model.Strong.Dataset]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def IsCheckOutForSign(self, InputDatasets: list[Teamcenter.Soa.Client.Model.Strong.Dataset]) -> CheckOutForSignResponse: ...

