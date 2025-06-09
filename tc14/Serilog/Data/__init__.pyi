import typing

TState = typing.TypeVar('TState')

class LogEventPropertyValueRewriter[TState](dict[TState, Serilog.Events.LogEventPropertyValue]):
    pass

TState = typing.TypeVar('TState'), TResult = typing.TypeVar('TResult')

class LogEventPropertyValueVisitor[TState, TResult]:
    pass

