import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class CollectPropertiesInputInfo:
    """
    
            This is a input structure containing rootNode, set of Traversal Rules and a set of
            Traversal Visitor info.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client ID"""
    RootNode: Teamcenter.Soa.Client.Model.ModelObject
    """The root node to traverse from."""
    TraversalRuleList: list[TraversalRuleInfo]
    """The traversal rules to be used while traversing BOP structure."""
    PropVisitorList: list[PropertyCollectorVisitorInfo]
    """The collection of type of MfgNodes and properties to collect for the type."""

class CollectPropertiesOutput:
    """
    Structure containing client Id and PropertyCollectoroutput
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client ID"""
    Output: list[PropertyCollectorOutput]
    """vector of PropertyCollectorOutput"""

class CollectPropertiesResponse:
    """
    Response structure containing service data
    """
    def __init__(self, ) -> None: ...
    OutputList: list[CollectPropertiesOutput]
    """The collection of MfgNode, property names and theit values."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """service data containing partial error data"""

class MFGNodePropertyValues:
    """
    The structure that holds MFGNode along with property names and their values.
    """
    def __init__(self, ) -> None: ...
    Node: Teamcenter.Soa.Client.Model.ModelObject
    """The MFGNode in BOP structure."""
    Props: System.Collections.Hashtable
    """Map of Property Name Value Pair"""

class PropertyCollectorOutput:
    """
    
            Output structure containing MfgNode, set of Properties that are evaluated for the
            node and set of property values corresponding to the property names.
            
    """
    def __init__(self, ) -> None: ...
    ContextType: str
    """Context Type of MfgNode"""
    NodeValueList: list[MFGNodePropertyValues]
    """The vector of MFGNodePropertyValues."""

class PropertyCollectorVisitorInfo:
    """
    
            This structure contains list of properties to collect for the corresponding Traversal
            Rule Key
            
    """
    def __init__(self, ) -> None: ...
    TraversalVisitorsKeys: list[TraversalKeyInfo]
    """The collection of type of MfgNode and its corresponding MfgContext type."""
    PropToCollectList: list[str]
    """The list of properties to be evaluated for the type of MfgNode specified in traversalRuleKey."""

class TraversalKeyInfo:
    """
    This is a structure of MFGNode types and MFGContext
    """
    def __init__(self, ) -> None: ...
    Types: list[str]
    """set of MFGNode types"""
    Context: str
    """context of MFGNodes"""

class TraversalRuleInfo:
    """
    This structure contains TraversalRuleKeys and their corresponding relations properties.
    """
    def __init__(self, ) -> None: ...
    TraversalRuleKeys: list[TraversalKeyInfo]
    """The collection of type of MfgNode and its corresponding MfgContext type."""
    Targets: list[str]
    """The list of properties to be used to traverse for current MfgNode to its sub nodes."""

class MFGPropertyCollector:
    """
    Interface MFGPropertyCollector
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CollectProperties(self, Input: list[CollectPropertiesInputInfo]) -> CollectPropertiesResponse:
        """    
             This function will call a Mfg function that takes the MfgNode, traversal rules and
             property names to collect and return a list of property values of input properties
             for every MfgNode in the BOP structure based on traversal rules.
             
        :param Input: 
                         MfgNode, traversal rules and property names to collect
             
        :return: a list of property values of input properties for every MfgNode in the BOP structure
        """
        ...

