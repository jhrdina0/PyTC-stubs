import Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetDomainRelevancyInput:
    """
    Input structure for getDomainRelevancyOfAnObject operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional."""
    InputObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            A design artifact or design instance object for which domain relevancy information
            is to be queried. The supported type for design artifact is a WorkspaceObject,
            for design instance it is a Mdl0ModelElement subclass.
            """
    Domain: str
    """The domain name used to find relevancy information; optional, can be empty string."""

class GetDomainRelevancyOfAnObjectOutput:
    """
    Return structure for getDomainRelevancyOfAnObject operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional."""
    RelevancyValue: str
    IsDesignArtifactBased: bool
    """
            If the relevancy value is from the design artifact this will be true, if the relevancy
            value is from the design instance then this will be false.
            """
    DomainRelevancy: Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.RelevancyInformation
    """
            The domain relevancy values. This will be populated only when the input domain is
            empty.
            """

class GetDomainRelevancyOfAnObjectResp:
    """
    Return structure for getDomainRelevancyOfAnObject operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[GetDomainRelevancyOfAnObjectOutput]
    """
            A list of the available domain relevancies for the  given input design objects and
            domains.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation."""

class SplitDesignArtifactInput:
    """
    Input structure for splitDesignArtifactsOfMDThread operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional."""
    DesignArtifacts: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """A  list of the original design artifacts which are to be split off."""
    SetValidationRequired: bool

class SplitDesignArtifactsOutput:
    """
    Output structure for the new Mdo0MDThread created for the split.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional."""
    IsSuccess: bool
    """If true, the split succeeded."""
    NewMDTObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The Mdo0MDThread object created for the given input design artifacts."""
    UpdatedMDTObjects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """
            The list of updated Mdo0MDThread  objects from  which the input design artifacts
            are split are also returned.
            """

class SplitDesignArtifactsResponse:
    """
    Return structure for splitDesignArtifactsOfMDThread operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[SplitDesignArtifactsOutput]
    """
            A list of created and updated Mdo0MDThread objects for the given input design
            artifacts.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation."""

class SplitDesignInstanceInput:
    """
    Input structure for splitDesignInstancesOfMDInstance operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional."""
    DesignInstances: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """A list of the original design instances which are to be split off."""
    Context: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            The context TC_Project object for which the design instances linking is applicable.
            It is an optional input.
            """
    SetValidationRequired: bool

class SplitDesignInstancesOutput:
    """
    Output structure for the new Mdo0MDInstance created for the split.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional."""
    IsSuccess: bool
    """True if split succeeded."""
    NewMDIObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """The Mdo0MDInstance created for the given input design instances."""
    UpdatedMDIObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            The updated Mdo0MDInstance objects from which the input design instances are
            split are also returned.
            """

class SplitDesignInstancesResponse:
    """
    Return structure for splitDesignInstancesOfMDInstance operation
    """
    def __init__(self, ) -> None: ...
    Output: list[SplitDesignInstancesOutput]
    """
            The list of created and updated Mdo0MDInstance objects for the given input
            design instances.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors that occurred during the operation."""

class MultiDisciplinaryDataMgt:
    """
    Interface MultiDisciplinaryDataMgt
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDomainRelevancyOfAnObject(self, Inputs: list[GetDomainRelevancyInput]) -> GetDomainRelevancyOfAnObjectResp:
        """    
             The operation returns domain relevancy of a design artifact or design instance for
             a input domain. If input is a design artifact, then the domain relevancy on the design
             artifact is used. If the input is a design instance, then the domain relevancy information
             of it is used. If there is no domain relevancy information on the design instance
             object for a domain, then domain relevancy information based on the underlying design
             artifact of the design instance will be used.
             
             If the input domain is specified then a relevancy value will be returned. If the
             input domain is not given then all domain relevancy information for the input object
             will be returned.
             

Use Cases:

             Associate a design artifact or design instance with domain relevancy information
             using the Mdo0::Soa::MDOManagement::_2017_05::MultiDisciplinaryDataMgt::updateDomainRelevancy
             service operation of MultiDisciplinaryDataMgt Service.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Input object and domain information for which domain relevancy is to be fetched.
             
        :return: 
        """
        ...
    def SplitDesignArtifactsOfMDThread(self, Inputs: list[SplitDesignArtifactInput]) -> SplitDesignArtifactsResponse:
        """    
             The operation removes the latest revision  ofdesign artifacts from their common Mdo0MDThread
             and links them to a newly created Mdo0MDThread object.
             
             The input design artifacts must be the latest revisions and must be associated with
             the same Mdo0MDThread.
             
             The new Mdo0MDThread will be returned. The updated Mdo0MDThread objects
             from which the input design artifacts are split are also returned.
             

Use Cases:

             Originally a set of design artifacts are linked to an Mdo0MDThread.
             
             Later a revise of one of the design artifacts will automatically link the new revision
             to the same Mdo0MDThread as the original design artifact.
             
             When a subset of the design artifacts need to be grouped differently, splitDesignArtifactsOfMDThread
             will remove them from one Mdo0MDThread and link them to a new Mdo0MDThread.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Design artifact information.
             
        :return: 
        """
        ...
    def SplitDesignInstancesOfMDInstance(self, Inputs: list[SplitDesignInstanceInput]) -> SplitDesignInstancesResponse:
        """    
             The operation removes the input design instances from their common Mdo0MDInstance
             and links them to a newly created Mdo0MDInstance object.  Currently the Mdl0ModelElement
             is the only supported object for design instance.
             
             The input design instances must be the latest revisions and must be associated with
             the same Mdo0MDInstance.
             
             The new Mdo0MDInstance will be returned. The updated Mdo0MDInstance
             objects from  which the input design instances are split are also returned.
             

Use Cases:

             Originally a set of design instances are linked to an Mdo0MDInstance.
             
             Later a revise of one of the design instances will automatically link the new revision
             to the same Mdo0MDInstance as the original design instances.
             
             When a subset of the design instances need to be grouped differently, splitDesignInstancesOfMDInstance
             will remove the design instances from one Mdo0MDInstance and link them to
             a new Mdo0MDInstance.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Design instance information.
             
        :return: 
        """
        ...

