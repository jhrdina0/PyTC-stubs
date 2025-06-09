import System
import Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch
import Teamcenter.Services.Strong.Structuremanagement._2010_04.StructureSearch
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ProximityExpression:
    """
    
ProximityExpression specifies one set of proximity criteria. The search results
for
each lines are combined together using an 'OR' operation.
    """
    def __init__(self, ) -> None: ...
    SrcLines: list[Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject]
    """
            A list of source Fnd0BOMLineLite or BOMLine objects to be used in the
            proximity search.
            """
    Distance: float
    """
            Proximity distance in metres from the outer surface of the Fnd0BOMLineLite
            or BOMLine geometry.
            """
    IncludeChildLines: bool
    """
            If true, all child Fnd0BOMLineLite objects or BOMLine of source srcLines
            are considered in the proximity search.
            """

class SearchExpressionSet:
    """
    
The full set of search expressions that are to be used to perform a single
structure
search. Each of the expressions provided are combined using a logical 'AND'
operator.
    """
    def __init__(self, ) -> None: ...
    ItemAndRevisionAttributeExpressions: list[Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.AttributeExpression]
    """A list of Item and ItemRevision attribute search expressions."""
    OccurrenceNoteExpressions: list[Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.OccurrenceNoteExpression]
    """A list of Occurrence Note attribute search expressions."""
    FormAttributeExpressions: list[Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.FormAttributeExpression]
    """A list of Form attribute search expressions."""
    ProximitySearchExpressions: list[ProximityExpression]
    """A list of spatial proximity search expressions."""
    BoxZoneExpressions: list[Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.BoxZoneExpression]
    """A list of spatial box zone expressions."""
    PlaneZoneExpressions: list[Teamcenter.Services.Strong.Structuremanagement._2010_04.StructureSearch.PlaneZoneExpression]
    """A list of spatial plane zone search expressions."""
    SavedQueryExpressions: list[Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.SavedQueryExpression]
    """A list of saved query search expressions."""
    InClassQueryExpressions: list[Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.InClassExpression]
    """A list of class attribute search expressions."""
    SizeSearchExpression: Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.SearchBySizeExpression
    """A list of spatial size search expressions."""
    DoTrushapeRefinement: bool
    """
            If true, Trueshape is perform. (use actual geometry rather using bounding box covering
            min and max points) refinement on the spatial search.
            """
    ReturnScopedSubTreesHit: bool
    """
            If true, return only the subset of scopeBomLines
            provided in input as part of SearchScope.
            """
    ExecuteVOOFilter: bool
    """
            If true, Valid Overlays Only (VOO) filter is applied prior to returning the results
            from the server.
            """
    ExecuteRemoteSearch: bool
    """
            If true, the search includes results from local and remote site(s) in response otherwise
            search results from local site are returned.
            """
    RemoteSiteID: str
    """
            The remote site ID to search from. By default, if the site ID is not specified, the
            search will use the site id that is configured by the admin in Teamcenter.
            """

class SearchScope:
    """
    SearchScope specifies the scope of a search.
    """
    def __init__(self, ) -> None: ...
    Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """
            The BOMWindow object specifying a structure context within which to perform
            search.
            """
    ScopeLines: list[Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject]
    """
            A list of Fnd0BOMLineLite or BOMLine objects, specifying scope of the
            search.
            """
    IgnoreOccurrenceTypes: list[str]
    """A list of occurrence types that are to be ignored from search results."""

class StructureSearchResultResponse:
    """
    The result set received from a single step in a structure search.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            An object of ServiceData which contains any
            exceptions if occurred during performing search.
            """
    OutLines: list[Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject]
    """
            A batch of Fnd0BOMLineLite or BOMLine objects that satisfy the search
            criteria for this search.
            """
    LinesDone: int
    """The number of lines returned in the response."""
    SearchCursor: Teamcenter.Soa.Client.Model.ModelObject
    """Search cursor object that holds the current state of the search in the BOM session."""
    Finished: bool
    """
            If true, the search is complete; otherwise, call nextSearch2
            to get next set of results.
            """

class StructureSearch:
    """
    Interface StructureSearch
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def NextSearch2(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> StructureSearchResultResponse:
        """    
             This operation gets the next set of search results, which was initialized by the
             startSearch2 operation. This operation returns the results in batches and needs to
             be called repeatedly until the flag for search complete is true in the response.
             Input to this operation is the search cursor object which was returned by the startSearch2
             or a previous call to nextSearch2 operation.
             

Use Cases:

             A user wants to perform structure search within a particular scope. The user needs
             to select search criteria(s), from the supported list to create search expression
             and start search operation. Once the initial set of a search result is returned,
             this operation will be used to get the next set of search result.
             

Dependencies:

             startSearch2
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param SearchCursor: 
                         SearchCursor identifies a search session which was started by calling startSearch2
                         operation. This object is returned from the startSearch2 or previous call to nextSearch2
                         operation. Same should be passed as input to current operation.
             
        :return: 
        """
        ...
    def StartSearch2(self, Scope: SearchScope, SearchExpression: SearchExpressionSet, ReturnLiteLines: bool) -> StructureSearchResultResponse:
        """    
             This operation initializes the structure search. The input to the operation is a
             search expression set and the scope to perform the search in.
             

Use Cases:

             A user wants to perform structure search within a particular scope. The user needs
             to select search criteria(s) from the supported list to create search expression
             and start search operation.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param Scope: 
                         The scope of the search.
             
        :param SearchExpression: 
                         The full set of search expressions that are used to perform a single structure search.
                         Each of the expressions provided are combined using a logical 'AND' operator.
             
        :param ReturnLiteLines: 
                         If true, <b>Fnd0BOMLineLite</b> are returned in response; otherwise, a normal <b>BOMLine</b>.
                         If scopeLines are of <b>Fnd0BOMLineLite</b> type, this flag should be true.
             
        :return: 
        """
        ...
    def StopSearch2(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> StructureSearchResultResponse:
        """    
             This operation stops the current search identified by the search cursor object. The
             input to the operation is the search cursor object which was returned by the startSearch2
             or previous call to nextSearch2 operation.
             

Use Cases:

             A user wants to perform Cacheless search within a particular scope. The user needs
             to select search criteria(s) from the supported list to create search expression
             and start search operation. Once the initial batch of search result is returned,
             this operation can be used to stop the search.
             

Dependencies:

             nextSearch2, startSearch2
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param SearchCursor: 
<b>SearchCursor</b> holds the current state of the search session which was created
                         in the startSearch2 or nextSearch2 operation. This is used as a handle to identify
                         this search when executing the next step of the search or stopping the search.
             
        :return: to indicate the search is
             complete and service data. This operation does not return any partial errors.
        """
        ...

