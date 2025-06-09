import Serilog.Events
import System
import typing

class Matching:
    @staticmethod
    @typing.overload
    def FromSource() -> dict[Serilog.Events.LogEvent, bool]: ...
    @staticmethod
    @typing.overload
    def FromSource(source: str) -> dict[Serilog.Events.LogEvent, bool]: ...
    @staticmethod
    @typing.overload
    def WithProperty(propertyName: str) -> dict[Serilog.Events.LogEvent, bool]: ...
    @staticmethod
    @typing.overload
    def WithProperty(propertyName: str, scalarValue: typing.Any) -> dict[Serilog.Events.LogEvent, bool]: ...
    @staticmethod
    @typing.overload
    def WithProperty(propertyName: str, predicate: dict[TScalar, bool]) -> dict[Serilog.Events.LogEvent, bool]: ...

class <>c__DisplayClass1_0:
    def __init__(self, ) -> None: ...
    source: str

class <>c__DisplayClass2_0:
    def __init__(self, ) -> None: ...
    propertyName: str

class <>c__DisplayClass3_0:
    def __init__(self, ) -> None: ...
    propertyName: str
    scalar: Serilog.Events.ScalarValue

TScalar = typing.TypeVar('TScalar')

class <>c__DisplayClass4_0[TScalar]:
    def __init__(self, ) -> None: ...
    propertyName: str
    predicate: dict[TScalar, bool]

