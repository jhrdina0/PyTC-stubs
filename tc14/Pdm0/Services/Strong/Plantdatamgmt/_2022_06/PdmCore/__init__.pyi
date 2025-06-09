import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FindPlantContentsUsingExtIdsResp2:
    """
    
            The structure consists of a map of external IDs to its corresponding configured elements
            Pdm0Design or Pdm0LogicalElmnt.
            

            Any errors are returned in the serviceData.
            
    """
    def __init__(self, ) -> None: ...
    ExternalIdToWorkspaceObjectMap: System.Collections.Hashtable
    """
            A map (String, WorkspaceObject) of external identifier string to its corresponding
            Pdm0Design or Pdm0LogicalElmnt object.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any partial errors encountered during this operation are returned in the ServiceData
            list.
            """

class PdmCore:
    """
    Interface PdmCore
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindPlantContentsUsingExtIds2(self, CapitalAssetRoot: Teamcenter.Soa.Client.Model.Strong.Pdm0CARoot, ExternalIds: list[str], ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> FindPlantContentsUsingExtIdsResp2: ...

