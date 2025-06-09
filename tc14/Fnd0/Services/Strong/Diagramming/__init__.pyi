import Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement
import Fnd0.Services.Strong.Diagramming._2012_09.DiagramManagement
import Fnd0.Services.Strong.Diagramming._2014_06.DNDManagement
import System
import Teamcenter.Soa.Client
import typing

class DiagramManagementRestBindingStub(DiagramManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateDiagram(self, InputData: list[Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.CreateDiagramInputInfo]) -> Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.CreateDiagramResponse: ...
    @typing.overload
    def CreateOrUpdateTemplate(self, InputData: Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.CreateOrUpdateTemplateInputInfo) -> Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.CreateOrUpdateTemplateResponse: ...
    @typing.overload
    def CreateOrUpdateTemplate(self, InputData: Fnd0.Services.Strong.Diagramming._2012_09.DiagramManagement.CreateOrUpdateTemplateInputInfo1) -> Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.CreateOrUpdateTemplateResponse: ...
    def GetDiagramMembers(self, InputData: list[Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.GetDiagramMembersInputInfo]) -> Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.GetDiagramMembersResponse: ...
    def OpenDiagram(self, InputData: list[Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.OpenDiagramInputInfo]) -> Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.OpenDiagramResponse: ...
    def SaveDiagram(self, InputData: list[Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.SaveDiagramInputInfo]) -> Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.SaveDiagramResponse: ...

class DiagramManagementService:
    """
    
            The DiagramManagement service provides operations to manage diagrams for Teamcenter
            business objects (WorkspaceObject/ ItemRevision/ Folder/ BOMLine).
            The operations in this service allow creation, saving and opening of saved diagrams.
            


Library Reference:

Fnd0SoaDiagrammingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DiagramManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateDiagram(self, InputData: list[Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.CreateDiagramInputInfo]) -> Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.CreateDiagramResponse:
        """    
             This operation creates a Visio Diagram for a Teamcenter object (WorkspaceObject/
             ItemRevision/ Folder/ BOMLine) using a Diagram Template. The objects and relations
             shown on the diagram are gathered by executing the Transfer Mode and Relation Rule
             specified on the diagram template. Relation Rule specifies the relations to be shown
             between the objects.
             
             Only those objects appear on the diagram for which there is a Visio Shape in the
             stencil and there is mapping defined between the Shape and the Teamcenter object
             in the mapping xml file. Mapping file has details about how to define the mappings.
             
             While creating a diagram, if user selects the "Open Diagram" option, the diagram
             object is created on the server and all the necessary information is returned in
             the response which is utilized to open the Visio diagram. If user does not select
             the option, then just the diagram object is created.
             


Use Cases:

             You can select a Teamcenter object in RAC and create a Visio diagram for the same
             by selecting a Diagram Domain and a Diagram Template.
             

Dependencies:

             createOrUpdateTemplate, createOrUpdateTemplate
             

Teamcenter Component:

             Diagram Management - Diagram Management
             
        :param InputData: 
                         The required information to create a diagram for the selected object.
             
        :return: The created diagram objects are returned along with the Service data elements. If
             there are any issues while creating a diagram, error code 267012 is returned.
        """
        ...
    @typing.overload
    def CreateOrUpdateTemplate(self, InputData: Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.CreateOrUpdateTemplateInputInfo) -> Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.CreateOrUpdateTemplateResponse: ...
    @typing.overload
    def CreateOrUpdateTemplate(self, InputData: Fnd0.Services.Strong.Diagramming._2012_09.DiagramManagement.CreateOrUpdateTemplateInputInfo1) -> Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.CreateOrUpdateTemplateResponse: ...
    def GetDiagramMembers(self, InputData: list[Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.GetDiagramMembersInputInfo]) -> Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.GetDiagramMembersResponse:
        """    
             This operation retrieves the specific types of members of the diagram based on its
             membership types. Following are the types of members apart from the ones that appear
             on the diagram as a result of transfer mode traversal and relationship rules.
             

User Added - The objects which are added to the diagram by the user.
             E.g. an Item object which is copied from Teamcenter and then pasted on to the diagram.
             
User Omitted - The objects which are deleted by the user from the
             diagram. E.g. user can remove an object from the diagram only. The object is removed
             from the diagram and not from database. It can be retrieved and again shown on the
             diagram.
             



Use Cases:

             None.
             

Teamcenter Component:

             Diagram Management - Diagram Management
             
        :param InputData: 
                         holds the required information to get the specific types of diagram members.
             
        :return: is returned.
        """
        ...
    def OpenDiagram(self, InputData: list[Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.OpenDiagramInputInfo]) -> Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.OpenDiagramResponse:
        """    
             This operation opens a Visio Diagram created for a Teamcenter object (WorkspaceObject/
             Item Revision/ Folder/ BOMLine). The objects and relations shown on the diagram
             are gathered by executing the Transfer Mode and Relation Rule specified on the diagram
             template. Relation Rule specifies the relations to be shown between the objects.
             
             Only those objects appear on the diagram for which there is a Visio Shape in the
             stencil and there is mapping defined between the Shape and the Teamcenter object
             in the mapping xml file. Mapping file has details about how to define the mappings.
             
             If the contents of the root object of the diagram are changed, for instance, a BOM
             structure changes or the contents of the folder are modified, then the diagram will
             show only the current information. This is because every time a diagram is opened,
             Transfer mode and Relation Rules are applied.
             

Use Cases:

             You can select a Teamcenter object and launch the open diagram dialog which shows
             the list of all diagrams created for that object. You can select a diagram to open.
             A Visio diagram is opened on the RAC. The content of the diagram is decided by the
             Transfer mode and the Relation Rule.
             

Dependencies:

             saveDiagram
             

Teamcenter Component:

             Diagram Management - Diagram Management
             
        :param InputData: 
                         holds the required information to open a diagram for the selected object.
             
        :return: will return
             the error codes.
        """
        ...
    def SaveDiagram(self, InputData: list[Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.SaveDiagramInputInfo]) -> Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.SaveDiagramResponse:
        """    
             This operation saves Visio Diagram(s) created for a Teamcenter object (WorkspaceObject/
             Item Revision/ Folder/ BOMLine). When a Visio diagram is saved, a skeleton file
             (.vdx) is created and stored as a dataset to hold all the non Teamcenter information,
             like notes if any. A preview image of the diagram content is also stored as an image
             data set. These Dataset objects are attached to the diagram object.
             
             For the Teamcenter business objects appearing on the diagram, Fnd0ShapeRelation
             objects are created with the diagram object to hold the position information so that
             the shapes appear in their original position and format next time the diagram is
             opened.
             

Use Cases:

             You can create or open an existing diagram and make changes to it. You can then save
             the diagram.
             

Dependencies:

             createDiagram, openDiagram
             

Teamcenter Component:

             Diagram Management - Diagram Management
             
        :param InputData: 
                         holds the information to save a diagram created for a Teamcenter business object.
             
        :return: if the saving
             the diagram fails.
        """
        ...

class DNDManagementRestBindingStub(DNDManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateAndPaste(self, InputData: list[Fnd0.Services.Strong.Diagramming._2014_06.DNDManagement.CreateAndPasteInputInfo]) -> Fnd0.Services.Strong.Diagramming._2014_06.DNDManagement.CreateAndPasteResponse: ...
    def CreateConnectionPortsAndConnect(self, InputData: list[Fnd0.Services.Strong.Diagramming._2014_06.DNDManagement.CreateConnectionPortsAndConnectInputInfo]) -> Fnd0.Services.Strong.Diagramming._2014_06.DNDManagement.CreateConnectionPortsAndConnectResponse: ...

class DNDManagementService:
    """
    
            DNDManagement service exposes operations that are used to create and add new objects
            to structures on drag and drop actions in diagram tools. In Systems Engineering these
            operations are used to author Functional/Logical structures via the Visio authoring
            tool.
            


Library Reference:

Fnd0SoaDiagrammingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DNDManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateAndPaste(self, InputData: list[Fnd0.Services.Strong.Diagramming._2014_06.DNDManagement.CreateAndPasteInputInfo]) -> Fnd0.Services.Strong.Diagramming._2014_06.DNDManagement.CreateAndPasteResponse:
        """    
             This operation creates an object of given type and pastes the newly created object
             onto the paste target object.The result of the operation is newly created object
             and any runtime object as a result of paste operation.
             

Use Cases:

             Use Case1:
             
             Create a new object and paste it under the paste target. User drags and drops shapes
             onto the diagram. Shapes are mapped to specific types and a mapping file specifies
             this information. On drag and drop a new object of the desired type is created and
             is pasted on to the diagram root object. When the diagram is for a BOM structure
             the paste operation also returns a resultant runtime object [BOMLine] in addition
             to the newly created object. The runtime/newly created object is mapped to the shape
             on the diagram.
             

             Use Case2:
             
             Connection Management
             

             Use Case2a:
             
             Create Connection, Ports and establish connection between them. User drags and drops
             a Connection shape onto the diagram and glues the same to Block shapes. Two port
             objects are created and pasted under the Block objects if connected_ToRules is set
             to allow connection between ports; a Connection object is created and pasted under
             its paste target object. Connection is established between the Connection object
             and Port objects.
             

             Use Case2b:
             
             Create Connection, establish connection between input ports. User drags and drops
             a Connection shape onto the diagram and glues the same to Port shapes. A Connection
             object is created and pasted under the paste target. Connection is established between
             the Connection object and Port objects if connected_ToRules is set to allow connection
             between ports.
             

             Use Case2c:
             
             Create Connection, a Port and establish connection between new port, input port.
             User drags and drops a Connection shape onto the diagram and glues the same to a
             Block shape and a Port shape. A Port object is created if connected_ToRules is set
             to allow connection between ports. A Connection object is created. Port and Connection
             objects are pasted under respective paste targets. Connection is established between
             the Connection object and Port objects.
             

             Use Case2d:
             
             Establish connection between existing Connection and Ports. User glues an existing
             Connection shape to Port shapes. Connection is established between the ports if connected_ToRules
             allows for connections between ports.
             

             Use Case2e:
             
             Create new ports and establish connection between existing Connection and the Ports.
             
             User glues an existing Connection shape to Block shapes. Port objects are created
             and pasted under respective paste target objects if connected_ToRules allows for
             connections between ports. Connection is established between the Port objects and
             Connection object.
             

             Use Case2f:
             
             Create new port and establish connection between existing Connection, Port and newly
             created Port. User glues an existing Connection shape to a Block shape and Port shape.
             A Port objects is created and pasted under it's paste target object if connected_ToRules
             allows for connections between ports. Connection is established between the Port
             objects and Connection object.
             

             Use Case2g:
             
             Establish connection between existing Connection and Blocks. User glues an existing
             Connection shape to Block shapes. Connection is established between the Blocks and
             Connection object if connected_ToRules allows for connection between blocks.
             


Teamcenter Component:

             Diagram Management - Diagram Management
             
        :param InputData: 
                         An input object containing the type[s] to create,property mappings,paste target object[s]
                         and desired paste relation[s].
             
        :return: 
        """
        ...
    def CreateConnectionPortsAndConnect(self, InputData: list[Fnd0.Services.Strong.Diagramming._2014_06.DNDManagement.CreateConnectionPortsAndConnectInputInfo]) -> Fnd0.Services.Strong.Diagramming._2014_06.DNDManagement.CreateConnectionPortsAndConnectResponse:
        """    
             This operation creates ports and connection object given the port types, connection
             type. Pastes the new objects under respective paste targets and then connects the
             connection object to the ports. Connection, one or both ports can exist, in that
             case the missing objects are created and connection is established. Connection can
             also be established directly between blocks.
             

Use Cases:

             Use Case1:
             
             Create a new object and paste it under the paste target. User drags and drops shapes
             onto the diagram. Shapes are mapped to specific types and a mapping file specifies
             this information. On drag and drop a new object of the desired type is created and
             is pasted on to the diagram root object. When the diagram is for a BOM structure
             the paste operation also returns a resultant runtime object [BOMLine] in addition
             to the newly created object. The runtime/newly created object is mapped to the shape
             on the diagram.
             

             Use Case2:
             
             Connection Management
             

             Use Case2a:
             
             Create Connection, Ports and establish connection between them. User drags and drops
             a Connection shape onto the diagram and glues the same to Block shapes. Two port
             objects are created and pasted under the Block objects if connected_ToRules is set
             to allow connection between ports; a Connection object is created and pasted under
             its paste target object. Connection is established between the Connection object
             and Port objects.
             

             Use Case2b:
             
             Create Connection, establish connection between input ports. User drags and drops
             a Connection shape onto the diagram and glues the same to Port shapes. A Connection
             object is created and pasted under the paste target. Connection is established between
             the Connection object and Port objects if connected_ToRules is set to allow connection
             between ports.
             

             Use Case2c:
             
             Create Connection, a Port and establish connection between new    port,
             input port.
             
             User drags and drops a Connection shape onto the diagram and glues the same to a
             Block shape and a Port shape. A Port object is created if connected_ToRules is set
             to allow connection between ports. A Connection object is created. Port and Connection
             objects are pasted under respective paste targets. Connection is established between
             the Connection object and Port objects.
             

             Use Case2d:
             
             Establish connection between existing Connection and Ports
             
             User glues an existing Connection shape to Port shapes. Connection is established
             between the ports if connected_ToRules allows for connections between ports.
             

             Use Case2e:
             
             Create new ports and establish connection between existing Connection and the Ports.
             
             User glues an existing Connection shape to Block shapes. Port objects are created
             and pasted under respective paste target objects if connected_ToRules allows for
             connections between ports. Connection is established between the Port objects and
             Connection object.
             

             Use Case2f:
             
             Create new port and establish connection between existing Connection, Port and newly
             created Port. User glues an existing Connection shape to a Block shape and Port shape.
             A Port objects is created and pasted under it's paste target object if connected_ToRules
             allows for connections between ports. Connection is established between the Port
             objects and Connection object.
             

             Use Case2g:
             
             Establish connection between existing Connection and Blocks. User glues an existing
             Connection shape to Block shapes. Connection is established between the Blocks and
             Connection object if connected_ToRules allows for connection between blocks.
             


Teamcenter Component:

             Diagram Management - Diagram Management
             
        :param InputData: 
                         The required information to create connection, ports and connect them.
             
        :return: 
        """
        ...

