import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateDiagramInputInfo:
    """
    The parameters required to create a diagram.
    """
    def __init__(self, ) -> None: ...
    SelectedObject: Teamcenter.Soa.Client.Model.ModelObject
    """Teamcenter business object for which a Visio diagram will be created."""
    OpenDiagram: bool
    """If true, the created Visio diagram will be opened upon creation."""
    PropNamevsValueMap: System.Collections.Hashtable
    """
            A map of property names and values (string/string). Valid keys are Description,
            Name, templateName and ID.
            """

class CreateDiagramOutput:
    """
    
CreateDiagramOutput structure represents
            the output parameters as a result of creating a diagram.
            
    """
    def __init__(self, ) -> None: ...
    DiagramTmplFileTickets: list[str]
    """A list of FMS tickets to the diagram stencils files associated with the diagram template."""
    DiagMappingFileTicket: str
    """The FMS ticket to the diagram's property map file associated with the diagram template."""
    DiagramRev: Teamcenter.Soa.Client.Model.Strong.Fnd0DiagramRevision
    """The newly created Diagram Revision object."""
    DiagramMembers: list[DiagramMembers]
    """
            A list of diagram members, each element holds the primary object, the shape relation
            object, the persistent object, the type of the object and a Boolean to indicate if
            user has manually removed this object's shape from the diagram.
            """
    RelationsOnDiagram: list[RelationsOnDiagram]
    """
            A list of relations on the created diagram. Each element holds the relation object,
            the shape relation object, the primary and secondary objects of the relation, the
            type of the relation object and a Boolean to indicate if user has manually removed
            this object's shape from the diagram.
            """
    AppDomain: str
    """The Application Domain name of the diagram."""

class CreateDiagramResponse:
    """
    
CreateDiagramResponse structure represents
            the output of create diagram operation.
            
    """
    def __init__(self, ) -> None: ...
    CreateDiagOutput: list[CreateDiagramOutput]
    """A list of created diagrams"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class CreateOrUpdateTemplateInputInfo:
    """
    
            CreateOrUpdateTemplateInputInfo structure represents the parameters required to create
            a diagram template.
            
    """
    def __init__(self, ) -> None: ...
    Available: bool
    """If true, the Diagram Template is available for use."""
    TmplStencilFileTickets: list[str]
    """A list of FMS tickets to the Diagram tool specific stencils or Template files."""
    TmplMappingFileTicket: str
    """FMS ticket to the Property Map xml file."""
    MembershipRule: Teamcenter.Soa.Client.Model.Strong.TransferMode
    """
            The Transfer mode, which will be used for traversing the structure for the diagram
            root object.
            """
    RelationRule: list[str]
    """
            The Relation Rule which is the list of relations between the objects shown on the
            diagram.
            """
    DiagramTmplRev: Teamcenter.Soa.Client.Model.Strong.Fnd0DiagramTmplRevision
    """The updated template object."""
    PropNamevsPropValueMap: System.Collections.Hashtable
    """
            A map of property names and values (string/string). Valid keys are Description,
            Name, templateName and ID.
            """

class CreateOrUpdateTemplateOuput:
    """
    
CreateOrUpdateTemplateOuput structure represents
            the output parameters required for creating or updating a diagram template.
            
    """
    def __init__(self, ) -> None: ...
    DiagramTmplRev: Teamcenter.Soa.Client.Model.Strong.Fnd0DiagramTmplRevision
    """The created or updated  template object."""

class CreateOrUpdateTemplateResponse:
    """
    
CreateOrUpdateTemplateResponse structure
            represents the list of CreateOrUpdateTemplateOuput
            structures as a result of creating or updating a diagram template.
            
    """
    def __init__(self, ) -> None: ...
    Outputs: list[CreateOrUpdateTemplateOuput]
    """
            A list of CreateOrUpdateTemplateOuput structures, which hold the information of created
            templates.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """If true, the created Visio diagram will be opened on creation."""

class DiagramMembers:
    """
    
DiagramMembers structure holds the details
            of the members shown on the diagram.
            
    """
    def __init__(self, ) -> None: ...
    PrimaryObject: Teamcenter.Soa.Client.Model.ModelObject
    """The primary object of the shape shown on the diagram."""
    ShapeRelation: Teamcenter.Soa.Client.Model.Strong.Fnd0ShapeRelation
    """The relation object, which holds the shape information of Visio shape."""
    PersistentObject: Teamcenter.Soa.Client.Model.ModelObject
    """The persistent object of the primary object shown on the diagram."""
    ObjectTCTypeName: str
    """The TC type name of the object."""
    IsMemberOmitted: bool
    """
            If true, indicates that the shape was removed from the diagram by the user. Such
            shapes can be restored.
            """

class GetDiagramMembersInputInfo:
    """
    
GetDiagramMembersInputInfo structure represents
            the parameters required to get specific types of members from the diagram.
            
    """
    def __init__(self, ) -> None: ...
    MembershipType: int
    """The membership type."""
    DiagramRevision: Teamcenter.Soa.Client.Model.Strong.Fnd0DiagramRevision
    """The Diagram Revision object."""
    SelectedObject: Teamcenter.Soa.Client.Model.ModelObject
    """The Diagram Root object."""

class GetDiagramMembersOutput:
    """
    
GetDiagramMembersOutput structure represents
            the output parameters.
            
    """
    def __init__(self, ) -> None: ...
    DiagramMembers: list[DiagramMembers]
    """
            A list of structure which holds the primary object, the shape relation object, the
            persistent object, the type of the object and a Boolean to indicate if user has manually
            removed this object's shape from the diagram.
            """
    RelationsOnDiagram: list[RelationsOnDiagram]
    """
            A list of structure which holds the relation object, the shape relation object, the
            primary and secondary objects of the relation, the type of the relation object and
            a Boolean to indicate if user has manually removed this object's shape from the diagram.
            """

class GetDiagramMembersResponse:
    """
    
GetDiagramMembersResponse structure represents
            the output of the get diagram members operation.
            
    """
    def __init__(self, ) -> None: ...
    Outputs: list[GetDiagramMembersOutput]
    """A list of GetDiagramMembersOutput structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData"""

class OpenDiagramInputInfo:
    """
    
OpenDiagramInputInfo structure represents
            the parameters required to open a diagram.
            
    """
    def __init__(self, ) -> None: ...
    SelectedObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The Teamcenter object for which a Visio diagram will be created, either a Workspace
            object or a BOM Line.
            """
    DiagramRevision: Teamcenter.Soa.Client.Model.Strong.Fnd0DiagramRevision
    """The Diagram revision object."""

class OpenDiagramOutput:
    """
    OpenDiagramOutput structure represents the parameters as a result of opening a diagram.
    """
    def __init__(self, ) -> None: ...
    DiagramTmplFileTickets: list[str]
    """A list of FMS tickets to the diagram stencils files associated with the diagram template."""
    DiagMappingFileTicket: str
    """FMS ticket to the diagram's property map file associated with the diagram template."""
    DiagramFileTicket: str
    """FMS ticket to the diagram's vdx file which is stored in the transient volume."""
    DiagramMembers: list[DiagramMembers]
    """
            A list of structure which holds the primary object, the shape relation object, the
            persistent object, the type of the object and a Boolean to indicate if user has manually
            removed this object's shape from the diagram.
            """
    RelationsOnDiagram: list[RelationsOnDiagram]
    """
            A list of structure which holds the relation object, the shape relation object, the
            primary and secondary objects of the relation, the type of the relation object and
            a Boolean to indicate if user has manually removed this object's shape from the diagram.
            """
    ObjectUIDvsShapeID: System.Collections.Hashtable
    """
            The map of the UIDs of all the objects and the Visio unique ids of their corresponding
            shapes (string/string).
            """
    AppDomain: str
    """The Application Domain name of the diagram."""
    StartObject: Teamcenter.Soa.Client.Model.ModelObject
    """The root object of the diagram."""

class OpenDiagramResponse:
    """
    
OpenDiagramResponse structure represents
            the output of the open diagram operation.
            
    """
    def __init__(self, ) -> None: ...
    OpenDiagOutput: list[OpenDiagramOutput]
    """A list of OpenDiagramOutput structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class RelationsOnDiagram:
    """
    
RelationsOnDiagram structure holds the details
            of the relations shown on the diagram.
            
    """
    def __init__(self, ) -> None: ...
    Relation: Teamcenter.Soa.Client.Model.Strong.ImanRelation
    """The relation object to be shown on the diagram."""
    ShapeRelation: Teamcenter.Soa.Client.Model.Strong.Fnd0ShapeRelation
    """The relation object, which holds the shape information of Visio shape."""
    PrimaryObject: Teamcenter.Soa.Client.Model.ModelObject
    """The primary object of the relation, required to show the relation between the members."""
    SecondaryObject: Teamcenter.Soa.Client.Model.ModelObject
    """The secondary object of the relation, required to show the relation between the members."""
    RelationType: str
    """The TC type name of the relation object."""
    IsRelationMemberOmitted: bool
    """
            If true, indicates that the relation shape was removed from the diagram by the user.
            Such shapes can be restored.
            """

class SaveDiagramInputInfo:
    """
    
SaveDiagramInputInfo structure represents
            the parameters required to save a diagram.
            
    """
    def __init__(self, ) -> None: ...
    DiagFileTicket: str
    """FMS ticket to the diagram's .vdx file to be saved."""
    DiagImageFileTicket: str
    """FMS ticket to the diagram's preview image to be saved."""
    DiagramRevision: Teamcenter.Soa.Client.Model.Strong.Fnd0DiagramRevision
    """The diagram revision object."""
    SelectedObject: Teamcenter.Soa.Client.Model.ModelObject
    """The Teamcenter business object."""

class SaveDiagramOutput:
    """
    
SaveDiagramOutput structure represents the
            output parameters as a result of saving a diagram.
            
    """
    def __init__(self, ) -> None: ...
    ResultObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of Teamcenter objects, which appear on the diagram, for which shape relations
            are created during the saving of the diagram.
            """

class SaveDiagramResponse:
    """
    
SaveDiagramResponse structure represents
            the output of the save diagram operation.
            
    """
    def __init__(self, ) -> None: ...
    SaveDiagOutput: list[SaveDiagramOutput]
    """A list of SaveDiagramOutput structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class DiagramManagement:
    """
    Interface DiagramManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateDiagram(self, InputData: list[CreateDiagramInputInfo]) -> CreateDiagramResponse:
        """    
             This operation creates a Visio Diagram for a Teamcenter object (WorkspaceObject/
             ItemRevision/ Folder/ BOMLine) using a Diagram Template. The objects and relations
             shown on the diagram are gathered by executing the Transfer Mode and Relation Rule
             specified on the diagram template. Relation Rule specifies the relations to be shown
             between the objects.
             
             Only those objects appear on the diagram for which there is a Visio Shape in the
             stencil and there is mapping defined between the Shape and the Teamcenter object
             in the mapping xml file. Mapping file has details about how to define the mappings.
             
             While creating a diagram, if user selects the "Open Diagram" option, the diagram
             object is created on the server and all the necessary information is returned in
             the response which is utilized to open the Visio diagram. If user does not select
             the option, then just the diagram object is created.
             


Use Cases:

             You can select a Teamcenter object in RAC and create a Visio diagram for the same
             by selecting a Diagram Domain and a Diagram Template.
             

Dependencies:

             createOrUpdateTemplate, createOrUpdateTemplate
             

Teamcenter Component:

             Diagram Management - Diagram Management
             
        :param InputData: 
                         The required information to create a diagram for the selected object.
             
        :return: The created diagram objects are returned along with the Service data elements. If
             there are any issues while creating a diagram, error code 267012 is returned.
        """
        ...
    def CreateOrUpdateTemplate(self, InputData: CreateOrUpdateTemplateInputInfo) -> CreateOrUpdateTemplateResponse:
        """    
             createOrUpdateTemplate provides the ability to either create a new diagram template
             or modify an existing diagram template.
             

Teamcenter Component:

             Diagram Management - Diagram Management
             
        :param InputData: 
                         Input Information for createOrUpdateTemplate
             
        :return: CreateOrUpdateTemplateResponse that contains the diagram template revision object.
        """
        ...
    def GetDiagramMembers(self, InputData: list[GetDiagramMembersInputInfo]) -> GetDiagramMembersResponse:
        """    
             This operation retrieves the specific types of members of the diagram based on its
             membership types. Following are the types of members apart from the ones that appear
             on the diagram as a result of transfer mode traversal and relationship rules.
             

User Added - The objects which are added to the diagram by the user.
             E.g. an Item object which is copied from Teamcenter and then pasted on to the diagram.
             
User Omitted - The objects which are deleted by the user from the
             diagram. E.g. user can remove an object from the diagram only. The object is removed
             from the diagram and not from database. It can be retrieved and again shown on the
             diagram.
             



Use Cases:

             None.
             

Teamcenter Component:

             Diagram Management - Diagram Management
             
        :param InputData: 
                         holds the required information to get the specific types of diagram members.
             
        :return: is returned.
        """
        ...
    def OpenDiagram(self, InputData: list[OpenDiagramInputInfo]) -> OpenDiagramResponse:
        """    
             This operation opens a Visio Diagram created for a Teamcenter object (WorkspaceObject/
             Item Revision/ Folder/ BOMLine). The objects and relations shown on the diagram
             are gathered by executing the Transfer Mode and Relation Rule specified on the diagram
             template. Relation Rule specifies the relations to be shown between the objects.
             
             Only those objects appear on the diagram for which there is a Visio Shape in the
             stencil and there is mapping defined between the Shape and the Teamcenter object
             in the mapping xml file. Mapping file has details about how to define the mappings.
             
             If the contents of the root object of the diagram are changed, for instance, a BOM
             structure changes or the contents of the folder are modified, then the diagram will
             show only the current information. This is because every time a diagram is opened,
             Transfer mode and Relation Rules are applied.
             

Use Cases:

             You can select a Teamcenter object and launch the open diagram dialog which shows
             the list of all diagrams created for that object. You can select a diagram to open.
             A Visio diagram is opened on the RAC. The content of the diagram is decided by the
             Transfer mode and the Relation Rule.
             

Dependencies:

             saveDiagram
             

Teamcenter Component:

             Diagram Management - Diagram Management
             
        :param InputData: 
                         holds the required information to open a diagram for the selected object.
             
        :return: will return
             the error codes.
        """
        ...
    def SaveDiagram(self, InputData: list[SaveDiagramInputInfo]) -> SaveDiagramResponse:
        """    
             This operation saves Visio Diagram(s) created for a Teamcenter object (WorkspaceObject/
             Item Revision/ Folder/ BOMLine). When a Visio diagram is saved, a skeleton file
             (.vdx) is created and stored as a dataset to hold all the non Teamcenter information,
             like notes if any. A preview image of the diagram content is also stored as an image
             data set. These Dataset objects are attached to the diagram object.
             
             For the Teamcenter business objects appearing on the diagram, Fnd0ShapeRelation
             objects are created with the diagram object to hold the position information so that
             the shapes appear in their original position and format next time the diagram is
             opened.
             

Use Cases:

             You can create or open an existing diagram and make changes to it. You can then save
             the diagram.
             

Dependencies:

             createDiagram, openDiagram
             

Teamcenter Component:

             Diagram Management - Diagram Management
             
        :param InputData: 
                         holds the information to save a diagram created for a Teamcenter business object.
             
        :return: if the saving
             the diagram fails.
        """
        ...

