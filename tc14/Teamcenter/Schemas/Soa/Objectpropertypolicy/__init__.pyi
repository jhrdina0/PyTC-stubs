import System.Collections

class ObjectPropertyPolicy:
    def __init__(self, ) -> None: ...
    WithProperties: str
    IsWithPropertiesSet: bool
    ExcludeParentProperties: str
    IsExcludeParentPropertiesSet: bool
    AsAttribute: str
    IsAsAttributeSet: bool
    UIValueOnly: str
    IsUIValueOnlySet: bool
    ExcludeUiValues: str
    IsExcludeUiValuesSet: bool
    ExcludeIsModifiable: str
    IsExcludeIsModifiableSet: bool
    IncludeIsModifiable: str
    IsIncludeIsModifiableSet: bool
    ObjectType: list[ObjectType]
    def get_WithProperties(self) -> str: ...
    def set_WithProperties(self, value: str) -> None: ...
    def getWithProperties(self) -> str: ...
    def setWithProperties(self, val: str) -> None: ...
    def get_IsWithPropertiesSet(self) -> bool: ...
    def get_ExcludeParentProperties(self) -> str: ...
    def set_ExcludeParentProperties(self, value: str) -> None: ...
    def getExcludeParentProperties(self) -> str: ...
    def setExcludeParentProperties(self, val: str) -> None: ...
    def get_IsExcludeParentPropertiesSet(self) -> bool: ...
    def get_AsAttribute(self) -> str: ...
    def set_AsAttribute(self, value: str) -> None: ...
    def getAsAttribute(self) -> str: ...
    def setAsAttribute(self, val: str) -> None: ...
    def get_IsAsAttributeSet(self) -> bool: ...
    def get_UIValueOnly(self) -> str: ...
    def set_UIValueOnly(self, value: str) -> None: ...
    def getUIValueOnly(self) -> str: ...
    def setUIValueOnly(self, val: str) -> None: ...
    def get_IsUIValueOnlySet(self) -> bool: ...
    def get_ExcludeUiValues(self) -> str: ...
    def set_ExcludeUiValues(self, value: str) -> None: ...
    def getExcludeUiValues(self) -> str: ...
    def setExcludeUiValues(self, val: str) -> None: ...
    def get_IsExcludeUiValuesSet(self) -> bool: ...
    def get_ExcludeIsModifiable(self) -> str: ...
    def set_ExcludeIsModifiable(self, value: str) -> None: ...
    def getExcludeIsModifiable(self) -> str: ...
    def setExcludeIsModifiable(self, val: str) -> None: ...
    def get_IsExcludeIsModifiableSet(self) -> bool: ...
    def get_IncludeIsModifiable(self) -> str: ...
    def set_IncludeIsModifiable(self, value: str) -> None: ...
    def getIncludeIsModifiable(self) -> str: ...
    def setIncludeIsModifiable(self, val: str) -> None: ...
    def get_IsIncludeIsModifiableSet(self) -> bool: ...
    def get_ObjectType(self) -> list[ObjectType]: ...
    def set_ObjectType(self, value: list[ObjectType]) -> None: ...
    def getObjectType(self) -> System.Collections.ArrayList: ...
    def setObjectType(self, val: System.Collections.ArrayList) -> None: ...

class ObjectType:
    def __init__(self, ) -> None: ...
    WithProperties: str
    IsWithPropertiesSet: bool
    ExcludeParentProperties: str
    IsExcludeParentPropertiesSet: bool
    Name: str
    AsAttribute: str
    IsAsAttributeSet: bool
    UIValueOnly: str
    IsUIValueOnlySet: bool
    ExcludeUiValues: str
    IsExcludeUiValuesSet: bool
    ExcludeIsModifiable: str
    IsExcludeIsModifiableSet: bool
    IncludeIsModifiable: str
    IsIncludeIsModifiableSet: bool
    Property: list[Property]
    def get_WithProperties(self) -> str: ...
    def set_WithProperties(self, value: str) -> None: ...
    def getWithProperties(self) -> str: ...
    def setWithProperties(self, val: str) -> None: ...
    def get_IsWithPropertiesSet(self) -> bool: ...
    def get_ExcludeParentProperties(self) -> str: ...
    def set_ExcludeParentProperties(self, value: str) -> None: ...
    def getExcludeParentProperties(self) -> str: ...
    def setExcludeParentProperties(self, val: str) -> None: ...
    def get_IsExcludeParentPropertiesSet(self) -> bool: ...
    def get_Name(self) -> str: ...
    def set_Name(self, value: str) -> None: ...
    def getName(self) -> str: ...
    def setName(self, val: str) -> None: ...
    def get_AsAttribute(self) -> str: ...
    def set_AsAttribute(self, value: str) -> None: ...
    def getAsAttribute(self) -> str: ...
    def setAsAttribute(self, val: str) -> None: ...
    def get_IsAsAttributeSet(self) -> bool: ...
    def get_UIValueOnly(self) -> str: ...
    def set_UIValueOnly(self, value: str) -> None: ...
    def getUIValueOnly(self) -> str: ...
    def setUIValueOnly(self, val: str) -> None: ...
    def get_IsUIValueOnlySet(self) -> bool: ...
    def get_ExcludeUiValues(self) -> str: ...
    def set_ExcludeUiValues(self, value: str) -> None: ...
    def getExcludeUiValues(self) -> str: ...
    def setExcludeUiValues(self, val: str) -> None: ...
    def get_IsExcludeUiValuesSet(self) -> bool: ...
    def get_ExcludeIsModifiable(self) -> str: ...
    def set_ExcludeIsModifiable(self, value: str) -> None: ...
    def getExcludeIsModifiable(self) -> str: ...
    def setExcludeIsModifiable(self, val: str) -> None: ...
    def get_IsExcludeIsModifiableSet(self) -> bool: ...
    def get_IncludeIsModifiable(self) -> str: ...
    def set_IncludeIsModifiable(self, value: str) -> None: ...
    def getIncludeIsModifiable(self) -> str: ...
    def setIncludeIsModifiable(self, val: str) -> None: ...
    def get_IsIncludeIsModifiableSet(self) -> bool: ...
    def get_Property(self) -> list[Property]: ...
    def set_Property(self, value: list[Property]) -> None: ...
    def getProperty(self) -> System.Collections.ArrayList: ...
    def setProperty(self, val: System.Collections.ArrayList) -> None: ...

class Property:
    def __init__(self, ) -> None: ...
    WithProperties: str
    IsWithPropertiesSet: bool
    ExcludeParentProperties: str
    IsExcludeParentPropertiesSet: bool
    Name: str
    AsAttribute: str
    IsAsAttributeSet: bool
    UIValueOnly: str
    IsUIValueOnlySet: bool
    ExcludeUiValues: str
    IsExcludeUiValuesSet: bool
    ExcludeIsModifiable: str
    IsExcludeIsModifiableSet: bool
    IncludeIsModifiable: str
    IsIncludeIsModifiableSet: bool
    def get_WithProperties(self) -> str: ...
    def set_WithProperties(self, value: str) -> None: ...
    def getWithProperties(self) -> str: ...
    def setWithProperties(self, val: str) -> None: ...
    def get_IsWithPropertiesSet(self) -> bool: ...
    def get_ExcludeParentProperties(self) -> str: ...
    def set_ExcludeParentProperties(self, value: str) -> None: ...
    def getExcludeParentProperties(self) -> str: ...
    def setExcludeParentProperties(self, val: str) -> None: ...
    def get_IsExcludeParentPropertiesSet(self) -> bool: ...
    def get_Name(self) -> str: ...
    def set_Name(self, value: str) -> None: ...
    def getName(self) -> str: ...
    def setName(self, val: str) -> None: ...
    def get_AsAttribute(self) -> str: ...
    def set_AsAttribute(self, value: str) -> None: ...
    def getAsAttribute(self) -> str: ...
    def setAsAttribute(self, val: str) -> None: ...
    def get_IsAsAttributeSet(self) -> bool: ...
    def get_UIValueOnly(self) -> str: ...
    def set_UIValueOnly(self, value: str) -> None: ...
    def getUIValueOnly(self) -> str: ...
    def setUIValueOnly(self, val: str) -> None: ...
    def get_IsUIValueOnlySet(self) -> bool: ...
    def get_ExcludeUiValues(self) -> str: ...
    def set_ExcludeUiValues(self, value: str) -> None: ...
    def getExcludeUiValues(self) -> str: ...
    def setExcludeUiValues(self, val: str) -> None: ...
    def get_IsExcludeUiValuesSet(self) -> bool: ...
    def get_ExcludeIsModifiable(self) -> str: ...
    def set_ExcludeIsModifiable(self, value: str) -> None: ...
    def getExcludeIsModifiable(self) -> str: ...
    def setExcludeIsModifiable(self, val: str) -> None: ...
    def get_IsExcludeIsModifiableSet(self) -> bool: ...
    def get_IncludeIsModifiable(self) -> str: ...
    def set_IncludeIsModifiable(self, value: str) -> None: ...
    def getIncludeIsModifiable(self) -> str: ...
    def setIncludeIsModifiable(self, val: str) -> None: ...
    def get_IsIncludeIsModifiableSet(self) -> bool: ...

