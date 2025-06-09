import Prg0.Services.Strong.Programinfra._2016_04.ProgramManagement
import System
import System.Collections
import typing

class ClonePlanHierarchyProjectInput:
    """
    
            This is a input structure that contains the below
            

Map of string and source Prg0AbsPlan object.
            
Map of cloning options.
            
Prime Event date
            
Map of property values.
            


    """
    def __init__(self, ) -> None: ...
    CloneInfoMap: System.Collections.Hashtable
    CloneOptionsMap: System.Collections.Hashtable
    PrimeEventDate: System.DateTime
    """
            Planned date for the Prime Event of target Prg0AbsPlan object.
            
            The Prime Event is always the first Event for the Program level even if there are
            Project or Subproject Events that are earlier than the Program's first event.
            """
    PropertyValuesMap: System.Collections.Hashtable
    """
            Map (string, string) of input property values for the target Prg0AbsPlan object
            to be created.
            
            Valid properties are:
            
            1. object_name
            
            2. object_desc
            """

class ProgramManagement:
    """
    Interface ProgramManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ClonePlanHierarchyWithProject(self, CloneInfoInput: list[ClonePlanHierarchyProjectInput]) -> Prg0.Services.Strong.Programinfra._2016_04.ProgramManagement.ClonePlanHierarchyResponse: ...

