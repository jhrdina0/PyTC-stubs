import System
import Teamcenter.Services.Strong.Core._2011_06.DataManagement
import Teamcenter.Soa.Client.Model
import typing

class RelateInfoIn:
    """
    Information to perform relate operation
    """
    def __init__(self, ) -> None: ...
    Target: Teamcenter.Soa.Client.Model.ModelObject
    """
            parent object to which the created object will be related. This value will be ignored
            if relate is false. If value is null and relate is true, then a default target will
            be used based on WsoInsertNoSelectionsPref.
            """
    PropertyName: str
    """
            Name of the property with which the created object will be related to the input target
            object if defined or the default one.This value will be ignored if relate is false.
            If value is empty and relate is true, then default relation will be used.
            """
    Relate: bool
    """A relation is created only if this value is true."""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SaveAsObjectAndRelate(self, SaveAsInput: list[Teamcenter.Services.Strong.Core._2011_06.DataManagement.SaveAsIn], RelateInfo: list[RelateInfoIn]) -> Teamcenter.Services.Strong.Core._2011_06.DataManagement.SaveAsObjectsResponse:
        """    
             This operation saves the given object and its related objects as new instances. Related
             objects are identifed using deep copy rules. Optionally,this method relates the new
             object to the input target object or to a default folder.
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param SaveAsInput: 
                         The property values to be used for the new objects. The properties passed in should
                         be defined in SaveAs descriptor.
             
        :param RelateInfo: 
                         The paste options used to relate the newly created object.
             
        :return: A list of objects that are created through saveas operation, including children objects.
             CreatedList contains objects that are created by SaveAs operation.. It contains GRM
             relations created due to paste operation. UpdatedList contains target objects to
             which the newly created objects are related. Failure for any element in the input
             list is returned as a Partial Error in the ServiceData . The Partial Error includes
             the index of the failed element from the input list. 214424: SaveAs action succeeded.
             But server could not identify a suitable target object to relate the newly created
             object.. 214425:  When item revision is saved as new instance,server relates item
             to target folder. Presence of this error code indicates that server could not paste
             item and instead has pasted the created item revision. 214426: SaveAs operation on
             that specifc object has failed.
        """
        ...

