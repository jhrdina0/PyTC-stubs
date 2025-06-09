import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AssociateWireProtectionToSegmentsResponse:
    """
    Return structure for associateWireProtectionToSegments  operation
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a common data structure used to return sets of Teamcenter Data Model objects
            from a service request. This also holds services exceptions and updated objects.
            """

class HarnessObjectInfo:
    """
    This is the input/output structure for Harness object information
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier string that helps the client to track the object(s) created."""
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """A Harness, ItemRevision, or ItemElement object."""
    ObjectOcc: Teamcenter.Soa.Client.Model.ModelObject
    """A Harness, Item, or ItemElement object occurrence."""
    ObjectOccThread: Teamcenter.Soa.Client.Model.ModelObject
    """A Harness or ItemElement object occurrence thread."""

class CableData:
    """
    This is a structure to hold the cable data.
    """
    def __init__(self, ) -> None: ...
    Cable: HarnessObjectInfo
    """This is a HarnessObjectInfo input structure containing cable object information."""
    CableOccProps: System.Collections.Hashtable
    """
            It is a map of name/value pairs (string/string) of cable occurrence properties. It
            is optional.
            """
    Connections: list[ConnectionData]
    """These are connections associated with this cable."""
    Connectors: list[ConnectorData]
    """These are connectors associated with this cable."""
    Childcables: list[CableData]
    """These are child cables of this cable."""
    Shields: list[ShieldData]
    """These are shields associated with this cable."""
    Devices: list[DeviceData]
    """These are devices associated with this cable."""
    Wires: list[WireInfo]
    """These are wires associated with this cable."""

class ColorData:
    """
    ColorData structure of WireData input/output structure.
    """
    def __init__(self, ) -> None: ...
    ColorType: str
    """This is a wire color type."""
    Color: str
    """This is the color of the wire."""

class ConnectionData:
    """
    This is a structure for Connection data.
    """
    def __init__(self, ) -> None: ...
    Connection: HarnessObjectInfo
    """This is HarnessObjectInfo input structure containing Connection object information."""
    ConnectionOccProps: System.Collections.Hashtable
    """
            It is a map of name/value pairs (string/string) of connection occurrence properties.
            It is optional.
            """
    AssociatedPorts: list[HarnessObjectInfo]
    """
            This is a list of connection to port (Connect_To) association information to be created
            in the harness structure.
            """
    AssociatedWires: list[HarnessObjectInfo]
    """
            This is a list of connection to wire (Implemented_By) association information to
            be created in the harness structure.
            """
    Associatedshilds: list[HarnessObjectInfo]
    """
            This is a list of connection to shield (Implemented_By) association information to
            be created in the harness structure.
            """

class ConnectorData:
    """
    This is structure for Connector data.
    """
    def __init__(self, ) -> None: ...
    Connector: HarnessObjectInfo
    """This is a HarnessObjectInfo input structure containing connector object information."""
    ConnectorOccProps: System.Collections.Hashtable
    """
            It is a map of name/value pairs (string/string) of connector occurrence properties.
            It is optional.
            """
    Ports: list[ItemElementData]
    """A list of ports connected to this connector."""

class ControlPoint:
    """
    ControlPoint structure for CurveData structure
    """
    def __init__(self, ) -> None: ...
    Points: list[float]
    """Array of control points."""

class CreateOrUpdateHarnessResponse:
    """
    This is a return structure for createOrUpdateHarness operation.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a common data structure used to return sets of Teamcenter Data Model object
            from a service request. This also holds services exceptions.
            """
    Output: list[HarnessObjectInfo]
    """
            This is a list of HarnessObjectInfo objects which contains the created harness data
            and the instance data.
            """

class CreateOrUpdateRouteObjectsResponse:
    """
    The response structure for the createOrUpdateRouteObjects operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[RouteDataOutputInfo]
    """
            A list of created route objects and their associated RouteData, NodeData, SegmentData
            and CurveData.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a common data structure used to return sets of Teamcenter Data Model objects
            from a service request. This also holds services exceptions.
            """

class CreateOrUpdateWireDataResponse:
    """
    
This structure is a response from this operation.  It returns the created and
updated
objects, as well as any errors.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a common data structure is used to return sets of Teamcenter Data Model objects
            from a service request as well as partial error.  ServiceData has the wire business
            objects which were created or updated according to the input provided by the client
            developer.
            """

class CreateRouteLocationsResponse:
    """
    Return structure for RouteLocations operation
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""
    Output: list[RouteLocationOutput]
    """
            A list of created RouteLocation business objects and associated RouteLocationRevision
            business objects.
            """

class CurveData:
    """
    CurveData structure of RouteData input structure for createOrUpdateRouteObjects
operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    Name: str
    """The name of the Route curve to be created."""
    ControlPoints: list[ControlPoint]
    """A list of points which will control the curve for the Route Object."""
    Knots: list[float]
    """A list of knots on the curve the Route Object."""
    Multiplicities: list[int]
    """A list of multiplicities on the curve of the Route Object."""
    CurveAttributes: System.Collections.Hashtable
    """
            A map of attributes names and initial values pairs (string/string). The calling client
            is responsible for converting the different property types (int, float, date, etc.)
            to a string using the appropriate toXXXString functions in the SOA client framework's
            Property class. Multi-valued properties are represented with a comma separated string.
            
            The following attributes are supported:
            

degree Degree of the Route curve.
            
dimension Dimension of the Route curve.
            
isRational Flag indicating whether this Route curve is rational.
            
isUniform Flag indicating whether this Route curve is uniform.
            
startParameter Start interval of the Route curve between 0 and 1.
            
endParameter End interval of the Route curve between 0 and 1.
            

"""
    Curve: Teamcenter.Soa.Client.Model.ModelObject
    """The RouteCurve object used to update the route object."""

class DataOutput:
    """
    Output structure for Route, Segment, Node and Curve
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this output structure.
            """
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The output object."""

class DeleteRouteObjectsInfo:
    """
    Input structure for deleteRouteObjects operation
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """
            This is input of type PSBOMView revision BVR (BOM view revision) in which
            the route object needs to be deleted. It is required if the deleteAll flag is true.
            """
    DeleteAll: bool
    """This is used to indicate if all the route objects need to be deleted"""
    Routes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of route objects to be deleted (optional)."""
    Nodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of route node objects to be deleted (optional)."""
    Segments: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of route segment objects to be deleted (optional)."""
    Curves: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of route curve objects to be deleted (optional)."""

class DeleteRouteObjectsResponse:
    """
    
This is the response structure for the deleteRouteObjects operation.
DeleteRouteObjectsResponse
consists of servicedata. Service data has unique identifier string for each
object
which was deleted as part of the deleted objects list of the ServiceData
element,
as well as the objects which were not deleted as part of the partial errors.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a common data structure used to return sets of Teamcenter Data Model objects
            from a service request. This also holds services exceptions.
            """

class DeleteWireDataResponse:
    """
    Return structure for deleteWireData operation
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a common data structure used to return sets of Teamcenter Data Model objects
            from a service request. This also holds services exceptions.
            """

class DeviceData:
    """
    This is a structure to hold device data .
    """
    def __init__(self, ) -> None: ...
    Device: HarnessObjectInfo
    """This is a HarnessObjectInfo input structure containing device object information."""
    DeviceOccProps: System.Collections.Hashtable
    """
            It is a map of name/value pairs (string/string) of device occurrence properties.
            It is optional.
            """
    Connectors: list[ConnectorData]
    """These are connectors associated with this device."""
    Ports: list[ItemElementData]
    """These are ports associated with this device."""
    AssociatedConnectors: list[HarnessObjectInfo]
    """These are connectors associated with this device."""

class DisplayData:
    """
    
DisplayData structure of RouteData input structure for
createOrUpdateRouteObjects
operation
    """
    def __init__(self, ) -> None: ...
    Font: int
    """The font for display of route data."""
    Width: float
    """The width for display of route data."""
    RgbValues: list[float]
    """This is a list which contains display color with RGB values for route data."""

class ExtendedAttributes:
    """
    
Input structure for createItems operation to support setting attribute values on
the created Item, ItemRevision, or corresponding master forms that may be
created
with the objects.
    """
    def __init__(self, ) -> None: ...
    ObjectType: str
    """
            The type of object to set these properties on, RouteLocation, RouteLocationRevision
            etc.
            """
    Attributes: System.Collections.Hashtable
    """
            A map of attributes names and initial values pairs (string/string). The calling client
            is responsible for converting the different property types (int, float, date, etc.)
            to a string using the appropriate toXXXString functions in the SOA client framework's
            Property class. Multi-valued properties are represented with a comma separated string.
            """

class GetWireDataResponse:
    """
    Return structure for getWireData operation
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a common data structure used to return sets of Teamcenter Data Model objects
            from a service request. This also holds services exceptions.
            """
    WireData: list[WireData]
    """This is an output list of wire data."""

class GetWireProtectionSegmentResponse:
    """
    This is the return structure of getWireProtectionSegments operation.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a common data structure used to return the sets of Teamcenter Data Model
            objects from a service request. This also holds the partial errors.
            """
    Output: list[WireProtectionData]
    """
            This is a list of WireProtectionData objects corresponding to the BOMLine
            objects sent as an input to the getWireProtectionSegments operation.
            """

class HarnessData:
    """
    This is a HarnessData input structure for createOrUpdateRouteObjects operation.
    """
    def __init__(self, ) -> None: ...
    Harness: HarnessObjectInfo
    """This contains Harness object information."""
    HarnessOccProps: System.Collections.Hashtable
    """
            It is a map of name/value pairs (string/string) of harness occurrence properties.
            It is optional.
            """
    Connections: list[ConnectionData]
    """A list of connection data."""
    Connectors: list[ConnectorData]
    """A list of connector data."""
    Cables: list[CableData]
    """A list of cable data."""
    Shields: list[ShieldData]
    """A list of shield data."""
    Devices: list[DeviceData]
    """A list of device data."""
    Wires: list[WireInfo]
    """A list of wire data."""

class HarnessInfo:
    """
    
This is an Input structure for createOrUpdateHarness operation and specifies the
parent and harness data
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID can be used to identify returned
            HarnessObjectInfo elements and associated Partial Errors.
            """
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """
            This object is the parent of the harness structure to which the harness data are
            to be added as children.
            """
    HarnessData: list[HarnessData]
    """
            This contains the data to be used to create or update harness data in Teamcenter
            database.
            """

class ItemElementData:
    """
    ItemElementData structure.
    """
    def __init__(self, ) -> None: ...
    ItemElement: HarnessObjectInfo
    """This is a HarnessObjectInfo input structure containing item object information."""
    ItemElementOccProps: System.Collections.Hashtable
    """
            It is a map of name/value pairs (string/string) of item occurrence properties. It
            is optional.
            """
    ChildItemElements: list[ItemElementData]
    """A list of item element data children."""
    RealizedPorts: list[HarnessObjectInfo]
    """A list of Port to Port (Realized_By) association information."""

class LengthData:
    """
    LengthData structure of WireData input/output structure.
    """
    def __init__(self, ) -> None: ...
    LengthType: str
    """This is a wire length type."""
    Length: float
    """This is the length of the wire."""

class NodeData:
    """
    NodeData structure of RouteData input structure for createOrUpdateRouteObjects
operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    Name: str
    """The name of the RouteNode to be created."""
    NodeAttributes: System.Collections.Hashtable
    """
            A map of attributes names and initial values pairs (string/string). The calling client
            is responsible for converting the different property types (int, float, date .etc)
            to a string using the appropriate toXXXString functions in the SOA client framework's
            Property class. Multi-valued properties are represented with a comma separated string.
            
            The following attributes are supported:
            

x The x coordinate for this Route Node.
            
y The y coordinate for this Route Node.
            
z The z coordinate for this Route Node.
            

"""
    Node: Teamcenter.Soa.Client.Model.ModelObject
    """The RouteNode Object used to update the route object."""

class RemoveWireProtectionAssociationResponse:
    """
    Return structure for RemoveWireProtectionAssociationResponse  operation
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a common data structure used to return sets of Teamcenter Data Model objects
            from a service request. This also holds services exceptions and updated objects.
            """

class RouteData:
    """
    RouteData input structure for createOrUpdateRouteObjects operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    Name: str
    """The name of the Route data to be created."""
    DisplayData: DisplayData
    """The DisplayData."""
    NodeData: list[NodeData]
    """A list which will hold NodeData information."""
    SegmentData: list[SegmentData]
    """A list which will hold SegmentData information."""
    CurveData: CurveData
    """The CurveData."""
    RouteAttributes: System.Collections.Hashtable
    """
            A map of attributes names and initial values pairs (string/string). The calling client
            is responsible for converting the different property types (int, float, date .etc)
            to a string using the appropriate toXXXString functions in the SOA client framework's
            Property class. Multi-valued properties are represented with a comma separated string.
            """
    Route: Teamcenter.Soa.Client.Model.ModelObject
    """This is a RouteData Object and used in case of update of RouteObject."""

class RouteDataOutput:
    """
    Output structure for RouteDataOutput
    """
    def __init__(self, ) -> None: ...
    Route: DataOutput
    """Output information for route object."""
    Segments: list[SegmentDataOutput]
    """
            A list which consists of output information for Route Segments and its associated
            nodes and curve.
            """
    Nodes: list[DataOutput]
    """A Route node list."""
    Curve: DataOutput
    """Output information for route curve."""

class SegmentDataOutput:
    """
    Output structure for SegmentDataOutput
    """
    def __init__(self, ) -> None: ...
    Segment: DataOutput
    """Output information for route segment."""
    Nodes: list[DataOutput]
    """A Route node list."""
    Curve: DataOutput
    """Output information for route curve."""

class RouteDataOutputInfo:
    """
    Output structure for RouteData for createOrUpdateRouteObjects operation
    """
    def __init__(self, ) -> None: ...
    Route: RouteDataOutput
    """This will have output information for the route object which is created or updated."""
    Segment: SegmentDataOutput
    """This will have output information for the route segments which are created or updated."""
    Node: DataOutput
    """Output information for route node."""
    Curve: DataOutput
    """Output information for route curve."""

class SegmentData:
    """
    
SegmentData structure of RouteData input structure for
createOrUpdateRouteObjects
operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    Name: str
    """The name of the Route segment data to be created."""
    StartNode: NodeData
    """The start node of the Route segment."""
    EndNode: NodeData
    """The end node of the Route segment."""
    CenterCurve: CurveData
    """The B-Spline curve associated with the given Route segment."""
    SegmentAttributes: System.Collections.Hashtable
    """
            A map of attributes names and initial values pairs (string/string). The calling client
            is responsible for converting the different property types (int, float, date .etc)
            to a string using the appropriate toXXXString functions in the SOA client framework's
            Property class. Multi-valued properties are represented with a comma separated string.
            
            The following attributes are supported:
            

position It is a position of the segment in the Route context. First
            segment starts at 0 and so on and -1 indicates, the segments are placed in order.
            
realLength The real length of the segment.
            
representedLength The represented length of the segment.
            
crossSectionalArea The cross sectional area of the segment.
            

"""
    Segment: Teamcenter.Soa.Client.Model.ModelObject
    """The RouteSegment object, used to update the route object."""

class RouteInfo:
    """
    
Any one or all of the routeData, nodeData, segmentData, curveData can be
provided
as input and route data will be created in the given context.
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """This is PSBOMViewRevision in which the route object needs to be created."""
    RouteData: RouteData
    """Associated data for route object."""
    NodeData: NodeData
    """Associated route node data of route object."""
    SegmentData: SegmentData
    """Associated route segment data of route object."""
    CurveData: CurveData
    """Associated curve data for route object."""

class RouteLocationOutput:
    """
    Output structure for createRouteLocations operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifying string from the source RouteLocations Properties."""
    RouteLoc: Teamcenter.Soa.Client.Model.Strong.RouteLocation
    """The RouteLocation object reference that was created."""
    RouteLocRev: Teamcenter.Soa.Client.Model.Strong.RouteLocationRevision
    """The newly created RouteLocationRevision reference for the newly created RouteLocation."""

class RouteLocationProperties:
    """
    
Input structure for createRouteLocations operation.  Specifies attributes for
the
new RouteLocation or RouteLocationRevision.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify returned RouteLocationOutput
            elements and Partial Errors associated with this input RouteLocationProperties.
            """
    RouteLocId: str
    """ID for the RouteLocation objects to be created."""
    Name: str
    """Name of the RouteLocation to be created."""
    Type: str
    """The type of RouteLocation to be created, if left blank, default type is RouteLocation."""
    RevId: str
    """Identifier of the initial revision of the RouteLocation to be created."""
    Uom: str
    """
            The Unit Of Measure for RouteLocation to be created, if left blank no UOM
            will be set for the RouteLocation.
            """
    Description: str
    """The description text for the RouteLocation to be created."""
    ExtendedAttributes: list[ExtendedAttributes]
    """
            Any additional attribute values to be set on the created RouteLocation, RouteLocationRevision
            or corresponding RouteLocation Master Forms.
            """

class ShieldData:
    """
    This is a structure to hold the shield data.
    """
    def __init__(self, ) -> None: ...
    Shield: HarnessObjectInfo
    """This is a HarnessObjectInfo input structure containing shield object information."""
    ShieldOccProps: System.Collections.Hashtable
    """
            It is a map of name/value pairs (string/string) of cable occurrence properties. It
            is optional.
            """
    Connections: list[ConnectionData]
    """These are connections associated with this shield."""
    Connectors: list[ConnectorData]
    """These are connectors associated with this shield."""
    Cables: list[CableData]
    """These are cables associated with this shield."""
    Childshields: list[ShieldData]
    """These are child shields of this shield."""
    Devices: list[DeviceData]
    """These are devices associated with this shield."""
    Wires: list[WireInfo]
    """These are wires associated with this shield."""

class WireProperties:
    """
    WireProperties structure of WireData input/output structure.
    """
    def __init__(self, ) -> None: ...
    WireNumber: str
    """Wire number gives wire specifications."""
    Multiplier: str
    """This is the multiplier attribute of the wire."""
    Offset: str
    """This is the offset attribute of the wire."""
    SeparationCode: str
    """Separation code used for routing of the wire."""

class WireData:
    """
    The WireData structure represents all the details of a wire business object.
    """
    def __init__(self, ) -> None: ...
    Wire: Teamcenter.Soa.Client.Model.ModelObject
    """
            A wire business object. This can be a wire Item or a wire BOMLine.
            To assign color data, a wire item revision needs to be provided as input. To assign
            length/properties the BOMLine of the wire needs to be provided as input.
            """
    LengthData: list[LengthData]
    """This is a list of wire length information."""
    ColorData: list[ColorData]
    """This is a list of wire color information."""
    Properties: WireProperties
    """This contains wire properties like multiplier, offset, separation code."""

class WireInfo:
    """
    WireInfo structure.
    """
    def __init__(self, ) -> None: ...
    Wire: HarnessObjectInfo
    """HarnessObjectInfo input sturcture containg Wire object info."""
    WireOccProps: System.Collections.Hashtable
    """Name/value pairs of Wire occurrence properties and it is optional."""

class WireProtectionData:
    """
    Input structure for associateWireProtectionToSegments operation
    """
    def __init__(self, ) -> None: ...
    WireProtectionLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            This is a primary wire protection BOMLine to which the protection data and
            the route segments are to be assigned.
            """
    Segments: list[Teamcenter.Soa.Client.Model.ModelObject]
    """These are the route segments to be associated with the wire protection BOMLines."""
    ProtectionAreaData: System.Collections.Hashtable
    """
            This is a map of (String/String) name/value pairs of protection area data to be associated
            with the wire protection lines.
            
            The Map provides the following information.
            

Key=start_location, Value=e.g. 10.00
            
Key=end_location, Value=e.g. 20.00
            
Key=gradient, Value=e.g. 30.00
            
Key=taping_direction, Value=e.g. north
            


            The values of start_location, end_location and gradient need to be converted from
            double to string while populating protectionAreaData.
            """

class WireHarness:
    """
    Interface WireHarness
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateRouteObjects(self, Inputs: list[RouteInfo]) -> CreateOrUpdateRouteObjectsResponse:
        """    
             This operation allows client applications to create route objects in a specified
             context which is provided as an input by the client developer. When route objects
             get created, they are associated with its Route segments, Route Curves and nodes.
             Node is nothing but a point in space. You define nodes with RouteNode objects.
             RouteSegment defines the segment of a start node and an end node. RouteCurve
             models the 3D shape (b spline curve) associated with a RouteSegment object.
             The shape of the segment can optionally be defined with a RouteCurve object.
             If a RouteCurve is not defined, Teamcenter assumes that the segment is a straight
             line between start and end nodes. All RouteObjects are defined only in the context
             of a given structure and these objects cannot be shared across multiple structures.
             

Use Cases:

             Typically this is used by the client applications which perform routing of a CAD
             model based on connectivity information that is specified by a logical model. Once
             client applications decide how routes are created based on physical geometry etc,
             the route created need to be persisted into Teamcenter. Similarly, existing routes
             can also change, based on changes in physical [CAD] geometry. In such cases, this
             SOA can be used to create and or update the route objects. You need to mention this.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         This is a list of RouteInfo structures and it contains information regarding the
                         Routeobject which the user wants to create. RouteInfo has the context in which the
                         client developer wants to create Routeobject, RouteData, NodeData, SegmentData and
                         CurveData.
             
        :return: 
        """
        ...
    def CreateRouteLocations(self, Properties: list[RouteLocationProperties], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> CreateRouteLocationsResponse:
        """    
             This operation is used to create a list of RouteLocations and their associated
             data. Associated data consists of RouteLocation Revision, RouteLocation Master form,
             RouteLocation Revision Master form based on the input attribute structures and creates
             the specified relation type between the created RouteLocation and the input
             container object. If the container and relation type are not input, none of the RouteLocations
             will be related to a container. Container is not defaulted, if a destination is desired,
             it must be input. RouteLocation objects model a region of space using objects
             such as RouteSegments, RouteNodes and other electrical items to identify
             the region of space in which they are located.
             

Use Cases:

             When the client developer wants to work on a Wire Harness design, and needs to describe
             a space or region of the electrical system. In Teamcenter this is done by using the
             RouteLocation object which is associated by RouteSegments, RouteNodes
             and RouteCurves. Using this operation, the user will able to create a RouteLocation
             object.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Properties: 
                         An <b>Item</b> is created for each <b>RouteLocation</b> Property in the list. The
                         data on the <b>RouteLocation</b> Properties is used to create initial values on the
                         <b>RouteLocation</b> and related objects.
             
        :param Container: 
                         Object to which all the <b>RouteLocations</b> created will be related to via the
                         input relationType (Folder instance and contents relationType). If not specified
                         the <b>RouteLocation</b> will be created, but without a relation to a containing
                         object.
             
        :param RelationType: 
                         The name of the relation used to attach the created <b>RouteLocation</b> to the input
                         container. This argument is used only when the container argument is present.
             
        :return: 
        """
        ...
    def DeleteRouteObjects(self, Inputs: list[DeleteRouteObjectsInfo]) -> DeleteRouteObjectsResponse:
        """    
             This operation allows client applications to delete the route objects along with
             associated route segments, route curves and nodes in a specific context which is
             given by the client developer.
             

Use Cases:

             When the client developer wants to delete route objects and its associated route
             segment, route curve and route node objects, the deleteRouteObjects operation should
             be used.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         This is a list of DeleteRouteObjectsInfo structures and contains information of
                         the route object which the user wants to delete. DeleteRouteObjectsInfo has the context
                         in which client developer wants to delete the route object, RouteData, NodeData,
                         SegmentData and curvedata.
             
        :return: 
        """
        ...
    def AssociateWireProtectionToSegments(self, Inputs: list[WireProtectionData]) -> AssociateWireProtectionToSegmentsResponse:
        """    
             This operation is used to create the wire protection to segments association between
             primary and secondary BOMLines/objects in a structure and update the protection
             data.
             

Use Cases:

             Associate wire protection data to a segment.
             
             A list of WireProtectionData is first created. WireProtectionData must contain the
             BOMLine to which the route segments and the protection data are to be assigned,
             also the list of segments and the protection data values. The protection data values
             such as "start_location", "end_location", "gradient" and "taping_direction" are set
             in the protectionAreaData map. Then this list of WireProtectionData is sent as an
             input parameter to the associateWireProtectionToSegments operation to establish the
             association.
             


Teamcenter Component:

             WireHarnessServices - SOA services to create/update/delete of Harness structure with
             devices; connectors; pins; wires; cables; shields; connections; their attributes
             and their association.
             
        :param Inputs: 
                         This is a list of WireProtectionData structures containing information about the
                         wire protection and the segments.
             
        :return: 
        """
        ...
    def CreateOrUpdateHarness(self, Inputs: list[HarnessInfo], BomViewTypeName: str, Precise: bool) -> CreateOrUpdateHarnessResponse:
        """    
             This operation is used to create or update the harness structures with all connections,
             devices, connectors, cables, shields, ports and wires with associations.
             

Use Cases:

             Create a Wire Harness.
             
             To create a wire harness the user must first create HarnessData. The HarnessData
             must be populated with all the connections, connectors, cables, shields, devices
             and wires that need to be created in the Teamcenter database. After all the HarnessData
             is ready it is passed to the server along with the BOM view type and a flag to create
             a precise or imprecise structure.
             


Teamcenter Component:

             WireHarnessServices - SOA services to create/update/delete of Harness structure with
             devices; connectors; pins; wires; cables; shields; connections; their attributes
             and their association.
             
        :param Inputs: 
                         This is a list of HarnessInfo for creating or updating the harness structure and
                         the associations between the <b>BOMLine</b> of the Harness Structure in Teamcenter
                         database.
             
        :param BomViewTypeName: 
                         This is a type of <b>BOMView</b> to be created.
             
        :param Precise: 
                         This is a flag that if true signals to create a precise structure else imprecise
                         structure.
             
        :return: 
        """
        ...
    def CreateOrUpdateWireData(self, Inputs: list[WireData]) -> CreateOrUpdateWireDataResponse:
        """    
             This operation is used to create or update a wire business object for each WireData
             structure. The Wiredata consists of length data, color data, number, multiplier,
             offset, separation code etc. associated with each wire business object. This operation
             requires a wire business object which the client developer wants to create or update,
             if it is not provided, the operation will fail for a particular wire business object
             and an error is returned in service data as a partial error. If the client developer
             inputs the wire business object as a wire BOMLine then only length and wire
             properties are applicable.
             

Use Cases:

             Typically this is used to create wire data, assigning the wire length, color, etc.
             It can also be used to update existing wire data, allowing these wire data attributes
             to be changed.
             

Teamcenter Component:

             WireHarnessServices - SOA services to create/update/delete of Harness structure with
             devices; connectors; pins; wires; cables; shields; connections; their attributes
             and their association.
             
        :param Inputs: 
                         Structures containing the details of the wire business object to be created/modified.
             
        :return: 
        """
        ...
    def DeleteWireData(self, Wires: list[Teamcenter.Soa.Client.Model.ModelObject]) -> DeleteWireDataResponse:
        """    
             This operation is used to delete all the wire related data (like length, color, multiplier
             etc.) of given wire objects. The updated wire object will be returned in the updated
             objects list of the ServiceData.
             

Use Cases:

             In this use case a list of wire Item objects or wire BOMLine objects
             are passed to be deleted.
             

Teamcenter Component:

             WireHarnessServices - SOA services to create/update/delete of Harness structure with
             devices; connectors; pins; wires; cables; shields; connections; their attributes
             and their association.
             
        :param Wires: 
                         Array of wire objects to be deleted from the Teamcenter database. These objects can
                         be wire <b>Items</b> or wire <b>BOMLines</b>.
             
        :return: 
        """
        ...
    def GetWireData(self, Wires: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetWireDataResponse:
        """    
             This operation is used to get the wire related data e.g. length, color, multiplier,
             offset etc.
             

Use Cases:

             In this use case a list of wire Item objects or wire BOMLine objects
             are passed. These passed objects must contain the unique identifier (uid) of the
             objects to be fetched. The operation returns the length, the color and the other
             information for wires in a list of WireData.
             

Teamcenter Component:

             WireHarnessServices - SOA services to create/update/delete of Harness structure with
             devices; connectors; pins; wires; cables; shields; connections; their attributes
             and their association.
             
        :param Wires: 
                         Array of wire objects to retrieve their wire data from the Teamcenter database. These
                         objects can be wire <b>Items</b> or wire <b>BOMLines</b>.
             
        :return: 
        """
        ...
    def GetWireProtectionSegments(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> GetWireProtectionSegmentResponse:
        """    
             This operation gets the segments and wire protection data of the input wire protection
             line. If errors occur during this operation they are returned as part of the partial
             errors list of the ServiceData element.
             

Use Cases:

             First create a list of BOMLines for which the wire protection data needs to
             be fetched. Then send this list as an input parameter of the operation. The operation
             gets the segments and the associated wire protection area data.
             

Teamcenter Component:

             WireHarnessServices - SOA services to create/update/delete of Harness structure with
             devices; connectors; pins; wires; cables; shields; connections; their attributes
             and their association.
             
        :param Inputs: 
                         This is a list of Wire protection <b>BOMLines</b> for which the WireProtectionData
                         needs to be retrieved.
             
        :return: 
        """
        ...
    def RemoveWireProtectionAssociation(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> RemoveWireProtectionAssociationResponse:
        """    
             This operation removes the association between the segments and the wire protection
             line and also deletes the associated wire protection area data for the BOMLine.
             The updated wire protection business objects will be returned as part of the updated
             objects list of the ServiceData.
             

Use Cases:

             Remove the wire protection association from a BOMLine.
             
             First create a list of BOMLines for which wire protect data needs to be removed.
             Then send this list as an input parameter of the operation. This operation removes
             the association between the segments and the wire protection line, deletes the associated
             wire protection area data for the BOMLine and returns the updated objects.
             


Teamcenter Component:

             WireHarnessServices - SOA services to create/update/delete of Harness structure with
             devices; connectors; pins; wires; cables; shields; connections; their attributes
             and their association.
             
        :param Inputs: 
                         This is a list of Wire protection <b>BOMLines</b>.
             
        :return: 
        """
        ...

