import Fnd0.Services.Strong.Participant._2018_11.Participant
import System
import Teamcenter.Soa.Client

class ParticipantRestBindingStub(ParticipantService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def AddParticipants(self, Input: list[Fnd0.Services.Strong.Participant._2018_11.Participant.ParticipantInfoInput]) -> Fnd0.Services.Strong.Participant._2018_11.Participant.ParticipantResponse: ...
    def ReassignParticipants(self, Input: list[Fnd0.Services.Strong.Participant._2018_11.Participant.ReassignParticipantInfoInput]) -> Fnd0.Services.Strong.Participant._2018_11.Participant.ReassignParticipantResponse: ...
    def RemoveParticipants(self, Input: list[Fnd0.Services.Strong.Participant._2018_11.Participant.ParticipantInfo]) -> Fnd0.Services.Strong.Participant._2018_11.Participant.ParticipantResponse: ...

class ParticipantService:
    """
    
            Participant service exposes operations to add, remove and reassign participants.
            Participants are added, removed and ressigned on WorkspaceObjects like workflow targets
            or the workflow (EPMJob) itself. The participants can then be used by handlers within
            the workflow during execution.
            


Library Reference:

Fnd0SoaParticipantStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ParticipantService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def AddParticipants(self, Input: list[Fnd0.Services.Strong.Participant._2018_11.Participant.ParticipantInfoInput]) -> Fnd0.Services.Strong.Participant._2018_11.Participant.ParticipantResponse: ...
    def ReassignParticipants(self, Input: list[Fnd0.Services.Strong.Participant._2018_11.Participant.ReassignParticipantInfoInput]) -> Fnd0.Services.Strong.Participant._2018_11.Participant.ReassignParticipantResponse: ...
    def RemoveParticipants(self, Input: list[Fnd0.Services.Strong.Participant._2018_11.Participant.ParticipantInfo]) -> Fnd0.Services.Strong.Participant._2018_11.Participant.ParticipantResponse: ...

