import Ods0.Services.Internal.Strong.Objectdataservices._2020_04.ObjectDataServices
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class Expression2:
    def __init__(self, ) -> None: ...
    Operands: list[OperandAndOperator]
    ExpressionOperator: str

class FilteredObject2:
    def __init__(self, ) -> None: ...
    FilteredObj: Teamcenter.Soa.Client.Model.ModelObject
    ExpandedObject: System.Collections.Hashtable

class ResultOffsetInfo:
    def __init__(self, ) -> None: ...
    LastProcessedIndex: int
    LastProcessedObjId: str

class ListOfObjects2:
    def __init__(self, ) -> None: ...
    Objects: list[FilteredObject2]
    OffsetInfo: ResultOffsetInfo
    Count: int

class Operand2:
    def __init__(self, ) -> None: ...
    OperandType: str
    OperandValue: str
    Attributes: list[str]
    Expressions: list[Expression2]
    StartIndex: int
    MaxToReturn: int
    OffsetInfo: ResultOffsetInfo
    ExpandCriteria: System.Collections.Hashtable
    AttributeSortCriteria: list[Ods0.Services.Internal.Strong.Objectdataservices._2020_04.ObjectDataServices.SortAttribute]
    ReferencedObjectAttributeSortCriteria: list[Ods0.Services.Internal.Strong.Objectdataservices._2020_04.ObjectDataServices.NestedSortCriteria]

class OperandAndOperator:
    def __init__(self, ) -> None: ...
    UnaryOperator: str
    Operand: Operand2

class ReturnObjects2:
    def __init__(self, ) -> None: ...
    Objects: list[ListOfObjects2]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ObjectDataServices:
    def __init__(self , *args: typing.Any) -> None: ...
    def FindObjects2(self, Input: list[OperandAndOperator]) -> ReturnObjects2: ...

