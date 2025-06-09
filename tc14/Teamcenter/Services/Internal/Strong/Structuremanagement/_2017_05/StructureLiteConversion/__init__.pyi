import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ClassicBOMLineInfo:
    def __init__(self, ) -> None: ...
    InputLWBIndex: int
    ConvertedBOMLine: Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject
    LwbChildren: list[Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject]

class ConversionResponse:
    def __init__(self, ) -> None: ...
    ConvertedBOMLines: list[ClassicBOMLineInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class StructureLiteConversion:
    def __init__(self , *args: typing.Any) -> None: ...
    def LiteBOMLinesToBOMLines(self, LinesToConvert: list[Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject]) -> ConversionResponse: ...

