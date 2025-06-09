import System
import System.Collections
import Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch
import Teamcenter.Services.Strong.Structuremanagement._2010_04.StructureSearch
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BoundingBoxInfo:
    """
    Contains the six Coordinates of the Bbox
    """
    def __init__(self, ) -> None: ...
    Xmin: float
    """Minimum 'x' coordinate value for bounding box."""
    Ymin: float
    """Minimum 'y' coordinate value for bounding box."""
    Zmin: float
    """Minimum 'z' coordinate value for bounding box."""
    Xmax: float
    """Maximum 'x' coordinate value for bounding box."""
    Ymax: float
    """Maximum 'y' coordinate value for bounding box."""
    Zmax: float
    """Maximum 'z' coordinate value for bounding box."""

class BoundingBoxInfoResponse:
    """
    
A map of Item passed in the input list to the BoundingBoxInfo
object, for the corresponding Item.
    """
    def __init__(self, ) -> None: ...
    BoundingBoxes: System.Collections.Hashtable
    """
            Map of(Item/ BoundingBoxInfo) for
            each input Item and corresponding bounding box coordinates.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            An object of ServiceData which contains any
            exceptions if occurred during getting bounding box.
            """

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
    PlaneZoneExpressions: list[Teamcenter.Services.Strong.Structuremanagement._2010_04.StructureSearch.PlaneZoneExpression]
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
            Specifies whether the search result should return only the subset of scopeBomLines given as input as part of the SearchScope
"""
    ExecuteVOOFilter: bool
    """
            If true, Valid Overlays Only (VOO) filter is applied prior to returning results from
            the server.
            """
    ExecuteRemoteSearch: bool
    """Specifies whether the search should include results from the remote site in response."""
    RemoteSiteID: str
    """
            The remote site id to search from. By default, if the site id is not specified, the
            search will use the site id that is configured by the admin in Teamcenter.
            """

class StructureSearch:
    """
    Interface StructureSearch
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def StartSearch(self, Scope: Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.SearchScope, SearchExpression: SearchExpressionSet) -> Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.StructureSearchResultResponse:
        """    
             This operation initializes the structure search. The input to the operation is a
             search expression set and the scope the search is to be perform in.
             

Use Cases:

             A user wants to perform structure search within a particular scope. The user needs
             to select search criteria(s) from the supported list to create search expression
             and start search operation.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param Scope: 
                         The scope within which the search should be performed.
             
        :param SearchExpression: 
                         The full set of search expressions that are used to perform a single structure search.
                         Each one of the expressions provided are combined together using a logical 'AND'
                         between them
             
        :return: 
        """
        ...
    def GetAssemblyBoundingBox(self, Items: list[Teamcenter.Soa.Client.Model.Strong.Item]) -> BoundingBoxInfoResponse:
        """    
             This operation returns the bounding box for each Item.The bounding box returned
             is for all revisions of the Item. It represents the box for entire assembly.
             

Use Cases:

             A user wants to get the bounding box for the items selected.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param Items: 
                         A list of <b>Items</b> whose bounding box information is expected in the response
             
        :return: 
        """
        ...
    def IsSpatialDataAvailable(self, TopItem: Teamcenter.Soa.Client.Model.Strong.Item) -> bool:
        """    
             This operation checks if the spatial data is available for the Item provided
             in input. If yes, it returns "true" otherwise it returns "false".
             

Use Cases:

             A user wants to check if spatial data is created for given Item which is pre-requiste
             for spatial search operation.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param TopItem: 
                         Specifies the top <b>Item</b> of the assembly for which user wants to find out whether
                         the spatial data exists or not.
             
        :return: else returns
             false. This operation does not return any partial error.
        """
        ...

