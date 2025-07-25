import Newtonsoft.Json
import Newtonsoft.Json.Serialization
import Newtonsoft.Json.Utilities
import System
import System.Collections.Generic
import System.Globalization
import System.Reflection
import System.Xml
import System.Xml.Linq
import typing

class BinaryConverter(Newtonsoft.Json.JsonConverter):
    def __init__(self, ) -> None: ...
    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> None: ...
    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: System.Type, existingValue: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> typing.Any: ...
    def CanConvert(self, objectType: System.Type) -> bool: ...

class BsonObjectIdConverter(Newtonsoft.Json.JsonConverter):
    def __init__(self, ) -> None: ...
    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> None: ...
    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: System.Type, existingValue: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> typing.Any: ...
    def CanConvert(self, objectType: System.Type) -> bool: ...

T = typing.TypeVar('T')

class CustomCreationConverter[T](Newtonsoft.Json.JsonConverter):
    CanWrite: bool
    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> None: ...
    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: System.Type, existingValue: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> typing.Any: ...
    def Create(self, objectType: System.Type) -> T: ...
    def CanConvert(self, objectType: System.Type) -> bool: ...
    def get_CanWrite(self) -> bool: ...

class DataSetConverter(Newtonsoft.Json.JsonConverter):
    def __init__(self, ) -> None: ...
    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> None: ...
    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: System.Type, existingValue: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> typing.Any: ...
    def CanConvert(self, valueType: System.Type) -> bool: ...

class DataTableConverter(Newtonsoft.Json.JsonConverter):
    def __init__(self, ) -> None: ...
    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> None: ...
    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: System.Type, existingValue: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> typing.Any: ...
    def CanConvert(self, valueType: System.Type) -> bool: ...

class DateTimeConverterBase(Newtonsoft.Json.JsonConverter):
    def CanConvert(self, objectType: System.Type) -> bool: ...

class DiscriminatedUnionConverter(Newtonsoft.Json.JsonConverter):
    def __init__(self, ) -> None: ...
    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> None: ...
    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: System.Type, existingValue: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> typing.Any: ...
    def CanConvert(self, objectType: System.Type) -> bool: ...

class EntityKeyMemberConverter(Newtonsoft.Json.JsonConverter):
    def __init__(self, ) -> None: ...
    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> None: ...
    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: System.Type, existingValue: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> typing.Any: ...
    def CanConvert(self, objectType: System.Type) -> bool: ...

class ExpandoObjectConverter(Newtonsoft.Json.JsonConverter):
    def __init__(self, ) -> None: ...
    CanWrite: bool
    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> None: ...
    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: System.Type, existingValue: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> typing.Any: ...
    def CanConvert(self, objectType: System.Type) -> bool: ...
    def get_CanWrite(self) -> bool: ...

class IsoDateTimeConverter(DateTimeConverterBase):
    def __init__(self, ) -> None: ...
    DateTimeStyles: System.Globalization.DateTimeStyles
    DateTimeFormat: str
    Culture: System.Globalization.CultureInfo
    def get_DateTimeStyles(self) -> System.Globalization.DateTimeStyles: ...
    def set_DateTimeStyles(self, value: System.Globalization.DateTimeStyles) -> None: ...
    def get_DateTimeFormat(self) -> str: ...
    def set_DateTimeFormat(self, value: str) -> None: ...
    def get_Culture(self) -> System.Globalization.CultureInfo: ...
    def set_Culture(self, value: System.Globalization.CultureInfo) -> None: ...
    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> None: ...
    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: System.Type, existingValue: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> typing.Any: ...

class JavaScriptDateTimeConverter(DateTimeConverterBase):
    def __init__(self, ) -> None: ...
    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> None: ...
    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: System.Type, existingValue: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> typing.Any: ...

class KeyValuePairConverter(Newtonsoft.Json.JsonConverter):
    def __init__(self, ) -> None: ...
    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> None: ...
    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: System.Type, existingValue: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> typing.Any: ...
    def CanConvert(self, objectType: System.Type) -> bool: ...

class RegexConverter(Newtonsoft.Json.JsonConverter):
    def __init__(self, ) -> None: ...
    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> None: ...
    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: System.Type, existingValue: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> typing.Any: ...
    def CanConvert(self, objectType: System.Type) -> bool: ...

class StringEnumConverter(Newtonsoft.Json.JsonConverter):
    @typing.overload
    def __init__(self, ) -> None: ...
    @typing.overload
    def __init__(self, camelCaseText: bool) -> None: ...
    @typing.overload
    def __init__(self, namingStrategy: Newtonsoft.Json.Serialization.NamingStrategy, allowIntegerValues: bool = True) -> None: ...
    @typing.overload
    def __init__(self, namingStrategyType: System.Type) -> None: ...
    @typing.overload
    def __init__(self, namingStrategyType: System.Type, namingStrategyParameters: list[typing.Any]) -> None: ...
    @typing.overload
    def __init__(self, namingStrategyType: System.Type, namingStrategyParameters: list[typing.Any], allowIntegerValues: bool) -> None: ...
    CamelCaseText: bool
    NamingStrategy: Newtonsoft.Json.Serialization.NamingStrategy
    AllowIntegerValues: bool
    def get_CamelCaseText(self) -> bool: ...
    def set_CamelCaseText(self, value: bool) -> None: ...
    def get_NamingStrategy(self) -> Newtonsoft.Json.Serialization.NamingStrategy: ...
    def set_NamingStrategy(self, value: Newtonsoft.Json.Serialization.NamingStrategy) -> None: ...
    def get_AllowIntegerValues(self) -> bool: ...
    def set_AllowIntegerValues(self, value: bool) -> None: ...
    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> None: ...
    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: System.Type, existingValue: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> typing.Any: ...
    def CanConvert(self, objectType: System.Type) -> bool: ...

class UnixDateTimeConverter(DateTimeConverterBase):
    def __init__(self, ) -> None: ...
    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> None: ...
    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: System.Type, existingValue: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> typing.Any: ...

class VersionConverter(Newtonsoft.Json.JsonConverter):
    def __init__(self, ) -> None: ...
    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> None: ...
    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: System.Type, existingValue: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> typing.Any: ...
    def CanConvert(self, objectType: System.Type) -> bool: ...

class XmlDocumentWrapper(XmlNodeWrapper):
    def __init__(self, document: System.Xml.XmlDocument) -> None: ...
    DocumentElement: IXmlElement
    def CreateComment(self, data: str) -> IXmlNode: ...
    def CreateTextNode(self, text: str) -> IXmlNode: ...
    def CreateCDataSection(self, data: str) -> IXmlNode: ...
    def CreateWhitespace(self, text: str) -> IXmlNode: ...
    def CreateSignificantWhitespace(self, text: str) -> IXmlNode: ...
    def CreateXmlDeclaration(self, version: str, encoding: str, standalone: str) -> IXmlNode: ...
    def CreateXmlDocumentType(self, name: str, publicId: str, systemId: str, internalSubset: str) -> IXmlNode: ...
    def CreateProcessingInstruction(self, target: str, data: str) -> IXmlNode: ...
    @typing.overload
    def CreateElement(self, elementName: str) -> IXmlElement: ...
    @typing.overload
    def CreateElement(self, qualifiedName: str, namespaceUri: str) -> IXmlElement: ...
    @typing.overload
    def CreateAttribute(self, name: str, value: str) -> IXmlNode: ...
    @typing.overload
    def CreateAttribute(self, qualifiedName: str, namespaceUri: str, value: str) -> IXmlNode: ...
    def get_DocumentElement(self) -> IXmlElement: ...

class XmlElementWrapper(XmlNodeWrapper):
    def __init__(self, element: System.Xml.XmlElement) -> None: ...
    IsEmpty: bool
    def SetAttributeNode(self, attribute: IXmlNode) -> None: ...
    def GetPrefixOfNamespace(self, namespaceUri: str) -> str: ...
    def get_IsEmpty(self) -> bool: ...

class XmlDeclarationWrapper(XmlNodeWrapper):
    def __init__(self, declaration: System.Xml.XmlDeclaration) -> None: ...
    Version: str
    Encoding: str
    Standalone: str
    def get_Version(self) -> str: ...
    def get_Encoding(self) -> str: ...
    def set_Encoding(self, value: str) -> None: ...
    def get_Standalone(self) -> str: ...
    def set_Standalone(self, value: str) -> None: ...

class XmlDocumentTypeWrapper(XmlNodeWrapper):
    def __init__(self, documentType: System.Xml.XmlDocumentType) -> None: ...
    Name: str
    System: str
    Public: str
    InternalSubset: str
    LocalName: str
    def get_Name(self) -> str: ...
    def get_System(self) -> str: ...
    def get_Public(self) -> str: ...
    def get_InternalSubset(self) -> str: ...
    def get_LocalName(self) -> str: ...

class XmlNodeWrapper:
    def __init__(self, node: System.Xml.XmlNode) -> None: ...
    WrappedNode: typing.Any
    NodeType: System.Xml.XmlNodeType
    LocalName: str
    ChildNodes: list[IXmlNode]
    Attributes: list[IXmlNode]
    ParentNode: IXmlNode
    Value: str
    NamespaceUri: str
    def get_WrappedNode(self) -> typing.Any: ...
    def get_NodeType(self) -> System.Xml.XmlNodeType: ...
    def get_LocalName(self) -> str: ...
    def get_ChildNodes(self) -> list[IXmlNode]: ...
    def get_Attributes(self) -> list[IXmlNode]: ...
    def get_ParentNode(self) -> IXmlNode: ...
    def get_Value(self) -> str: ...
    def set_Value(self, value: str) -> None: ...
    def AppendChild(self, newChild: IXmlNode) -> IXmlNode: ...
    def get_NamespaceUri(self) -> str: ...

class IXmlDocument:
    def __init__(self , *args: typing.Any) -> None: ...
    DocumentElement: IXmlElement
    def CreateComment(self, text: str) -> IXmlNode: ...
    def CreateTextNode(self, text: str) -> IXmlNode: ...
    def CreateCDataSection(self, data: str) -> IXmlNode: ...
    def CreateWhitespace(self, text: str) -> IXmlNode: ...
    def CreateSignificantWhitespace(self, text: str) -> IXmlNode: ...
    def CreateXmlDeclaration(self, version: str, encoding: str, standalone: str) -> IXmlNode: ...
    def CreateXmlDocumentType(self, name: str, publicId: str, systemId: str, internalSubset: str) -> IXmlNode: ...
    def CreateProcessingInstruction(self, target: str, data: str) -> IXmlNode: ...
    @typing.overload
    def CreateElement(self, elementName: str) -> IXmlElement: ...
    @typing.overload
    def CreateElement(self, qualifiedName: str, namespaceUri: str) -> IXmlElement: ...
    @typing.overload
    def CreateAttribute(self, name: str, value: str) -> IXmlNode: ...
    @typing.overload
    def CreateAttribute(self, qualifiedName: str, namespaceUri: str, value: str) -> IXmlNode: ...
    def get_DocumentElement(self) -> IXmlElement: ...

class IXmlDeclaration:
    def __init__(self , *args: typing.Any) -> None: ...
    Version: str
    Encoding: str
    Standalone: str
    def get_Version(self) -> str: ...
    def get_Encoding(self) -> str: ...
    def set_Encoding(self, value: str) -> None: ...
    def get_Standalone(self) -> str: ...
    def set_Standalone(self, value: str) -> None: ...

class IXmlDocumentType:
    def __init__(self , *args: typing.Any) -> None: ...
    Name: str
    System: str
    Public: str
    InternalSubset: str
    def get_Name(self) -> str: ...
    def get_System(self) -> str: ...
    def get_Public(self) -> str: ...
    def get_InternalSubset(self) -> str: ...

class IXmlElement:
    def __init__(self , *args: typing.Any) -> None: ...
    IsEmpty: bool
    def SetAttributeNode(self, attribute: IXmlNode) -> None: ...
    def GetPrefixOfNamespace(self, namespaceUri: str) -> str: ...
    def get_IsEmpty(self) -> bool: ...

class IXmlNode:
    def __init__(self , *args: typing.Any) -> None: ...
    NodeType: System.Xml.XmlNodeType
    LocalName: str
    ChildNodes: list[IXmlNode]
    Attributes: list[IXmlNode]
    ParentNode: IXmlNode
    Value: str
    NamespaceUri: str
    WrappedNode: typing.Any
    def get_NodeType(self) -> System.Xml.XmlNodeType: ...
    def get_LocalName(self) -> str: ...
    def get_ChildNodes(self) -> list[IXmlNode]: ...
    def get_Attributes(self) -> list[IXmlNode]: ...
    @staticmethod
    def get_ParentNode() -> IXmlNode: ...
    def get_Value(self) -> str: ...
    def set_Value(self, value: str) -> None: ...
    def AppendChild(self, newChild: IXmlNode) -> IXmlNode: ...
    def get_NamespaceUri(self) -> str: ...
    def get_WrappedNode(self) -> typing.Any: ...

class XDeclarationWrapper(XObjectWrapper):
    def __init__(self, declaration: System.Xml.Linq.XDeclaration) -> None: ...
    NodeType: System.Xml.XmlNodeType
    Version: str
    Encoding: str
    Standalone: str
    def get_NodeType(self) -> System.Xml.XmlNodeType: ...
    def get_Version(self) -> str: ...
    def get_Encoding(self) -> str: ...
    def set_Encoding(self, value: str) -> None: ...
    def get_Standalone(self) -> str: ...
    def set_Standalone(self, value: str) -> None: ...

class XDocumentTypeWrapper(XObjectWrapper):
    def __init__(self, documentType: System.Xml.Linq.XDocumentType) -> None: ...
    Name: str
    System: str
    Public: str
    InternalSubset: str
    LocalName: str
    def get_Name(self) -> str: ...
    def get_System(self) -> str: ...
    def get_Public(self) -> str: ...
    def get_InternalSubset(self) -> str: ...
    def get_LocalName(self) -> str: ...

class XDocumentWrapper(XContainerWrapper):
    def __init__(self, document: System.Xml.Linq.XDocument) -> None: ...
    ChildNodes: list[IXmlNode]
    DocumentElement: IXmlElement
    def get_ChildNodes(self) -> list[IXmlNode]: ...
    def CreateComment(self, text: str) -> IXmlNode: ...
    def CreateTextNode(self, text: str) -> IXmlNode: ...
    def CreateCDataSection(self, data: str) -> IXmlNode: ...
    def CreateWhitespace(self, text: str) -> IXmlNode: ...
    def CreateSignificantWhitespace(self, text: str) -> IXmlNode: ...
    def CreateXmlDeclaration(self, version: str, encoding: str, standalone: str) -> IXmlNode: ...
    def CreateXmlDocumentType(self, name: str, publicId: str, systemId: str, internalSubset: str) -> IXmlNode: ...
    def CreateProcessingInstruction(self, target: str, data: str) -> IXmlNode: ...
    @typing.overload
    def CreateElement(self, elementName: str) -> IXmlElement: ...
    @typing.overload
    def CreateElement(self, qualifiedName: str, namespaceUri: str) -> IXmlElement: ...
    @typing.overload
    def CreateAttribute(self, name: str, value: str) -> IXmlNode: ...
    @typing.overload
    def CreateAttribute(self, qualifiedName: str, namespaceUri: str, value: str) -> IXmlNode: ...
    def get_DocumentElement(self) -> IXmlElement: ...
    def AppendChild(self, newChild: IXmlNode) -> IXmlNode: ...

class XTextWrapper(XObjectWrapper):
    def __init__(self, text: System.Xml.Linq.XText) -> None: ...
    Value: str
    ParentNode: IXmlNode
    def get_Value(self) -> str: ...
    def set_Value(self, value: str) -> None: ...
    def get_ParentNode(self) -> IXmlNode: ...

class XCommentWrapper(XObjectWrapper):
    def __init__(self, text: System.Xml.Linq.XComment) -> None: ...
    Value: str
    ParentNode: IXmlNode
    def get_Value(self) -> str: ...
    def set_Value(self, value: str) -> None: ...
    def get_ParentNode(self) -> IXmlNode: ...

class XProcessingInstructionWrapper(XObjectWrapper):
    def __init__(self, processingInstruction: System.Xml.Linq.XProcessingInstruction) -> None: ...
    LocalName: str
    Value: str
    def get_LocalName(self) -> str: ...
    def get_Value(self) -> str: ...
    def set_Value(self, value: str) -> None: ...

class XContainerWrapper(XObjectWrapper):
    def __init__(self, container: System.Xml.Linq.XContainer) -> None: ...
    ChildNodes: list[IXmlNode]
    ParentNode: IXmlNode
    def get_ChildNodes(self) -> list[IXmlNode]: ...
    def get_ParentNode(self) -> IXmlNode: ...
    def AppendChild(self, newChild: IXmlNode) -> IXmlNode: ...

class XObjectWrapper:
    def __init__(self, xmlObject: System.Xml.Linq.XObject) -> None: ...
    WrappedNode: typing.Any
    NodeType: System.Xml.XmlNodeType
    LocalName: str
    ChildNodes: list[IXmlNode]
    Attributes: list[IXmlNode]
    ParentNode: IXmlNode
    Value: str
    NamespaceUri: str
    def get_WrappedNode(self) -> typing.Any: ...
    def get_NodeType(self) -> System.Xml.XmlNodeType: ...
    def get_LocalName(self) -> str: ...
    def get_ChildNodes(self) -> list[IXmlNode]: ...
    def get_Attributes(self) -> list[IXmlNode]: ...
    def get_ParentNode(self) -> IXmlNode: ...
    def get_Value(self) -> str: ...
    def set_Value(self, value: str) -> None: ...
    def AppendChild(self, newChild: IXmlNode) -> IXmlNode: ...
    def get_NamespaceUri(self) -> str: ...

class XAttributeWrapper(XObjectWrapper):
    def __init__(self, attribute: System.Xml.Linq.XAttribute) -> None: ...
    Value: str
    LocalName: str
    NamespaceUri: str
    ParentNode: IXmlNode
    def get_Value(self) -> str: ...
    def set_Value(self, value: str) -> None: ...
    def get_LocalName(self) -> str: ...
    def get_NamespaceUri(self) -> str: ...
    def get_ParentNode(self) -> IXmlNode: ...

class XElementWrapper(XContainerWrapper):
    def __init__(self, element: System.Xml.Linq.XElement) -> None: ...
    Attributes: list[IXmlNode]
    Value: str
    LocalName: str
    NamespaceUri: str
    IsEmpty: bool
    def SetAttributeNode(self, attribute: IXmlNode) -> None: ...
    def get_Attributes(self) -> list[IXmlNode]: ...
    def AppendChild(self, newChild: IXmlNode) -> IXmlNode: ...
    def get_Value(self) -> str: ...
    def set_Value(self, value: str) -> None: ...
    def get_LocalName(self) -> str: ...
    def get_NamespaceUri(self) -> str: ...
    def GetPrefixOfNamespace(self, namespaceUri: str) -> str: ...
    def get_IsEmpty(self) -> bool: ...

class XmlNodeConverter(Newtonsoft.Json.JsonConverter):
    def __init__(self, ) -> None: ...
    DeserializeRootElementName: str
    WriteArrayAttribute: bool
    OmitRootObject: bool
    EncodeSpecialCharacters: bool
    def get_DeserializeRootElementName(self) -> str: ...
    def set_DeserializeRootElementName(self, value: str) -> None: ...
    def get_WriteArrayAttribute(self) -> bool: ...
    def set_WriteArrayAttribute(self, value: bool) -> None: ...
    def get_OmitRootObject(self) -> bool: ...
    def set_OmitRootObject(self, value: bool) -> None: ...
    def get_EncodeSpecialCharacters(self) -> bool: ...
    def set_EncodeSpecialCharacters(self, value: bool) -> None: ...
    def WriteJson(self, writer: Newtonsoft.Json.JsonWriter, value: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> None: ...
    def ReadJson(self, reader: Newtonsoft.Json.JsonReader, objectType: System.Type, existingValue: typing.Any, serializer: Newtonsoft.Json.JsonSerializer) -> typing.Any: ...
    def CanConvert(self, valueType: System.Type) -> bool: ...

class Union:
    def __init__(self, tagReader: Newtonsoft.Json.Utilities.FSharpFunction, cases: list[UnionCase]) -> None: ...
    TagReader: Newtonsoft.Json.Utilities.FSharpFunction
    Cases: list[UnionCase]

class UnionCase:
    def __init__(self, tag: int, name: str, fields: list[System.Reflection.PropertyInfo], fieldReader: Newtonsoft.Json.Utilities.FSharpFunction, constructor: Newtonsoft.Json.Utilities.FSharpFunction) -> None: ...
    Tag: int
    Name: str
    Fields: list[System.Reflection.PropertyInfo]
    FieldReader: Newtonsoft.Json.Utilities.FSharpFunction
    Constructor: Newtonsoft.Json.Utilities.FSharpFunction

class <>c__DisplayClass8_0:
    def __init__(self, ) -> None: ...
    tag: int

class <>c__DisplayClass9_0:
    def __init__(self, ) -> None: ...
    caseName: str
    <>9__0: dict[UnionCase, bool]

