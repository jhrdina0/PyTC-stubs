import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetDisciplineResponse:
    """
    
            This structure is the object returned by this operation. It holds the Discipline
            object found and ServiceData object.
            
    """
    def __init__(self, ) -> None: ...
    Discipline: Teamcenter.Soa.Client.Model.Strong.Discipline
    """The discipline object found with the given name."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The object which holds the possible error in the search of the discipline."""

class DisciplineManagement:
    """
    Interface DisciplineManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDiscipline(self, DisciplineName: str) -> GetDisciplineResponse:
        """    
             This operation gets the Discipline object with given name. If no discipline
             object is found with the given name, the returned discipline object would be null.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param DisciplineName: 
                         This parameter specifies the name of the discipline object to be found.
             
        :return: in the ServiceData.
        """
        ...

