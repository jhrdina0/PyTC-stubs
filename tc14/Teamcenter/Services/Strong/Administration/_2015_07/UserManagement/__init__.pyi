import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateOrUpdateUserInputs:
    """
    Input structure to create or update User object.
    """
    def __init__(self, ) -> None: ...
    UserId: str
    """User ID of the User object which need to be created or updated."""
    Person: str
    """Name of the Person this User belongs to."""
    Password: str
    """Password of the User in plain text."""
    DefaultGroup: str
    """Default group of the User."""
    NewOwner: str
    """
            The user ID of the new owning user of objects owned by the user to be deactivated.
            It should be set only if the current user is going to be deactivated.
            """
    NewOwningGroup: str
    """
            The name of new owning group of objects owned by the user to be deactivated. It should
            be set only if the current user is going to be deactivated.
            """
    UserPropertyMap: System.Collections.Hashtable
    UserAddlPropertyMap: System.Collections.Hashtable

class CreateOrUpdateUserResponse:
    """
    Response structure of creteOrUpdateUser operation.
    """
    def __init__(self, ) -> None: ...
    UserObjectMap: System.Collections.Hashtable
    """
            User Id and its corresponding UserObjectStructure which contains User, Person
            and Fnd0CustomUserProfile objects.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data with partial errors if any."""

class UserObjectStructure:
    """
    
            The output structure for createOrUpdateUser operation. It contains created or updated
            User with its Person and Fnd0CustomUserProfile objects.
            
    """
    def __init__(self, ) -> None: ...
    User: Teamcenter.Soa.Client.Model.Strong.User
    """The User object."""
    Person: Teamcenter.Soa.Client.Model.Strong.Person
    """The Person object of corresponding User."""
    Profile: Teamcenter.Soa.Client.Model.Strong.Fnd0CustomUserProfile
    """The Fnd0CustomUserProfile object of corresponding User."""

class UserManagement:
    """
    Interface UserManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateUser(self, UserInputs: list[CreateOrUpdateUserInputs]) -> CreateOrUpdateUserResponse: ...

