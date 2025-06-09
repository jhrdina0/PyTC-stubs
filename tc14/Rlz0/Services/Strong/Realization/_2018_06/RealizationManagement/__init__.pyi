import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ModelElementInfo:
    """
    
            This structure contains a unique clientId and a Mdl0ModelElement realized
            from an Item assembly. The clientId is mandatory and used to identify configuration
            information for the input Mdl0ModelElement.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify the configuration
            information returned and partial errors associated with this input.
            """
    ModelElement: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """
            Reference to the Mdl0ModelElement. The configuration information of its source
            Item assembly will be queried and returned.
            """

class SourceItemConfigData:
    """
    
            This structure represents the configuration information used to configure the source
            item assembly of the Model Element (Mdl0ModelElement) during realization.
            
    """
    def __init__(self, ) -> None: ...
    ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            Reference to the ConfigurationContext object which contains configuration
            information used to configure the source item assembly. It is created as a transient
            object and needs to be deleted by the caller.
            """
    BomView: str
    """
            The BOM view (BOMView) type of the BOM Window (BOMWindow) during the
            Item realization.
            """

class SourceItemConfigResponse:
    """
    
            This structure represents the output response of this operation. It contains configuration
            information and BOMView type that were used to configure the BOMWindow
            of the source Item assembly. This structure also represents the SourceItemConfigData
            mapped with the clientId specified as input to this operator.
            
    """
    def __init__(self, ) -> None: ...
    ConfigMap: System.Collections.Hashtable
    """
            A map (string, SourceItemConfigData) of clientId to SourceItemConfigData.
            SourceItemConfigData contains configuration information used to configure
            the source Item during Item realization.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ConfigurationContext objects are returned in Create object list while
            error messages are returned in the Partial Error list.
            """

class RealizationManagement:
    """
    Interface RealizationManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetSourceItemConfigInfo(self, ElementInfos: list[ModelElementInfo]) -> SourceItemConfigResponse: ...

