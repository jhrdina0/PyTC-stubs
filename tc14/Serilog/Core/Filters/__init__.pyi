import Serilog.Events
import System

class DelegateFilter:
    def __init__(self, isEnabled: dict[Serilog.Events.LogEvent, bool]) -> None: ...
    def IsEnabled(self, logEvent: Serilog.Events.LogEvent) -> bool: ...

