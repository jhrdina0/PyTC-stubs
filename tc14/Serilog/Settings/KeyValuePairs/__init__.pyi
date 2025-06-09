import Serilog
import System
import System.Collections.Generic
import System.Linq
import System.Reflection
import System.Text.RegularExpressions

class CallableConfigurationMethodFinder:
    pass

class KeyValuePairSettings:
    def __init__(self, settings: dict[str, str]) -> None: ...
    def Configure(self, loggerConfiguration: Serilog.LoggerConfiguration) -> None: ...

class SettingValueConversions:
    def __init__(self, ) -> None: ...
    @staticmethod
    def ConvertToType(value: str, toType: System.Type) -> typing.Any: ...

class SurrogateConfigurationMethods:
    pass

class <>c__DisplayClass0_0:
    def __init__(self, ) -> None: ...
    configType: System.Type

class <>c:
    def __init__(self, ) -> None: ...
    <>9: <>c
    <>9__0_4: dict[System.Type, System.Reflection.TypeInfo]
    <>9__0_5: dict[System.Reflection.TypeInfo, bool]
    <>9__0_0: dict[System.Reflection.Assembly, list[System.Reflection.TypeInfo]]
    <>9__0_1: dict[System.Reflection.TypeInfo, list[System.Reflection.MethodInfo]]
    <>9__0_2: dict[System.Reflection.MethodInfo, bool]

class ConfigurationMethodCall:
    def __init__(self, ) -> None: ...
    MethodName: str
    ArgumentName: str
    Value: str
    def get_MethodName(self) -> str: ...
    def set_MethodName(self, value: str) -> None: ...
    def get_ArgumentName(self) -> str: ...
    def set_ArgumentName(self, value: str) -> None: ...
    def get_Value(self) -> str: ...
    def set_Value(self, value: str) -> None: ...

class <>c__DisplayClass21_0:
    def __init__(self, ) -> None: ...
    matchCallables: System.Text.RegularExpressions.Regex

class <>c:
    def __init__(self, ) -> None: ...
    <>9: <>c
    <>9__21_0: dict[dict[str, str], bool]
    <>9__21_1: dict[dict[str, str], str]
    <>9__21_2: dict[dict[str, str], str]
    <>9__21_6: dict[dict[str, str], bool]
    <>9__21_7: dict[dict[str, str], bool]
    <>9__21_5: dict[dict[dict[str, str], System.Text.RegularExpressions.Match], dict[System.Type, ConfigurationMethodCall]]
    <>9__21_8: dict[dict[System.Type, ConfigurationMethodCall], System.Type]
    <>9__21_9: dict[dict[System.Type, ConfigurationMethodCall], ConfigurationMethodCall]
    <>9__21_10: dict[ConfigurationMethodCall, str]
    <>9__23_2: dict[dict[dict[str, str], System.Text.RegularExpressions.Match], dict[str, str]]
    <>9__28_0: dict[dict[str, str], bool]

class <>c__DisplayClass23_0:
    def __init__(self, ) -> None: ...
    matchLevelSwitchDeclarations: System.Text.RegularExpressions.Regex

class <>c__DisplayClass26_0:
    def __init__(self, ) -> None: ...
    declaredSwitches: dict[str, Serilog.Core.LoggingLevelSwitch]
    <>9__1: dict[dict[System.Reflection.ParameterInfo, ConfigurationMethodCall], typing.Any]

class <>c__DisplayClass26_1:
    def __init__(self, ) -> None: ...
    directiveInfo: dict[str, ConfigurationMethodCall]

class <>c__DisplayClass26_2:
    def __init__(self, ) -> None: ...
    p: System.Reflection.ParameterInfo

class <>c__DisplayClass27_0:
    def __init__(self, ) -> None: ...
    name: str
    suppliedArgumentValues: list[ConfigurationMethodCall]
    <>9__2: dict[System.Reflection.ParameterInfo, bool]
    <>9__4: dict[System.Reflection.ParameterInfo, bool]

class <>c__DisplayClass27_1:
    def __init__(self, ) -> None: ...
    p: System.Reflection.ParameterInfo

class <>c__DisplayClass27_2:
    def __init__(self, ) -> None: ...
    p: System.Reflection.ParameterInfo

class <>c__DisplayClass2_0:
    def __init__(self, ) -> None: ...
    toTypeInfo: System.Reflection.TypeInfo

class <>c__DisplayClass2_1:
    def __init__(self, ) -> None: ...
    memberName: str

class <>c:
    def __init__(self, ) -> None: ...
    <>9: <>c
    <>9__2_1: dict[dict[System.Type, dict[str, typing.Any]], dict[str, typing.Any]]
    <>9__2_3: dict[System.Reflection.PropertyInfo, bool]
    <>9__2_4: dict[System.Reflection.PropertyInfo, bool]
    <>9__2_5: dict[System.Reflection.PropertyInfo, bool]
    <>9__2_7: dict[System.Reflection.FieldInfo, bool]
    <>9__2_8: dict[System.Reflection.FieldInfo, bool]
    <>9__2_11: dict[System.Reflection.ParameterInfo, bool]
    <>9__2_9: dict[System.Reflection.ConstructorInfo, bool]
    <>9__2_10: dict[System.Reflection.ParameterInfo, typing.Any]

class <>c:
    def __init__(self, ) -> None: ...
    <>9: <>c

