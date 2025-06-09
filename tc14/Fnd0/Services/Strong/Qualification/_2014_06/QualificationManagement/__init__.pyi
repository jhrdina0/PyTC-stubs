import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AssignUserQualificationInfo:
    """
    
            List of  AssignUserQualificationInfo structures, each containing information required
            for assigning a Fnd0Qualification object to a Teamcenter User.
            

    """
    def __init__(self, ) -> None: ...
    User: Teamcenter.Soa.Client.Model.Strong.User
    """Teamcenter User object to assign the qualification."""
    Qualification: Teamcenter.Soa.Client.Model.Strong.Fnd0Qualification
    """Fnd0Qualification object to assign user qualification."""
    LevelName: str
    """Name of the Qualification level."""
    EffectiveDate: System.DateTime
    """EffectiveDate for the Qualification to assign."""
    ExpiryDate: System.DateTime
    """Expiry Date for for the Qualification to assign."""

class ManageQualificationInfo:
    """
    Information required to create Fnd0Qualification objects.
    """
    def __init__(self, ) -> None: ...
    QualificationName: str
    """A unique name for the Fnd0Qualification."""
    Description: str
    """Description of the Fnd0Qualification."""
    IsExpiryDateRequired: bool
    """
            Indicates whether effective and expiry dates are required for the Qualification.
            This is used to decide whether effective and expiry dates are required while assigning
            the Fnd0Quailification to a Teamcenter User.
            """
    QualificationLevels: list[str]
    """
            The levels are defined on Fnd0Qualification object as ordered list of strings.
            Levels signifies the ranking amongst the user once the Fnd0Qualification is
            assigned to User with a level.  Levels are defined by administrator. Valid values
            for level can be any string. For example "Advanced" , "Beginner" etc.
            """

class QualificationLevelInfo:
    """
    
            List of QualificationLevelInfo structures containing the Fnd0Qualification
            object and the level to remove.
            
    """
    def __init__(self, ) -> None: ...
    Qualification: Teamcenter.Soa.Client.Model.Strong.Fnd0Qualification
    """
Fnd0Qualification object to remove qualification level.
            

"""
    LevelName: str
    """Name of Level to remove."""

class RemoveUserQualificationInfo:
    """
    
            List of RemoveUserQualificationInfo structures, each containing the User and
            the Fnd0Qualification to be removed.
            
    """
    def __init__(self, ) -> None: ...
    User: Teamcenter.Soa.Client.Model.Strong.User
    """User Object to remove qualification from the user"""
    Qualification: Teamcenter.Soa.Client.Model.Strong.Fnd0Qualification
    """Fnd0Qualification object to remove user qualification from the user."""

class UpdateQualificationInfo:
    """
    Information required to update Fnd0Qualification objects.
    """
    def __init__(self, ) -> None: ...
    Qualification: Teamcenter.Soa.Client.Model.Strong.Fnd0Qualification
    """Fnd0Qualification object to be updated."""
    QualificationInfo: ManageQualificationInfo
    """Qualification information to be updated."""

class QualificationManagement:
    """
    Interface QualificationManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AppendQualificationLevel(self, QualificationLevelInfo: list[QualificationLevelInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Appends a level to the ordered list of Fnd0Qualification levels.
             

Teamcenter Component:

             Qualification - Teamcenter SOA component for Services related to Qualification Object.
             
        :param QualificationLevelInfo: 
                         List of qualificationLevelInfo structures, each containing the <b>Fnd0Qualification</b>
                         object and the level to append.
             
        :return: 
        """
        ...
    def AssignUserQualification(self, AssignUserQualificationInfo: list[AssignUserQualificationInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Assigns a Fnd0Qualification object to a Teamcenter User. Each AssignUserQualificationInfo
             structure in the input list contains information required to assign a Fnd0Qualification
             object to a Teamcenter User. A Fnd0UserHasQual relation object will
             be created on successful assignment of Fnd0Qualification to a User.
             

Teamcenter Component:

             Qualification - Teamcenter SOA component for Services related to Qualification Object.
             
        :param AssignUserQualificationInfo: 
                         List of  AssignUserQualificationInfo structures, each containing information required
                         for assigning a <b>Fnd0Qualification</b> object to a Teamcenter User.
             
        :return: 
        """
        ...
    def CreateQualification(self, QualificationInfo: list[ManageQualificationInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Creates a list of Fnd0Qualification objects. A single Fnd0Qualification
             object is created for each ManageQualificationInfo structure in the list.
             

Teamcenter Component:

             Qualification - Teamcenter SOA component for Services related to Qualification Object.
             
        :param QualificationInfo: 
                         Information required to create <b>Fnd0Qualification</b> objects.
             
        :return: 
        """
        ...
    def RemoveQualificationLevel(self, QualificationLevelInfo: list[QualificationLevelInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Removes a level from the list of Qualification levels.
             

Teamcenter Component:

             Qualification - Teamcenter SOA component for Services related to Qualification Object.
             
        :param QualificationLevelInfo: 
                         List<b> </b>of <b>QualificationLevelInfo</b> structures containing the <b>Fnd0Qualification</b>
                         object and the level to remove.
             
        :return: 
        """
        ...
    def RemoveUserQualification(self, RemoveUserQualificationInfo: list[RemoveUserQualificationInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Removes a Fnd0Qualification object that is assigned to a Teamcenter User
             by deleting the Fnd0UserHasQual relation object that relates the User and
             the Fnd0Qualification.
             

Teamcenter Component:

             Qualification - Teamcenter SOA component for Services related to Qualification Object.
             
        :param RemoveUserQualificationInfo: 
                         List of RemoveUserQualificationInfo structures, each containing the User and the
                         <b>Fnd0Qualification </b>to be removed.
             
        :return: 
        """
        ...
    def UpdateQualification(self, UpdateQualificationInfo: list[UpdateQualificationInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation updates a list of Fnd0Qualification objects.
             

Teamcenter Component:

             Qualification - Teamcenter SOA component for Services related to Qualification Object.
             
        :param UpdateQualificationInfo: 
                         Information required to update <b>Fnd0Qualification</b> objects. Each UpdateQualificationInfo
                         structure contains the <b>Fnd0Qualification</b> object to update and the ManageQualificationInfo
                         structure providing the information to be updated.
             
        :return: 
        """
        ...

