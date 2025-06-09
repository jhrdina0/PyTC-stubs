import Imd0.Services.Strong.Medicaldevice._2020_01.DIManagement
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model.Strong

class DIManagementRestBindingStub(DIManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetHigherLevelPkgSKUInfo(self, Input: Teamcenter.Soa.Client.Model.Strong.Pmg0ItemSKURevision) -> Imd0.Services.Strong.Medicaldevice._2020_01.DIManagement.HigherLevelPkgSKUResponse: ...

class DIManagementService:
    """
    
            The DIManagement service exposes operations which enables users to manage Device
            Identifier(DI) of a Medical Device. This service provides following use cases:
            

Get information of Package Device Identifier(subtype of Higher Level
            Package) associated to a Device Identifier(subtype of CPG Item SKU)
            




Library Reference:

Imd0SoaMedicalDeviceStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DIManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetHigherLevelPkgSKUInfo(self, Input: Teamcenter.Soa.Client.Model.Strong.Pmg0ItemSKURevision) -> Imd0.Services.Strong.Medicaldevice._2020_01.DIManagement.HigherLevelPkgSKUResponse:
        """    
             This service operation returns packaging information of parent Pmg0HighLevelSKURevision
             associated to Pmg0ItemSKURevision.
             

             Use Case:
             

Pmg0ItemSKURevision will be associated to multiple Pmg0HighLevelSKURevision.
             The packaging information of the parent needs to be shown on the child in the format
             as required by various regulatory agencies.
             

Teamcenter Component:

             Medical Device Submissions Template - Solution template that provides capability
             to create and manage UDI data for FDA-US, IMDRF and NMPA-China
             
        :param Input: 
                         The <b>Pmg0ItemSKURevision</b> object used for searching the associated parent <b>Pmg0HighLevelSKURevision</b>.
             
        :return: 
        """
        ...

