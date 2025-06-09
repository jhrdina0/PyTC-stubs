import System
import Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt
import Teamcenter.Services.Strong.Asbuilt._2009_06.AsBuilt
import Teamcenter.Services.Strong.Asbuilt._2010_04.AsBuilt
import Teamcenter.Services.Strong.Asbuilt._2014_06.AsBuilt
import Teamcenter.Soa.Client
import typing

class AsBuiltRestBindingStub(AsBuiltService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    @typing.overload
    def GenerateAsBuiltStructure(self, Input: list[Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt.GenerateAsBuiltStructInput]) -> Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt.GenerateAsBuiltStructureResponse: ...
    @typing.overload
    def GenerateAsBuiltStructure(self, Input: list[Teamcenter.Services.Strong.Asbuilt._2014_06.AsBuilt.GenerateAsBuiltStructInput1]) -> Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt.GenerateAsBuiltStructureResponse: ...
    def InstallPhysicalPart(self, InstallPhysicalPrtInput: list[Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt.InstallPhysicalPrtInput]) -> Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt.InstallPhysicalPartResponse: ...
    def UnInstallPhysicalPart(self, RemovePhPartInput: list[Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt.RemoveLineInput]) -> Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt.UnInstallPhysicalPartResponse: ...
    def ReplaceAsBuiltPart(self, InputData: list[Teamcenter.Services.Strong.Asbuilt._2009_06.AsBuilt.ReplaceAsBuiltPartInputInfo]) -> Teamcenter.Services.Strong.Asbuilt._2009_06.AsBuilt.ReplaceAsBuiltPartResponse: ...
    def RebuildAsBuiltStructure(self, Input: list[Teamcenter.Services.Strong.Asbuilt._2010_04.AsBuilt.RebuildAsBuiltStructureInfo]) -> Teamcenter.Services.Strong.Asbuilt._2010_04.AsBuilt.RebuildAsBuiltStructureResponse: ...
    def SearchInstallablePhysPart(self, Input: list[Teamcenter.Services.Strong.Asbuilt._2010_04.AsBuilt.SearchInstallablePhysPartInputInfo]) -> Teamcenter.Services.Strong.Asbuilt._2010_04.AsBuilt.SearchInstallablePhysPartResponse: ...
    def SetMroWindowTopLine(self, Input: list[Teamcenter.Services.Strong.Asbuilt._2010_04.AsBuilt.SetMroWindowTopLineInfo]) -> Teamcenter.Services.Strong.Asbuilt._2010_04.AsBuilt.SetMroWindowTopLineResponse: ...

class AsBuiltService:
    """
    
            The AsBuilt service provides operations to
            manage as-built physical part structures. As-Built physical part structures can be
            generated for Item objects whose type has the value of business object constant
            IsMRONeutralType set to true in BMIDE.
            
            The AsBuilt service can perform the following:
            

Generate an as-built structure
            
Install as-built parts in the structure
            
Uninstall as-built parts from the structure
            
Replace as-built parts in the structure
            
Rebuilt an existing as-built structure
            
Get all open positions in an as-built structure in which parts can
            be installed
            
Create BOM windows for as-built parts
            
Search for all installable as-built parts in the system which can
            be installed in a given position in an as-built structure
            
Perform BOM comparison of two as-built structures
            
Perform accountability check on two as-built structures
            
Performa BOM comparison of an as-built and a design item structure
            




Library Reference:

TcSoaAsBuiltStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> AsBuiltService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    @typing.overload
    def GenerateAsBuiltStructure(self, Input: list[Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt.GenerateAsBuiltStructInput]) -> Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt.GenerateAsBuiltStructureResponse: ...
    @typing.overload
    def GenerateAsBuiltStructure(self, Input: list[Teamcenter.Services.Strong.Asbuilt._2014_06.AsBuilt.GenerateAsBuiltStructInput1]) -> Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt.GenerateAsBuiltStructureResponse: ...
    def InstallPhysicalPart(self, InstallPhysicalPrtInput: list[Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt.InstallPhysicalPrtInput]) -> Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt.InstallPhysicalPartResponse:
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
    def UnInstallPhysicalPart(self, RemovePhPartInput: list[Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt.RemoveLineInput]) -> Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt.UnInstallPhysicalPartResponse:
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
    def ReplaceAsBuiltPart(self, InputData: list[Teamcenter.Services.Strong.Asbuilt._2009_06.AsBuilt.ReplaceAsBuiltPartInputInfo]) -> Teamcenter.Services.Strong.Asbuilt._2009_06.AsBuilt.ReplaceAsBuiltPartResponse:
        """    
             This operation replaces an as-built PhysicalPartRevision in a structure with
             a given as-built PhysicalPartRevision object.  The existing as-built PhysicalPartRevision
             object will be removed from the structure and the new object will be installed in
             that position. A new AsBuiltStructure relation will be created between the
             parent and the new PhysicalPartRevision objects. The Installation Time
             specified will be set as the Installation Time on the relation object.
             

Dependencies:

             installPhysicalPart
             

Teamcenter Component:

             MRO As-Built - This component provides capabilities to generate and perform actions
             on As-Built structures.
             
        :param InputData: 
                         ReplaceAsBuiltPartInputInfo structure object which contains the required information
                         for replace action
             
        :return: 
        """
        ...
    def RebuildAsBuiltStructure(self, Input: list[Teamcenter.Services.Strong.Asbuilt._2010_04.AsBuilt.RebuildAsBuiltStructureInfo]) -> Teamcenter.Services.Strong.Asbuilt._2010_04.AsBuilt.RebuildAsBuiltStructureResponse:
        """    
             This operation generates a new as-built PhysicalPart structure based on an
             existing as-built structure. This activity is known as Rebuilding. The new
             PhysicalPart objects created are linked to the design Item objects
             of the parts in the existing as-built structure, with PhysicalRealization
             relation object. New AsBuiltStructure relation objects are created between
             the PhysicalPartRevision objects in the new structure.
             

Teamcenter Component:

             MRO As-Built - This component provides capabilities to generate and perform actions
             on As-Built structures.
             
        :param Input: 
                         A list of <b>AsBuiltBOMLine</b> objects to rebuild an AsBuilt structure.
             
        :return: 
        """
        ...
    def SearchInstallablePhysPart(self, Input: list[Teamcenter.Services.Strong.Asbuilt._2010_04.AsBuilt.SearchInstallablePhysPartInputInfo]) -> Teamcenter.Services.Strong.Asbuilt._2010_04.AsBuilt.SearchInstallablePhysPartResponse:
        """    
             This operation returns all the PhysicalPartRevision objects which can be installed
             in a given position in an as-built structure.  Following are the lists of installable
             objects returned based on the position selected.
             

Preferred Parts    All the preferred revision
             objects
             
Alternate Parts     All the revision objects
             realized from the Alternate parts of the design Item object
             
Substitute Parts     All the revision objects
             realized from the Substitute parts of the design Item object
             
Deviated Parts     All the revision objects which
             have allowed deviations set up
             



Use Cases:

             MOIN
             

Teamcenter Component:

             MRO As-Built - This component provides capabilities to generate and perform actions
             on As-Built structures.
             
        :param Input: 
                         Structures which hold the required information to query all the installable as-built
                         <b>PhysicalPartRevision</b> objects.
             
        :return: list of partial
             errors.
        """
        ...
    def SetMroWindowTopLine(self, Input: list[Teamcenter.Services.Strong.Asbuilt._2010_04.AsBuilt.SetMroWindowTopLineInfo]) -> Teamcenter.Services.Strong.Asbuilt._2010_04.AsBuilt.SetMroWindowTopLineResponse:
        """    
             This operation sets a given PhysicalPart object as the top line in the given
             MroBOMWindow object by constructing an object of AsBuiltBOMLine. If
             the object is an as-built PhysicalPartRevision, then it is directly set as
             the top line. If the object is a PhysicalPart, then the latest as-built
             revision of the object is queried and set as the top line. It is possible for
             a PhysicalPart object to have as-built revisions and non as-built
             revisions.
             

Dependencies:

             createMROBOMWindows
             

Teamcenter Component:

             MRO As-Built - This component provides capabilities to generate and perform actions
             on As-Built structures.
             
        :param Input: 
                         Structure which holds the required information to set an as-built <b>PhysicalPart</b>
                         or <b>PhysicalPartRevision</b> as the top line in a <b>MroBOMWindow</b> object.
             
        :return: 
        """
        ...

