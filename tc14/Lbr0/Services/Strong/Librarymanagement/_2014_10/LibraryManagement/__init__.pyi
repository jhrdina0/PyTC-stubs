import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AssignedContexts:
    """
    Contains information about the contexts assigned to one Library.
    """
    def __init__(self, ) -> None: ...
    Library: Teamcenter.Soa.Client.Model.Strong.Lbr0Library
    """The Library (Lbr0Library)"""
    Contexts: list[LibraryContextInfo]
    """The context(s) assigned to the Library."""

class AssignOrRemoveContextIn:
    """
    
            The input structure containing the details of the Library and Context to assign /
            remove.
            
    """
    def __init__(self, ) -> None: ...
    Library: Teamcenter.Soa.Client.Model.Strong.Lbr0Library
    """The Library for which the contexts are assigned / removed."""
    AssignContexts: list[LibraryContextInfo]
    """The context(s) to be assigned to the Library."""
    RemoveContexts: list[LibraryContextInfo]
    """The context(s) to be removed for the Library."""

class CreateHierarchiesIn:
    """
    
            This structure contains the input details for the creation of a Library Hierarchy
            within a Library.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    BoName: str
    """
            Business Object (BO) type name. If empty string is specified, the default BO type
            name, Lbr0Hierarchy, will be assumed.
            """
    Id: str
    """The ID of the Library Hierarchy. If empty string is specified, an ID would be auto-generated."""
    Name: str
    """The name of the Library Hierarchy. An empty string cannot be specified."""
    Description: str
    """The description of the Library Hierarchy"""
    Library: Teamcenter.Soa.Client.Model.Strong.Lbr0Library
    """The Library in which the Hierarchy is to be created"""
    AllowedMemberTypes: list[str]
    """
            The list of allowed object Member Types for the Library Hierarchy. This restricts
            the type of Library Objects that can be added to any Node in the Library Hierarchy.
            This overrides the definition on the Library.
            
            Each string in this list should be of the form '<TypeName>' or '<TypeName>*'.
            To specify a single type, use '<TypeName>'. To specify a type including all sub-types,
            use '<TypeName>*'.
            
"""
    AdditionalProperties: System.Collections.Hashtable
    """
            Any additional properties and their values to be set for the Library Hierarchy. This
            can also be used for properties defined for custom Hierarchy BO instances.
            
            The calling client is responsible for converting the different property types (int,
            float, date .etc) to a string using the appropriate toXXXString functions in the
            SOA client  framework's Property class.
            
"""

class CreateHierarchiesOutput:
    """
    
            A structure that contains information about the created Library Hierarchy with the
            corresponding clientID.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            The unmodified client id from CreateHierarchiesInput
            structure that can be used to identify the source input data.
            """
    Hierarchy: Teamcenter.Soa.Client.Model.Strong.Lbr0Hierarchy
    """The Library Hierarchy that was created."""

class CreateHierarchiesResponse:
    """
    
            The response structure containing information about the Library Hierarchy instances
            created.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateHierarchiesOutput]
    """A list of the created Hieararchy ( Lbr0Hierarchy ) objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service Data including partial errors that are mapped to the client id from the input.
            Created objects are also added to the Created list in the Service Data.
            """

class CreateLibrariesIn:
    """
    This structure contains the input details for the creation of a Library.
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    BoName: str
    """
            Business Object (BO) type name. If empty, the default BO type name, Lbr0Library,
            will be assumed.
            """
    Id: str
    """The ID of the Library to create. If empty string is specified, an ID would be auto-generated."""
    Name: str
    """The name of the Library. An empty string cannot be specified."""
    Description: str
    """The description of the Library."""
    LibraryType: str
    """Defines the scope the Library is used for. E.g. Domain or Project."""
    Disciplines: list[str]
    """The disciplines that this Library is used in. Example : Mechanical, Electrical."""
    Administrators: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            A list of administrators for the Library. The allowed value(s) are User or Group
            objects.
            """
    AllowedMemberTypes: list[str]
    """
            The list of allowed object Member Types for the Library. This restricts the type
            of 'Library Objects' that can be added to any Node in the Library.
            
            Each string in this list should be of the form '<TypeName>' or '<TypeName>*'.
            To specify a single type, use '<TypeName>'. To specify a type including all sub-types,
            use '<TypeName>*'.
            
"""
    Contexts: list[LibraryContextInfo]
    """A list of contexts that this Library is assigned to."""
    AdditionalProperties: System.Collections.Hashtable
    """
            Any additional properties and their values to be set for the Library. This can also
            be used for properties defined for custom Library BO instances.
            
            The calling client is responsible for converting the different property types (int,
            float, date .etc) to a string using the appropriate toXXXString functions in the
            SOA client  framework's Property class.
            
"""

class CreateLibrariesOutput:
    """
    
            A structure that contains information about the created Library with the corresponding
            clientID.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            The unmodified client id from CreateLibrariesInput
            structure that can be used to identify the source input data.
            """
    Library: Teamcenter.Soa.Client.Model.Strong.Lbr0Library
    """The Library that was created."""

class CreateLibrariesResponse:
    """
    The response structure containing information about the Library instances created.
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateLibrariesOutput]
    """A list of the created Library ( Lbr0Library ) instances."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service Data including partial errors that are mapped to the client id from the input.
            Created objects are also added to the Created list in the Service Data.
            """

class CreateNodesIn:
    """
    
            This structure contains the input details for the creation of a Library Hierarchy
            Node within a Library Hierarchy.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    BoName: str
    """
            Business Object (BO) type name. If empty, the default BO type name, Lbr0HierarchyNode,
            will be assumed.
            """
    Id: str
    """The ID of the Library Node. If empty string is specified, an ID would be auto-generated."""
    Name: str
    """The name of the Library Node. An empty string cannot be specified."""
    Description: str
    """The description of the Library Node."""
    AllowedMemberTypes: list[str]
    """
            The list of allowed object Member Types for the Library Node. This restricts the
            type of Library Objects that can be added to the Library Node. This overrides the
            definition on the Library Hierarchy.
            
            Each string in this list should be of the form 'TypeName' or 'TypeName*'.
            To specify a single type, use 'TypeName'. To specify a type including all
            sub-types, use 'TypeName*'.
            
"""
    Hierarchy: Teamcenter.Soa.Client.Model.Strong.Lbr0Hierarchy
    """
            The Library Hierarchy to which this node belongs. All Nodes belong to some Hierarchy
            in a Library.
            """
    ParentNode: Teamcenter.Soa.Client.Model.Strong.Lbr0HierarchyNode
    """
            The parent Node of this Node being created. If NULL, this indicates that a 'top-level'
            node should be created directly under the Library Hierachy object.
            """
    ClassificatioNode: Teamcenter.Soa.Client.Model.Strong.Cls0HierarchyNode
    """
            The Classification Node reference for this Library Node. If NULL, a 'General' Library
            Node will be created.
            """
    ReplicateClsNodes: bool
    """
            Indicates whether to replicate a Classification Node structure into the Library.
            If true, a Library Node structure will be created that reflects the Classification
            Node structure, starting with the Classification node specified using the classificationNode
            parameter.
            """
    AdditionalProperties: System.Collections.Hashtable
    """
            Any additional properties and their values to be set for the Library Node. This can
            also be used for properties defined for custom Node BO instances.
            
            The calling client is responsible for converting the different property types (int,
            float, date .etc) to a string using the appropriate toXXXString functions in the
            SOA client  framework's Property class.
            
"""

class CreateNodesOutput:
    """
    
            A structure that contains information about the created Library Hierarchy Node with
            the corresponding clientID. If replicateClsNodes was set as true in the input, the
            nodeHierarchy will contain all the corresponding nodes created to replicate the input
            Classification Node.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            The unmodified client id from CreateHierarchyInput
            structure that can be used to identify the source input data.
            """
    Node: Teamcenter.Soa.Client.Model.Strong.Lbr0HierarchyNode
    """The Library Node that was created."""
    NodeHierarchy: System.Collections.Hashtable
    """
            A map of Parent and Child Nodes created. Applicable in case replicateClsNodes was set to true. This then contains the entire
            hierarchy of Library Nodes created. To traverse this hierarchy, start with the key
            that is equal to node.
            """

class CreateNodesResponse:
    """
    
            The response structure containing information about the Library Hierarchy Node instances
            created.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateNodesOutput]
    """A list of the created Library Node ( Lbr0HierarchyNode ) objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service Data including partial errors that are mapped to the client id from the input.
            Created objects are also added to the Created list in the Service Data.
            """

class DeleteLibraryContentIn:
    """
    The input structure that specifies the Library related object to delete.
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """
            The object to delete. The supported objects are Lbr0Library,
            Lbr0Hierarchy and Lbr0HierarchyNode.
            
"""
    DeleteContent: bool
    """Flag to indicate whether the contents should be deleted recursively."""

class DeleteLibraryContentResponse:
    """
    
            The response contains a list of any input objects that could not be deleted.The service
            data contains any errors and the list of objects deleted by the operation.
            
    """
    def __init__(self, ) -> None: ...
    UndeletedObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of the undeleted ( Lbr0Library, Lbr0Hierarchy, Lbr0HierarchyNode
            ) objects.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service Data including partial errors that are mapped to the client id from the input.
            Deleted objects are also added to the Deleted list in the Service Data.
            """

class FindAssignedContextsResponse:
    """
    
            The response structure containing information about contexts assigned to the input
            Library instances.
            
    """
    def __init__(self, ) -> None: ...
    AssignedContexts: list[AssignedContexts]
    """The context(s) assigned to the Library."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData response."""

class LibraryContextInfo:
    """
    A structure that contains information about a context.
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """
            The context in which the Library is used. This can be a Project/Program (TcProject)
            or a Design Context.
            """
    IsOwningContext: bool
    """
            Specifies whether the Library is owned by the context. More than one context cannot
            be specified as an Owning Context for a Library.
            """

class LibraryManagement:
    """
    Interface LibraryManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AssignOrRemoveContexts(self, ContextInfo: list[AssignOrRemoveContextIn]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def CreateHierarchies(self, CreateInput: list[CreateHierarchiesIn]) -> CreateHierarchiesResponse:
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
    def CreateLibraries(self, CreateInput: list[CreateLibrariesIn]) -> CreateLibrariesResponse:
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
    def CreateNodes(self, CreateInput: list[CreateNodesIn]) -> CreateNodesResponse:
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
    def DeleteLibraryContent(self, DeleteIn: list[DeleteLibraryContentIn]) -> DeleteLibraryContentResponse:
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
    def FindAssignedContexts(self, Libraries: list[Teamcenter.Soa.Client.Model.Strong.Lbr0Library]) -> FindAssignedContextsResponse:
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

