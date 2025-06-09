import System
import Teamcenter.Soa.Client.Model
import typing

class FindNodeInContextInputInfo:
    """
    Input struct for the find node in context service
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """Client ID"""
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """The topline that defines the search scope."""
    Nodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The nodes to search."""
    ByIdOnly: bool
    """If true all abs occs with the same Id will be search for, if no exact apn is matched."""
    AllContexts: bool
    """
            If true then all contexts will be searched otherwise only the current context will
            be searched if no current context specified at the time then the context of the topline
            is used.
            """
    InContextLine: Teamcenter.Soa.Client.Model.ModelObject
    """A more specific scope to searh in."""

class FindNodeInContextResponse:
    """
    The Response struct.
    """
    def __init__(self, ) -> None: ...
    ResultInfo: list[FoundNodesInfo]
    """Infornation retrieves for each input struct that we looked for."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data."""

class FoundNodesInfo:
    """
    A struct that hold all the results on a single search parallel to the one input struct.
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """Client ID"""
    ResultNodes: list[NodeInfo]
    """In each search we look into a vector of nodes to search."""

class GetAffectedPropertiesArg:
    """
    
            This structure provides the input parameters for the getAffectedProperties operation.
            It describes the property changes applied to a process or operation structure for
            which the affected runtime properties are inquired.
            
    """
    def __init__(self, ) -> None: ...
    RootNode: Teamcenter.Soa.Client.Model.ModelObject
    """he root node of the process or operation structure that is inspected."""
    ChangedNodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The list of process or operation nodes that have been changed."""
    ChangedProperties: list[str]
    """The name of the properties that have been changed."""

class NodeInfo:
    """
    The struct that holds the result for each node in the input.
    """
    def __init__(self, ) -> None: ...
    FoundNodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The found nodes we find."""
    OriginalNode: Teamcenter.Soa.Client.Model.ModelObject
    """The original input node."""

class Core:
    """
    Interface Core
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindNodeInContext(self, Input: list[FindNodeInContextInputInfo]) -> FindNodeInContextResponse:
        """    Finding parallel line in a given window of a given line.
        :param Input: 
                         Input struct.
             
        :return: The found lines.
        """
        ...
    def GetAffectedProperties(self, Arguments: list[GetAffectedPropertiesArg], RequestedProperties: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Returns the runtime properties of dependent nodes which are affected when the duration
             of one or more nodes has been changed in a process or operation structure.
             
        :param Arguments: 
                         A list of GetAffectedPropertiesChanges structures that describe the changes that
                         have been made to a process or operation structure.
             
        :param RequestedProperties: 
                         The names of the properties that are to be retrieved. In the first version only the
                         properties that are processed by the Gantt application are accepted (Mfg0calc_duration,
                         Mfg0calc_start_time, Mfg0calc_dur_start_time).
             
        :return: A ServiceData structure that contains the computed property values in the DataObject
             member. The structure also informs about errors that occurred during the course of
             the operation.
        """
        ...

