import Serilog.Events
import System.IO

class RawFormatter:
    def __init__(self, ) -> None: ...
    def Format(self, logEvent: Serilog.Events.LogEvent, output: System.IO.TextWriter) -> None: ...

