import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetAlignedDesignElementsResponse:
    def __init__(self, ) -> None: ...
    PartUsageToAlignedDesignElements: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class AlignmentManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAlignedDesignElements(self, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, PartUsages: list[Teamcenter.Soa.Client.Model.Strong.Bom0AbstractPartUsage]) -> GetAlignedDesignElementsResponse: ...

