import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DisplayUtilizationInfo:
    """
    
Structure represents the parameters required to get the utilization data for the
given PhysicalPart.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    PhysicalPart: Teamcenter.Soa.Client.Model.Strong.PhysicalPart
    """The object for which the utilization data is to be retrieved."""
    TillDate: System.DateTime
    """The date till the utilization is retrieved for Utilization."""

class DisplayUtilizationOutput:
    """
    Structure represents the list of the utilization data for the given
PhysicalPart.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input DisplayUtilizationInfo element. This value is unchanged from the
            input, and can be used to identify this response element with the corresponding input
            element.
            """
    Output: list[Teamcenter.Soa.Client.Model.Strong.Utilization]
    """The list of Utilization objects."""

class DisplayUtilizationResponse:
    """
    
Structure represents a list of Utilization objects along with the ServiceData.
    """
    def __init__(self, ) -> None: ...
    Output: list[DisplayUtilizationOutput]
    """A list Utilization objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class MROCore:
    """
    Interface MROCore
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def DisplayUtilization(self, InputInfo: list[DisplayUtilizationInfo]) -> DisplayUtilizationResponse:
        """    
             This operation gets the utilization data till the date specified for a PhysicalPart.
             The data is represented by Utilization object. Utilization object contains
             the information like Characteristic Name, Characteristic Unit, Time Since New, Last
             Recorded Value etc.
             

Teamcenter Component:

             MRO Core - MRO Core
             
        :param InputInfo: 
                         The information to capture the utilization data for a <b>PhysicalPart</b>.
             
        :return: list
             of partial errors.
        """
        ...

