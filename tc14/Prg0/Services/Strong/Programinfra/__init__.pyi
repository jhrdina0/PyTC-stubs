import Prg0.Services.Strong.Programinfra._2016_04.ProgramManagement
import Prg0.Services.Strong.Programinfra._2016_10.ProgramManagement
import Prg0.Services.Strong.Programinfra._2021_06.ProgramManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class ProgramManagementRestBindingStub(ProgramManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ClonePlanHierarchy(self, InputInfo: list[Prg0.Services.Strong.Programinfra._2016_04.ProgramManagement.ClonePlanHierarchyInputInfo]) -> Prg0.Services.Strong.Programinfra._2016_04.ProgramManagement.ClonePlanHierarchyResponse: ...
    def GetEvents(self, OperationInput: list[Teamcenter.Soa.Client.Model.Strong.Prg0AbsPlan]) -> Prg0.Services.Strong.Programinfra._2016_04.ProgramManagement.GetEventsResponse: ...
    def GetPlanHierarchy(self, OperationInput: list[Teamcenter.Soa.Client.Model.Strong.Prg0AbsPlan]) -> Prg0.Services.Strong.Programinfra._2016_04.ProgramManagement.GetPlanHierarchyResponse: ...
    def ClonePlanHierarchyWithProject(self, CloneInfoInput: list[Prg0.Services.Strong.Programinfra._2016_10.ProgramManagement.ClonePlanHierarchyProjectInput]) -> Prg0.Services.Strong.Programinfra._2016_04.ProgramManagement.ClonePlanHierarchyResponse: ...
    def MovePlanObjects(self, MovePlanObjectsInput: list[Prg0.Services.Strong.Programinfra._2021_06.ProgramManagement.MovePlanObjectsInputInfo], MoveOptions: list[Prg0.Services.Strong.Programinfra._2021_06.ProgramManagement.NameValueStringPair]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def MoveEvents(self, Events: list[Teamcenter.Soa.Client.Model.Strong.Prg0AbsEvent], NewEventDate: System.DateTime, UpdateSecondaryEvents: bool, RunInBackground: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class ProgramManagementService:
    """
    
            This service exposes operations related to Program Management in Teamcenter. A Program
            represents a unit of business investment to pursue the market opportunity and meet
            business goals. When a new Program is defined, the Governance for that Program is
            also defined. Program Management begins from analysis of market requirements and
            alignment with corporate goals. During Program execution, detailed analysis of portfolio
            Projects is done and individual Projects are approved for execution. Targets are
            captured for the planning entities and aggregated at the architecture nodes and then
            rolled up based on models for each Project/Program.
            


Library Reference:

Prg0SoaProgramInfraStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ProgramManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ClonePlanHierarchy(self, InputInfo: list[Prg0.Services.Strong.Programinfra._2016_04.ProgramManagement.ClonePlanHierarchyInputInfo]) -> Prg0.Services.Strong.Programinfra._2016_04.ProgramManagement.ClonePlanHierarchyResponse:
        """    
             This operation clones the input Prg0AbsPlan object, its child Prg0AbsPlan
             objects and all the associated Prg0AbsEvent objects. If the input plan level
             is of type Prg0AbsProgramPlan (or its subtype), the entire Plan hierarchy
             is copied under a new Prg0AbsProgramPlan object.
             
             Please note that the clone of Prg0AbsProjectPlan object is not supported.
             

Use Cases:

             Program_1---------------------------------> Event_1 (Planned Date: 01-01-2015)
             
             ----|----Project_1------------------------------> Event_2(Planned Date: 02-02-2018)
             
             --------|----SubProject_11----------------------------> Event_3 (Planned Date:
             03-03-2016)
             
             --------|----SubProject_12----------------------------> Event_4 (Planned Date:
             03-03-2017)
             
             --------|----SubProject_13----------------------------> Event_5 (Planned Date:
             03-03-2017)
             
             ----|----Project_2------------------------------> Event_6 (Planned Date: 04-04-2018)
             
             --------|----SubProject_21-----------------------------> Event_7 (Planned Date:
             05-05-2016)
             
             --------|----SubProject_22-----------------------------> Event_8 (Planned Date:
             05-05-2017)
             

             Use Case 1: Prg0ProgramPlan and primeEventDate
             as input
             
             Operation returns the cloned Prg0ProgramPlan object with all the Plan levels
             and associated Prg0Event objects. Input primeEventDate
             is set as Planned date of the Prime Prg0Event object for the cloned Prg0ProgramPlan
             object. Delta between the Planned date of source Prime Prg0Event object and
             input primeEventDate is used to calculate
             the Planned date of all the Prg0Event objects of all the Plan levels.
             

             E.g. If Program_1 is the input as Prg0AbsPlan and 01-01-2018 input as primeEventDate and
             object_name as "New_Program_1" then the cloned plan hierarchy will be created
             as below:
             

             New_Program_1-----------------------------> Event_1 (Planned Date: 01-01-2018)
             
             ----|----Project_1------------------------------> Event_2(Planned Date: 02-02-2021)
             
             --------|----SubProject_11----------------------------> Event_3 (Planned Date:
             03-03-2019)
             
             --------|----SubProject_12----------------------------> Event_4 (Planned Date:
             03-03-2020)
             
             --------|----SubProject_13----------------------------> Event_5 (Planned Date:
             03-03-2020)
             
             ----|----Project_2------------------------------> Event_6 (Planned Date: 04-04-2021)
             
             --------|----SubProject_21----------------------------> Event_7 (Planned Date:
             05-05-2019)
             
             --------|----SubProject_22----------------------------> Event_8 (Planned Date:
             05-05-2020)
             

             Use Case 2: Prg0ProgramPlan which does not have Prg0Event objects associated
             with it
             
             Operation returns an information message saying "Operation cannot be completed as
             source Prg0ProgramPlan object does not have Prg0Event object associated
             with it".
             

             Use Case 3: Prg0ProjectPlan as input
             
             Operation returns an information message saying "Operation cannot performed for objects
             of type Prg0ProjectPlan".
             

             Use Case 4: Prg0SubProjectPlan as input
             
             Operation returns an information message saying "Operation cannot performed for objects
             of type Prg0SubProjectPlan".
             

Notes:


Actual date and forecast date are set to null value for all the Prg0Event
             objects of all the Plan levels of cloned Prg0AbsPlan objects.
             
Prg0State is set to value
             "Not Started" for all the Plan levels of
             cloned Prg0AbsPlan objects.
             
All other attribute values are copied as it is.
             



Teamcenter Component:

             Program Management Infrastructure - Defines the Program Management infrastructure
             components (Program, Project and Event Management)
             
        :param InputInfo: 
                         A list of structure containing <b>ClonePlanHierarchyInputInfo</b> objects.
             
        :return: 
        """
        ...
    def GetEvents(self, OperationInput: list[Teamcenter.Soa.Client.Model.Strong.Prg0AbsPlan]) -> Prg0.Services.Strong.Programinfra._2016_04.ProgramManagement.GetEventsResponse:
        """    
             This operation returns a list of Events associated with a Program, a Project or a
             Sub-Project depending upon the input.
             
             The operation accepts a vector of Prg0AbsPlan objects  which can contain a
             Prg0ProgramPlan, Prg0ProjectPlan or Prg0SubProjectPlan object as
             input.
             

Use Cases:

             Plan Hierarchy
             

             Program1------------------------------------------->Event1
             
             -----|--------Project1------------------------------>Event2
             
             --------------------|------------SubProject1------->Event3
             
             --------------------|------------SubProject2
             
             -----|--------Project2------------------------------->Event4
             
             --------------------|------------SubProject3
             
             --------------------|------------SubProject4-------->Event5
             

             Use case 1: Prg0ProgramPlan object is passed as input.
             
             The operation returns a list of Prg0AbsEvent objects along with the parent
             Prg0ProgramPlan object.
             
             If user specifies input as Program1, the output will be a structure containing Program1
             and a list containing Event1.
             

             Use Case 2: Prg0ProjectPlan object is passed as input.
             
             The operation returns a list of Prg0AbsEvent objects along with the parent
             Prg0ProjectPlan object.
             
             If user specifies input as Project2, the output will be a structure containing Project2
             and a list containing Event4.
             

             Use Case 3: Prg0SubProjectPlan object is passed as input.
             
             The operation would return a list of Prg0AbsEvent objects along with the parent
             Prg0SubProjectPlan object.
             
             If user specifies input as SubProject1, the output will be a structure containing
             SubProject1 and a list containing Event3.
             

Teamcenter Component:

             Program Management Infrastructure - Defines the Program Management infrastructure
             components (Program, Project and Event Management)
             
        :param OperationInput: 
                         A list of <b>Prg0AbsPlan</b> objects.
             
        :return: 
        """
        ...
    def GetPlanHierarchy(self, OperationInput: list[Teamcenter.Soa.Client.Model.Strong.Prg0AbsPlan]) -> Prg0.Services.Strong.Programinfra._2016_04.ProgramManagement.GetPlanHierarchyResponse:
        """    
             This operation returns a hierarchy of  plan objects that include the Prg0AbsProgramPlan
             object and its child Prg0AbsProjectPlan objects based on the input provided.
             
             This operation accepts a vector of Prg0AbsPlan objects each of which can contain
             a Prg0ProgramPlan, Prg0ProjectPlan or Prg0SubProjectPlan object
             as input.
             

Use Cases:

             The user can pass a Prg0ProgramPlan, Prg0ProjectPlan or Prg0SubProjectPlan
             object as input.
             

             Plan Hierarchy
             

             Program1
             
             ------|------Project1
             
             ----------------|------SubProject1
             
             ----------------|------SubProject2
             
             ------|------Project2
             
             ----------------|------SubProject3
             
             ----------------|------SubProject4
             

             Use case 1: Prg0ProgramPlan object is passed as input.
             
             If the user passes a Program as input, this operation returns its child Projects
             and Sub-Projects along with the Program itself.
             
             Consider Program1 is passed as input. The output would be a structure containing
             Program1 and a list of its child Projects and Sub-Projects in the order Program1,
             Project1, SubProject1, SubProject2, Project2, SubProject3 and SubProject4.
             

             Use Case 2: Prg0ProjectPlan object is passed as input.
             
             If the user passes a Project as input, this operation returns its parent Program
             and its child Sub-Projects.
             
             Consider Project2 is passed as input. The output would be a structure containing
             Project2 and a list of its parent Plan Program1 followed by Project2 and its child
             Sub-Projects, SubProject3 and SubProject4.
             

             Use Case 3: Prg0SubProjectPlan object is passed as input.
             
             If the user passes a Sub-Project as input, this operation returns the input Sub-Project,
             its parent Project and the root Program.
             
             Consider SubProject3 is passed as input. The output would be a structure containing
             SubProject3 and a list containing its root Plan Program1 and its parent Plan Project2
             and SubProject3.
             

Teamcenter Component:

             Program Management Infrastructure - Defines the Program Management infrastructure
             components (Program, Project and Event Management)
             
        :param OperationInput: 
                         A list of <b>Prg0AbsPlan</b> objects.
             
        :return: 
        """
        ...
    def ClonePlanHierarchyWithProject(self, CloneInfoInput: list[Prg0.Services.Strong.Programinfra._2016_10.ProgramManagement.ClonePlanHierarchyProjectInput]) -> Prg0.Services.Strong.Programinfra._2016_04.ProgramManagement.ClonePlanHierarchyResponse: ...
    def MovePlanObjects(self, MovePlanObjectsInput: list[Prg0.Services.Strong.Programinfra._2021_06.ProgramManagement.MovePlanObjectsInputInfo], MoveOptions: list[Prg0.Services.Strong.Programinfra._2021_06.ProgramManagement.NameValueStringPair]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation moves Plan Objects to a different location in the Plan hierarchy within
             same level, i.e. under the common parent Plan.
             

             Use Case:
             
             The user can pass a  Prg0AbsPlan or its subtypes e.g. Prg0ProjectPlan
             or Prg0SubProjectPlan object as input.
             

             Plan Hierarchy
             

             Program1
             
             ------|------Project1
             
             ----------------|------SubProject1
             
             ----------------|------SubProject2
             
             ----------------|------SubProject3
             
             ------|------Project2
             
             ----------------|------SubProject1
             
             ------|------Project3
             
             ----------------|------SubProject1
             

             Use Case 1: Prg0ProjectPlan object is passed as input.
             
             If the user wants to move Projects within Program this operation will update the
             order of the input project.
             

             Program1
             
             ------|------Project2
             
             ----------------|------SubProject1
             
             ------|------Project1
             
             ----------------|------SubProject1
             
             ----------------|------SubProject2
             
             ----------------|------SubProject3
             
             ------|------Project3
             
             ----------------|------SubProject1
             

             Use Case 2: Prg0SubProjectPlan object is passed as input.
             
             If the user wants to move Subprojects within Project this operation will update the
             order of the input subproject.
             

             Program1
             
             ------|------Project1
             
             ----------------|------SubProject3
             
             ----------------|------SubProject2
             
             ----------------|------SubProject1
             
             ------|------Project2
             
             ----------------|------SubProject1
             
             ------|------Project3
             
             ----------------|------SubProject1
             

Teamcenter Component:

             Program Management Infrastructure - Defines the Program Management infrastructure
             components (Program, Project and Event Management)
             
        :param MovePlanObjectsInput: 
                         A list of structures containing information to move PlanObjects.
             
        :param MoveOptions: 
                         allowMovingUnderDifferentParent: true/false (Set true to allow plan object to be
                         moved under a different parent.)
             
        :return: 
        """
        ...
    def MoveEvents(self, Events: list[Teamcenter.Soa.Client.Model.Strong.Prg0AbsEvent], NewEventDate: System.DateTime, UpdateSecondaryEvents: bool, RunInBackground: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

