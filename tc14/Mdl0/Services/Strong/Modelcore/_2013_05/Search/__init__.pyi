import Mdl0.Services.Strong.Modelcore._2011_06.Search
import System
import System.Collections
import Teamcenter.Soa.Client.Model.Strong
import typing

class OptionSetExpression:
    """
    Elemental Transfer Option Set Expression
    """
    def __init__(self, ) -> None: ...
    OptionSet: Teamcenter.Soa.Client.Model.Strong.TransferOptionSet
    """Reference to the <b>TransferOptionSet</b>"""
    OptionSetMap: System.Collections.Hashtable
    """Map containing names and values of options to be used with the <b>TransferOptionSet</b>"""
    SearchDef: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchDef
    """
            Reference to the Mdl0SearchDef object that represents the rest of the search
            expression.
            """

class OptionSetExpressionInput:
    """
    Option Set Expression Input - Request Structure
    """
    def __init__(self, ) -> None: ...
    OptionSetExpression: OptionSetExpression
    """Search expression representing the <b>TransferOptionSet</b>"""
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
    ProximitySearchExpressions: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ProximitySearchExpressionInput]
    """
            Input for creating Proximity Search Expressions. Contains reference to a set of <font
            face=&quot;courier&quot; height=&quot;10&quot;>ModelElements</font>
            (that are targets) and the proximity distance.
            """
    BoxZoneExpressions: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.BoxZoneExpressionInput]
    """
            input for creating box zone search expressions. Contains the Min and Max coordinated
            of a test Box definition.
            """
    PlaneZoneExpressions: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.PlaneZoneExpressionInput]
    """
            input for creating plane zone search expressions. Contains a point in the plane and
            the normal vector definition.
            """
    SavedQueryExpressions: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.SavedQueryExpressionInput]
    """
            input for creating saved query search expressions. Contains reference to a stored
            saved query object and a coordinated list of entries and values to be used in the
            saved query. Some queries may contain empty list for entries and values (depends
            on the definition of the Saved Query). Wildcards are accepted for values in the Saved
            Query.
            """
    ClosureQueryExpression: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ClosureQueryExpressionInput]
    """
            Closure Query Expression  that traverses results using a closure rule  Not implemented
            in Tc9.1.0 or Tc10.1.0.
            """
    OptionSetExpressions: list[OptionSetExpressionInput]
    """
            Option Set Expression that defines the Transfer Option Set and option values that
            are used traverse the closure defined for the Transfer Option Oet
            """
    IncludeElements: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ModelElementInput]
    """
            References to elements to be included into the search results. The server creates
            a Search Expression for this input as well, so that it could be combined with other
            search expressions in a search recipe.
            """
    ExcludeElements: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ModelElementInput]
    """
            Reference to elements that should be explicitly excluded in the search results. Again
            a search expression is returned for the exclude elements so that it could be combined
            with other search expressions in a search recipe.
            """

class Search:
    """
    Interface Search
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateSearchExpressions(self, SearchExpInput: SearchExpressionInput) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchExpressionResponse:
        """    
             This operation creates the elemental search expressions that could be combined using
             logical operators to build up a complex search recipe in CPD application. The createSearchExpressions
             operation could be used to create multiple search expressions at the same time. The
             following types of expressions could be created by this operation
             

Bounding Box Expression (Mdl0SearchBoxZone)
             
Plane Zone Expression (Mdl0SearchPlaneZone)
             
Proximity Expression (Mdl0SearchProximity)
             
Saved Query Expression (Mdl0SearchSavedQuery)
             
Include Content Expression (Mdl0SearchSlctContent)
             
Exclude Content Expression (Mdl0SearchGroup)
             



Use Cases:

             The createSearchExpressions is a required operation before an executeSearch or setRecipes
             call is made. This operation creates the runtime Search Definition objects based
             on the input search expression data structures. The intent of this operation is to
             create all the individual elemental search expressions so that they could be combined
             using logical operators (AND/OR/NOT) to create a complex search recipe.
             

Dependencies:

             createSearchExpressions
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param SearchExpInput: 
                         Search Expression Input Structure
             
        :return: SearchExpressionResponse data structure that returns the Search Expression objects
             created for the given Search Expression Input data structures.
        """
        ...

