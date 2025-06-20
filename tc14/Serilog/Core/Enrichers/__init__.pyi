import Serilog.Core
import Serilog.Events
import System
import System.Collections.Generic

class ConditionalEnricher:
    def __init__(self, wrapped: Serilog.Core.ILogEventEnricher, condition: dict[Serilog.Events.LogEvent, bool]) -> None: ...
    def Enrich(self, logEvent: Serilog.Events.LogEvent, propertyFactory: Serilog.Core.ILogEventPropertyFactory) -> None: ...
    def Dispose(self) -> None: ...

class EmptyEnricher:
    def __init__(self, ) -> None: ...
    def Enrich(self, logEvent: Serilog.Events.LogEvent, propertyFactory: Serilog.Core.ILogEventPropertyFactory) -> None: ...

class FixedPropertyEnricher:
    def __init__(self, eventProperty: Serilog.Events.EventProperty&) -> None: ...
    def Enrich(self, logEvent: Serilog.Events.LogEvent, propertyFactory: Serilog.Core.ILogEventPropertyFactory) -> None: ...

class PropertyEnricher:
    def __init__(self, name: str, value: typing.Any, destructureObjects: bool = False) -> None: ...
    def Enrich(self, logEvent: Serilog.Events.LogEvent, propertyFactory: Serilog.Core.ILogEventPropertyFactory) -> None: ...

class SafeAggregateEnricher:
    def __init__(self, enrichers: list[Serilog.Core.ILogEventEnricher]) -> None: ...
    def Enrich(self, logEvent: Serilog.Events.LogEvent, propertyFactory: Serilog.Core.ILogEventPropertyFactory) -> None: ...

