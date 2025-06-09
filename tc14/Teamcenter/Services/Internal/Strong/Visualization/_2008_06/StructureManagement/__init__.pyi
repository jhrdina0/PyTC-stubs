import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AreRecipesMergableInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    RecipeObj: Teamcenter.Soa.Client.Model.ModelObject
    Topline: Teamcenter.Soa.Client.Model.ModelObject
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow

class AreRecipesMergableOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    IsMergable: bool

class AreRecipesMergableResponse:
    def __init__(self, ) -> None: ...
    Output: list[AreRecipesMergableOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class CreateBOMsFromRecipesInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    RecipeObj: Teamcenter.Soa.Client.Model.ModelObject
    Topline: Teamcenter.Soa.Client.Model.ModelObject

class CreateBOMsFromRecipesOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow

class CreateBOMsFromRecipesResponse:
    def __init__(self, ) -> None: ...
    Output: list[CreateBOMsFromRecipesOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class CreateVisSCsFromBOMsInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    OccurrencesList: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    StaticStructureFile: Teamcenter.Soa.Client.Model.ModelObject

class CreateVisSCsFromBOMsOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    StructureRecipe: Teamcenter.Soa.Client.Model.Strong.VisStructureContext

class CreateVisSCsFromBOMsResponse:
    def __init__(self, ) -> None: ...
    Output: list[CreateVisSCsFromBOMsOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ExpandPSData:
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    ObjectOfBOMLine: Teamcenter.Soa.Client.Model.ModelObject
    RelatedObjects: list[ExpandPSRelatedObjectInfo]

class ExpandPSFromOccurrenceListInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    Occurrences: list[OccurrenceListInfo]

class ExpandPSFromOccurrenceListOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    OccurrenceList: list[OccurrenceListResults]

class ExpandPSFromOccurrenceListPref:
    def __init__(self, ) -> None: ...
    WantDatasets: bool
    Info: list[RelationAndTypesFilter]

class ExpandPSFromOccurrenceListResponse:
    def __init__(self, ) -> None: ...
    Output: list[ExpandPSFromOccurrenceListOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ExpandPSNamedReferenceInfo:
    def __init__(self, ) -> None: ...
    NamedReferenceType: str
    NamedReferenceName: str
    ReferenceObject: Teamcenter.Soa.Client.Model.ModelObject
    FileTicket: str

class ExpandPSParentData:
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    ObjectOfBOMLine: Teamcenter.Soa.Client.Model.ModelObject
    ParentRelatedObjects: list[ExpandPSRelatedObjectInfo]

class ExpandPSRelatedObjectInfo:
    def __init__(self, ) -> None: ...
    RelatedObject: Teamcenter.Soa.Client.Model.ModelObject
    NamedRefList: list[ExpandPSNamedReferenceInfo]

class OccurrenceChain:
    def __init__(self, ) -> None: ...
    ClientId: str
    OccurrenceChainStr: list[str]

class OccurrenceChainList:
    def __init__(self, ) -> None: ...
    ClientId: str
    ParentBomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    OccurrenceList: list[OccurrenceChain]

class OccurrenceChainResult:
    def __init__(self, ) -> None: ...
    ClientId: str
    OccurrenceChain: list[ExpandPSData]

class OccurrenceListInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    AttributeNames: list[str]
    OccurrenceChainsByParent: list[OccurrenceChainList]

class OccurrenceListResults:
    def __init__(self, ) -> None: ...
    ClientId: str
    Parent: ExpandPSParentData
    OccurrenceList: list[OccurrenceChainResult]

class RelatedObjectTypeAndNamedRefs:
    def __init__(self, ) -> None: ...
    RelationTypeName: str
    NamedReferenceNames: list[str]

class RelationAndTypesFilter:
    def __init__(self, ) -> None: ...
    RelationName: str
    RelatedObjAndNamedRefs: list[RelatedObjectTypeAndNamedRefs]
    NamedRefHandler: str

class StructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def AreRecipesMergable(self, Info: list[AreRecipesMergableInfo]) -> AreRecipesMergableResponse: ...
    def CreateBOMsFromRecipes(self, Info: list[CreateBOMsFromRecipesInfo]) -> CreateBOMsFromRecipesResponse: ...
    def CreateVisSCsFromBOMs(self, Info: list[CreateVisSCsFromBOMsInfo]) -> CreateVisSCsFromBOMsResponse: ...
    def ExpandPSFromOccurrenceList(self, Info: list[ExpandPSFromOccurrenceListInfo], Pref: ExpandPSFromOccurrenceListPref) -> ExpandPSFromOccurrenceListResponse: ...

