import Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity
import Mdc0.Services.Strong.Mdconnectivity._2016_10.MDConnectivity
import Mdc0.Services.Strong.Mdconnectivity._2017_11.MDConnectivity
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class MDConnectivityRestBindingStub(MDConnectivityService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def QueryOrderedElementGroupByPartition(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.QueryOrderedElementGroupByPartitionListInputInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.QueryOrderedElementGroupByPartitionResponse: ...
    def CreateOrUpdateElementGroups(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.ElementGroupInputInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.ElementGroupResponse: ...
    def CreateOrUpdateModelElements(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.CreateOrUpdateModelElementsInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.CreateOrUpdateModelElementsResponse: ...
    def FindConnectionsOnPort(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.FindConnectionsOnPortInputInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.FindConnectionsOnPortResponse: ...
    def FindPorts(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.FindPortsInputInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.FindPortsResponse: ...
    def FindPortsGroups(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.FindPortsGroupsInputInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.FindPortsGroupsResponse: ...
    def GetConditionalElemGroups(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetConditionalElementGroupInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetConditionalElemGroupsResponse: ...
    def GetIdentity(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetIdentityInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetIdentityResponse: ...
    def GetOrderedElementGroups(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetOrderedElementGroupsInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetOrderedElementGroupsResponse: ...
    def GetRealizedLogicalElements(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetRealizedLogicalElementsInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetRealizedLogicalElementsResponse: ...
    def InsertConnectionElement(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.ConnectionElementInsertInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def InsertOrderedElementGroupElements(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.OrderedElementGroupInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def QueryConnectionModelElements(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetConnectionModelElementsInputInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetConnectionModelElementsResponse: ...
    def QueryModelElementsOfElementGroup(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetElementsOfConditionalElementGroupInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetElementsOfConditionalElemGroupResponse: ...
    def QueryParentElementGroup(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetConditionalElemGroupAndOrderedElemGroupInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetConditionalElemGroupAndOrderedElemGroupResponse: ...
    def ReverseOrderedElementGroupElements(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.ReverseOrderedElementGroupInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SplitOrderedElementGroupElements(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.SplitOrderedElementGroupInputInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.SplitOrderedElementGroupResponse: ...
    def FindConnectionsOnPort2(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.FindConnectionsOnPortInputInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2016_10.MDConnectivity.FindConnectionsOnPortResponse2: ...
    def QueryParentElementGroup2(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2016_10.MDConnectivity.GetParentElementGroupInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2016_10.MDConnectivity.GetParentElementGroupResponse: ...
    def CreateOrUpdateElementGroups2(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2017_11.MDConnectivity.ElementGroupInputInfo2]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.ElementGroupResponse: ...
    def CreateOrUpdateModelElements2(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2017_11.MDConnectivity.CreateOrUpdateModelElementsInfo2]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.CreateOrUpdateModelElementsResponse: ...

class MDConnectivityService:
    """
    
            This Service provides capabilities to create and update Model Elements, Ports, Connections
            and their relations.
            


Library Reference:

Mdc0SoaMDConnectivityStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> MDConnectivityService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def QueryOrderedElementGroupByPartition(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.QueryOrderedElementGroupByPartitionListInputInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.QueryOrderedElementGroupByPartitionResponse:
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
    def CreateOrUpdateElementGroups(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.ElementGroupInputInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.ElementGroupResponse:
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
    def CreateOrUpdateModelElements(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.CreateOrUpdateModelElementsInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.CreateOrUpdateModelElementsResponse:
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
    def FindConnectionsOnPort(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.FindConnectionsOnPortInputInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.FindConnectionsOnPortResponse:
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
    def FindPorts(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.FindPortsInputInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.FindPortsResponse:
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
    def FindPortsGroups(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.FindPortsGroupsInputInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.FindPortsGroupsResponse:
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
    def GetConditionalElemGroups(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetConditionalElementGroupInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetConditionalElemGroupsResponse:
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
    def GetIdentity(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetIdentityInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetIdentityResponse:
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
    def GetOrderedElementGroups(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetOrderedElementGroupsInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetOrderedElementGroupsResponse:
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
    def GetRealizedLogicalElements(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetRealizedLogicalElementsInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetRealizedLogicalElementsResponse:
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
    def InsertConnectionElement(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.ConnectionElementInsertInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def InsertOrderedElementGroupElements(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.OrderedElementGroupInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def QueryConnectionModelElements(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetConnectionModelElementsInputInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetConnectionModelElementsResponse:
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
    def QueryModelElementsOfElementGroup(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetElementsOfConditionalElementGroupInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetElementsOfConditionalElemGroupResponse:
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
    def QueryParentElementGroup(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetConditionalElemGroupAndOrderedElemGroupInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.GetConditionalElemGroupAndOrderedElemGroupResponse:
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
    def ReverseOrderedElementGroupElements(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.ReverseOrderedElementGroupInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def SplitOrderedElementGroupElements(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.SplitOrderedElementGroupInputInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.SplitOrderedElementGroupResponse:
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
    def FindConnectionsOnPort2(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.FindConnectionsOnPortInputInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2016_10.MDConnectivity.FindConnectionsOnPortResponse2:
        """    
             This operation finds all Mdc0ConnectionElement objects for the given Mdc0PortArtifact
             objects associated with Mdl0ConditionalElement objects.
             

Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         The search criteria.
             
        :return: 
        """
        ...
    def QueryParentElementGroup2(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2016_10.MDConnectivity.GetParentElementGroupInfo]) -> Mdc0.Services.Strong.Mdconnectivity._2016_10.MDConnectivity.GetParentElementGroupResponse:
        """    
             This operation finds the parent Mdc0ConditionalElementGroup object and Mdc0OrderedElementGroup
             object that are associated with given Mdl0ConditionalElement object.
             

Use Cases:

             Use Case 1: The client wants to find the conditional groups and ordered groups that
             a conditional element is a member of.
             

Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         Holds the informaiton about the <b>Mdc0ConnectionElement</b> object for querying
                         the elements.
             
        :return: 
        """
        ...
    def CreateOrUpdateElementGroups2(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2017_11.MDConnectivity.ElementGroupInputInfo2]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.ElementGroupResponse:
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
             element group, known as a run in Piping and Instrumentation Diagram/Drawing (P&ID)
             applications) so the conditional element group object has to be created before the
             create ordered element group action can be performed. The conditional element groups
             role is to manage a list of ordered element group objects. It also maintains a list
             of Mdl0ConditionalElements objects not in the conditional element group.
             

             An ordered element group object for example in the P&ID application is referred
             to as a branch and its basic role is to manage an ordered list of Mdc0ConditionalElement
             objects along with a begin and end Mdc0CondtionalElement. The create or update
             operation is used to set properties on the Mdc0OrderedElementGroup object
             which include the ordered list of equipment's, beginning and ending equipment and
             the optional Specification library property. The library specification contains for
             example a Pipe Specification in the P&ID application.
             

             If Ptn0Patition object is provided as an input, all the created Mdc0ConditionalElementGroup
             and Mdc0OrderedElementGroup objects will be added to the partition as membership
             objects and if not provided, it will skip this step.
             

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
             
If Mdl0ConditionalElement objects are to be updated in the
             conditional element group they are provided.
             
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
             
Update any values passed in via the attributeInfo
             parameter.
             
Update elements property
             if it is supplied.
             
Update startelement and endelement property if they are supplied.
             
Update specification property
             if it is supplied.
             



Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         Data used to create or update an <b>Mdc0ConditionalElementGroup</b> object and zero
                         or more  <b>Mdc0OrderedElementGroup</b> objects. It is a list of <b>ElementGroupInputInfo2</b>
                         structures.
             
        :return: 
        """
        ...
    def CreateOrUpdateModelElements2(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2017_11.MDConnectivity.CreateOrUpdateModelElementsInfo2]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.CreateOrUpdateModelElementsResponse:
        """    
             This operation creates or updates Mdl0ConditionalElement, Mdc0PortArtifact
             and Mdc0ConnectionElement objects. Using this API, applications can create
             and update Mdc0ModelElement, Mdc0PortArtifact and Mdc0ConnectionElement
             objects between the model elements in bulk, giving better through put that might
             otherwise be achieved using standard object create and update API. If partition object
             is provided, all the created objects will be added to the partition as membership
             objects. And if not provided, it will skip this step.
             

Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         Holds information for creating and updating objects of <b>Mdl0ConditionalElement</b>,
                         <b>Mdc0PortArtifact</b> and <b>Mdc0ConnectionElement.</b>

        :return: 
        """
        ...

