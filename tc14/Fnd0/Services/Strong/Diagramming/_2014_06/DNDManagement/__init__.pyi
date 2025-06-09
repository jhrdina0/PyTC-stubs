import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class CreateInput:
    """
    The parameters required to create the Business Object.
    """
    def __init__(self, ) -> None: ...
    BoName: str
    """Business Object type name"""
    PropertyNameValues: System.Collections.Hashtable
    """
            Map of property name (key) and property values (values) in string format, to be set
            on new object being created. Note: The calling client is responsible for converting
            the different property types (int, float, date .etc) to a string using the appropriate
            function(s) in the SOA client framework Property class.
            """
    CompoundCreateInput: System.Collections.Hashtable
    """CreateInput for compounded objects."""

class CreateAndPasteInputInfo:
    """
    
CreateAndPasteInputInfo structure represents the information necessary to
            create a new object and paste the same.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data     elements
            and partial errors associated     with this input structure.
            """
    OpType: str
    """
            createAndPaste - use in cases where create     and paste both
            are needed
            
            pasteOnly    - use in cases where paste alone     is
            needed.newObject should have valid value     in this case.
            
"""
    CreateData: CreateInput
    """Input data for create operation."""
    NewObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The object to paste in pasteTarget in case of pasteOnly else it is NULL.
            
"""
    PasteTarget: Teamcenter.Soa.Client.Model.ModelObject
    """The target object onto which the newly created object is to be pasted."""
    PasteRelation: str
    """
            The relation to create between the object     being pasted and
            paste target.If no value is     specified the default relation
            is used.
            """

class CreateAndPasteOutput:
    """
    This structure represents the details of the output of CreateAndPaste operation.
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            The clientId from the input CreateAndPasteInputInfo element.This value is unchanged
            from the input, and can be used to identify this response elementwith the corresponding
            input element.
            """
    PasteResultObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Runtime object resulting from the paste of newly created object.This can be null
            in some cases.E.g: Paste in a Folder object.
            """
    NewObject: Teamcenter.Soa.Client.Model.ModelObject
    """Newly created object."""

class CreateAndPasteResponse:
    """
    
            The structure represents the output of CreateAndPaste operation.It contains
            the CreateAndPasteOutput object and ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateAndPasteOutput]
    """
CreateAndPasteOutput objects containing information about the newly created
            object and paste result object.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData."""

class CreateConnectionPortsAndConnectInputInfo:
    """
    
            This structure contains the details required for creating, pasting port and connection
            objects and establishing connection between them.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used  to identify return data
            elements and partial errors associated with this input structure.
            """
    InputMap: System.Collections.Hashtable
    """A map of key input data (string/CreateAndPasteInputInfo) valid keys are PORT1,PORT2,CONNECTION"""
    ConnectCase: str
    """
            It can be one of the following values
            

create2PortsConxAndConnToPorts -  Use this to create    two
            ports, connection and establish connection between them.
            
create1PortConxAndConnToPorts - Uset this to create one    port,
            connection and establish connection between the    existing port,newly
            created port and connection.
            
createConxConnectToPorts - Use this to create a connection and connect
            it to existing ports.
            
create2PortsConxExistsConnToPorts- Use this to create two ports and
            connect the existing connection to these ports.
            
create1PortConxExistsConnToPorts - Use this to create a    single
            port and then connect the existing connection to this port and existing port.
            
createConxConnToBlocks- Use this to establish connection between
            blocks [preference connected_ToRules should also allow this]
            

"""
    ObjectsToConnectTo: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Ports / Blocks to connect the connection."""
    ConnectionObject: Teamcenter.Soa.Client.Model.ModelObject
    """The Connection object if already exists."""

class CreateConnectionPortsAndConnectResponse:
    """
    
            This structure represents the output of createConnectionPortsAndConnect operation.
            It contains ConnectOutputDataMap object[s] and ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[System.Collections.Hashtable]
    """A map of key output data (string/ CreateAndPasteOutput) .Valid keys are PORT1,PORT2,CONNECTION"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData"""

class DNDManagement:
    """
    Interface DNDManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateAndPaste(self, InputData: list[CreateAndPasteInputInfo]) -> CreateAndPasteResponse:
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
    def CreateConnectionPortsAndConnect(self, InputData: list[CreateConnectionPortsAndConnectInputInfo]) -> CreateConnectionPortsAndConnectResponse:
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

