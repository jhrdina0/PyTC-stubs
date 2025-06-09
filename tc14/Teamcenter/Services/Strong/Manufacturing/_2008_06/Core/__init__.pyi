import System
import Teamcenter.Soa.Client.Model
import typing

class FindCheckedOutsInStructureResponse:
    """
    Return structure for findCheckedOutsInStructure operation
    """
    def __init__(self, ) -> None: ...
    CheckedOutList: list[Teamcenter.Soa.Client.Model.ModelObject]
    """This is the structure contains the Tags of all the checked outs objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a common data strucuture used to return sets of Teamcenter Data Model object
            from a service request. This also holds services exceptions.
            """

class Core:
    """
    Interface Core
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindCheckedOutsInStructure(self, SearchScope: list[Teamcenter.Soa.Client.Model.ModelObject]) -> FindCheckedOutsInStructureResponse:
        """    Finds all the checked out items in the objects.
        :param SearchScope: 
                         Vector of lines, that we would like to get all the checked out objects from.
             
        :return: Structure that contains a vector of all the checked out objects in search scope,
             also holds services exceptions.
        """
        ...

