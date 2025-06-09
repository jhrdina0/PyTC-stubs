import Fdp0.Services.Strong.Fourdplanning._2013_05.DataManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class DataManagementRestBindingStub(DataManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateOrUpdateProcessToTaskRelation(self, Inputs: list[Fdp0.Services.Strong.Fourdplanning._2013_05.DataManagement.CreateOrUpdateProcessToTaskRelationInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class DataManagementService:
    """
    
            Data Management Service
            


Library Reference:

Fdp0SoaFourDPlanningStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DataManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateOrUpdateProcessToTaskRelation(self, Inputs: list[Fdp0.Services.Strong.Fourdplanning._2013_05.DataManagement.CreateOrUpdateProcessToTaskRelationInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation takes the source, target and naming information as input and creates
             a process structure based on that.
             

Teamcenter Component:

             FourD Planning - This Teamcenter component deals with specific requirements related
             to Ship Building Industry.        Which includes enhancements to structure search
             to support 4D search  i.e. search along a time line.
             
        :param Inputs: 
                         Vector of CreateOrUpdateProcessToTaskRelationInfo structure.
             
        :return: - Delete relation operation failed.
        """
        ...

