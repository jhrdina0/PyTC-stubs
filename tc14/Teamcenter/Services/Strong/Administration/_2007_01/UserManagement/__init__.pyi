import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DisciplineObject:
    """
    
            This structure holds initial property values for a new discipline object and the
            corresponding client ID.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify returned CreateDisciplinesOutput
            element and partial errors associated with the DisciplineObject input.
            """
    Name: str
    """The name of the new Discipline object to be created."""
    Description: str
    """The description text of the new Discipline object to be created."""
    DefaultRate: float
    """The default rate property of the new Discipline object to be created."""
    Levels: list[DisciplineLevel]
    """The list of Discipline level."""
    Users: list[DisciplineUser]
    """
            The list of DisciplineUser objects which specifies user members for the new Discipline
            to be created.
            """

class CreateDisciplinesIn:
    """
    
            This structure holds a DisciplineObject object which specifies the values of a new
            Discipline object. as well as the parent group for the new discipline.
            
    """
    def __init__(self, ) -> None: ...
    Discipline: DisciplineObject
    """The object with initial data for the creation of a new Discipline object."""
    Group: Teamcenter.Soa.Client.Model.Strong.Group
    """The parent group of the new Discipline object."""
    Role: Teamcenter.Soa.Client.Model.Strong.Role
    """
            The role for the Discipline object. However it is not currently supported
            by this operation.
            """

class CreateDisciplinesOutput:
    """
    
            This structure holds the newly created Discipline object and corresponding
            client ID.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifying string from the source DisciplineObject."""
    Discipline: Teamcenter.Soa.Client.Model.Strong.Discipline
    """The new Discipline object created in this operation."""

class CreateDisciplinesResponse:
    """
    This structure holds a list of newly created Discipline objects.
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateDisciplinesOutput]
    """List of CreateDisciplinesOutput objects, one for each CreateDisciplinesIn object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The object which holds the partial errors that occurred during creation of new Discipline
            objects with all newly created discipline object in its created object list.
            """

class DisciplineLevel:
    """
    Struct containing the discipline level name and number attribute information.
    """
    def __init__(self, ) -> None: ...
    LevelName: str
    """levelName"""
    LevelNumber: int
    """levelNumber"""

class DisciplineUser:
    """
    This structure  holds a user and its discipline level name.
    """
    def __init__(self, ) -> None: ...
    User: Teamcenter.Soa.Client.Model.Strong.User
    """The Teamcenter User object to be added to the new discipline."""
    LevelName: str
    """Not supported."""

class UserManagement:
    """
    Interface UserManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateDisciplines(self, Disciplines: list[CreateDisciplinesIn]) -> CreateDisciplinesResponse:
        """    
             This operation creates a list of new Discipline objects based on the list
             of CreateDisciplineIn objects. If  parent group is specified in the CreateDisciplinesIn
             object, the discipline objects would be added into the group. This operation requires
             system administration or group administration privilege.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param Disciplines: 
                         A list of CreateDisciplinesIn objects to specify initial data for the new discipline
                         objects and parent group. A new discipline object is created for each CreateDisciplinesIn
                         object in the list.
             
        :return: .
        """
        ...

