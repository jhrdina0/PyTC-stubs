import System
import System.Collections.Generic
import typing

class ObjectPropertyPolicy:
    """
    
The Object Property Policy is a list of Teamcenter types and classes, and
properties associated with those types.
The properties defined in a parent type are inherited by child types. The Object
Property Policy defines which properties
are returned from a service operation for a given object type. The business
logic of a service operation determines what
Business Objects are returned while the Object Property Policy determines which
properties will be returned on each
Business Object instance. This allows the client application to determine how
much or how little data is returned
based on how the client application will use those returned Business Objects.
The policy is applied uniformly to all
service operations. The client application manages what policy is to be used at
any given time during the session
    """
    @typing.overload
    def __init__(self, ) -> None: ...
    @typing.overload
    def __init__(self, objects: dict[str, PolicyType], modifiers: dict[str, str]) -> None: ...
    Types: dict[str, PolicyType]
    """
            Get all policy types associated with current ObjPropPolicy class.
            """
    Modifiers: dict[str, bool]
    TypeNames: list[str]
    """Get the list of type names."""
    ModifierNames: list[str]
    """get the list of modifiers."""
    @typing.overload
    def AddType(self, policyType: PolicyType) -> None: ...
    @typing.overload
    def AddType(self, name: str) -> None: ...
    @typing.overload
    def AddType(self, name: str, properties: list[str]) -> None: ...
    def get_Types(self) -> dict[str, PolicyType]: ...
    def get_Modifiers(self) -> dict[str, bool]: ...
    def get_TypeNames(self) -> list[str]: ...
    def GetType(self, name: str) -> PolicyType: ...
    def RemoveType(self, typeName: str) -> bool:
        """    
            Remove the properties from the given type.
            If the source PolicyType defines a type with no properties, the whole type is removed.

        :param typeName: Type name to be removed
        :return: True, if succeeded else false
        """
        ...
    def RemoveProperties(self, type: PolicyType) -> bool:
        """    
            Remove the properties from the given type.
            If the source PolicyType defines a type with no properties, the whole type is removed.
            
        :param type: PolicyType with desired properties to remove.
        :return: True, if succeeded else false
        """
        ...
    def SetModifier(self, name: str, value: bool) -> None:
        """    
             Set the value for a modifier
            
        :param name: The name of the desired modifier.
              Legal value are:
              <ul><li>WITH_PROPERTIES</li><li>EXCLUDE_UI_VALUE</li><li>INCLUDE_MODIFIABLE</li><li>AS_ATTRIBUTE</li><li>UI_VALUE_ONLY</li><li>EXCLUDE_PARENT_PROPERTIES</li></ul>

        :param value: true/false value to set the modifier to.
        :return: 
        """
        ...
    def GetBooleanModifier(self, name: str) -> bool:
        """    Get the value of specific modifier.
        :param name: Name of the modifier which value we need to get
        :return: Returns the boolean value of the modifier
        """
        ...
    def get_ModifierNames(self) -> list[str]: ...
    def Equals(self, obj: typing.Any) -> bool:
        """    
            Compare the elements.
            
        :param obj: Instance of Object to be compared
        :return: True if all elements are equal else false
        """
        ...
    def Save(self, filePath: str) -> None:
        """    This function loads the ObjectPropertyPolicy from the xml file
            The format of the xml file is defined according to Policy schema.For More information
            Refer Teamcenter Services Guide.
            
        :param filePath: Full path of file where the policy wants to get saved
        :return: 
        """
        ...
    def Load(self, filePath: str) -> None:
        """    
            Loads the ObjectPropertyPolicy from the XML file specified.
            The format of the XML file is as per the policy schema. Please refer Teamcenter Services
            Guide for more information.
            
            Property modifiers WITH_PROPERTIES) that exist on the ObjectPropetyPolicy will be applied
            to the data read from the file. If the source properties in the file already exists in the ObjectPropertyPolicy, all modifiers
            on those properties will be lost and only the modifiers from the source file will be applied.

        :param filePath: Full path of file from where the policy needs to get loaded
        :return: 
        """
        ...

class PolicyType:
    """
    
The PolicyType class manages a list of properties for a single Type or Class.
    """
    @typing.overload
    def __init__(self, ) -> None: ...
    @typing.overload
    def __init__(self, name: str) -> None: ...
    @typing.overload
    def __init__(self, name: str, properties: list[str]) -> None: ...
    @typing.overload
    def __init__(self, name: str, properties: list[str], modifiers: list[str]) -> None: ...
    ModifierNames: list[str]
    """get the list of modifiers."""
    Name: str
    """
            Get the name this Type or Class.
            """
    PropertyNames: list[str]
    """Get the list of type names."""
    Properties: dict[str, PolicyProperty]
    """
            Get all policy properties associated with current type.
            """
    Modifiers: dict[str, bool]
    def HasProperty(self, propertyName: str) -> bool:
        """    
             Returns true if the named property is in this type.
            
        :param propertyName: The name of the desired property.
        :return: true if the property is in this type.
        """
        ...
    def SetModifier(self, name: str, value: bool) -> None:
        """    
             Set the value for a modifier
            
        :param name: The name of the desired modifier.
              Legal value are:
              <ul><li>WITH_PROPERTIES</li><li>EXCLUDE_UI_VALUE</li><li>INCLUDE_MODIFIABLE</li><li>AS_ATTRIBUTE</li><li>UI_VALUE_ONLY</li><li>EXCLUDE_PARENT_PROPERTIES</li></ul>

        :param value: true/false value to set the modifier to.
        :return: 
        """
        ...
    def GetBooleanModifier(self, name: str) -> bool:
        """    Get the value of specific modifier.
        :param name: Name of the modifier which value we need to get
        :return: Returns the boolean value of the modifier
        """
        ...
    def get_ModifierNames(self) -> list[str]: ...
    def set_Name(self, value: str) -> None: ...
    def get_Name(self) -> str: ...
    def get_PropertyNames(self) -> list[str]: ...
    def get_Properties(self) -> dict[str, PolicyProperty]: ...
    def get_Modifiers(self) -> dict[str, bool]: ...
    def GetProperty(self, name: str) -> PolicyProperty:
        """    
            Returns the a named PolicyProperty.
            
        :param name: The name of the desired PolicyProperty
        :return: The pointer to the PolicyProperty for the given name, NULL if the named type does not exist.
        """
        ...
    def ToString(self) -> str:
        """    
            Return a string that represents this Object Property list.
            The string will have the format:
            TypeOrClassName { propertyName [,propertyName]...}
            
        :return: 
        """
        ...
    @typing.overload
    def AddProperty(self, propName: str) -> None: ...
    @typing.overload
    def AddProperty(self, prop: PolicyProperty) -> None: ...
    def EraseProperty(self, propName: str) -> None:
        """    
             Erase a property from the list of properties
            
        :param propName: The name of the property to erase
        :return: 
        """
        ...
    def AddProperties(self, props: str) -> None:
        """    
            Adds to the list of properties for this Type or Class.
            Property modifiers (i.e. WITH_PROPERTIES) that exist on the PolicyType will 
            be applied to the named properties. If the source property already exists in the PolicyType, all modifiers on
            that property will be lost and only the modifiers from the PolicyType will be applied.
            
        :param props: List of property names, i.e. '{volume,mailbox,home_folder}'.
        :return: 
        """
        ...
    def SetProperties(self, props: str) -> None:
        """    
            Sets the list of properties for this Type or Class.
            Any properties currently maintained by this instance of ObjectProperties are
            thrown away.
            
        :param props: List of property names, i.e. '{volume,mailbox,home_folder}'.
        :return: 
        """
        ...
    def Equals(self, obj: typing.Any) -> bool:
        """    
            Compare the elements in object.
            
        :param obj: Instace of Object to compare
        :return: True,if all elements are equal else false.
        """
        ...

class PolicyProperty:
    """
    
This is used to set ObjectPropertyPolicy.
    """
    @typing.overload
    def __init__(self, ) -> None: ...
    @typing.overload
    def __init__(self, name: str) -> None: ...
    @typing.overload
    def __init__(self, name: str, modifiers: list[str]) -> None: ...
    WITH_PROPERTIES: str
    """
             Key value to be used in the get/set Modifier methods.
             By default the Object Property Policy is applied only to the objects explicitly 
             returned by the service implemenation. So if the service returns a 'User' object and the 'home_folder' property is
             part of the policy, the referenced 'home_folder' obect will be added to the return data, but without any associated properties. 
             By setting this modifier to true, on the the 'home_folder' property,  properties for home folder will also be returned.
            """
    EXCLUDE_UI_VALUE: str
    """
             Key value to be used in the get/setModifier methods.
             By default the Object Property Policy returns both the database and UI value for each property. By setting this modifier to 
             true, only the database values of a property are returned, the UI value is excluded from the return data.
            """
    EXCLUDE_MODIFIABLE: str
    """
             Obsolete
             Use POLICY_MODIFIER_INCLUDE_MODIFIABLE to include the 'Is Modifiable' when the client actually needs 
             this data.
            """
    INCLUDE_MODIFIABLE: str
    """
             Key value to be used in the get/setModifier methods.
             By default the Object Property Policy does not returns the 'Is Modifiable' flag with
             each property value. The 'modifiable' flag is the instance based flag vs. the Meta Model flag
             defined on the PropertyDesciption. By setting this modifier to 
             true, the 'Is Modifiable' flag will be returned.
            """
    AS_ATTRIBUTE: str
    """
             Key value to be usedin the get/setModifier methods.
             This modifier is effective only for attribute properties stored directly in the database (those of type ImanPropAttribute).
             By default the Object Property Policy ensures that all standard and customized runtime modifications are performed
             on the property value before it is returned.  By setting this modifier to true, the database attribute value
             is returned without checking for runtime modifications.  This can be used as a perrformance enhancement, but should be used only
             when the application and customizations do not use any runtime modifications for the property.
             """
    UI_VALUE_ONLY: str
    """
            Key value to be used in the get/set Modifier methods. 
            By default the full property information is returned for the named property, this includes the database value,
            the display or UI value, and flags such as ‘isModifiable’. With this flag set to ‘true’ only the UI value will be returned.
            This flag takes precedence over any other flags set in the policy for the named property.
            """
    EXCLUDE_PARENT_PROPERTIES: str
    """
            Key value to be used in the get/set Modifier methods. 
            By default the properties defined on the parent type are included in the current type. 
            With this property set to 'true' properties defined on the parent are excluded.
            """
    ModifierNames: list[str]
    """get the list of modifiers."""
    Modifiers: dict[str, bool]
    Name: str
    """
            Get name of current Property
            """
    def SetModifier(self, name: str, value: bool) -> None:
        """    
             Set the value for a modifier
            
        :param name: The name of the desired modifier.
              Legal value are:
              <ul><li>WITH_PROPERTIES</li><li>EXCLUDE_UI_VALUE</li><li>INCLUDE_MODIFIABLE</li><li>AS_ATTRIBUTE</li><li>UI_VALUE_ONLY</li><li>EXCLUDE_PARENT_PROPERTIES</li></ul>

        :param value: true/false value to set the modifier to.
        :return: 
        """
        ...
    def get_ModifierNames(self) -> list[str]: ...
    def get_Modifiers(self) -> dict[str, bool]: ...
    def GetBooleanModifier(self, name: str) -> bool:
        """    Get the value of specific modifier.
        :param name: Name of the modifier which value we need to get
        :return: Returns the boolean value of the modifier
        """
        ...
    def set_Name(self, value: str) -> None: ...
    def get_Name(self) -> str: ...
    def Equals(self, obj: typing.Any) -> bool:
        """    
            Compare the elements of object.
            
        :param obj: Instance of the object to compare.
        :return: True,if elements are equal else false.
        """
        ...

class Version:
    @typing.overload
    def __init__(self, major: int, minor: int, maintenance: int) -> None: ...
    @typing.overload
    def __init__(self, version: str) -> None: ...
    major: int
    """ 
            Major release, 2007, 8000, etc.
            """
    minor: int
    """ 
            Minor release number
            """
    maintenance: int
    """ 
            Maintenance Patch number
            """
    phase: int
    """ 
            Phase number, as of 11000.2.4
            """
    TEAMCENTER_VERSION_LABLEL: str
    TEAMCENTER_VERSION: str
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    @staticmethod
    def op_Equality(left: Version, right: Version) -> bool: ...
    @staticmethod
    def op_Inequality(left: Version, right: Version) -> bool: ...
    @staticmethod
    def op_GreaterThan(left: Version, right: Version) -> bool: ...
    @staticmethod
    def op_GreaterThanOrEqual(left: Version, right: Version) -> bool: ...
    @staticmethod
    def op_LessThan(left: Version, right: Version) -> bool: ...
    @staticmethod
    def op_LessThanOrEqual(left: Version, right: Version) -> bool: ...

