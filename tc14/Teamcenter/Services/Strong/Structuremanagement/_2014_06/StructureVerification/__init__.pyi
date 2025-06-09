import Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ACFavoriteInfo:
    """
    
Accountability check settings which can be used to run accountability check or
to
load the settings in the accountability check dialog. The following partial
errors
may be returned in ServiceData element.

Â Â Â Â 204045Â Â Â Â Â Â Â Â Input
dataset UID is not a valid dataset of accountability check favorite.

Â Â Â Â 204047Â Â Â Â Â Â Â Â The
accountability check favorites XML is invalid. It may contain the entries that Â
Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â cannot
be evaluated by XML parser.

    """
    def __init__(self, ) -> None: ...
    AccSettings: Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.ACInput
    """Accountability check settings."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Teamcenter service data."""

class ACFavoritesInput:
    """
    The required parameters for the manageACFavorites method.
    """
    def __init__(self, ) -> None: ...
    AccSettings: Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.ACInput
    """
            Accountability check settings to save. May have empty values for update and delete
            actions.
            """
    Name: str
    """
            Name of the dataset containing accountability check settings of the favorite.  May
            have empty string for update and delete actions.
            """
    Description: str
    """
            Description of the favorite that is being created or updated. May have empty string
            for update and delete actions.
            """
    DatasetUID: str
    """
            UID of the dataset to be updated or deleted . If the value is empty a new dataset
            is created.
            """
    Action: str
    """
            Specifies the action to be performed on the dataset. Possible values are "create",
            "update" or "delete".
            """

class ACFavoritesResponse:
    """
    
The created or updated DataSet. The following partial errors may be returned:

Â Â Â Â 204042Â Â Â Â Â Â Â Â Input
dataset uid is not a valid dataset to update the accountability check favorites.

Â Â Â Â 204043Â Â Â Â Â Â Â Â No
transient volume directory, cannot create favorites xml file.

Â Â Â Â 204044Â Â Â Â Â Â Â Â Invalid
accountability check favorites xml.

Â Â Â Â 204045Â Â Â Â Â Â Â Â Dataset
missing named reference file.

Â Â Â Â 204046Â Â Â Â Â Â Â Â Parser
unable to parse xml named reference file.

Â Â Â Â 204047Â Â Â Â Â Â Â Â Dataset
is not text type.

    """
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Dataset containing the accountability check settings."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Teamcenter service data."""

class StructureVerification:
    """
    Interface StructureVerification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetACFavorite(self, DatasetUID: str) -> ACFavoriteInfo:
        """    
             This operation returns accountability check settings for a given dataset UID of accountability
             check favorite. These settings from a favorite are usually required to populate the
             accountability check dialog whenever a favorite is loaded or when accountability
             check is run.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param DatasetUID: 
                         UID of the Dataset that has the accountability check settings for the favorite.
             
        :return: 
        """
        ...
    def ManageACFavorites(self, Input: ACFavoritesInput) -> ACFavoritesResponse:
        """    
             This operation creates, updates or deletes an accountability check favorite. Internally
             the dataset representing the accountablity check favorite is created, updated or
             deleted.
             
             To create accountability check favorite, the parameters account settings, name, description
             and action are mandatory.
             
             To update or delete accountability check favorite, the parameters action and datasetUID
             are mandatory.
             


Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         The required parameters for the manageACFavorites method.
             
        :return: Â Â Â Â 204047Â Â Â Â Â Â Â Â Dataset
             is not text type.
        """
        ...

