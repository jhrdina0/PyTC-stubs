import System.Collections

class EnvironmentInfo:
    def __init__(self, ) -> None: ...
    def LoadEnvironment(self, expression: str) -> None: ...
    def LoadAllEnvironments(self) -> None: ...
    def GetEnvironments(self) -> System.Collections.ArrayList: ...
    def GetEnvironment(self, envName: str) -> Environment: ...
    def GetEnvsForVersion(self, expression: str) -> System.Collections.ArrayList: ...
    def GetEnvironmentsForURL(self, inURL: str) -> System.Collections.ArrayList: ...

class EnvironmentInfo:
    def __init__(self, ) -> None: ...
    def LoadEnvironment(self, expression: str) -> None: ...
    def LoadAllEnvironments(self) -> None: ...
    def GetEnvironments(self) -> System.Collections.ArrayList: ...
    def GetEnvironment(self, envName: str) -> Environment: ...
    def GetEnvsForVersion(self, expression: str) -> System.Collections.ArrayList: ...
    def GetEnvironmentsForURL(self, inURL: str) -> System.Collections.ArrayList: ...

class Environment:
    def __init__(self, ) -> None: ...
    def SetService(self, type: str, value: Service) -> None: ...
    def GetService(self, type: str) -> Service: ...
    def GetName(self) -> str: ...
    def SetName(self, val: str) -> None: ...
    def GetIndex(self) -> int: ...
    def SetIndex(self, val: str) -> None: ...

class EnvironmentInfoWrapper:
    def __init__(self, ) -> None: ...
    def GetEnvironments(self) -> System.Collections.ArrayList: ...
    def GetEnvsForVersion(self, expression: str) -> System.Collections.ArrayList: ...
    def LoadAllEnvironments(self) -> None: ...
    def GetEnvironment(self, envName: str) -> Environment: ...
    def GetEnvironmentsForURL(self, inURL: str) -> System.Collections.ArrayList: ...

class Service:
    def __init__(self, ) -> None: ...
    def SetProperty(self, name: str, value: str) -> None: ...
    def GetProperty(self, name: str) -> str: ...

class Environment:
    def __init__(self, ) -> None: ...
    def SetService(self, type: str, value: Service) -> None: ...
    def GetService(self, type: str) -> Service: ...
    def GetName(self) -> str: ...
    def SetName(self, val: str) -> None: ...
    def GetIndex(self) -> int: ...
    def SetIndex(self, val: str) -> None: ...

class EnvironmentInfoWrapper:
    def __init__(self, ) -> None: ...
    def GetEnvironments(self) -> System.Collections.ArrayList: ...
    def GetEnvsForVersion(self, expression: str) -> System.Collections.ArrayList: ...
    def LoadAllEnvironments(self) -> None: ...
    def GetEnvironment(self, envName: str) -> Environment: ...
    def GetEnvironmentsForURL(self, inURL: str) -> System.Collections.ArrayList: ...

class Service:
    def __init__(self, ) -> None: ...
    def SetProperty(self, name: str, value: str) -> None: ...
    def GetProperty(self, name: str) -> str: ...

