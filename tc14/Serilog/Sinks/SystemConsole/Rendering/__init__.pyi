import Serilog.Events
import Serilog.Parsing
import Serilog.Sinks.SystemConsole.Formatting
import Serilog.Sinks.SystemConsole.Themes
import System
import System.Collections.Generic
import System.IO

class AlignmentExtensions:
    @staticmethod
    def Widen(alignment: Serilog.Parsing.Alignment, amount: int) -> Serilog.Parsing.Alignment: ...

class Casing:
    @staticmethod
    def Format(value: str, format: str) -> str: ...

class Padding:
    @staticmethod
    def Apply(output: System.IO.TextWriter, value: str, alignment: list[Serilog.Parsing.Alignment]) -> None: ...

class ThemedMessageTemplateRenderer:
    def __init__(self, theme: Serilog.Sinks.SystemConsole.Themes.ConsoleTheme, valueFormatter: Serilog.Sinks.SystemConsole.Formatting.ThemedValueFormatter, isLiteral: bool) -> None: ...
    def Render(self, template: Serilog.Events.MessageTemplate, properties: dict[str, Serilog.Events.LogEventPropertyValue], output: System.IO.TextWriter) -> int: ...

