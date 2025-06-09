import System
import Teamcenter.Services.Strong.Asbasmalignment._2009_06.AsbAsmAlignment
import Teamcenter.Soa.Client

class AsbAsmAlignmentRestBindingStub(AsbAsmAlignmentService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GeneratePhysicalStructure(self, Input: list[Teamcenter.Services.Strong.Asbasmalignment._2009_06.AsbAsmAlignment.GeneratePhysicalStructInputInfo]) -> Teamcenter.Services.Strong.Asbasmalignment._2009_06.AsbAsmAlignment.GeneratePhysicalStructResponse: ...

class AsbAsmAlignmentService:
    """
    
            The MRO As-Built / As-Maintained Alignment service provides operations to generate
            As-Built structures from As-Maintained structures and vice versa.
            
            The alignment service can be used to support the following:
            

Â Â Â Â Generate an As-Maintained structure from
            an As-Built structure
            
Â Â Â Â Generate an As-Built structure from an As-Maintained
            structure
            




Library Reference:

TcSoaAsbAsmAlignmentStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> AsbAsmAlignmentService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GeneratePhysicalStructure(self, Input: list[Teamcenter.Services.Strong.Asbasmalignment._2009_06.AsbAsmAlignment.GeneratePhysicalStructInputInfo]) -> Teamcenter.Services.Strong.Asbasmalignment._2009_06.AsbAsmAlignment.GeneratePhysicalStructResponse:
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

