import Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt
import Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DesignArtifactInfo2:
    """
    
            The searched design artifact objects will be returned. Also all the validation status
            captured on the Mdo0MDThread association for each design artifacts for an
            Mdo0MDThread will also be returned.
            
    """
    def __init__(self, ) -> None: ...
    DesignArtifact: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            Design artifact which are associated to the Mdo0MDThread. The design artifacts
            will be of type WorkspaceObject.
            """
    NeedsValidation: bool
    """
            The value of the Md0MDThread association status to state whether it needs
            validation is returned. True value means it needs validation.  False means no validation
            will be required. It can be empty too.
            """
    IsValidated: bool
    """
            The value of the Md0MDThread association status to state whether it is validated
            is returned. True means this association is already validated. False means it is
            not validated. It can be empty too.
            """
    RelevantDomains: list[str]
    """
            The list of relevant domains for the design artifact. This will be empty when input
            filter criteria is passed for domain relevancy.
            """
    IrrelevantDomains: list[str]
    """
            The list of irrelevant domains for the design artifact. This will be empty when input
            filter criteria is passed for domain relevancy.
            """

class DesignInstancesInput2:
    """
    Input structure for linkDesignInstances2 operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional"""
    DesignInstancesData: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.DesignInstancesData]
    """List of design instances to be linked"""
    MdoObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The Mdo0MDThread information to be set on Mdo0MDInstance linkage. This
            is an optional input.
            """
    Context: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            The context information for which the design instances linking is applicable. It
            is an optional input.
            """

class RelevancyInformation:
    """
    List of relevant and irrelevant domain names for a design artifact or design instance.
    """
    def __init__(self, ) -> None: ...
    RelevantDomain: list[str]
    """The list of relevant domains for a design artifact or design instance."""
    IrrelevantDomain: list[str]
    """The list of irrelevant domains for a design artifact or design instance."""

class DomainRelevancyInput:
    """
    Input structure for UpdateDomainRelevancy operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional."""
    DesignArtifact: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The design artifact or design instance for which the domain relevancy information
            has to be updated.
            """
    AddInformation: RelevancyInformation
    """
            The list of domains for which the domain relevancy information has to be added for
            the design artifact or design instance.
            """
    RemoveInformation: RelevancyInformation
    """
            The list of domains for which the domain relevancy information has to be removed
            from the design artifact or design instance.
            """

class DomainRelevancyOutput:
    """
    Domain relevancy information available for a design artifact or design instance.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional."""
    DesignArtifact: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The design artifact or design instance for which the domain relevancy information
            is updated.
            """
    DomainRelevancy: RelevancyInformation
    """
            The list of relevant and irrelevant domain information available for the input design
            artifact or design instance.
            """

class FilterForDomainRelevancy:
    """
    Filter criteria to filter design artifacts based on domain relevancy information
    """
    def __init__(self, ) -> None: ...
    IsFilterForRelevantDomain: bool
    """
            The input flag to indicate the filter for domain has to be applied on relevant or
            irrelevant domain information.  If it is true, all the design artifacts which are
            marked as relevant for this domain only will be returned. If it is false, all the
            design artifact which are marked  as irrelevant for this domain only will be returned.
            """
    Domain: str
    """The domain for which the filter is applied."""

class ImpactedDesignInstanceInfo2:
    """
    
            The searched design instance objects will be returned. Also all the validation status
            captured on the Mdo0MDInstance association for each design instance for an
            Mdo0MDInstance will be returned. Also the relevant and irrelevant domain for
            the design instance or the design artifact of the linked design instance will be
            returned.
            
    """
    def __init__(self, ) -> None: ...
    DesignInstance: Teamcenter.Soa.Client.Model.Strong.POM_object
    """Linked design artifact which is associated to the Mdo0MDInstance."""
    NeedsValidation: bool
    """
            The value of the Mdo0MDInstance association status to state whether it needs
            validation is returned. True value means it needs validation.  False means no validation
            will be required. It can be empty too.
            """
    IsValidated: bool
    """
            The value of the Mdo0MDInstance association status to state whether it is
            validated is returned. True means this association is already validated. False means
            it is not validated.
            """
    RelevantDomains: list[str]
    """
            The list of relevant domains for the design instance or the design artifact of the
            linked design instance.
            """
    IrrelevantDomains: list[str]
    """
            The list of irrelevant domains for the design instance or the design artifact of
            the linked design instance.
            """

class InstanceLinkingObjectData:
    """
    
            The created instance linking object and the Mdo0MDThread object set on the
            Mdo0MDInstance object will be returned.
            
    """
    def __init__(self, ) -> None: ...
    MdiObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """The Mdo0MDInstance object to which the design instances are linked together."""
    MdoObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The Mdo0MDThread object set on the Mdo0MDInstance object."""

class InstancesToLinkOutput2:
    """
    
            A flag to indicate whether the instances are linked successfully or not is returned.
            Also the created or updated Mdo0MDInstance object data will be returned
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    IsSuccess: bool
    """Flag to indicate whether linking is successful or not"""
    InstanceLinkingObjectData: list[InstanceLinkingObjectData]
    """The list of instance object  to which the design instances are linked together."""

class InstancesToLinkResponse2:
    """
    Return structure for linkDesignInstances2 operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[InstancesToLinkOutput2]
    """
            A list of  Mdo0MDInstance objects to which design instance is linked and flag
            to indicate the status of linking.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation."""

class LinkedInstances2:
    """
    The linked design instances searched.
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.Strong.POM_object
    """Context object if any available, for which the design instances are linked together."""
    MdiObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """The Mdo0MDInstance object to which the instance is linked to."""
    MdoObjectsLinkedToMDI: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """The list of Mdo0MDThread  objects associated to the linked Mdo0MDInstance."""
    InstancesInfo: list[ImpactedDesignInstanceInfo2]
    """List of linked design instances for the given input design instances."""

class LinkedInstancesOuput2:
    """
    Output structure for searched linked design instances.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional"""
    LinkedInstances: list[LinkedInstances2]
    """The searched linked design instances."""

class MDInstanceData:
    """
    
            The Mdo0MDInstance and the design instances with needs validation status captured
            on association is searched and returned.
            
    """
    def __init__(self, ) -> None: ...
    MdiObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """The Mdo0MDInstance object to which the instance is linked to."""
    Instances: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """List of linked design instances for the given input design instances."""

class MDInstanceLinkCarryFwdInput:
    """
    Input structure for carryForwardMDInstanceAssociation operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input."""
    OriginalDesignInstance: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            The original design instance whose Mdo0MDInstance association will be carried forward
            to the new design instance.
            """
    TargetDesignInstance: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            The target design instance which will  be associated with the same Mdo0MDInstance
            association as the original design instance.
            """
    SetValidationRequired: bool
    """
            This input controls, whether needsValidation attribute is set to true or not in association
            between Mdo0MDInstance and design instance.
            """

class MDInstanceToMDThreadInput:
    """
    Input structure for UpdateMDInstanceToMDThreadLink operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional"""
    MdiObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            The Mdo0MDInstance for which the Mdo0MDThread information has to be
            updated.
            """
    AddMDOObjects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """The list of Mdo0MDThread objects to be set on  Mdo0MDInstance."""
    RemoveMDOObjects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """The list of Mdo0MDThread objects to be removed from Mdo0MDInstance."""

class MDIToMDOLinkOutput:
    """
    The Mdo0MDThread to Mdo0MDInstance association results.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    LinkedMDOObjects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """The list of Mdo0MDThread objects set on Mdo0MDInstance."""

class MDOOutput3:
    """
    
            The searched Mdo0MDThread object will be returned. Also all the associated
            design artifacts for the Mdo0MDThread will be returned.
            
    """
    def __init__(self, ) -> None: ...
    MdoObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The searched Mdo0MDThread object."""
    AssociatedDesignArtifact: list[DesignArtifactInfo2]
    """
            Design artifacts which are associated to the Mdo0MDThread. The design artifacts
            will be of type WorkspaceObject.
            """

class MDOSearchOutput3:
    """
    
            The search results for each input are returned. For each input there can be a one
            or more of Mdo0MDThread objects found.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    MdoOutput: list[MDOOutput3]
    """
            List of Mdo0MDThread found for each search input. All the associated design
            artifacts along with domain information will be part of MDOOutput3. The design artifacts
            will be of type WorkspaceObject.
            """

class MDThreadLinkCarryFwdInput:
    """
    Input structure for carryForwardMDThreadAssociation operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input."""
    OriginalDesignArtifact: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The original design artifact based on which Mdo0MDThread is identified and to which
            the target design artifact has to be associated
            """
    TargetDesignArtifact: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The target design artifact for which the Mdo0MDThread has to be carried forward based
            on original design artifact input.
            """
    SetValidationRequired: bool
    """
            This input controls, whether needsValidation attribute is set to true or not in association
            between Mdo0MDThread and design artifact.
            """

class NeedsValidationLinkInput:
    """
    Input structure for queryNeedsValidationLink operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    InputMDO: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The input Mdo0MDThread for which all association to design artifacts which
            has needs validation status captured on association needs to be identified. If this
            input is passed in, inputDesignArtifact input will be ignored.
            """
    InputDesignArtifact: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The input design artifact for which the associated association with the needs validation
            is to be identified with all its design artifact association which has needs validation
            status captured on association.
            """
    InputDesignInstance: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            The input design instance for which the associated association with the needs validation
            is to be identified with all its design instance association which has needs validation
            status captured on association.
            """
    QueryAllMDOLinks: bool
    """
            The flag to indicate that all Mdo0MDThread association which has needs validation
            status captured on association needs to be searched. If this is true then inputMDO,
            and inputDesignArtifact inputs will be ignored.
            """
    QueryAllMDILinks: bool
    """
            The flag to indicate that all Mdo0MDInstance association which has needs validation
            status captured on association needs to be searched. If this is true then inputDesignInstance
            input will be ignored.
            """

class NeedsValidationLinkOutput:
    """
    
            The Mdo0MDThread and Mdo0MDInstance association which has needs validation
            status captured on association is searched and returned.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    MdoLinkOutput: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.MDOOutput]
    """
            The list of Mdo0MDThread association which has needs validation status captured
            on association.
            """
    MdiLinkOutput: list[MDInstanceData]
    """
            The list of Mdo0MDInstance association which has needs validation status captured
            on association.
            """

class NeedsValidationLinkResponse:
    """
    
            The Mdo0MDThread and Mdo0MDInstance association which has needs validation
            status captured on association is searched and returned.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation."""
    LinkQueryOutput: list[NeedsValidationLinkOutput]
    """
            The Mdo0MDThread and Mdo0MDInstance association with needsvalidation
            status captured.
            """

class SearchForDesignArtifactInput3:
    """
    Input structure for searchForArtifactsUsingInstances3 operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional"""
    DesignInstances: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            List of Design instances (Mdl0ModelElement)for which compatible design instances
            are to be searched.
            """
    FilterForDomainRelevancy: FilterForDomainRelevancy
    """
            The filter information to be applied on searched design artifacts and only design
            artifact satisfying the filter criteria will be returned. If this input is empty,
            all the design artifact will be returned with relevant and irrelevant domain information.
            It is an optional input.
            """

class SearchForLinkedInstances2Response:
    """
    Return structure for searchForLinkedDesignInstances2 operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[LinkedInstancesOuput2]
    """The linked design instances for the given input design instances ."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation."""

class SearchInput3:
    """
    Input structure for searchMDO3 operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    MdoCriteria: System.Collections.Hashtable
    """Input search criteria for Mdo0MDThread object."""
    DesignArtifactInputs: Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.DesignArtifactInputsForSearch
    """
            Search input for design artifacts . This input is used for search of MDThread for
            single design artifact or combination of design artifacts. If more than one design
            artifact object is given as input, the search will return all the MDThread which
            has this set of design artifact associated with it. If design artifact criteria are
            provided, the MDThread search uses the design artifact criteria and MdThread criteria.
            """
    FilterCriteria: Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.FilterForSearch
    """
            The criteria to be applied on compatible design artifacts of MDThread. Only compatible
            design artifacts satisfying the filter criteria will be returned as part of search
            output. It is an optional input.
            """
    FilterForDomainRelevancy: FilterForDomainRelevancy
    """
            The filter information to be applied on searched design artifacts and only design
            artifact satisfying the filter criteria will be returned. If this input is empty,
            all the design artifact will be returned with relevant and irrelevant domain information.
            It is an optional input.
            """

class SearchMDO3Response:
    """
    
            The searched Mdo0MDThread objects will be returned. Also all the associated
            design artifacts for the Mdo0MDThread  will be returned.
            
    """
    def __init__(self, ) -> None: ...
    MdoSearchOutput: list[MDOSearchOutput3]
    """Search result  for each  search inputs."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation."""

class UpdatedLinksOutput:
    """
    
            The Mdo0MDThread, Mdo0MDInstance whose associations are updated will
            be returned.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    MdiObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            The Mdo0MDInstance for which the Mdo0HasInstanceAssociation is updated
            to validated status.
            """
    MdoObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The Mdo0MDThread for which the Mdo0MDTAssociation is updated to validated
            status.
            """

class UpdateDomainRelevancyResponse:
    """
    Return structure for UpdateDomainRelevancy operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[DomainRelevancyOutput]
    """Domain relevancy information  for each  input."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors that occurred during the operation."""

class UpdateLinkStatusToValidatedInput:
    """
    Input structure for UpdateLinksToValidated operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional"""
    MdiDataForUpdate: MDInstanceData
    """
            The Mdo0MDInstance and design instance for which the Mdo0HasInstanceAssociation
            needs to be updated to validated status.
            """
    MdoDataForUpdate: Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.MDOOutput
    """
            The Mdo0MDThread and design artifact for which the Mdo0MDTAssociation
            needs to be updated to validated status.
            """

class UpdateLinksToValidatedResponse:
    """
    
            The Mdo0MDThread, Mdo0MDInstance whose association is updated will
            be returned.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[UpdatedLinksOutput]
    """
Mdo0MDInstance and Mdo0MDThread whose associations are updated  for
            each  input.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation."""

class UpdateMDInstanceToMDThreadResponse:
    """
    The Mdo0MDThread objects associated to Mdo0MDInstance will be returned.
    """
    def __init__(self, ) -> None: ...
    LinkOutput: list[MDIToMDOLinkOutput]
    """Mdo0MDInstance to MDo0MDThread association output  for each  inputs."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation."""

class MultiDisciplinaryDataMgt:
    """
    Interface MultiDisciplinaryDataMgt
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CarryForwardMDInstanceAssociation(self, Inputs: list[MDInstanceLinkCarryFwdInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchForLinkedInstancesResponse:
        """    
             The operation searches for the Mdo0MDInstance associated with input original design
             instance and associates the target design instance with the identified Mdo0MDInstance
             objects precisely. The newly created Mdo0MDInstance association will capture the
             needs validation status on the association as yes.
             

Use Cases:

             Impacted design instances are associated to Mdo0MDInstance using linkDesignInstances
             services operation.
             
             Later the design instance of Mdo0MDInstance is revised.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Design instance information from which the Mdo0MDInstance association needs to be
                         carried forward to a new design instance.
             
        :return: 
        """
        ...
    def CarryForwardMDThreadAssociation(self, Inputs: list[MDThreadLinkCarryFwdInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchMDOResponse:
        """    
             The operation searches for the Mdo0MDThread associated with input original design
             artifact and associates the target design artifact with the identified Mdo0MDThread
             objects. The newly created Mdo0MDThread association will capture the needs validation
             status on the association as yes.
             

Use Cases:

             Compatible design artifacts are associated to Mdo0MDThread using createOrUpdateMDO
             services operation.
             
             Later the design artifact of Mdo0MDThread is revised.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Design artifact information  based on which the Mdo0MDThread  association needs to
                         be carried forward to the new design artifact.
             
        :return: 
        """
        ...
    def LinkDesignInstances2(self, Inputs: list[DesignInstancesInput2]) -> InstancesToLinkResponse2:
        """    
             The operation links two or more design instances from multi-discipline designs together
             through a common object Mdo0MDInstance. The operation may also update the
             design instance linkage by adding more design instances to the existing design instance
             linkage. Currently the Mdl0ModelElement is the only supported object for design
             instance. If the linking is precise, the given design instance is used to link to
             the Mdo0Instance. If the linking is imprecise, the Mdl0ElementThread
             object of the Mdl0ModelElement is used for linking. If the input design instance
             is not a revisable type and do not have Mdl0ElementThread  then the instance
             will be linked precisely always. Context information  for the linking of design instances
             is optional. If the context information is provided while linking design instances,
             then the design instance linkage is valid only for that context.  Mdo0MDThread
             information to be set on Mdo0MDIntance can be part of input.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Design instance information to be linked together .
             
        :return: 
        """
        ...
    def QueryNeedsValidationLink(self, QueryInput: list[NeedsValidationLinkInput]) -> NeedsValidationLinkResponse:
        """    
             This operation searches for Mdo0MDThread association and Mdo0MDInstance
             association which has needs validation status captured on the association. If queryAllMDOLinks
             input is passed in, all the Mdo0MDThread association with the needs validation
             will be searched and returned. If inputMDO is passed in, only Mdo0MDThread
             association with passed in input as primary and association which has needs validation
             will be identified and returned. If input inputDesignArtifact is passed in, all Mdo0MDThread
             association having this design artifact as secondary and needs validation captured
             on association will be returned. If queryAllMDILinks input is passed in, all the
             Mdo0MDInstance association with the needs validation will be searched and
             returned. If input inputDesignInstance is passed in, all Mdo0MDInstance association
             having this design instance as secondary and needs validation captured on association
             will be returned.
             

Use Cases:

             Case1:
             
             Compatible design artifacts are associated to Mdo0MDThread using createOrUpdateMDO
             services operation.
             
             The design artifact of Mdo0MDThread is revised.
             
             Query for MDO association with needs validation link.
             
             Case2:
             
             Impacted design instances are associated to Mdo0MDInstance using linkDesignInstances
             services operation.
             
             The design instance of Mdo0MDInstance is revised.
             
             Query for MDI association with needs validation link.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param QueryInput: 
                         Input search criteria for <b>Mdo0MDThread</b> association and <b>Mdo0MDInstance</b>
                         association which has needs validation status on association.
             
        :return: 
        """
        ...
    def SearchForArtifactsUsingInstances3(self, Inputs: list[SearchForDesignArtifactInput3]) -> SearchMDO3Response: ...
    def SearchForLinkedDesignInstances2(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchForLinkedInstancesInput]) -> SearchForLinkedInstances2Response:
        """    
             The operation is used to search for linked  design instances for the given input
             design instances. Currently the Mdl0ModelElement is the supported object for
             design instance. If search is for precise design instance,  using the given input
             design instance, the linked other design instances are searched and returned.  If
             search is for imprecise design instance, the Mdl0ElementThread  object of
             the Mdl0ModelElement is used for search. If the context information is provided
             along with design instances input while searching for design instances, then the
             Mdo0MDInstance object for the given design instance and context is identified
             and design instance of the Mdo0MDInstance are returned as linked design instances.
             If only context information is provided as input, all the Mdo0MDInstance for
             that context is identified and all the design instances of the MdoMDInstance is retrurned
             as linked design instances. If configuration destail are provided as part of input,
             for every  linked design instance if any configuration is provided in input, the
             configuration is applied and if it is valid for this configuration, then the design
             instance is returned as linked design instances.  Otherwise, the design instance
             is not returned as linked design instance for this input configuration.
             

Use Cases:

             The related design instances from Multi-discipline designs are linked together.
             
             Later the impacted design instance can be queried before making any change to the
             design instance.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         List of input data which contains design instance information and optional context
                         and configuration details for which linked instances are to be searched for.
             
        :return: 
        """
        ...
    def SearchMDO3(self, SearchInputs3: list[SearchInput3]) -> SearchMDO3Response: ...
    def UpdateDomainRelevancy(self, Inputs: list[DomainRelevancyInput]) -> UpdateDomainRelevancyResponse: ...
    def UpdateLinksToValidated(self, Inputs: list[UpdateLinkStatusToValidatedInput]) -> UpdateLinksToValidatedResponse:
        """    
             The operation updates  association between the given Mdo0MDInstance and its
             design instance,  the given Mdo0MDThread and its design artifact association
             to validated status.
             

Use Cases:

             Case1:
             
             Compatible design artifacts are associated to Mdo0MDThread using createOrUpdateMDO
             services operation.
             
             The design artifact of Mdo0MDThread is revised.
             
             Query for MDO association with needs validation link.
             
             Update the MDO association status to validated.
             
             Case2:
             
             Impacted design instances are associated to Mdo0MDInstance using linkDesignInstances
             services operation.
             
             The design instance of Mdo0MDInstance is revised.
             
             Query for MDI association with needs validation link.
             
             Update the MDI association status to validated.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         The input for <b>Mdo0MDThread</b> and <b>Mdo0MDInstance</b> associations to be updated.
             
        :return: 
        """
        ...
    def UpdateMDInstanceToMDThreadLink(self, Inputs: list[MDInstanceToMDThreadInput]) -> UpdateMDInstanceToMDThreadResponse:
        """    
             The operation sets or removes association between the given Mdo0MDInstance
             and Mdo0MDThread business object.
             

Use Cases:

             Compatible design artifacts are associated to Mdo0MDThread using createOrUpdateMDO
             services operation.
             
             The related design instances from Multi-discipline designs are linked together.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         The <b>Mdo0MDThread</b> information to be set on <b>Mdo0MDIntance</b> or removed
                         from <b>Mdo0MDInstance</b>.
             
        :return: 
        """
        ...

