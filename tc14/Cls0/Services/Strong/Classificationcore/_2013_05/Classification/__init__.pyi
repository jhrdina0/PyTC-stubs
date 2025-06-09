import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ClassificationObjectInfo:
    """
    
            This structure provides the input information to be used to create or modify Classification
            (Cls0ClassBase) object.
            
    """
    def __init__(self, ) -> None: ...
    ObjectToUpdate: Teamcenter.Soa.Client.Model.Strong.Cls0ClassBase
    """
            Reference of the Cls0ClassBase  to update with the supplied object details. For create
            mode of this operation, this parameter will be empty.
            """
    ObjectId: str
    """
            ID for the Classification Object.This parameter is only used when creating a new
            Classification Object.
            """
    ObjectName: str
    """The name for this Classification Object."""
    ObjectDesc: str
    """
            The description for this Classification Object.
            
            This is an optional parameter and an empty string can be passed in.
            """
    NodeRef: Teamcenter.Soa.Client.Model.Strong.Cls0HierarchyNode
    """
            The Cls0HierarchyNode where this Classification Object should be created.
            
            This parameter is only used when creating a new Classification Object.
            """
    ClassifiedObjectRef: Teamcenter.Soa.Client.Model.ModelObject
    """
            The BusinessObject that is being classified.
            
            This parameter can be empty which indicates that a standalone Classification Object
            should be created.
            
            This parameter is only used when creating a new Classification Object.
            
"""
    PropValues: list[NameValueStruct]
    """
            The list of Classification property names and values that should be set for the Classification
            Object.
            
            This parameter can be empty which indicates that no properties should be set or that
            the Classification Object does not have any properties.
            """

class CreateOrUpdateClassificationObjectsResponse:
    """
    
            This is the response structure that holds reference to created or modified Classification
            (Cls0ClassBase) object.
            
    """
    def __init__(self, ) -> None: ...
    ClassificationObjects: list[Teamcenter.Soa.Client.Model.Strong.Cls0ClassBase]
    """List of references of the newly created or updated Classification Objects."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data response."""

class CreateOrUpdateHierarchyNodesResponse:
    """
    
            This is the response structure that holds references to created or updated Hierarchy
            nodes.
            
    """
    def __init__(self, ) -> None: ...
    NodeObjects: list[Teamcenter.Soa.Client.Model.Strong.Cls0HierarchyNode]
    """The list of created or updated Hierarchy node object."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            The Service Data response. The created / updated objects will be returned in the
            Create / Update lists.
            """

class FilterExpression:
    """
    
            The structure contains a Property Name and an Expression that is used during search
            operations.
            
    """
    def __init__(self, ) -> None: ...
    PropertyName: str
    """The Property name to filter using (Ex: Diameter)."""
    Expression: str
    """
            The expression for the Property (Ex: >= 10.0) An expression is of the form: <operator>
            : used only for IS_NULL, IS_NOT_NULL <operator> <value> : used for =,!=,>,>=,<,<=
            <value> <operator> <value> : used for range(-) valid operators are:  =,!=,>,>=,<,<=,IS_NULL,IS_NOT_NULL,-(range)
            Each expression can also contain a tolerance value that is specified in [] brackets
            just after the value. The tolerance can be an absolute value or a % value.
            """

class GetClassificationSearchResultsInputInfo:
    """
    
            This structure specifies the details of which objects to fetch from a given Result
            Set.
            
    """
    def __init__(self, ) -> None: ...
    ResultSet: str
    """A reference to the Result Set containing all the objects found in the search."""
    Start: int
    """The position in the resultSet to start fetching the objects from."""
    NumObjects: int
    """The number of objects to fetch from resultSet."""

class GetClassificationSearchResultsResponse:
    """
    This is the response structure that holds the Objects being returned.
    """
    def __init__(self, ) -> None: ...
    Objects: list[Teamcenter.Soa.Client.Model.Strong.Cls0ClassBase]
    """List of Classification objects fetched from the Result Set."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data response."""

class GetHierarchyNodeChildrenInputInfo:
    """
    
            This structure provides the input information to be used while fetching the children
            of the given Node.
            
    """
    def __init__(self, ) -> None: ...
    Node: Teamcenter.Soa.Client.Model.Strong.Cls0HierarchyNode
    """The Hierarchy Node for which the children need to be obtained."""
    Filters: list[FilterExpression]
    """
            An optional list of filters to be applied while getting the children. In case filtering
            is not required, pass in an empty list.
            """
    Recursive: bool
    """Indicates whether to fetch children at all levels or only the immediate children."""
    ExtendedInfoRequested: list[str]
    """
            An optional list of strings that indicate the extended information to be fecthed.
            Example: InstanceCount. If no extended information is required, pass in an empty
            list.
            """

class GetHierarchyNodeChildrenResponse:
    """
    
            This contains the response from the operation that holds the Children for each of
            the input Nodes. The ChildrenMap structure has this information.
            
    """
    def __init__(self, ) -> None: ...
    Children: System.Collections.Hashtable
    """A map containing  information about the children of each hierarchy node."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData response."""

class GetHierarchyNodeDetailsResponse:
    """
    
            This is the response structure from this operation that contains the details of the
            Nodes. This information includes things like Node Type, attached Icons / Images,
            etc.
            
    """
    def __init__(self, ) -> None: ...
    NodeDetails: System.Collections.Hashtable
    """A map containing the information about each Hierarchy node."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData response."""

class GetTopLevelNodesResponse:
    """
    
            This is the response structure that holds the information about the top level Nodes
            for a Hierarchy.
            
    """
    def __init__(self, ) -> None: ...
    TopLevelNodes: list[Teamcenter.Soa.Client.Model.Strong.Cls0HierarchyNode]
    """A list that contains the top level Hierarchy Nodes."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """
            The Service Data response. The top level nodes are returned in the Plain list of
            serviceData.
            """

class HierarchyNodeDetails:
    """
    contains detailed information about one Hierarchy Node.
    """
    def __init__(self, ) -> None: ...
    NodeToUpdate: Teamcenter.Soa.Client.Model.Strong.Cls0HierarchyNode
    """
            Reference of the Hierarchy node to update with the supplied node details. For create
            mode of this operation, this parameter will contain a NULL.
            """
    NodeId: str
    """Node ID of this Hierarchy node."""
    NodeName: str
    """Node Name of this Hierarchy node."""
    NodeDesc: str
    """Node Description for this Hierarchy node."""
    NodeType: str
    """Refers to the type of Hierarchy node [e.g. Group / Master / Reference]"""
    Parent: Teamcenter.Soa.Client.Model.Strong.Cls0HierarchyNode
    """Reference to the immediate Parent Node of node."""
    StorageClassTypeName: str
    """
            Type name of the storage class, associated with this Hierarchy node.
            
            A storage class can only be assigned to a Master node type of Hierarchy nodes.
            """
    MasterNode: Teamcenter.Soa.Client.Model.Strong.Cls0HierarchyNode
    """
            References the Master node associated with this Reference node.
            
            This parameter is only valid when working with Reference nodes. Also, it is a mandatory
            parameter for Reference nodes.
            """
    IsLeafNode: bool
    """Flag to indicate whether the Hierarchy Node is a Leaf node or not."""
    LevelSortIndex: int
    """Sort index for this Hierarchy node amongst its peers under the common parent."""
    Icon: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Reference to the dataset object that holds the icon for this Node."""
    Images: list[Teamcenter.Soa.Client.Model.Strong.Dataset]
    """Reference to the dataset object that holds all the images for this Node."""
    Attachments: list[Teamcenter.Soa.Client.Model.Strong.Dataset]
    """
            Reference to the dataset object that holds all other documents attached to this Node
            (other than icon and images). This could be Word documents, Excel sheets etc.
            """
    IsAbstract: bool
    """Indicates whether the node is Abstract or Storage (Instantiable)."""
    IsAssembly: bool
    """Indicates whether the node classifies an Assembly."""
    AllowMultipleClassification: bool
    """Indicates if the same object can be classified multiple times in this node."""
    InstanceCount: int
    """Instance count of the objects classified in this node."""

class NameValueStruct:
    """
    This structure holds property name and values for each property.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the property."""
    Values: list[str]
    """The value(s) of the property."""

class SearchClassificationObjectsInputInfo:
    """
    
            This structure holds all the information needed to execute a search for Classification
            objects.
            
    """
    def __init__(self, ) -> None: ...
    Node: Teamcenter.Soa.Client.Model.Strong.Cls0HierarchyNode
    """The reference to an existing classification hierarchy node."""
    PropertyNames: list[str]
    """Vector of Property names to be used in search criteria."""
    Expressions: list[str]
    """
            Vector of expressions. An expression is of the form: <operator> : used only for
            IS_NULL, IS_NOT_NULL <operator> <value> : used for =,!=,>,>=,<,<= <value>
            <operator> <value> : used for range(-) valid operators are:  =,!=,>,>=,<,<=,IS_NULL,IS_NOT_NULL,-(range)
            Each expression can also contain a tolerance value that is specified in [] brackets
            just after the value. The tolerance can be an absolute value or a % value.
            """
    Options: int
    """
            For specifying certain search options. These options can be combined. Example: Whether
            to find instances of only given node or all Children nodes as well o SEARCH_HIERARCHICAL
            o SEARCH_COUNT_ONLY
            """
    SortOrder: list[SortOrder]
    """Specifies the sort parameters to use while sorting the search results."""

class SearchClassificationObjectsResponse:
    """
    This is the response structure that holds information about the search results.
    """
    def __init__(self, ) -> None: ...
    NumRows: int
    """The number of objects found that match the search criteria."""
    ResultSet: str
    """
            Reference to a Result Set containing the objects found in the search. This is a reference
            to a single object. Subsequent to this operation call, you need to call the getClassificationSearchResults
            passing in this value to get the actual objects returned in the search operation.
            """
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data response."""

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

class Classification:
    """
    Interface Classification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateClassificationObjects(self, ClassificationObjectInfos: list[ClassificationObjectInfo]) -> CreateOrUpdateClassificationObjectsResponse:
        """    
             This operation creates or modifies Classification (Cls0ClassBase) objects. This operation
             can be used to classify existing Teamcenter objects or to create standalone Classification
             objects.
             

Teamcenter Component:

             Next Generation Classification application - Provides a set of features to work with
             Classification node hierarchy and Classification data.  Application allows Classification
             of product data-standard parts.
             
        :param ClassificationObjectInfos: 
                         List of structures, each representing a set of properties for creation or modification
                         of a Classification object.
             
        :return: 
        """
        ...
    def CreateOrUpdateHierarchyNodes(self, HierarchyNodeDetails: list[HierarchyNodeDetails]) -> CreateOrUpdateHierarchyNodesResponse:
        """    
             This operation is used to Create or Update Hierarchy nodes in a given hierarchy.
             
             The response structure for this operation will contain a list of newly created or
             updated Hierarchy nodes along with any errors during the operation.
             


Teamcenter Component:

             Next Generation Classification application - Provides a set of features to work with
             Classification node hierarchy and Classification data.  Application allows Classification
             of product data-standard parts.
             
        :param HierarchyNodeDetails: 
                         List of structures of Hierarchy node properties.
             
        :return: The created / updated Classification Presentation Layer's Hierarchy Nodes. Partial
             errors are returned in the ServiceData if a Hierarchy node could not created / updated
             for some reason.
        """
        ...
    def DiscardClassificationSearchResults(self, ResultSet: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Discards the results of a Classification search that was previously started. The
             resultSet needs to be a valid resultSet obtained from a previous operation call to
             the operation getClassificationSearchResults. This operation should be called after
             you are done using the results obtained from a search.
             

Teamcenter Component:

             Next Generation Classification application - Provides a set of features to work with
             Classification node hierarchy and Classification data.  Application allows Classification
             of product data-standard parts.
             
        :param ResultSet: 
                         The identifier of an existing Result Set that was obtained using a call to the operation
                         getClassificationSearchResults.
             
        :return: 
        """
        ...
    def GetClassificationSearchResults(self, SearchResultsInput: GetClassificationSearchResultsInputInfo) -> GetClassificationSearchResultsResponse:
        """    
             From a Result Set that contains search results, fetch the specified number of results
             (objects). The Result Set passed in here should be one created as a result of a Classification
             search operation like searchClassificationObjects.
             

Teamcenter Component:

             Next Generation Classification application - Provides a set of features to work with
             Classification node hierarchy and Classification data.  Application allows Classification
             of product data-standard parts.
             
        :param SearchResultsInput: 
                         Structure containing the Result Set identifier and which objects to fetch from the
                         Result Set.
             
        :return: The specified objects from the Result Set. Partial errors will be returned ServiceData
        """
        ...
    def GetHierarchyNodeChildren(self, NodeInfo: list[GetHierarchyNodeChildrenInputInfo]) -> GetHierarchyNodeChildrenResponse:
        """    
             This operation gets the children along with associated Node information for all the
             given Classification Presentation Layer's Hierarchy Nodes. If recursive is set as
             true in the input structure, all the children up to the leafmost Nodes would be found
             and returned. If recursive is set as false, only the first level children would be
             found and returned. You can request for extended information about the returned Nodes
             by passing in predefined strings in the extendInfoRequested parameter in the input
             structure. Example: Passing in the string InstanceCount in extendInfoRequested would
             return the number of Classification (Cls0ClassBase) Object instances of the Classification
             Presentation Layer's Hierarchy Node.
             

Teamcenter Component:

             Next Generation Classification application - Provides a set of features to work with
             Classification node hierarchy and Classification data.  Application allows Classification
             of product data-standard parts.
             
        :param NodeInfo: 
                         Structure containing the details of the Nodes for which the children need to be found.
             
        :return: The children found for each of the input Nodes is returned in the GetChildrenResponse
             structure.
        """
        ...
    def GetHierarchyNodeDetails(self, Nodes: list[Teamcenter.Soa.Client.Model.Strong.Cls0HierarchyNode]) -> GetHierarchyNodeDetailsResponse:
        """    
             Gets the detailed information about the Classification Presenatation Layer's Hierarchy
             Nodes including information like Node Type, attached Icons / Images,  etc. This information
             can be typically used for displaying details about the node in Teamcenter user interface.
             

Teamcenter Component:

             Next Generation Classification application - Provides a set of features to work with
             Classification node hierarchy and Classification data.  Application allows Classification
             of product data-standard parts.
             
        :param Nodes: 
                         The list of Classification Hierarchy Nodes for which you need the detailed information.
             
        :return: The detailed information about Classification Presentation Layer's Hierarchy Nodes
             including information like Node Type, attached Icons / Images, etc. This information
             can be typically used for displaying details about the node in Teamcenter user interface.
             Partial errors will be returned in ServiceData if there are any. Example:Attached
             dataset cannot be read.
        """
        ...
    def GetTopLevelNodes(self) -> GetTopLevelNodesResponse:
        """    
             Gets all the top-level Hierarchy Nodes of a Classification Presentation Layer Hierarchy.
             Obtaining the top level nodes would usually be one of the first steps while trying
             to fetch the Classification Presentation Layer Hierarchy. After the top level nodes
             are obtained, further nodes can be obtained using the operation getHierarchyNodeChildren.
             

Teamcenter Component:

             Next Generation Classification application - Provides a set of features to work with
             Classification node hierarchy and Classification data.  Application allows Classification
             of product data-standard parts.
             
        :return: 
        """
        ...
    def SearchClassificationObjects(self, SearchInput: SearchClassificationObjectsInputInfo) -> SearchClassificationObjectsResponse:
        """    
             This operation allows searching for Classification (Cls0ClassBase) Objects that match
             the specified search criteria. The inputs specify which Classification Presenataion
             Layer's Hierarchy Node to search in and the Properties used in the search.
             

Teamcenter Component:

             Next Generation Classification application - Provides a set of features to work with
             Classification node hierarchy and Classification data.  Application allows Classification
             of product data-standard parts.
             
        :param SearchInput: 
                         Input structure for searching classification objects.
             
        :return: You need to invoke the getClassificationSearchResults operation after this operation
             to get the actual Classification (Cls0ClassBase) Objects that were found in the search.
        """
        ...

