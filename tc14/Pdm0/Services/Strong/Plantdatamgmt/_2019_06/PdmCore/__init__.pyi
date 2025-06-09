import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FindPlantContentsUsingExtIdsResponse:
    """
    
            The response contains a map of external ids to its corresponding configured conditional
            model elements (Mdl0ConditionalElement).
            

            Any errors are returned in the serviceData.
            
    """
    def __init__(self, ) -> None: ...
    ExternalIdToWorkspaceObjectMap: System.Collections.Hashtable
    """
            A map (string, Mdl0ConditionalElement) of external identifier string and its
            corresponding conditional model element objects (Mdl0ConditionalElement) that are
            configured by configuration context if specified. By default only working conditional
            model elements that do not have any status will be retreived and returned.
            
            If there is no workspace object mapped to an external object using specified External
            Identifier then no object will be returned.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains a list of any errors which occurred during the operation."""

class PdmCore:
    """
    Interface PdmCore
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindPlantContentsUsingExtIds(self, Plant: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel, ExternalIds: list[str], ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> FindPlantContentsUsingExtIdsResponse: ...

