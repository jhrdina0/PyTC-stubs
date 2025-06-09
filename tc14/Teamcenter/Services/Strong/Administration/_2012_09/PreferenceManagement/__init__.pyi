import System
import Teamcenter.Soa.Client.Model
import typing

class PreferenceDefinition:
    """
    Contains all the preference definition details.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the preference."""
    Category: str
    """
            The name of the category where the preference is sorted.
            
            A category is a logical group of preferences.
            """
    Description: str
    """The description associated with the preference."""
    Type: int
    """
            Type of the preference.
            
            Values are:
            

0 : String preference
            
1: Logical preference
            
2: Integer preference
            
3: Double preference
            
4: Date preference
            

"""
    IsArray: bool
    """Determines if the preference is multi-valued."""
    IsDisabled: bool
    """
            Determines if the preference is disabled. From Teamcenter 11.6.0, this is not supported.
            It is set to false always.
            """
    ProtectionScope: str
    """
            Determines the protection scope of the preference, which is who is the lowest person
            (in the organization) who is allowed to provide values. Valid values are User, Role,
            Group, Site, System.
            """
    IsEnvEnabled: bool
    """Determines if the value can be taken from an environment variable."""
    IsOOTBPreference: bool
    """
            Determines if the preference is defined out-of-the-box. From Teamcenter 11.6.0, this
            is not supported since there is no differentiation between OOTB and non OOTB preferences.
            It is set to false always.
            """

class PreferenceValue:
    """
    
            Contains the preference value and its location.
            
            This structure is used by different operations with different possible values for
            the location parameter.
            
    """
    def __init__(self, ) -> None: ...
    Values: list[str]
    """The values associated with this preference."""
    ValueOrigination: str
    """
            Defines where the preference values are coming from.
            
            Valid values are:
            

"COTS": The value is the one defined by Siemens.
            
"Overlay":  The COTS value has been altered.
            
"Group": The value is defined at the group level.
            
"Role": The value is defined at the role level.
            
"User": The value is defined at the user level.
            
"Env": The value is coming from an environment variable.
            

"""

class CompletePreference:
    """
    
            Composite structure completely representing a preference: its definition is captured
            in the PreferenceDefinition structure, and its values in the PreferenceValue
            structure.
            
    """
    def __init__(self, ) -> None: ...
    Definition: PreferenceDefinition
    """A structure holding all the preference definition parameters."""
    Values: PreferenceValue
    """A structure holding the preference values."""

class GetPreferencesAtLocationsResponse:
    """
    
            Structure returned by the getPreferencesAtLocation
            operation.
            
    """
    def __init__(self, ) -> None: ...
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """Partial errors. Each partial error will contain the index of the related input data."""
    Responses: list[CompletePreference]
    """
            The preference description and category for the locations OOTB (out-of-the-box),
            Overlay or Site. In the other cases, those strings will be empty.
            """

class GetPreferencesResponse:
    """
    
            Contains the preference information (value and description if requested), as well
            as any potential partial errors.
            
    """
    def __init__(self, ) -> None: ...
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """Contains the partial errors in the same order as in the input list."""
    Response: list[CompletePreference]
    """
            A list of complete preference information.
            
            Each structure holds all the preference definition (PreferenceDefinition
            structure) and its values (PreferenceValue
            structure).
            """

class PreferenceLocation:
    """
    
            Defines where the preference is to be retrieved.
            
            This structure is used by different operations with different possible values for
            the location parameter.
            
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """
            Object where the preferences will be retrieved. This can be a User, Role or Group.
            
            This value can only be used if the location string is empty.
            
"""
    Location: str
    """
            Name of the location.
            
            This value can only be specified if the object is not specified.
            """

class ImportPreferencesAtLocationDryRunIn:
    """
    A structure that contains all the parameters for the import dry run operation.
    """
    def __init__(self, ) -> None: ...
    Location: PreferenceLocation
    """Location where to simulate the import."""
    FileTicket: str
    """Ticket of the input XML file in the transient volume uploaded by the client"""
    CategoryNames: list[str]
    """Vector of category names to be considered for import. No value means import all categories"""

class ImportPreferencesAtLocationDryRunResponse:
    """
    Response from importPreferencesAtLocationDryRun operation.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            A ServiceData structure. The following partial errors will be returned:  * An error
            1759 will be returned if the preference name is empty.   * An error 1760 will be
            returned if the preference name is invalid ("*" for instance).   * An error 1700
            will be returned if the preference does not exist.  * An error 1751 will be returned
            if the specified object information does not correspond to any user, role or group.
            * An error 1752 will be returned if both an object and a location are specified
            for an entry.  * An error 1753 will be returned if the specified location is invalid.
            * An error 1725 will be returned if the logged-in user does not have the requested
            permission to carry-out the operation.  * An error 1728 will be returned in case
            the protection scope of the preference prevents a creation of one instance at the
            specified location.
            """
    DbImpactedPreferences: list[CompletePreference]
    """List of preferences in the database that would be impacted by the import."""
    ConflictingPreferencesFromFile: list[CompletePreference]
    """
            Llist of preferences from the input file, for which conflict will arise.  Conflicts
            are cases in which either the preference already exists in the database and is different,
            or the preference does not exist in the database yet.
            """

class ImportPreferencesAtLocationsIn:
    """
    A structure that contains all the parameters for the import operation.
    """
    def __init__(self, ) -> None: ...
    Locations: list[PreferenceLocation]
    """A list of structures defining where the preferences are to be imported."""
    FileTicket: str
    """Ticket of the input XML file in the transient volume uploaded by the client."""
    CategoryNames: list[str]
    """
            List of category names to be considered for import.
            
            No value means import all categories.
            """
    ImportAction: str
    """
            Specifies what to do when the preference already exists.
            
            Valid values are:
            

"SKIP": to skip the import of this preference.
            
"OVERRIDE": to override the preference value at this location
            with the value specified in the input file.
            
"MERGE": to append the preference value from the input file
            to the preference value at the location. This is only possible if the preference
            is a multi-valued preference. Otherwise, this will result in the "SKIP" action
            for this preference.
            


            If a wrong value is provided, the operation will revert to using the "SKIP"
            mode.
            """

class PreferenceResponseWithFileTicket:
    """
    
            Response that also contains a file ticket, which usage differs upon the operation
            returning it.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            A ServiceData structure.   It will contain errors at indexes where errors have occurred.
            Error details will vary according to the calling operation, and it will be specified
            in its description.
            """
    FileTicket: str
    """
            A ticket of a file in the transient volume uploaded by the client. The content of
            the file will depend on the calling operation, and it will be specified in its description.
            """

class PreferencesAtLocationIn:
    """
    Defines a list of preferences at a provided location.
    """
    def __init__(self, ) -> None: ...
    Location: PreferenceLocation
    """The desired location of the requested preferences."""
    PreferenceNames: list[str]
    """
            A list of desired preference names.
            
            If the list is empty or its first element is "*", all the preferences for the specified
            locations (and only for preference instances at this location) are returned.
            """

class SetPreferences2In:
    """
    Structure of preference name and values.
    """
    def __init__(self, ) -> None: ...
    PreferenceName: str
    """The name of the preference."""
    Values: list[str]
    """
            The list of values.
            

            Even though the value can be of a type different than string, the conversion to string
            should be made using the Property class provided
            by the SOA framework.
            """

class SetPreferencesAtLocationsIn:
    """
    Contains the preference definition, values and the location where to set the information.
    """
    def __init__(self, ) -> None: ...
    Location: PreferenceLocation
    """
            Structure defining where the preferences are to be set.
            

            The intent is that only the system administrator should create a preference. However,
            this could be needed from non-directly-related user interactions. Therefore, the
            decision to make a call to this operation is delegated to its caller.
            """
    PreferenceInputs: SetPreferences2In
    """Structure that contains the preference name, definition and values."""

class SetPreferencesDefinitionIn:
    """
    
            Structure containing a PreferenceDefinition
            structure and a list of strings representing the preference values at the site level.
            
    """
    def __init__(self, ) -> None: ...
    Definition: PreferenceDefinition
    """A structure holding the preference definition (possibly simplified)."""
    Values: list[str]
    """
            The list of values at the site level.
            
            Even though the values can be of a type different than string, they should be converted
            to a string through the use of the Property
            class from the SOA framework.
            
"""

class PreferenceManagement:
    """
    Interface PreferenceManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def DeletePreferenceDefinitions(self, PreferenceNames: list[str], DeleteAllCustomDefinitions: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Deletes the definition and all value instances of the specified preferences.
             
             Since preferences will not be differentiated as Custom or COTS going forward, the
             input parameter deleteAllCustomDefinitions will not be used when performing this
             operation.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param PreferenceNames: 
                         The list of names for the preference definitions to delete.
             
        :param DeleteAllCustomDefinitions: 
                         Not used.
             
        :return: 
        """
        ...
    def DeletePreferencesAtLocations(self, DeletePreferencesAtLocationIn: list[PreferencesAtLocationIn]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Deletes the given preference instances at the specified location only.
             
             This operation takes a list of PreferencesAtLocationIn
             structures representing the preferences to delete and the location.
             
             The location is a PreferenceLocation structure,
             which contains 2 mutually exclusive parameters:
             
             1. The location parameter, for which values can be for this specific operation:
             

"Site": The preference will be deleted from current site location.
             
"Group": The preference will be deleted for the group of the
             logged-in user.
             
"Role": The preference will be deleted for the role of the
             logged-in user.
             
"User": The preference will be deleted for the logged-in user.
             


             2. The object parameter, which represents the User, Role or Group
             where to delete the values. This is to be used when the target is for the non-logged-in
             user.
             

Use Cases:

             A preference instance is present at the user level, and it needs to be removed.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param DeletePreferencesAtLocationIn: 
                         A list of preferences at a given location.
             
        :return: 
        """
        ...
    def GetPreferences(self, PreferenceNames: list[str], IncludePreferenceDescriptions: bool) -> GetPreferencesResponse:
        """    
             Retrieves the values for the preferences specified in the list of names, as seen
             by the current logged-in user, based on current application context. If there are
             no values in current application context, values are retrieved from default application
             context if exists.
             
             If the list is empty or its first value is equal to "*", all the preferences as seen
             by the logged-in user will be returned (not only the preference instances created
             by the logged-in user).
             

Use Cases:

             Retrieving the value for a series of preferences.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param PreferenceNames: 
                         If the list is empty or its first value is equal to "*", all the preferences visible
                         by the logged-in user will be returned (not only the preference instances created
                         by the logged-in user).
             
        :param IncludePreferenceDescriptions: 
                         Decides if the preference descriptions will be included in the response. Valid values
                         are true (descriptions are added) or false (no description). This offers flexibility
                         to decide the important information to the caller and reduce the size of the response
                         payload.
             
        :return: 
        """
        ...
    def GetPreferencesAtLocations(self, GetPreferenceAtLocationIn: list[PreferencesAtLocationIn], IncludePreferenceDescriptions: bool) -> GetPreferencesAtLocationsResponse:
        """    
             Retrieves the values for the specified preferences and locations.The input structure
             contains:
             
A vector preference names. If the list is empty or its first element is "*",
             all the preferences for the specified locations (and only for preference instances
             at this location) are being returned.
             
A PreferenceLocation  structure, which
             contains 2 mutually exclusive parameters:The location parameter, for which
             values can be for this specific operation:"Site": The
             preference will be retrieved either as overwritten or as an out-of-the-box (OOTB)
             value (whichever gives a value first).
             
"Group": The preference will be retrieved for the group of the logged-in
             user.
             
"Role": The preference will be retrieved for the role of the logged-in
             user.
             
"User": The preference will be retrieved for the logged-in user.
             


 The object parameter, which represents the User, Role
             or Group where to retrieve the values. This is to be used when the target
             is for the non-logged-in user.
             





Use Cases:

             1. The logged-in user needs to know the preference value given at her/his Role or
             Group level.
             
             2. The logged-in user needs to know the preference value given by another user, or
             a Role/Group than hers/his.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param GetPreferenceAtLocationIn: 
                         The desired list of preferences for a given location.
             
        :param IncludePreferenceDescriptions: 
                         Decides if the preference descriptions will be included in the response. Valid values
                         are true (descriptions are added) or false (no description). This offers flexibility
                         to decide the important information to the caller and reduce the size of the response
                         payload.
             
        :return: 
        """
        ...
    def ImportPreferencesAtLocationDryRun(self, ImportPreferences: ImportPreferencesAtLocationDryRunIn) -> ImportPreferencesAtLocationDryRunResponse:
        """    
             Pretends to import the preferences from the input file into the specified location.
             On the contrary to the import operation, the dry run operates on one location at
             a time. The objective is to gather information on what would be the final result
             for proceeding with the real import operation.  This operation takes a vector of
             structure representing the preferences and the location where to import. The valid
             values for the location parameter in the PreferenceLocation structure are: Site,
             Group, Role, User. The Site value means that the preference will be imported for
             the entire organization. Group or Role means that the value will be imported for
             the Group or Role of the current logged-in user. It is also possible to import for
             the non-current user.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param ImportPreferences: 
                         A structure that contains all the parameters for the import operation
             
        :return: 
        """
        ...
    def ImportPreferencesAtLocations(self, ImportPreferenceIn: ImportPreferencesAtLocationsIn) -> PreferenceResponseWithFileTicket:
        """    
             Imports the preferences from the input file into the specified locations.  This operation
             takes a vector of structure representing the preferences and the location where to
             import. The valid values for the location parameter in the PreferenceLocation structure
             are: Site, Group, Role, User. The Site value means that the preference will be imported
             for the entire organization. Group or Role means that the value will be imported
             for the Group or Role of the current logged-in user. It is also possible to import
             for the non-current user.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param ImportPreferenceIn: 
                         A structure that contains all the parameters for the import operation
             
        :return: A <font face="courier" height="10">PreferenceResponseWithFileTicket</font>
             structure, which contains:<ol><li>A file ticket to the report file (generated
             by the import operation) in the transient volume uploaded by the client. If the operation
             is called to import at several locations, all the report informations are gathered
             in the same file. </li><li>A ServiceData structure, which contains errors
             at indexes where errors have occurred. The following partial errors will be returned
             at the same index as the input structure:<ul type="circle"><li>1700:
             If the preference does not exist. </li><li>1725: If the logged-in user
             does not have the requested permission to carry-out the operation. </li><li>1751:
             If the specified object information does not correspond to any <b>User</b>,
             <b>Role</b> or <b>Group</b>. </li><li>1752: If
             both an object and a location are specified for an entry. </li><li>1753:
             if the specified location is invalid. </li></ol>
        """
        ...
    def RemoveStalePreferenceInstancesAtLocations(self, Locations: list[PreferenceLocation]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Since the preference manager utility has a cleanup mode that does the same thing
             as removeStalePreferenceInstancesAtLocations-_2012_09-PreferenceManagementService.
             There is no need of a SOA operation to achieve this.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param Locations: 
                         The locations where to remove the stale preference instances.
             
        :return: structure, which will not contain
             any error.
        """
        ...
    def SetPreferences2(self, PreferenceInput: list[SetPreferences2In]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Allows the logged-in user to set the values for the given preferences for the logged-in
             user.
             
             Values can only be given to preferences already defined in the system and for which
             the protection scope allows the user to give a value. Otherwise, the operation will
             return an error for this preference.
             
             Preference name and values are specified in input structure SetPreferences2In.
             


Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param PreferenceInput: 
                         A list of preference names and values.
             
        :return: 
        """
        ...
    def SetPreferencesAtLocations(self, SetPreferenceIn: list[SetPreferencesAtLocationsIn]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Sets the values for the specified preferences and locations. The input
             PreferenceLocation structure (within the
             SetPreferencesAtLocationsIn structure) contains
             2 mutually exclusive parameters: The location parameter, for which values
             can be for this specific operation: "Site": The preference
             will be set for the entire organization.
             
"Group": the preference will be set for the group of the logged-in user.
             
"Role": The preference will be set for the role of the logged-in user.
             
"User": The preference will be set for the logged-in user.
             


 The object parameter, which represents the User, Role or Group
             where to set the values. This is to be used when the target is for the non-logged-in
             user. Note that the caller must have permission to set the preference values for
             the specified object.
             



Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param SetPreferenceIn: 
                         A list of preference definition, values and the location where to set the information.
             
        :return: 
        """
        ...
    def SetPreferencesDefinition(self, PreferenceInput: list[SetPreferencesDefinitionIn]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Allows system administrators to create the definitions for new preferences, or to
             modify existing preference definitions. If the preferences do not exist, it sets
             the definitions and values for the specified preferences. If the preferences already
             exist (i.e. they have been defined already), it modifies them.
             

             This is a system administrator level operation. The intent is that only the system
             administrator should create a preference. However, this could be needed from non-directly-related
             user interactions. Therefore, the decision to make a call to this operation is delegated
             to its caller. This operation takes a list of SetPreferencesDefinitionIn
             structures, which contains a PreferenceDefinition
             structure. This structure can be simplified in case of preference modifications.
             

             Its parameters are:
             


category: The category where the preference is stored. If
             the input string is empty, the parameter will not be taken into account. However,
             in case the preference has not been created yet, it will be assumed that the preference
             will go under the "General" category. If the string is not empty, and if the category
             does not exists in the system already, new category would be created and the preference
             would go under this category.  
             




description: The textual explanation of what the preference
             does. If the input string is empty, the parameter will not be taken into account. 
             




type: The preference type. Valid values are:
             


                                     0:
             String preference.
             
                                     1:
             Logical preference.
             
                                     2:
             Integer preference.
             
                                     3:
             Double preference.
             
                                     4:
             Date preference.
             
                             If
             the preference does not exist, this piece of information will be needed. If the preference
             exists and if the value is provided and if a preference instance already exist with
             the old type and the conversion from the old type to the new one is not possible
             and an error would be returned. 
             


protectionScope: The level at which the preference is protected.
             Valid values are:                        
             


                                     "User":
             All users can provide a value for the preference.
             
                                     "Role":
             Only system and group administrators can provide a value.
             
                                     "Group":
             Only system and group administrators can provide a value.
             
                                     "Site":
             Only system administrators can provide a value.
             
                                     "System":
             Only system administrators can provide a value. Furthermore, the protection scope
             cannot be changed from then on. If the preference does not exist, this information
             is mandatory. If the preference exists and the protection scope string is empty,
             the parameter will not be taken into account. If the  preference exists and the protection
             scope string is not empty, the code will consider this to be a modification. 
             

isEnvEnabled: Status if the preference value can be set through
             an environment variable, in which case it will come from that location first. This
             piece of information will always be taken into consideration.
             




isOOTBPreference: Not used for this operation.
             



Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param PreferenceInput: 
                         A list of preference definitions.
             
        :return: 
        """
        ...

