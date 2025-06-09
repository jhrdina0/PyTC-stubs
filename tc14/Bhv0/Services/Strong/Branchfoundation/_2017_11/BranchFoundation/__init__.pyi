import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetPromoteBranchCandidatesInfo:
    """
    
GetPromoteBranchCandidatesInfo structure provides the source branch object
            and list of  version objects that are used to retrieve the parent branch objects
            for the requested source branch object.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """Identifier defined by client to track the related object."""
    SourceBranchObject: Teamcenter.Soa.Client.Model.Strong.Fnd0Branch
    """The parent Fnd0Branch object of the versionObject."""
    VersionObjects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """A list of WorkspaceObjects that will be used to find its parent branches."""

class GetPromoteBranchCandidatesOutput:
    """
    
GetPromoteBranchCandidatesOutput structure represents the parent branch objects
            related to the source branch object being requested.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """Identifier defined by client to track parent branch objects requests."""
    ParentBranches: list[Teamcenter.Soa.Client.Model.Strong.Fnd0Branch]
    """
            The list of parent Fnd0Branch objects for the requested source branch and
            version object.
            """

class GetPromoteBranchCandidatesResponse:
    """
    
GetPromoteBranchCandidatesResponse structure represents a list of parent branch
            object output lists related to the source branch object and version object being
            requested.
            
    """
    def __init__(self, ) -> None: ...
    Results: list[GetPromoteBranchCandidatesOutput]
    """The list of parent branch objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard return; includes any error information."""

class BranchFoundation:
    """
    Interface BranchFoundation
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPromoteBranchCandidates(self, Inputs: list[GetPromoteBranchCandidatesInfo]) -> GetPromoteBranchCandidatesResponse:
        """    
             This operation returns a list of Branch (Fnd0Branch) candidates for the given
             version object which could be used as target Branch (Fnd0Branch) of promotion
             action. The returned list of parent branch objects are ordered with the immediate
             parent branch first in the list followed by parents, grandparents, etc.
             

Use Cases:

             1. As a system designer I want to promote a version object (e.g. WorkspaceObject)
             to from source Branch (Fnd0Branch) to a parent Branch (Fnd0Branch).
             This operation will provide the list of available target Branch (Fnd0Branch)
             objects which can be selected for promote action.
             

Teamcenter Component:

             Branching Versioning Foundation - This component consists of the Client and Enterprise
             Tier code and constructs that support Branching Versioning Foundation related functionality
             including such things as Teamcenter application plus SOA, ITK and Preferences.
             
        :param Inputs: 
                         Structures which hold the version objects (e.g. <b>ItemRevision</b>) and source Branch
                         (<b>Fnd0Branch</b>) information to retrieve a list of promotion Branch (<b>Fnd0Branch</b>)
                         candidates.
             
        :return: 
        """
        ...

