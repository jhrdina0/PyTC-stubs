import Teamcenter.Services.Strong.Core._2009_04.ProjectLevelSecurity
import Teamcenter.Soa.Client.Model.Strong
import typing

class ProjectLevelSecurity:
    """
    Interface ProjectLevelSecurity
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDefaultProject(self, TcUser: Teamcenter.Soa.Client.Model.Strong.User, TcGroup: Teamcenter.Soa.Client.Model.Strong.Group, TcRole: Teamcenter.Soa.Client.Model.Strong.Role) -> Teamcenter.Services.Strong.Core._2009_04.ProjectLevelSecurity.LoadProjectDataForUserResponse: ...

