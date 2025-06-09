import System
import Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt
import Teamcenter.Soa.Client.Model.Strong
import typing

class AsBuiltStructureInfo1:
    """
    
            Structure represents the parameters required to generate an As-Built PhysicalPart
            structure for a given design Item structure
            
    """
    def __init__(self, ) -> None: ...
    NeutralItemId: str
    """The item id of the design Item object."""
    SerialNumber: str
    """The Serial Number, required to uniquely identify a serialized PhysicalPart"""
    LotNumber: str
    """The Lot Number,  if the PhysicalPart is of Lot type."""
    ManufacturerId: str
    """The Manufacturer's id, required to uniquely identify a serialized PhysicalPart"""
    StructureContext: str
    """
            Name of the StructureContext object. Structure context object is created with
            the current configuration of the MroBOMWindow and saved on the top PhysicalPart
"""
    InstallationDate: System.DateTime
    """The date on which the actual Physical Part was installed on its parent Physical Part."""
    ManufacturingDate: System.DateTime
    """The date on which the Physical Part was manufactured."""
    UseSerialNumberGenerators: bool
    """
            A Boolean to indicate if Serial Number generators are to be used to generate the
            Serial Numbers for the Physical Parts.
            """
    NumberOfLevels: int
    """
            An integer which indicates the depth of the design Item structure to be traversed
            for generating the AsBuilt Physical Part structure.
            """
    ExtendedData: Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt.ExtendedAttributes
    """The ExtendedAttributes structure, which can hold any additional properties and values."""
    Quantity: float
    """
            The quantity to set on PhysicalPart.
            
            For the serialized parts the quantity will not be editable as the serial number provided
            is for a physical part.  (E.g. Engine is Serialized part. Serial number is for a
            single engine.)
            

If the top part is Lot part then only integer value (Lot usage and
            size are integer) for quantity is allowed and the specified quantity should be deducted
            from the specified Lot.
            
Non-serialized and non-lot physical part can have quantity defined
            as double.
            
For unit of measure each, the quantity should be Integer.
            

"""

class GenerateAsBuiltStructInput1:
    """
    
            GenerateAsBuiltStructureInput1 structure represents the parameters required to generate
            an As-Built PhysicalPart structure for a given design Item structure.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    NeutralBOMLine: Teamcenter.Soa.Client.Model.Strong.NeutralBOMLine
    """The NeutralBOMLine object, which holds all the properties from the PartLogisticsForm."""
    AsBuiltStructureInfo: AsBuiltStructureInfo1
    """The information required to generate an As-Built PhysicalPart structure."""

class AsBuilt:
    """
    Interface AsBuilt
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GenerateAsBuiltStructure(self, Input: list[GenerateAsBuiltStructInput1]) -> Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt.GenerateAsBuiltStructureResponse:
        """    
             This operation generates an As-Built Physical Part structure for a given design Item
             structure. The design structure should be first set in a BOMWindow object so that
             NeutralBOMLine objects are constructed for every Item in the structure. An As-Built
             Physical Part is created for every Item in the structure which is marked as Traceable
             (This value is set on the PartLogisticsForm associated with the Item). All the parent/child
             As-Built Physical Part objects are related to each other by AsBuiltStructure relation.
             A Structure context object is created with the configuration applied to the BOMWindow
             and saved on the top Physical Part.
             

             One can specify the following parameters on the PartLogisticsForm.
             

Traceable  If marked true, a Physical Part will be created for the
             Item.
             
Serialized   If marked true, the created Physical Part will be marked
             as Serialized.
             
Lot  If marked true, the created Physical Part will be marked as
             Lot.
             
Preserve Quantity  If marked true, only one Physical Part will be
             created irrespective of the Quantity specified on the design Item.
             



             An As-Built physical part structure is a precise structure. The parent and child
             relation, the AsBuiltStructure relation, is between the revisions of the parent and
             child.
             

             In a PhysicalPart structure, if the parts are serialized and all the required
             information like Serial Number, Lot Number(in case of Lot parts), Manufacturer's
             id are specified, then the PhysicalPart object's usage is set as Preferred.
             The parts which are not marked as Serialized or Lot, the default value is set to
             Preferred. For the serialized or lot parts, if the Serial or Lot Number is not specified,
             those parts are set as Missing. Once the required information is provided, the usage
             is changed to Preferred.
             

             A Business object constant defined for the Item class governs the type of PhysicalPart
             object to be created during the structure generation. By default the value it set
             to PhysicalPart.
             

Use Cases:

             You can generate an As-Built PhysicalPart structure for a design Item
             structure using the generateAsBuiltStructure operation. For every Traceable Item
             in the structure, an As-Built PhysicalPart object will be created.
             

Teamcenter Component:

             MRO As-Built - This component provides capabilities to generate and perform actions
             on As-Built structures.
             
        :param Input: 
                         A list of GenerateAsBuiltStructInput1 structures which holds the required information
                         to generate an AsBuilt Physical Part structure for a design <b>Item</b> structure.
             
        :return: 
        """
        ...

