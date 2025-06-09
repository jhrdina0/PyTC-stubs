import System
import Teamcenter.Soa.Client.Model
import typing

class DCDFilterInfo:
    """
    DCD Filter Information.
    """
    def __init__(self, ) -> None: ...
    OccTypes: list[str]
    """A list of Occurrence type of the Mes0MEDCD."""
    ObjTypes: list[str]
    """A list of Object type of the Mes0MEDCD."""

class GetDCDsOutput:
    """
    Information about list of DCDs.
    """
    def __init__(self, ) -> None: ...
    SelectedObject: Teamcenter.Soa.Client.Model.ModelObject
    """The selected object."""
    DcdLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The list of DCDs."""

class GetDCDsResponse:
    """
    Information about DCD lines output including service data.
    """
    def __init__(self, ) -> None: ...
    GetDCDsOutput: list[GetDCDsOutput]
    """The returned GetDCDsOutput."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Including partial errors."""

class PMIManagement:
    """
    Interface PMIManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDCDs(self, InputBOs: list[Teamcenter.Soa.Client.Model.ModelObject], DcdFilterInfo: DCDFilterInfo) -> GetDCDsResponse:
        """    
             The operation gets all the GDELines containing Mes0MEDCDs under the selected objects.
             
             There is an option to filter out Mes0MEDCDs from the results according to occurrence
             type and object type.
             

Teamcenter Component:

             Product Manufacturing Information (PMI) Component - Product Manufacturing Information
             (PMI) solution to manage the PMI information in Teamcenter.
             
        :param InputBOs: 
                         The list of BOMLines to return the list of GDELines containing Mes0MEDCDs.
             
        :param DcdFilterInfo: 
                         Occurrence type and object type in order to filter out DCDs from the results.
             
        :return: 690020 - The DCD object doesn't have associated in context form.
        """
        ...

