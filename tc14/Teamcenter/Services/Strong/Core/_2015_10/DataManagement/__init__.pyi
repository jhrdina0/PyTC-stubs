import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ReassignParticipantInfo:
    """
    
            A structure containing  a list of input objects  whose participant roles are reassigned,
            assignee to reassign from, assignee to reassign to, a list of participant types,
            a boolean to indicate all participant types and comments.
            
    """
    def __init__(self, ) -> None: ...
    ItemRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    """List of ItemRevision objects to reassign participants roles."""
    FromAssignee: Teamcenter.Soa.Client.Model.ModelObject
    """
            The business object (User, GroupMember or a ResourcePool) to
            be replaced with the toAssignee business object.
            """
    ToAssignee: Teamcenter.Soa.Client.Model.ModelObject
    """
            The business object (User, GroupMember or a ResourcePool) to
            replace the fromAssignee business object.
            """
    ParticipantTypes: list[str]
    """
            List of participant types to be reassigned.  Valid types are:
            

ProposedResponsibleParty

ProposedReviewer

ChangeImplementationBoard

ChangeReviewBoard

ChangeSpecialist1

ChangeSpecialist2

ChangeSpecialist3

Analyst

Requestor



            Custom participant types are also allowed.
            """
    AllParticipantTypes: bool
    """
            If true, all the participant roles for the fromAssignee will be considered for reassignment.
            The values provided in the participantTypes list will be ignored.
            

            If false, only the participant roles provided in the particpantTypes list will be
            considered.
            """
    Comments: str
    """A comment provided during reassignment."""
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify the return data
            elements and partial errors associated with the input structure.
            """

class ReassignParticipantOutput:
    """
    Contains clientId and a list of objects on which the reassign operation failed.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify the return data
            elements and partial errors associated with the input structure.
            """
    FailedItemRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    """A list of ItemRevision objects on which the reassign operation failed."""

class ReassignParticipantResponse:
    """
    Contains a list of failed objects information and ServiceData.
    """
    def __init__(self, ) -> None: ...
    FailedObjects: list[ReassignParticipantOutput]
    """A list of failed objects information."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The modified participant objects are returned along with partial errors."""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ReassignParticipants(self, ReassignParticipantInfo: list[ReassignParticipantInfo]) -> ReassignParticipantResponse:
        """    
             Reassigns the participant roles from one user to another for a given list of participant
             types on the input list of objects. The Particpant for the fromAssignee User
             is replaced with the Particpant for the toAssignee User. If the toAssignee
             User already exists as participant, then the fromAssignee User will
             not be replaced.
             

Use Cases:

             For Change Management use cases, user may need to reassign participant roles on the
             change objects like analyst, change specialist etc.  This operation can be used to
             reassign such participants.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param ReassignParticipantInfo: 
                         A list of structures containing a list of input objects whose participant roles are
                         reassigned, assignee to reassign from, assignee to reassign to list of participant
                         types, flag to indicate all participan types and comments.
             
        :return: 214470 - Failed to reassign participants.
        """
        ...

