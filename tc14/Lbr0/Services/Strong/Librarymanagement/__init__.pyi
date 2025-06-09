import Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement
import Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySearch
import Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement
import Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryUsage
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class LibraryManagementRestBindingStub(LibraryManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def AssignOrRemoveContexts(self, ContextInfo: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.AssignOrRemoveContextIn]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateHierarchies(self, CreateInput: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.CreateHierarchiesIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.CreateHierarchiesResponse: ...
    def CreateLibraries(self, CreateInput: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.CreateLibrariesIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.CreateLibrariesResponse: ...
    def CreateNodes(self, CreateInput: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.CreateNodesIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.CreateNodesResponse: ...
    def DeleteLibraryContent(self, DeleteIn: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.DeleteLibraryContentIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.DeleteLibraryContentResponse: ...
    def FindAssignedContexts(self, Libraries: list[Teamcenter.Soa.Client.Model.Strong.Lbr0Library]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.FindAssignedContextsResponse: ...

class LibraryManagementService:
    """
    
            This service exposes operations related to Library Management in Teamcenter. Libraries
            provide control of how reusable components are managed and Instantiated into Designs.
            Libraries are organized in a hierarchical structure similar to Classification, such
            that a Library is composed of one or more Hierarchies with each having child Nodes.
            This service deals with all aspects related to managing the structure and configuration
            of Libraries.
            



Library Reference:

Lbr0SoaLibraryManagementStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> LibraryManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def AssignOrRemoveContexts(self, ContextInfo: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.AssignOrRemoveContextIn]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation assigns or removes  Libraries from a Context. A Context can be a Project/Program
             or a Design Context. Assigning Libraries  to a context limits which Libraries can
             be used when that context is "active".
             

Use Cases:

             An Administrator creates three Libraries say L1, L2, L3. This user then assigns Libraries
             L1  and L3 to a Design Context "D1".
             
             A Designer user working in a Design Context "D1"  gets the available Libraries using
             a call to the operation searchLibraries()
             and passes in the Context information. The Libraries L1 and L3 are returned since
             these are the ones  assigned to the context. Library L2 is not returned because it
             was not assigned to the Context D1.<br  />Parameters:
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param ContextInfo: 
                         The input structure containing the details of the Library and Context to assign /
                         remove
             
        :return: 143135 - if the Library is not assigned to the Context.
        """
        ...
    def CreateHierarchies(self, CreateInput: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.CreateHierarchiesIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.CreateHierarchiesResponse:
        """    
             This operation creates new Library  Hierarchy (Lbr0Hierarchy) objects, within
             a given Library. A Hierarchy acts as the  "root node" of one Hierarchy in the Library.
             A Hierarchy object can only be created at the  "top" level in a Library and does
             not support child Hierarchy objects.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param CreateInput: 
                         The input structure containing the details of the Library Hierarchies to be created.
             
        :return: 38207 - if a property required for creation (like name) was not specified.
        """
        ...
    def CreateLibraries(self, CreateInput: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.CreateLibrariesIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.CreateLibrariesResponse:
        """    
             This operation creates new Library (Lbr0Library)  objects. A Library provides
             control of how reusable components are managed and instantiated into Designs.  Configuration
             information like "allowed Member Types" for a Library can also be specified in  this
             operation.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param CreateInput: 
                         The input containing the details of the Libraries to be created.
             
        :return: 
        """
        ...
    def CreateNodes(self, CreateInput: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.CreateNodesIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.CreateNodesResponse:
        """    
             This operation creates new Library Node (Lbr0HierarchyNode)  objects within
             a given Library. Nodes are created within a Hierarchy in the Library.
             
             The  operation supports creating a Library Node structure based on an existing Classification
             Node structure,  so that the Library has a Node structure similar to Classification.
             During this "replication",  the ID, Name & Description of the Library Node are
             copied over from the Classification Node.<br  />
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param CreateInput: 
                         The input structure containing the details of the Library Nodes to be created.
             
        :return: 143105 - if the specified parent_node is not part of the hierarchy specified.
        """
        ...
    def DeleteLibraryContent(self, DeleteIn: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.DeleteLibraryContentIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.DeleteLibraryContentResponse:
        """    
             This operation deletes existing Library objects, including its content. The supported
             objects for this operation are: Lbr0Library,
             Lbr0Hierarchy, Lbr0HierarchyNode.
             
             Deleting a Library by specifying the deleteContent
             as true will attempt to delete the entire Library, all its Hierarchies and all the
             Nodes in the Hierarchies. All the Library Elements added as content to the Nodes
             will also be attempted to be deleted.
             


Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param DeleteIn: 
                         The input list of Library related objects to be deleted.
             
        :return: 143107 - The specified object is invalid for deletion.
        """
        ...
    def FindAssignedContexts(self, Libraries: list[Teamcenter.Soa.Client.Model.Strong.Lbr0Library]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryManagement.FindAssignedContextsResponse:
        """    
             Find the assigned Contexts for given  Libraries. This finds both Project/Program
             and Design Contexts assigned to the Libraries. The context  information returned
             also says whether it is an owning context.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param Libraries: 
                         A list of Libraries.
             
        :return: Information regarding the  assigned contexts for each Library is returned in the
             response structure FindAssignedContextsResponse.
        """
        ...

class LibrarySearchRestBindingStub(LibrarySearchService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def DiscardSearchResults(self, ResultSet: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SearchLibraries(self, Contexts: list[Teamcenter.Soa.Client.Model.ModelObject], SearchExprs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySearch.FilterExpression]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SearchLibraryElements(self, SearchInput: Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySearch.SearchLibraryElementsIn) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySearch.SearchResponse: ...

class LibrarySearchService:
    """
    
            This Search service is part of the overall Library Management capabilities. It provides
            operations to do various Search related functions in the context of a Library. As
            an example, the searchLibraryElements operation
            searches for Library Elements based on given search criteria.
            


Library Reference:

Lbr0SoaLibraryManagementStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> LibrarySearchService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
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
    def SearchLibraries(self, Contexts: list[Teamcenter.Soa.Client.Model.ModelObject], SearchExprs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySearch.FilterExpression]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def SearchLibraryElements(self, SearchInput: Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySearch.SearchLibraryElementsIn) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySearch.SearchResponse:
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

class LibrarySpecificationManagementRestBindingStub(LibrarySpecificationManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateActionSets(self, ActionSetInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.CreateActionSetsIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.CreateActionSetsResponse: ...
    def CreateApplicationData(self, AppDataInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.CreateApplicationDataIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.CreateApplicationDataResponse: ...
    def CreateSpecificationRules(self, SpecRulesInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.CreateSpecificationRulesIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.CreateSpecificationRulesResponse: ...
    def CreateSpecifications(self, CreateSpecInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.CreateSpecificationsIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.CreateSpecificationsResponse: ...
    def GetActionSetsInfo(self, ActionSetInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetActionSetsInfoIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetActionSetsInfoResponse: ...
    def GetApplicationData(self, AppDataInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetApplicationDataIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetApplicationDataResponse: ...
    def GetGenericPostPlacementData(self, GenPPDataInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GenericPostPlacementDataIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetPostPlacementDataResponse: ...
    def GetSpecificationRules(self, SpecRulesInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetSpecificationRulesIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetSpecificationRulesResponse: ...
    def GetSpecifications(self, GetSpecsInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetSpecificationsIn], ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetSpecificationsResponse: ...
    def SearchGenericPostPlacementParts(self, GenPPInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.SearchGenericPostPlacementsIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.SearchGenericPostPlacementPartsResp: ...
    def SearchPostPartsForCompConns(self, SearchPPInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.SearchPostPartsForCompConnsIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.SearchPostPartsForCompConnsResp: ...
    def SetGenericPostPlacementData(self, GenPPDatas: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GenericPostPlacementData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetInterfaceConstraintData(self, InterfaceConstraintInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.InterfaceConstraintDataInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def AttachSpecificationToLibraries(self, Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification, Libraries: list[Teamcenter.Soa.Client.Model.Strong.Lbr0Library]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DetachSpecificationFromLibraries(self, Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification, Libraries: list[Teamcenter.Soa.Client.Model.Strong.Lbr0Library]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetInterfaceConstraintData(self, Specifications: list[Teamcenter.Soa.Client.Model.Strong.Lbr0Specification]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.InterfaceConstraintDataResponse: ...

class LibrarySpecificationManagementService:
    """
    
            This service exposes operations related to Specification Management functionality
            in Teamcenter. The operations under this service allow users to create, manage and
            search the Specification objects and the related objects and data. This data could
            be used to perform searches based on the specification input data.
            

            Specifications provide a rule based configuration that guides the user to find only
            those components suitable to his design context.
            

            The rules (and other constructs) are formed using objects such as SpecificationRules,
            ActionSets, ActionDefinitions and ApplicationData.
            

            The 'Specification Management' functionality is an integral part of the 'Library
            Management' functionality. The Specifications objects created are to exist in context
            of the Libraries and are meant to be used to help filter and search such Library
            elements, which fulfill the constraints defined by the Specifications.
            

            Following operations could be performed -
            

Create, manage and search Specification objects, and the associated
            objects.
            
Perform search operations to search the design components in Libraries,
            based on specifications input.
            
Set and get Interface Constraints data and generic post-placements
            data.
            




Library Reference:

Lbr0SoaLibraryManagementStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> LibrarySpecificationManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateActionSets(self, ActionSetInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.CreateActionSetsIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.CreateActionSetsResponse:
        """    
             The operation creates ActionSet (Lbr0ActionSet) objects for the specified
             Specification object(s).
             
             This data is used to define the criteria for compatibility between two connections
             based on Connection types.
             
             (The types defined as the Source and target connection type make a valid combination
             for the connection).
             
             The operation should also be used to create and associate ActionDefinition (Lbr0ActionDefinition)
             objects to the ActionSets being created. The ActionDefinition objects define the
             action to find the additional parts that should be placed in the design when a connection
             is made as per definition in ActionSet.
             
             This data is defined using Specification Rules, and specifies the criteria to find
             the appropriate additional part. The ActionDefinition objects hold the reference
             to this information. Specification Rule objects created for this are added to the
             ActionDefinition objects.
             
             The operation could optionally also associate existing ApplicationData objects to
             the ActionSet being created.
             
             Consider following example -
             
             Suppose, in a design, if the designer wants to allow connection to be made between
             a 'Valve' and a 'Flange' part, only when both have connection type defined as "FLANGE",
             he can set the connection compatibility combination accordingly.
             
             ----------------------------------------------------------------
             
             Conn Type Source    |    Conn Type destination
             
             -----------------------------------------------------------------
             
             FLANGE                
             |     FLANGE
             
             -----------------------------------------------------------------
             
             For above data, user may want to define "Gasket" and "Bolt" as the parts to be placed
             in design, after the connection is made (post-placement parts).
             
             This operation provides a convenient mechanism to create a large set of connection
             compatibility definition data, and to set the post-placements data definition.
             
             Steps to be typically followed for creating data for above example -
             
             1.    Create Specification
             
             2.    Create Specification rules defining the constraints for
             the objects to be added as post-placement parts.
             
             3.    Using this info, create ActionSets and ActionDefinition
             objects, and pass in the Specification rules info as part of the input structure
             for creating ActionDefinition.
             

             Related operations:
             

getActionSetsInfo
             
createSpecifications
             
createSpecificationRules
             
createApplicationData
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param ActionSetInputs: 
                         The list of structures containing the input information for creating the ActionSet
                         objects.
             
        :return: 143336 - The type specified for action set object is invalid.
        """
        ...
    def CreateApplicationData(self, AppDataInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.CreateApplicationDataIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.CreateApplicationDataResponse:
        """    
             The operation creates the ApplicationData (Lbr0ApplicationData) objects.
             
             The objects represent the application specific data to be stored, along with other
             connection compatibility and post-placement information.
             

             Related operations:
             

getApplicationDataInfo
             
createActionSets
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param AppDataInputs: 
                         The list of structure objects containing the input information for creating the ApplicationData
                         objects.
             
        :return: 
        """
        ...
    def CreateSpecificationRules(self, SpecRulesInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.CreateSpecificationRulesIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.CreateSpecificationRulesResponse:
        """    
             This operation creates the Specification Rule (Lbr0SpecificationRule) objects
             for the given Specification.
             
             A Specification can have multiple Specification Rule objects associated with it.
             The Specification Rules define the constraints on the design which help to filter
             and find the right design components matching to the criteria defined by the rules.
             
             The specification rules (of type 'Specification') could be associated to the library
             nodes and the filter criteria of such specification rules is formed from the attributes
             of the library node on which they are added.
             
             When not associated with library nodes, they are treated as 'Global' rules (the rules
             applicable over complete library).
             

             Following are the valid Specification types -
             

Specification - The general node rules. These rules are used
             to form the constraints based on which the design components will be searched.
             


             This type is used for creating Global rules and the rules pertaining to specific
             nodes.
             
             For Global rules, the node Id must be specified as empty string.
             
             For the rules associated to specific rules, appropriate Library node must be specified.
             

Action - Rules representing the constraints specified for
             particular actions (defined by ActionSets). These rules are created for Action Sets.
             
InterfaceConstraint - Rules created for representing Interface
             Constraints, also called as Branch Compatibility. This type is used as an internal
             type.
             




             Related operations -
             

getSpecificationRules
             
createSpecifications
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param SpecRulesInputs: 
                         The list of Specification Rules input structure objects.
             
        :return: 
        """
        ...
    def CreateSpecifications(self, CreateSpecInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.CreateSpecificationsIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.CreateSpecificationsResponse:
        """    
             This operation creates the specification (Lbr0Specification) objects.
             
             The Specifications are created in context of the specified Library object(s).
             
             The Specification objects could be associated with multiple Specification Rules,
             and Action sets, and Application data objects which help define the various constraints.
             
             The API also provides the capability to create those associated objects, and return
             them as part of the output.
             

             A specification defines constraints to configure and control which design components
             to be returned during the search operations.
             

             Related operations -
             

getSpecifications
             
createSpecificationRules
             
createActionSets
             
createApplicationData
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param CreateSpecInputs: 
                         The input structure containing the details of the Specifications to be created.
             
        :return: 
        """
        ...
    def GetActionSetsInfo(self, ActionSetInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetActionSetsInfoIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetActionSetsInfoResponse:
        """    
             The operation returns the ActionSet (Lbr0ActionSet) objects found for the
             specified specification.
             
             Further filtering could be done based on the ActionSet property info (like id, name,
             description etc.) provided in the input search expressions.
             
             Information about the ActionDefinition objects and ApplicationData objects associated
             to the found ActionSet is also returned.
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param ActionSetInputs: 
                         The list of structures containing the input information for searching the ActionSet
                         objects.
             
        :return: 
        """
        ...
    def GetApplicationData(self, AppDataInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetApplicationDataIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetApplicationDataResponse: ...
    def GetGenericPostPlacementData(self, GenPPDataInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GenericPostPlacementDataIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetPostPlacementDataResponse:
        """    
             The operation returns the Generic Post placement data definition for the given Specification(s)
             and other criteria.
             
             This 'Generic post-placement data' concept defines the constraints for helping to
             search such components in design, which need to be automatically post-placed based
             on adding some specific design components.
             
             The generic post-placement data is stored in the database as a combination of ActionSet,
             ActionDefinition and SpecificationRule(s).
             
             This operation provides a convenient mechanism to get this data.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param GenPPDataInputs: 
                         The structure containing the input criteria to search the post-placement data.
             
        :return: 
        """
        ...
    def GetSpecificationRules(self, SpecRulesInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetSpecificationRulesIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetSpecificationRulesResponse:
        """    
             This operation searches the Specification Rule (Lbr0SpecificationRule) objects
             for the given Specifications.
             
             Further filtering could be done based on the Specification Rule property info (like
             rule id, name, description etc.) provided in the input search expressions.
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param SpecRulesInputs: 
                         The list of structures containing the info about Specification Rules being searched.
             
        :return: 
        """
        ...
    def GetSpecifications(self, GetSpecsInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetSpecificationsIn], ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GetSpecificationsResponse:
        """    
             This operation searches for available Specification objects in the specified libraries.
             Further filtering could be done based on the specification properties info (like
             Specification id, name, discipline etc.) provided in the input search expressions.
             

             The configured revision of the Specification will be returned based on the specified
             Configuration Context object. If Configuration Context object is not specified, all
             the revisions belonging to the specified library (and matching the filter criteria)
             will be returned.
             

             Related operations -
             
                 createSpecifications().
             


Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param GetSpecsInputs: 
                         The list of structures containing the input information. If this is specified empty,
                         then all the Specifications in the database will be searched and returned.
             
        :param ConfigContext: 
                         The Configuration Context object containing the configuration info based on the revision
                         rule. This info is used to identify the correct revision of the Specification object
                         to be used.
             
        :return: 143303 - Invalid number of inputs specified in the search criteria.
        """
        ...
    def SearchGenericPostPlacementParts(self, GenPPInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.SearchGenericPostPlacementsIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.SearchGenericPostPlacementPartsResp:
        """    
             The operation returns the valid and matching design parts (Library Elements) found
             based on the generic post-placement data definition for the given component (Library
             Element) in the specified Specification(s).
             
             This 'Generic post-placement data' concept defines the constraints for helping to
             search such components in design, which need to be automatically post-placed based
             on adding some specific design components.
             
             The generic post-placement data is stored in the database as a combination of ActionSet,
             ActionDefinition and SpecificationRule(s).
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param GenPPInputs: 
                         The list of input structures containing the source element info, for which the generic
                         post-placement parts are to be searched.
             
        :return: 
        """
        ...
    def SearchPostPartsForCompConns(self, SearchPPInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.SearchPostPartsForCompConnsIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.SearchPostPartsForCompConnsResp:
        """    
             This operation returns the matching design components (Library Elements) for the
             specified compatible types.
             
             The found design components will be used as post-placement part(s) for the compatible
             connection(s).
             
             Based on the input connection types, first the compatibility will be checked between
             these types.
             
             If found compatible, then based on the connection compatibility data stored, the
             library elements will be searched.
             

             Example: Consider scenario where in a design, the designer makes a connection between
             a 'Valve' and a 'Flange' part, consider both have connection types defined as 'FLANGE',
             and the connection compatibility for this combination is already set in database.
             The post placement part defined for this FLANGE - FLANGE compatibility is set as,
             say, 'Gasket'.
             
             This API takes in inputs the connection types of the Valve and Flange part, checks
             the compatibility between them, and searches for the matching Gaskets based on the
             criteria stored. The matching Gaskets thus found will be placed on the Flange part
             (target) of the above connection.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param SearchPPInputs: 
                         The list of structures containing the input information for creating or updating
                         the ActionSet objects.
             
        :return: 
        """
        ...
    def SetGenericPostPlacementData(self, GenPPDatas: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.GenericPostPlacementData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation sets or updates the definition for Generic Post-placement data for
             the given Specification.
             
             This concept defines the constraints for helping to search such components in design,
             which need to be automatically post-placed based on adding some specific design components.
             
             The generic post-placement data is stored in the database as a combination of ActionSet,
             ActionDefinition and SpecificationRule(s).
             
             This operation provides a convenient mechanism to create this data.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param GenPPDatas: 
                         The list of structures containing the input information for creating Generic Post-placement
                         data definition.
             
        :return: 
        """
        ...
    def SetInterfaceConstraintData(self, InterfaceConstraintInputs: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.InterfaceConstraintDataInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation sets the interface constraints (also called as Branch Compatibility
             data) data for the specified Specification object(s).
             
             The interface constraints data is used for identifying the compatible values for
             specified attributes.
             
             E.g. In a design, a Pipe with NPS=25 can only have a reducing Tee object which has
             NPS_BRANCH=10, 15 or 20, as valid match.
             
             Example of an interface constraints data set -
             
             --------------------------------------------------------------
             
             NPS (source)            |    NPS_BRANCH
             (destination)
             
             (Attribute Id=1001)    |    (Attribute Id=1008)
             
             --------------------------------------------------------------
             
             10                        |    4
             
             10                        |    2
             
             20                        |    2
             
             30                        |    30
             
             ---------------------------------------------------------------
             
             This data can be stored and used while searching the matching components during search
             operations, through interface constraints data definition.
             
             This data is stored in database as specification rules.
             
             This operation provides a convenient mechanism to create a large set of compatibility
             definition data.
             

             Related operations -
             
             getInterfaceConstraintData
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param InterfaceConstraintInputs: 

        :return: 
        """
        ...
    def AttachSpecificationToLibraries(self, Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification, Libraries: list[Teamcenter.Soa.Client.Model.Strong.Lbr0Library]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation attaches the given Library (Lbr0Library) objects to the specified
             Specification (Lbr0Specification) object.
             
             This is used to share the Specification between multiple libraries.
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param Specification: 
                         The Specification to which the specified Libraries will be attached to.
             
        :param Libraries: 
                         The list of libraries which will be attached to the specified Specification.
             
        :return: 
        """
        ...
    def DetachSpecificationFromLibraries(self, Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification, Libraries: list[Teamcenter.Soa.Client.Model.Strong.Lbr0Library]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation detaches the given Library(Lbr0Library) objects from specified Specification(Lbr0Specification)
             object.
             
             If no library is specified, then the given specification will be detached from all
             the associated Libraries.
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param Specification: 
                         The Specification which the specified Libraries will be detached from.
             
        :param Libraries: 
                         The libraries to be detached. If no library is specified, then the Specification
                         will be detached from all the associated libraries.
             
        :return: 143101 - Invalid library object is passed as an input.
        """
        ...
    def GetInterfaceConstraintData(self, Specifications: list[Teamcenter.Soa.Client.Model.Strong.Lbr0Specification]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibrarySpecificationManagement.InterfaceConstraintDataResponse:
        """    
             The operation returns the details of the interface constraints (also called as branch
             compatibility data), set for the Specification object(s) specified.
             

             Related operation:
             
             setInterfaceConstraintData
             


Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param Specifications: 
                         The list of the specifications for which the interface constraints data is requested.
             
        :return: 
        """
        ...

class LibraryUsageRestBindingStub(LibraryUsageService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def FindInstantiations(self, LibraryElements: list[Teamcenter.Soa.Client.Model.Strong.Lbr0LibraryElement]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryUsage.FindInstantiationsResponse: ...
    def PublishObjectsToLibrary(self, ObjectsInput: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryUsage.PublishObjectsIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryUsage.PublishObjectsResponse: ...
    def RetractObjectsFromLibrary(self, ObjectsInput: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryUsage.RetractObjectsIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryUsage.RetractObjectsResponse: ...
    def ValidateInstantiations(self, InstantiateIn: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryUsage.ValidateInstantiationIn]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class LibraryUsageService:
    """
    
            This service exposes operations related to using a Library in Teamcenter. Libraries
            provide control of how reusable components are managed and Instantiated into Designs.
            
            This service deals with aspects of using a Library in day to day operations, which
            include adding & removing objects from a Library and Instantiating objects from
            a Library into a Design.
            



Library Reference:

Lbr0SoaLibraryManagementStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> LibraryUsageService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def FindInstantiations(self, LibraryElements: list[Teamcenter.Soa.Client.Model.Strong.Lbr0LibraryElement]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryUsage.FindInstantiationsResponse:
        """    
             Find all the Design Components that  are registered as Instantiations of the given
             Library Elements.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param LibraryElements: 
                         The Library Elements whose Instantiations need to be found.
             
        :return: output
             structure.
        """
        ...
    def PublishObjectsToLibrary(self, ObjectsInput: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryUsage.PublishObjectsIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryUsage.PublishObjectsResponse:
        """    
             Publish (add) the given objects  to the specified Library (Node). This creates a
             new Library Element in the specified Library Node that  references the object. An
             object can be published to either a Classifying Library Node or a General Library
             Node. In case the Node specified here is a Classifying Library Node, classification
             properties &  values can be passed in for the creation of the Classification
             object. Passing in false for the doBulkPublish
             parameter ensures that all  custom logic and workflows configured for Publish are
             skipped during the operation.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param ObjectsInput: 
                         The objects to Publish to the Library Node alongwith relevant information for each
                         object.
             
        :return: 
        """
        ...
    def RetractObjectsFromLibrary(self, ObjectsInput: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryUsage.RetractObjectsIn]) -> Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryUsage.RetractObjectsResponse:
        """    
             Retract (remove) the given  objects from the specified Library (Node). This operation
             deletes the Library Element, which effectively  removes the Library Object from the
             Node. The Library Object is not deleted. The operation can also optionally  delete
             the Classification object that is referenced by this Library Element. Passing in
             false for the  doBulkRetract parameter ensures
             that all custom logic and workflows configured for Retract are skipped during the
             operation.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param ObjectsInput: 
                         The objects to Retract from the Library Node.
             
        :return: 143504 - if the element being retracted is instantiated in one or more Designs.
        """
        ...
    def ValidateInstantiations(self, InstantiateIn: list[Lbr0.Services.Strong.Librarymanagement._2014_10.LibraryUsage.ValidateInstantiationIn]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is used to validate whether an Instantiate can be done for the required
             Library Element(s).
             

Use Cases:

             Using a Library Element in a Design is known as Instantiation. Instantiation is a
             multi-step operation wherein the Library and the Design need to exchange information
             in order to validate the Instantiation and perform this operation.
             
             The first step in an Instantiation is typically to validate whether the Library Elements
             can be instantiated. The user calls this operation when such validation is to be
             done.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param InstantiateIn: 
                         Contains the Library Elements to instanatiate and any custom data that needs to be
                         passed in from the Design application.
             
        :return: 
        """
        ...

