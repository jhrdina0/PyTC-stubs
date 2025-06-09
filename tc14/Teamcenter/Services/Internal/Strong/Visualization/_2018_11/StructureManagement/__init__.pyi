import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class EffectivityInfo:
    def __init__(self, ) -> None: ...
    EffectivityUnitNo: int
    EffectivityDate: System.DateTime
    EndItem: Teamcenter.Soa.Client.Model.ModelObject

class GetProductStructureIdResponse:
    def __init__(self, ) -> None: ...
    PsIdInfos: list[ProductStructureIdInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ProductAndConfigInfo:
    def __init__(self, ) -> None: ...
    Product: Teamcenter.Soa.Client.Model.ModelObject
    RevisionRule: Teamcenter.Soa.Client.Model.ModelObject
    EffectivityInfos: list[EffectivityInfo]
    VariantInfos: list[VariantRuleInfo]

class ProductStructureIdInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    ProductStrutureIdentifier: str
    ProductAndConfig: ProductAndConfigInfo
    RevRuleInfo: list[RevRuleInfo]

class ProductStructureIdInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    RecipeObject: Teamcenter.Soa.Client.Model.ModelObject
    ProductAndConfig: ProductAndConfigInfo

class RevRuleInfo:
    def __init__(self, ) -> None: ...
    RevRuleEntryNames: list[str]
    EffectivityExpr: str
    VariantExpr: str
    RevRuleDate: System.DateTime
    Context: str

class VariantRuleInfo:
    def __init__(self, ) -> None: ...
    VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule
    VariantRuleOwningObject: Teamcenter.Soa.Client.Model.ModelObject

class StructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetStructureIdFromRecipe(self, ProductStructureIdInput: list[ProductStructureIdInput]) -> GetProductStructureIdResponse: ...

