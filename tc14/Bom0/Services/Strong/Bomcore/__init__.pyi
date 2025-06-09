import Bom0.Services.Strong.Bomcore._2016_10.AlignmentManagement
import System
import Teamcenter.Soa.Client

class AlignmentManagementRestBindingStub(AlignmentManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetAlignedBOMData(self, Inputs: list[Bom0.Services.Strong.Bomcore._2016_10.AlignmentManagement.DesignElementInfoGroup]) -> Bom0.Services.Strong.Bomcore._2016_10.AlignmentManagement.GetAlignedBOMDataResponse: ...

class AlignmentManagementService:
    """
    
            This service contains the operations related to the alignment between BOM and Design
            data.
            


Library Reference:

Bom0SoaBomCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> AlignmentManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetAlignedBOMData(self, Inputs: list[Bom0.Services.Strong.Bomcore._2016_10.AlignmentManagement.DesignElementInfoGroup]) -> Bom0.Services.Strong.Bomcore._2016_10.AlignmentManagement.GetAlignedBOMDataResponse:
        """    
             This operation returns BOM data aligned to Cpd0DesignElement objects configured
             with input ConfigurationContext. This operation
             works in set based fashion where you can provide Cpd0DesignElement objects
             in multiple ConfigurationContexts. The operation
             would return BOM Data corresponding to the Cpd0DesignElement  objects it is
             aligned with.
             

Use Cases:

             A NX user can view the BOM data by selecting Cpd0DesignElement objects within
             his ConfigurationContext.
             

Teamcenter Component:

             bom0bommanagement - Component for the template - bom0bommanagement
             
        :param Inputs: 
                         Information used to get the alinged BOM data.
             
        :return: 
        """
        ...

