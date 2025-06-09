import System
import Teamcenter.Soa.Client.Model
import typing

class ContextsArray:
    """
    the structure contains array of contexts
    """
    def __init__(self, ) -> None: ...
    Contextsarray: list[Teamcenter.Soa.Client.Model.ModelObject]
    """array of contexts ( any types)"""

class ReferencedContexts:
    """
    the structure used for three different modes: add, set, remove
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """the top line of BOP window which will be referenced"""
    AddRefContexts: list[Teamcenter.Soa.Client.Model.ModelObject]
    """contexts, which will reference"""
    RemoveRefContexts: list[Teamcenter.Soa.Client.Model.ModelObject]
    """contexts, which will be removed"""
    RemoveExistingRef: bool
    """remove all referenced contexts"""

class ReferencedContextsResponse:
    """
    the structure contains referenced contexts and used for response.
    """
    def __init__(self, ) -> None: ...
    Refcontexts: list[ContextsArray]
    """vector of vectors referenced contexts according to the order from the input vector"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """service data will return errors only. No data will be return via Service Data."""

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetReferenceContexts(self, Contexts: list[Teamcenter.Soa.Client.Model.ModelObject]) -> ReferencedContextsResponse:
        """    return referenced contexts of input context.
        :param Contexts: 
                         vector of input contexts
             
        :return: return ReferenceContextResponse structure
        """
        ...
    def SetReferenceContexts(self, Input: list[ReferencedContexts]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    set Reference context according to user choice.
        :param Input: 
                         includes ReferencedContexts structure
             
        :return: service data will return errors only and no data.
        """
        ...

