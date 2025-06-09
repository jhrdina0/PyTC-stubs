import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ActivityToolInfo:
    """
    TODO
    """
    def __init__(self, ) -> None: ...
    ProcessBV: Teamcenter.Soa.Client.Model.Strong.PSBOMView
    """The context bom view"""
    ToolOccThreadChains: System.Collections.Hashtable
    """The context bom view"""

class CreateOrUpdateMEActivityFolderResponse:
    """
    TODO
    """
    def __init__(self, ) -> None: ...
    SuccessfullyProcessedMEAct: System.Collections.Hashtable
    """successfullyProcessedMEAct"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""

class CreateOrUpdateMENXObjectResponse:
    """
    TODO
    """
    def __init__(self, ) -> None: ...
    SuccessfullyProcessedMENXObj: System.Collections.Hashtable
    """successfullyProcessedMENXObj"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""

class MEActivityFolderInfo:
    """
    TODO
    """
    def __init__(self, ) -> None: ...
    Activity: Teamcenter.Soa.Client.Model.Strong.MEActivity
    """The MEActivity object tag in cases of update"""
    Name: str
    """Name of the activity folder that needs to created/updated."""
    Description: str
    """Description of the acivity folder that needs to created or updated."""
    Type: str
    """Type of the activity folder that needs to be created."""
    ToolInfo: ActivityToolInfo
    """toolInfo"""
    Contents: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """Objects that need to be inserted into the activity folder as contents."""
    ParentActivities: list[Teamcenter.Soa.Client.Model.Strong.MEActivity]
    """Parent activity folder into which this folder needs to inserted as a content."""
    Predecessors: list[Teamcenter.Soa.Client.Model.Strong.MEActivity]
    """MEActivity folder that need to added as predecessors."""
    Attributes: list[NameValueStruct]
    """
            A vector of NameValueStruct  that has the name value pairs. Through this act_location,
            time and start_time can be set for the folder.
            """
    Complete: bool
    """
            Whether the given information completely represents the folder to be updated. This
            is flag is applicable only for completely replacing tools, predecessors and contents.
            """

class MENXObjectInfo:
    """
    TODO
    """
    def __init__(self, ) -> None: ...
    MenxObject: Teamcenter.Soa.Client.Model.Strong.MENXObject
    """The MENXObject object tag in cases of update"""
    Name: str
    """Name of the MENXObject that needs to created or updated."""
    Description: str
    """Description of the MENXObject that needs to created or updated."""
    Type: str
    """Type of the MENXObject that needs to created."""
    SubType: str
    """Sub-Type of the MENXObject that needs to created."""
    Attributes: list[NameValueStruct]
    """
            A vector of NameValueStruct  that has the name value pairs. Through this the attributes
            of the MENXObject like double_attrs, double_keys, int_attrs, int_keys, string_attrs,
            string_keys can be set.
            """

class NameValueStruct:
    """
    TODO
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Title of the attribute that needs to be set"""
    Values: list[str]
    """Values of the attribute to be set"""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateMEActivityFolders(self, ActivityInfos: list[MEActivityFolderInfo]) -> CreateOrUpdateMEActivityFolderResponse:
        """    
             Allows the user to create and/or update a MEActivityFolder.  If the given MEActivity
             object exists but the input attribute values that differ from those already set,
             an attempt is made to update the values if possible. If multiple level of sub activities
             are to be created those activities can be passed in as the objects if they already
             exist in database. The created folder and updated folders are returned to the client
             through the createdObjects and updatedObject list of the service data respectively.
             
        :param ActivityInfos: 
                         Input is a vector of MEActivityFolderInfo structs. A Boolean value part of the structure
                         signifying if the input data represents the complete representation of the folder
                         tools, predecessors, and contents or if it represents objects to be appended to the
                         existing folder tools, predecessors, and contents (folder context information) if
                         complete is true, then the expectation is that the entire folder context information
                         is supplied and any folder context not supplied that currently exist in Teamcenter
                         will be removed from the folder context, if complete is false, the input context
                         elements will be appended to the input folder.
             
        :return: contains map between the index of the input structure and the created or updated
             object, All Object ids that were successfully created or updated are added to ServiceData.
             Objects/object ids that failed the find are returned in a list of failures in the
             ServiceData with its index.
        """
        ...
    def CreateOrUpdateMENXObjects(self, MeObjectInfos: list[MENXObjectInfo], Container: Teamcenter.Soa.Client.Model.Strong.Folder) -> CreateOrUpdateMENXObjectResponse:
        """    
             Allows the user to create and/or update a MENXObject. If the given MENXObject object
             exists but the input attribute values that differ from those already set, an attempt
             is made to update the values if possible.
             
        :param MeObjectInfos: 
                         Input is a vector of MENXObjectInfo structs.
             
        :param Container: 
                         The folder into which the created objects are to be placed. This can be a NULLTAG
                         in which case the created objects will not be inserted into any folder.
             
        :return: contains map between the index of the input structure and the created or updated
             object, All Object ids that were successfully created or updated are added to ServiceData.
             Objects/object ids that failed the find are returned in a list of failures in the
             ServiceData with its index.
        """
        ...

