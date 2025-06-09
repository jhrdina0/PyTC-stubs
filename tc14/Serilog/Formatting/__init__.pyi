import Serilog.Events
import System.IO
import typing

class ITextFormatter:
    def __init__(self , *args: typing.Any) -> None: ...
    def Format(self, logEvent: Serilog.Events.LogEvent, output: System.IO.TextWriter) -> None: ...

