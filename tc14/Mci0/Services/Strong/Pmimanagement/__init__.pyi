import Mci0.Services.Strong.Pmimanagement._2011_12.PMIManagement
import Mci0.Services.Strong.Pmimanagement._2014_06.PMIManagement
import Mci0.Services.Strong.Pmimanagement._2015_10.PMIManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class PMIManagementRestBindingStub(PMIManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreatePMI(self, CreatePMIInputInfo: list[Mci0.Services.Strong.Pmimanagement._2011_12.PMIManagement.CreatePMIInputInfo]) -> Mci0.Services.Strong.Pmimanagement._2011_12.PMIManagement.CreatePMIResponse: ...
    def ImportPMIs(self, InputInfo: list[Mci0.Services.Strong.Pmimanagement._2011_12.PMIManagement.ImportPMIInputInfo]) -> Mci0.Services.Strong.Pmimanagement._2011_12.PMIManagement.ImportPMIsResponse: ...
    def GetDCDs(self, InputBOs: list[Teamcenter.Soa.Client.Model.ModelObject], DcdFilterInfo: Mci0.Services.Strong.Pmimanagement._2014_06.PMIManagement.DCDFilterInfo) -> Mci0.Services.Strong.Pmimanagement._2014_06.PMIManagement.GetDCDsResponse: ...
    def GetPMIProperties(self, Input: list[Mci0.Services.Strong.Pmimanagement._2015_10.PMIManagement.GetPMIPropertiesInputData]) -> Mci0.Services.Strong.Pmimanagement._2015_10.PMIManagement.GetPMIPropertiesResponse: ...
    def ImportPMIs2(self, InputInfo: list[Mci0.Services.Strong.Pmimanagement._2015_10.PMIManagement.ImportPMIInputInfo2]) -> Mci0.Services.Strong.Pmimanagement._2011_12.PMIManagement.ImportPMIsResponse: ...

class PMIManagementService:
    """
    
            The PMIManagement service exposes operations used to create and import Product Manufacturing
            Information (PMI) objects. It introduces new functionality in order to create new
            PMIs, update existing ones and mark as delete PMIs.
            


Library Reference:

Mci0SoaPMIManagementStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> PMIManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreatePMI(self, CreatePMIInputInfo: list[Mci0.Services.Strong.Pmimanagement._2011_12.PMIManagement.CreatePMIInputInfo]) -> Mci0.Services.Strong.Pmimanagement._2011_12.PMIManagement.CreatePMIResponse:
        """    
             This operation creates  Mci0PMI objects under the target ItemRevision. The Mci0PMI
             data will be stored in a Mci0PMIChracteristicFrm in context of the target ItemRevision.
             

Teamcenter Component:

             Product Manufacturing Information (PMI) Component - Product Manufacturing Information
             (PMI) solution to manage the PMI information in Teamcenter.
             
        :param CreatePMIInputInfo: 
                         The input  for createPMIInput
             
        :return: This operation returns the newly created GDELines referring to the new created Mci0PMI.
             The following partial errors may be returned: 69013: Unable to create the Mci0PMIChracteristicFrm
             for the PMI.
        """
        ...
    def ImportPMIs(self, InputInfo: list[Mci0.Services.Strong.Pmimanagement._2011_12.PMIManagement.ImportPMIInputInfo]) -> Mci0.Services.Strong.Pmimanagement._2011_12.PMIManagement.ImportPMIsResponse:
        """    
             The operation imports all the PMIs data from the Mci0PMIXml dataset attached to the
             source ItemRevision. New Mci0PMI objects will be created under the target ItemRevision.
             Existing  Mci0PMI  will be updated or marked as deleted as necessary.
             

Teamcenter Component:

             Product Manufacturing Information (PMI) Component - Product Manufacturing Information
             (PMI) solution to manage the PMI information in Teamcenter.
             
        :param InputInfo: 
                         The input ImportPMIInfo.
             
        :return: The ImportPMIsOutput contains all the information regarding the created, updated
             and marked as deleted PMIs along with target object. The following partial errors
             may be returned: 69005: The dataset is not attached to the BOM Structure. 69011:
             Import PMI operation failed.
        """
        ...
    def GetDCDs(self, InputBOs: list[Teamcenter.Soa.Client.Model.ModelObject], DcdFilterInfo: Mci0.Services.Strong.Pmimanagement._2014_06.PMIManagement.DCDFilterInfo) -> Mci0.Services.Strong.Pmimanagement._2014_06.PMIManagement.GetDCDsResponse:
        """    
             The operation gets all the GDELines containing Mes0MEDCDs under the selected objects.
             
             There is an option to filter out Mes0MEDCDs from the results according to occurrence
             type and object type.
             

Teamcenter Component:

             Product Manufacturing Information (PMI) Component - Product Manufacturing Information
             (PMI) solution to manage the PMI information in Teamcenter.
             
        :param InputBOs: 
                         The list of BOMLines to return the list of GDELines containing Mes0MEDCDs.
             
        :param DcdFilterInfo: 
                         Occurrence type and object type in order to filter out DCDs from the results.
             
        :return: 690020 - The DCD object doesn't have associated in context form.
        """
        ...
    def GetPMIProperties(self, Input: list[Mci0.Services.Strong.Pmimanagement._2015_10.PMIManagement.GetPMIPropertiesInputData]) -> Mci0.Services.Strong.Pmimanagement._2015_10.PMIManagement.GetPMIPropertiesResponse:
        """    
             This SOA operation takes Business Object, Search criteria and PMI Property names
             as input. It finds out if PMIs exist based on the criteria(objcet type and occurrence
             type). If PMIs exist it returns values of specified PMI properties.
             

Teamcenter Component:

             Product Manufacturing Information (PMI) Component - Product Manufacturing Information
             (PMI) solution to manage the PMI information in Teamcenter.
             
        :param Input: 
                         A collection of objects which holds business object, information about PMI filter
                         criteria and PMI properties
             
        :return: 69022 :  The PMI property "%1$" does not exist. Please contact your system administrator.
        """
        ...
    def ImportPMIs2(self, InputInfo: list[Mci0.Services.Strong.Pmimanagement._2015_10.PMIManagement.ImportPMIInputInfo2]) -> Mci0.Services.Strong.Pmimanagement._2011_12.PMIManagement.ImportPMIsResponse:
        """    
             This operation imports a list of PMIs from the Named References .xml or .JT file,
             attached to a Dataset related to an ItemRevision. New Mci0PMI objects are either
             created, updated, or mark as deleted under the target ItemRevision. A list of PMI
             IDs (accountability ID) in order to allow an import of these PMIs. In case this list
             is empty all the existing PMIs will be imported from the file.
             

Teamcenter Component:

             Product Manufacturing Information (PMI) Component - Product Manufacturing Information
             (PMI) solution to manage the PMI information in Teamcenter.
             
        :param InputInfo: 
                         The input ImportPMIInputInfo.
             
        :return: 69020:The traversing of the following Dataset Named Reference JT file has failed.
             Please check the syslog for more details.
        """
        ...

