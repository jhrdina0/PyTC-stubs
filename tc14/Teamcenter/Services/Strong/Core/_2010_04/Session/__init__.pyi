import System
import System.Collections
import Teamcenter.Services.Strong.Core._2007_01.Session
import Teamcenter.Services.Strong.Core._2008_03.Session
import Teamcenter.Soa.Client.Model
import typing

class GetShortcutsResponse:
    """
    
            A structure contains Favorites hierarchy and map of LHNSectionComponent given section
            names.
            
    """
    def __init__(self, ) -> None: ...
    Favorites: Teamcenter.Services.Strong.Core._2008_03.Session.FavoritesList
    """
            A hierarchical Favorites tree structure list that contains all the favorites containers
            and favorites objects for the current session user. The Favorites section can be
            populated only if FavoritesSection is passed as a key in the input map to this API.
            """
    Shortcuts: System.Collections.Hashtable
    """
            A map structure that includes the given section name and corresponding content of
            the section. The key is the name of the section and the value is the LHNSectionComponent
            structure, which has a Teamcenter object and a nonTeamcenter object . The preferred
            keys allowed in this map are MyFavorites, HistoryList, QuickLinksSection,  MyQuicklinkSection
            etc.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            ServiceData contains any failures and Teamcenter objects  wrapped in LHNSecitonComponents
            and default properties. The following errors may be encountered:
            
            1700 (error code):  The preference cannot be found.
            
            515024 ( error code): The given tag does not exist in the database or is not a persistent
            object tag.
            """

class LHNNonTcObjectSectionComponent:
    """
    
            The sections in the left hand navigation can contain either Teamcenter objects or
            non-Teamcenter  objects. Sections which contain Teamcenter objects are 'Open Items',
            'History', etc and the sections which  contain non-Teamcenter bjects are 'I Want
            To' section. This structure in turn contains the LHNSectionComponentDetails which
            maintains additional information pertaining to the object.  Example: Consider that
            the 'I Want To' section in the left hand navigation contains the command 'Create
            an  Item'. This structure would contain the below details in the LHNSectionComponentDetails.
            Key = ActionName, Value = newItemAction Key = DisplayName, Value = Create an Item
            Key = CommandID, Value = com.teamcenter.rac.newItem  Consider that the 'QuickLinkSection'
            section in the left hand navigation contains the command 'like  a 'home folder'
            in quick links. key = QuickLinkId
            
    """
    def __init__(self, ) -> None: ...
    NonTcObjects: System.Collections.Hashtable
    """Non Tc Objects like Home, folder etc"""

class LHNSectionComponents:
    """
    
            The purpose of this structure is to give a single name to 'LHNNonTcObjectSectionComponentMap'
            and  'LHNTcObjectSectionComponentMap' which is section component. Each section component
            is puted into   LHNSectionComponentsMap.  LHNNonTcObjectSectionComponentMap: It is
            a map for nontcobject , whose key is 'int' using for  placeHolder and value are NonTcObjectSection.
            LHNTcObjectSectionComponentMap key is for placeholder and value as tccomponent object.
            
    """
    def __init__(self, ) -> None: ...
    NonTcObjects: System.Collections.Hashtable
    """nonTcObjects"""
    TcObjects: System.Collections.Hashtable
    """tcObjects"""

class LHNTcObjectSectionComponent:
    """
    
            The purpose of this structure is to represents the Teamcenter object details, Which
            is get use in  the Left Hand Navigation pane of the clients. Which is either a tcobject
            or non tcobject.  Teamcenter::BusinessObject  This is a TcComponent which have all
            the bussiness property of   teamcenter object. e.g Items in History section, Items
            in OpenItemSection etc.               LHNSectionComponentDetails It must contain
            the detail information about the nonTcObject at which  place we have to insert and
            what are the action name and display name  associated with it. e.g LHNSectionComponentDetails('Action
            Name',  newItemAction );     LHNSectionComponentDetails('Display Name',  Create an
            Item );
            
    """
    def __init__(self, ) -> None: ...
    TcObject: Teamcenter.Soa.Client.Model.ModelObject
    """Specifies the Teamcenter object"""
    Details: System.Collections.Hashtable
    """Additional details of the section component."""

class MultiPreferenceResponse2:
    """
    The structure used to get the returned preference
    """
    def __init__(self, ) -> None: ...
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """The successful Object ids, partial errors and failures"""
    Preferences: list[ReturnedPreferences2]
    """List of ReturnedPreferences2 Object"""

class ReturnedPreferences2:
    """
    This is the structure which is used to define the information for one preference.
    """
    def __init__(self, ) -> None: ...
    Scope: str
    """The scope of the preference, "all", "site", "user", "group", or "role"."""
    Category: str
    """The variable to hold the category name"""
    Description: str
    """The variable to hold the description"""
    PrefType: int
    """Preference Type"""
    IsArray: bool
    """Preference Array"""
    IsDisabled: bool
    """Is the preference disabled"""
    Values: list[str]
    """The value of the preference"""
    Name: str
    """The name of the preference"""

class Session:
    """
    Interface Session
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPreferences2(self, PreferenceNames: list[Teamcenter.Services.Strong.Core._2007_01.Session.ScopedPreferenceNames]) -> MultiPreferenceResponse2:
        """    
             This operation takes an input structure which contains a scope value and vector of
             preference names. The return type of this operation is the MultiPreferencesResponse2
             structure whose elements are the ServiceData and the vector of ReturnedPreferences2
             structure.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param PreferenceNames: 
                         The input structure, the object of which would ahve 2 input parameters of scope and
                         the preference names.
             
        :return: This structure is used to return Preference
        """
        ...
    def GetShortcuts(self, ShortcutInputs: System.Collections.Hashtable) -> GetShortcutsResponse:
        """    
             This operation gets the sections and corresponding content in Left Hand Navigation
             task pane given the section name and the corresponding preference name for the current
             session user. The preference name is the key to look up section content stored in
             preference.    In the rich client, the LHN sections are Quick
             Links, Open Items, History, Favorites and I Want To. The user can organize Teamcenter
             data in these sections during runtime, which is persisted in the preference. The
             Quick Links section provides a quick access point to the user`s home folder, work
             list, favorite Web links, projects, saved searches, and View Markup. The Open Items
             section lists Teamcenter components currently opened in the active perspective. The
             History section lists Teamcenter components opened before, but currently closed.
             The Favorites section contains the Favorites container and Teamcenter components
             the user added there for quick access. The I Want To section contains commands configured
             by default or configured by the user.
             

Use Cases:

             The user logs in to the rich client and retrieves Quick Links, Open Items, History,
             Favorites and I Want To task pane section for Left Hand Navigation.
             

Teamcenter Component:

             RAC Views Viewer - Rich client views and viewer framework components extending from
             eclipse jface viewer and view extension.
             
        :param ShortcutInputs: 
                         A map of the key representing the  section name in the left hand navigation and the
                         value representing the preference name that needs to be looked up to get the content.
                         For example,  Key =QuickLinksSection, Value = MyTeamcenterQuicklinksection;  Key
                         = FavoritesSection, value= My Favorites . Valid keys in the map are QuickLinksSection,
                         HistorySection, FavoritesSection, IWantToSection, OpenItemsSection. Valid values
                         for these keys in the map could be MyFavorites, HistoryList, QuickLinksSection, MyQuicklinkSection,
                         OpenItemSection, etc.
             
        :return: Â Â Â Â 515024 (error code): The given tag does not exist in the
             database or is not a persistent object tag.
        """
        ...

