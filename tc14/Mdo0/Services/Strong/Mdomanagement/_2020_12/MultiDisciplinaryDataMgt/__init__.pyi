import Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BVRAnd4GDesignInstancesInput:
    """
    Input structure for link4GAndBVRDesignInstances operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional."""
    DesignInstancesFor4G: list[InstanceDataFor4G]
    """A list of 4G design instances to be linked ."""
    BvrDesignInstances: list[BVRInstanceData]
    """A list of Product Structure assembly instances to be linked."""
    MdoObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The Mdo0MDThread information to be set on Mdo0MDInstance linkage. This
            is an optional input.
            """
    Context: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """
            The context TC_Project object for which the design instances linking is applicable.
            It is an optional input.
            """

class BVRAnd4GDesignInstancesUnlinkInput:
    """
    Input structure for unlink4GAndBVRDesignInstances operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional."""
    DesignInstancesFor4G: list[InstanceDataFor4G]
    """A list of 4G design instances to be unlinked."""
    BvrDesignInstances: list[BVRInstanceData]
    """A list of Product Structure assembly instances to be unlinked."""
    Context: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """
            The context TC_Project object for which the design instances are to be unlinked.
            It is an optional input.
            """
    UnlinkAllAssociatedDesignInstances: bool
    """
            If true, for the input design instance, Mdo0MDInstance will be identified and  all
            design instances associated with the identified Mdo0MDInstance will be unlinked and
            the identified Mdo0MDInstance will be deleted. If false, for the input design instances,
            Mdo0MDInstance will be identified and only the input design instances will be unlinked
            from the identified Mdo0MDInstance.
            """

class BVRAssemblyDetails:
    """
    Product Structure assembly details for the instance.
    """
    def __init__(self, ) -> None: ...
    ToplineObject: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Topline ItemRevision object for the Product Structure assembly."""
    ConfigData: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            ConfigurationContext object which contains configuration details to be applied on
            the Product Structure assembly. It is  optional. If this is not provided default
            revision rule set for Product Structure will be used.
            """

class BVRInstanceData:
    """
    Product Structure assembly design instance data for operation.
    """
    def __init__(self, ) -> None: ...
    InstanceOccThreadPath: str
    ConfiguredObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The configured underlying object of the Product Structure instance. Supported types
            are ItemRevision, GeneralDesignElement and its subclasses.
            """
    AssemblyDetails: BVRAssemblyDetails
    """Product Structure assembly details of the instance."""

class GetLinked4GAndBVRInstancesResponse:
    """
    Return structure for the getLinkedInstancesFor4G or getLinkedInstancesForBVR operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[Linked4GAndBVRInstancesOuput]
    """
            A list of output data which contains the information about linked design instances
            for the given input design instances.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains any partial errors occurred during the operation."""

class InstanceDataFor4G:
    """
    4G Design instance input for operation.
    """
    def __init__(self, ) -> None: ...
    DesignInstanceFor4G: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """4G Design Instance. The design instance will be of type Mdl0ModelElement."""
    IsPreciseLink: bool
    """If true, the linking is precise; otherwise, linking is imprecise."""

class GetLinkedInstancesInputFor4G:
    """
    Input structure for getLinkedInstancesFor4G operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input.It is optional."""
    Input4GDesignInstance: InstanceDataFor4G
    """Input 4G design instance for which linked design instances are to be searched."""
    Context: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """
            The context TC_Project object for which the linked design instances are to be searched.
            It is an optional input.
            """
    ConfigForOtherSide4GData: System.Collections.Hashtable
    """
            A map of context object and configuration data(Mdl0ApplicationModel, ConfigurationContext)
            to be used for search of 4G design instances. It is an optional input.
            """
    ConfigForOtherSideBVRData: list[BVRAssemblyDetails]
    """
            A list of configuration information for other side linked Product Structure assembly
            instances. This input is required to identify the PSOccurrenecThread path for the
            linked instance, topline context ItemRevision object, configured underlying object
            of the linked Product Structure assembly instance. It is an optional input.
            """

class GetLinkedInstancesInputForBVR:
    """
    Input structure for getLinkedInstancesForBVR operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input.It is optional."""
    InputBVRDesignInstance: BVRInstanceData
    """
            Input Product Structure assembly instance for which linked design instances are to
            be searched.
            """
    Context: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """
            The context TC_Project object for which the linked design instances are to be searched.
            It is an optional input.
            """
    ConfigForOtherSide4GData: System.Collections.Hashtable
    """
            A map of context object and configuration data( Mdl0ApplicationModel, ConfigurationContext)
            to be used for search of 4G design instances . This is an optional input.
            """
    ConfigForOtherSideBVRData: list[BVRAssemblyDetails]
    """
            A list of configuration information for other side linked Product Structure assembly
            instances. This input is required to identify the PSOccurrenecThread path for the
            linked instance, topline context ItemRevision object, configured underlying object
            of the linked Product Structure assembly instance. This is an optional input.
            """

class Impacted4GAndBVRInstanceInfo:
    """
    
            The searched design instance objects will be returned. Also all the validation status
            captured on the Mdo0MDInstance association for each design instance for an Mdo0MDInstance
            will be returned. The relevant and irrelevant domain information for the 4G design
            instance will be returned.
            
    """
    def __init__(self, ) -> None: ...
    DesignInstanceFor4G: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """
            Linked 4G design instance which is associated to the Mdo0MDInstance. The 4G design
            instance will be of Mdl0ModelElement and its subclasses.
            """
    BvrInstanceData: BVRInstanceData
    """
            Linked Product Structure assembly instance data which is associated to the Mdo0MDInstance.
            Either 4GDesignInstance or bvrInstanceData will be populated for linked design instance.
            """
    NeedsValidation: bool
    """
            The value of the Mdo0MDInstance association status to state whether it needs validation
            is returned. If true, the association needs validation, otherwise, no validation
            is required.
            """
    IsValidated: bool
    """
            The value of the Mdo0MDInstance association status to state whether it is validated
            is returned. If true, the association is validated; otherwise, the association is
            not validated.
            """
    RelevantDomains: list[str]
    IrrelevantDomains: list[str]

class InstancesToUnlinkOutput2:
    """
    
            A structure which contains the Mdo0MDInstance objects from which the design instance
            is unlinked will be returned.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    InstanceLinkingObject: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            A list of Mdo0MDInstance objects from which the design instances are unlinked. If
            Mdo0MDInstance is deleted as part of unlink process, this will be empty.
            """

class InstancesToUnlinkResponse2:
    """
    Return structure for unlink4GAndBVRDesignInstances operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[InstancesToUnlinkOutput2]
    """
            A list of output data which contains the Mdo0MDInstance object from which the design
            instances are unlinked.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains any partial errors occurred during the operation."""

class Linked4GAndBVRInstances:
    """
    
            The structure which contains information of linked design instances identified as
            part of search and its associated information.
            
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """
            The context TC_Project object if any available, for which the design instances are
            linked together.
            """
    MdiObject: Teamcenter.Soa.Client.Model.Strong.Mdo0MDInstance
    """The Mdo0MDInstance object to which the instance is linked to."""
    MdoObjectsLinkedToMDI: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """A list of Mdo0MDThread object associated to the linked Mdo0MDInstance."""
    InstancesInfo: list[Impacted4GAndBVRInstanceInfo]
    """
            A list of linked design instances and associated information for the given input
            design instance.
            """

class Linked4GAndBVRInstancesOuput:
    """
    Output structure for searched linked design instances.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    HasLinkedInstance: bool
    """
            If input design instance is linked to another design instance the value is set to
            true. This will be used by application, to know that the input design instance is
            linked, and other side Product Structure assembly instance information cannot be
            fetched due to insufficient additional input.
            """
    LinkedInstances: list[Linked4GAndBVRInstances]
    """A list of searched linked design instance information."""

class MultiDisciplinaryDataMgt:
    """
    Interface MultiDisciplinaryDataMgt
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetLinkedInstancesFor4G(self, Inputs: list[GetLinkedInstancesInputFor4G]) -> GetLinked4GAndBVRInstancesResponse: ...
    def GetLinkedInstancesForBVR(self, Inputs: list[GetLinkedInstancesInputForBVR]) -> GetLinked4GAndBVRInstancesResponse: ...
    def Link4GAndBVRDesignInstances(self, Inputs: list[BVRAnd4GDesignInstancesInput]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.InstancesToLinkResponse2: ...
    def Unlink4GAndBVRDesignInstances(self, Inputs: list[BVRAnd4GDesignInstancesUnlinkInput]) -> InstancesToUnlinkResponse2: ...

