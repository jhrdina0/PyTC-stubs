import Serilog.Events
import Serilog.Formatting
import Serilog.Sinks.SystemConsole.Themes
import System

class ConsoleSink:
    def __init__(self, theme: Serilog.Sinks.SystemConsole.Themes.ConsoleTheme, formatter: Serilog.Formatting.ITextFormatter, standardErrorFromLevel: list[Serilog.Events.LogEventLevel]) -> None: ...
    def Emit(self, logEvent: Serilog.Events.LogEvent) -> None: ...

