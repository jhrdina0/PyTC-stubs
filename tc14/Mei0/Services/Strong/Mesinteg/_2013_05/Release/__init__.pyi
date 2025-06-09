import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class UnitEffectivityInfo:
    """
    Unit effectivity details.
    """
    def __init__(self, ) -> None: ...
    EndItem: Teamcenter.Soa.Client.Model.ModelObject
    """The Effectivity end item."""
    EndItemRev: Teamcenter.Soa.Client.Model.ModelObject
    """The Effectivity end item revision."""
    OrderId: int
    """The order ID which is saved on the Effectivity object."""

class ApplyReleaseStatusToLinesInputData:
    """
    Release status details to be applied to the lines.
    """
    def __init__(self, ) -> None: ...
    Roots: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The Mfg0BvrProcess and Mfg0BvrOperation to be traversed."""
    ReleaseStatus: str
    """The ReleaseStatus to be created from the string."""
    UnitEffectivityInfo: UnitEffectivityInfo
    """The input parameters in order to create the Effectivity object."""
    IsRecursive: bool
    """
            True to expend below the structure from the roots to the leaves, otherwise use only
            the root object.
            """

class CreatedBopWindowInfo:
    """
    The configuration details of the BOP window and the top line information.
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """The context of the BOPWindow."""
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The top line of the BOPWindow."""

class ReleaseCandidatesDeltaReleaseInfo:
    """
    Information about Release Candidates.
    """
    def __init__(self, ) -> None: ...
    ReleaseCandidatesFromReleaseStatus: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of Mfg0BvrProcess and  Mfg0BvrOperation."""
    ReleaseCandidatesWithIncrementalChange: System.Collections.Hashtable
    """
            The key will be the IncrementalChange and the value is the list of Mfg0BvrProcess
            and Mfg0BvrOperation affected by.
            """

class ReleaseCandidatesFullReleaseInfo:
    """
    
            The structure has the additional information in case that the user exports the entire
            structure and not just a delta export.
            
    """
    def __init__(self, ) -> None: ...
    ExecutionPlan: Teamcenter.Soa.Client.Model.ModelObject
    """The Mei0ExecutionPlan (Derives from CCObject) to be exported."""
    TargetSites: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of sites to export the data."""

class CreateReleaseUpdatePackageInputData:
    """
    
            A vector of objects that holds all the release candidates objects and ICs for the
            created workflow.
            
    """
    def __init__(self, ) -> None: ...
    DeltaReleaseinfo: ReleaseCandidatesDeltaReleaseInfo
    """Information about Release Candidates."""
    FullReleaseInfo: ReleaseCandidatesFullReleaseInfo
    """
            The structure has the additional information in case that the user exports the entire
            structure and not just a delta export.
            """
    FullReleaseUpdate: bool
    """True in case that a full release update, false in case of a delta release"""
    WorkflowTemplate: Teamcenter.Soa.Client.Model.ModelObject
    """The EPMTaskTemplate to be created."""
    InfoForm: Teamcenter.Soa.Client.Model.ModelObject
    """
            The Mei0ReleaseUpdateToMesInfo form or any other customized form with the export
            additional information to be attached to the workflow.
            """

class CreateReleaseUpdatePackageResponse:
    """
    The results of the created workflow
    """
    def __init__(self, ) -> None: ...
    Workflows: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The list of created EPMJob."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The list of errors Partial Errors are returned in the ServiceData:  286520:   A full
            export had not been created primary to releasing an update. 286523:   Cannot have
            more than a single BOPWindow configured in the structure. 286524: The EPMTaskTemplate
            does not exist. 286525: The object is not valid to be export, the object ID and name
            will be supplied.
            """

class FindReleaseCandidatesInputData:
    """
    
            The input structure contains the data we need in order to find the release candidates
            Lines or ICs for release and Release to the MES system
            
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """The context of the BOP window.Currently will be passed as NULL from the client."""
    ReleaseCandidatesRoots: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of Mfg0BvrProcess and Mfg0BvrOperation to be traversed."""
    CheckIncrementalChange: bool
    """Whether to check the incremental changes or not."""

class FindReleaseCandidatesResponse:
    """
    
            The results of the calculation for finding the release candidates lines from Item
            Revisions and from ICs.
            
    """
    def __init__(self, ) -> None: ...
    ReleaseCandidatesInformationList: list[ReleaseCandidatesDeltaReleaseInfo]
    """A list of the release candidate's information."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Including partial errors These errors will be returned in the serviceData as partial
            errors:- 286520:   A full export had not been created primary to releasing an update.
            286523:   Cannot have more than a single BOPWindow configured in the structure. 286525:
            The object is not valid to be export, the object ID and name will be supplied.
            """

class IsUpdateAllowedResponse:
    """
    Response.
    """
    def __init__(self, ) -> None: ...
    PreviousReleaseInformationList: list[PreviousReleaseInfo]
    """
            A list of structures which contains the information regarding the previous release
            and export for the same Mei0ExecutionPlan object.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The list of errors Partial Errors are returned in the ServiceData: 286523: Cannot
            have more than a single BOPWindow configured in the structure.
            """

class OpenPreviousReleasedVersionResponse:
    """
    OpenPreviousReleasedVersionResponse
    """
    def __init__(self, ) -> None: ...
    CreatedWindowInfo: list[CreatedBopWindowInfo]
    """The returned CreatedBopWindowInfo."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            These errors will be returned in the serviceData as partial errors. 286520:    A
            full export had not been created primary to releasing an update. 286523:Cannot have
            more than a single BOPWindow configured in the structure.
            """

class PreviousReleaseInfo:
    """
    
            Contains the information regarding the previous release and export which had already
            done for the same Mei0ExecutionPlan object.
            
    """
    def __init__(self, ) -> None: ...
    AppInterface: Teamcenter.Soa.Client.Model.ModelObject
    """The AppInterface used for the previous export."""
    IsAllowed: bool
    """
            The Boolean result of this operation. Is true if the RequestObject was found otherwise
            false.
            """

class Release:
    """
    Interface Release
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ApplyReleaseStatusToLines(self, Input: list[ApplyReleaseStatusToLinesInputData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation collects all the Mfg0BvrProcess and Mfg0BvrOperation recursively from
             the configured structure and adds a ReleaseStatus object to the non-released objects.
             

Teamcenter Component:

             MES Integration Services Component - Manufacturing execution system (MES) Integration
             Services Component supports the integration with the SIMATIC IT (SIT) and general
             MES systems.
             
        :param Input: 
                         Release status details to be applied to the lines.
             
        :return: 286541: If the provided release status cannot be applied to the object.
        """
        ...
    def CreateReleaseUpdatePackage(self, Input: list[CreateReleaseUpdatePackageInputData]) -> CreateReleaseUpdatePackageResponse:
        """    
             The operation creates the workflow ReleaseUpdateToMes which exports the released
             candidate objects to the MES system.  It is a preliminary to call the operation findReleaseCandidates
             before calling the createReleaseUpdatePackage operation.
             

Teamcenter Component:

             MES Integration Services Component - Manufacturing execution system (MES) Integration
             Services Component supports the integration with the SIMATIC IT (SIT) and general
             MES systems.
             
        :param Input: 
                         A vector of objects that holds all the release candidates objects and ICs for the
                         created workflow.
             
        :return: The results of the created workflow
        """
        ...
    def FindReleaseCandidates(self, Input: list[FindReleaseCandidatesInputData]) -> FindReleaseCandidatesResponse:
        """    
             The operation returns all the Mfg0BvrProcess and Mfg0BvrOperation candidates to be
             exported to the MES system. The candidate objects will be captured in one out of
             the two ways: 1. By a new release status Mei0PendingRelease or the status defined
             within the preference Mei0PendingReleaseStatus added to the revision.  2. Any change
             that was done within the incremental change which is configured in the structure.
             

Teamcenter Component:

             MES Integration Services Component - Manufacturing execution system (MES) Integration
             Services Component supports the integration with the SIMATIC IT (SIT) and general
             MES systems.
             
        :param Input: 
                         The input structure contains the data we need in order to find the release candidates
                         Lines or ICs for release and Release to the MES system
             
        :return: The results of the calculation for finding the release candidates lines from Item
             Revisions and from ICs.
        """
        ...
    def IsUpdateAllowed(self, ExecutionPlans: list[Teamcenter.Soa.Client.Model.ModelObject]) -> IsUpdateAllowedResponse:
        """    
             The operation checks if a delta update is allowed for the Mei0ExecutionPlan.
             

Teamcenter Component:

             MES Integration Services Component - Manufacturing execution system (MES) Integration
             Services Component supports the integration with the SIMATIC IT (SIT) and general
             MES systems.
             
        :param ExecutionPlans: 
                         This object derives from an MECollaborationContext object.
             
        :return: These errors will be returned in the serviceData as partial errors. 286523: Cannot
             have more than a single BOPWindow configured in the structure.
        """
        ...
    def OpenPreviousReleasedVersion(self, ExecutionPlans: list[Teamcenter.Soa.Client.Model.ModelObject]) -> OpenPreviousReleasedVersionResponse:
        """    
             This operation returns the correlative structure which had been released and exported
             for the existing Mei0ExecutionPlan.
             

Teamcenter Component:

             MES Integration Services Component - Manufacturing execution system (MES) Integration
             Services Component supports the integration with the SIMATIC IT (SIT) and general
             MES systems.
             
        :param ExecutionPlans: 
                         The Mei0ExecutionPlan which had been exported.
             
        :return: Response
        """
        ...

