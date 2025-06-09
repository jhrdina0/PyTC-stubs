import Mdl0.Services.Strong.Modelcore._2014_10.Search
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class CreateInput:
    def __init__(self, ) -> None: ...
    BoName: str
    StringProps: System.Collections.Hashtable
    StringArrayProps: System.Collections.Hashtable
    DoubleProps: System.Collections.Hashtable
    DoubleArrayProps: System.Collections.Hashtable
    FloatProps: System.Collections.Hashtable
    FloatArrayProps: System.Collections.Hashtable
    IntProps: System.Collections.Hashtable
    IntArrayProps: System.Collections.Hashtable
    BoolProps: System.Collections.Hashtable
    BoolArrayProps: System.Collections.Hashtable
    DateProps: System.Collections.Hashtable
    DateArrayProps: System.Collections.Hashtable
    ObjectProps: System.Collections.Hashtable
    ObjectArrayProps: System.Collections.Hashtable
    CompoundCreateInput: System.Collections.Hashtable

class CreateIn:
    def __init__(self, ) -> None: ...
    ClientId: str
    Data: CreateInput

class RecipeContainerInfo:
    def __init__(self, ) -> None: ...
    CreateInput: CreateIn
    Recipe: Mdl0.Services.Strong.Modelcore._2014_10.Search.SearchRecipe2

class RecipeContainerResponse:
    def __init__(self, ) -> None: ...
    ClientIdToBoMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Search:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateRecipeContainers(self, RecipeContainerInfos: list[RecipeContainerInfo]) -> RecipeContainerResponse: ...

