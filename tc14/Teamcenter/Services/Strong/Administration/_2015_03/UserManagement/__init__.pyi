import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class UserProfileProperties:
    """
    User and its Fnd0CustomUserProfile properties
    """
    def __init__(self, ) -> None: ...
    User: Teamcenter.Soa.Client.Model.Strong.User
    """User object on which Fnd0CustomUserProfile properties need to be set."""
    PropertyMap: System.Collections.Hashtable
    """
            Property map with property name and list of values in string format. The calling
            client is responsible for converting the different property types (int, float, date
            .etc) to a string using the appropriate functions in the SOA client framework's Property
            class.
            """

class UserProfilePropertiesResponse:
    """
    
            A list of Fnd0CustomUserProfile objects, one for each of the given User
            object.
            
    """
    def __init__(self, ) -> None: ...
    UserProfileMap: System.Collections.Hashtable
    """User and its corresponding Fnd0CustomUserProfile object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data with partial errors if any."""

class UserManagement:
    """
    Interface UserManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SetUserProfileProperties(self, UserProfileInputs: list[UserProfileProperties]) -> UserProfilePropertiesResponse:
        """    
             This operation sets the given properties on the Fnd0CustomUserProfile of the
             specified User. A new Fnd0CustomUserProfile object will be created
             if it does not already exist and the fnd0custom_user_profile property of the
             User will be set to the newly created Fnd0CustomUserProfile object.
             

Use Cases:

             Use Case 1: Set the properties for a User who does not have a Custom User Profile
             object.
             
             Use Case 2: Set the properties for a User who has a Custom User Profile object.
             


Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param UserProfileInputs: 
                         List of UserProfileProperties
             
        :return: 
        """
        ...

