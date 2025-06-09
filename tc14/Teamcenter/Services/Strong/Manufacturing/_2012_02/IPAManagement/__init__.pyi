import System
import Teamcenter.Soa.Client.Model
import typing

class DeleteFilteredIPAInputInfo:
    """
    Contains the information about deleting filtered IPAs.
    """
    def __init__(self, ) -> None: ...
    Process: Teamcenter.Soa.Client.Model.ModelObject
    """The business object of the process from which filtered IPA needs to be deleted."""
    IsRecursive: bool
    """
            Indicates whether all the filtered IPAs in the hierachy of the process should be
            deleted or just one filtered IPA directly under the process should be deleted.
            """

class GetFilteredIPATypeResponse:
    """
    resopnse for getFilteredIPAType SOA
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serive data"""
    Flat: list[Teamcenter.Soa.Client.Model.ModelObject]
    """a vector of processes that their process structure already contain a flat FIPA."""
    Nested: list[Teamcenter.Soa.Client.Model.ModelObject]
    """a vector of processes that their process structure already contains a nested FIPA"""
    Unset: list[Teamcenter.Soa.Client.Model.ModelObject]
    """processes that their process structure doesn't contain any FIPA yet."""

class IPAManagement:
    """
    Interface IPAManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def DeleteFilteredIPA(self, Input: list[DeleteFilteredIPAInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This API will delete the filtered IPA(s) under the process depending on the boolean
             member "isRecursive" of the input structure. If " isRecursive" is true, then all
             the filtered IPAs in the hierarchy of the member "process" will be deleted. Else
             just one filtered IPA directly under the process will be deleted.
             
        :param Input: 
                         Contains the information about deleting filtered IPAs.
             
        :return: the standard serviceData that contains errors\notes from executing the deletion.
        """
        ...
    def GetFilteredIPAType(self, Processes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetFilteredIPATypeResponse:
        """    
             For each process, return the type of the FIPA used for this process structure.  For
             processes from the same process structure, the answer is the same. Therefore, from
             perforemence point of view, it is better to pass the process context (topline) as
             an input, instead of sending several processes from the same structure.
             
        :param Processes: 
                         a vector of processes.
             
        :return: For each process, return the type of the FIPA used for this process structure (can
             be either flat or nested). If there is no FIPA for this process structure, return
             unset.
        """
        ...

