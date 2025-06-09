import System
import Teamcenter.Services.Internal.Strong.Query._2012_02.SavedQuery
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DescribeSavedQueryDefnResponse3:
    def __init__(self, ) -> None: ...
    Definitions: list[SavedQueryDefinition3]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SavedQueryClause3:
    def __init__(self, ) -> None: ...
    AttributeName: str
    EntryL10NKey: str
    EntryNameDisplay: str
    LogicalOperator: str
    MathOperator: str
    DefaultInternalValue: str
    DefaultDisplayValue: str
    HasLOV: bool
    KeyLovId: int
    AttributeType: int

class SavedQueryDefinition3:
    def __init__(self, ) -> None: ...
    Query: Teamcenter.Soa.Client.Model.Strong.ImanQuery
    Clauses: list[SavedQueryClause3]
    SortAttributes: list[Teamcenter.Services.Internal.Strong.Query._2012_02.SavedQuery.SavedQuerySortAttribute]

class SavedQuery:
    def __init__(self , *args: typing.Any) -> None: ...
    def DescribeSavedQueryDefinitions3(self, RequestedQueries: list[Teamcenter.Services.Internal.Strong.Query._2012_02.SavedQuery.DescribeSavedQueryDefinitionInput]) -> DescribeSavedQueryDefnResponse3: ...

