import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ChangeContextStructIn:
    """
    Structure containing configuration mode and the list of input objects.
    """
    def __init__(self, ) -> None: ...
    ChangeConfigurationMode: str
    InputObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """The objects to be configured for the input context."""

class ChangeContextStructOut:
    """
    Structure of the context used to configure objects and the list of configured objects.
    """
    def __init__(self, ) -> None: ...
    ChangeContext: Teamcenter.Soa.Client.Model.Strong.Fnd0ChangeContext
    """A business object that contains the input context and the configuration mode used."""
    ConfiguredObjs: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """List of configured objects."""

class SetChangeContextResponse2:
    """
    
            The valid input contexts and the corresponding configured objects are added to configuredObjectsMap.
            If the input context is not a valid context for configuring objects, no value is
            added to configuredObjectsMap for this context, and a partial error is added for
            this context. If the context is valid, and an object is not valid for configuration
            in that context, a partial error is added for that object.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains any partial errors for the operation."""
    ConfiguredObjectsMap: System.Collections.Hashtable
    """
            A map (business object, list of ChangeContextStructOut) between a context and the
            list of configured objects.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SetChangeContext2(self, Inputs: System.Collections.Hashtable) -> SetChangeContextResponse2:
        """    
             This operation  configures business objects to allow the objects to be edited, queried
             or deleted in a context without changing the public versions of the objects. This
             operation can also configure business objects with no context in order to edit, query
             or delete the public versions of the objects.
             
             This operation does not have any effect on business objects that are not minor revisable
             and such objects will always be returned without being configured.
             
             The operation can be used to configure multiple sets of objects using different contexts.
             

Use Case:

             Use Case 1: User wants to edit the properties of a set of business objects in an
             isolated context with the intention to share the proposed changes with other users.
             


User creates a Fnd0MarkupSpace object that abstracts the context
             within which the edit needs to be performed.
             
The Fnd0MarkupSpace object is provided as input to the operation
             along with the business objects that need to be edited.
             
The configured business objects are returned in the response and
             can be used for performing edits in the context.
             



             Use Case 2: User wants to query the properties of a set of business objects in an
             isolated context that have been edited in the context of a ChangeNotice.
             


User creates a ChangeNotice object that abstracts the context
             within which the edit needs to be performed.
             
The ChangeNotice object is provided as input to the operation
             along with the business objects that need to be configured.
             
The configured business objects are returned in the response and
             can be used for performing edits in the context.
             




             Use Case 3: User wants to query a property belonging to the public version of a business
             object that is currently configured for editing in a collaborative space.
             


User passes a null value for the context along with the business
             object that needs to be inspected in public.
             
The unconfigured business objects are returned in the response and
             any queries performed on the objects will return public data.
             



Teamcenter Component:

             Edit Context - Teamcenter Component for Edit Context.
             
        :param Inputs: 
                         The operation accepts multiple sets of objects that need to be configured using different
                         contexts. A map (business object, list of ChangeContextStructIn) between a context
                         and a list of objects to be configured using this context. The context object can
                         be null, in which case the corresponding list of objects will be configured for public.
                         The context can also be a runtime business object which holds the context and the
                         change configuration mode.
             
        :return: 
        """
        ...

