import Teamcenter.Soa.Client.Model
import typing

class GetSubTypeHierarchicalTreeInput:
    def __init__(self, ) -> None: ...
    TypeInternalName: str
    ClientId: str

class GetSubTypeHierarchicalTreeResponse:
    def __init__(self, ) -> None: ...
    TreeRootNodes: list[TypeHierarchicalTreeNode]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class TypeHierarchicalTreeNode:
    def __init__(self, ) -> None: ...
    TypeInternalName: str
    TypeDisplayName: str
    SubTypes: list[TypeHierarchicalTreeNode]

class Type:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetSubTypeHierarchicalTrees(self, GivenTypes: list[GetSubTypeHierarchicalTreeInput]) -> GetSubTypeHierarchicalTreeResponse: ...

