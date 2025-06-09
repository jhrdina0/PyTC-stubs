import Teamcenter.Soa.Client.Model
import typing

class ConnectResponse:
    def __init__(self, ) -> None: ...
    OutputVal: int
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FavoritesContainer:
    def __init__(self, ) -> None: ...
    ClientId: str
    Id: str
    Type: str
    DisplayName: str
    ParentId: str

class FavoritesList:
    def __init__(self, ) -> None: ...
    Containers: list[FavoritesContainer]
    Objects: list[FavoritesObject]

class FavoritesInfo:
    def __init__(self, ) -> None: ...
    CurFavorites: FavoritesList
    NewFavorites: FavoritesList

class FavoritesObject:
    def __init__(self, ) -> None: ...
    ClientId: str
    ObjectTag: Teamcenter.Soa.Client.Model.ModelObject
    DisplayName: str
    ParentId: str

class FavoritesResponse:
    def __init__(self, ) -> None: ...
    Output: FavoritesList
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Session:
    def __init__(self , *args: typing.Any) -> None: ...
    def Connect(self, FeatureKey: str, Action: str) -> ConnectResponse: ...
    def GetFavorites(self) -> FavoritesResponse: ...
    def SetFavorites(self, Input: FavoritesInfo) -> Teamcenter.Soa.Client.Model.ServiceData: ...

