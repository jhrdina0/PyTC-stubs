import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DeleteNamedVariantExpressions:
    def __init__(self, ) -> None: ...
    ArchRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    Code: list[Teamcenter.Soa.Client.Model.Strong.NamedVariantExpression]

class GetMultipleNVEResponse:
    def __init__(self, ) -> None: ...
    ANves: list[Teamcenter.Soa.Client.Model.Strong.NamedVariantExpression]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetSVRInfo:
    def __init__(self, ) -> None: ...
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    SvrData: list[SVRData]

class GetSVRResponse:
    def __init__(self, ) -> None: ...
    ASVRs: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MultipleNamedVariantExpressions:
    def __init__(self, ) -> None: ...
    ArchRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    IgnoreDuplicates: bool
    NveInfo: list[NamedVariantExpressionsInfo]

class NamedVariantExpressionsInfo:
    def __init__(self, ) -> None: ...
    Code: str
    Desc: str
    VarCondition: Teamcenter.Soa.Client.Model.ModelObject

class SVRData:
    def __init__(self, ) -> None: ...
    VarRule: Teamcenter.Soa.Client.Model.ModelObject
    Name: str
    Desc: str
    Relation: str
    Option: list[Teamcenter.Soa.Client.Model.ModelObject]
    Value: list[str]

class VariantManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateMultipleNamedVariantExpressions(self, Input: MultipleNamedVariantExpressions) -> GetMultipleNVEResponse: ...
    def CreateSavedVariantRules(self, Input: GetSVRInfo) -> GetSVRResponse: ...
    def DeleteMultipleNamedVariantExpressions(self, Input: DeleteNamedVariantExpressions) -> Teamcenter.Soa.Client.Model.ServiceData: ...

