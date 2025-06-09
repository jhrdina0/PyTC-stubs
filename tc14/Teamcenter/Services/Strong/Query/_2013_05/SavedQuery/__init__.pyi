import Teamcenter.Soa.Client.Model
import typing

class SavedQueryProperties:
    """
    Contains properties of the saved query to be created.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify returned partial
            errors associated with this input structure.
            """
    QueryName: str
    """Name of the saved query to be created."""
    QueryDesc: str
    """Description of the saved query to be created, may be an empty string."""
    QueryClass: str
    """
            The storage class name of the business object type this query will find object instances
            of.
            """
    QueryClauses: str
    """
            Query clauses of the saved query to be created. To make sure the query clauses is
            in correct formate, please use Export button in Query Builder to export the saved
            query into a XML file, pick up the string value of QueryClause element in the XML,
            replace all " with " to get the final string, the final query clauses string should
            be the same as seen in View Properties dialog.
            """

class SavedQuery:
    """
    Interface SavedQuery
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateSavedQueries(self, Inputs: list[SavedQueryProperties]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    Creates a list of saved queries based on the input properties structure.
        :param Inputs: 
                         A saved query is created for each <font face="courier" height="10">SavedQueryProperties</font>
                         in the list.
             
        :return: 
        """
        ...

