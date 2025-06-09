import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class RebuildAsBuiltStructureInfo:
    """
    
            Structure represents the parameters required to rebuild an as-built PhysicalPart
            structure from a released as-built structure.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    RebuildDate: System.DateTime
    """
            Used as the installation time on the AsBuiltStructure relation objects in
            the new as-built structure.
            """
    SelectedBOMLine: Teamcenter.Soa.Client.Model.Strong.AsBuiltBOMLine
    """The top level object for rebuilding."""

class RebuildAsBuiltStructureOutput:
    """
    
The output data of the rebuildAsBuiltStructure
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input RebuildAsBuiltStructureInfo element. This value is unchanged from
            the input, and can be used to identify this response element with the corresponding
            input element.
            """
    NewPhysPartRev: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision
    """The newly created object."""

class RebuildAsBuiltStructureResponse:
    """
    
            Structures containing the created top level as-built PhysicalPart object and
            the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[RebuildAsBuiltStructureOutput]
    """A list of rebuild PhysicalPart objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class SearchInstallablePhysPartInfo:
    """
    
            Structure represents the parameters required to search all the installable as-built
            PhysicalPartRevision objects.
            
    """
    def __init__(self, ) -> None: ...
    SearchMap: System.Collections.Hashtable
    """A map of attribute names and value pairs (string/string)."""

class SearchInstallablePhysPartInputInfo:
    """
    
            Structure represents the parameters required to search all the installable as-built
            PhysicalPartRevision objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure
            """
    PhysBOMLine: Teamcenter.Soa.Client.Model.Strong.PhysicalBOMLine
    """The object under which the parts are going to be installed."""
    UsageBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The object corresponding to the usage specified."""
    SearchInfo: SearchInstallablePhysPartInfo
    """Search criteria"""

class SearchInstallablePhysPartOutput:
    """
    Structure represents the output parameters of the operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input SearchInstallablePhysPartInputInfo
            element. This value is unchanged from the input, and can be used to identify this
            response element with the corresponding input element.
            """
    PrefInstallablePhysParts: list[Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision]
    """A list of Preferred PhysicalPartRevision objects."""
    AltInstallablePhysParts: list[Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision]
    """A list of Alternate PhysicalPartRevision objects."""
    SubInstallablePhysParts: list[Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision]
    """A list of Substitute PhysicalPartRevision objects."""
    DeviatedInstallablePhysParts: list[Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision]
    """A list of Deviated PhysicalPartRevision objects."""

class SearchInstallablePhysPartResponse:
    """
    
            Structures containing the lists of installable PhysicalPartRevision objects
            and the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[SearchInstallablePhysPartOutput]
    """A list of PhysicalPart objects matching the search criteria."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class SetMroWindowTopLineInfo:
    """
    
            Structure represents the parameters required to set an as-built PhysicalPart
            object as a top line in a given MroBOMWindow object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """The object for which the top line is to be set."""
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """The PhysicalPart object."""
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The PhysicalPartRevision object."""

class SetMroWindowTopLineOutput:
    """
    Structure represents the output parameters of the Set Top Line operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input SetMroWindowTopLineInfo
            element. This value is unchanged from the input, and can be used to identify this
            response element with the corresponding input element.
            """
    TopLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The created object."""

class SetMroWindowTopLineResponse:
    """
    
            Structures containing the created AsBuiltBOMLine object and the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[SetMroWindowTopLineOutput]
    """Created AsBuiltBOMLine object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class AsBuilt:
    """
    Interface AsBuilt
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def RebuildAsBuiltStructure(self, Input: list[RebuildAsBuiltStructureInfo]) -> RebuildAsBuiltStructureResponse:
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
    def SearchInstallablePhysPart(self, Input: list[SearchInstallablePhysPartInputInfo]) -> SearchInstallablePhysPartResponse:
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
    def SetMroWindowTopLine(self, Input: list[SetMroWindowTopLineInfo]) -> SetMroWindowTopLineResponse:
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

