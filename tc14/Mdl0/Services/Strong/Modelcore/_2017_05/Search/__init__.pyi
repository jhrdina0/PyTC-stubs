import Mdl0.Services.Strong.Modelcore._2011_06.Search
import Mdl0.Services.Strong.Modelcore._2013_05.Search
import Mdl0.Services.Strong.Modelcore._2014_10.Search
import System
import typing

class BoxZoneExpressionInput:
    """
    Box Zone Expression Input Structure
    """
    def __init__(self, ) -> None: ...
    RootType: str
    TraversalKey: str
    BoxZoneExpression: Mdl0.Services.Strong.Modelcore._2011_06.Search.BoxZoneExpression
    """Box zone expression, contains the definition of the coordinates to a spatial 3D box."""
    Clientid: str
    """
            A unique string sent by the calling function, so that the output search expression
            object could be mapped back to the input.
            """

class CompositeSearchExpressionInput:
    """
    Input Data Structure to create the Group of Elemental Composite Search Expressions
    """
    def __init__(self, ) -> None: ...
    CompositeSearchType: str
    SearchExpressions: list[SearchExpressionInput]
    """Group of Elemental Search Expressions"""
    Clientid: str
    """
            A unique string sent by the calling function, so that the output Search Expression
            object could be mapped back to the input.
            """

class PlaneZoneExpressionInput:
    """
    Plane Zone Input Structure
    """
    def __init__(self, ) -> None: ...
    RootType: str
    TraversalKey: str
    PlaneZoneExpression: Mdl0.Services.Strong.Modelcore._2011_06.Search.PlaneZoneExpression
    """3D plane expression around which the spatial search is performed."""
    Clientid: str
    """
            A unique string sent by the calling function, so that the output search expression
            object could be mapped back to the input.
            """

class ProximitySearchExpressionInput:
    """
    Proximity Expression Input - Request Structure
    """
    def __init__(self, ) -> None: ...
    RootType: str
    TraversalKey: str
    ProximityExpression: Mdl0.Services.Strong.Modelcore._2011_06.Search.ProximityExpression
    """
            Proximity search expression. Contains reference to the target elements whose proximity
            is searched and the distance to search.
            """
    Clientid: str
    """
            A unique string sent by the calling function, so that the output search expression
            object could be mapped back to the input.
            """

class SavedQueryExpressionInput:
    """
    Saved query Expression Input Data Structure
    """
    def __init__(self, ) -> None: ...
    RootType: str
    TraversalKey: str
    SavedQueryExpression: Mdl0.Services.Strong.Modelcore._2011_06.Search.SavedQueryExpression
    """Search expression for a saved query search."""
    Clientid: str
    """
            A unique string sent by the calling function, so that the output Search Expression
            object could be mapped back to the input.
            """

class SearchExpressionInput:
    """
    Input Data Structure to create the Group of Elemental Search Expressions
    """
    def __init__(self, ) -> None: ...
    ReturnType: str
    """
            Type name of the the Business Objects to be returned. All objects returned will be
            of this type, or sub-type of the this type.
            """
    ProximitySearchExpressions: list[ProximitySearchExpressionInput]
    """
            A list for creating proximity search expressions. Contains reference to a set of
            ModelElements (that are targets) and the proximity distance.
            """
    BoxZoneExpressions: list[BoxZoneExpressionInput]
    """
            A list for creating box zone search expressions. Contains the minimum and maximum
            coordinates of a test box definition.
            """
    PlaneZoneExpressions: list[PlaneZoneExpressionInput]
    """
            A list for creating plane zone search expressions. Contains a point in the plane
            and the normal vector definition.
            """
    SavedQueryExpressions: list[SavedQueryExpressionInput]
    """
            A list for creating saved query search expressions. Contains reference to a stored
            saved query object and a coordinated list of entries and values to be used in the
            saved query. Some queries may contain empty list for entries and values (depends
            on the definition of the saved query). Wildcards are accepted for values in the saved
            query.
            """
    CompositeExpressions: list[CompositeSearchExpressionInput]
    """
            A list of search expressions to be executed as single search term. This will typically
            be used to search for objects based on properties of some other object. The composite
            search terms will be combined together with logical AND operator
            """
    ClosureQueryExpression: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ClosureQueryExpressionInput]
    """Not implemented."""
    OptionSetExpressions: list[Mdl0.Services.Strong.Modelcore._2013_05.Search.OptionSetExpressionInput]
    """
            Option Set Expression that defines the Transfer Option Set and option values that
            are used traverse the closure defined for the Transfer Option Set
            """
    GeomConstraintExpressions: list[Mdl0.Services.Strong.Modelcore._2014_10.Search.GeomConstraintExpressionInput]
    """
            Input for creating geometric constraint collection search expressions. Contains an
            integer flag that indicates how the search result is treated to fetch the related
            constraint data and reference to source search criteria on which the constraint search
            term is to be applied.
            """
    IncludeElements: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ModelElementInput]
    """
            A list of elements to be included into the search results. The server creates a Search
            Expression for this input as well, so that it could be combined with other search
            expressions in a search recipe.
            """
    ExcludeElements: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ModelElementInput]
    """
            A list of elements that should be explicitly excluded in the search results. Again
            a search expression is returned for the exclude elements so that it could be combined
            with other search expressions in a search recipe.
            """

class Search:
    """
    Interface Search
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateSearchExpressions(self, SearchExpressionInput: SearchExpressionInput) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchExpressionResponse:
        """    
             This operation creates the elemental search expressions that could be combined using
             logical operators to build up a complex search recipe. The createSearchExpressions
             operation could be used to create multiple search expressions at the same time. The
             following types of expressions could be created by this operation
             

             Bounding Box Expression (Mdl0SearchBoxZone)
             
             Plane Zone Expression (Mdl0SearchPlaneZone)
             
             Proximity Expression (Mdl0SearchProximity)
             
             Saved Query Expression (Mdl0SearchSavedQuery)
             
             Composite Search Expression(Mdl0CompositeSearchDef)
             
             Geometric Constraint Expression (Mdl0SearchGeomConstraint)
             
             Include Content Expression (Mdl0SearchSlctContent)
             
             Exclude Content Expression (Mdl0SearchGroup)
             

             The above search expressions can be build for various types of Business Object types.
             Information about how to traverse from one type to another type is embedded within
             a search expression input.
             

Use Cases:

             The createSearchExpressions is a required operation before an executeSearch
             or setRecipes2 call is made. This operation creates the runtime Search Definition
             objects based on the input search expression data structures. The intent of this
             operation is to create all the individual elemental search expressions so that they
             could be combined using logical operators (AND, OR, NOT) to create a complex search
             recipe.
             

Dependencies:

             executeSearch, setRecipes, setRecipes2
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param SearchExpressionInput: 
                         Search Expression Input Structure
             
        :return: SearchExpressionResponse data structure that returns the Search Expression objects
             created for the given Search Expression Input data structures.
        """
        ...

