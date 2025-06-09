import Teamcenter.Soa.Client.Model
import typing

class ConnectResponse:
    """
    Indicates number of licenses avaliable and any failure
    """
    def __init__(self, ) -> None: ...
    OutputVal: int
    """The number of available licenses for the specified featureKey parameter."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData structure contains these potential error numbers:
            
                  214401: The initialization of the license module has failed.
            
                  214402: Detaching the requested license has failed.
            
                  214403: The deallocation of the license feature key has
            failed.
            
                  214404: Checking of the license feature key has failed.
            
                  214405: The allocation of the license feature key has failed.
            
                  214406: The module is not purchased.
            
                  214407: The passed in action is invalid.
            """

class FavoritesContainer:
    """
    
            A Favorites object that contains one or more subordinate favorite containers and/or
            Teamcenter objects supporting a hierarchical favorites structure.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The identifier that relates a set of favorites container information to reported
            errors.
            """
    Id: str
    """
            The container identifier that is unique for all favorites. The identifier format
            is four numeric characters with leading zeros.
            """
    Type: str
    """The container type."""
    DisplayName: str
    """The display name used for the favorites container."""
    ParentId: str
    """The parent container identifier.  An identifier of 0000 indicates the root container."""

class FavoritesList:
    """
    
            A hierarchical favorites tree structure list that contains all the favorites containers
            and favorites objects for the current session user. The favorites section can be
            populated only if FavoritesSection is passed
            as a key in the input map to this API.
            
    """
    def __init__(self, ) -> None: ...
    Containers: list[FavoritesContainer]
    """List of favorite containers for the current session user."""
    Objects: list[FavoritesObject]
    """List of favorite objects for the current session user."""

class FavoritesInfo:
    """
    Input information for setting the favorites for the session user.
    """
    def __init__(self, ) -> None: ...
    CurFavorites: FavoritesList
    """
            The client copy of the current favorites containers and objects. If current containers
            and objects are specified, they must match the current saved favorites exactly for
            the specified new favorites to be saved.  If curFavorites
            does not match the current saved favorites in Teamcenter, newFavorites
            will not be saved.  This provides the client the ability to protect against simultaneous
            updates by two clients.
            """
    NewFavorites: FavoritesList
    """
            The new favorites containers and objects to be saved.  The containers and objects
            specified in newFavorites make up the entire
            list of favorites.  If no new containers and no new objects are specified, the saved
            favorites for the session user will be cleared.
            """

class FavoritesObject:
    """
    A Teamcenter favorites object.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """The identifier that relates a set of favorites object information to reported errors."""
    ObjectTag: Teamcenter.Soa.Client.Model.ModelObject
    """The favorite object."""
    DisplayName: str
    """The display name used for the favorites object."""
    ParentId: str
    """The parent container identifier.  An identifier of 0000 indicates the root container."""

class FavoritesResponse:
    """
    
            The set of Favorites containers and Favorites objects that define a hierarchical
            Favorites structure for the current session user.
            
    """
    def __init__(self, ) -> None: ...
    Output: FavoritesList
    """List of favorite containers and favorite objects for the current session user."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The service data. This operation will populate the Service Data plain objects list
            with the Favorite containers and objects.
            """

class Session:
    """
    Interface Session
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def Connect(self, FeatureKey: str, Action: str) -> ConnectResponse:
        """    
             Performs Teamcenter Flexlm license related operations, depending on the input parameters.
             

             The low level actions are:
             

             1.  ILM__init_module: Initializes the license module (if it has not already been
             initialized).
             
             2.  ILM__leave_module: Deallocates a license of the given module. If the user had
             N free licenses for this module, (N plus one) will be left after this call.
             
             3.  ILM__check_module: Checks to see if the user has bought the specified module
             and returns the number of purchased licenses.
             
             4.  ILM__enter_module: Allocates one license of the given module. If the user has
             bought N licenses for this module, (N minus one) will be left after this call.
             
             5.  ILM__exit_module: Leaves the module.
             


Teamcenter Component:

             Licensing - Provides the capability to assign and monitor licenses such that the
             users (an individual; a system; a module etc.) of teamcenter can be limited to use
             the capabilities that they have privileges for
             
        :param FeatureKey: 
                         A string corresponding to the product as listed in the license file (e.g. teamcenter_author)
             
        :param Action: 

        :return: contains a ServiceData (ConnectResponse.serviceData), and number of licenses avaliable.
             Any failure will be returned via ServiceData with error message.
        """
        ...
    def GetFavorites(self) -> FavoritesResponse:
        """    
             This operation retrieves the saved Favorites containers and Favorites objects for
             the current session user.  You can use Favorites to track containers and objects
             you access frequently, such as folders, parts or forms.
             

             If errors are encountered, partial results are returned. Partial errors are returned
             with client IDs reflecting the index value of the saved Favorite. A service exception
             is thrown if an error is encountered that is not related to a specific Favorite container
             or Favorite object.
             

             Any Teamcenter object that is returned as a Favorite object is added to ServiceData plain objects.  For example, if an item exists in
             the list of Favorite objects, the object tag value for that item will be returned
             in the ServiceData list of plain objects.
             


Use Cases:

             User logs in and selects their saved Favorites.
             

             The Favorites view in the client application is populated with the Favorites containers
             and objects returned from this operation.
             


Dependencies:

             setFavorites
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :return: 
        """
        ...
    def SetFavorites(self, Input: FavoritesInfo) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation saves new favorite containers and favorite objects for the current
             session user.
             

             Any partial errors encountered during this operation are returned using the clientID specified by the caller. A service exception
             is thrown if an error is encountered that is not related to a specific favorite container
             or favorite object.  You can use favorites to track containers and objects you access
             frequently, such as folders, parts or forms.  For example, the Newstuff folder could
             be added as a container to the list of favorites.
             


Use Cases:

             User saves a container to their favorites list.
             

             For this operation, the list of all current favorites for the user and the list containing
             the container the user desires to add are supplied as input and the new container
             is added to the list of saved favorites in Teamcenter.
             


Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Input: 
                         The information required to establish a new set of saved favorites for the current
                         session user.
             
        :return: 
        """
        ...

