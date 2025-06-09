import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetAttributeComplexDataIn:
    """
    
            This operation gets the complex data for the given Attribute Definition or Measurable
            Attribute.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """clientId Identifier defined by client to track the related object."""
    ObjectToRetrieve: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The object from which complex data on its properties need to be retrieved."""
    AttrPropNames: list[str]
    """
            The Att0Attributetable property names on which the complex data need to be retrieved
            for the given object.
            """
    MeasurePropNames: list[str]
    """
            The Att0ValueTable property names of Measurements on which the complex data need
            to be retrieved for the given object.
            """

class GetAttributeComplexDataOutput:
    """
    
            GetAttributeComplexDataOutput structure represents all the information needed to
            retrieve complex data for properties on Attribute Definition or Measurable Attribute.
            
    """
    def __init__(self, ) -> None: ...
    ObjectToRetrieve: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The object from which complex data on its properties need to be retrieved."""
    AttrPropNamesToAttrComplexDataMap: System.Collections.Hashtable
    """
            A map of name of attribute property and its AttributeComplexData to be read from
            objectToRetrieve.
            """
    MeasurePropNamesToMeasurementComplexDataMap: System.Collections.Hashtable
    """A map of name of measure property and its AttributeComplexData to be read from objectToRetrieve."""

class GetAttributeComplexDataResp:
    """
    
            GetAttributeComplexDataInput structure represents all the information needed to retrieve
            complex data for properties on Attribute Definition or Measurable Attribute.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData with partial errors for GetAttributeComplexDataInput identified by
            its clientID.
            """
    AttributeComplexDataOutput: list[GetAttributeComplexDataOutput]
    """
            attributeComplexDataOutput represents all the information needed to retrieve complex
            data for properties on Attribute Definition or Measurable Attribute.
            """

class AttributeTargetManagement:
    """
    Interface AttributeTargetManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAttributeComplexData(self, Inputs: list[GetAttributeComplexDataIn]) -> GetAttributeComplexDataResp:
        """    
             This operation gets the complex data for the given Attribute Definition or Measurable
             Attribute.
             

Use Cases:

             The System Engineer opens Attribute Definition or Measurable Attribute in Active
             Workspace and reviews the complex data (if existing) for Goal or Min or Max properties.
             

Teamcenter Component:

             Attribute Target Management - This component consists of the Client and Enterprise
             Tier code and constructs that support Attribute and Target related functionality
             including such things as Teamcenter Active Workspace application plus SOA, ITK and
             Preferences.
             
        :param Inputs: 
                         Input information required for the getAttributeComplexData in the form of GetAttributeComplexDataIn.
             
        :return: * 185050 - The property does not exist on Att0MeasurableAttribute, please provide
             valid property name.
        """
        ...

