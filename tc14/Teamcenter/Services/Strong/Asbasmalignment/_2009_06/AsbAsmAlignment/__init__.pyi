import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GeneratePhysicalStructInfo:
    """
    
            The parameters required to generate an as-maintained structure for a given as-built
            structure and vice versa.
            
    """
    def __init__(self, ) -> None: ...
    PhysicalLocationName: str
    """The name of the PhysicalLocation object."""
    DispositionType: str
    """
            The disposition value to be assigned to newly generated PhysicalPart object.
            User can define Disposition types to be assigned to the objects, for instance, In-Service.
"""
    NumberOfLevels: int
    """
            The number of levels in the as-built or as-maintained structure to be traversed while
            generating the target structure. All levels will be traversed if the value is set
            to -1.
            """
    GenerateAsBuilt: bool
    """If true an as-built structure will  be generated from the as-maintained structure."""
    RebuildDate: System.DateTime
    """
            Used as the installation time on the AsBuiltStructure or AsMaintainedStructure
            relation objects.
            """

class GeneratePhysicalStructInputInfo:
    """
    
            The parameters required to generate an as-maintained structure for a given as-built
            structure and vice versa.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input GeneratePhysicalStructInputInfo element. This value is unchanged
            from the input, and can be used to identify this response element with the corresponding
            input element.
            """
    PhysPartRev: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision
    """The PhysicalPartRevision object from the source structure."""
    GeneratePhysicalStructInfo: GeneratePhysicalStructInfo
    """The structure containing parameters required to generate a PhysicalPart structure."""

class GeneratePhysicalStructOutput:
    """
    Structure represents the output parameters of the generateAsMaintainedStructure operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the output GeneratePhysicalStructOutput element. This value is unchanged
            from the input, and can be used to identify this response element with the corresponding
            input element.
            """
    NewPhysPartRev: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision
    """
            The newly created top level PhysicalPartRevision object, either as-built or
            as-maintained depending on the selection.
            """

class GeneratePhysicalStructResponse:
    """
    
            Structures containing the newly created top level PhysicalPartRevision object
            and the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GeneratePhysicalStructOutput]
    """A newly created top level PhysicalPartRevision object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class AsbAsmAlignment:
    """
    Interface AsbAsmAlignment
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GeneratePhysicalStructure(self, Input: list[GeneratePhysicalStructInputInfo]) -> GeneratePhysicalStructResponse:
        """    
             This operation generates an as-maintained structure from an as-built structure. It
             can also generate an as-built structure from an as-maintained structure. The target
             structure will be released by applying the Status value specified for PhysicalPart
             in BMIDE.
             

Teamcenter Component:

             MRO As-Built/MRO As-Maintained Alignment - This component provides capabilities to
             generate As-Built structures from As-Maintained structures and vice versa.
             
        :param Input: 
                         Input
             
        :return: 
        """
        ...

