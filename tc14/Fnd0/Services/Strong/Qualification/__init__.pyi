import Fnd0.Services.Strong.Qualification._2014_06.QualificationManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class QualificationManagementRestBindingStub(QualificationManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def AppendQualificationLevel(self, QualificationLevelInfo: list[Fnd0.Services.Strong.Qualification._2014_06.QualificationManagement.QualificationLevelInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def AssignUserQualification(self, AssignUserQualificationInfo: list[Fnd0.Services.Strong.Qualification._2014_06.QualificationManagement.AssignUserQualificationInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateQualification(self, QualificationInfo: list[Fnd0.Services.Strong.Qualification._2014_06.QualificationManagement.ManageQualificationInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RemoveQualificationLevel(self, QualificationLevelInfo: list[Fnd0.Services.Strong.Qualification._2014_06.QualificationManagement.QualificationLevelInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RemoveUserQualification(self, RemoveUserQualificationInfo: list[Fnd0.Services.Strong.Qualification._2014_06.QualificationManagement.RemoveUserQualificationInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UpdateQualification(self, UpdateQualificationInfo: list[Fnd0.Services.Strong.Qualification._2014_06.QualificationManagement.UpdateQualificationInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class QualificationManagementService:
    """
    
            Service For Qualification operations
            


Library Reference:

Fnd0SoaQualificationStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> QualificationManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def AppendQualificationLevel(self, QualificationLevelInfo: list[Fnd0.Services.Strong.Qualification._2014_06.QualificationManagement.QualificationLevelInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def AssignUserQualification(self, AssignUserQualificationInfo: list[Fnd0.Services.Strong.Qualification._2014_06.QualificationManagement.AssignUserQualificationInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def CreateQualification(self, QualificationInfo: list[Fnd0.Services.Strong.Qualification._2014_06.QualificationManagement.ManageQualificationInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def RemoveQualificationLevel(self, QualificationLevelInfo: list[Fnd0.Services.Strong.Qualification._2014_06.QualificationManagement.QualificationLevelInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def RemoveUserQualification(self, RemoveUserQualificationInfo: list[Fnd0.Services.Strong.Qualification._2014_06.QualificationManagement.RemoveUserQualificationInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def UpdateQualification(self, UpdateQualificationInfo: list[Fnd0.Services.Strong.Qualification._2014_06.QualificationManagement.UpdateQualificationInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
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

