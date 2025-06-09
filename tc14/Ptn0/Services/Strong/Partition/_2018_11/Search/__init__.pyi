import Ptn0.Services.Strong.Partition._2012_09.Search
import System
import typing

class ExportOption:
    """
    Specifies the mode of the export to be used.
    """
    def __init__(self, ) -> None: ...
    ApplicationFormat: str
    """
            The application format for the export. Valid value is MSExcel. If it is empty,
            the operation executes search and returns the search results to client. Otherwise,
            it executes the search, exports the search results in background and returns immediately.
            """
    ColumnAttributes: list[str]
    """
            List of columns to be exported for the business objects. Each element of the list
            should be specified in the object_type.column_name format.
            """

class Search:
    """
    Interface Search
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteSearch(self, SearchOptions: Ptn0.Services.Strong.Partition._2012_09.Search.SearchOptions, Scope: Ptn0.Services.Strong.Partition._2012_09.Search.PartitionScope, Recipe: Ptn0.Services.Strong.Partition._2012_09.Search.SearchRecipe, ExportOption: ExportOption) -> Ptn0.Services.Strong.Partition._2012_09.Search.SearchResponse: ...

