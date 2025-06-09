import System
import Teamcenter.Soa.Client.Model
import typing

class Context:
    """
    Represents the preference context values.
    """
    def __init__(self, ) -> None: ...
    ContextName: str
    """
            Context name for the values.
            

            The default one is "Teamcenter". It can also be set to be used with NXManager,
            by setting the TC_Application environment variable to UGMAN.
            
"""
    Value: list[str]
    """List of values applicable for the context."""

class PreferenceDefinition:
    """
    
            The PreferenceDefinition structure represents the definition for a preference in
            Teamcenter.
            
    """
    def __init__(self, ) -> None: ...
    PreferenceName: str
    """Name of the preference."""
    PreferenceCategory: str
    """Category of the preference."""
    PreferenceDescription: str
    """Description of the preference."""
    PreferenceScope: str
    """Scope of the preference. It can be "USER", "ROLE", "GROUP" or "SITE"."""
    PreferenceType: str
    """Type of the preference. It can be "STRING", "LOGICAL", "INTEGER", "DOUBLE" or "DATE"."""
    IsArray: bool
    """Specifies if this preference takes multiple values."""
    IsDisabled: bool
    """Specifies if this preference is enabled."""

class PreferenceInfo:
    """
    
            Holds the complete information about a preference: its definition is captured in
            the PreferenceDefinition structure, and its values in the list of Context
            structures.
            

    """
    def __init__(self, ) -> None: ...
    PreferenceDefinition: PreferenceDefinition
    """A structure holding the definition of the preference."""
    ContextInformation: list[Context]
    """A list of Context structures, each representing the values for a given context."""

class PreferencesInfo:
    """
    Contains a list of PreferenceInfo structures.
    """
    def __init__(self, ) -> None: ...
    PrefsInfo: list[PreferenceInfo]
    """List of PreferenceInfo structure."""

class PreferencesSetInput:
    """
    Input to be provided for setting preferences.
    """
    def __init__(self, ) -> None: ...
    PreferenceScope: str
    """Location of the preference."""
    InputPrefs: PreferencesInfo
    """Preferences to be set."""
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """
            Object to which the preferences have to be assigned.
            
            This can be a User, Role or Group. If no value is specified, preferences are set
            for the current session based on the scope.
            
            To be able to set preferences for the site, the user must be a system administrator.
            
            To be able to set preferences for a group or a role, the user must be group administrator
            or a system administrator.
            
"""

class PreferenceManagement:
    """
    Interface PreferenceManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SetPreferences(self, SetPrefInput: list[PreferencesSetInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Sets the values for session or non-session preferences.
             

             Session preferences are preferences as seen from the current logged-in user.
             
             Non-session preferences are preferences that are normally not accessible to the current
             logged-in user.
             

             To set a non-session preference, a target object must be specified in the PreferencesSetInput structure. For user preferences, only the
             value of preference is stored in the database. The description of user preference
             is never stored in the database.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param SetPrefInput: 
                         Details of the preferences to be set.
             
        :return: Success is defined by the Partial Errors list in the service data object returned.
             Only Pass/Fail is returned in the error list. <br /><br />The error stack
             can contain the following error: <br /><ul><ul><li type="disc">1713:
             if the scope parameter of the <font face="courier" height="10">PreferencesSetInput</font>
             structure is set to "<b>SITE</b>" and an object is added to the structure.</li><li>1771:
             If one of the values is incompatible with a preference of type Integer.</li><li>1772:
             If one of the values is incompatible with a preference of type Double.</li><li>1773:
             If one of the values is incompatible with a preference of type Date.</li><li>1774:
             If one of the values is incompatible with a preference of type Logical.</li></ul></ul>
        """
        ...

