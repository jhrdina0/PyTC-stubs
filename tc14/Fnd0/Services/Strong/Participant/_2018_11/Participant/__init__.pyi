import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ParticipantInfo:
    """
    
            ParticipantInfo structure contains information about WorkspaceObject and list
            of Participant objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    Wso: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """WorkspaceObject whose participants are modified."""
    Participants: list[Teamcenter.Soa.Client.Model.Strong.Participant]
    """A list of Participant objects."""
    AdditionalData: System.Collections.Hashtable

class ParticipantInfoInput:
    """
    
            ParticipantInfoInput structure contains information about WorkspaceObject
            and list of ParticipantInput structures.
            
    """
    def __init__(self, ) -> None: ...
    Wso: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The WorkspaceObject on which the particpant is to be added."""
    AdditionalData: System.Collections.Hashtable
    ParticipantInputData: list[ParticipantInput]
    """
            A list of ParticipantInput structures. Each element will contain the assignee and
            corresponding participant type.
            """

class ParticipantInfoOutput:
    """
    
            ParticipantInfoOutput structure contains information about list of WorkspaceObject
            objects on which the participant failed to get reassigned.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    WsoList: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """
            A list of WorkspaceObject objects on which the participants failed to get
            reassigned.
            """
    AdditionalData: System.Collections.Hashtable

class ParticipantInput:
    """
    ParticipantInput structure contains information about assignee and participant type.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    Assignee: Teamcenter.Soa.Client.Model.ModelObject
    """The participant which can be a User, GroupMember or a ResourcePool."""
    ParticipantType: str
    """
            Corresponding participant type to which the assignee will be added. For example PROPOSED_RESPONSIBLE_PARTY,
            PROPOSED_REVIEWERS, CHANGE_SPECIALIST1, CHANGE_SPECIALIST2, CHANGE_SPECIALIST3, CHANGE_REVIEW_BOARD,
            CHANGE_IMPLEMENTATION_BOARD, ANALYST, REQUESTOR.
            """

class ParticipantResponse:
    """
    
            ParticipantResponse structure contains information about list of ParticipantInfo
            structures and service data.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[ParticipantInfo]
    """A list of ParticipantInfo structure."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class ReassignParticipantInfoInput:
    """
    
            ReassignParticipantInfoInput structure contains information about WorkspaceObject,
            old value of assignee, new value of assignee, participant types and comments.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    WsoList: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """A list of WorkspaceObject to reassign participant roles."""
    FromAssignee: Teamcenter.Soa.Client.Model.ModelObject
    """
            The business object that can be User, GroupMember or ResourcePool
            to be replaced with the toAssignee business object.
            """
    ToAssignee: Teamcenter.Soa.Client.Model.ModelObject
    """
            The business object that can be User, GroupMember or ResourcePool
            to replace the fromAssignee business object.
            """
    ParticipantTypes: list[str]
    """A list of Participant types to be reassigned."""
    AllParticipantTypes: bool
    """
            If true, all the participant roles for the fromAssignee will be considered for reassignment.
            The values provided in the participantTypes list will be ignored. If false, only
            the participant roles provided in the participantTypes list will be considered.
            """
    Comment: str
    """A comment provided during reassignment."""
    AdditionalData: System.Collections.Hashtable

class ReassignParticipantResponse:
    """
    
            ReassignParticipantResponse structure contains information about list of ParticipantInfoOutput
            structures and service data.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[ParticipantInfoOutput]
    """A list of ParticipantInfoOutput structure."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class Participant:
    """
    Interface Participant
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddParticipants(self, Input: list[ParticipantInfoInput]) -> ParticipantResponse: ...
    def ReassignParticipants(self, Input: list[ReassignParticipantInfoInput]) -> ReassignParticipantResponse: ...
    def RemoveParticipants(self, Input: list[ParticipantInfo]) -> ParticipantResponse: ...

