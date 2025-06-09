import Ptn0.Services.Strong.Partition._2012_09.Search
import Ptn0.Services.Strong.Partition._2018_11.Search
import typing

class AttributeSearchOptions:
    """
    Order in which results are sorted Ascending or Descending.
    """
    def __init__(self, ) -> None: ...
    SortAttribute: str
    """
            Attribute of the class being searched based on which the results will be sorted.
            The attribute should be specified in the "object_type.attribute_name" format.
            """
    SortOrder: str
    """Order in which results are sorted Asending or Descending."""

class SearchOptions:
    """
    Search options for the given search.
    """
    def __init__(self, ) -> None: ...
    SortOptions: list[AttributeSearchOptions]
    """A list of attribute search options based on which the results will be sorted."""
    DefaultLoadCount: int
    """
            Number of objects returned by this search. The rest of them could be retrieved by
            calling fetchNextSearchResults. A defaultLoadCount of zero will return all the results
            found.
            """

class Search:
    """
    Interface Search
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteSearch(self, Options: SearchOptions, Scope: Ptn0.Services.Strong.Partition._2012_09.Search.PartitionScope, Recipe: Ptn0.Services.Strong.Partition._2012_09.Search.SearchRecipe, ExportOption: Ptn0.Services.Strong.Partition._2018_11.Search.ExportOption) -> Ptn0.Services.Strong.Partition._2012_09.Search.SearchResponse: ...

