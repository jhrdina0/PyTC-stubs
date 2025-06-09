import System
import Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ReplaceAsBuiltPartInfo:
    """
    
            Structure represents the parameters required to replace an as-built PhysicalPart
            object.
            
    """
    def __init__(self, ) -> None: ...
    InstallationDate: System.DateTime
    """
            The Installation Time which will be set on the AsBuiltStructure relation
            object created between the parent and the replaced as-built PhysicalPartRevision
            objects.
            """
    ExtendedData: Teamcenter.Services.Strong.Asbuilt._2008_06.AsBuilt.ExtendedAttributes
    """
            A ExtendedAttributes structure which will hold any additional parameters passed by
            the consumer of this operation.
            """

class ReplaceAsBuiltPartInputInfo:
    """
    
            Structure represents the parameters required to replace an as-built PhysicalPart
            object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    SelectedLine: Teamcenter.Soa.Client.Model.Strong.AsBuiltBOMLine
    """An object, which will be replaced."""
    CopiedPhysicalPartRevision: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision
    """A object which will replace the existing PhysicalPartRevision object."""
    ReplaceAsBuiltPartInfo: ReplaceAsBuiltPartInfo
    """A replace parameters like replace date."""

class ReplaceAsBuiltPartOutput:
    """
    Structure represents the output parameters of the replaceAsBuiltPart operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input ReplaceAsBuiltPartInputInfo
            element. This value is unchanged from the input, and can be used to identify this
            response element with the corresponding input element.
            """
    ReplacerLine: Teamcenter.Soa.Client.Model.Strong.AsBuiltBOMLine
    """
            An object created for the PhysicalPartRevision object which replaced the existing
            object.
            """

class ReplaceAsBuiltPartResponse:
    """
    Structure contains the replace line and the ServiceData.
    """
    def __init__(self, ) -> None: ...
    Output: list[ReplaceAsBuiltPartOutput]
    """A list of replaced lines."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class AsBuilt:
    """
    Interface AsBuilt
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ReplaceAsBuiltPart(self, InputData: list[ReplaceAsBuiltPartInputInfo]) -> ReplaceAsBuiltPartResponse:
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

