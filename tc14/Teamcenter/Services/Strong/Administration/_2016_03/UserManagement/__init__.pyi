import Teamcenter.Soa.Client.Model
import typing

class DeleteUsersInput:
    """
    Input structure to delete User object.
    """
    def __init__(self, ) -> None: ...
    UserId: str
    """The User ID of the User to be deleted."""
    NewOwningUser: str
    """
            The User ID to assign ownership of the objects currently owned by userId. This value is ignored if deleteObjects
            is true. A value must be provided if deleteObjects
            is false.
            """
    NewOwningGroup: str
    """
            The name of the Group to assign Group ownership of object currently owned
            by the userId. The newOwningUser
            must be a member of this group.The Group name is ignored if deleteObjects is true. If deleteObjects
            is false and value is not given then the default group of newOwningUser
            is used.
            """
    DeleteObjects: bool
    """
            If true, the objects owned by userId are
            deleted. If false, the objects are kept and their ownership is transferred to newOwningUser and newOwningGroup.
            """

class UserManagement:
    """
    Interface UserManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def DeleteUser(self, UserInput: list[DeleteUsersInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes User objects from Teamcenter. The objects owned by
             the user can be deleted or keep and transfer their ownership to a new user. This
             operation requires system administration privilege.
             

Use Cases:

             Use Case 1: Delete User with given user id.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param UserInput: 
                         List of Users that need to be deleted.
             
        :return: 
        """
        ...

