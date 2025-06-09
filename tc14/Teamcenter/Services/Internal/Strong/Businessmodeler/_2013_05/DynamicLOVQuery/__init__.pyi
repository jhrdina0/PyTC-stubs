import System
import Teamcenter.Soa.Client.Model
import typing

class LOVData:
    def __init__(self, ) -> None: ...
    ValueProperty: str
    DescriptionProperty: str
    FilterProperties: list[str]

class LovFilterData:
    def __init__(self, ) -> None: ...
    FilterString: str
    MaxResult: int
    NumberToLoad: int
    SortPropertyName: str
    SortOrder: int

class LOVSearchResults:
    def __init__(self, ) -> None: ...
    LovValues: list[LOVData]
    UnprocessedUIDs: list[str]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class QueryData:
    def __init__(self, ) -> None: ...
    QueryClass: str
    QueryString: str
    LovInputData: LOVData
    FilterData: LovFilterData
    UnprocessedUIDs: list[str]

class DynamicLOVQuery:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteDynamicLOVQuery(self, QueryData: QueryData) -> LOVSearchResults: ...

