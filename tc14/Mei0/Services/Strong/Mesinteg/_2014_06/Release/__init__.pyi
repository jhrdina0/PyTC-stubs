import System
import Teamcenter.Soa.Client.Model
import typing

class UnitEffectivityInfo:
    """
    Unit effectivity details.
    """
    def __init__(self, ) -> None: ...
    EndItem: Teamcenter.Soa.Client.Model.ModelObject
    """The Effectivity end item."""
    EndItemRev: Teamcenter.Soa.Client.Model.ModelObject
    """The Effectivity end item revision."""
    Effectivity: str
    """The effectivity range."""

class ApplyReleaseStatusToLinesInputData:
    """
    Release status details to be applied to the lines.
    """
    def __init__(self, ) -> None: ...
    Roots: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The Mfg0BvrProcess and Mfg0BvrOperation to be traversed."""
    ReleaseStatus: str
    """The ReleaseStatus to be created from the string."""
    UnitEffectivityInfo: UnitEffectivityInfo
    """The input parameters in order to create the Effectivity object."""
    IsRecursive: bool
    """
            True to expend below the structure from the roots to the leaves, otherwise use only
            the root object.
            """

class Release:
    """
    Interface Release
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ApplyReleaseStatusToLines(self, Input: list[ApplyReleaseStatusToLinesInputData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation collects all the Mfg0BvrProcess and Mfg0BvrOperation recursively from
             the configured structure and adds a ReleaseStatus object to the non-released objects.
             

Teamcenter Component:

             MES Integration Services Component - Manufacturing execution system (MES) Integration
             Services Component supports the integration with the SIMATIC IT (SIT) and general
             MES systems.
             
        :param Input: 
                         Release status details to be applied to the lines.
             
        :return: 
        """
        ...

