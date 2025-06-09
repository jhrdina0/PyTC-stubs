import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExpressionResponse:
    """
    
            Expression Response structure that carries the search expressions created in the
            server
            
    """
    def __init__(self, ) -> None: ...
    SearchDef: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchDef
    """
            Reference to the Mdl0SearchDef object which is the search expression object
            created based on the input expression type information.
            """
    Clientid: str
    """
            A unique string sent by the calling function, so that the output Search Expression
            object could be mapped back to the input.
            """

class PartitionQueryExpression:
    """
    Input data structure to create a partition search expression (Ptn0SearchPartition)
    """
    def __init__(self, ) -> None: ...
    PartitionObjectExpression: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchDef
    """Search Criteria specifying the specific Partitions"""
    PartitionItemRevExpression: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchDef
    """
            Search Criteria specifying partition item revisions whose partition instances should
            be included
            """
    Clientid: str
    """Client ID to track response with request"""

class UnassignedQueryExpression:
    """
    
            Search for unassigned model elements  Elements not assigned to a partition of given
            scheme names.
            
    """
    def __init__(self, ) -> None: ...
    PartitionSchemeNames: list[str]
    """
            list of Ptn0PartitionScheme names in which the search needs to be performed
            to find the unassigned model elements. This could be a wild card character (*), which
            means that the model elements that should be found are not assigned to any partition
            in any of the schemes in that Application Model.
            """
    Clientid: str
    """
            A unique string sent by the calling function, so that the output Search Expression
            object could be mapped back to the input.
            """

class PartitionSearchExpressionInput:
    """
    Input for creating Partition Search Expression Objects
    """
    def __init__(self, ) -> None: ...
    PartitionQueryExpressions: list[PartitionQueryExpression]
    """
            A PartitionQueryExpression has a partitionObjectExpression and a partitionItemRevExpression.
            Both of these are Search Expression objects. Either one or both could be specified
            that would find partition objects and the Partition Query Expression is to resolve
            to the members of those partitions.
            """
    UnassignedQueryExpression: UnassignedQueryExpression
    """
            This data structure carries a list of partition scheme names and creates a search
            expression that finds all members (Model Elements) that are not partitioned using
            those schemes. If the schemes contain a wild card, then the search is done for model
            elements that are not partitioned in any of the partition schemes, in that application
            model.
            """

class SearchExpressionResponse:
    """
    
            Response data structure that returns the Search Expression objects created for the
            given Search Expression Input data structures.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service Data for any error information. Any malformed input expressions will result
            in an ITK error being returned in the service data. Following errors are possible
            partial errors returned in the ServiceData:
            

PTN0PARTITION_search_has_no_valid_criteria
            (280012)  When the Partition Search input has neither partition criteria nor
            an Partition Item Revision criteria specified, then this error is thrown.
            

"""
    Expressions: list[ExpressionResponse]
    """
            A list of ExpressionResponse structures that has the search expression object embedded.
            Each ExpressionResponse structure consists
            of a reference to an Mdl0SearchDef object and the corresponding clientid (based
            on the clientid of input data).
            """

class Search:
    """
    Interface Search
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreatePartitionExpressions(self, PartitionSearchexpInput: PartitionSearchExpressionInput) -> SearchExpressionResponse:
        """    
             This operation creates Partition Search expressions (Ptn0SearchPartition)
             that would be used in a Search Recipe (to perform executeSearch
             or setRecipes call). Since Partition is an
             optional BMIDE template on top of the AppModel template, creating Partition Search
             expressions are provided as part of the Partition Search SOA service.
             
createPartitionExpressions is an array based
             operation that takes multiple Partition Search expression input data and creates the SearchExpressionResponse
             that is similar to its counterpart (createSearchExpressions)
             in the AppModel Search service.
             


Use Cases:

             There are 2 use cases supported by this operation to create the elemental search
             expressions to find members of Partitions.
             
             1.Create Partition Search Expressions   A Partition Search expression is used
             to first find the partition that are specified by the Search recipe and then searching
             for the members of partitions that are of interest.
             
             2. Create Unpartitioned Elements Search Expression   Search expression used
             to find unpartitioned elements on a given partition scheme or on all partition schemes
             in that Product Design.
             

Dependencies:

             createPartitionExpressions
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param PartitionSearchexpInput: 
                         Input for the runtime partition expressions
             
        :return: :Response data structure
             that returns the Search Expression objects created for the given Search Expression
             Input data structures.
        """
        ...

