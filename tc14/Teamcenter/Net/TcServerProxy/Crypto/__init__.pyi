import System
import System.Globalization
import typing

class PKCS7:
    @typing.overload
    def __init__(self, ) -> None: ...
    @typing.overload
    def __init__(self, locale: System.Globalization.CultureInfo) -> None: ...
    @typing.overload
    def sign(self, message: str) -> str: ...
    @typing.overload
    def sign(self, messages: list[str]) -> list[typing.Any]: ...
    @typing.overload
    def sign(self, message: list[System.Byte]) -> str: ...
    @typing.overload
    def sign(self, messages: list[list[System.Byte]]) -> list[typing.Any]: ...

class PKCS7:
    @typing.overload
    def __init__(self, ) -> None: ...
    @typing.overload
    def __init__(self, locale: System.Globalization.CultureInfo) -> None: ...
    @typing.overload
    def sign(self, message: str) -> str: ...
    @typing.overload
    def sign(self, messages: list[str]) -> list[typing.Any]: ...
    @typing.overload
    def sign(self, message: list[System.Byte]) -> str: ...
    @typing.overload
    def sign(self, messages: list[list[System.Byte]]) -> list[typing.Any]: ...

