import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateMultilevelSVConfigParam:
    def __init__(self, ) -> None: ...
    ConfigCriteria: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsConfiguratorCriteria
    ConfigPreferences: System.Collections.Hashtable

class CreateSVItemDescriptor:
    def __init__(self, ) -> None: ...
    BoName: str
    StringProps: System.Collections.Hashtable
    StringListProps: System.Collections.Hashtable
    DoubleProps: System.Collections.Hashtable
    DoubleListProps: System.Collections.Hashtable
    FloatProps: System.Collections.Hashtable
    FloatListProps: System.Collections.Hashtable
    IntProps: System.Collections.Hashtable
    IntListProps: System.Collections.Hashtable
    BoolProps: System.Collections.Hashtable
    BoolListProps: System.Collections.Hashtable
    DateProps: System.Collections.Hashtable
    DateListProps: System.Collections.Hashtable
    BoProps: System.Collections.Hashtable
    BoListProps: System.Collections.Hashtable
    CompoundCreateSVItemDescriptor: System.Collections.Hashtable

class CreateSVItemInfo:
    def __init__(self, ) -> None: ...
    CreateSVItemDesc: CreateSVItemDescriptor
    SvCategoryType: int

class CreateSVItemInput:
    def __init__(self, ) -> None: ...
    GenericBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    CreateSVItemInfo: CreateSVItemInfo

class CreateMultilevelSVInput:
    def __init__(self, ) -> None: ...
    CreateSVItemInput: CreateSVItemInput
    MappedSVBOMLineUID: str

class CreateMultilevelSVOutput:
    def __init__(self, ) -> None: ...
    GenericBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    NewSVBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    StatusInfo: str

class CreateMultilevelSVResponse:
    def __init__(self, ) -> None: ...
    CreatMultilevelSVOutputList: list[CreateMultilevelSVOutput]
    ExpandedBOMLineMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class CreateSVItemOutput:
    def __init__(self, ) -> None: ...
    GenericBomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    NewVariantItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    AlreadyExists: bool

class CreateSVItemResponse:
    def __init__(self, ) -> None: ...
    CreateSVItemOutput: list[CreateSVItemOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class LoadSVItemResponse:
    def __init__(self, ) -> None: ...
    LoadSVItemsOutputList: list[LoadSVItemsOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class LoadSVItemsOutput:
    def __init__(self, ) -> None: ...
    SvItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    SvItemPropsMap: System.Collections.Hashtable

class SearchParameter:
    def __init__(self, ) -> None: ...
    SearchConfigCriteria: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsConfiguratorCriteria
    SvCategories: int
    SearchPreferences: System.Collections.Hashtable

class SearchSVItemOutput:
    def __init__(self, ) -> None: ...
    SourceBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    UnloadedSVItemObjectsUIDList: System.Collections.Hashtable
    IntialSVItemOutputList: list[LoadSVItemsOutput]

class SearchSVItemsResponse:
    def __init__(self, ) -> None: ...
    SearchSVItemOutputList: list[SearchSVItemOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SolutionVariantManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateMultilevelSolutionVariants(self, CreateMultilevelSVInputList: list[CreateMultilevelSVInput], CreateMultilevelSVConfigParam: CreateMultilevelSVConfigParam) -> CreateMultilevelSVResponse: ...
    def CreateSolutionVariantItems(self, CreateSVItemInputList: list[CreateSVItemInput], ConfigCriteria: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsConfiguratorCriteria) -> CreateSVItemResponse: ...
    def LoadSolutionVariantItems(self, SvItemObjectsToBeLoadedList: System.Collections.Hashtable) -> LoadSVItemResponse: ...
    def SearchSolutionVariantItems(self, SourceBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], SearchParameter: SearchParameter) -> SearchSVItemsResponse: ...

