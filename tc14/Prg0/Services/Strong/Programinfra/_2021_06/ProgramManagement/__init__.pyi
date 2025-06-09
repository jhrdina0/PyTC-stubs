import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class MovePlanObjectsInputInfo:
    """
    
            The input information required to perform move of plan objects based on the given
            plan and new previous sibling objects
            
    """
    def __init__(self, ) -> None: ...
    Plan: Teamcenter.Soa.Client.Model.Strong.Prg0AbsPlan
    """The Prg0AbsPlan to move."""
    NewParent: Teamcenter.Soa.Client.Model.Strong.Prg0AbsPlan
    """
            The new parent Prg0AbsPlan for the plan object.
            
            If the new parent is not defined, then the plan object will be moved under the same
            parent plan. (Optional)
            """
    PrevSibling: Teamcenter.Soa.Client.Model.Strong.Prg0AbsPlan
    """
            The new previous sibling Prg0AbsPlan for the plan object.
            
            If not provided, then the plan object will be moved to be the first child of parent.
            If provided, then the plan object will be moved next to new sibling. (Optional)
            """

class NameValueStringPair:
    """
    Structure containing a pair (string, string) of name and value respectively.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of key in Pair."""
    KeyValue: str
    """The value of key in Pair."""

class ProgramManagement:
    """
    Interface ProgramManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def MovePlanObjects(self, MovePlanObjectsInput: list[MovePlanObjectsInputInfo], MoveOptions: list[NameValueStringPair]) -> Teamcenter.Soa.Client.Model.ServiceData:
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

