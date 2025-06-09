import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetGroupRoleViewModelInput:
    def __init__(self, ) -> None: ...
    UserObject: Teamcenter.Soa.Client.Model.Strong.User
    StartIndex: int
    PageSize: int

class GetGroupRoleViewModelResponse:
    def __init__(self, ) -> None: ...
    ViewModelRows: list[ViewModelObject]
    TotalFound: int
    EndIndex: int
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ViewModelObject:
    def __init__(self, ) -> None: ...
    ModelObject: Teamcenter.Soa.Client.Model.ModelObject
    ViewModelProperties: list[ViewModelProperty]

class ViewModelProperty:
    def __init__(self, ) -> None: ...
    PropInternalName: str
    PropDisplayName: str
    PropDBValue: str
    PropUIValue: str
    PropDataType: str
    IsEditable: bool
    HasLOV: bool
    IsModifiable: bool
    PropBO: Teamcenter.Soa.Client.Model.ModelObject

class UserManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetGroupRoleViewModelRows(self, Input: GetGroupRoleViewModelInput) -> GetGroupRoleViewModelResponse: ...

