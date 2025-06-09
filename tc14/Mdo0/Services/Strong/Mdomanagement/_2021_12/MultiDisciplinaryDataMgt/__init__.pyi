import Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt
import Mdo0.Services.Strong.Mdomanagement._2018_06.MultiDisciplinaryDataMgt
import Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DesignInstanceInfo:
    """
    Design instance information input for operation.
    """
    def __init__(self, ) -> None: ...
    DesignInstanceFor4G: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """The Application Model design instance and the design instance will be of type Mdl0ModelElement."""
    BvrDesignInstance: Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.BVRInstanceData
    """The Product Structure assembly design instance."""

class DomainRelevancyInput2:
    """
    Input structure for UpdateDomainRelevancy2 operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    DesignArtifact: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The design artifact for which the domain relevancy information is to be updated.
            Design artifact is of type: WorkspaceObject. The supported types are defined
            in type constant Mdo0ValidMDTAssocTypes. Out of the box supported types are: Item,
            ItemRevision, Lbr0LibraryElement .
"""
    DesignInstanceInfo: DesignInstanceInfo
    """
            The design instance information for which the domain relevancy information is to
            be updated. The design instance can be Application Model or Product Structure Assembly
            design instance.
            """
    AddInformation: Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.RelevancyInformation
    """The domain relevancy information is to be added."""
    RemoveInformation: Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.RelevancyInformation
    """The domain relevancy information is to be removed."""

class DomainRelevancyOutput2:
    """
    Domain relevancy information available for a design artifact or design instance.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    DesignArtifact: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The design artifact for which the domain relevancy information is updated. Design
            artifact is of type: WorkspaceObject. The supported types are defined in type
            constant Mdo0ValidMDTAssocTypes. Out of the box supported types are: Item, ItemRevision,
            Lbr0LibraryElement.
"""
    DesignInstanceInfo: DesignInstanceInfo
    """
            The design instance information for which the domain relevancy information is updated.
            The design instance can be Application Model or Product Structure Assembly design
            instance.
            """
    DomainRelevancy: Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.RelevancyInformation
    """
            The relevant and irrelevant domain information available for the input design artifact
            or design instance.
            """

class GetDomainRelevancyInput2:
    """
    Input structure for getDomainRelevancyOfAnObject2 operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    DesignArtifact: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The design artifact for which the domain relevancy information is to be fetched.
            Design artifact is of type: WorkspaceObject. The supported types are defined
            in type constant Mdo0ValidMDTAssocTypes. Out of the box supported types are: Item,
            ItemRevision, Lbr0LibraryElement.
"""
    DesignInstanceInfo: DesignInstanceInfo
    """
            The design instance information for which the domain relevancy information is to
            be fetched. The design instance can be Application Model or Product Structure Assembly
            design instance.
            """
    Domain: str
    """
            The domain name for which relevancy information is to be identified for input object.
            It is an optional input. If empty, all the domain relevancy information for the input
            object will be identified and returned.
            """

class UpdateDomainRelevancyResponse2:
    """
    Return structure for UpdateDomainRelevancy2 operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[DomainRelevancyOutput2]
    """A list of domain relevancy information  for each  input."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains any partial errors occurred during the operation."""

class MultiDisciplinaryDataMgt:
    """
    Interface MultiDisciplinaryDataMgt
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDomainRelevancyOfAnObject2(self, Inputs: list[GetDomainRelevancyInput2]) -> Mdo0.Services.Strong.Mdomanagement._2018_06.MultiDisciplinaryDataMgt.GetDomainRelevancyOfAnObjectResp: ...
    def UpdateDomainRelevancy2(self, Inputs: list[DomainRelevancyInput2]) -> UpdateDomainRelevancyResponse2: ...

