import Cls0.Services.Strong.Classificationcore._2013_05.Classification
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class ClassificationRestBindingStub(ClassificationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateOrUpdateClassificationObjects(self, ClassificationObjectInfos: list[Cls0.Services.Strong.Classificationcore._2013_05.Classification.ClassificationObjectInfo]) -> Cls0.Services.Strong.Classificationcore._2013_05.Classification.CreateOrUpdateClassificationObjectsResponse: ...
    def CreateOrUpdateHierarchyNodes(self, HierarchyNodeDetails: list[Cls0.Services.Strong.Classificationcore._2013_05.Classification.HierarchyNodeDetails]) -> Cls0.Services.Strong.Classificationcore._2013_05.Classification.CreateOrUpdateHierarchyNodesResponse: ...
    def DiscardClassificationSearchResults(self, ResultSet: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetClassificationSearchResults(self, SearchResultsInput: Cls0.Services.Strong.Classificationcore._2013_05.Classification.GetClassificationSearchResultsInputInfo) -> Cls0.Services.Strong.Classificationcore._2013_05.Classification.GetClassificationSearchResultsResponse: ...
    def GetHierarchyNodeChildren(self, NodeInfo: list[Cls0.Services.Strong.Classificationcore._2013_05.Classification.GetHierarchyNodeChildrenInputInfo]) -> Cls0.Services.Strong.Classificationcore._2013_05.Classification.GetHierarchyNodeChildrenResponse: ...
    def GetHierarchyNodeDetails(self, Nodes: list[Teamcenter.Soa.Client.Model.Strong.Cls0HierarchyNode]) -> Cls0.Services.Strong.Classificationcore._2013_05.Classification.GetHierarchyNodeDetailsResponse: ...
    def GetTopLevelNodes(self) -> Cls0.Services.Strong.Classificationcore._2013_05.Classification.GetTopLevelNodesResponse: ...
    def SearchClassificationObjects(self, SearchInput: Cls0.Services.Strong.Classificationcore._2013_05.Classification.SearchClassificationObjectsInputInfo) -> Cls0.Services.Strong.Classificationcore._2013_05.Classification.SearchClassificationObjectsResponse: ...

class ClassificationService:
    """
    
            Contains Cls0Classification related operations.
            


Library Reference:

Cls0SoaClassificationCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ClassificationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateOrUpdateClassificationObjects(self, ClassificationObjectInfos: list[Cls0.Services.Strong.Classificationcore._2013_05.Classification.ClassificationObjectInfo]) -> Cls0.Services.Strong.Classificationcore._2013_05.Classification.CreateOrUpdateClassificationObjectsResponse:
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
    def CreateOrUpdateHierarchyNodes(self, HierarchyNodeDetails: list[Cls0.Services.Strong.Classificationcore._2013_05.Classification.HierarchyNodeDetails]) -> Cls0.Services.Strong.Classificationcore._2013_05.Classification.CreateOrUpdateHierarchyNodesResponse:
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
    def GetClassificationSearchResults(self, SearchResultsInput: Cls0.Services.Strong.Classificationcore._2013_05.Classification.GetClassificationSearchResultsInputInfo) -> Cls0.Services.Strong.Classificationcore._2013_05.Classification.GetClassificationSearchResultsResponse:
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
    def GetHierarchyNodeChildren(self, NodeInfo: list[Cls0.Services.Strong.Classificationcore._2013_05.Classification.GetHierarchyNodeChildrenInputInfo]) -> Cls0.Services.Strong.Classificationcore._2013_05.Classification.GetHierarchyNodeChildrenResponse:
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
    def GetHierarchyNodeDetails(self, Nodes: list[Teamcenter.Soa.Client.Model.Strong.Cls0HierarchyNode]) -> Cls0.Services.Strong.Classificationcore._2013_05.Classification.GetHierarchyNodeDetailsResponse:
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
    def GetTopLevelNodes(self) -> Cls0.Services.Strong.Classificationcore._2013_05.Classification.GetTopLevelNodesResponse:
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
    def SearchClassificationObjects(self, SearchInput: Cls0.Services.Strong.Classificationcore._2013_05.Classification.SearchClassificationObjectsInputInfo) -> Cls0.Services.Strong.Classificationcore._2013_05.Classification.SearchClassificationObjectsResponse:
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

