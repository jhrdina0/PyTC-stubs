import System
import System.Collections
import Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ConfigurationContextChoice:
    """
    This structure contains context related info.
    """
    def __init__(self, ) -> None: ...
    InternalValue: str
    """Internal value of business object."""
    DisplayValue: str
    """Display value of business object."""
    IsDefaultValue: bool
    """If true, this choice is set to default; otherwise, false."""

class ProjectInformation2:
    """
    Structure that holds the information required to create the destination project.
    """
    def __init__(self, ) -> None: ...
    ProjectId: str
    """The project ID of the project to be created."""
    ProjectName: str
    """The name of the project to be created."""
    ProjectDescription: str
    """The description of the project to be created."""
    UseProgramContext: bool
    """
            The value of useProgramContext property in TC_Project.
            
            If value is true TC_Project is treated as program and if false it is project.
            """
    Active: bool
    """
            The value of property  in TC_Project.
            
            If value is true than project is active so user can add/remove objects into this
            project. If value is false than project is no longer active. It will only available
            for viewing purpose. No further modification can be done on project.
            """
    Visible: bool
    """
            The value of visible property in TC_Project.
            
            If value is true than this project will be visible to user in teamcenter otherwise
            project will be invisible.
            """
    TeamMembers: list[Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.TeamMemberInfo]
    """A list of TeamMemberInfo structures."""
    ClientId: str
    """Unique identifier used by the client to track any errors."""
    PropertyMap: System.Collections.Hashtable
    """
            A map of property names and desired values (string/string). This is map with property
            name and list of values in string format. The calling client is responsible for converting
            the different property types (int, float, date .etc) to a string using the appropriate
            functions in the SOA client framework's Property class.
            """

class CopyProjectsInfo2:
    """
    
            Structure that holds project information required to create a new TC_Project object
            using this operation.
            
    """
    def __init__(self, ) -> None: ...
    SourceProject: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """The TC_Project object needs to be copied."""
    ProjectInfo: ProjectInformation2
    """The information required to copy the project."""
    ClientId: str
    """Unique identifier used by the client to track any errors."""

class ModifyProjectsInfo2:
    """
    
            This structure holds the TC_Project object and the information required to modify
            the project.
            
    """
    def __init__(self, ) -> None: ...
    SourceProject: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """The TC_Project object to be modified."""
    ProjectInfo: ProjectInformation2
    """The information required to create the destination project."""
    ClientId: str
    """Unique identifier used by the client to track any errors."""

class OverrideInfo:
    """
    This contains information about the override RevisionRule entry
    """
    def __init__(self, ) -> None: ...
    RuleEntry: Teamcenter.Soa.Client.Model.Strong.CFMOverrideEntry
    """Refers to the CFMOverrideEntry of a RevisionRule object."""
    Folder: Teamcenter.Soa.Client.Model.Strong.Folder
    """Refers to the Folder of override rule entry of RevisionRule object ."""

class PaginationInfo:
    """
    A Structure containing pagination criteria.
    """
    def __init__(self, ) -> None: ...
    StartIndexForAvailableProjects: int
    """The start index to return the  available projects."""
    MaxToReturnForAvailableProjects: int
    """The maximum number of available available projects to return."""

class PropagationConfigurationContext:
    """
    
            PropagationConfigurationContext contains data which can be applied to assign to projects
            and remove from projects operation.
            
    """
    def __init__(self, ) -> None: ...
    SelectedTopLevelObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Selected top level object in context of ACE ( Active Content Expericence ), if this
            object is passed we will fetch variant rule and revision rule.
            """
    VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule
    """

            The VariantRule in context of the assign to project  or attach to license operation.
            """
    RevisionRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """The RevisionRule associated with the assign to project or attach to license operation."""
    TypeOption: int
    """
            An integer indicating the type of Item or Item Revision, valid values are 0 for Item
            and 1 for Item Revision.
            """
    Depth: int
    """
            A number indicating how deep the traversal needs to be performed for a given structure,
            applicable only for structures.
            """

class ProjectAssignOrRemoveInput:
    """
    

            Contains data used for assigning given set of objects to a list project objects for
            a given set of  configuration context.
            
    """
    def __init__(self, ) -> None: ...
    ProjectsToAssign: list[Teamcenter.Soa.Client.Model.Strong.TC_Project]
    """A list of TC_Project objects to for assignment."""
    ObjectsForAssignment: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of BusinessObject that needs to be assigned (added) to the given projects
            provided by projectsToAssing input parameter.
            """
    ProjectsForRemoval: list[Teamcenter.Soa.Client.Model.Strong.TC_Project]
    """The TC_Project objects which needs to be removed from the given set of objects."""
    ObjectsToRemoveFromProjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of BusinessObject that needs to be removed from the given set of projects
            provided in projectsForRemoval parameter.
            """
    ContextInfo: PropagationConfigurationContext
    """A PropagationConfigurationContext structure."""
    ProcessAsynchronously: bool
    """
            Flag indicating if this operation needs to be processed in asynchronously. A value
            True means to process it asynchronously. If the value is not set or is set to False
            then processing happens synchronously in the same request.
            """

class ProjectOrLicenseDataInput:
    """
    Structure containing data for changing license and project data on WorkspaceObject.
    """
    def __init__(self, ) -> None: ...
    SelectedObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of WorkspaceObject objects to be either attached or detached from selected
            list of Licenses or assigned or removed from selected list of projects
            """
    SelectedProjectsOrLicenses: list[str]
    """
            A list of license IDs of ADA_License or Project IDs for TC_Project.
            These are strings of each with a maximum of 128 bytes size.
            """
    EadParagraph: list[str]
    """
            A list of authorizing paragraphs for the licenses being attached to WorkspaceObject
            objects. These are strings with a maximum of 80 bytes size. The size of eadParagraph
            vector should match the size of the selectedLicenses (each entry in eadParagraph
            maps to corresponding entry in selectedLicenses). If a paragraph entry is not applicable
            for a specific license (paragraph entries are applicable only for licenses of ITAR
            type), then that entry can be left blank. System will ignore any paragraph entry
            if it is not applicable for a license to be attached. This is an optional parameter.
            The eadParagraph is used for setting the ead_Paragraph attribute on WorkspaceObject.
            """
    PropertyName: str
    """
            The name of the property associated with the data it is either project_list
            or license_list.
            """

class ProjectsInput:
    """
    
            A structure contain logged in user info, selected input objects list, configuration
            context info and pagination info.
            
    """
    def __init__(self, ) -> None: ...
    User: Teamcenter.Soa.Client.Model.Strong.User
    """A user object, which is used to retrieve available projects to assign."""
    SelectedObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of Selected Input Objects."""
    AssignedObjects: list[Teamcenter.Soa.Client.Model.Strong.TC_Project]
    """A list of assigned objects from UI but not yet committed."""
    PaginationInfo: PaginationInfo
    """The pagination criteria."""
    FilterText: str
    """The filterText which should be applied for available projects to be returned."""
    IsAceContext: bool
    """If true, the user is in ActiveWorkspace Content context; otherwise, false."""

class ProjectsOutput:
    """
    A list of projectsOutput objects.
    """
    def __init__(self, ) -> None: ...
    AssignedProjectsList: list[Teamcenter.Soa.Client.Model.Strong.TC_Project]
    """A list of TC_Project objects which are assigned to the selected InputObject."""
    SelectedObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of selected input objects."""

class ProjectsOutputResponse:
    """
    
            This structure holds the information for all assigned projects to the input objects
            and all the available projects.
            
    """
    def __init__(self, ) -> None: ...
    ProjectOutput: ProjectsOutput
    """A list of projectsOutput objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the Service, plain objects, and error information. For this service, all objects
            are returned to the plain objects group. Error information will also be returned.
            """
    AvailableProjectList: list[Teamcenter.Soa.Client.Model.Strong.TC_Project]
    """A list of available TC_Project objects sorted in  alphabetical order."""
    ProjectOptions: System.Collections.Hashtable
    """
            A map(string, list of ConfigurationContextChoice) of ActiveWorkspace Content context
            attributes with the list of ActiveWorkspace Content context attributes possible values.
            """
    TotalFound: int
    """The total number of projects found."""
    TotalLoaded: int
    """The total number of projects loaded."""
    EndIndex: int
    """The end index to return the projects."""

class RevisionRuleEntryProps:
    """
    This contains information about the RevisionRule entry properties.
    """
    def __init__(self, ) -> None: ...
    UnitNo: int
    """The unit number of RevisionRule object."""
    Date: System.DateTime
    """The date of RevisionRule object."""
    Today: bool
    """Refers to a flag to indicate that the date is today on RevisionRule object."""
    EndItem: Teamcenter.Soa.Client.Model.Strong.Item
    """The  Item that indicates end item for RevisionRule object."""
    EndItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            The ItemRevision that indicates end item revision for RevisionRule
            object.
            """
    OverrideFolders: list[OverrideInfo]
    """A list of OverrideInfo struct."""

class RevisionRuleConfigInfo:
    """
    This contains the RevisionRule object and a RevisionRuleEntryProps  structure.
    """
    def __init__(self, ) -> None: ...
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """The RevisionRule object used for configuration of this BOMWindow object."""
    Props: RevisionRuleEntryProps
    """Refers to RevisionRuleEntryProps struct object."""

class ReconstructBOMWindowsInfo:
    """
    
            This contains the list of BOMWindow objects and the corresponding RevisionRule and
            VariantRule objects or StoredOptionSet object information.
            
    """
    def __init__(self, ) -> None: ...
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """Item object reference."""
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ItemRevision object reference."""
    BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView
    """PSBOMView object reference."""
    ObjectsForConfigure: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of variant rules or single stored option set object to set on this window."""
    RevRuleConfigInfo: RevisionRuleConfigInfo
    """Refers to a RevisionRuleConfigInfo struct object."""
    ActiveAssemblyArrangement: Teamcenter.Soa.Client.Model.Strong.AssemblyArrangement
    """Active assembly arrangement of this BOMWindow."""
    ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """ConfigurationContext object reference."""
    BomWinPropFlagMap: System.Collections.Hashtable
    """
            Mapping for window property and respective value that needs to be set on window.
            User need to populate this map with following property string values as key and true
            or false as value, which will be set or unset on the window. Valid property values
            are
            """

class PropagationDataInput:
    """
    
            Structure selected objects, configuration information which will be used for propagation
            and a structure of ReconstructBOMWindowInfo.
            
    """
    def __init__(self, ) -> None: ...
    AssignOrAttachData: list[ProjectOrLicenseDataInput]
    """
            A list of projects to be assigned to a given set of objects or list of licenses that
            needs to be attached to a given set of objects.
            """
    RemoveOrDetachData: list[ProjectOrLicenseDataInput]
    """
            A list containing license to be detached from a given set of objects or projects
            to be removed from a given set of objects.
            """
    PropertyDataToSetAndPropagate: list[PropertyChangeData]
    """A list of selected business object with property value to be removed or added."""
    ConfigInfo: PropagationConfigurationContext
    """The configuration information for propagation."""
    ReconstructConfigurationInfo: ReconstructBOMWindowsInfo
    """
            Information that will be used to reconstruct the given BOMWindow if the operation
            needs to be performed in a different process.
            """

class PropertyChangeData:
    """
    
            A Structure containing the name of property which needs to be modified, the new intended
            value after modification and set of selected objects.
            
    """
    def __init__(self, ) -> None: ...
    SelectedObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of selected objects for which the property needs to be changed."""
    PropertyName: str
    """The name of propagation enabled property for modification."""
    NewPropertyValues: list[str]
    """
            A list of values that are need to be set for the given property. This is the intended
            property values after the change.
            """

class ProjectLevelSecurity:
    """
    Interface ProjectLevelSecurity
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AssignOrRemoveObjectsFromProjects(self, AssignOrRemoveInput: list[ProjectAssignOrRemoveInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation assigns the given set of workspace objects to the given projects.
             Similarly, it removes an additional set of given workspace objects from the same
             set of given projects. If the input contains revision rule and or variant rule these
             will be applied to the given set of objects for traversing the structure i.e. the
             project will be propagated to the objects which are obtained by applying these configurations.
             If the additional input parameters type options and depth are specified; the assign
             or remove operation will filter out additional objects based on the inputs. If user
             is not privileged to assign objects to any of the given projects then this operation
             will return the error 101014 : You have insufficient privilege to assign object to
             a project. Similarly, if user is not privileged to remove objects from any of the
             given projects then this operation will return error 101015: You have insufficient
             privilege to remove object from a project. These errors will not terminate processing
             of rest of the objects.
             

Use Cases:


Assign projects to objects specified in an input by applying the
             given revision rules and variant rules for 4GD structures.
             
Assign project to objects specified in the input by applying the
             current BOM window in classic BOM
             
Assign projects to objects specified without applying any configuration
             information
             



Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param AssignOrRemoveInput: 
                         The list of ProjectAssignOrRemoveInput structure.
             
        :return: The service data will contain nothing in case the operation is to be processed asynchronously.
             This is controlled by one of the arguments in ProjectAssignOrRemoveInput input structure.
        """
        ...
    def CopyProjects2(self, CopyProjectInfos: list[CopyProjectsInfo2]) -> Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectOpsResponse:
        """    
             This operation copies the given list of TC_Project objects. The operation also copies
             any information which is in contained in the project. Data such as project team members
             and any objects assigned to the source project will also be copied to the new project.
             If a project with given project ID exists in the system then this operation will
             return error 101010. The operation will continue with copying the other projects.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param CopyProjectInfos: 
                         List of CopyProjectsInfo2 structure.
             
        :return: * 101026: The Project name is already exists. It must be unique within a site.
        """
        ...
    def CreateProjects2(self, ProjectInfos: list[ProjectInformation2]) -> Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectOpsResponse: ...
    def GetProjectsForAssignOrRemove(self, ProjectsInput: list[ProjectsInput]) -> ProjectsOutputResponse:
        """    
             This operation retrieves the assigned projects to the input data and all available
             projects where the input user is a priveleged member. When multiple business objects
             are selected this operation retrieves the assigned projects which are in common for
             the complete input data. It also retrieves level or structure information in case
             of ActiveWorkspace Content context. In ActiveWorkspace Content context, if the selected
             object does not have further child objects then level or structure information will
             not be returned.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param ProjectsInput: 
                         A list of ProjectsInput objects.
             
        :return: A list of assigned projects to the input data and all available projects where the
             input user is a priveleged member of. In the ProjectOutputsResponse, all the available
             TC_Project are returned in the availableProjects list and all the assigned projects
             to the input data are returned in the assignedProjects list, level or structure information
             in ActiveWorkspace Content context is returned in projectOptions Map.
        """
        ...
    def ModifyProjects2(self, ModifyProjectsInfos: list[ModifyProjectsInfo2]) -> Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectOpsResponse:
        """    
             This operation modifies the given list of TC_Project objects using the input specified.
             The input contains new values for all the project properties. Values for properties
             other than the project team are ignored unless the user is the Project Administrator.
             
             The entire Project Team, with the exception of the Project Administrator, is replaced
             with the specified team. Therefore, a Project Team Administrator must be specified.
             If the new Project Team is different than the current team, the user performing this
             operation must be either the Project Administrator or Project Team Administrator
             for the project being modified.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param ModifyProjectsInfos: 
                         List of ModifyProjectsInfo2 structures.
             
        :return: * 101026: The Project name is already exists. It must be unique within a site.
        """
        ...

