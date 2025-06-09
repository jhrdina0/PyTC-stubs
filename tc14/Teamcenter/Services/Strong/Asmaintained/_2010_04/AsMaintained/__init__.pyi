import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class SearchInstallablePhysPartInfo:
    """
    
            Structure represents the parameters to get the installable physical part for the
            specified usage.
            
    """
    def __init__(self, ) -> None: ...
    SearchMap: System.Collections.Hashtable
    """A structure containing the search criteria."""

class SearchInstallablePhysPartInputInfo:
    """
    
            Structure represents the parameters to get the installable PhysicalPart for
            the specified usage.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    PhysBOMLine: Teamcenter.Soa.Client.Model.Strong.PhysicalBOMLine
    """The line object, for  which the PhysicalPart objects are searched to install."""
    UsageBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The line object corresponding to the selected usage."""
    SearchInfo: SearchInstallablePhysPartInfo
    """A structure containing the search criteria."""

class SearchInstallablePhysPartOutput:
    """
    
            Structure represents the output parameters of the search installable physical part
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input SearchInstallablePhysPartInputInfo element. This value is unchanged
            from the input, and can be used to identify this response element with the corresponding
            input element.
            """
    PrefInstallablePhysParts: list[Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision]
    """A list of preferred objects."""
    AltInstallablePhysParts: list[Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision]
    """A list of alternate objects."""
    SubInstallablePhysParts: list[Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision]
    """A list of substitute objects."""
    DeviatedInstallablePhysParts: list[Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision]
    """A list of deviated  objects."""

class SearchInstallablePhysPartResponse:
    """
    
            Structure represents a list of installable PhysicalPart and the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[SearchInstallablePhysPartOutput]
    """A list of installable PhysicalPart objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class SetMroWindowTopLineInfo:
    """
    Structure represents the parameters for setting the BOMWindow topline.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """The BOM window object."""
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """The Item object that would be set on the top line."""
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The revision object that would be set on the top line."""
    MroRevRule: Teamcenter.Soa.Client.Model.Strong.MroRevisionRule
    """As-maintained revision rule."""

class SetMroWindowTopLineOutput:
    """
    Structure represents the output parameters of the set window topline operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input SetMroWindowTopLineInfo element. This value is unchanged from
            the input, and can be used to identify this response element with the corresponding
            input element.
            """
    TopLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The created line object is set as the topline on the MROBOMWindow object."""

class SetMroWindowTopLineResponse:
    """
    Structure represents the set top line and the ServiceData.
    """
    def __init__(self, ) -> None: ...
    Output: list[SetMroWindowTopLineOutput]
    """A list containing the top line."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class AsMaintained:
    """
    Interface AsMaintained
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SearchInstallablePhysPart(self, Input: list[SearchInstallablePhysPartInputInfo]) -> SearchInstallablePhysPartResponse:
        """    
             This operation gets the installable PhysicalPartRevision based on the usage
             name. It will get the Preferred, Alternate, Substitute and Deviated
PhysicalPartRevision for specified usage.
             

Teamcenter Component:

             MRO As-Maintained - This component provides capabilities to generate and perform
             actions on As-Maintained structures.
             
        :param Input: 
                         The required information to search the installable Physical Parts.
             
        :return: list of partial errors.
        """
        ...
    def SetMroWindowTopLine(self, Input: list[SetMroWindowTopLineInfo]) -> SetMroWindowTopLineResponse:
        """    
             This operation will set the given object as top line for the specified BOMWindow.
             

Teamcenter Component:

             MRO As-Maintained - This component provides capabilities to generate and perform
             actions on As-Maintained structures.
             
        :param Input: 
                         The required information to set the object as top line for a <b>BOMWindow</b>.
             
        :return: list of partial errors.
        """
        ...

