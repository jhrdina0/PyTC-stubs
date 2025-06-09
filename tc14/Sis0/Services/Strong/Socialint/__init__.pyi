import Sis0.Services.Strong.Socialint._2019_06.TeamCollaborationService
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class TeamCollaborationServiceRestBindingStub(TeamCollaborationServiceService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def DeleteKeys(self, Input: list[Sis0.Services.Strong.Socialint._2019_06.TeamCollaborationService.DeleteKeyInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetChannels(self, Input: list[Sis0.Services.Strong.Socialint._2019_06.TeamCollaborationService.AppId]) -> Sis0.Services.Strong.Socialint._2019_06.TeamCollaborationService.GetChannelsResponse: ...
    def PostToSocial(self, Input: list[Sis0.Services.Strong.Socialint._2019_06.TeamCollaborationService.WriteInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def QueryAppIds(self, Input: list[str]) -> Sis0.Services.Strong.Socialint._2019_06.TeamCollaborationService.QueryAppIdsResponse: ...
    def RegisterSocialUser(self, Input: list[Sis0.Services.Strong.Socialint._2019_06.TeamCollaborationService.SocialUserInput]) -> Sis0.Services.Strong.Socialint._2019_06.TeamCollaborationService.RegisterSocialUserResponse: ...
    def RotateTokens(self, Input: list[Sis0.Services.Strong.Socialint._2019_06.TeamCollaborationService.AppId]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class TeamCollaborationServiceService:
    """
    
            This service contains all the operations which support the Team Collaboration Integration
            Solution.
            


Library Reference:

Sis0SoaSocialIntStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> TeamCollaborationServiceService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def DeleteKeys(self, Input: list[Sis0.Services.Strong.Socialint._2019_06.TeamCollaborationService.DeleteKeyInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetChannels(self, Input: list[Sis0.Services.Strong.Socialint._2019_06.TeamCollaborationService.AppId]) -> Sis0.Services.Strong.Socialint._2019_06.TeamCollaborationService.GetChannelsResponse:
        """    
             This operation returns the list of configured channels for the specified workspace.
             

Use Cases:

Post to channel use case:

             1. User logs into ActiveWorkspace.
             
             2. User brings up the "Share to Social" dialog.
             
             3. User selects which workspace to post to.
             
             4. ActiveWorkspace uses the workspace information invoke the getChannels operation.
             
             5. ActiveWorkspace populates the channels box with the list of available channels.
             

Teamcenter Component:

             Team Collaboration Integration - The Team Collaboration Integration component enables
             Teamcenter to communicate with Social Applications.
             
        :param Input: 
                         The list of AppIds for which to query channels.
             
        :return: 
        """
        ...
    def PostToSocial(self, Input: list[Sis0.Services.Strong.Socialint._2019_06.TeamCollaborationService.WriteInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def QueryAppIds(self, Input: list[str]) -> Sis0.Services.Strong.Socialint._2019_06.TeamCollaborationService.QueryAppIdsResponse: ...
    def RegisterSocialUser(self, Input: list[Sis0.Services.Strong.Socialint._2019_06.TeamCollaborationService.SocialUserInput]) -> Sis0.Services.Strong.Socialint._2019_06.TeamCollaborationService.RegisterSocialUserResponse: ...
    def RotateTokens(self, Input: list[Sis0.Services.Strong.Socialint._2019_06.TeamCollaborationService.AppId]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

