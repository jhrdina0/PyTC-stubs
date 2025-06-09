import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AddChildGroupsToGroupStructure:
    """
    Groups to be added to a parent Group.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    GroupsToAdd: list[Teamcenter.Soa.Client.Model.Strong.Group]
    """
            A list of existing Group objects to be added to the parent Group as
            child groups.
            """
    GroupsToCreateAndAdd: list[CreateAndAddChildGrpsToGrpStructure]
    """
            A list of CreateAndAddChildGrpsToGrpStructure objects for Group. A new Group
            will be created for each input in the list and added to the parent Group.
            """
    ParentGroup: Teamcenter.Soa.Client.Model.Strong.Group
    """The parent Group the child groups are to be added to."""

class CreateAndAddChildGrpsToGrpStructure:
    """
    Group to be created.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Name of the Group to be created."""
    Description: str
    """Description of the Group."""
    Privilege: bool
    """
            Indicates whether members of the Group will get administrative privileges.
            
            If true, all members of this Group will have system administration privilege;
            otherwise members will not have administration privilege.
            """
    LocalVolume: Teamcenter.Soa.Client.Model.Strong.ImanVolume
    """
            Default local volume for the Group, local volume refers to a physical location
            with same site as Group where the Teamcenter files are stored. This temporary local
            volume allows the file to be stored locally before it is automatically transferred
            to the final destination in the background. Once the file is stored in the default
            local volume, the user can continue working without having to wait for the upload
            to take place.
            """
    Security: str
    """
            Specifies the project level security settings of Group. Valid values are "Internal"
            or "External". The internal/external Security setting allows or restricts access
            to data. For example, members of external groups can only access data in their group.
            """
    Volume: Teamcenter.Soa.Client.Model.Strong.ImanVolume
    """The location where the Teamcenter files to be stored by the users of this Group."""

class GroupManagement:
    """
    Interface GroupManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddChildGroups(self, ChildGroupsToGroupStructs: list[AddChildGroupsToGroupStructure]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Adds new groups and existing groups as child groups to specified Group objects.
             If groups are new, then they will be created first before they are added.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param ChildGroupsToGroupStructs: 
<b>Group</b> objects to be created and/or to be added to<b> </b>a <b>Group</b> object
                         as child groups.
             
        :return: 
        """
        ...

