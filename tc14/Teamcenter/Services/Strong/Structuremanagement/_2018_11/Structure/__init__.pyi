import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateGroupInput:
    """
    The structure represents all of the data necessary to create interchangeable
groups.
    """
    def __init__(self, ) -> None: ...
    ObjectType: str
    """
            Type of the Interchangeable Group to be created, Substitute Group or Alternate
            Group.
            """
    Props: System.Collections.Hashtable
    """
            A map of Interchangeable Group properties names and initial values pairs (string,
            string). Multi-valued properties are represented with a comma separated string.
            """
    SourceObjs: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of occurences (Occurrence level) or a list of Item/ItemRevision
            objects (Global level) that needs to be all replaced together as a group by an interchangeable
            group.
            """
    InterChangeableObjs: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """A list of interchangeable parts to be associcated as an Interchangeable Group."""

class Structure:
    """
    Interface Structure
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateInterchangeableGroups(self, Inputs: list[CreateGroupInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

