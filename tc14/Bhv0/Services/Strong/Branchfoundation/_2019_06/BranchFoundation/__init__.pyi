import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetBranchCandidateInput:
    """
    
GetBranchCandidateInput structure provides the branch (Fnd0Branch)
            object and list of branch contents (WorkspaceObject) that are used to retrieve
            parent, children or sibling branch (Fnd0Branch) candidates for the requested
            branch (Fnd0Branch) object and input criteria.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """Identifier defined by client to track the related object."""
    Branch: Teamcenter.Soa.Client.Model.Strong.Fnd0Branch
    """The Fnd0Branch object to be used to retrieve candidates."""
    BranchContents: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """
            A list of WorkspaceObject objects that will be used to find the valid branch
            candidates.
            """
    InputCriteria: list[str]

class GetBranchCandidatesOutput:
    """
    
GetBranchCandidatesOutput structure represents the branch objects related
            to branch candidates being requested based on criteria.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """Identifier defined by client to track branch candidate requests."""
    BranchMap: System.Collections.Hashtable
    """
            The information (string, list of WorkspaceObject) about  branch candidates
            for given critiria.
            """

class GetBranchCandidatesResponse:
    """
    
GetBranchCandidatesResponse structure represents a list of branch candidates
            output lists related to the branch object and version object being requested.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard return; includes any error information."""
    BranchCandidates: list[GetBranchCandidatesOutput]
    """A list of branch candidates."""

class BranchFoundation:
    """
    Interface BranchFoundation
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetBranchCandidatesInfo(self, Inputs: list[GetBranchCandidateInput]) -> GetBranchCandidatesResponse: ...

