import Teamcenter.Soa.Client.Model
import typing

class Arg:
    def __init__(self, ) -> None: ...
    Val: str
    Structure: list[Structure]
    Array: list[Array]

class Array:
    def __init__(self, ) -> None: ...
    Entries: list[Entry]

class Entry:
    def __init__(self, ) -> None: ...
    Val: str
    Structure: list[Structure]
    Array: list[Array]

class InvokeICTMethodResponse:
    def __init__(self, ) -> None: ...
    Output: list[Arg]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Structure:
    def __init__(self, ) -> None: ...
    Args: list[Arg]

class ICT:
    def __init__(self , *args: typing.Any) -> None: ...
    def InvokeICTMethod(self, ClassName: str, MethodName: str, Args: list[Arg]) -> InvokeICTMethodResponse: ...

