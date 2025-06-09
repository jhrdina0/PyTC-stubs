import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class AssignedStationsInfo:
    """
    A structure providing information on already assigned stations to the provision.
    """
    def __init__(self, ) -> None: ...
    Station: Teamcenter.Soa.Client.Model.ModelObject
    """Represents a station of type Mfg0BvrWorkArea which is assigned to the provision."""
    IsValid: bool
    """The flag representing whether the assigned station is a valid candidate for the provision."""

class AssignStationsResponse:
    """
    
            The response contains a map which holds the station as a key and a list of assigned
            containers as the value. Additionally the reponse contains the service data. The
            service data can contain following error messages.
            


64002 - The information for this object cannot be fetched
            as the object is not in the  context of Logistics Bill Of Processes (BOP).
            


    """
    def __init__(self, ) -> None: ...
    AssignedStationsInfo: System.Collections.Hashtable
    """
            The map (Mfg0BvrWorkArea, list of Lgt0BvrContainer) of a station and
            the list of containers assigned to that station.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data containing partial errors."""

class CandidateStationResponse:
    """
    
            The response contains a map which holds the part family as a key and a list of structure
            containing the  information related to provisions and their candidate stations. The
            reponse also contains service data that reports following error messages.
            

64002 - The information for this object cannot be fetched
            as the object is not in the  context of Logistics Bill Of Processes (BOP).
            
64003 - The information cannot be fetched for this object.
            


    """
    def __init__(self, ) -> None: ...
    InfoMap: System.Collections.Hashtable
    """
            A map(Lgt0BvrPartFamProc, list of stationInfo) of part family and  stationInfo
            list specifying provisions and candidate stations pairs for that part family.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data containing partial errors."""

class PlantInfoStruct:
    """
    The structure holding the plant information.
    """
    def __init__(self, ) -> None: ...
    Plant: Teamcenter.Soa.Client.Model.ModelObject
    """The BOMLine representing the plant line of type Mfg0BvrWorkArea."""
    PlantAddress: list[str]
    """The list of strings holding the address of the plant."""

class StationInfo:
    """
    The structure containing the details about the provisions and their candidate stations
    """
    def __init__(self, ) -> None: ...
    PartFamily: Teamcenter.Soa.Client.Model.ModelObject
    """
            Represents the part family of type Lgt0BvrPartFamProc to which supply chain
            and provision belongs.
            """
    SupplyChain: Teamcenter.Soa.Client.Model.ModelObject
    """
            Represents inbound supply chain of type Lgt0BvrInbdSupChain to which provision
            belongs
            """
    Provision: Teamcenter.Soa.Client.Model.ModelObject
    """
            Represents the provision of type Lgt0BvrProvision for which candidate stations
            are fetched
            """
    CandidateStationsList: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of stations of type Mfg0BvrWorkArea which can be assigned to the provision"""
    ParentHeirarchyList: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            List of BOMLines representing the parent hierarchy of the provision. The first member
            in the list represents the immediate parent of the provision and so on
            """
    AssignedStationsList: list[AssignedStationsInfo]
    """A list of structures providing information on already assigned stations to the provision"""

class SupplierInfoStruct:
    """
    The structure containing the details about the supplier.
    """
    def __init__(self, ) -> None: ...
    PartFamily: Teamcenter.Soa.Client.Model.ModelObject
    """
            The BOMLine of the part family to which inbound supply chain belongs. The
            supplier is associated with this inbound supply chain.
            """
    Supplier: Teamcenter.Soa.Client.Model.ModelObject
    """The BOMLine of the supplier associated with the inbound supply chain."""
    SupplierAddress: list[str]
    """Address of the supplier."""

class TransportNetworkResponse:
    """
    
            The response contains the information about the plant to which materials are delivered
            and a map which holds the Inbound supply chain as a key and a structure containing
            its supplier information. Additionally the reponse contains the service data. The
            service data can contain following error messages.
            

264002 - The information for this object cannot be fetched
            as the object is not in the  context of Logistics Bill Of Processes (BOP).
            
264003 - The operation is not supported for this object.
            


    """
    def __init__(self, ) -> None: ...
    PlantInfo: PlantInfoStruct
    """The structure holding the plant information."""
    SupplyChainDetails: System.Collections.Hashtable
    """
            The map (Lgt0BvrInbdSupChain, supplierInfoStruct) of inbound supply chain
            and related supplier information pairs.
            

            The key represents a BOMline representing the inbound supply chain of type
            Lgt0BvrInbdSupChain and the value represents the structure containing the
            details about the supplier
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data containing partial errors."""

class LogisticsPlanning:
    """
    Interface LogisticsPlanning
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AssignContainersToStations(self, InputList: list[Teamcenter.Soa.Client.Model.ModelObject]) -> AssignStationsResponse:
        """    
             This service operation assigns the container available in an in-plant supply chain
             to the station. In the logistics structure, this station is found under the provision
             of the in-plant supply chain.
             
             The operation takes a list of BOMLine(s) in the context of Logistics BOP as
             input. The acceptable BOMLine objects are station, provision, in-plant supply
             chain, part family, logistics folder or the logistics Bill Of Process (BOP).
             
             In response, the operation returns a map having the station as a key and the list
             of all assigned containers as the value. The BOMLine(s) in the response are in the
             context of the plant structure.
             


Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param InputList: 
<ul>
<li type="disc"><b>Mfg0BvrWorkArea</b> - Station Line.
                         </li>
<li type="disc"><b>Lgt0BvrProvision</b> - Provision line.
                         </li>
<li type="disc"><b>Lgt0BvrInbdSupChain</b> In-plant supply chain line.
                         </li>
<li type="disc"><b>Lgt0BvrPartFamProc</b>- Part family line.
                         </li>
<li type="disc"><b>Lgt0BvrLogisticFldr</b> - Logistics folder line.
                         </li>
<li type="disc"><b>Lgt0BvrLogisticBOP</b> - Logistics BOP line.
                         </li>
</ul>

        :return: 
        """
        ...
    def GetCandidateStations(self, InputList: list[Teamcenter.Soa.Client.Model.ModelObject]) -> CandidateStationResponse:
        """    
             This service operation fetches the information about all the stations which can be
             assigned to the provisions under the hierarchy of the given input BOMLine.
             The acceptable BOMLine objects are Lgt0BvrProvision Lgt0BvrInbdSupChain, Lgt0BvrPartFamProc,
             Lgt0BvrLogisticFldr or the Lgt0BvrLogisticBOP.
             
             The operation returns BOMLine(s) representing all the candidate stations which
             can be assigned to the provisions. It also returns the station that is assigned to
             the provision and indicates whether the assigned station is one of the candidates.
             
             Additionally the operation returns the list of business objects representing the
             parent hierarchy of the provision lines in the Logistics BOP structure.
             


Use Cases:

Use Case 1: Fetching candidate stations for a given BOMLine.

             This operation can be used to fetch the candidate stations for the provisions under
             the heirarchy of the given BOM Line. In response, a list of candidate stations are
             fetched and populated on the view against each provision. User can select a station
             among candidate stations to resolve with provision. The view indicates the station
             which is assigned to the provision.
             
             A separate list of business objects representing the parent heirarchy of the provision
             line is also fetched and displayed on the view.
             


Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param InputList: 
<ul>
<li type="disc"><b>Lgt0BvrProvision</b> - Provision line.
                         </li>
<li type="disc"><b>Lgt0BvrInbdSupChain</b> - Inbound supply chain line.
                         </li>
<li type="disc"><b>Lgt0BvrPartFamProc</b> - Part family line.
                         </li>
<li type="disc"><b>Lgt0BvrLogisticFldr</b> - Logistics folder line.
                         </li>
<li type="disc"><b>Lgt0BvrLogisticBOP</b> - Logistics BOP line.
                         </li>
</ul>

        :return: 
        """
        ...
    def GetTransportNetworkInfo(self, InputList: list[Teamcenter.Soa.Client.Model.ModelObject]) -> TransportNetworkResponse:
        """    
             This service operation fetches the information about the transport networks from
             suppliers to the plant.
             
             The operation takes a list of business objects as input. The valid business objects
             are inbound supply chain, part family, logistics folder and the logistics bill of
             process (BOP).
             
             In response, the operation fetches the information of the supplier associated with
             the supply chains of each part family in the hierarchy of the input BOMLine.
             The address of the supplier and the plant with other relevant properties value are
             also fetched.
             


Use Cases:

Use Case 1: Drawing the transport network on the map.

             This operation can be used to fetch the transport network information for the supplier
             and the plant and can be displayed on the map. The network information on the map
             shows locations of suppliers and their distance from the plant.
             


Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param InputList: 
<ul>
<li type="disc"><b>Lgt0BvrInbdSupChain</b>- Inbound supply chain line.
                         </li>
<li type="disc"><b>Lgt0BvrPartFamProc</b>- Part family line.
                         </li>
<li type="disc"><b>Lgt0BvrLogisticFldr</b>- Logistics folder line.
                         </li>
<li type="disc"><b>Lgt0BvrLogisticBOP</b> - BOP - Logistics BOP line.
                         </li>
</ul>

        :return: 
        """
        ...

