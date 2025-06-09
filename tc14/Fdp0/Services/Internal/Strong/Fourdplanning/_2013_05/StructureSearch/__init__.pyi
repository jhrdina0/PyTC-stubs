import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttributeValues:
    def __init__(self, ) -> None: ...
    BoolValues: list[bool]
    IntValues: list[int]
    DoubleValues: list[float]
    StringValues: list[str]
    DateValues: System.DateTime
    TagValues: list[Teamcenter.Soa.Client.Model.ModelObject]

class AttributeExpression:
    def __init__(self, ) -> None: ...
    ClassName: str
    AttributeName: str
    AttributeType: str
    QueryOperator: str
    Values: AttributeValues

class BoxZoneExpression:
    def __init__(self, ) -> None: ...
    SearchBoxes: list[SearchBox]
    BoxOperator: str

class DateCriteria:
    def __init__(self, ) -> None: ...
    Date: System.DateTime
    ObjectTag: Teamcenter.Soa.Client.Model.ModelObject
    Type: str

class FormAttributeExpression:
    def __init__(self, ) -> None: ...
    IsItemForm: bool
    RelationType: Teamcenter.Soa.Client.Model.ModelObject
    FormType: Teamcenter.Soa.Client.Model.ModelObject
    AttributeName: str
    AttributeType: str
    QueryOperator: str
    Values: AttributeValues

class FourDExpressionSet:
    def __init__(self, ) -> None: ...
    DateCriteria: list[DateCriteria]
    SearchCriteriaMap: System.Collections.Hashtable

class SearchBySizeExpression:
    def __init__(self, ) -> None: ...
    LargerThan: bool
    DiagonalLength: bool

class SearchExpressionSet:
    def __init__(self, ) -> None: ...
    ItemAndRevisionAttributeExpressions: list[AttributeExpression]
    OccurrenceNoteExpressions: list[OccurrenceNoteExpression]
    FormAttributeExpressions: list[FormAttributeExpression]
    ProximitySearchExpressions: list[ProximityExpression]
    BoxZoneExpressions: list[BoxZoneExpression]
    PlaneZoneExpressions: list[PlaneZoneExpression]
    SavedQueryExpressions: list[SavedQueryExpression]
    InClassQueryExpressions: list[InClassExpression]
    SizeSearchExpression: SearchBySizeExpression
    DoTrushapeRefinement: bool
    ReturnScopedSubTreesHit: bool

class FourDSearchInputInfo:
    def __init__(self, ) -> None: ...
    ProcessScope: list[Teamcenter.Soa.Client.Model.ModelObject]
    ProductScope: list[Teamcenter.Soa.Client.Model.ModelObject]
    SearchExpression: SearchExpressionSet
    FourDExpression: FourDExpressionSet

class FourDSearchResultResponse:
    def __init__(self, ) -> None: ...
    ResultMap: System.Collections.Hashtable
    FindLinesInProcStructure: bool
    ObjectDone: int
    EstimatedObjectsLeft: int
    PercentComplete: float
    SearchCursor: Teamcenter.Soa.Client.Model.ModelObject
    Finished: bool
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class InClassExpression:
    def __init__(self, ) -> None: ...
    InClassClassNames: list[str]
    InClassAttributeIDs: list[int]
    InClassAttributeValues: list[str]

class ObjectOccChainPair:
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    OccChain: str

class OccurrenceNoteExpression:
    def __init__(self, ) -> None: ...
    NoteType: str
    QueryOperator: str
    Values: list[str]

class PlaneZone:
    def __init__(self, ) -> None: ...
    Xvalue: float
    Yvalue: float
    Zvalue: float
    Displacement: float

class PlaneZoneExpression:
    def __init__(self, ) -> None: ...
    PlaneZone: PlaneZone
    PlaneZoneOperator: str

class ProximityExpression:
    def __init__(self, ) -> None: ...
    BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    Distance: float
    IncludeChildBomLines: bool

class SavedQueryExpression:
    def __init__(self, ) -> None: ...
    SavedQuery: Teamcenter.Soa.Client.Model.ModelObject
    Entries: list[str]
    Values: list[str]

class SearchBox:
    def __init__(self, ) -> None: ...
    Xmin: float
    Ymin: float
    Zmin: float
    Xmax: float
    Ymax: float
    Zmax: float
    Transform: list[float]

class StructureSearch:
    def __init__(self , *args: typing.Any) -> None: ...
    def NextFourDSearch(self, Input: FourDSearchInputInfo, FindLinesInProcStructure: bool, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> FourDSearchResultResponse: ...
    def StartFourDSearch(self, Input: FourDSearchInputInfo) -> FourDSearchResultResponse: ...
    def StopFourDSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> FourDSearchResultResponse: ...

