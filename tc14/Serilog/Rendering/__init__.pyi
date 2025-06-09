import Serilog.Events
import Serilog.Parsing
import System
import System.Collections.Generic
import System.IO

class Casing:
    @staticmethod
    def Format(value: str, format: str) -> str: ...

class MessageTemplateRenderer:
    @staticmethod
    def Render(messageTemplate: Serilog.Events.MessageTemplate, properties: dict[str, Serilog.Events.LogEventPropertyValue], output: System.IO.TextWriter, format: str, formatProvider: System.IFormatProvider) -> None: ...
    @staticmethod
    def RenderTextToken(tt: Serilog.Parsing.TextToken, output: System.IO.TextWriter) -> None: ...
    @staticmethod
    def RenderPropertyToken(pt: Serilog.Parsing.PropertyToken, properties: dict[str, Serilog.Events.LogEventPropertyValue], output: System.IO.TextWriter, formatProvider: System.IFormatProvider, isLiteral: bool, isJson: bool) -> None: ...

class Padding:
    @staticmethod
    def Apply(output: System.IO.TextWriter, value: str, alignment: list[Serilog.Parsing.Alignment]) -> None: ...

