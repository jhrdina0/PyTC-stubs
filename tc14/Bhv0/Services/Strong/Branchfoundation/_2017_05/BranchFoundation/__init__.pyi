import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AddContentToBranchInfo:
    """
    
            AddContentToBranchInfo structure to represents the information related to the objects
            being added to the branch.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """Identifier defined by client to track the related object."""
    ParentBranch: Teamcenter.Soa.Client.Model.Strong.Fnd0Branch
    """The parent Fnd0Branch object."""
    BranchContent: list[BranchContentInfo]
    """Information related to the objects being added to the branch."""

class BranchContentInfo:
    """
    
            BranchContentInfo structure represents the information of each object being added
            to the branch.
            
    """
    def __init__(self, ) -> None: ...
    VersionObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """WorkspaceObject to be added to the branch."""
    PropMap: System.Collections.Hashtable
    """
            Map (string, list of strings) of properties to be updated on the Fnd0BranchContent
            relation object.
            """

class BranchRelatedCreateInput:
    """
    
            BranchRelatedCreateInput structure represents information to create the branch or
            branch related object like branch comments.
            
    """
    def __init__(self, ) -> None: ...
    BoName: str
    """The business object name. Only support Fnd0Branch or its sub type."""
    PropMap: System.Collections.Hashtable
    """Property map to create branch related object."""

class BranchCreateInput:
    """
    
            BranchCreateInput structure represents the criteria to publich revisable object to
            a branch.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """Identifier defined by client to track the related object."""
    ParentClientID: str
    """
            Another BranchPublicationInput clientID that will be created as parent branch of
            the current branch.
            """
    ParentBranch: Teamcenter.Soa.Client.Model.Strong.Fnd0Branch
    """
            The parent Fnd0Branch object.
            

If both parentClientID and parentBranch are null, current branch
            object will be created as a trunk.
            

"""
    BranchContents: list[BranchContentInfo]
    """A list of branch content (version object and relation properties) to be added."""
    BranchObj: BranchRelatedCreateInput
    """
            BranchRelatedCreateInput which contains information to create branch object
            

Trunk when current object is a trunk
            
Branch-x when current object is a branch
            

"""
    BranchComment: BranchRelatedCreateInput
    """BranchRelatedCreateInput which contains information to create branch comment object."""

class CreateBranchResponse:
    """
    
            CreateBranchResponse holds the response of publication object to branch. This output
            structure contains service data with partial errors and outputMap which contains
            list of Fnd0Branch objects related to structure.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The Service Data with partial errors for BranchPublicationInput identified by its
            clientId.
            """
    OutputMap: System.Collections.Hashtable
    """A map of client identifer and list of BranchInfo pairs."""

class BranchFoundation:
    """
    Interface BranchFoundation
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddContentToBranch(self, Inputs: list[AddContentToBranchInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateBranches(self, Inputs: list[BranchCreateInput]) -> CreateBranchResponse:
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

