import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExtendedAttributes:
    """
    
            The ExtendedAttributes structure represents the structure containing additional attributes
            that might be passed from the client
            
    """
    def __init__(self, ) -> None: ...
    ObjectType: str
    """objectType"""
    Attributes: System.Collections.Hashtable
    """attributes"""

class AsBuiltStructureInfo:
    """
    
            Structure represents the parameters required to generate an as-built PhysicalPart
            structure for a given design Item structure.
            
    """
    def __init__(self, ) -> None: ...
    NeutralItemId: str
    """The item id of the design Item object."""
    SerialNumber: str
    """The Serial Number, required to uniquely identify a serialized PhysicalPart."""
    LotNumber: str
    """The Lot Number,  if the PhysicalPart is of Lot type."""
    ManufacturerId: str
    """The Manufacturer's id, required to uniquely identify a serialized PhysicalPart."""
    StructureContext: str
    """
            Name of the StructureContext object. Structurecontext object is created
            with the current configuration of the MroBOMWindow and saved on the top PhysicalPart.
            """
    InstallationDate: System.DateTime
    """The date on which the actual PhysicalPart was installed on its parent PhysicalPart."""
    ManufacturingDate: System.DateTime
    """The date on which the PhysicalPart was manufactured."""
    UseSerialNumberGenerators: bool
    """
            If SerialNumberGenerators are to be used to generate the Serial Numbers for
            the PhysicalPart objects.
            """
    NumberOfLevels: int
    """
            An integer which indicates the depth of the design Item structure to be traversed
            for generating the as-built PhysicalPart structure.
            """
    ExtendedData: ExtendedAttributes
    """The structure, which can hold any additional properties and values."""

class GenerateAsBuiltStructInput:
    """
    
            Structure represents the parameters required to generate an as-built PhysicalPart
            structure for a given design Item structure.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    NeutralBOMLine: Teamcenter.Soa.Client.Model.Strong.NeutralBOMLine
    """The object, which holds all the properties from the PartLogisticsForm."""
    AsBuiltStructureInfo: AsBuiltStructureInfo
    """The information required to generate an as-built PhysicalPart structure."""

class GenerateAsBuiltStructureOutput:
    """
    Structure represents the output parameters of the generateAsBuiltStructure operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input GenerateAsBuiltStructInput
            element. This value is unchanged from the input, and can be used to identify this
            response element with the corresponding input element.
            """
    PhysicalPartRevision: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision
    """The top level object."""

class GenerateAsBuiltStructureResponse:
    """
    
            Structures containing the created top level PhysicalPart object and the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GenerateAsBuiltStructureOutput]
    """Created PhysicalPart object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class InstallPhysicalPartInfo:
    """
    
            Structure represents the parameters required to install an as-built PhysicalPartRevision
            under a parent.
            
    """
    def __init__(self, ) -> None: ...
    UsageName: str
    """A String which holds the name of the Usage. E.g. occurrence name."""
    InstallationDate: System.DateTime
    """The Installation Date which will be set on the AsBuiltStructure relation object."""
    Attributes: System.Collections.Hashtable
    """An AttributeNameValueMap object, used to pass additional information."""

class InstallPhysicalPartOutput:
    """
    
            Structure represents the output parameters of the install as-built PhysicalPart
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input InstallPhysicalPrtInput
            element. This value is unchanged from the input, and can be used to identify this
            response element with the corresponding input element.
            """
    Relation: Teamcenter.Soa.Client.Model.Strong.AsBuiltStructure
    """The relation object created as a result of the installation."""
    InstalledLine: Teamcenter.Soa.Client.Model.Strong.AsBuiltBOMLine
    """An object created to represent the installed PhysicalPartRevision object."""

class InstallPhysicalPartResponse:
    """
    Structure contains the relation created and the ServiceData.
    """
    def __init__(self, ) -> None: ...
    Output: list[InstallPhysicalPartOutput]
    """The Service Data."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data contains Allowed Deviation as createdObjects along with any errors."""

class InstallPhysicalPrtInput:
    """
    
            Structure represents the parameters required to install an as-built PhysicalPart
            revision under a parent.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    ParentAsBuiltBOMLineImpl: Teamcenter.Soa.Client.Model.Strong.AsBuiltBOMLine
    """The parent  object, under which the PhysicalPartRevision object will be installed."""
    ChildPhysicalPartRevisionImpl: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision
    """The child object which will be installed."""
    InstallInfo: InstallPhysicalPartInfo
    """A install information like install date."""
    UsageType: str
    """A String which specifies the Usage e.g. Extra to Design."""
    SelectedBOMLineImpl: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The object used to identify the occurrence object."""

class RemovedLineOutput:
    """
    Structure represents the output parameters of the operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input RemoveLineInput
            element. This value is unchanged from the input, and can be used to identify this
            response element with the corresponding input element.
            """
    ReplacerLine: Teamcenter.Soa.Client.Model.Strong.AsBuiltBOMLine
    """The new object created in place of the uninstalled AsBuiltBOMLine object."""

class RemoveLineInput:
    """
    
            Structure represents the parameters required to uninstall an as-built PhysicalPartRevision
            object from the structure.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    AsbuiltBOMLine: Teamcenter.Soa.Client.Model.Strong.AsBuiltBOMLine
    """The object to be removed from the structure."""

class UnInstallPhysicalPartResponse:
    """
    Structure represents a list of replacer line and the ServiceData.
    """
    def __init__(self, ) -> None: ...
    Output: list[RemovedLineOutput]
    """A list of replacer  line."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class AsBuilt:
    """
    Interface AsBuilt
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GenerateAsBuiltStructure(self, Input: list[GenerateAsBuiltStructInput]) -> GenerateAsBuiltStructureResponse:
        """    
             This operation generates an as-built PhysicalPart structure for a given design
             Item structure. The design structure should be first set in a BOMWindow
             object so that NeutralBOMLine objects are constructed for every Item
             in the structure. An as-built PhysicalPart is created for every Item
             in the structure which is marked as Traceable (This value is set on the PartLogisticsForm
             associated with the Item). All the parent/child as-built PhysicalPart
             objects are related to each other by AsBuiltStructure relation. A StructureContext
             object is created with the configuration applied to the BOMWindow and saved
             on the top PhysicalPart.
             

             One can specify the following parameters on the PartLogisticsForm.
             


Traceable                 If marked true, a PhysicalPart will
             be created for the Item.
             
Serialized                  If marked true, the created PhysicalPart
             will be marked Serialized.
             
Lot                         If marked true, the created PhysicalPart
             will be marked as Lot.
             
Preserve Quantity      If marked true, only one PhysicalPart
             will be created irrespective of the Quantity specified on the design Item.
             



             An as-built PhysicalPart structure is a precise structure. The parent and
             child relation, the AsBuiltStructure relation, is between the revisions of
             the parent and child.
             

             In a PhysicalPart structure, if the parts are serialized and all the required
             information like Serial Number, Lot Number(in case of Lot parts), Manufacturer's
             id are specified, then the PhysicalPart object's usage is set as Preferred.
             The parts which are not marked as Serialized or Lot, the default value is set to
             Preferred. For the serialized or lot parts, if the Serial or Lot Number is
             not specified, those parts are set as Missing. Once the required information
             is provided, the usage is changed to Preferred.
             

             A Business object constant defined for the Item class governs the type of PhysicalPart
             object to be created during the structure generation. By default the value it set
             to PhysicalPart.
             

Dependencies:

             createMROBOMWindows
             

Teamcenter Component:

             MRO As-Built - This component provides capabilities to generate and perform actions
             on As-Built structures.
             
        :param Input: 
                         Structures which holds the required information to generate an as-built <b>PhysicalPart</b>
                         structure for a design <b>Item</b> structure.
             
        :return: 
        """
        ...
    def InstallPhysicalPart(self, InstallPhysicalPrtInput: list[InstallPhysicalPrtInput]) -> InstallPhysicalPartResponse:
        """    
             This operation installs a PhysicalPart object under a parent object in a given
             position. In the as-built structure, the relations are precise. Hence a revision
             of the child PhysicalPart object will be installed under a revision of the
             parent PhysicalPart object. An object of AsBuiltStructure will be created
             between the two objects.
             
             Based on the specified position, the usage will be determined by the code. Following
             values are possible.
             

Preferred          If the
             design Item of the child part is a part of the configured design Item
             structure for the parent part.
             
Alternate          If the
             design Item of the child part is an Alternate of the Item configured
             in the design Item structure for the parent part.
             
Substitute          If the
             design Item of the child part is a Substitute of the Item configured
             in the design Item structure for the parent part.
             
Deviated          If the
             design Item of the child part is not a part of the Item configured in the
             design Item structure for the parent part. A Valid deviation should be already set
             up between the parent and the child parts.
             



Teamcenter Component:

             MRO As-Built - This component provides capabilities to generate and perform actions
             on As-Built structures.
             
        :param InstallPhysicalPrtInput: 
                         Structures which hold the required information to install an as-built <b>PhysicalPart</b>
                         under a parent.
             
        :return: 
        """
        ...
    def UnInstallPhysicalPart(self, RemovePhPartInput: list[RemoveLineInput]) -> UnInstallPhysicalPartResponse:
        """    
             This operation uninstalls an as-built PhysicalPartRevision object from a structure.
             When an as-built object is uninstalled from a structure, a new PhysicalPartRevision
             object is created in the structure in that position. A new AsBuiltBOMLine
             object is constructed to represent that new part. The usage of the new part is set
             to Missing as there is no actual part in that position (If the uninstalled
             part is Extra to Design, the Missing part is not created). An object of AsBuiltStructure
             relation is created between the new part and the parent part.
             

Teamcenter Component:

             MRO As-Built - This component provides capabilities to generate and perform actions
             on As-Built structures.
             
        :param RemovePhPartInput: 
                         Structures which holds the required information to un-install an as-built <b>PhysicalPartRevision</b>
                         from a structure.
             
        :return: 
        """
        ...

