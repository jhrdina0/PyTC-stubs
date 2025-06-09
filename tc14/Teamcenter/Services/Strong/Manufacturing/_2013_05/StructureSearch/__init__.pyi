import System
import Teamcenter.Soa.Client.Model
import typing

class FindStudiesResponse:
    """
    The response data from the findStudies service operation.
    """
    def __init__(self, ) -> None: ...
    Results: list[FindStudiesResults]
    """The found Mfg0BvrStudy objects for each inputNodes Mfg0BvrProcess or Mfg0BvrOperation"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data"""

class FindStudiesResults:
    """
    A list of Mfg0BvrStudy objects
    """
    def __init__(self, ) -> None: ...
    ListOfStudies: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of Mfg0BvrStudy objects"""

class StructureSearch:
    """
    Interface StructureSearch
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindStudies(self, InputNodes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> FindStudiesResponse:
        """    
             This operation finds all study objects that reference a given process/operation business
             object.
             
        :param InputNodes: 
                         A list of business objects for which referencing studies should be searced (objects
                         of type Mfg0BvrProcess or Mfg0BvrOperation).
             
        :return: The Mfg0BvrStudy objects that refer to the input business objects.
        """
        ...

