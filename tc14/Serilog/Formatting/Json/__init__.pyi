import Serilog.Data
import Serilog.Events
import Serilog.Parsing
import System
import System.IO
import typing

class JsonFormatter:
    @typing.overload
    def __init__(self, closingDelimiter: str, renderMessage: bool = False, formatProvider: System.IFormatProvider) -> None: ...
    @typing.overload
    def __init__(self, omitEnclosingObject: bool, closingDelimiter: str, renderMessage: bool = False, formatProvider: System.IFormatProvider) -> None: ...
    def Format(self, logEvent: Serilog.Events.LogEvent, output: System.IO.TextWriter) -> None: ...
    @staticmethod
    def Escape(s: str) -> str: ...

class JsonValueFormatter(dict[System.IO.TextWriter, bool]):
    def __init__(self, typeTagName: str = '_typeTag') -> None: ...
    def Format(self, value: Serilog.Events.LogEventPropertyValue, output: System.IO.TextWriter) -> None: ...
    @staticmethod
    def WriteQuotedJsonString(str: str, output: System.IO.TextWriter) -> None: ...

class <>c:
    def __init__(self, ) -> None: ...
    <>9: <>c
    <>9__7_0: list[typing.Any, bool, System.IO.TextWriter]
    <>9__7_1: list[typing.Any, bool, System.IO.TextWriter]
    <>9__7_2: list[typing.Any, bool, System.IO.TextWriter]
    <>9__7_3: list[typing.Any, bool, System.IO.TextWriter]
    <>9__7_4: list[typing.Any, bool, System.IO.TextWriter]
    <>9__7_5: list[typing.Any, bool, System.IO.TextWriter]
    <>9__7_6: list[typing.Any, bool, System.IO.TextWriter]
    <>9__8_0: dict[Serilog.Parsing.PropertyToken, bool]
    <>9__8_1: dict[Serilog.Parsing.PropertyToken, str]

class <>c__DisplayClass9_0:
    def __init__(self, ) -> None: ...
    writer: dict[typing.Any, System.IO.TextWriter]

