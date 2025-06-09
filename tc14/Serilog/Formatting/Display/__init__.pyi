import Serilog.Events
import System
import System.Collections.Generic
import System.IO

class LevelOutputFormat:
    @staticmethod
    def GetLevelMoniker(value: Serilog.Events.LogEventLevel, format: str) -> str: ...

class MessageTemplateTextFormatter:
    def __init__(self, outputTemplate: str, formatProvider: System.IFormatProvider) -> None: ...
    def Format(self, logEvent: Serilog.Events.LogEvent, output: System.IO.TextWriter) -> None: ...

class OutputProperties:
    MessagePropertyName: str
    TimestampPropertyName: str
    LevelPropertyName: str
    NewLinePropertyName: str
    ExceptionPropertyName: str
    PropertiesPropertyName: str
    @staticmethod
    def GetOutputProperties(logEvent: Serilog.Events.LogEvent) -> dict[str, Serilog.Events.LogEventPropertyValue]: ...

class PropertiesOutputFormat:
    @staticmethod
    def Render(template: Serilog.Events.MessageTemplate, properties: dict[str, Serilog.Events.LogEventPropertyValue], outputTemplate: Serilog.Events.MessageTemplate, output: System.IO.TextWriter, format: str, formatProvider: System.IFormatProvider) -> None: ...

class <>c:
    def __init__(self, ) -> None: ...
    <>9: <>c
    <>9__8_0: dict[dict[str, Serilog.Events.LogEventPropertyValue], str]
    <>9__8_1: dict[dict[str, Serilog.Events.LogEventPropertyValue], Serilog.Events.LogEventPropertyValue]

class <>c__DisplayClass1_0:
    def __init__(self, ) -> None: ...
    template: Serilog.Events.MessageTemplate
    outputTemplate: Serilog.Events.MessageTemplate

class <>c:
    def __init__(self, ) -> None: ...
    <>9: <>c
    <>9__1_1: dict[dict[str, Serilog.Events.LogEventPropertyValue], Serilog.Events.LogEventProperty]

