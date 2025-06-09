import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AskChildPathBOMLinesInfo:
    """
    
            A set of input information for a single product structure including the associated
            child paths to be evaluated by this operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier used to relate partial errors associated with an instance of this information."""
    ParentBomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            The BOM line parent of the first PS Occurrence Thread UID specified by each of the
            paths.
            """
    UseAsStable: bool
    """
            Indicates that the child paths are specified by "stable" rather than "real" PS Occurrence
            Thread UIDs.
            """
    ChildPaths: list[AskChildPathBOMLinesPath]
    """One or more PS Occurrence Thread child paths."""

class AskChildPathBOMLinesPath:
    """
    
            One or more PS Occurrence Threads defining an input child path within a given product
            structure from a parent to a child.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier used to relate partial errors associated with an instance of this information."""
    ChildPath: list[str]
    """
            An ordered list of PS Occurrence Thread UIDs that specify a path from a parent Teamcenter::BOMLineImpl
            through the product structure to the child.
            """

class AskChildPathBOMLinesResponse:
    """
    Defines the response from the askPSOccThreadChildBOMLines operation.
    """
    def __init__(self, ) -> None: ...
    Output: System.Collections.Hashtable
    """A map of input PS Occurrence Thread UIDs to BOMLines."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The SOA framework object containing plain objects, and error information."""

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AskChildPathBOMLines(self, Input: list[AskChildPathBOMLinesInfo]) -> AskChildPathBOMLinesResponse:
        """    
             Given one or more sets of product structure information containing child paths specified
             by PS Occurrence Thread chains, this method returns the corresponding BOM Lines.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Input: 
                         Specifies sets of product structure information each containing parent BOM line,
                         based on a BOM Window opened by the client, and one or more child paths specified
                         as an ordered set of PS Occurrence Thread UIDs. BOM configuration is managed by the
                         BOM Window. Input client IDs must be unique for all input.
             
        :return: map of input PS Occurrence Thread UIDs, specified as child paths in the input, to
             the corresponding BOMLines. BOMLine objects are returned as Service Data plain objects
             to inflate properties. Partial failures can result for each child path or product
             structure being evaluated and can be associated with the input by the input client
             ID.
        """
        ...

