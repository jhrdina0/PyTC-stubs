import Newtonsoft.Json
import System
import System.Collections.Generic
import System.IO
import typing

class BsonBinaryType(System.Enum, int):
    Binary: BsonBinaryType = ...
    Function: BsonBinaryType = ...
    BinaryOld: BsonBinaryType = ...
    UuidOld: BsonBinaryType = ...
    Uuid: BsonBinaryType = ...
    Md5: BsonBinaryType = ...
    UserDefined: BsonBinaryType = ...

class BsonBinaryWriter:
    def __init__(self, writer: System.IO.BinaryWriter) -> None: ...
    DateTimeKindHandling: System.DateTimeKind
    def get_DateTimeKindHandling(self) -> System.DateTimeKind: ...
    def set_DateTimeKindHandling(self, value: System.DateTimeKind) -> None: ...
    def Flush(self) -> None: ...
    def Close(self) -> None: ...
    def WriteToken(self, t: BsonToken) -> None: ...
    def WriteUtf8Bytes(self, s: str, byteCount: int) -> None: ...

class BsonObjectId:
    def __init__(self, value: list[System.Byte]) -> None: ...
    Value: list[System.Byte]
    def get_Value(self) -> list[System.Byte]: ...

class BsonReader(Newtonsoft.Json.JsonReader):
    @typing.overload
    def __init__(self, stream: System.IO.Stream) -> None: ...
    @typing.overload
    def __init__(self, reader: System.IO.BinaryReader) -> None: ...
    @typing.overload
    def __init__(self, stream: System.IO.Stream, readRootValueAsArray: bool, dateTimeKindHandling: System.DateTimeKind) -> None: ...
    @typing.overload
    def __init__(self, reader: System.IO.BinaryReader, readRootValueAsArray: bool, dateTimeKindHandling: System.DateTimeKind) -> None: ...
    JsonNet35BinaryCompatibility: bool
    ReadRootValueAsArray: bool
    DateTimeKindHandling: System.DateTimeKind
    def get_JsonNet35BinaryCompatibility(self) -> bool: ...
    def set_JsonNet35BinaryCompatibility(self, value: bool) -> None: ...
    def get_ReadRootValueAsArray(self) -> bool: ...
    def set_ReadRootValueAsArray(self, value: bool) -> None: ...
    def get_DateTimeKindHandling(self) -> System.DateTimeKind: ...
    def set_DateTimeKindHandling(self, value: System.DateTimeKind) -> None: ...
    def Read(self) -> bool: ...
    def Close(self) -> None: ...

class BsonToken:
    Type: BsonType
    Parent: BsonToken
    CalculatedSize: int
    def get_Type(self) -> BsonType: ...
    @staticmethod
    def get_Parent() -> BsonToken: ...
    def set_Parent(self, value: BsonToken) -> None: ...
    def get_CalculatedSize(self) -> int: ...
    def set_CalculatedSize(self, value: int) -> None: ...

class BsonObject(BsonToken):
    def __init__(self, ) -> None: ...
    Type: BsonType
    def Add(self, name: str, token: BsonToken) -> None: ...
    def get_Type(self) -> BsonType: ...
    def GetEnumerator(self) -> list[BsonProperty]: ...

class BsonArray(BsonToken):
    def __init__(self, ) -> None: ...
    Type: BsonType
    def Add(self, token: BsonToken) -> None: ...
    def get_Type(self) -> BsonType: ...
    def GetEnumerator(self) -> list[BsonToken]: ...

class BsonEmpty(BsonToken):
    Null: BsonToken
    Undefined: BsonToken
    Type: BsonType
    def get_Type(self) -> BsonType: ...

class BsonValue(BsonToken):
    def __init__(self, value: typing.Any, type: BsonType) -> None: ...
    Value: typing.Any
    Type: BsonType
    def get_Value(self) -> typing.Any: ...
    def get_Type(self) -> BsonType: ...

class BsonBoolean(BsonValue):
    False: BsonBoolean
    True: BsonBoolean

class BsonString(BsonValue):
    def __init__(self, value: typing.Any, includeLength: bool) -> None: ...
    ByteCount: int
    IncludeLength: bool
    def get_ByteCount(self) -> int: ...
    def set_ByteCount(self, value: int) -> None: ...
    def get_IncludeLength(self) -> bool: ...

class BsonBinary(BsonValue):
    def __init__(self, value: list[System.Byte], binaryType: BsonBinaryType) -> None: ...
    BinaryType: BsonBinaryType
    def get_BinaryType(self) -> BsonBinaryType: ...
    def set_BinaryType(self, value: BsonBinaryType) -> None: ...

class BsonRegex(BsonToken):
    def __init__(self, pattern: str, options: str) -> None: ...
    Pattern: BsonString
    Options: BsonString
    Type: BsonType
    def get_Pattern(self) -> BsonString: ...
    def set_Pattern(self, value: BsonString) -> None: ...
    def get_Options(self) -> BsonString: ...
    def set_Options(self, value: BsonString) -> None: ...
    def get_Type(self) -> BsonType: ...

class BsonProperty:
    def __init__(self, ) -> None: ...
    Name: BsonString
    Value: BsonToken
    def get_Name(self) -> BsonString: ...
    def set_Name(self, value: BsonString) -> None: ...
    def get_Value(self) -> BsonToken: ...
    def set_Value(self, value: BsonToken) -> None: ...

class BsonType(System.Enum, int):
    Number: BsonType = ...
    String: BsonType = ...
    Object: BsonType = ...
    Array: BsonType = ...
    Binary: BsonType = ...
    Undefined: BsonType = ...
    Oid: BsonType = ...
    Boolean: BsonType = ...
    Date: BsonType = ...
    Null: BsonType = ...
    Regex: BsonType = ...
    Reference: BsonType = ...
    Code: BsonType = ...
    Symbol: BsonType = ...
    CodeWScope: BsonType = ...
    Integer: BsonType = ...
    TimeStamp: BsonType = ...
    Long: BsonType = ...
    MinKey: BsonType = ...
    MaxKey: BsonType = ...

class BsonWriter(Newtonsoft.Json.JsonWriter):
    @typing.overload
    def __init__(self, stream: System.IO.Stream) -> None: ...
    @typing.overload
    def __init__(self, writer: System.IO.BinaryWriter) -> None: ...
    DateTimeKindHandling: System.DateTimeKind
    def get_DateTimeKindHandling(self) -> System.DateTimeKind: ...
    def set_DateTimeKindHandling(self, value: System.DateTimeKind) -> None: ...
    def Flush(self) -> None: ...
    def WriteComment(self, text: str) -> None: ...
    def WriteStartConstructor(self, name: str) -> None: ...
    def WriteRaw(self, json: str) -> None: ...
    def WriteRawValue(self, json: str) -> None: ...
    def WriteStartArray(self) -> None: ...
    def WriteStartObject(self) -> None: ...
    def WritePropertyName(self, name: str) -> None: ...
    def Close(self) -> None: ...
    @typing.overload
    def WriteValue(self, value: typing.Any) -> None: ...
    @typing.overload
    def WriteValue(self, value: str) -> None: ...
    @typing.overload
    def WriteValue(self, value: int) -> None: ...
    @typing.overload
    def WriteValue(self, value: System.UInt32) -> None: ...
    @typing.overload
    def WriteValue(self, value: int) -> None: ...
    @typing.overload
    def WriteValue(self, value: System.UInt64) -> None: ...
    @typing.overload
    def WriteValue(self, value: float) -> None: ...
    @typing.overload
    def WriteValue(self, value: float) -> None: ...
    @typing.overload
    def WriteValue(self, value: bool) -> None: ...
    @typing.overload
    def WriteValue(self, value: int) -> None: ...
    @typing.overload
    def WriteValue(self, value: System.UInt16) -> None: ...
    @typing.overload
    def WriteValue(self, value: System.Char) -> None: ...
    @typing.overload
    def WriteValue(self, value: System.Byte) -> None: ...
    @typing.overload
    def WriteValue(self, value: System.SByte) -> None: ...
    @typing.overload
    def WriteValue(self, value: System.Decimal) -> None: ...
    @typing.overload
    def WriteValue(self, value: System.DateTime) -> None: ...
    @typing.overload
    def WriteValue(self, value: System.DateTimeOffset) -> None: ...
    @typing.overload
    def WriteValue(self, value: list[System.Byte]) -> None: ...
    @typing.overload
    def WriteValue(self, value: System.Guid) -> None: ...
    @typing.overload
    def WriteValue(self, value: System.TimeSpan) -> None: ...
    @typing.overload
    def WriteValue(self, value: System.Uri) -> None: ...
    def WriteNull(self) -> None: ...
    def WriteUndefined(self) -> None: ...
    def WriteObjectId(self, value: list[System.Byte]) -> None: ...
    def WriteRegex(self, pattern: str, options: str) -> None: ...

class BsonReaderState(System.Enum, int):
    Normal: BsonReaderState = ...
    ReferenceStart: BsonReaderState = ...
    ReferenceRef: BsonReaderState = ...
    ReferenceId: BsonReaderState = ...
    CodeWScopeStart: BsonReaderState = ...
    CodeWScopeCode: BsonReaderState = ...
    CodeWScopeScope: BsonReaderState = ...
    CodeWScopeScopeObject: BsonReaderState = ...
    CodeWScopeScopeEnd: BsonReaderState = ...

class ContainerContext:
    def __init__(self, type: BsonType) -> None: ...
    Type: BsonType
    Length: int
    Position: int

