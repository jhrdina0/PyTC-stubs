import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateInput:
    """
    
            This structure captures the inputs required for creation of a business object. This
            is a recursive structure containing the <code>CreateInput</code>(s) for any
            secondary(compounded) objects that might be created (e.g Item also creates
            ItemRevision and ItemMaster Form, etc.)
            
    """
    def __init__(self, ) -> None: ...
    BoName: str
    """Business object type name"""
    StringProps: System.Collections.Hashtable
    """Map of string property names to values (<code>string, string</code>)"""
    StringArrayProps: System.Collections.Hashtable
    """Map of string array property names to values (<code>string, vector<string></code>)"""
    DoubleProps: System.Collections.Hashtable
    """Map of double property names to values (<code>string, double</code>)"""
    DoubleArrayProps: System.Collections.Hashtable
    """Map of double array property names to values (<code>string, vector<double></code>)"""
    FloatProps: System.Collections.Hashtable
    """Map of float property names to values (<code>string, float</code>)"""
    FloatArrayProps: System.Collections.Hashtable
    """Map of float array property names to values (<code>string, vector<float></code>)"""
    IntProps: System.Collections.Hashtable
    """Map of int property names to values (<code>string, int</code>)"""
    IntArrayProps: System.Collections.Hashtable
    """Map of int array property names to values (<code>string, vector<int></code>)"""
    BoolProps: System.Collections.Hashtable
    """Map of boolean property names to values (string, bool)"""
    BoolArrayProps: System.Collections.Hashtable
    """Map of boolean array property names to values (<code>string, vector<bool></code>)"""
    DateProps: System.Collections.Hashtable
    """Map of DateTime property names to values (<code>string, DateTime</code>)"""
    DateArrayProps: System.Collections.Hashtable
    """Map of DateTime array property names to values (<code>string, vector<DateTime></code>)"""
    TagProps: System.Collections.Hashtable
    """Map of BusinessObject property names to values (<code>string, BusinessObjec</code>t)"""
    TagArrayProps: System.Collections.Hashtable
    """Map of BusinessObject array property names to values (<code>string, vector<BusinessObject></code>)"""
    CompoundCreateInput: System.Collections.Hashtable
    """
            Map of reference or relation property name to secondary <code>CreateInput</code>
            objects <code>(string, vector<CreateInput></code>)
            """

class CreateOrUpdateMDOResponse:
    """
    Return structure for created or updated MDThread as part of this operation
    """
    def __init__(self, ) -> None: ...
    MdoOutput: list[MDOOutput]
    """The created MDThread object or updated MDThread object output"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation"""

class DesignArtifactInput:
    """
    Design artifact input for createOrUpdateMDO operation
    """
    def __init__(self, ) -> None: ...
    AddDesignArtifact: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """
WorkspaceObject which has to be associated to the MDThread. Will be
            filled for create scenario. And optionally during update scenario.
            """
    RemoveDesignArtifact: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """
WorkspaceObject which has to be dis-associated from the MDThread. Used
            in update use case only. Will be empty for brand new MDThread creation. For
            replace scenario, the design artifacts which is substituting the old design artifact
            associated with MDO has to be passed in addDesignArtifact list, and the old and the
            old design artifact which is getting replace has to be passed in removeDesignArtifact
            list.
            """

class DesignArtifactInputsForSearch:
    """
    Design artifact search input for searchMDO operation.
    """
    def __init__(self, ) -> None: ...
    DesignArtifactsObjects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """
            Input set of WorkspaceObject for which the MDThread has to be searched.
            Searched MDThread should have minimum these design artifacts associated to
            it.
            """
    DesignArtifactCriteria: list[SearchAttribute]
    """
            Search criteria for design artifacts. If designArtifactsObjects is set, this input
            will be ignored. (This is for future purpose)
            """

class DesignInstancesData:
    """
    Design instance input for linkDesignInstances, unlinkDesignInstances operation.
    """
    def __init__(self, ) -> None: ...
    DesignInstance: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            Design Instance to be linked or unlinked or to be used for searching linked design
            instance.
            """
    IsPreciseLink: bool
    """
            Flag to indicate whether the linking or unlinking or search is to precise or imprecise
            design instance.
            """

class DesignInstancesInput:
    """
    
            Input structure for linkDesignInstances or unlinkDesignInstances or searchForLinkedDesignInstances
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional."""
    DesignInstancesData: list[DesignInstancesData]
    """List of design instances to be linked or unlinked or to be used for search."""
    Context: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            The context information for which the design instances are to be linked or unlinked
            or to be used for search. It is an optional input.
            """

class InstancesToLinkOutput:
    """
    
            A flag to indicate whether the instances are linked successfully or not is returned.
            Also the created or updated Mdo0MDInstance object will be returned.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    IsSuccess: bool
    """Flag to indicate whether linking is successful or not."""
    InstanceLinkingObject: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            The list of objects (Mdo0MDInstance) to which the design instances are linked
            together.
            """

class InstancesToLinkResponse:
    """
    Return structure for linkDesignInstances operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[InstancesToLinkOutput]
    """
            A list of  Mdo0MDInstance objects to which design instance is linked and flag
            to indicate the status of linking.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation."""

class InstancesToUnlinkResponse:
    """
    Return structure for unlinkDesignInstances operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[InstanceToUnlinkOutput]
    """The Mdo0MDInstance object from which the design instances are unlinked."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation."""

class InstanceToUnlinkOutput:
    """
    
            A flag to indicate whether the instances are unlinked successfully or not is returned.
            Also the Mdo0MDInstance object from which the design instance is unlinked
            will be returned.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    IsSuccess: bool
    """Flag to indicate whether unlinking is successful or not."""
    InstanceLinkingObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """The object (Mdo0MDInstance) from which the design instances are unlinked."""

class LinkedInstances:
    """
    The linked design instances searched.
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.Strong.POM_object
    """Context object if any available, for which the design instances are linked together."""
    Instances: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            List of linked design instances (Mdl0ModelElement) for the given input design
            instances.
            """

class LinkedInstancesOutput:
    """
    Output structure for searched linked design instances.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input."""
    LinkedInstances: list[LinkedInstances]
    """A list of LinkedInstances .The searched linked design instances."""

class MDOInput:
    """
    Input structure for createOrUpdateMDO operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    MdoCreInput: CreateInput
    """
            Create input structure with required inputs for creating MDThread  object.
            This data is ignored if the mdoObject is set, and the MDThread is being updated.
            """
    AttributeValues: System.Collections.Hashtable
    """
            A map of  attribute names and  values (key type/value type i.e. string/string)to
            be updated on the mdoObject. This map is ignored for creates.
            """
    ArtifactInput: DesignArtifactInput
    """Design artifacts (WorkspaceObject) to be associated or removed from MDThread."""
    MdoObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """MDThread object for update scenario. Set to NULL for create."""

class MDOOutput:
    """
    
            The created or updated or queried MDThread object will be returned. Also all
            the associated design artifacts for the MDThread will be returned.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    MdoObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The MDThread object."""
    AssociatedDesignArtifact: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """List of WorkspaceObject, Design artifacts which are associated to the MDThread."""

class MDOSearchOutput:
    """
    
            The search results for each input are returned. For each input there can be a one
            or more of MDThread objects found.
            
    """
    def __init__(self, ) -> None: ...
    MdoOutputs: list[MDOOutput]
    """
            List of MDThread found for each search input. All the associated design artifacts
            will be part of MDOOutput. The design artifacts will be of type WorkspaceObject.
            
            """

class SearchAttribute:
    """
    Attribute based search criteria for design artifacts.
    """
    def __init__(self, ) -> None: ...
    TypeObj: Teamcenter.Soa.Client.Model.Strong.ImanType
    """
ImanType object of the design artifacts for which the search criteria is defined.
            For eg: ItemRevision, LibraryElement
"""
    AttributeValues: System.Collections.Hashtable
    """
            A map of attribute names and  values (key type/value type i.e. string/string)to be
            used for search.
            """

class SearchForDesignArtifactInput:
    """
    Input structure for searchForArtifactsUsingInstances operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional."""
    DesignInstances: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            List of Design instances (Mdl0ModelElement)for which compatible design instances
            are to be searched.
            """

class SearchForLinkedInstancesInput:
    """
    Input structure for searchForLinkedDesignInstances operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional."""
    DesignInstanceInput: DesignInstancesInput
    """Design instances for which linked design instances are to be searched."""
    ConfigurationDetails: System.Collections.Hashtable
    """
            A map of context object and configuration data ( POM_object, ConfigurationContext)
            information for which linked design instances are to be searched for. This map may
            be empty.
            """
    Context: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            The context information for which the linked design instances are to be searched.
            It is an optional input.
            """

class SearchForLinkedInstancesResponse:
    """
    Return structure for searchForLinkedDesignInstances operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[LinkedInstancesOutput]
    """A list of linked design instances for the given input design instances."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation."""

class SearchInput:
    """
    Input structure for searchMDO operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    MdoCriteria: System.Collections.Hashtable
    """Input search criteria for MDThread object"""
    DesignArtifactInputs: DesignArtifactInputsForSearch
    """
            Search input for design artifacts . This input is used for search of MDThread
            for single design artifact or combination of design artifacts. If more than one design
            artifact object is given as input, the search will return all the MDThread
            which has this set of design artifact associated with it. If design artifact criteria
            are provided, the MDThread search uses the design artifact criteria and MdThread
            criteria.
            """

class SearchMDOResponse:
    """
    
            The searched MDThread objects will be returned. Also all the associated design
            artifacts for the MDThread will be returned.
            
    """
    def __init__(self, ) -> None: ...
    MdoSearchOutput: list[MDOSearchOutput]
    """Search result for each  search inputs"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation."""

class MultiDisciplinaryDataMgt:
    """
    Interface MultiDisciplinaryDataMgt
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateMDO(self, MdoInputs: list[MDOInput]) -> CreateOrUpdateMDOResponse:
        """    
             The operation creates a  new MDThread  object based on the MDThread
             properties and set of design artifacts (WorkspaceObject). The operation can
             optionally update an existing MDThread object by associating additional required
             design artifacts to it, or removing existing design artifacts association.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param MdoInputs: 
                         List of input data which contains information about the <b>MDThread</b> to be created
                         or updated
             
        :return: 
        """
        ...
    def LinkDesignInstances(self, Inputs: list[DesignInstancesInput]) -> InstancesToLinkResponse:
        """    
             The operation links two or more design instances from multi-discipline designs together
             through a common object Mdo0MDInstance. The operation may also update the
             design instance linkage by adding more design instances to the existing design instance
             linkage. Currently the Mdl0ModelElement is the supported object for design
             instance. If the linking is precise, the given design instance is used to link to
             the Mdo0Instance. If the linking is imprecise, the Mdl0ElementThread
             object of the Mdl0ModelElement is used for linking. If the input design instance
             is not a revisable type and do not have Mdl0ElementThread  then the instance
             will be linked precisely always.  Context information  for the linking of design
             instances is optional. If the context information is provided while linking design
             instances, then the design instance linkage is valid only for that context.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Design instance information to be linked together .
             
        :return: 
        """
        ...
    def SearchForArtifactsUsingInstances(self, SearchInputs: list[SearchForDesignArtifactInput]) -> SearchMDOResponse:
        """    
             The operation searches for MDThread and compatible design artifacts for the
             given design instances. Currently the Mdl0ModelElement is the supported object
             for design instance.  The underlying object for the Mdl0ModelElement is used
             for searching for Md0MDThread. If more than 1 design instance is given as
             input, all the designinstance's underlying object will be identified and collected.
             Then all the Mdo0MDThread objects containing this set of design artifacts
             will be returned.
             

Use Cases:

             Compatible design artifacts are associated to MDThread using createOrUpdateMDO services
             operation.
             
             Later the compatible design artifacts can be searched for using design instances.
             


Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param SearchInputs: 
                         Design instance information and for which compatible design artifacts are to be searched
                         for.
             
        :return: objects along with the associated design artifacts.
             Any failure will be returned with client id mapped to error message in the ServiceData
             list of partial errors.
        """
        ...
    def SearchForLinkedDesignInstances(self, Inputs: list[SearchForLinkedInstancesInput]) -> SearchForLinkedInstancesResponse:
        """    
             The operation searches for linked  design instances for the given design instances.
             Currently the Mdl0ModelElement is the supported object for design instance.
             If search is for precise design instance,  using the given input design instance,
             the linked other design instances are searched and returned.  If search is for imprecise
             design instance, the Mdl0ElementThread  object of the Mdl0ModelElement
             is used for search. If the input design instance is not a revisable type and do not
             have Mdl0ElementThread  then the search will be based on precise instance
             always.  If the context information is provided along with design instances input
             while searching for design instances, then the Mdo0MDInstance object for the
             given design instance and context is identified and design instance of the MdoMDInstance
             are returned as linked design instances. If only context information is provided
             as input, all the MdoMDInstance for that context are identified and all the
             design instances of the MdoMDInstance are returned as linked design instances.
             If configuration details are provided as part of input, for every  linked design
             instance if any configuration is provided in input, the configuration is applied
             and if it is valid for this configuration, then the design instance is returned as
             linked design instances.  Otherwise, the design instance is not returned as linked
             design instance for this input configuration.
             

Use Cases:

             The related design instances from Multi-discipline designs are linked together.
             
             Later the impacted design instance can be queried before making any change to the
             design instance.
             


Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Design instance information and optional context and configuration details for which
                         linked instances are to be searched for.
             
        :return: 
        """
        ...
    def SearchMDO(self, SearchInputs: list[SearchInput]) -> SearchMDOResponse:
        """    
             This operation searches the MDThread object based on attributes like name,
             description for MDThread and the search criteria for attributes like name,
             id, type for design artifacts associated to MDThread. Design artifacts will
             be of type WorkspaceObject.  All objects satisfying both MDThread attributes
             criteria and the design artifacts criteria will be returned as search results.
             
             If input has only design artifact objects in input, all MDThread having these
             design artifact associated with it will be returned.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param SearchInputs: 
                         Input search criteria for <b>MDThread</b> object based on <b>MDThread</b> attributes
                         and design artifact objects or attribute input for design artifacts.
             
        :return: search.
        """
        ...
    def UnlinkDesignInstances(self, Inputs: list[DesignInstancesInput]) -> InstancesToUnlinkResponse:
        """    
             The operation unlinks one or more design instances which are linked together through
             a common Mdo0MDInstance object. Currently the Mdl0ModelElement is the
             supported object for design instance. If the unlinking is precise, the given design
             instance is used to unlink from the Mdo0Instance. If the unlinking is imprecise,
             the Mdl0ElementThread  object of the Mdl0ModelElement is used for unlinking.
             If the input design instance is not a revisable type and do not have Mdl0ElementThread
             then the instance will be unlinked precisely always. Context information  for the
             unlinking of design instances is optional. If the context information is provided
             while unlinking design instances, then the Mdo0MDInstance object for the given
             context is indentified and design instance is unlinked from the MdoMDInstance.
             If the last design instance from the MdoMDInstance is unlinked, the MdoMDInstance
             will also be deleted.
             

Use Cases:

             The related design instances from Multi-discipline designs are linked together.
             
             Later the instance linkage can be modified, by unlinking some of the deisgn instance
             .
             


Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         The design instance information to be unlinked.
             
        :return: 
        """
        ...

