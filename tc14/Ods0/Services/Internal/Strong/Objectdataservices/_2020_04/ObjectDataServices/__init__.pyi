import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class Operand:
    def __init__(self, ) -> None: ...
    OperandType: str
    OperandValue: str
    Attributes: list[str]
    Expressions: list[Expression]
    StartIndex: int
    MaxToReturn: int
    ExpandCriteria: System.Collections.Hashtable
    AttributeSortCriteria: list[SortAttribute]
    ReferencedObjectAttributeSortCriteria: list[NestedSortCriteria]

class Expression:
    def __init__(self, ) -> None: ...
    Lhs: Operand
    Rhs: Operand
    ExpressionOperator: str

class FilteredObject:
    def __init__(self, ) -> None: ...
    FilteredObj: Teamcenter.Soa.Client.Model.ModelObject
    ExpandedObject: System.Collections.Hashtable

class ListOfObjects:
    def __init__(self, ) -> None: ...
    Objects: list[FilteredObject]
    Count: int

class NestedSortCriteria:
    def __init__(self, ) -> None: ...
    AttributeName: str
    ClassName: str
    SimpleSortCriteria: list[SortAttribute]
    ReferencedObjectsSortCriteria: list[NestedSortCriteria]

class ReturnObjects:
    def __init__(self, ) -> None: ...
    Objects: list[ListOfObjects]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SortAttribute:
    def __init__(self, ) -> None: ...
    Attribute: str
    SortDirection: str

class ObjectDataServices:
    def __init__(self , *args: typing.Any) -> None: ...
    def FindObjects(self, Input: list[Operand]) -> ReturnObjects: ...

