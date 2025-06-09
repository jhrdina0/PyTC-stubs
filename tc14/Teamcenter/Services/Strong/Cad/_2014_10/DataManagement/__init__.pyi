import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class PropDescInfo:
    """
    
            The PropDescInfo struct contains information
            about the Teamcenter property descriptor associated with the attribute mapping definition.
            
    """
    def __init__(self, ) -> None: ...
    BoTypeName: str
    """
            The business object type name with which the property descriptor is associated.
            This can be used to look up the client-side PropertyDescription
            object in the SOA ClientMetaModel data.
            """
    PropDescName: str
    """
            The name of the property descriptor.  This can be used to look up the client-side
            PropertyDescription object in the ClientMetaModel data.
            """

class AttrMappingInfo:
    """
    Attribute mapping information.
    """
    def __init__(self, ) -> None: ...
    CadAttrMappingDefinition: Teamcenter.Soa.Client.Model.Strong.CadAttrMappingDefinition
    """The CadAttrMappingDefinition object reference representing the mapping definition."""
    PropDescInfo: PropDescInfo
    """
            The property descriptor information for the attribute mapping.  This information
            can be used to look up the client-side business object Type
            and PropertyDescription object in the ClientMetaModel data.
            """
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure. If clientId is not provided then it can be difficult to align the
            input with any returned errors.
            """

class GetAttrMappingsFilter:
    """
    
            Input filter for the data returned from the getAttrMappings
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ItemTypeName: str
    """The item type name used to find an attribute mapping."""
    DatasetTypeName: str
    """The dataset type name used to find an attribute mapping."""
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure. If clientId is not provided then it can be difficult to align the
            input with any returned errors.
            """

class GetAttrMappingsResponse:
    """
    
            The response returned from the getAttrMappings
            operation.
            
    """
    def __init__(self, ) -> None: ...
    AttrMappingInfos: list[AttrMappingInfo]
    """A list of attribute mapping information."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData. This operation will populate
            the ServiceData plain objects with CadAttrMappingDefinition objects and property
            descriptor LOV objects.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAttrMappings(self, Filter: list[GetAttrMappingsFilter]) -> GetAttrMappingsResponse:
        """    
             This operation retrieves all CAD attribute mapping definitions or only the definitions
             that match the dataset and item type combinations included in the input filter.
             CadAttributeMappingDefinition objects are returned with the associated business
             object name and property descriptor name.  The business object name and property
             descriptor name can be used to get the PropertyDescription
             object from the client-side Meta Model, ClientMetaModel.
             The PropertyDescription object can then
             be used to access any needed property descriptor information, such as attached ListOfValues (LOV) objects.
             

             Since this operation returns existing Teamcenter attribute mappings, please reference
             the Teamcenter help section on creating attribute mappings.
             


Use Cases:

             User needs to have attributes set on an object in Teamcenter.
             

             For this operation, the client application uses the list of returned attribute mapping
             definitions to present the correct CAD attributes to the user that correspond to
             the correct Teamcenter attributes including property descriptor information about
             the Teamcenter attributes.
             


Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Filter: 
                         The input filter for narrowing the attribute mapping definitions returned in the
                         response. All of the attribute mappings defined in Teamcenter are returned when no
                         filter is specified.
             
        :return: 
        """
        ...

