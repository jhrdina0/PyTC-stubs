import typing

class PreferenceManagement:
    """
    Interface PreferenceManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def RefreshPreferences(self) -> bool:
        """    
             Refreshes the preference values stored in the server cache, so that they are synchronized
             with the latest values.
             

             This situation might happen when the preferences for a given user are being changed
             in 2 different sessions, or when an administrator is making changes to the Site /
             Role or Group preferences.
             
             <Calling the refreshPreferences operation will retrieve the updated values.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :return: 
        """
        ...

