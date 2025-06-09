import Lgt0.Services.Strong.Logistics._2014_06.LogisticsPlanning
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class LogisticsPlanningRestBindingStub(LogisticsPlanningService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def AssignContainersToStations(self, InputList: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Lgt0.Services.Strong.Logistics._2014_06.LogisticsPlanning.AssignStationsResponse: ...
    def GetCandidateStations(self, InputList: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Lgt0.Services.Strong.Logistics._2014_06.LogisticsPlanning.CandidateStationResponse: ...
    def GetTransportNetworkInfo(self, InputList: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Lgt0.Services.Strong.Logistics._2014_06.LogisticsPlanning.TransportNetworkResponse: ...

class LogisticsPlanningService:
    """
    
            The service contains the operations that fetch logistics data.
            

Dependencies:

            ProcessHistoryManagement
            


Library Reference:

Lgt0SoaLogisticsStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> LogisticsPlanningService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def AssignContainersToStations(self, InputList: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Lgt0.Services.Strong.Logistics._2014_06.LogisticsPlanning.AssignStationsResponse:
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
    def GetCandidateStations(self, InputList: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Lgt0.Services.Strong.Logistics._2014_06.LogisticsPlanning.CandidateStationResponse:
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
    def GetTransportNetworkInfo(self, InputList: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Lgt0.Services.Strong.Logistics._2014_06.LogisticsPlanning.TransportNetworkResponse:
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

