import System
import Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch
import typing

class PlaneZoneExpression:
    """
    
PlaneZoneExpression represents a 3D plane to search against. It may define a
search
for all parts that intersect with the plane, or a search for all parts on one
side
of the plane.
    """
    def __init__(self, ) -> None: ...
    PlaneZone: Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.PlaneZone
    """It defines a plane to search against"""
    PlaneZoneOperator: str
    """Operator to use for expression"""

class SearchExpressionSet:
    """
    
SearchExpression data structure specifies the full set of search expressions
that
are to be used to perform a single structure search. Each one of the expressions
provided are combined together using a logical 'AND' between them.
    """
    def __init__(self, ) -> None: ...
    ItemAndRevisionAttributeExpressions: list[Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.AttributeExpression]
    """A collection of Item and ItemRevision attribute search expressions"""
    OccurrenceNoteExpressions: list[Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.OccurrenceNoteExpression]
    """A collection of Occurrence Note attribute search expressions"""
    FormAttributeExpressions: list[Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.FormAttributeExpression]
    """A collection of Form attribute search expressions"""
    ProximitySearchExpressions: list[Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.ProximityExpression]
    """A collection of spatial proximity search expressions"""
    BoxZoneExpressions: list[Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.BoxZoneExpression]
    """A collection of spatial box zone expressions"""
    PlaneZoneExpressions: list[PlaneZoneExpression]
    """A collection of spatial plane zone search expressions"""
    SavedQueryExpressions: list[Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.SavedQueryExpression]
    """A collection of saved query search expressions"""
    InClassQueryExpressions: list[Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.InClassExpression]
    """A collection of inclass attribute search expressions"""
    SizeSearchExpression: Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.SearchBySizeExpression
    """A collection of spatial size search expressions"""
    DoTrushapeRefinement: bool
    """
            Specifies whether to perform trushape (use actual geometry rather using bounding
            box covering min and max points) refinement on the spatial search
            """
    ReturnScopedSubTreesHit: bool
    """
            Specifies whether the search result should return only the sub-set of scopeBomLines
given
            as input as part of the SearchScope
            """

class StructureSearch:
    """
    Interface StructureSearch
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def StartSearch(self, Scope: Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.SearchScope, SearchExpression: SearchExpressionSet) -> Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.StructureSearchResultResponse:
        """    Start searching a structure for a given search expression within the scope specified.
        :param Scope: 
                         - scope within which to search
             
        :param SearchExpression: 
                         searchExpression  data structure specifies the full set of search expressions that
                         are to be used to perform this structure search
             
        :return: - result of search startup
        """
        ...

