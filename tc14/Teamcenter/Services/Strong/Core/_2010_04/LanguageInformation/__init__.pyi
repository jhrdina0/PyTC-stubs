import Teamcenter.Soa.Client.Model
import typing

class FullTranslationStatus:
    """
    
            Fully defines a translation status: its associated enumeration, display name and
            description.
            
    """
    def __init__(self, ) -> None: ...
    Status: str
    """TranslationStatus associated with the status"""
    StatusName: str
    """Display name of the status"""
    StatusDescription: str
    """Description of the status"""

class Language:
    """
    Contains information about a language
    """
    def __init__(self, ) -> None: ...
    LanguageCode: str
    """
            The name of the desired locale. The valid locale name should be in the format as
            outlined in the Java Standard Language (i.e. en_US for English, United States).
            """
    LanguageName: str
    """The localized language name"""

class LanguageResponse:
    """
    Information about the list of languages
    """
    def __init__(self, ) -> None: ...
    LanguageList: list[Language]
    """An ordered list of languages"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Any partial errors that may occur when filling this request"""

class TranslationStatusResponse:
    """
    Response associated to some LanguageInformation operation calls
    """
    def __init__(self, ) -> None: ...
    FullTranslationStatuses: list[FullTranslationStatus]
    """List of all the full translation statuses"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData."""

class LanguageInformation:
    """
    Interface LanguageInformation
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAllTranslationStatuses(self) -> TranslationStatusResponse:
        """    
             Retrieves the full set of translation statuses: their enumeration, localized name
             and description.
             
             Currently, the translation statuses in the Teamcenter system includes: "Master",
             "Approved", "Pending", "In-Review", and "Invalid"
             


Teamcenter Component:

             Core Model L10N framework - The framework to provide a user interface in the locale
             of users as well as manage the product information (metadata, operation data and
             file content) in multiple languages.
             
        :return: 
        """
        ...
    def GetLanguagesList(self, Scenario: str) -> LanguageResponse:
        """    
             Retrieves a list of languages according to different scenarios as specified in the
             input parameter.
             
             All the returned language names are in the Java-standard format.
             

Teamcenter Component:

             Core Model L10N framework - The framework to provide a user interface in the locale
             of users as well as manage the product information (metadata, operation data and
             file content) in multiple languages.
             
        :param Scenario: 
<ul>
<li type="disc">"<i>supportedLanguages</i>": To retrieve all the languages supported
                         by the system.
                         </li>
<li type="disc">"<i>localizationLanguages</i>": To retrieve all languages supported
                         by the system and declared as usable for property value localization in the both
                         BMIDE Global Constant "<font face="courier" height="10">Fnd0SelectedLocales</font>"
                         and "<font face="courier" height="10">SiteMasterLocale</font>".
                         </li>
</ul>

        :return: 
        """
        ...

