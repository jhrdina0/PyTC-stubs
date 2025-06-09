import System
import Teamcenter.Services.Strong.Structuremanagement._2014_12.Effectivity
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class EditOccEffectivityInput:
    """
    The information required to update occurrence effectivity for the  BOMLine
    """
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The BOMLine whose effectivity is updated"""
    EffectivityComponent: Teamcenter.Soa.Client.Model.Strong.Effectivity
    """The effectivity object to be updated"""
    EffectivityInfoInput: Teamcenter.Services.Strong.Structuremanagement._2014_12.Effectivity.EffectivityInfoInput
    """A structure to hold effectivity info"""

class EditRelStatusEffectivityInput:
    """
    The information required to update effectivity on a released status
    """
    def __init__(self, ) -> None: ...
    ReleaseStatus: Teamcenter.Soa.Client.Model.Strong.ReleaseStatus
    """The released status whose effectivity is updated"""
    EffectivityComponent: Teamcenter.Soa.Client.Model.Strong.Effectivity
    """The effectivity object to be updated"""
    EffectivityInfoInput: Teamcenter.Services.Strong.Structuremanagement._2014_12.Effectivity.EffectivityInfoInput
    """A structure to hold effectivity info"""

class RemoveOccEffectivitiesInput:
    """
    
The information required to remove effectivity objects from specified BOMLine
objects.
    """
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The BOMLine whose effectivities are removed"""
    EffectivityComponents: list[Teamcenter.Soa.Client.Model.Strong.Effectivity]
    """The effectivity objects to be removed"""

class RemoveRelStatusEffectivityInput:
    """
    The information required to remove Effectivity from a released status
    """
    def __init__(self, ) -> None: ...
    ReleaseStatus: Teamcenter.Soa.Client.Model.Strong.ReleaseStatus
    """The released status whose Effectivity is removed"""
    EffectivityComponent: Teamcenter.Soa.Client.Model.Strong.Effectivity
    """The effectivity object to be removed"""

class Effectivity:
    """
    Interface Effectivity
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def EditOccurrenceEffectivity(self, Input: list[EditOccEffectivityInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation updates effectivity object for the specified BOMLine.
             

Use Cases:

             User can configure a release status by choosing Tools->Effectivity->Revision Effectivity,
             then in the Effectivity dialog, select the corresponding release status and click
             create. Define Unit/Date range to set effectivity on the release status.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         The information required to update occurrence effectivity for the  <b>BOMLine</b>

        :return: 
        """
        ...
    def EditReleaseStatusEffectivity(self, Input: list[EditRelStatusEffectivityInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation updates effectivity object for the specified released status.
             

Use Cases:


User can edit a release status by choosing Views->Effectivity->Revision
             Effectivity, then in the Revision Effectivity dialog box, select the corresponding
             release status effectivity and click Edit. Modify Unit/Date range to update effectivity
             on the release status.
             
User can also edit release status effectivity in My Teamcenter. Double-click
             the item status and change the displayed value.
             



Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Input: 
                         The information required to update effectivity on a released status
             
        :return: 
        """
        ...
    def RemoveOccurrenceEffectivities(self, Input: list[RemoveOccEffectivitiesInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation removes effectivity objects from the specified BOMLine objects.
             

Use Cases:

             User can remove an occurrence effectivity by choosing Tools->Effectivity->Occurrence
             Effectivity, then in the Occurrence Effectivity dialog box, click Remove to clear
             all boxes. Click OK and Teamcenter removes the effectivity object from the selected
             occurrence. Any other occurrences sharing this effectivity retain their references
             to the effectivity object.
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Input: 
                         The information required to remove a list of <b>Effectivity</b> objects from specified
                         <b>BOMLine</b>

        :return: 
        """
        ...
    def RemoveReleaseStatusEffectivity(self, Input: list[RemoveRelStatusEffectivityInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation removes effectivity object from the specified released status.
             

Use Cases:

             User can remove a release status effectivity by choosing Views->Effectivity->Revision
             Effectivity, then in the Effectivity dialog, select the corresponding release status
             and click Delete.
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Input: 
                         The information required to remove <b>Effectivity</b> from a released status
             
        :return: 
        """
        ...

