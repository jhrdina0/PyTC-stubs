import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BasedOnOptionInfo:
    def __init__(self, ) -> None: ...
    BasedOnType: int
    Path: str
    BasedOptionId: int
    OwningModuleKey: str
    OwningOptionName: str

class BOMVariantConfigOutput:
    def __init__(self, ) -> None: ...
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    ConfiguredOptions: list[BOMVariantConfigurationOption]
    DbSOSOrSVR: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject

class BOMVariantConfigOptionResponse:
    def __init__(self, ) -> None: ...
    Output: BOMVariantConfigOutput
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ModularOption:
    def __init__(self, ) -> None: ...
    OptionId: int
    OptionName: str
    OptionDescription: str
    OptionValueType: int
    OptionType: int
    AllowedValues: list[str]
    DefaultValue: str
    OptionScope: int
    MinValues: list[float]
    MaxValues: list[float]
    OperationTypes: list[int]
    BasedOnOption: BasedOnOptionInfo
    MvlDefinitions: list[str]

class ClassicOption:
    def __init__(self, ) -> None: ...
    OptionName: str
    OptionDescription: str
    ItemId: str
    OptionValues: list[str]
    Variant: Teamcenter.Soa.Client.Model.Strong.Variant
    VariantRev: Teamcenter.Soa.Client.Model.Strong.VariantRevision

class BOMVariantConfigurationOption:
    def __init__(self, ) -> None: ...
    VariantType: str
    HowSet: int
    ValueSet: str
    WhereSet: str
    DefaultSet: int
    DefaultValue: str
    ModularOption: ModularOption
    ClassicOption: ClassicOption

class ModularOptions:
    def __init__(self, ) -> None: ...
    Options: list[ModularOption]
    Mvl: str

class ModularOptionsForBomResponse:
    def __init__(self, ) -> None: ...
    OptionsOutput: list[ModularOptionsOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ModularOptionsInfo:
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    Options: ModularOptions

class ModularOptionsInput:
    def __init__(self, ) -> None: ...
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]

class ModularOptionsOutput:
    def __init__(self, ) -> None: ...
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    OptionsInfo: list[ModularOptionsInfo]

class VariantManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetModularOptionsForBom(self, Modules: list[ModularOptionsInput]) -> ModularOptionsForBomResponse: ...
    def GetBOMVariantConfigOptions(self, BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow, BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine) -> BOMVariantConfigOptionResponse: ...

