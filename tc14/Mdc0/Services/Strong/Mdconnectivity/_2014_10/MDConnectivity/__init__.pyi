import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ConditionalElementGroupInfo:
    """
    
            The input values needed to create or update a conditional element group object. Zero
            or more ordered element groups will be attached to this object via a list and are
            defined in the OrderedElementGroupInfo structure.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    BoType: str
    """
            Conditional element group business object type, valid types are Mdc0ConditionalElementGroup
            and derived object types.
            """
    AttributeInfo: System.Collections.Hashtable
    """A map of attribute names and initial values pairs (string/string)."""
    ConditionalElementGroup: Teamcenter.Soa.Client.Model.Strong.Mdc0ConditionalElementGroup
    """
            An existing Mdc0ConditionalElementGroup object to update.  Empty on create.
            Required for update.
            """
    Elements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """
            List of Mdl0ConditionalElement objects contained in this conditional element
            group. Optional.
            """
    OrderedGroups: list[Teamcenter.Soa.Client.Model.Strong.Mdc0OrderedElementGroup]
    """
            List of Mdc0OrderedElementGroup objects contained in this conditional element
            group. Updated when an ordered element group object is created. Optional.
            """
    ModelObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The model object."""
    LastModifiedDateGuard: System.DateTime
    """
            This property is used only during the update operation. If it is not NULL, then updates
            are allowed only if the LMD is earlier to this date. If it is NULL, it is ignored
            and update is forced.
            """

class ConnectionElementInfo:
    """
    
            Structure represents the parameters required to create or update Mdc0ConnectionElement
            objects connecting the Mdc0PortArtifact objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    BoType: str
    """The type (Mdc0ConnectionElement) of the object to be created."""
    ConnectionObject: Teamcenter.Soa.Client.Model.Strong.Mdc0ConnectionElement
    """The Mdc0ConnectionElement object."""
    End1Object: Teamcenter.Soa.Client.Model.Strong.Mdc0PortArtifact
    """
            The Mdc0PortArtifact object. This acts as the first end of the connection.
            This may be NULL.
            """
    End1ClientId: str
    """
            ClientId that matches clientId on PortArtifactInfo structure. Must either
            set this or end1Object.
            
"""
    End2Object: Teamcenter.Soa.Client.Model.Strong.Mdc0PortArtifact
    """
            The Mdc0PortArtifact object. This acts as the other end of the connection.
            This may be NULL.
            """
    End2ClientId: str
    """
            ClientId that matches clientId on PortArtifactInfo structure. Must either set this
            or end2Object.
            """
    ModelObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The application model object (Smd0Model, Mdl0ApplicationModel)."""
    AttributeInfo: System.Collections.Hashtable
    """A map (string, string) of attribute names and initial values pairs."""
    LastModifiedDateGuard: System.DateTime
    """
            This property is used only during the update operation. If it is not NULL, then updates
            are allowed only if the LMD is earlier to this date. If it is NULL, it is ignored
            and update is forced.
            """

class ConnectionElementInsertInput:
    """
    
            Structure represents the parameters required to insert the Mdl0ConditionalElement
            object within a existing Mdc0OrderedElementGroup object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    Element: Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement
    """
            This is the new Mdl0ConditionalElement object that will be inserted into the
            Mdc0OrderedElementGroup.
            """
    Port1: Teamcenter.Soa.Client.Model.Strong.Mdc0PortArtifact
    """The port artifact that is considered to be the input of the inserted Mdl0ConditionalElement."""
    Port2: Teamcenter.Soa.Client.Model.Strong.Mdc0PortArtifact
    """The port artifact that is considered to be the output of the inserted Mdl0ConditionalElement."""
    AttributeInfo: System.Collections.Hashtable
    """
            A map of attribute names and initial values pairs (string/string) used when creating
            the new Mdc0ConnectionElement.
            """
    Connection: Teamcenter.Soa.Client.Model.Strong.Mdc0ConnectionElement
    """The Mdc0ConnectionElement to be split."""
    OrderedElemGroup: Teamcenter.Soa.Client.Model.Strong.Mdc0OrderedElementGroup
    """The Mdc0OrderdElementGroup to be updated."""

class CreateOrUpdateModelElementsInfo:
    """
    
            Structure represents the parameters required to create or update Mdl0ConditionalElement
            and its related objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    ModelElementObjects: list[ModelElementInfo]
    """A list of ModelElementInfo structures."""
    PortObjects: list[PortArtifactInfo]
    """A list of PortArtifactInfo structures."""
    ConnectionObjects: list[ConnectionElementInfo]
    """A list of ConnectionElementInfo structures."""

class CreateOrUpdateModelElementsResponse:
    """
    
            Structure contains a map of input client IDs to the objects that were created or
            updated and the Service Data.
            
    """
    def __init__(self, ) -> None: ...
    ClientIDMap: System.Collections.Hashtable
    """
            The map (string, BusinessObject) of clientIds to the corresponding objects that were
            created.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class ElementGroupInputInfo:
    """
    
            The input values needed to create or update a conditional element group and one or
            more ordered element groups.
            
    """
    def __init__(self, ) -> None: ...
    ConditionalElementGroups: ConditionalElementGroupInfo
    """Create or update info for conditional element group."""
    OrderedElementGroups: list[OrderedElementGroupInfo]
    """Create or update info for ordered element groups. Optional."""

class ElementGroupOutput:
    """
    The created or updated ordered element group and its ordered element groups.
    """
    def __init__(self, ) -> None: ...
    CondElementGroupClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify conditional element
            group return data elements and partial errors associated with this input structure.
            """
    CondElementGroup: Teamcenter.Soa.Client.Model.Strong.Mdc0ConditionalElementGroup
    """The created or updated conditional element group."""
    OrderedElementGroup: System.Collections.Hashtable
    """
            List of the created or updated ordered element groups by clientId of the OrderedElementGroupInfo
            structure.
            """

class ElementGroupResponse:
    """
    
            The created or updated conditional element group and zero or more ordered element
            groups.
            
    """
    def __init__(self, ) -> None: ...
    Results: list[ElementGroupOutput]
    """
            List of Mdc0CondtionalElementGroup object  and Mdc0OrderedElementGroup
            objects that were created or updated..
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard return;includes any error information. For create operations, the newly
            created items are returned in the Created List, while the container object from the
            input is returned in the Updated list.
            """

class ElementsOfConditionalElementGroupOutput:
    """
    Structure represents the output parameters of queryModelElementsOfElementGroup operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input queryModelElementsOfElementGroup element. This
            value is unchanged from the input, and can be used to identify this response element
            with the corresponding input element.
            """
    Elements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """A list of Mdl0ConditionalElement objects."""

class FindConnectionsOnPortInputInfo:
    """
    
            This structure represents the parameters required to identify the query for finding
            the connections associated with the port.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure. It may be empty.
            """
    Port: Teamcenter.Soa.Client.Model.Strong.Mdc0PortArtifact
    """The port to look for connections on."""
    Context: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """The configuration context (Configuration Context) object."""

class FindConnectionsOnPortOutput:
    """
    This structure contains the connections associated with the input port.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the FindConnectionsOnPortInputInfo.clientId.
            This can be used by the caller to indentify this data structure with the source input
            data.
            """
    Connection: Teamcenter.Soa.Client.Model.Strong.Mdc0ConnectionElement
    """The Mdc0ConnectionElement that contains the port."""

class FindConnectionsOnPortResponse:
    """
    This structure contains the search results along with the serviceData.
    """
    def __init__(self, ) -> None: ...
    Results: list[FindConnectionsOnPortOutput]
    """The list of the search results."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard return; includes any error information. An error will be reported if the
            search terms are improperly defined.
            """

class FindPortsGroupsInputInfo:
    """
    
            This structure represents the parameters required to identify the query for finding
            the elements and groups associated with the port.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.  It may be empty.
            """
    Port: Teamcenter.Soa.Client.Model.Strong.Mdc0PortArtifact
    """The port to look for connections on."""
    Context: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """The configuration context (Configuration Context) object."""

class FindPortsGroupsOutput:
    """
    This structure contains the elements and groups associated with the input port.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the FindPortsGroupsInputInfo.clientId.
            This can be used by the caller to indentify this data structure with the source input
            data.
            """
    Element: Teamcenter.Soa.Client.Model.Strong.Rlz0RealizedItem
    """The Rlz0RealizedItem that the port is attached to."""
    Connection: Teamcenter.Soa.Client.Model.Strong.Mdc0ConnectionElement
    """The Mdc0ConnectionElement that includes the port."""
    OrderedGroups: list[Teamcenter.Soa.Client.Model.Strong.Mdc0OrderedElementGroup]
    """
            The list of Mdc0OrderedConnectionGroups that the port's element is attached
            to.
            """
    ConditionalGroups: list[Teamcenter.Soa.Client.Model.Strong.Mdc0ConditionalElementGroup]
    """
            The list of Mdc0ConditionalElementGroups that the port's element is attached
            to.
            """

class FindPortsGroupsResponse:
    """
    This structure contains the search results along with the serviceData.
    """
    def __init__(self, ) -> None: ...
    Results: list[FindPortsGroupsOutput]
    """The list of the search results."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard return; includes any error information. An error will be reported if the
            search terms are improperly defined.
            """

class FindPortsInputInfo:
    """
    
            This structure represents the parameters required to identify the query for finding
            ports on the element or the configured structure.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.  It may be empty.
            """
    Element: Teamcenter.Soa.Client.Model.Strong.Rlz0RealizedItem
    """The Rlz0RealizedItem to search for ports on. Optional."""
    Partition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """The Ptn0Partition to search for ports on. Optional."""
    Context: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """The configuration context object to filter results by."""
    PortDiscipline: str
    """Filter the results based on port discipline. Optional."""
    PortDirection: str
    """Filter the results based on port direction. Optional."""

class FindPortsOutput:
    """
    
            This structure represents the output parameters of the findPorts
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the FindPortsInputInfo.clientId.
            This can be used by the caller to indentify this data structure with the source input
            data.
            """
    FreePorts: list[Teamcenter.Soa.Client.Model.Strong.Mdc0PortArtifact]
    """List of unconnected ports that match the search criteria."""
    ConnectedPorts: list[Teamcenter.Soa.Client.Model.Strong.Mdc0PortArtifact]
    """List of connected ports that match the search criteria."""

class FindPortsResponse:
    """
    This structure contains the found ports along with the serviceData.
    """
    def __init__(self, ) -> None: ...
    Results: list[FindPortsOutput]
    """Mapping of the search criteria to the list of matching ports."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard return; includes any error information.  An error will be reported if the
            search terms are improperly defined.
            """

class GetConditionalElementGroupInfo:
    """
    
            Structure represents the parameters required to query Mdc0ConditionalElementGroup
            objects contained in a given Ptn0Partition object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    PartitionObject: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """The Ptn0Partition object."""
    Context: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """The Configuration Context object to filter results by."""

class GetConditionalElemGroupAndOrderedElemGroupInfo:
    """
    
            Structure represents the parameters required to query the Mdc0OrderedElementGroup
            object and Mdc0ConditionalElementGroup object that contain the given Mdl0ConditionalElement
            object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    ConditionalElement: Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement
    """The Mdl0ConditionalElement or Mdc0ConnectionElement."""

class GetConditionalElemGroupAndOrderedElemGroupOutput:
    """
    Structure represents the output parameters of queryParentElementGroup operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input GetConditionalElemGroupAndOrderedConnGroupInfo element.
            This value is unchanged from the input, and can be used to identify this response
            element.
            """
    OrderedElemGroup: list[Teamcenter.Soa.Client.Model.Strong.Mdc0OrderedElementGroup]
    """The parent Mdc0OrderedElementGroup objects of a given Mdl0ConditionalElement."""
    ConditionalElemGroup: list[Teamcenter.Soa.Client.Model.Strong.Mdc0ConditionalElementGroup]
    """The parent Mdc0ConditionalElementGroup objects of a given Mdl0ConditionalElement."""

class GetConditionalElemGroupAndOrderedElemGroupResponse:
    """
    
            Structure contains the queried Mdc0OrderedElementGroup and Mdc0ConditionalElementGroup
            objects.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetConditionalElemGroupAndOrderedElemGroupOutput]
    """A list of GetConditionalElemGroupAndOrderedElemGroupOutput structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Added, updated, object data plus any error information."""

class GetConditionalElemGroupOutput:
    """
    Structure represents the output parameters of getConditionalElemGroups operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input GetConditionalElementGroupInfo element. This value
            is unchanged from the input, and can be used to identify this response element with
            the corresponding input element.
            """
    ConditionalElemGroupObjects: list[Teamcenter.Soa.Client.Model.Strong.Mdc0ConditionalElementGroup]
    """A list of Mdc0ConditionalElementGroup objects."""

class GetConditionalElemGroupsResponse:
    """
    Structure contains the queried Mdc0ConditionalElementGroup objects.
    """
    def __init__(self, ) -> None: ...
    Output: list[GetConditionalElemGroupOutput]
    """A list of GetConditionalElemGroupOutput structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class GetConnectionModelElementOutput:
    """
    Structure represents the output parameters of queryConnectionModelElements operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input GetConnectionLogicalElementsInputInfo element.
            This value is unchanged from the input, and can be used to identify this response
            element with the corresponding input element.
            """
    Elements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """
            A list of Mdl0ConditionalElement objects that were connected by the input
            Mdc0ConnectionElement object.
            """

class GetConnectionModelElementsInputInfo:
    """
    
            Structure represents the parameters required to query the Mdl0ConditionalElements
            objects connected by a given Mdc0ConnectionElement object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    ConnectionElement: Teamcenter.Soa.Client.Model.Strong.Mdc0ConnectionElement
    """The Mdc0ConnectionElement object."""

class GetConnectionModelElementsResponse:
    """
    Structure contains the queried Mdl0ConditionalElements objects.
    """
    def __init__(self, ) -> None: ...
    Output: list[GetConnectionModelElementOutput]
    """A list of GetConnectionModelElementsOutput structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class GetElementsOfConditionalElementGroupInfo:
    """
    
            Structure represents the parameters required to query the Mdl0ConditionalElement
            objects contained in a given Mdc0ConditionalElementGroup object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    ConditionalElemGroup: Teamcenter.Soa.Client.Model.Strong.Mdc0ConditionalElementGroup
    """The Mdc0ConditionalElementGroup object."""
    Context: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """The configuration context object to filter results by."""
    BoTypes: list[str]
    """The business object types to be returned."""

class GetElementsOfConditionalElemGroupResponse:
    """
    Structure contains the queried Mdl0ConditionalElement objects.
    """
    def __init__(self, ) -> None: ...
    Output: list[ElementsOfConditionalElementGroupOutput]
    """A list of ElementsOfConditionalElementGroupOutput structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class GetIdentityInfo:
    """
    Structure represents the parameters required to identify the equipment.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    ModelElement: Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement
    """The object (Mdl0ConditionalElement)  for which the identity is to be generated."""
    ModelObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The application model (WorkspaceObject) object."""
    Context: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """The configuration context (ConfigurationContext) object."""

class GetIdentityOutput:
    """
    Structure represents the output parameters of getIdentity operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input GetIdentityInfo
            element. This value is unchanged from the input, and can be used to identify this
            response element with the corresponding input element.
            """
    Identity: str
    """The identity of model element in given partition."""

class GetIdentityResponse:
    """
    Structures containing the string representing the identity of the equipment.
    """
    def __init__(self, ) -> None: ...
    Output: list[GetIdentityOutput]
    """A list of equipment identity."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class GetOrderedElementGroupsInfo:
    """
    
            Structure represents the parameters required query Mdc0OrderedElementGroup
            objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    ConditionalElemGroup: Teamcenter.Soa.Client.Model.Strong.Mdc0ConditionalElementGroup
    """
            The Mdc0ConditionalElementGroup object used to query the objects in the given
            configuration.
            """
    ModelObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The application model object."""
    Context: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """The ConfigurationContext object."""

class GetOrderedElementGroupsOutput:
    """
    Structure represents the output parameters of getOrderedElementGroups operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input GetOrderedElementGroupsInfo element. This value
            is unchanged from the input, and can be used to identify this response element with
            the corresponding input element.
            """
    OrderedElementGroupObjects: list[Teamcenter.Soa.Client.Model.Strong.Mdc0OrderedElementGroup]
    """A list of Md0OrderedElementGroup objects."""

class GetOrderedElementGroupsResponse:
    """
    
            Structure containing the response of the getOrderedElementGroups operation
            and the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetOrderedElementGroupsOutput]
    """A list of GetOrderedElementGroupsOutput structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class GetRealizedLogicalElementsInfo:
    """
    
            Structure represents the parameters required to return all the realized Rlz0RealizedItem
            objects for the given ItemRevision object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The ItemRevision object"""
    ModelObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The application model object"""
    Context: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """The Configuration Context object"""

class GetRealizedLogicalElementsOutput:
    """
    Structure represents the output parameters of getRealizeLogicalElements operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input GetRealizedLogicalElementsInfo element. This value
            is unchanged from the input, and can be used to identify this response element with
            the corresponding input element.
            """
    LogicalElements: list[Teamcenter.Soa.Client.Model.Strong.Rlz0RealizedItem]
    """A list of Rlz0RealizedItem objects"""

class GetRealizedLogicalElementsResponse:
    """
    
            Structure containing the output of the getRealizedLogicalElements operation
            and the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetRealizedLogicalElementsOutput]
    """A list of GetRealizedLogicalElementsOutput structures"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class ModelElementInfo:
    """
    
            Structure represents the parameters required to create or update Mdl0ConditionalElement
            and its related objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    BoType: str
    """
            The type (Mdl0ConditionalElement) of the object to be created. Mdl0ConditionalElement
            is an abstract class. The input must be a persistent type name.
            """
    ModelElement: Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement
    """
            The Mdl0ConditionalElement object. It should be passed as NULL for creating
            a new object.
            """
    ParentModelElementClientId: str
    """
            The clientId of the ModelElementInfo which
            will be parent of this element.
            """
    ParentModelElement: Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement
    """
            The Mdl0ConditionalElement object. If set, this will be set as the presented
            parent of the Mdl0ConditionalElement created as "subordinate" with
            the input data.
            """
    ModelObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The Mdl0ModelElement object."""
    SourceObject: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            The ItemRevision object which the Mdl0ConditionalElement object is
            realized from. It will be NULL if there is no realization.
            """
    UpdateSubordinates: bool
    """If true, subordinates will be updated; otherwise, not."""
    LastModifiedDateGuard: System.DateTime
    """
            This property is used only during the update operation. If it is not NULL, then updates
            are allowed only if the LMD is earlier to this date. If it is NULL, it is ignored
            and update is forced.
            """
    AttributeInfo: System.Collections.Hashtable
    """A map (string, string) of attribute names and initial values pairs."""
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """
RevisionRule to be applied to configure the structure of the source object.
            The configured structure objects will be realized in to the Application Model.
            """
    VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule
    """The VariantRule object."""
    BomView: str
    """The BOMView name which is used to create the BOMView window."""

class OrderedElementGroupInfo:
    """
    
            The input values needed to create or update an ordered element group. This ordered
            group will be contained in a list in the conditional element group defined in the
            ConditionalElementGroupInfo structure.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    BoType: str
    """
            Ordered element group business object type, valid types are Mdc0OrderedElementGroup
            and derived object types.
            """
    OrderedElementGroup: Teamcenter.Soa.Client.Model.Strong.Mdc0OrderedElementGroup
    """
            An existing Mdc0OrderedElementGroup object to update.        
            Empty on create. Required for update.
            """
    AttributeInfo: System.Collections.Hashtable
    """A map of attribute names and initial values pairs (string/string). Optional."""
    StartElement: Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement
    """This is the beginning process equipment in the ordered element group. Optional."""
    EndElement: Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement
    """This is the ending process equipment in the ordered element group. Optional."""
    Elements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """
            Ordered list of Mdl0ConditionalElement objects contained in this ordered element
            group. Optional.
            """
    Specification: Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement
    """Specification object. Optional."""
    LastModifiedDateGuard: System.DateTime
    """
            This property is used only during the update operation. If it is not NULL, then updates
            are allowed only if the LMD is earlier to this date. If it is NULL, it is ignored
            and update is forced.
            """

class OrderedElementGroupInput:
    """
    
            The input values needed to insert additional elements into an existing ordered element
            group.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    OrderedElementGroup: Teamcenter.Soa.Client.Model.Strong.Mdc0OrderedElementGroup
    """An existing Mdc0OrderedElementGroup object to update. This is required."""
    Elements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """
            Ordered list of Mdl0ConditionalElement objects to be inserted into the existing
            ordered element list.
            """
    StartIndex: int
    """
            Index where elements are to be inserted in the existing ordered element list. Index
            must be greater than 0. If value is greater than length of current list, elements
            will be added to the end of the list.
            """
    LastModifiedDateGuard: System.DateTime
    """
            This property is used only during the update operation. If it is not NULL, then updates
            are allowed only if the LMD is earlier to this date. If it is NULL, it is ignored
            and update is forced.
            
"""

class PortArtifactInfo:
    """
    
            Structure represents the parameters required to create or update Mdc0PortArtifact
            objects for the given Mdl0ConditionalElement object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    BoType: str
    """The type name (Mdc0PortArtifact) of the object to be created."""
    PortObject: Teamcenter.Soa.Client.Model.Strong.Mdc0PortArtifact
    """The Mdc0PortArtifact object."""
    ModelElementClientId: str
    """The clientId of the LogicalElementsInfo structure."""
    ModelElement: Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement
    """The Mdl0ConditionalElement object."""
    AttributeInfo: System.Collections.Hashtable
    """A map (string, string) of attribute names and initial values pairs."""
    LastModifiedDateGuard: System.DateTime
    """
            This property is used only during the update operation. If it is not NULL, then updates
            are allowed only if the LMD is earlier to this date. If it is NULL, it is ignored
            and update is forced.
            """
    SourceObject: Teamcenter.Soa.Client.Model.Strong.GeneralDesignElement
    """
            The GeneralDesignElement object which the Mdc0PortArtifact object is
            realized from. It will be NULL if there is no realization.
            """

class QueryOrderedElementGroupByPartitionListInputInfo:
    """
    The input values needed to query an ordered element group.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    Discipline: str
    """
            The discipline of Mdc0ConnectionElement elements to filter on (Electrical,
            Hydraulic, Instrumentation).
            """
    OrderedElementGroup: Teamcenter.Soa.Client.Model.Strong.Mdc0OrderedElementGroup
    """An existing Mdc0OrderedElementGroup object to query.         This is required."""
    Partition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """The Ptn0Partition object to check."""
    Context: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """The ConfigurationContext object to filter results by."""

class QueryOrderedElementGroupByPartitionOutput:
    """
    The structure contains the query output.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the QueryOrderedElementGroupByPartitionListInput.clientId.
            This can be used by the caller to indentify this data structure with the source input
            data.
            """
    Elements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """List of Mdl0ConditionalElement objects found matching the query parameters."""

class QueryOrderedElementGroupByPartitionResponse:
    """
    
            The response containing a list of QueryOrderedElementGroupByPartitionOutput
            and ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Outputs: list[QueryOrderedElementGroupByPartitionOutput]
    """List of result elements found for each search."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard return; includes any error information."""

class ReverseOrderedElementGroupInputInfo:
    """
    The input values needed to reverse an ordered element group.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    OrderedElementGroup: Teamcenter.Soa.Client.Model.Strong.Mdc0OrderedElementGroup
    """An existing Mdc0OrderedElementGroup object.         This is required."""
    LastModifiedDateGuard: System.DateTime
    """
            This property is used only during the update operation. If it is not NULL, then updates
            are allowed only if the LMD is earlier to this date. If it is NULL, it is ignored
            and update is forced.
            
"""

class SplitOrderedElementGroupInputInfo:
    """
    
            The input values needed to split an ordered element group. The Mdc0OrderedElementGroup
            object specified in the input will be split into two objects. The split index will
            determine the end of the ordered element list of the orginal object. The existing
            object will have its end element updated to the element at index plus one and the
            new object will also have as its start element the element specified at index plus
            one. The existing object's ordered element list will be shortened to end at the element
            at index. The new objects ordered element list will comprise elements starting at
            index plus two of the existing Mdc0OrderedElementGroup object. The new object's
            end element will the be set to the existing object's end element.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    OrderedElementGroup: Teamcenter.Soa.Client.Model.Strong.Mdc0OrderedElementGroup
    """
            An existing Mdc0OrderedElementGroup object to split.        
            This is required.
            """
    ConditionalElementGroup: Teamcenter.Soa.Client.Model.Strong.Mdc0ConditionalElementGroup
    """
            The conditional element group object that contains the ordered element group object
            being split into two ordered element group objects.
            """
    Index: int
    """
            The first element in an ordered element list is index 1. The index specifies where
            the split happens in the ordered element list of the specified Mdc0OrderedElementGroup
            object. The split element index specifies the end of the original ordered element
            list, index plus one is the new start element of the second Mdc0OrderedElementGroup
            object and elements starting at index plus two will comprise the elements in the
            new Mdc0OrderedElementGroup object's ordered element list.
            """
    LastModifiedDateGuard: System.DateTime
    """
            This property is used only during the update operation. If it is not NULL, then updates
            are allowed only if the LMD is earlier to this date. If it is NULL, it is ignored
            and update is forced.
            
"""

class SplitOrderedElementGroupOutput:
    """
    
            The output that contains the existing Mdc0OrderedElementGroup object split
            and the newly created Mdc0OrderedElementGroup object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the SplitOrderedElementGroupInput.clientId. This can be
            used by the caller to indentify this data structure with the source input data.
            """
    OrderedElementGroups: list[Teamcenter.Soa.Client.Model.Strong.Mdc0OrderedElementGroup]
    """The list contains the modified and created Mdc0OrderedElementGroup objects."""

class SplitOrderedElementGroupResponse:
    """
    Response that contains a list of SplitOrderedElementGroupOutput and ServiceData.
    """
    def __init__(self, ) -> None: ...
    Outputs: list[SplitOrderedElementGroupOutput]
    """Response for each Mdc0OrderedElementGroup object split."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard return; includes any error information."""

class MDConnectivity:
    """
    Interface MDConnectivity
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def QueryOrderedElementGroupByPartition(self, Input: list[QueryOrderedElementGroupByPartitionListInputInfo]) -> QueryOrderedElementGroupByPartitionResponse:
        """    
             This operation finds all elements that are in common between an Mdc0OrderedElementGroup
             object and a Ptn0Partition object and filtered by discipline.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         A list of structures which hold data used to search elements in the <b>Mdc0OrderedElementGroup</b>
                         object.
             
        :return: 
        """
        ...
    def CreateOrUpdateElementGroups(self, Input: list[ElementGroupInputInfo]) -> ElementGroupResponse:
        """    
             Create or update of an Mdc0ConditionalElementGroup (conditional element group)
             and zero or more Mdc0OrderedElementGroup (ordered element group) objects in
             an application model (Cpd0CollaborativeDesign) based on input structure.
             The value of the conditional element group (conditionalElementGroup) and ordered
             element group (orderedConnGroup) input parameters will control whether we are performing
             a create or an update operation. A non null value will cause an update operation
             to be performed. Creation and update operations can only be mixed if the conditional
             element group exists and you want to create an additional ordered element group.
             

             An ordered element group is attached to an Mdc0ConditionalElementGroup (conditional
             element group, known as a run in P&ID applications) so the conditional element
             group object has to be created before the create ordered element group action can
             be performed. The conditional element groups role is to manage a list of ordered
             element group objects. It also maintains a list of Mdl0ConditionalElements
             objects not in the conditional element group.
             

             An ordered element group object for example in the P&ID application is referred
             to as a branch and its basic role is to manage an ordered list of Mdc0ConditionalElement
             objects along with a begin and end Mdc0CondtionalElement. The create or update
             operation is used to set properties on the Mdc0OrderedElementGroup object
             which include the ordered list of equipment's, beginning and ending equipment and
             the optional Specification library property. The library specification contains for
             example a Pipe Specification in the P&ID application.
             

             Multiple sets of conditional element groups and its associated ordered element group
             objects can be created or updated by passing in a list of input structures.
             


Use Cases:

             Use Case 1: Creation of new conditional element group and zero or more ordered element
             groups.
             


For the conditional element group the conditionalElementGroup
             parameter is empty.
             
The attributeInfo parameter defines the Mdc0ConditionalElementGroup
             object name. Any additional attributes will also be applied at this time.
             
If Mdl0ConditionalElements are to be added to the conditional
             element group at creation time they are provided in the elements
             parameter.
             
At creation time the list of ordered element groups is ignored.
             
For each entry in the input list of ordered element groups, an ordered
             element group is created.
             
The attributeInfo parameter
             defines optional properties on the Mdc0OrderedElementGroup object, if provided,
             they are applied at this time.
             
The properties of elements,
             startElement, endElement,
             and specification in the Mdc0OrderedElementGroup
             are optional at creation time. If provided, they are stored as properties. If not
             provided, then they can be set during an update.
             



             Use Case 2: Update of existing conditional element group.
             


For the conditional element group update the conditionalElementGroup parameter is provided.
             
If Mdl0ConditionalElements are to be updated in the conditional
             element group they are provided.
             
Update any values passed in via the attributeInfo
             parameter.
             
To remove ordered element groups, the list of updated ordered element
             groups is provided.
             



             Use Case 3: Creation of new ordered element group.
             

Ordered element group elements are always created and attached to
             a list in the conditional element group defined in the ConditionalElementGroupInfo
             structure. Without a valid conditional element group, either a valid conditionalElementGroup parameter had to be defined or a conditional
             element group just created, the ordered element group create operation will not succeed.
             
The input parameter orderedElementGroup
             is null, so we are doing a create operation.
             
The attributeInfo parameter defines optional properties on the Mdc0OrderedElementGroup
             object, if provided, they are applied at this time.
             
The properties of elements,
             startElement, endElement,
             and specification in the Mdc0OrderedElementGroup
             are optional at creation time. If provided, they are stored as properties. If not
             provided, then they can be set during an update.
             




             Use Case 4: Update of existing ordered element group
             

The conditionalElementGroup
             must be a valid id.
             
The input parameter orderedElementGroup
             is not null, perform an update of that object.
             
Update any values passed in via the attributeInfo parameter.
             
Update elements property
             if it is supplied.
             
Update startelement and endelement property if they are supplied.
             
Update specification property
             if it is supplied.
             



Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         Data used to create or update an <b>Mdc0ConditionalElementGroup</b> object and zero
                         or more  <b>Mdc0OrderedElementGroup</b> objects. It is a list of ElementGroupInputInfo
                         structures.
             
        :return: 
        """
        ...
    def CreateOrUpdateModelElements(self, Input: list[CreateOrUpdateModelElementsInfo]) -> CreateOrUpdateModelElementsResponse:
        """    
             This operation creates or updates Mdl0ConditionalElement, Mdc0PortArtifact
             and Mdc0ConnectionElement objects. Using this API, applications can create
             and update model elements, their ports and the connections between the model elements
             in bulk, giving better through put that might otherwise be achieved using standard
             object create and update API.
             

Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         Holds information for creating and updating objects of <b>Mdl0ConditionalElement,
                         Mdc0PortArtifact</b> and<b> Mdc0ConnectionElement.</b>

        :return: 
        """
        ...
    def FindConnectionsOnPort(self, Input: list[FindConnectionsOnPortInputInfo]) -> FindConnectionsOnPortResponse:
        """    
             This operation finds the Mdc0ConnectionElement, if any, that contains a Mdc0PortArtifact.
             

             Multiple queries may be done by passing in a list of input structures.
             

Use Cases:

             Use Case 1: The client wants to find the connection that includes a particular port.
             

Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         The search criteria.
             
        :return: 
        """
        ...
    def FindPorts(self, Input: list[FindPortsInputInfo]) -> FindPortsResponse:
        """    
             This operation finds all Mdc0PortArtifacts that are associated with an Rlz0RealizedItem
             or a Ptn0Partition. The results can be filtered by port discipline and direction
             (string values). Port artifacts that match the search criteria are sorted into one
             of two groups, depending on whether or not the port is connected or free, and both
             groups are included in the response.
             

             Multiple queries may be done by passing in a list of input structures.
             


Use Cases:

             Use Case 1: The client wants to find the connected/unconnected ports attached to
             an element in a configured structure, filtered by port discipline.
             


The partition and portDirection input parameters will be empty.
             


             Use Case 2: The client wants to find the connected/unconnected ports in a configured
             structure, filtered by port direction.
             


The element and portDiscipline input parameters will be empty.
             



Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         The search criteria.
             
        :return: 
        """
        ...
    def FindPortsGroups(self, Input: list[FindPortsGroupsInputInfo]) -> FindPortsGroupsResponse:
        """    
             This operation takes a Mdc0PortArtifact as input and return the Rlz0RealizedItem,
             Mdc0ConnectionElement, Mdc0OrderedConnectionGroup (branch), and Md0ConditionalElementGroup
             (run) objects associated with that port, if any.
             
             Multiple queries may be done by passing in a list of input structures.
             

Use Cases:

             Use Case 1: The client wants to find the ordered groups and connection groups that
             a port is a member of.
             

Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         The search criteria.
             
        :return: 
        """
        ...
    def GetConditionalElemGroups(self, Input: list[GetConditionalElementGroupInfo]) -> GetConditionalElemGroupsResponse:
        """    
             Given an object of Ptn0Partition, this operation returns all Mdc0ConditionalElementGroup
             objects contained in that partition object.
             

Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         Holds the information required to query the objects of <b>Mdc0ConditionalElementGroup</b>
                         in a given partition.
             
        :return: 
        """
        ...
    def GetIdentity(self, Input: list[GetIdentityInfo]) -> GetIdentityResponse:
        """    
             An equipment may have different identifier in the different partition scheme. It
             may also be different in different context. This operation return the identity of
             the equipment in the context it is used.
             

Use Cases:

             Equipment E2 may have an identifier L-1/L-2/E2 based on the Location breakdown while
             the same equipment E2 may have identifiers S01:02:03:E2 and S:01-02-03-E2 in the
             context of Context1 and Context2 respectively.
             

Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         A list of structures which hold the equipment and the application model information
                         to get the identity.
             
        :return: 
        """
        ...
    def GetOrderedElementGroups(self, Input: list[GetOrderedElementGroupsInfo]) -> GetOrderedElementGroupsResponse:
        """    
             This operation returns the list of Mdc0OrderedConnectionGroup objects in a
             given Product Design by applying the given configuration.
             

Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         Holds information about the<b> Mdc0ConditionalElementGroup</b> object to query the
                         <b>Mdc0OrderedConnectionGroup</b> objects.
             
        :return: 
        """
        ...
    def GetRealizedLogicalElements(self, Input: list[GetRealizedLogicalElementsInfo]) -> GetRealizedLogicalElementsResponse:
        """    
             This operation returns all the Rlz0RealizedItem objects realized from the
             ItemRevision object in a given Product Design object by applying the given configuration.
             

Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         Holds information  about querying the realized <b>Rlz0RealizedItem</b> objects from
                         an <b>ItemRevision</b> object.
             
        :return: 
        """
        ...
    def InsertConnectionElement(self, Input: list[ConnectionElementInsertInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation allows a new inline Mdl0ConditionalElement object to be placed
             within an existing Mdc0OrderedElementGroup object.  The existing connection
             will be broken, by updating its output port (mdc0End2), with the input port
             of the inserted logical element (port1).
             

             A new Mdc0ConnectionElement object will be created using the output port of
             the new logical element (port2) connected to its input port. The new connection output
             port will then be connected to the input of the existing logical element.    Both
             the new Mdc0ConnectionElement and new Mdl0ConditionalElement will be
             inserted in the existing Mdc0OrderedElementGroup.
             


Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         A list of structures which hold data used to update an <b>Mdc0ConnectionElement</b>
                         object and create a new <b>Mdc0ConnectionElement</b>.
             
        :return: 
        """
        ...
    def InsertOrderedElementGroupElements(self, Input: list[OrderedElementGroupInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Update of an Mdc0OrderedElementGroup (ordered element group) in an application
             model (Cpd0CollaborativeDesign) based on input structure.
             

             An ordered element group object for example in the P&ID application is referred
             to as a branch and its basic role is to manage an ordered list of Mdc0ConditionalElement
             objects. This update will insert additional Mdc0ConditionalElement elements
             into the existing ordered element list at the start index specified in the input
             parameters. The start index specified must be greater than 0. The element list starts
             at element one. If the start index value is greater than the length of the existing
             element list, then the new elements are added to the end of the existing list. If
             the index is not greater than the length then the new elements are inserted at the
             specified start index.
             

             Multiple ordered element group objects can be updated by passing in a list of input
             structures.
             


Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         A list of structures which hold data used to update an <b>Mdc0OrderedElementGroup</b>
                         object.
             
        :return: Â Â Â Â
        """
        ...
    def QueryConnectionModelElements(self, Input: list[GetConnectionModelElementsInputInfo]) -> GetConnectionModelElementsResponse:
        """    
             This operation finds the Mdl0ConditionalElements objects that are connected
             by an Mdc0ConnectionElement object.
             

Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         A list of structures which hold data used to find the <b>Mdl0ConditionalElements</b>
                         connected by a   <b>Mdc0ConnectionElement</b> object.
             
        :return: 
        """
        ...
    def QueryModelElementsOfElementGroup(self, Input: list[GetElementsOfConditionalElementGroupInfo]) -> GetElementsOfConditionalElemGroupResponse:
        """    
             This operation returns all Mdl0ConditionalElement objects of a given Mdc0ConditionalElementGroup
             object.
             

Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         Holds the information about <b>Mdc0ConditionalElementGroup</b> object for querying
                         the elements.
             
        :return: 
        """
        ...
    def QueryParentElementGroup(self, Input: list[GetConditionalElemGroupAndOrderedElemGroupInfo]) -> GetConditionalElemGroupAndOrderedElemGroupResponse:
        """    
             This operation finds the parent Mdc0ConditionalElementGroup object and Mdc0OrderedElementGroup
             object that are associated with given Mdl0ConditionalElement object.
             

Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         Holds the informaiton about the <b>Mdc0ConnectionElement</b> object for querying
                         the elements
             
        :return: 
        """
        ...
    def ReverseOrderedElementGroupElements(self, Input: list[ReverseOrderedElementGroupInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Reverse of an Mdc0OrderedElementGroup (ordered element group) in an application
             model (Cpd0CollaborativeDesign) based on the input structure.
             
             An ordered element group object for example in the P&ID application is referred
             to as a branch and its basic role is to manage an ordered list of Mdc0CondtionalElement
             objects. This operation reverses the order of elements in the ordered element group
             which includes the start and end element as well the elements in the ordered element
             list.
             


Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         A list of structures which hold data used to reverse an <b>Mdc0OrderedElementGroup</b>
                         object.
             
        :return: 
        """
        ...
    def SplitOrderedElementGroupElements(self, Input: list[SplitOrderedElementGroupInputInfo]) -> SplitOrderedElementGroupResponse:
        """    
             Split of an Mdc0OrderedElementGroup (ordered element group) in an application
             model (Cpd0CollaborativeDesign) based on input structure.
             
             An ordered element group object for example in the P&ID application is referred
             to as a branch and its basic role is to manage an ordered list of Mdc0ConditionalElement
             objects. This splits the ordered element group into multiple ordered element groups.
             

             The input contains an index where the ordered element group will be split. The index
             must point to a connection element and it must be followed by a logical element.
             The logical element will represent the ending element of the original ordered element
             group and the starting element of the new ordered element group. All elements in
             the original ordered element list after the ending/starting element will become the
             new ordered element list in the created ordered element group object. The ending
             element of the new ordered element group will be set to the ending element of the
             existing ordered element group.
             


Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         A list of structures which hold data used to split an <b>Mdc0OrderedElementGroup</b>
                         object.
             
        :return: 
        """
        ...

