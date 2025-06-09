import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DescribeSavedQueryDefinitionInput:
    def __init__(self, ) -> None: ...
    Query: Teamcenter.Soa.Client.Model.Strong.ImanQuery
    SubstituteKeyword: bool

class DescribeSavedQueryDefinitionsResponse:
    def __init__(self, ) -> None: ...
    Definitions: list[SavedQueryDefinition]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SavedQueryClause:
    def __init__(self, ) -> None: ...
    AttributeName: str
    EntryName: str
    EntryNameDisplay: str
    LogicalOperation: str
    MathOperation: str
    DefaultValue: str
    Lov: Teamcenter.Soa.Client.Model.Strong.ListOfValues
    AttachedSpecifier: int
    DependentIndexes: list[int]
    KeyLovId: int
    AttributeType: int

class SavedQueryDefinition:
    def __init__(self, ) -> None: ...
    Query: Teamcenter.Soa.Client.Model.Strong.ImanQuery
    Clauses: list[SavedQueryClause]
    SortAttributes: list[SavedQuerySortAttribute]

class SavedQuerySortAttribute:
    def __init__(self, ) -> None: ...
    AttributeName: str
    EntryName: str
    EntryNameDisplay: str
    OrderBy: str

class SavedQuery:
    def __init__(self , *args: typing.Any) -> None: ...
    def DescribeSavedQueryDefinitions(self, RequestedQueries: list[DescribeSavedQueryDefinitionInput]) -> DescribeSavedQueryDefinitionsResponse: ...

