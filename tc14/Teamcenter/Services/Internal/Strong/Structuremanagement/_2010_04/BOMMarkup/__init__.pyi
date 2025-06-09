import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ApplyBOMMarkupParam:
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    Recursive: bool
    Evaluate: bool

class CreateBOMMarkupOutput:
    def __init__(self, ) -> None: ...
    MarkupChange: Teamcenter.Soa.Client.Model.Strong.POM_object
    Markup: Teamcenter.Soa.Client.Model.Strong.POM_object
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine

class CreateBOMMarkupParam:
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    MarkupType: int
    InputObject: Teamcenter.Soa.Client.Model.ModelObject
    Context: Teamcenter.Soa.Client.Model.ModelObject
    PropertyName: str
    PropertyValue: str
    Note: str

class CreateBOMMarkupResponse:
    def __init__(self, ) -> None: ...
    CreateBOMMarkupsList: list[CreateBOMMarkupOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class BOMMarkup:
    def __init__(self , *args: typing.Any) -> None: ...
    def ApplyBOMMarkup(self, Input: list[ApplyBOMMarkupParam]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateBOMMarkup(self, Input: list[CreateBOMMarkupParam]) -> CreateBOMMarkupResponse: ...
    def SavePendingEditsAsMarkup(self, Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow) -> CreateBOMMarkupResponse: ...

