import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class EffectivityInfoInput:
    """
    A structure to hold effectivity info
    """
    def __init__(self, ) -> None: ...
    EffectivityId: str
    """Effectivity ID"""
    EndItem: Teamcenter.Soa.Client.Model.Strong.Item
    """Effectivity end Item"""
    EndItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Effectivity end ItemRevision"""
    UnitRangeText: str
    """
            Effectivity unit range, a valid range of unit numbers. Always specified in the context
            of the end Item to which the units apply. It can be a discrete,noncontinuous
            range.
            """
    DateRange: list[System.DateTime]
    """
            The array of effectivity date range,a valid range of dates.
            
            -    Open range,for example,from 05 January onward.
            
            -    Closed range,for example,from 01 January to 30 April.
            
"""
    OpenEndedStatus: int
    """
            Effectivity open ended status, 0 for EFFECTIVITY_closed, 1 for EFFECTIVITY_open_ended,
            2 for FFECTIVITY_stock_out
            """
    IsProtected: bool
    """
            True to add new range to any existing ranges
            
            False to overwrite existing ranges
            
"""

class CreateOccEffectivityInput:
    """
    The information required to create occurrence effectivity for a list of BOMLine
    """
    def __init__(self, ) -> None: ...
    BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """The BOMLine objects for which to add effectivity"""
    EffectivityInfoInput: EffectivityInfoInput
    """A structure to hold effectivity info"""
    IsShared: bool
    """
            True to share effectivity among BOMLine objects
            
            False to not share effectivity among BOMLine objects
            
"""

class ReleaseStatusEffectivityInput:
    """
    The information required to create effectivity on a release status
    """
    def __init__(self, ) -> None: ...
    ReleaseStatus: Teamcenter.Soa.Client.Model.Strong.ReleaseStatus
    """The release status for which to set effectivity"""
    EffectivityInfoInput: EffectivityInfoInput
    """A structure to hold effectivity input info"""

class Effectivity:
    """
    Interface Effectivity
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOccurrenceEffectivities(self, Input: list[CreateOccEffectivityInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates a new effectivity object for each BOMLine  in the list.
             If the isShared flag is true the operation applies same effectivity for all BOMLine
             in the list.
             

Use Cases:


User can create and associate the effectivity with one occurrence
             by selecting appropriate line in the structure and choosing Tools->Effectivity->Occurrence
             Effectivity->View,Create and Edit.

User can create and associate the effectivity with several occurrences
             by selecting appropriate lines in the structure and choosing Tools->Effectivity->Occurrence
             Effectivity->Create on Multiple BOM Lines, ensure the Use shared effectivity
             check box is cleared so the effectivity is not shared between BOMLines.
             
User can create and associate the same effectivity with several occurrences
             by selecting appropriate lines in the structure and choosing Tools->Effectivity->Occurrence
             Effectivity->Create on Multiple BOM Lines, ensure the Use shared effectivity
             check box is checked so the effectivity can be shared among all occurrences.
             



Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         The information required to create occurrence effectivity for a list of <b>BOMLine</b>

        :return: 37062   Effectivity with unit range cannot have null end item.
        """
        ...
    def CreateReleaseStatusEffectivity(self, Input: list[ReleaseStatusEffectivityInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation sets new effectivity on a release status.
             

Use Cases:

             User can configure a release status by choosing Tools->Effectivity->Revision Effectivity,
             then in the Effectivity dialog, select the corresponding release status and click
             create. Define Unit/Date range to set effectivity on the release status.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         Information required to create effectivity on a release status
             
        :return: 
        """
        ...

