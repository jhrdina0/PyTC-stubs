import Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity
import System
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateOrUpdateModelElementsInfo2:
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
    ModelElementObjects: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.ModelElementInfo]
    """A list of ModelElementInfo structures."""
    PortObjects: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.PortArtifactInfo]
    """A list of PortArtifactInfo structures."""
    ConnectionObjects: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.ConnectionElementInfo]
    """A list of ConnectionElementInfo structures."""
    Partition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """
            The Ptn0Partition object. Optional. If provided, the created Mdc0ModelElement
            and Mdc0ConnectionElement objects will be added to the partition as membership
            objects and if not provided, this step is skipped.
            """

class ElementGroupInputInfo2:
    """
    
            The input values needed to create or update a conditional element group and one or
            more ordered element groups.
            
    """
    def __init__(self, ) -> None: ...
    ConditionalElementGroups: Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.ConditionalElementGroupInfo
    """Create or update info for conditional element group."""
    OrderedElementGroups: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.OrderedElementGroupInfo]
    """Create or update info for ordered element groups. Optional."""
    Partition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """
            The Ptn0Partition object. Optional. If provided, the created Mdc0ConditionalElementGroup
            object will be added to the partition as a membership object and if not provided,
            this step is skipped.
            """

class MDConnectivity:
    """
    Interface MDConnectivity
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateElementGroups2(self, Input: list[ElementGroupInputInfo2]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.ElementGroupResponse:
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
    def CreateOrUpdateModelElements2(self, Input: list[CreateOrUpdateModelElementsInfo2]) -> Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.CreateOrUpdateModelElementsResponse:
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

