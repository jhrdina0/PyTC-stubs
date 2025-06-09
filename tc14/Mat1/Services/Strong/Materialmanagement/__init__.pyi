import Mat1.Services.Strong.Materialmanagement._2012_09.MaterialManagement
import Mat1.Services.Strong.Materialmanagement._2021_06.MaterialManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class MaterialManagementRestBindingStub(MaterialManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetMaterialSubstanceInfo(self, Objs: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mat1.Services.Strong.Materialmanagement._2012_09.MaterialManagement.MaterialSubstanceInfoResponse: ...
    def ExportMaterialsData(self, Input: list[Mat1.Services.Strong.Materialmanagement._2021_06.MaterialManagement.ExportMaterialsDataIn]) -> Mat1.Services.Strong.Materialmanagement._2021_06.MaterialManagement.ImportExportMaterialsDataResponse: ...
    def ImportMaterialsData(self, Input: list[Mat1.Services.Strong.Materialmanagement._2021_06.MaterialManagement.ImportMaterialsDataIn]) -> Mat1.Services.Strong.Materialmanagement._2021_06.MaterialManagement.ImportExportMaterialsDataResponse: ...

class MaterialManagementService:
    """
    
            The Material Management service exposes operations that are used to query material
            and substance related information associated with a part. Substances can be defined
            as basic forms of matter that cannot be disintegrated further using some mechanical
            or physical process, e.g. iron. Substances have Chemical Abstracts Service registry
            numbers to uniquely identify them. Material is defined as matter composed of several
            substances, e.g. iron, carbon, cadmium, etc. with definite or variable compositions.
            A Teamcenter part can be made of several materials, e.g. Steel Alloy 440, Cast Iron
            2300 Series, etc. with definite masses of materials. The queries data is a set of
            Mat1MaterialInfo objects that contains the material reference with the mass
            in a unit of measure (UoM) related to ItemRevision or BOMLine objects
            and a set of Mat1SubstanceInfo objects that contain the substance reference
            with the mass in a UoM related to ItemRevision objects or BOMLine objects.
            


Library Reference:

Mat1SoaMaterialManagementStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> MaterialManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetMaterialSubstanceInfo(self, Objs: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mat1.Services.Strong.Materialmanagement._2012_09.MaterialManagement.MaterialSubstanceInfoResponse:
        """    
             Method to query material and substance related information associated with a part.
             Substances can be defined as basic form of matter which cannot be disintegrated further
             using some mechanical or physical process, e.g. iron. Substances have a Chemical
             Abstracts Service registry number to uniquely identify them. Material is defined
             as matter composed of several substances, e.g. iron, carbon, cadmium etc. with definite
             or variable compositions. A Teamcenter part can be made of several materials, e.g.
             Steel Alloy 440, Cast Iron 2300 Series, etc. The query data is a set of Mat1MaterialInfo
             objects that contain material references with their mass in a unit of measure (UoM)
             related to ItemRevision or BOMLine objects, and a set of Mat1SubstanceInfo
             objects that contain substance references with their mass in UoM related to ItemRevision
             or BOMLine objects.
             

Teamcenter Component:

             Material Management SOA Component - Component for Mat1SoaMaterialMgmt.
             
        :param Objs: 
                         References of <b>ItemRevision</b> objectss or <b>BOMLine</b> objects for which material
                         and substance information is sought.
             
        :return: objects.
        """
        ...
    def ExportMaterialsData(self, Input: list[Mat1.Services.Strong.Materialmanagement._2021_06.MaterialManagement.ExportMaterialsDataIn]) -> Mat1.Services.Strong.Materialmanagement._2021_06.MaterialManagement.ImportExportMaterialsDataResponse:
        """    
             Exports one of the following
             
             1. Instances of input Mat1MaterialRevision & its' decendent classes and
             its parameters in the provided format which belongs to same belonging Mat1MatCatalogRevision.
             One or more instances Mat1MaterialRevision or its' decendent classes is expected.
             
             2. Instances of Mat1MaterialRevision & its' decendent classes and its
             parameters in the provided format belonging to input Mat1MatCatalogRevision.
             Only one instance of Mat1MatCatalogRevision is expected in input.
             
             3. Instances of input Mat1MaterialClassification & all Mat1MaterialClassification
             objects pointing to input object. One or more instances of Mat1MaterialClassification
             class is expected.
             

             ImportExportOptions play an important role in the way Mat1MaterialRevision
             objects are exported.
             

Use Cases:

             X
             

Teamcenter Component:

             Material Management SOA Component - Component for Mat1SoaMaterialMgmt.
             
        :param Input: 
                         List of ExportMaterialsDataIn objects. Each structure contains list of <b>Mat1MaterialRevision</b>
                         objects &amp; corresponding export options. If mutiple objects are to be exported
                         in different export formats, each export format should have one ExportMaterialsDataIn
                         object.
             
        :return: is expected as input.
        """
        ...
    def ImportMaterialsData(self, Input: list[Mat1.Services.Strong.Materialmanagement._2021_06.MaterialManagement.ImportMaterialsDataIn]) -> Mat1.Services.Strong.Materialmanagement._2021_06.MaterialManagement.ImportExportMaterialsDataResponse:
        """    
             Import one of the following
             
             1. Materials and its parameters from given list of files in specified file format.
             
             2. Material classes and its heirarchy.
             

             ImportExportOptions also play an important role in determining the way Materials
             are imported.
             

Use Cases:

             x
             

Teamcenter Component:

             Material Management SOA Component - Component for Mat1SoaMaterialMgmt.
             
        :param Input: 
                         List of ImportMaterialsDataIn objects.
             
        :return: and its' decendent classes are allowed.
        """
        ...

