import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ColumnSet:
    def __init__(self, ) -> None: ...
    Column: list[Column]
    Table: str

class RowSet:
    def __init__(self, ) -> None: ...
    Row: list[Row]

class RowColumn:
    def __init__(self, ) -> None: ...
    ColumnSet: ColumnSet
    RowSet: RowSet

class AlignmentResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    UpdatedItemRowSet: RowColumn
    ItemsToRemove: list[str]

class BomLineType:
    def __init__(self, ) -> None: ...
    ClientID: str
    Design: Teamcenter.Soa.Client.Model.Strong.BOMLine

class Column:
    def __init__(self, ) -> None: ...
    Name: str
    Datatype: str
    Table: str
    LogicalName: str
    Width: int

class DesignType:
    def __init__(self, ) -> None: ...
    ClientID: str
    Design: Teamcenter.Soa.Client.Model.Strong.ItemRevision

class PartAlignmentInputType:
    def __init__(self, ) -> None: ...
    PmmInputObject: RowColumn
    UpdateAndAlignInfo: list[UpdateAndAlignDesignInfoType]
    Operation: str
    Authorization: str
    AutoCommit: bool

class PmmObjectUpdateInfoType:
    def __init__(self, ) -> None: ...
    Field: System.Collections.Hashtable
    Tuid: str
    ClientID: str
    RelatedObjectUpdate: list[RelatedObjectUpdateInfoType]

class RelatedObjectType:
    def __init__(self, ) -> None: ...
    Action: str
    Tuid: str
    Field: System.Collections.Hashtable

class RelatedObjectUpdateInfoType:
    def __init__(self, ) -> None: ...
    Table: str
    RelatedObjects: list[RelatedObjectType]

class Row:
    def __init__(self, ) -> None: ...
    Value: list[str]
    ClientID: str

class SolutionAlignmentInputType:
    def __init__(self, ) -> None: ...
    PmmInputObject: RowColumn
    UpdateAndAlignInfo: list[UpdateAndAlignBomLineInfoType]
    Operation: str
    Authorization: str
    AutoCommit: bool

class UpdateAndAlignBomLineInfoType:
    def __init__(self, ) -> None: ...
    PmmObjectUpdateInfo: PmmObjectUpdateInfoType
    Designs: list[BomLineType]

class UpdateAndAlignDesignInfoType:
    def __init__(self, ) -> None: ...
    PmmObjectUpdateInfo: PmmObjectUpdateInfoType
    Designs: list[DesignType]

class AlignmentManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def AlignCadOccsWithSolutions(self, AlignmentInput: SolutionAlignmentInputType) -> AlignmentResponse: ...
    def AlignDesignsWithParts(self, AlignmentInput: PartAlignmentInputType) -> AlignmentResponse: ...

