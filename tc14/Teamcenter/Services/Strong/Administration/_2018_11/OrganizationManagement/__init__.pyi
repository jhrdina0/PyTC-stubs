import Teamcenter.Soa.Client.Model
import typing

class UserConsentStatement:
    """
    Output strucutre of getUserConsentStatement operation.
    """
    def __init__(self, ) -> None: ...
    ConsentStatement: str
    """User consent statement for the locale the user is logged in."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data with the partial error information."""

class OrganizationManagement:
    """
    Interface OrganizationManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetUserConsentStatement(self) -> UserConsentStatement: ...
    def RecordUserConsent(self, UserConsent: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

