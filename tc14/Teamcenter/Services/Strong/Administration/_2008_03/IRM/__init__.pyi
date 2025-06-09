import Teamcenter.Soa.Client.Model
import typing

class ActivateUserInput:
    """
    
            This structure holds the User object to be activated and the license level
            to be granted for the user.
            
    """
    def __init__(self, ) -> None: ...
    LicenseLevel: int
    """The license level to be granted to the user."""
    TargetUser: Teamcenter.Soa.Client.Model.ModelObject
    """The user to be activated and granted the licnese level."""

class DeactivateUserInput:
    """
    
            This structure holds the target user to be deactivated and new user and group to
            take the ownership of objects owned by the target user.
            
    """
    def __init__(self, ) -> None: ...
    TargetUser: Teamcenter.Soa.Client.Model.ModelObject
    """The user to be deactivated."""
    NewUser: Teamcenter.Soa.Client.Model.ModelObject
    """The new user to take ownership transferred from the deactivated user."""
    NewGroup: Teamcenter.Soa.Client.Model.ModelObject
    """The new group to take ownership transferred from the deactivated user."""

class LicenseStatus:
    """
    
            This structure  holds the number of licenses purchased and the number of licenses
            used.
            
    """
    def __init__(self, ) -> None: ...
    NumPurchasedLicenses: int
    """The number of licenses purchased."""
    NumUsedLicenses: int
    """The number of licenses used."""

class LicenseStatusResponse:
    """
    
            This structure  holds a list of license statuses for the each given user license
            type.
            
    """
    def __init__(self, ) -> None: ...
    LicStatus: list[LicenseStatus]
    """List of LicenseStatus objects, one for each ActivateUserInput object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Object with all activated User objects in updated list and any errors that
            occurred during activating users.
            """

class IRM:
    """
    Interface IRM
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ActivateUsers(self, ActivateUser: list[ActivateUserInput]) -> LicenseStatusResponse:
        """    
             This operation can be used to activate user(s) based on the number of allowed active
             author or consumer licenses. If not enough licenses are available, this operation
             will return corresponding error code for the given license level. This operation
             activates only the user and not the Group Members corresponding to the user.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param ActivateUser: 
                         A list of ActivateUserInput objects with user and license level to set.
             
        :return: 
        """
        ...
    def DeactivateUsers(self, DeactivateUser: list[DeactivateUserInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deactivates given users and transfers ownership of the objects owned
             by the users to be deactivated to new users if the new users are specified. The users
             deactivated successfully are added in the updated object list of the service data.
             If new users and groups are specified to take the ownership of the objects owned
             by the deactivated users, then the new users and groups are added in the updated
             object list as well after ownership is successfully transferred. This operation requires
             system administration privilege.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param DeactivateUser: 
                         A list of users objects to be deactivated.
             
        :return: .
        """
        ...

