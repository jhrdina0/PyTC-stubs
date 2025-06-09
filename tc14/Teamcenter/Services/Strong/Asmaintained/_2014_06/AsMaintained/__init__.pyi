import System
import Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained
import Teamcenter.Soa.Client.Model.Strong
import typing

class AsMaintainedStructureInfo1:
    """
    
            Structure represents the parameters required to generate an as-maintained PhysicalPart
            structure for a given design Item structure.
            
    """
    def __init__(self, ) -> None: ...
    NeutralItemId: str
    """The item id of the design Item object."""
    SerialNumber: str
    """The Serial Number, required to uniquely identify a serialized PhysicalPart."""
    LotNumber: str
    """The Lot Number, if the PhysicalPart is of Lot type."""
    ManufacturerId: str
    """The Manufacturer's id, required to uniquely identify a serialized PhysicalPart."""
    NumberOfLevels: int
    """
            An integer which indicates the depth of the design Item structure to be traversed
            for generating the as-maintained PhysicalPart structure.
            """
    UseSerialNumberGenerators: bool
    """
            A Boolean to indicate if Serial Number generators are to be used to generate the
            Serial Numbers for the PhysicalParts.
            """
    StructureContext: str
    """
            Name of the Structure Context object. Structure context object is created with the
            current configuration of the MroBOMWindow and saved on the top PhysicalPart.
            """
    LocationName: str
    """The name of the PhysicalLocation object."""
    InstallationDate: System.DateTime
    """The date on which the actual PhysicalPart was installed on its parent PhysicalPart."""
    ManufacturingDate: System.DateTime
    """The date on which the PhysicalPart was manufactured."""
    DispositionType: str
    """The disposition type to be applied to the PhysicalPart objects."""
    EffectiveFromDate: System.DateTime
    """The Date from which the PhysicalPartRevision object is effective."""
    EffectiveToDate: System.DateTime
    """The Date up to which the PhysicalPartRevision object is effective."""
    Quantity: float
    """The quantity to be set on PhysicalPart."""

class GenerateAsMaintainedStructureInfo1:
    """
    
            Represents the parameters required to generate an as-maintained PhysicalPart
            structure for a given design Item structure.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    NeutralBOMLine: Teamcenter.Soa.Client.Model.Strong.NeutralBOMLine
    """The line object which holds all the properties from the PartLogisticsForm."""
    AsMaintainedStructureInfo: AsMaintainedStructureInfo1
    """
            The structure holding all the information required to generate an as-maintained PhysicalPart
            structure.
            """

class AsMaintained:
    """
    Interface AsMaintained
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GenerateAsMaintainedStructure(self, Input: list[GenerateAsMaintainedStructureInfo1]) -> Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.GenerateAsMaintainedStructureResponse:
        """    
             This operation generates an as-maintained PhysicalPart structure for a given
             design Item structure. The design structure should be first set in a BOMWindow
             object so that NeutralBOMLine objects are constructed for every Item
             in the structure. An as-maintained PhysicalPart is created for every Item
             in the structure which is marked as Traceable (This value is set on the PartLogisticsForm
             associated with the Item). All the parent/child as-maintained PhysicalPart
             objects are related to each other by AsMaintainedStructure relation. A StructureContext
             object is created with the configuration applied to the BOMWindow and saved
             on the top PhysicalPart objects.
             
             One can specify the following parameters on the PartLogisticsForm.
             

                 Traceable    If marked true, a PhysicalPart
             will be created for the Item.
             
                 Serialized    If marked true, the created
             PhysicalPart will be marked as serialized.
             
                 Lot    If marked true, the created PhysicalPart
             will be marked as lot.
             
                 Preserve Quantity    If marked true,
             only one PhysicalPart will be created irrespective of the quantity specified
             on the design Item.
             


             An as-maintained PhysicalPart structure is an imprecise structure. The parent
             and child relation, the AsMaintainedStructure relation, is between the revision
             of the parent and the item of the child.
             
             In a PhysicalPart structure, if the parts are serialized and all the required
             information like Serial Number, Lot Number(in case of Lot parts), Manufacturer's
             id are specified, then the PhysicalPart object's usage is set as Preferred.
             The parts which are not marked as Serialized or Lot, the default value is set to
             Preferred. For the serialized or lot parts, if the Serial Number or Lot Number is
             not specified, those parts are set as Missing. Once the required information is provided,
             the usage is changed to Preferred.
             
             A Business object constant defined for the Item class governs the type of
             PhysicalPart object to be created during the structure generation. By default
             the value it set to PhysicalPart.
             


Teamcenter Component:

             MRO As-Maintained - This component provides capabilities to generate and perform
             actions on As-Maintained structures.
             
        :param Input: 
                         Holds the required information to generate an as-maintained <b>PhysicalPart</b> structure
                         for a design <b>Item</b> structure.
             
        :return: 
        """
        ...

