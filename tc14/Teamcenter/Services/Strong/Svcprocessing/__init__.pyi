import System
import Teamcenter.Services.Strong.Svcprocessing._2009_06.ServiceProcessing
import Teamcenter.Soa.Client

class ServiceProcessingRestBindingStub(ServiceProcessingService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def SetTxnElementStatus(self, Info: list[Teamcenter.Services.Strong.Svcprocessing._2009_06.ServiceProcessing.SetTxnStatusInfo]) -> Teamcenter.Services.Strong.Svcprocessing._2009_06.ServiceProcessing.SetTxnStatusResponse: ...

class ServiceProcessingService:
    """
    
            ServiceProcessing service

Library Reference:

TcSoaSvcProcessingStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ServiceProcessingService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def SetTxnElementStatus(self, Info: list[Teamcenter.Services.Strong.Svcprocessing._2009_06.ServiceProcessing.SetTxnStatusInfo]) -> Teamcenter.Services.Strong.Svcprocessing._2009_06.ServiceProcessing.SetTxnStatusResponse:
        """    
             This operation sets the status of the transaction element based on the SetTxnStatusInfo supplied. The SetTxnStatusInfo
             contains information for properties such as clientId
             and data. The value of the approval attribute
             is obtained and the corresponding transaction element status is set by calling the
             operation setTxnElementStatus.  This operation
             utilizes the input information which consists of the approval value, the transaction
             element type and name. The operation performs validations to ensure that all conditions
             are met and an attempt to approve an object that is already approved throws an appropriate
             error message to the user.
             

Teamcenter Component:

             Service Processing - This Component is intended to identify all Operations and Services
             under Service Processing.
             
        :param Info: 

        :return: 
        """
        ...

