import Bhv0.Services.Strong.Branchfoundation._2017_05.BranchFoundation
import Bhv0.Services.Strong.Branchfoundation._2017_11.BranchFoundation
import Bhv0.Services.Strong.Branchfoundation._2019_06.BranchFoundation
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class BranchFoundationRestBindingStub(BranchFoundationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def AddContentToBranch(self, Inputs: list[Bhv0.Services.Strong.Branchfoundation._2017_05.BranchFoundation.AddContentToBranchInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateBranches(self, Inputs: list[Bhv0.Services.Strong.Branchfoundation._2017_05.BranchFoundation.BranchCreateInput]) -> Bhv0.Services.Strong.Branchfoundation._2017_05.BranchFoundation.CreateBranchResponse: ...
    def GetPromoteBranchCandidates(self, Inputs: list[Bhv0.Services.Strong.Branchfoundation._2017_11.BranchFoundation.GetPromoteBranchCandidatesInfo]) -> Bhv0.Services.Strong.Branchfoundation._2017_11.BranchFoundation.GetPromoteBranchCandidatesResponse: ...
    def GetBranchCandidatesInfo(self, Inputs: list[Bhv0.Services.Strong.Branchfoundation._2019_06.BranchFoundation.GetBranchCandidateInput]) -> Bhv0.Services.Strong.Branchfoundation._2019_06.BranchFoundation.GetBranchCandidatesResponse: ...

class BranchFoundationService:
    """
    
            APIS for Branch Foundation
            


Library Reference:

Bhv0SoaBranchFoundationStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> BranchFoundationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def AddContentToBranch(self, Inputs: list[Bhv0.Services.Strong.Branchfoundation._2017_05.BranchFoundation.AddContentToBranchInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateBranches(self, Inputs: list[Bhv0.Services.Strong.Branchfoundation._2017_05.BranchFoundation.BranchCreateInput]) -> Bhv0.Services.Strong.Branchfoundation._2017_05.BranchFoundation.CreateBranchResponse:
        """    
             This operation publishes a set of revisable objects (e.g. ItemRevision) to
             a branch (Fnd0Branch) for versioning management in a branch.
             

             The Trunk (Fnd0Branch) is a special branch which is at the top level, and
             can specify rules such that there are no working revisions in a trunk. System could
             create a trunk or a branch based on input configuration.
             

Use Cases:


As a system designer, I want to publish a new revisable object or
             a set of revisable objects to Teamcenter branch object from a client application.
             System designer provides information like branch name, branch comment, and optional
             parent branch information to create branches; if there is no parent branch information
             provided in the input, system will create automatically the trunk (Fnd0Branch)
             and it will link the versioning object or the set of versioning objects to the trunk,
             and then lock the versioning objects if needed.
             
As a system designer, I want to branch out an existing versioning
             object for modification. System designer provides information like branch name, branch
             out comment; system will automatically create a branch (Fnd0Branch), and it
             will link the versioning object to the branch; and then lock the versioning object
             if needed; meanwhile a new link between this new branch (Fnd0Branch) to the
             source branch (Fnd0Branch) the versioning object linked with.
             



Teamcenter Component:

             Branching Versioning Foundation - This component consists of the Client and Enterprise
             Tier code and constructs that support Branching Versioning Foundation related functionality
             including such things as Teamcenter application plus SOA, ITK and Preferences.
             
        :param Inputs: 
<i>BranchCreateInput</i> structure represents the criteria to create branch for given
                         revisable objects.
             
        :return: 
        """
        ...
    def GetPromoteBranchCandidates(self, Inputs: list[Bhv0.Services.Strong.Branchfoundation._2017_11.BranchFoundation.GetPromoteBranchCandidatesInfo]) -> Bhv0.Services.Strong.Branchfoundation._2017_11.BranchFoundation.GetPromoteBranchCandidatesResponse:
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
    def GetBranchCandidatesInfo(self, Inputs: list[Bhv0.Services.Strong.Branchfoundation._2019_06.BranchFoundation.GetBranchCandidateInput]) -> Bhv0.Services.Strong.Branchfoundation._2019_06.BranchFoundation.GetBranchCandidatesResponse: ...

