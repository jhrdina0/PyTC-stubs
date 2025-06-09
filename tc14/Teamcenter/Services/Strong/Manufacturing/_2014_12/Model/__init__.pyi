import System
import Teamcenter.Soa.Client.Model
import typing

class ConsistencyData:
    """
    Structure containing information related to cycles.
    """
    def __init__(self, ) -> None: ...
    IsConsistent: bool
    """If true, no cycles are found under the given scope."""
    Cycles: list[CycleData]
    """The list of CycleData. Each element in the list contains data about a single cycle."""

class CycleData:
    """
    Structure containing information related to a specefic cycle identified.
    """
    def __init__(self, ) -> None: ...
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The list of operations/processes that participate in a cycle that. The list contains
            business objects of type Mfg0BvrOperation and Mfg0BvrProcess.
            """
    Flows: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The list of scope flows which participates in the cycle. These objects are of type
            Mfg0BvrScopeFlow.
            """

class FileTicket:
    """
    Structure containing information related to file ticket.
    """
    def __init__(self, ) -> None: ...
    Ticket: str
    """The FMS file ticket."""
    FileName: str
    """The original file name."""

class ValidateScopeFlowsConsistencyResponse:
    """
    Response structure for validateScopeFlowsConsistency service.
    """
    def __init__(self, ) -> None: ...
    Data: list[ConsistencyData]
    """
            A list of ConsistencyData. Each element in the list contains indication whether the
            data is consistent and information about the in-cosistencies (cycles), if found.
            """
    FileTicket: FileTicket
    """An FMS file ticket. The file contains report about the cycles found by the algorithm."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data."""

class Model:
    """
    Interface Model
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ValidateScopeFlowsConsistency(self, RootLines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> ValidateScopeFlowsConsistencyResponse:
        """    
             This operation will be used to identify scope flows created under the given input
             line are acyclic or not. This operation recieves a list of ImanItemBOPLine
             as an input.  (The type of the BOP line objects can be either Mfg0BvrProcess
             or Mfg0BvrOperation). For each input scope, the operation checks whether the
             scope-flows (defined in this scope), create a cycle of processes or operations.
             

             If a cycle is indentified during this operation, the relevant information for the
             cycle is returned in the response.
             


Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param RootLines: 
                         List of business objects representing BOP line objects (the type of the bop line
                         objects can be either<b> Mfg0BvrProcess</b> or <b>Mfg0BvrOperation</b>)
             
        :return: 
        """
        ...

