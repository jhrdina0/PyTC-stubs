import System
import System.IO
import typing

class LoggingFailedException(System.Exception):
    def __init__(self, message: str) -> None: ...

class SelfLog:
    Out: System.IO.TextWriter
    @staticmethod
    def set_Out(value: System.IO.TextWriter) -> None: ...
    @staticmethod
    @typing.overload
    def Enable(output: System.IO.TextWriter) -> None: ...
    @staticmethod
    @typing.overload
    def Enable(output: list[str]) -> None: ...
    @staticmethod
    def Disable() -> None: ...
    @staticmethod
    def WriteLine(format: str, arg0: typing.Any, arg1: typing.Any, arg2: typing.Any) -> None: ...

class <>c__DisplayClass3_0:
    def __init__(self, ) -> None: ...
    output: System.IO.TextWriter

