import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateMROBOMWindowsInfo:
    """
    Structure represents the parameters required to create a MroBOMWindow object.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """The object, required to configure the MroBOMWindow."""

class CreateMROBOMWindowsOutput:
    """
    Structure represents the output parameters of createMroBOMWindow operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input CreateMROBOMWindowsInfo
            element. This value is unchanged from the input, and can be used to identify this
            response element with the corresponding input element.
            """
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """The created object."""

class CreateMROBOMWindowsResponse:
    """
    
Structures containing the created MroBOMWindow objects along with the
ServiceData.
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateMROBOMWindowsOutput]
    """A list of created MroBOMWindow objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class DuplicatePhysStructInfo:
    """
    
Structure represents the parameters required to create the root PhysicalPart
object.
    """
    def __init__(self, ) -> None: ...
    SerialNumber: str
    """The Serial Number, required to uniquely identify a serialized PhysicalPart."""
    LotNumber: str
    """The Lot Number,  if the PhysicalPart is of Lot type."""
    ManufacturerId: str
    """The Manufacturer's id, required to uniquely identify a serialized PhysicalPart."""
    LocationName: str
    """The location where the PhysicalPart is."""
    DispositionType: str
    """The disposition for the PhysicalPart. The default disposition is In Service."""
    InstallationDate: System.DateTime
    """Installation Date"""
    ManufacturingDate: System.DateTime
    """The date on which the PhysicalPart was manufactured."""
    UseSrlNoGen: bool
    """
            If SerialNumberGenerators are to be used to generate the Serial Numbers for
            the PhysicalPart object.
            """
    NumberOfLevels: int
    """
            An integer which indicates the depth of the design Item structure to be traversed
            for generating the as-built PhysicalPart structure.
            """

class DuplicatePhysStructInputInfo:
    """
    Structure represents the parameters required to duplicate the physical
structure.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    PhysicalBOMLine: Teamcenter.Soa.Client.Model.Strong.PhysicalBOMLine
    """The object to identify the structure to duplicate."""
    DuplicatePhysStructInfo: DuplicatePhysStructInfo
    """
            Contains the information to create the root PhysicalPart. It contains the
            information like the Serial Number, Lot Number, Manufacturer Id, Installation Date,
            Manufacturing Date, Number of Levels etc.
            """

class DuplicatePhysStructOutput:
    """
    Structure contains the duplicate PhysicalPartRevision object.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input DuplicatePhysStructInputInfo element. This value is unchanged
            from the input, and can be used to identify this response element with the corresponding
            input element.
            """
    PhysicalPartRevision: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision
    """The top level object."""

class DuplicatePhysStructResponse:
    """
    Structure contains the duplicated PhysicalPart and ServiceData.
    """
    def __init__(self, ) -> None: ...
    Output: list[DuplicatePhysStructOutput]
    """Duplicated PhysicalPart object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class RenamePhysicalPartInputInfo:
    """
    Structure represents the parameters required to rename the PhysicalPartRevision.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    PhysBOMLine: Teamcenter.Soa.Client.Model.Strong.PhysicalBOMLine
    """The object for which its revision is renamed."""
    PhysPartRev: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision
    """The object to rename."""
    NewPartNumber: str
    """Part number to modify."""
    NewSerialNumber: str
    """Serial Number to modify."""
    RenameDate: System.DateTime
    """The rename date."""

class RenamePhysicalPartOutput:
    """
    Structure represents the output parameters of rename PhysicalPart operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input RenamePhysicalPartInputInfo element. This value is unchanged from
            the input, and can be used to identify this response element with the corresponding
            input element.
            """
    NewPhysPartRev: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision
    """
            If the PhysicalPart is revised then it contains the new revision else the
            modified revision.
            """

class RenamePhysicalPartResponse:
    """
    
Structures containing the new PhysicalPartRevision object along with the
ServiceData.
    """
    def __init__(self, ) -> None: ...
    Output: list[RenamePhysicalPartOutput]
    """A list of modified objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class MROCore:
    """
    Interface MROCore
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateMROBOMWindows(self, Input: list[CreateMROBOMWindowsInfo]) -> CreateMROBOMWindowsResponse:
        """    
             This operation creates MroBOMWindow and applies the RevisionRule.
             

Teamcenter Component:

             MRO Core - MRO Core
             
        :param Input: 
                         A list of structures which hold the required information to create <b>BOMwindows</b>.
             
        :return: list of partial errors.
        """
        ...
    def DuplicatePhysicalStructure(self, InputData: list[DuplicatePhysStructInputInfo]) -> DuplicatePhysStructResponse:
        """    
             This operation duplicates the physical structure. PhysicalBOMLine is provided
             to identify the structure to duplicate and the Serial Number, Lot Number, Manufacturer
             Id, Installation Date, Manufacturing Date, Number of Levels etc. is provided
             to create the top PhysicalPart object. If the global constant ReuseAuthorizedDeviation
             is set to true then the deviation authority is reused in the duplicated structure.
             The structure below the PhysicalPart with usage as "Extra to Design"
             is not duplicated.
             

Teamcenter Component:

             MRO Core - MRO Core
             
        :param InputData: 
                         Structures which hold the information to duplicate the Physical Structure like <b>PhysicalBOMLine</b>
                         and structure <i>DuplicatePhysStructInfo</i> which holds the information <i>Serial
                         Number, Lot Number, Manufacturer Id, Installation Date, Manufacturing Date, Number
                         of Levels</i> etc.
             
        :return: 
        """
        ...
    def RenamePhysicalPart(self, InputInfo: list[RenamePhysicalPartInputInfo]) -> RenamePhysicalPartResponse:
        """    
             This operation renames the PhysicalPart by modifying the modifying either
             Serial Number or Part Number or both. If the PhysicalPart is not as-built
             PhysicalPart and the PhysicalPartRevision is released then the PhysicalPart
             is revised otherwise the latest PhysicalPartRevision is updated.
             

Teamcenter Component:

             MRO Core - MRO Core
             
        :param InputInfo: 
                         Structures which hold the required information to rename the <b>PhysicalPart</b>.
             
        :return: 
        """
        ...

