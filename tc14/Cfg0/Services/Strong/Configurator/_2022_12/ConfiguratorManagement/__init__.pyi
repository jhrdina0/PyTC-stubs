import Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class VariabilityTreeData:
    """
    
            Tree structure representing variant data. This holds list of structure VariabilityNode.
            Each element represents either a Cfg0AbsFamilyGroup, Cfg0AbsFamily,
            Cfg0AbsValue or its subtypes in the response and list of all its children.
            For Cfg0AbsValue, no children data is populated. This structure will be populated
            based on mode information received in the requestInfo.
            
    """
    def __init__(self, ) -> None: ...
    VariabilityNodes: list[VariabilityNode]
    """A list of VariabilityNode struct representing variant data."""

class GetVariantInformationResponse:
    """
    
            The structure represents the response for getVariantInformation operation consisting
            of variant and configuration information for input VariantRule objects.
            
            The Configurator perspective information for the input objects is returned as part
            of props in viewModelObjectMap when configuration profile information is requested;
            this information contains the product information including the product name, product
            namespace, revision rule and rule date.
            
    """
    def __init__(self, ) -> None: ...
    VariantAndConfigurationInfo: list[VariantAndConfigurationInformation]
    """
            A list of variant and configuration information retrieved for input VariantRule
            objects.
            """
    ViewModelObjectMap: System.Collections.Hashtable
    """
            A map (string, ViewModelObject) of object UID to its corresponding ViewModelObject.
            This map contains the requested objects and its properties. If expression information
            is requested, it additionally contains variant data referenced in variantAndConfigurationInfo
            scope.
            """
    VariabilityTreeData: VariabilityTreeData
    """
            Tree structure representing variant data referred in variantAndConfigurationInfo
            scope. This field is populated only when expression information is requested for
            input objects.
            """
    ResponseInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]
    """A list of response names and value pairs. This is reserved for future use."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The service data for errors and returned objects. The plainObjects in serviceData
            contains the input targetObjects for the benefit of comparing various properties
            of targetObjects.
            """

class VariabilityNode:
    """
    
            Structure representing variability node where node object can either represent a
            Cfg0AbsFamilyGroup, Cfg0AbsFamily, Cfg0AbsValue or its subtypes
            and contains list of its children.
            
    """
    def __init__(self, ) -> None: ...
    NodeUid: str
    """
            The UID of Cfg0AbsFamilyGroup, Cfg0AbsFamily, Cfg0AbsValue or
            its subtypes.
            """
    ChildrenUids: list[str]
    Props: System.Collections.Hashtable

class VariantAndConfigurationInformation:
    """
    
            The structure for holding variant and configuration information for a VariantRule
            object.
            
    """
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.Strong.VariantRule
    """VariantRule object or its subtypes."""
    SolveProfile: str
    """
            The configuration solve profile as JSON string that consists of attributes governing
            the behavior of configurator constraint evaluation. This string adheres to the JSON
            schema for solve profile defined in SolveProfile_Schema.json; please refer
            to schema and sample solve profiles defined at %TC_DATA%/json/variabilityadaptor/schema
            for details. Solve profile information is populated when configuration profile information
            is requested.
            """
    VariantExpression: str

class ViewModelObject:
    """
    
            The generic object that is used to represent a single business object and its properties.
            
            It can represent either a Cfg0AbsFamilyGroup, Cfg0AbsFamily, Cfg0AbsValue,
            VariantRule or its subtypes and its properties.
            
    """
    def __init__(self, ) -> None: ...
    SourceUid: str
    """The unique ID of the business object."""
    DisplayName: str
    """The display name of the object."""
    SourceType: str
    """The type of the business object."""
    Props: System.Collections.Hashtable
    """A map (string, list of strings) of properties and values associated with the object."""

class ConfiguratorManagement:
    """
    Interface ConfiguratorManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetVariantInformation(self, TargetObjects: list[Teamcenter.Soa.Client.Model.Strong.VariantRule], RequestInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]) -> GetVariantInformationResponse: ...

