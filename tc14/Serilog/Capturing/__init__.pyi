import Serilog.Events
import Serilog.Parsing
import System
import System.Collections
import System.Collections.Generic
import System.Reflection
import typing

class PropertyValueConverter:
    def __init__(self, maximumDestructuringDepth: int, maximumStringLength: int, maximumCollectionCount: int, additionalScalarTypes: list[System.Type], additionalDestructuringPolicies: list[Serilog.Core.IDestructuringPolicy], propagateExceptions: bool) -> None: ...
    def CreateProperty(self, name: str, value: typing.Any, destructureObjects: bool = False) -> Serilog.Events.LogEventProperty: ...
    @typing.overload
    def CreatePropertyValue(self, value: typing.Any, destructureObjects: bool = False) -> Serilog.Events.LogEventPropertyValue: ...
    @typing.overload
    def CreatePropertyValue(self, value: typing.Any, destructuring: Serilog.Parsing.Destructuring) -> Serilog.Events.LogEventPropertyValue: ...

class GetablePropertyFinder:
    pass

class MessageTemplateProcessor:
    def __init__(self, propertyValueConverter: PropertyValueConverter) -> None: ...
    def Process(self, messageTemplate: str, messageTemplateParameters: list[typing.Any], parsedTemplate: Serilog.Events.MessageTemplate&, properties: Serilog.Events.EventProperty[]&) -> None: ...
    def CreateProperty(self, name: str, value: typing.Any, destructureObjects: bool = False) -> Serilog.Events.LogEventProperty: ...
    def CreatePropertyValue(self, value: typing.Any, destructureObjects: bool = False) -> Serilog.Events.LogEventPropertyValue: ...

class PropertyBinder:
    def __init__(self, valueConverter: PropertyValueConverter) -> None: ...
    def ConstructProperties(self, messageTemplate: Serilog.Events.MessageTemplate, messageTemplateParameters: list[typing.Any]) -> list[Serilog.Events.EventProperty]: ...

class DepthLimiter:
    def __init__(self, maximumDepth: int, propertyValueConverter: PropertyValueConverter) -> None: ...
    @staticmethod
    def SetCurrentDepth(depth: int) -> None: ...
    def CreatePropertyValue(self, value: typing.Any, destructuring: Serilog.Parsing.Destructuring) -> Serilog.Events.LogEventPropertyValue: ...

class <GetProperties>d__21:
    def __init__(self, <>1__state: int) -> None: ...
    <>3__value: typing.Any
    <>4__this: PropertyValueConverter

class <<TryConvertEnumerable>g__MapToDictionaryElements|14_0>d:
    def __init__(self, <>1__state: int) -> None: ...
    <>3__dictionaryEntries: System.Collections.IDictionary
    <>4__this: PropertyValueConverter
    <>3__destructure: Serilog.Parsing.Destructuring

class <<TryConvertEnumerable>g__MapToSequenceElements|14_1>d:
    def __init__(self, <>1__state: int) -> None: ...
    <>3__sequence: System.Collections.IEnumerable
    <>4__this: PropertyValueConverter
    <>3__destructure: Serilog.Parsing.Destructuring

class <>c__DisplayClass0_0:
    def __init__(self, ) -> None: ...
    seenNames: list[str]
    <>9__0: dict[System.Reflection.PropertyInfo, bool]

class <GetPropertiesRecursive>d__0:
    def __init__(self, <>1__state: int) -> None: ...
    <>3__type: System.Type

