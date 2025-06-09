import typing

class PreferenceManagement:
    """
    Interface PreferenceManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def LockSitePreferences(self) -> bool:
        """    
             Locks the Site preferences stored in the database.
             

             This can be used by system administrators only. It is not mandatory to lock Site
             preferences to make changes, but it ensures exclusive write accesses when necessary.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :return: 
        """
        ...
    def UnlockSitePreferences(self) -> bool:
        """    
             Releases the lock set on the site preferences stored in the database. The locking
             comes from the call to lockSitePreferences operation. Only the user who locked the
             site preferences is allowed to unlock them. As of Teamcenter 11.6, due to the re-architecture
             of preferences from XML storage to database objects, this operation is no longer
             required. So it is deprecated.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :return: 
        """
        ...

