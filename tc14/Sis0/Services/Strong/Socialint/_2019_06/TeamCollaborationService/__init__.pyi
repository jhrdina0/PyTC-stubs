import System
import Teamcenter.Soa.Client.Model
import typing

class AppId:
    """
    
            This object represents the input required in order to iinvoke operations for a configured
            social application workspace.
            
    """
    def __init__(self, ) -> None: ...
    Id: str
    """
            The Social Application Workspace or Team ID. Typically, this value is obtained as
            output from the QueryAppIds SOA operation.
            """
    SocialAppType: str

class DeleteKeyInput:
    """
    
            This object defines the required input for deleting a configured social application
            workspace.
            
    """
    def __init__(self, ) -> None: ...
    Id: str
    """The Social Application Workspace or Team ID to delete."""
    SocialAppType: str
    Uninstall: bool
    """
            If true, in addition to deleting the configured social application workspace, it
            will also uninstall the integration from the social app; otherwise, not.
            """

class GetChannelsResponse:
    """
    This object represents the output from the GetChannels operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[str]
    """The channel data in JSON format."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class QueryAppIdsResponse:
    """
    
            This object represents the queryAppIds response from the Team Collaboration Integration
            (TCI) microservice.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[str]
    """The JSON output representing the configured workspace/teams in the TCI microservice."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class RegisterSocialUserResponse:
    """
    This object represents the output from the registerSocialUser SOA operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[str]
    """The key for the register social user entry in the TCI microservice."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class SocialUserInput:
    """
    
            This object represents the data required in order to create a user in the Team Collaboration
            Integration microservice (TCI).
            
    """
    def __init__(self, ) -> None: ...
    SocialAppType: str
    RedirectUri: str
    """
            The URL to redirect the user back to after the user after the user is register in
            the Team Collaboration Integration (TCI).
            """

class WriteInput:
    """
    This class represents the input to the write API in the TCI microservice.
    """
    def __init__(self, ) -> None: ...
    AppId: str
    """The Social Application Workspace or Team ID to post to."""
    SocialAppType: str
    Channel: str
    """The Workspace Or Team channel to post to."""
    Text: str
    AsUser: bool
    """If true, post the message as a User; otherwise, as a System message."""

class TeamCollaborationService:
    """
    Interface TeamCollaborationService
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def DeleteKeys(self, Input: list[DeleteKeyInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetChannels(self, Input: list[AppId]) -> GetChannelsResponse:
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
    def PostToSocial(self, Input: list[WriteInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def QueryAppIds(self, Input: list[str]) -> QueryAppIdsResponse: ...
    def RegisterSocialUser(self, Input: list[SocialUserInput]) -> RegisterSocialUserResponse: ...
    def RotateTokens(self, Input: list[AppId]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

