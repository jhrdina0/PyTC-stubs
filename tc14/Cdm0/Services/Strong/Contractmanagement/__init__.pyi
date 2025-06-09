import Cdm0.Services.Strong.Contractmanagement._2014_10.ContractManagement
import Cdm0.Services.Strong.Contractmanagement._2018_06.ContractManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class ContractManagementRestBindingStub(ContractManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateOrUpdateSubDelSchedules(self, Cdm0Input: list[Cdm0.Services.Strong.Contractmanagement._2014_10.ContractManagement.CreateOrUpdateSubSchObjectProperties]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetImpactedDataReqItemRevisions(self, Cdm0Input: list[Cdm0.Services.Strong.Contractmanagement._2014_10.ContractManagement.ContractManagementInput]) -> Cdm0.Services.Strong.Contractmanagement._2014_10.ContractManagement.ContractManagementResponse: ...
    def CreateOrUpdateSubDelSchedules2(self, CreateOrUpdateSubSchInput: list[Cdm0.Services.Strong.Contractmanagement._2018_06.ContractManagement.CreateOrUpdateSubSchInput], PerformAsynchronously: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class ContractManagementService:
    """
    
            This contractmanagement service will implement the contract event rescheduling(create
            or update(reschedule) based on the changes in contract events and/or DRI events)
            functionality.
            


Library Reference:

Cdm0SoaContractManagementStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ContractManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateOrUpdateSubDelSchedules(self, Cdm0Input: list[Cdm0.Services.Strong.Contractmanagement._2014_10.ContractManagement.CreateOrUpdateSubSchObjectProperties]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates or updates Schedules for Cdm0ContractRevision or Cdm0DataReqItemRevision.
             Schedule corresponding to Cdm0ContractRevision is refered as Contract event
             schedule which can only be created and not updated. Schedule corresponding to Cdm0DataReqItemRevision
             is refered as submnittal deleivery schedule, which can be created or updated. Input
             will be list of  Cdm0DataReqItemRevision or Cdm0ContractRevision objects.
             Partial errors will be returned in the ServiceData (returns only error data and no
             created or updated business object), in case of,
             
                 Generation of submittal delivery schedule is not successful
             for    Cdm0DataReqItemRevision object OR
             
                 Generation of contract event schedule is not successful for
             Cdm0ContractRevision object
             

Use Cases:

             Use Case 1: User selects Cdm0DataReqItemRevision and invokes generate submittal
             delievery schedule in RAC.
             
             Description of Use case 1.
             
             1.    Create a contract with DRIs related to it. Add contract
             event schedule and add tasks to the contract event schedule.
             
             2.    Go to DRI revision and invoke "Generate Submittal Delivery
             Schedule"
             
             3.    Submittal delevery scehule will be generated for selected
             DRI
             
             4.    Check If schedule exists with DRI,
             
             a.    If does not exist it will generate new schedule.
             
             b.    If exists, it will update exisitng schedule
             

             Use Case 2: In RAC, user selects Cdm0ContractRevision and invokes Regenerate
             Submittal Delivery Schedules
             
             Description of Use case 2.
             
             1.    Create a contract with DRIs related to it.
             

             2.    Generate submittal delivery schedules for all the created
             DRIs using the 'Generate Submittal Delivery Schedules' menu at DRI revision level
             
             3.    All the Cdm0DataReqItemRevisions related to the
             contract will be updated with latest contract event schedule changes
             

             Use Case 3: In RAC, user selects Cdm0ContractRevision and invokes Add contract
             event schedule
             
             Description of Use case 3.
             
             1.    Create a contract with DRIs related to it.
             
             2.    Add contract event schedule and add tasks to the contract
             event schedule.  Select  Cdm0ContractRevision and invoke "Add contract event schedule"
             
             3.    Contract event schedule will be generated for the selected
             Cdm0ContractRevision



Teamcenter Component:

             ContractManagement - Component for Cdm0ContractManagement.
             
        :param Cdm0Input: 

        :return: 
        """
        ...
    def GetImpactedDataReqItemRevisions(self, Cdm0Input: list[Cdm0.Services.Strong.Contractmanagement._2014_10.ContractManagement.ContractManagementInput]) -> Cdm0.Services.Strong.Contractmanagement._2014_10.ContractManagement.ContractManagementResponse:
        """    
             This method retrieves impacted Cdm0DataReqItemRevision objects with associated
             Cdm0EventsTable objects for a given Cdm0ContractRevision.
             



Use Cases:

             Use Case 1: User selects Cdm0ContractRevision object and invokes "Reschedule
             Data Requirement Items" from RMB.
             

             Description of Use case 1.
             
             1.    User selects an existing Contract revison which has DRIs
             related to it
             
             2.    User invokes "Reschedule Data Requirement Items" from RMB
             menu
             
             3.    Imapcted Data Requirement Items with their corresponding
             event lists will be returned.
             


Teamcenter Component:

             ContractManagement - Component for Cdm0ContractManagement.
             
        :param Cdm0Input: 
                         ContractManagementInput contains clientId and contractObject
             
        :return: 
        """
        ...
    def CreateOrUpdateSubDelSchedules2(self, CreateOrUpdateSubSchInput: list[Cdm0.Services.Strong.Contractmanagement._2018_06.ContractManagement.CreateOrUpdateSubSchInput], PerformAsynchronously: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

