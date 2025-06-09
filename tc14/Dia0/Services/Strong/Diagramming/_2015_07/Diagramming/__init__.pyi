import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DiagramQueryAssociatedInputInfo:
    """
    
            Structure represents the parameters required to identify the query for elements on
            a diagram.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.  It may be empty.
            """
    Elements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """
            List of elements to compare with diagram subset.  Optional, if no list is given it
            will return all elements in the subset.
            """
    Diagram: Teamcenter.Soa.Client.Model.Strong.Dia0Sheet
    """Existing diagram object to search."""

class DiagramQueryInputInfo:
    """
    
            Structure represents the parameters required to identify the query for sheet elements
            missing from a partition.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.  It may be empty.
            """
    Diagram: Teamcenter.Soa.Client.Model.Strong.Dia0Sheet
    """Name of existing diagram to search."""
    Context: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """The configuration context object to filter results by."""

class DiagramQueryNotAssociatedInputInfo:
    """
    
            Structure represents the parameters required to identify the query for partition
            elements missing from  diagram(s).
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.  It may be empty.
            """
    Diagrams: list[Teamcenter.Soa.Client.Model.Strong.Dia0Sheet]
    """
            List of of existing Diagrams to search.  Optional, if not supplied it will use all
            diagrams that assosiated with the input partition.
            """
    Partition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """The partition to check"""
    Context: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """The configuration context object to filter results by."""

class ElementsOutput:
    """
    Structure represents the output parameters of queryDiagramElementsNotAssociated operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the clientId. This can be used by the caller to indentify
            this data structure with the source input data
            """
    Elements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """List of elements found."""

class ElementsResponse:
    """
    Structures containing the missing elements along with the ServiceData is returned.
    """
    def __init__(self, ) -> None: ...
    Results: list[ElementsOutput]
    """List of elements found by input clientId"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard return; includes any error information.  An error will be reported if the
            diagram is null, or the diagram  is missing either a partition or a subset.
            """

class FindDiagramInputInfo:
    """
    
            Structure represents the parameters required to identify the query for finding associated
            diagrams.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.  It may be empty.
            """
    Element: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The object to search for, must be either Smd0LogicalElement, Mdc0OrderedConnectionGroup,
            or Mdc0ConditionalElementGroup.
            """
    Partition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """The Ptn0Partition for which the sheets must belong.  Used to narrow search."""
    Context: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """The configuration context object to filter results by."""

class FindDiagramOutput:
    """
    Structure represents the output parameters of findDiagrams operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the FindDiagramInputInfo.clientId. This can be used by
            the caller to indentify this data structure with the source input data.
            """
    Diagrams: list[Teamcenter.Soa.Client.Model.Strong.Dia0Sheet]
    """List of diagrams found."""

class FindDiagramResponse:
    """
    Structures containing the found  diagram along with the ServiceData is returned.
    """
    def __init__(self, ) -> None: ...
    Results: list[FindDiagramOutput]
    """Mapping of object to list of sheets"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard return; includes any error information.  An error will be reported if  object
            is not of type Smd0LogicalElement, Mdc0OrderedConnectionGroup, or Mdc0ConditionalElementGroup
"""

class Diagramming:
    """
    Interface Diagramming
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindDiagrams(self, Input: list[FindDiagramInputInfo]) -> FindDiagramResponse: ...
    def QueryDiagramElementsAssociatedWith(self, Input: list[DiagramQueryAssociatedInputInfo]) -> ElementsResponse: ...
    def QueryDiagramElementsNotAssociated(self, Input: list[DiagramQueryInputInfo]) -> ElementsResponse: ...
    def QueryElementsNotInDiagram(self, Input: list[DiagramQueryNotAssociatedInputInfo]) -> ElementsResponse: ...

