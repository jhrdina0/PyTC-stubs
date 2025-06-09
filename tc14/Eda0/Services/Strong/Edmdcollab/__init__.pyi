import Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration
import Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class EDMDCollaborationRestBindingStub(EDMDCollaborationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CancelProcessChange(self, CancelProcessInput: Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.CancelProcessInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CancelPublishIntent(self, CancelPublishInput: Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.CancelPublishInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CheckIDXToProcess(self, CheckIDXInput: Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.CheckIDXInput) -> Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.CheckIDXToProcessResponse: ...
    def DeleteIDX(self, DeleteInput: Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.DeleteInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetCollaborationData(self, GetCollaborationData: Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.GetCollaborationInput) -> Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.GetCollaborationDataResponse: ...
    def PublishIDX(self, PublishInput: Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.PublishInput) -> Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.PublishIDXResponse: ...
    def RegisterPublishIntent(self, RegisterIntentInput: Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.RegisterIntentInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateOrUpdateCollaboration(self, CreateOrUpdateInput: Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.CreateOrUpdateInput) -> Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.CreateOrUpdateResponse: ...
    def GetAssemblyContext3DModels(self, DesignUID: str) -> Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.GetAssembly3DModelsResponse: ...
    def GetCollaborationData2(self, GetCollaborationInput: Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.GetCollaborationInput2) -> Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.GetCollaborationDataResponse2: ...
    def PublishAssemblyContext(self, PublishAssemblyInput: Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.PublishAssemblyInput) -> Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.PublishAssemblyResponse: ...
    def PublishIDX2(self, PublishInput: Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.PublishInput2) -> Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.PublishIDXResponse2: ...

class EDMDCollaborationService:
    """
    
            This service contains all the operations which support the Teamcenter ECAD MCAD Collaboration
            Solution.
            


Library Reference:

Eda0SoaEDMDCollabStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> EDMDCollaborationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CancelProcessChange(self, CancelProcessInput: Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.CancelProcessInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CancelPublishIntent(self, CancelPublishInput: Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.CancelPublishInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CheckIDXToProcess(self, CheckIDXInput: Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.CheckIDXInput) -> Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.CheckIDXToProcessResponse: ...
    def DeleteIDX(self, DeleteInput: Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.DeleteInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetCollaborationData(self, GetCollaborationData: Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.GetCollaborationInput) -> Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.GetCollaborationDataResponse: ...
    def PublishIDX(self, PublishInput: Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.PublishInput) -> Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.PublishIDXResponse: ...
    def RegisterPublishIntent(self, RegisterIntentInput: Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.RegisterIntentInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateOrUpdateCollaboration(self, CreateOrUpdateInput: Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.CreateOrUpdateInput) -> Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.CreateOrUpdateResponse: ...
    def GetAssemblyContext3DModels(self, DesignUID: str) -> Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.GetAssembly3DModelsResponse: ...
    def GetCollaborationData2(self, GetCollaborationInput: Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.GetCollaborationInput2) -> Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.GetCollaborationDataResponse2: ...
    def PublishAssemblyContext(self, PublishAssemblyInput: Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.PublishAssemblyInput) -> Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.PublishAssemblyResponse: ...
    def PublishIDX2(self, PublishInput: Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.PublishInput2) -> Eda0.Services.Strong.Edmdcollab._2020_04.EDMDCollaboration.PublishIDXResponse2:
        """    
             This operation creates a new Eda0IDX business object in Teamcenter for a Design
             participating in an ECAD MCAD Collaboration. Optionally, it also allows creation
             of a package containing 3D Model files corresponding to Printed Circuit Board components
             contained within an Eda0IDXBaseline or Eda0IDXIncrement.
             

             ECAD MCAD Collaboration is a process of exchange of incremental design changes between
             ECAD and MCAD engineers, during the design process for a Printed Circuit Board (PCB).
             The IDX file format is a STEP (STandard for the Exchange of Product
             model data) based neutral format that stores electromechanical data using an XML
             schema.
             

             In Teamcenter, IDX files for an ECAD MCAD Collaboration are managed as Eda0IDXBaseline,
             Eda0IDXIncrement and Eda0IDXResponse objects, which are types of Eda0IDX
             business object.
             

Eda0IDX represents any Teamcenter managed IDX object.
             

Eda0IDXBaseline represents the IDX Baseline object in ECAD MCAD Collaboration.
             The IDX Baseline object represents an IDX file, in which the board outline and the
             complete geometry information of the PCB is captured. The IDX Baseline is the agreed
             state of a PCB design, starting from which the ECAD and MCAD tools would make incremental
             changes and collaborate with each other in the PCB development process.
             

Eda0IDXIncrement represents an IDX (Interdomain Design Exchange) file which
             contains the incremental changes in a PCB layout, during the collaboration between
             ECAD and MCAD, as a part of PCB development process.
             

Eda0IDXResponse represents an IDX (Interdomain Design Exchange) file, which
             is created as a part of ECAD or MCAD tool reviewing and accepting or rejecting the
             proposed incremental changes. The IDX Response file is then imported by the tool
             which initiated the proposal, to bring the design in sync in both ECAD and MCAD tools.
             

Use Cases:

             Use Case 1:
             

ECAD or the MCAD designer while working on the PCB design, use the
             export IDX Baseline functionality within the respective tool, to create Eda0IDXBaseline
             object in Teamcenter. Optionally ECAD designer may also publish the Components 3D
             Model Package file along with Eda0IDXBaseline.
             
The preceding Eda0IDXBaseline and any Eda0IDXIncrement
             business objects published by the calling domain, if existing, are marked as obsoleted
             in Teamcenter.
             



             Use Case 2:
             

ECAD or the MCAD designer while working on the PCB design, use the
             export IDX Increment functionality within the respective tool, to create a Eda0IDXIncrement
             object in Teamcenter. Optionally ECAD designer may also publish the Components 3D
             Model Package file along with Eda0IDXIncrement.
             



             Use Case 3:
             

ECAD or the MCAD designer while working on the PCB design in their
             respective tool, imports an IDX Increment for reviewing the changes.
             
The designer reviews the changes contained within the IDX file, accepts
             or rejects each change and publishes an IDX Response to create an Eda0IDXResponse
             object in Teamcenter.
             



Teamcenter Component:

             EDA Server Support - This feature extends the Teamcenter data model to support Teamcenter
             Electronic Design Automation integrations that allow ECAD designers to log on to
             Teamcenter and open, save, request parts, and check in and check out PCB design data.
             
        :param PublishInput: 
                         This structure represents the input to the operation.
             
        :return: 
        """
        ...

