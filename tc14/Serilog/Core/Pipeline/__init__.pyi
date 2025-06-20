import Serilog
import Serilog.Core
import Serilog.Events
import System
import System.Collections.Generic
import typing

class MessageTemplateCache:
    def __init__(self, innerParser: Serilog.Core.IMessageTemplateParser) -> None: ...
    def Parse(self, messageTemplate: str) -> Serilog.Events.MessageTemplate: ...

class SilentLogger:
    Instance: Serilog.ILogger
    @typing.overload
    def ForContext(self, enricher: Serilog.Core.ILogEventEnricher) -> Serilog.ILogger: ...
    @typing.overload
    def ForContext(self, enrichers: list[Serilog.Core.ILogEventEnricher]) -> Serilog.ILogger: ...
    @typing.overload
    def ForContext(self, propertyName: str, value: typing.Any, destructureObjects: bool = False) -> Serilog.ILogger: ...
    @typing.overload
    def ForContext(self) -> Serilog.ILogger: ...
    @typing.overload
    def ForContext(self, source: System.Type) -> Serilog.ILogger: ...
    @typing.overload
    def Write(self, logEvent: Serilog.Events.LogEvent) -> None: ...
    @typing.overload
    def Write(self, level: Serilog.Events.LogEventLevel, messageTemplate: str) -> None: ...
    @typing.overload
    def Write(self, level: Serilog.Events.LogEventLevel, messageTemplate: str, propertyValue: T) -> None: ...
    @typing.overload
    def Write(self, level: Serilog.Events.LogEventLevel, messageTemplate: str, propertyValue0: T0, propertyValue1: T1) -> None: ...
    @typing.overload
    def Write(self, level: Serilog.Events.LogEventLevel, messageTemplate: str, propertyValue0: T0, propertyValue1: T1, propertyValue2: T2) -> None: ...
    @typing.overload
    def Write(self, level: Serilog.Events.LogEventLevel, messageTemplate: str, propertyValues: list[typing.Any]) -> None: ...
    @typing.overload
    def Write(self, level: Serilog.Events.LogEventLevel, exception: System.Exception, messageTemplate: str) -> None: ...
    @typing.overload
    def Write(self, level: Serilog.Events.LogEventLevel, exception: System.Exception, messageTemplate: str, propertyValue: T) -> None: ...
    @typing.overload
    def Write(self, level: Serilog.Events.LogEventLevel, exception: System.Exception, messageTemplate: str, propertyValue0: T0, propertyValue1: T1) -> None: ...
    @typing.overload
    def Write(self, level: Serilog.Events.LogEventLevel, exception: System.Exception, messageTemplate: str, propertyValue0: T0, propertyValue1: T1, propertyValue2: T2) -> None: ...
    @typing.overload
    def Write(self, level: Serilog.Events.LogEventLevel, exception: System.Exception, messageTemplate: str, propertyValues: list[typing.Any]) -> None: ...
    def IsEnabled(self, level: Serilog.Events.LogEventLevel) -> bool: ...
    @typing.overload
    def Verbose(self, messageTemplate: str) -> None: ...
    @typing.overload
    def Verbose(self, messageTemplate: str, propertyValue: T) -> None: ...
    @typing.overload
    def Verbose(self, messageTemplate: str, propertyValue0: T0, propertyValue1: T1) -> None: ...
    @typing.overload
    def Verbose(self, messageTemplate: str, propertyValue0: T0, propertyValue1: T1, propertyValue2: T2) -> None: ...
    @typing.overload
    def Verbose(self, messageTemplate: str, propertyValues: list[typing.Any]) -> None: ...
    @typing.overload
    def Verbose(self, exception: System.Exception, messageTemplate: str) -> None: ...
    @typing.overload
    def Verbose(self, exception: System.Exception, messageTemplate: str, propertyValue: T) -> None: ...
    @typing.overload
    def Verbose(self, exception: System.Exception, messageTemplate: str, propertyValue0: T0, propertyValue1: T1) -> None: ...
    @typing.overload
    def Verbose(self, exception: System.Exception, messageTemplate: str, propertyValue0: T0, propertyValue1: T1, propertyValue2: T2) -> None: ...
    @typing.overload
    def Verbose(self, exception: System.Exception, messageTemplate: str, propertyValues: list[typing.Any]) -> None: ...
    @typing.overload
    def Debug(self, messageTemplate: str) -> None: ...
    @typing.overload
    def Debug(self, messageTemplate: str, propertyValue: T) -> None: ...
    @typing.overload
    def Debug(self, messageTemplate: str, propertyValue0: T0, propertyValue1: T1) -> None: ...
    @typing.overload
    def Debug(self, messageTemplate: str, propertyValue0: T0, propertyValue1: T1, propertyValue2: T2) -> None: ...
    @typing.overload
    def Debug(self, messageTemplate: str, propertyValues: list[typing.Any]) -> None: ...
    @typing.overload
    def Debug(self, exception: System.Exception, messageTemplate: str) -> None: ...
    @typing.overload
    def Debug(self, exception: System.Exception, messageTemplate: str, propertyValue: T) -> None: ...
    @typing.overload
    def Debug(self, exception: System.Exception, messageTemplate: str, propertyValue0: T0, propertyValue1: T1) -> None: ...
    @typing.overload
    def Debug(self, exception: System.Exception, messageTemplate: str, propertyValue0: T0, propertyValue1: T1, propertyValue2: T2) -> None: ...
    @typing.overload
    def Debug(self, exception: System.Exception, messageTemplate: str, propertyValues: list[typing.Any]) -> None: ...
    @typing.overload
    def Information(self, messageTemplate: str) -> None: ...
    @typing.overload
    def Information(self, messageTemplate: str, propertyValue: T) -> None: ...
    @typing.overload
    def Information(self, messageTemplate: str, propertyValue0: T0, propertyValue1: T1) -> None: ...
    @typing.overload
    def Information(self, messageTemplate: str, propertyValue0: T0, propertyValue1: T1, propertyValue2: T2) -> None: ...
    @typing.overload
    def Information(self, messageTemplate: str, propertyValues: list[typing.Any]) -> None: ...
    @typing.overload
    def Information(self, exception: System.Exception, messageTemplate: str) -> None: ...
    @typing.overload
    def Information(self, exception: System.Exception, messageTemplate: str, propertyValue: T) -> None: ...
    @typing.overload
    def Information(self, exception: System.Exception, messageTemplate: str, propertyValue0: T0, propertyValue1: T1) -> None: ...
    @typing.overload
    def Information(self, exception: System.Exception, messageTemplate: str, propertyValue0: T0, propertyValue1: T1, propertyValue2: T2) -> None: ...
    @typing.overload
    def Information(self, exception: System.Exception, messageTemplate: str, propertyValues: list[typing.Any]) -> None: ...
    @typing.overload
    def Warning(self, messageTemplate: str) -> None: ...
    @typing.overload
    def Warning(self, messageTemplate: str, propertyValue: T) -> None: ...
    @typing.overload
    def Warning(self, messageTemplate: str, propertyValue0: T0, propertyValue1: T1) -> None: ...
    @typing.overload
    def Warning(self, messageTemplate: str, propertyValue0: T0, propertyValue1: T1, propertyValue2: T2) -> None: ...
    @typing.overload
    def Warning(self, messageTemplate: str, propertyValues: list[typing.Any]) -> None: ...
    @typing.overload
    def Warning(self, exception: System.Exception, messageTemplate: str) -> None: ...
    @typing.overload
    def Warning(self, exception: System.Exception, messageTemplate: str, propertyValue: T) -> None: ...
    @typing.overload
    def Warning(self, exception: System.Exception, messageTemplate: str, propertyValue0: T0, propertyValue1: T1) -> None: ...
    @typing.overload
    def Warning(self, exception: System.Exception, messageTemplate: str, propertyValue0: T0, propertyValue1: T1, propertyValue2: T2) -> None: ...
    @typing.overload
    def Warning(self, exception: System.Exception, messageTemplate: str, propertyValues: list[typing.Any]) -> None: ...
    @typing.overload
    def Error(self, messageTemplate: str) -> None: ...
    @typing.overload
    def Error(self, messageTemplate: str, propertyValue: T) -> None: ...
    @typing.overload
    def Error(self, messageTemplate: str, propertyValue0: T0, propertyValue1: T1) -> None: ...
    @typing.overload
    def Error(self, messageTemplate: str, propertyValue0: T0, propertyValue1: T1, propertyValue2: T2) -> None: ...
    @typing.overload
    def Error(self, messageTemplate: str, propertyValues: list[typing.Any]) -> None: ...
    @typing.overload
    def Error(self, exception: System.Exception, messageTemplate: str) -> None: ...
    @typing.overload
    def Error(self, exception: System.Exception, messageTemplate: str, propertyValue: T) -> None: ...
    @typing.overload
    def Error(self, exception: System.Exception, messageTemplate: str, propertyValue0: T0, propertyValue1: T1) -> None: ...
    @typing.overload
    def Error(self, exception: System.Exception, messageTemplate: str, propertyValue0: T0, propertyValue1: T1, propertyValue2: T2) -> None: ...
    @typing.overload
    def Error(self, exception: System.Exception, messageTemplate: str, propertyValues: list[typing.Any]) -> None: ...
    @typing.overload
    def Fatal(self, messageTemplate: str) -> None: ...
    @typing.overload
    def Fatal(self, messageTemplate: str, propertyValue: T) -> None: ...
    @typing.overload
    def Fatal(self, messageTemplate: str, propertyValue0: T0, propertyValue1: T1) -> None: ...
    @typing.overload
    def Fatal(self, messageTemplate: str, propertyValue0: T0, propertyValue1: T1, propertyValue2: T2) -> None: ...
    @typing.overload
    def Fatal(self, messageTemplate: str, propertyValues: list[typing.Any]) -> None: ...
    @typing.overload
    def Fatal(self, exception: System.Exception, messageTemplate: str) -> None: ...
    @typing.overload
    def Fatal(self, exception: System.Exception, messageTemplate: str, propertyValue: T) -> None: ...
    @typing.overload
    def Fatal(self, exception: System.Exception, messageTemplate: str, propertyValue0: T0, propertyValue1: T1) -> None: ...
    @typing.overload
    def Fatal(self, exception: System.Exception, messageTemplate: str, propertyValue0: T0, propertyValue1: T1, propertyValue2: T2) -> None: ...
    @typing.overload
    def Fatal(self, exception: System.Exception, messageTemplate: str, propertyValues: list[typing.Any]) -> None: ...
    def BindMessageTemplate(self, messageTemplate: str, propertyValues: list[typing.Any], parsedTemplate: Serilog.Events.MessageTemplate&, boundProperties: System.Collections.Generic.IEnumerable`1[[Serilog.Events.LogEventProperty, Serilog, Version=2.0.0.0, Culture=neutral, PublicKeyToken=24c2f752a8e58a10]]&) -> bool: ...
    def BindProperty(self, propertyName: str, value: typing.Any, destructureObjects: bool, property: Serilog.Events.LogEventProperty&) -> bool: ...

