import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AlignedBOMData:
    """
    
            Represents intermediate output structure to the getAlignedBOMData service operation
            containing bomData for each input Cpd0DesignElement object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This can be used by the caller to indentify this data structure with the source input
            data.
            """
    DesignElement: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignElement
    """Cpd0DesignElement object specified in input."""
    BomData: list[Teamcenter.Soa.Client.Model.Strong.Bom0CompositePartUsageAlignment]
    """
            List of Bom0CompositePartUsageAlignment objects containing information of
            aligned Bom0AbstractPartUsage object, Bom0AbstractPart object and Bom0AlignmentMember
            relation.
            """

class DesignElementInfo:
    """
    
            Represents the intermediate input to the getAlignedBOMData
            service operation containing clientId for
            each Cpd0DesignElement object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with the input.
            """
    DesignElement: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignElement
    """Cpd0DesignElement object for which aligned data information needs to be fetched."""

class DesignElementInfoGroup:
    """
    
            Represents input argument to the getAlignedBOMData
            service operation.
            
    """
    def __init__(self, ) -> None: ...
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """The selected parameters like effectivity, variant conditions, revisionrule."""
    DesignElements: list[DesignElementInfo]
    """List of input Cpd0DesignElement objects with clientId."""

class GetAlignedBOMDataResponse:
    """
    
            Represents response of the getAlignedBOMData
            service operation.
            
    """
    def __init__(self, ) -> None: ...
    AlignedDataForDesignElements: list[AlignedBOMData]
    """Represents aligned BOM data mapped to the input Cpd0DesignElement objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
Bom0CompositePartUsageAlignment objects aligned to Cpd0DesignElement
            objects are added to the plain lists. Also any partial errors during the operation
            are added to the error stack.
            """

class AlignmentManagement:
    """
    Interface AlignmentManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAlignedBOMData(self, Inputs: list[DesignElementInfoGroup]) -> GetAlignedBOMDataResponse:
        """    
             This operation returns BOM data aligned to Cpd0DesignElement objects configured
             with input ConfigurationContext. This operation
             works in set based fashion where you can provide Cpd0DesignElement objects
             in multiple ConfigurationContexts. The operation
             would return BOM Data corresponding to the Cpd0DesignElement  objects it is
             aligned with.
             

Use Cases:

             A NX user can view the BOM data by selecting Cpd0DesignElement objects within
             his ConfigurationContext.
             

Teamcenter Component:

             bom0bommanagement - Component for the template - bom0bommanagement
             
        :param Inputs: 
                         Information used to get the alinged BOM data.
             
        :return: 
        """
        ...

