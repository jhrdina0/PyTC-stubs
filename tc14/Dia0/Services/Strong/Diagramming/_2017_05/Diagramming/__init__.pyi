import Dia0.Services.Strong.Diagramming._2015_07.Diagramming
import System
import Teamcenter.Soa.Client.Model.Strong
import typing

class FindDiagramInputInfo2:
    """
    
            Structure represents the parameters required to identify the query for finding associated
            diagrams.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure. It may be empty.
            """
    Elements: list[Teamcenter.Soa.Client.Model.Strong.POM_application_object]
    """
            The list of objects to search for, must be either Smd0LogicalElement, Mdc0OrderedConnectionGroup,
            or Mdc0ConditionalElementGroup.
            """
    Partitions: list[Teamcenter.Soa.Client.Model.Strong.Ptn0Partition]
    """
            The list of Ptn0Partition for which the sheets must belong. Used to narrow
            search.
            """
    Context: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """The configuration context object to filter results by."""

class Diagramming:
    """
    Interface Diagramming
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindDiagrams2(self, Input: list[FindDiagramInputInfo2]) -> Dia0.Services.Strong.Diagramming._2015_07.Diagramming.FindDiagramResponse: ...

