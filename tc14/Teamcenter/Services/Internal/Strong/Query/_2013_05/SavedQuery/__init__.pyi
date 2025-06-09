import System
import Teamcenter.Services.Internal.Strong.Query._2012_02.SavedQuery
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DescribeSavedQueryDefinitionsResponse2:
    def __init__(self, ) -> None: ...
    Definitions: list[SavedQueryDefinition2]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SavedQueryClause2:
    def __init__(self, ) -> None: ...
    AttributeName: str
    EntryL10NKey: str
    EntryNameDisplay: str
    LogicalOperator: str
    MathOperator: str
    DefaultInternalValue: str
    DefaultDisplayValue: str
    Lov: Teamcenter.Soa.Client.Model.Strong.ListOfValues
    AttachedSpecifier: int
    DependentIndexes: list[int]
    KeyLovId: int
    AttributeType: int

class SavedQueryDefinition2:
    def __init__(self, ) -> None: ...
    Query: Teamcenter.Soa.Client.Model.Strong.ImanQuery
    Clauses: list[SavedQueryClause2]
    SortAttributes: list[Teamcenter.Services.Internal.Strong.Query._2012_02.SavedQuery.SavedQuerySortAttribute]

class SavedQuery:
    def __init__(self , *args: typing.Any) -> None: ...
    def DescribeSavedQueryDefinitions2(self, RequestedQueries: list[Teamcenter.Services.Internal.Strong.Query._2012_02.SavedQuery.DescribeSavedQueryDefinitionInput]) -> DescribeSavedQueryDefinitionsResponse2: ...

