import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ReferencerEditContextsOutput:
    """
    This structure contains an input object and its referencing edit contexts.
    """
    def __init__(self, ) -> None: ...
    InputObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The input WorkspaceObject."""
    EditContexts: list[Teamcenter.Soa.Client.Model.Strong.Fnd0EditContext]
    """The list of edit contexts referencing inputObject"""

class ReferencerEditContextsResponse:
    """
    
            This structure contains the input objects and the corresponding edit contexts that
            reference the input objects. Any partial errors that occur during the operation are
            returned in serviceData.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains any partial errors that occur during the operation."""
    RefnEditContextOutputs: list[ReferencerEditContextsOutput]
    """A list of ReferencerEditContextsOutput."""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetReferencerEditContexts(self, InputObjects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]) -> ReferencerEditContextsResponse:
        """    
             This operation will return the list of context (Fnd0EditContext) objects that
             reference the input WorkspaceObjects.
             

Use Cases:

             This operation enables the following use case.
             
             Use Case 1: User wants to provide a list of edit contexts that can be used to configure
             a business object to enable editing in a particular context.
             

User provides the business object as the input to this operation.
             
A list of edit contexts that reference the business object are returned.
             Any of these edit contexts can be used for configuring the business object for editing
             in that particular context.
             



Teamcenter Component:

             Edit Context - Teamcenter Component for Edit Context.
             
        :param InputObjects: 
                         The list of objects whose referencing edit contexts are required.
             
        :return: 
        """
        ...

