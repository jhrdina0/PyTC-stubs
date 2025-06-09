import Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FindConnectionsOnPortOutput2:
    """
    This structure contains all the connections associated with the input port.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the FindConnectionsOnPortInputInfo.clientId. This can be
            used by the caller to identify this data structure with the source input data.
            """
    Connections: list[Teamcenter.Soa.Client.Model.Strong.Mdc0ConnectionElement]
    """The list of Mdc0ConnectionElement that contains the port."""

class FindConnectionsOnPortResponse2:
    """
    This structure contains the search results along with the serviceData.
    """
    def __init__(self, ) -> None: ...
    Results: list[FindConnectionsOnPortOutput2]
    """The list of the search results."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard return; includes any error information. An error will be reported if the
            search terms are improperly defined.
            """

class GetParentElementGroupInfo:
    """
    
            Structure represents the parameters required to query the Mdc0OrderedElementGroup
            object and Mdc0ConditionalElementGroup object that contain the given Mdl0ConditionalElement
            object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    ConditionalElement: Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement
    """The Mdl0ConditionalElement or Mdc0ConnectionElement object."""
    Context: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            The Configuration Context (ConfigurationContext) object. This is optional
            and is applied to the objects. If NULL, it will not be applied to the objects.
            """

class GetParentElementGroupOutput:
    """
    Structure represents the output parameters of queryParentElementGroup2 operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input GetParentElementGroupInfo element. This value is unchanged
            from the input, and can be used to identify this response element.
            """
    OrderedElemGroup: list[Teamcenter.Soa.Client.Model.Strong.Mdc0OrderedElementGroup]
    """The parent Mdc0OrderedElementGroup object of a given Mdl0ConditionalElement."""
    ConditionalElemGroup: list[Teamcenter.Soa.Client.Model.Strong.Mdc0ConditionalElementGroup]
    """The parent Mdc0ConditionalElementGroup object of a given Mdl0ConditionalElement."""

class GetParentElementGroupResponse:
    """
    
            Structure contains the queried Mdc0OrderedElementGroup and Mdc0ConditionalElementGroup
            objects.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetParentElementGroupOutput]
    """A list of GetParentElementGroupOutput structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Added, updated, object data plus any error information."""

class MDConnectivity:
    """
    Interface MDConnectivity
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindConnectionsOnPort2(self, Input: list[Mdc0.Services.Strong.Mdconnectivity._2014_10.MDConnectivity.FindConnectionsOnPortInputInfo]) -> FindConnectionsOnPortResponse2:
        """    
             This operation finds all Mdc0ConnectionElement objects for the given Mdc0PortArtifact
             objects associated with Mdl0ConditionalElement objects.
             

Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         The search criteria.
             
        :return: 
        """
        ...
    def QueryParentElementGroup2(self, Input: list[GetParentElementGroupInfo]) -> GetParentElementGroupResponse:
        """    
             This operation finds the parent Mdc0ConditionalElementGroup object and Mdc0OrderedElementGroup
             object that are associated with given Mdl0ConditionalElement object.
             

Use Cases:

             Use Case 1: The client wants to find the conditional groups and ordered groups that
             a conditional element is a member of.
             

Teamcenter Component:

             Multi-Disciplinary Connectivity - Multi-Disciplinary Connectivity
             
        :param Input: 
                         Holds the informaiton about the <b>Mdc0ConnectionElement</b> object for querying
                         the elements.
             
        :return: 
        """
        ...

