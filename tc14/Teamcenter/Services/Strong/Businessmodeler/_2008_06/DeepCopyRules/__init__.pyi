import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DeepCopyData:
    """
    Holds the relavent information regarding applicable deep copy rules.
    """
    def __init__(self, ) -> None: ...
    OtherSideObjectTag: Teamcenter.Soa.Client.Model.ModelObject
    """This is a tag representing object on which the deep copy action need to be performed."""
    RelationTypeName: str
    """This is a string representing the name the relation that need to be deep copied."""
    NewName: str
    """
            This is a string representing the new name for the new copy of the object represented
            by otherSideObjectTag. The value for the
            newName will be NULL
            if the action is not CopyAsObject or ReviseAndRelateToLatest.
            """
    Action: int
    """
            This is an integer representing the action to be performed on the object represented
            by otherSideObjectTag. The values for action
            are: CopyAsObjectType = 0, CopyAsRefType = 1, DontCopyType
            =2, RelateToLatest = 3, ReviseAndRelateToLatest = 4.
            """
    IsTargetPrimary: bool
    """
            Boolean representing whether the given item revision is a primary object in the relation
            that need to be deep copied.
            """
    IsRequired: bool
    """
            Boolean representing whether the deep information is from a mandatory deep copy rule
            configured by the administrator or not.
            """
    CopyRelations: bool
    """
            Boolean representing whether the Properties on  the Relation if any in the Relation
            that exists between the Primary and the Secondary should be carried forward or not.
            """

class DeepCopyInfoKey:
    """
    
            Holds the ItemRevision object tag (itemRevisionTag)
            and the operation name for which the deep copy information should be obtained.
            
    """
    def __init__(self, ) -> None: ...
    ItemRevisionTag: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The ItemRevision object on which the operation is being performed."""
    Operation: str
    """
            The string representing the operation name (i.e., Revise
            or SaveAs ).
            """

class DeepCopyInfoKeyValue:
    """
    Store key and value pair for DeepCopyData.
    """
    def __init__(self, ) -> None: ...
    Key: DeepCopyInfoKey
    """Structure representing the key for the Deep Copy Info."""
    DeepCopyInfos: list[DeepCopyData]
    """
            The resultant deepCopyInfo values are returned
            as a list.
            """

class DeepCopyInfoResponse:
    """
    
            Holds the response for the getDeepCopyInfo
            method.
            
    """
    def __init__(self, ) -> None: ...
    Values: list[DeepCopyInfoKeyValue]
    """
            The resultant deepCopyInfo values are returned
            as a list.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains the status of the operation. This operation does not return any error code
            but propagates the error code from lower level functions.
            """

class DeepCopyRules:
    """
    Interface DeepCopyRules
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDeepCopyInfo(self, Keys: list[DeepCopyInfoKey]) -> DeepCopyInfoResponse:
        """    
             Deep copy rules define whether objects belonging to a business object instance can
             be copied when a user performs a save as or revise operation on that instance. Deep
             copy rules can be applied to any business object type, and are inherited by children
             business object types. This operation gets the applicable deep copy rules for the
             given list of objects and the operation specified for each object.
             

Teamcenter Component:

             BMIDE (Server) - Set of services provided by BMIDE that allow efficiently underyling
             capabilities to develop/modify business objects
             
        :param Keys: 
                         List of itemRevision object tag and the operation name for which deep copy information
                         is needed.
             
        :return: A structure containing the values of the applicable deep copy rules and status of
             the operation. This operation does not return any error other than propagating the
             errors received from low level functions which are called from within the operation.
        """
        ...

