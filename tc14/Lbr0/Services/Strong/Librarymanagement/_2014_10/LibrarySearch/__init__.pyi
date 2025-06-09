import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FilterExpression:
    """
    
            The structure contains a Property Name and an Expression that is used as criteria
            during search operations.
            
    """
    def __init__(self, ) -> None: ...
    PropertyName: str
    """The Property name to filter using (Ex: "Diameter")."""
    Expression: str
    """
            The expression for the Property (Ex: ">= 10.0")
            
            An expression is of the form:
            
operator value : used for =,!=,>,>=,<,<=
            
value operator value : used for range(-)
            
            valid operators are:  =,!=,>,>=,<,<=, -(range).
            
"""

class SearchLibraryElementsCriteria:
    """
    Structure containing the criteria used during the search for Library Elements.
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """
            The specification object. This will be used as additional filter for the element
            search.
            """
    SourceMember: Teamcenter.Soa.Client.Model.Strong.Lbr0LibraryElement
    """
            A Library Element that should be used as the 'Source Member' for filtering using
            Specification Rules. Either this or sourceMemberExprs
            should be specified
            """
    SourceMemberExprs: list[FilterExpression]
    """
            Search expressions based on the Source Member that should used during the search
            for filtering using Specification Rules. Either this or sourceMember
            should be specified.
            """
    SearchExpressions: list[FilterExpression]
    """
            Search expressions based on the Source Member that should used during the search
            for filtering using Specification Rules. Either this or sourceMember should be specified.
            """

class SearchLibraryElementsOptions:
    """
    Search Options for a given Library Elements search operation
    """
    def __init__(self, ) -> None: ...
    SortOrder: list[SortOrder]
    """Specifies the sort parameters to use while sorting the search results."""
    Options: int
    """
            Specifies search options that control certains aspects.  The options can be combined.
            This is the list of available options:
            

    LBRSEARCH_HIERARCHICAL: Specifies whether
            search should look in child Nodes as well
            
    LBRSEARCH_APPLY_EFFECTIVITY:  Specifies whether
            to filter the search results based on effectivity
            
    LBRSEARCH_COUNT_ONLY:  Only return a count
            of objects found, and not the objects themselves. If this is set, then objects will
            not be returned irrespective of other flags set in this options.
            

"""
    Start: int
    """The position in the search result set to start fetching the objects from."""
    LoadCount: int
    """
            Number of objects returned by this search. A loadCount of -1 will return all the
            results found.
            """

class SearchLibraryElementsIn:
    """
    Structure containing the input parameters for searching Library Elements.
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            This unique ID provided by the client application is used to identify the search
            query. Passing in the same ID on subsequent calls will reuse the query if possible.
            The ID should be different if the search criteria are different.
            """
    NodeToSearchIn: Teamcenter.Soa.Client.Model.Strong.Lbr0HierarchyNode
    """The Library Node for which the search is to be performed."""
    ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            The configuration context to be used in the search, to apply configuration filters
            like effectivity.
            """
    SearchOptions: SearchLibraryElementsOptions
    """Defines the options for search."""
    SearchCriteria: SearchLibraryElementsCriteria
    """
            Defines the search criteria containing the search expressions including Specifications
            filters.
            """

class SearchResponse:
    """
    This is the response structure that holds information about the search results.
    """
    def __init__(self, ) -> None: ...
    NumTotalResults: int
    """The total number of objects found that match the search criteria"""
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            List of objects from the ResultSet. Number of objects is restricted to loadCount, specified in the input.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data for any error information."""

class SortOrder:
    """
    
            This structure contains information about the Property name to be used for sorting
            and the kind of sorting needed (Ascending / Descending).
            
    """
    def __init__(self, ) -> None: ...
    AscendingSort: bool
    """Specifies whether to do an Ascending or Descending sort."""
    SortProperty: str
    """Specifies the Property on which to sort by."""

class LibrarySearch:
    """
    Interface LibrarySearch
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def DiscardSearchResults(self, ResultSet: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Discard the results of a Library search operation that was previously started. This
             operation  needs to be called to free up memory consumed by a search operation like
             searchLibraryElements. The operation should
             be called after the  search results have been consumed by the application.
             
             The resultSet needs to be a valid one obtained
             from a previous operation  call to a search operation. After this call, the Result
             Set will be no longer valid.
             


Dependencies:

             searchLibraryElements
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param ResultSet: 
                         The identifier of an existing Result Set
             
        :return: 132701 - The Result Set provided is not a valid one
        """
        ...
    def SearchLibraries(self, Contexts: list[Teamcenter.Soa.Client.Model.ModelObject], SearchExprs: list[FilterExpression]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation searches for available  Libraries in Teamcenter. Filtering can be
             done based on the Context assigned or properties of the Library  like ID, Name etc.
             If no filtering is specified, all the Libraries in Teamcenter are returned.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param Contexts: 
                         The Project / Program or Design Context object to filter on
             
        :param SearchExprs: 
                         Search expressions for additional filtering
             
        :return: 515156 - if any of the property names specified is not a valid one.
        """
        ...
    def SearchLibraryElements(self, SearchInput: SearchLibraryElementsIn) -> SearchResponse:
        """    
             This operation searches for Library  Elements (Lbr0LibraryElement) in a given
             Library that match the specified search criteria.  If no search criteria are specified,
             it will return all the Elements for the Node. The search criteria  can include Specifications
             related criteria.
             
             The results of the search are returned one set  at a time based on the defaultLoadCount  specified in the searchOptions.
             More results for the search can be obtained by calling this operation again with
             the same inputs, varying  only the start
             parameter in searchOptions.
             
             After the search  results have been consumed by the application, it is necessary
             to call the discardSearchResults operation
             to free up memory consumed by the  search.
             


Dependencies:

             discardSearchResults
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param SearchInput: 
                         The input parameters for the search.
             
        :return: 515156 - if any of the property names specified is not a valid one.
        """
        ...

