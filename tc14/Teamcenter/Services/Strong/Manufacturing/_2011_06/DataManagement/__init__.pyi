import System
import Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement
import Teamcenter.Soa.Client.Model
import typing

class ContextGroup:
    """
    A group of contexts opened by openContexts operation
    """
    def __init__(self, ) -> None: ...
    Contexts: list[OpenContextInfo]
    """A vector with information on each opened context in the group"""
    CollaborationContext: Teamcenter.Soa.Client.Model.ModelObject
    """
            The container of the context group (CC). This is relevant only in case the context
            to open is a CC object
            """

class OpenContextInfo:
    """
    Contains information on an opened context
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """The opened context (The top line of the created window)"""
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """
            The object which was passed to the method as input if this context was opened directly.
            If this context was opened as an outcome of another context or if CC was opened then
            this will be NULL
            """
    Views: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A vector with the top lines of the opened views (OG windows)"""
    StructureContext: Teamcenter.Soa.Client.Model.ModelObject
    """
            The structure context containing this context. This is relevant only in case the
            context to open is a CC or SC object
            """

class OpenContextInput:
    """
    Input for openContexts operation
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The object to open"""
    OpenViews: bool
    """Defines whether to open all connected views"""
    OpenAssociatedContexts: bool
    """Defines whether to open also associated contexts"""
    ContextSettings: Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement.CreateInput
    """
            Defines additional context settings such as configuration (revision rule, variant
            rule, IC), show-unconfigured options, Product Configurator context flag, etc.
            """

class OpenContextsResponse:
    """
    Response object for openContexts operation
    """
    def __init__(self, ) -> None: ...
    Output: list[ContextGroup]
    """A vector with information of the method output"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The operation ServiceData"""

class OpenViewsResponse:
    """
    Response object for openViews operation
    """
    def __init__(self, ) -> None: ...
    Views: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A vector with the opened views (the top lines of the created OG windows)"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The operation ServiceData"""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CloseContexts(self, Contexts: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This method is used to close contexts (base view windows). For each context, this
             method closes the base view window and all the open views (OG windows) associated
             to it
             
        :param Contexts: 
                         A vector with the contexts (top lines of the windows) to close
             
        :return: The service data of the operation
        """
        ...
    def CloseViews(self, StructureContext: Teamcenter.Soa.Client.Model.ModelObject, Views: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    This method is used to close opened views (OG windows).
        :param StructureContext: 
                         The structure context containing the views. Can be NULL if not using structire context.
             
        :param Views: 
                         A vector with the open views (top lines of the OG windows) to close
             
        :return: The service data of the operation
        """
        ...
    def OpenContexts(self, Input: list[OpenContextInput]) -> OpenContextsResponse:
        """    This method is used to open existing objects in new base view windows.
        :param Input: 
                         A list of OpenContextInput representing the objects to open
             
        :return: The response of the operation
        """
        ...
    def OpenViews(self, Context: Teamcenter.Soa.Client.Model.ModelObject, StructureContext: Teamcenter.Soa.Client.Model.ModelObject, Views: list[Teamcenter.Soa.Client.Model.ModelObject]) -> OpenViewsResponse:
        """    
             This method is used to open views (OG windows) for an already opened context (base
             view window).
             
        :param Context: 
                         The context (top line of the base view window) for which the views will be opened
             
        :param StructureContext: 
                         The structure context containing the context. This can be null
             
        :param Views: 
                         A vector with the views to open
             
        :return: The response of the operation
        """
        ...

