import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DeleteIn:
    """
    
            The DeleteIn structure is used to hold the input container, objects to be deleted
            associated as the property of the container. This structure also holds a flag to
            unlink the objects from the input container in case deletion fails.
            
    """
    def __init__(self, ) -> None: ...
    Container: Teamcenter.Soa.Client.Model.Strong.POM_object
    """A  POM_object that is related to the objects to be deleted."""
    ObjectsToDelete: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            A list POM_object objects be unrelated from the container object and  then
            deleted.
            """
    Property: str
    """
            The  name of the TypedRef or relation property with which the objects to be
            deleted are related to the input container
            """
    UnlinkAlways: bool
    """
            If true the operation will unlink the objects from the input container in case of
            delete operation otherwise they remained linked.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def UnlinkAndDeleteObjects(self, DeleteInput: list[DeleteIn]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation unlinks the input objects from their corresponding container and then
             attempts to deletes them. The input objects are related to the container as the reference
             or relation property supplied as part of the input. The operation also takes a flag
             whether to unlink the objects from the container in case the deletion fails.
             

             After unlinking the objects from the input container, if the objects being deleted
             are still referenced by other objects then error is returned to the caller. Any other
             error in deletion of the objects are also returned to the caller.
             

             In case the input argument objectsToDelete contains objects of type Item,
             then the operation also deletes all ItemRevision objects, associated ItemMaster,
             ItemRevisionMaster form objects.
             

             If the input argument objectsToDelete are of type ItemRevision and if is the
             last revision of the Item then the operation deletes the Item, associated
             ItemMaster, ItemRevisionMaster form objects.
             

             The input argument objectsToDelete can be an ImanRelation.
             

Teamcenter Component:

             Core Model Types - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Types
             framework.
             
        :param DeleteInput: 
                         A list containing an input container and list of objects to be first unrelated from
                         the container and then deleted.
             
        :return: 214139  - The business object could not be deleted. Please refer to the Teamcenter
             server syslog file for more information.
        """
        ...

