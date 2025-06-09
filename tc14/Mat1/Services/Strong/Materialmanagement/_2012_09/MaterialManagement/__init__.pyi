import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class Material:
    """
    
            Dataset that contains set of Material objects, set of UOM of material and set of
            material mass respectively, related to ItemRevision or BOMLine.
            
    """
    def __init__(self, ) -> None: ...
    MaterialRef: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Reference to MaterialRevision"""
    MaterialUOMTag: str
    """Unit of Measure"""
    MaterialMass: float
    """Mass in the UoM"""
    MaterialName: str
    """Name of Material"""

class MaterialSubstance:
    """
    
            Dataset that contains set of Material objects, set of Substance objects related to
            ItemRevision or BOMLine. Material object contains Material reference with their mass
            in UoM related to ItemRevision(s) or BOMLine(s). Substance object contains Substance
            reference with their mass in UoM related to ItemRevision(s) or BOMLine(s).
            
    """
    def __init__(self, ) -> None: ...
    Materials: list[Material]
    """std::vector<Mat1::Soa::MaterialManagement::_2012_09::MaterialManagement::Material>"""
    Substances: list[Substance]
    """Mat1::Soa::MaterialManagement::_2012_09::MaterialManagement::Substance"""

class MaterialSubstanceInfo:
    """
    
            Dataset that contains set of MaterialInfo objects, set of SubstanceInfo
            objects related to ItemRevision or BOMLine. MaterialInfo object
            contains Material reference with their mass in UoM related to ItemRevision(s)
            or BOMLine(s). SubstanceInfo object contains Substance reference
            with their mass in UoM related to ItemRevision(s) or BOMLine(s).
            
    """
    def __init__(self, ) -> None: ...
    MaterialInfos: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            Set of Mat1MaterialInfo objects that contains material reference with the
            mass  in a UoM related to ItemRevision or BOMLine objects.
            """
    SubstanceInfos: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            Set of Mat1SubstanceInfo objects that contains substance reference with the
            mass in a UoM related to the ItemRevision or BOMLine objects.
            """

class MaterialSubstanceInfoResponse:
    """
    
            Response that contains set of MaterialSubstanceInfo objects related to ItemRevision(s)
            or BOMLine(s) in sequence and the ServiceData.
            MaterialInfo objects contain Material reference with their mass in
            UoM related to each ItemRevision or BOMLine. SubstanceInfo objects
            contain Substance reference with their mass in UoM related to each ItemRevision
            or BOMLine.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Returned service data related to the MaterialSubstanceInfoResponse."""
    MaterialSubstanceInfos: list[MaterialSubstanceInfo]
    """
            Response that contains a set of Mat1lSubstanceInfo objects related to ItemRevision
            or BOMLine objects and the ServiceData.
            """
    MaterialSubstance: list[MaterialSubstance]
    """
            Response that contains set of MaterialSubstance object related to ItemRevision(s)
            or BOMLine(s) in sequence and the service data.
            """

class Substance:
    """
    
            Dataset that contains set of Substance objects, set of UOM of substance, set of minimum
            substance mass, set of maximum substance mass and set of mass in range respectively,
            related to ItemRevision or BOMLine.
            
    """
    def __init__(self, ) -> None: ...
    SubstanceRef: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """Reference to Substance"""
    SubstanceUOMTag: str
    """Unit of Measure"""
    SubstanceMinMass: float
    """Minimum Mass"""
    SubstanceMaxMass: float
    """Maximum Mass"""
    SubstanceMassInRange: bool
    """Is the mass in range?"""
    SubstanceName: str
    """Name of Substance"""
    SubstanceCASNumber: str
    """Substance CAS Number"""

class MaterialManagement:
    """
    Interface MaterialManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetMaterialSubstanceInfo(self, Objs: list[Teamcenter.Soa.Client.Model.ModelObject]) -> MaterialSubstanceInfoResponse:
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

