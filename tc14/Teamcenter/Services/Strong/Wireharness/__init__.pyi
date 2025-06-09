import System
import Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class WireHarnessRestBindingStub(WireHarnessService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateOrUpdateRouteObjects(self, Inputs: list[Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.RouteInfo]) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.CreateOrUpdateRouteObjectsResponse: ...
    def CreateRouteLocations(self, Properties: list[Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.RouteLocationProperties], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.CreateRouteLocationsResponse: ...
    def DeleteRouteObjects(self, Inputs: list[Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.DeleteRouteObjectsInfo]) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.DeleteRouteObjectsResponse: ...
    def AssociateWireProtectionToSegments(self, Inputs: list[Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.WireProtectionData]) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.AssociateWireProtectionToSegmentsResponse: ...
    def CreateOrUpdateHarness(self, Inputs: list[Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.HarnessInfo], BomViewTypeName: str, Precise: bool) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.CreateOrUpdateHarnessResponse: ...
    def CreateOrUpdateWireData(self, Inputs: list[Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.WireData]) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.CreateOrUpdateWireDataResponse: ...
    def DeleteWireData(self, Wires: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.DeleteWireDataResponse: ...
    def GetWireData(self, Wires: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.GetWireDataResponse: ...
    def GetWireProtectionSegments(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.GetWireProtectionSegmentResponse: ...
    def RemoveWireProtectionAssociation(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.RemoveWireProtectionAssociationResponse: ...

class WireHarnessService:
    """
    
            The WireHarness service exposes operations to create, update, and
delete Harness
            structures. It works with all types of harness objects like
Connections, Devices,
            Connectors, cables, Shields, Ports, Wires. It handles all associated
data and allows
            the creation of  associations between harness elements in the
structure. The operations
            allow creating precise and imprecise structures. Along with Harness
structure creation
            the associations like ConnectedTo, ImplementedBy, RealizedBy etc can
also be created
            using the operations exposed in this service. The service also
exposes operations
            which create and update Route objects and creating, deleting, or
updating their associated
            data like RoutePath, RouteSegment, RouteNode, and RouteCurve.
            The service exposes operations to update properties on Harness
objects. The service
            also contains operations which creates and updates wire data, length
data, and color
            data of the wire objects.  The service exposes operations to manage
the association
            between wire protection objects and segment objects.

            The service provides the following use cases for Harness data
structure:

Creation of precise or imprecise harness structure.

Modifying the harness data of the structure.

Creating associations between structure elements of Harness structure.

Removing associations between structure elements of Harness structure.

Creating Route and associated objects.

Updating of Route and associated objects.

Deletion of Route and associated objects.

Creation of wire data.

Updating of wire data.

            .

Dependencies:

            DataManagement, StructureManagement

Library Reference:

TcSoaWireHarnessStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> WireHarnessService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateOrUpdateRouteObjects(self, Inputs: list[Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.RouteInfo]) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.CreateOrUpdateRouteObjectsResponse:
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
    def CreateRouteLocations(self, Properties: list[Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.RouteLocationProperties], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.CreateRouteLocationsResponse:
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
    def DeleteRouteObjects(self, Inputs: list[Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.DeleteRouteObjectsInfo]) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.DeleteRouteObjectsResponse:
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
    def AssociateWireProtectionToSegments(self, Inputs: list[Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.WireProtectionData]) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.AssociateWireProtectionToSegmentsResponse:
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
    def CreateOrUpdateHarness(self, Inputs: list[Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.HarnessInfo], BomViewTypeName: str, Precise: bool) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.CreateOrUpdateHarnessResponse:
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
    def CreateOrUpdateWireData(self, Inputs: list[Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.WireData]) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.CreateOrUpdateWireDataResponse:
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
    def DeleteWireData(self, Wires: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.DeleteWireDataResponse:
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
    def GetWireData(self, Wires: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.GetWireDataResponse:
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
    def GetWireProtectionSegments(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.GetWireProtectionSegmentResponse:
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
    def RemoveWireProtectionAssociation(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Services.Strong.Wireharness._2008_06.WireHarness.RemoveWireProtectionAssociationResponse:
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

