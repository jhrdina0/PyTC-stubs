import Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateOrUpdateTemplateInputInfo1:
    """
    
            CreateOrUpdateTemplateInputInfo1 structure represents the parameters required to
            create a diagram template.
            
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
    HidePorts: bool
    """If true, the interface shapes will not be shown on the created diagram."""

class DiagramManagement:
    """
    Interface DiagramManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateTemplate(self, InputData: CreateOrUpdateTemplateInputInfo1) -> Fnd0.Services.Strong.Diagramming._2011_06.DiagramManagement.CreateOrUpdateTemplateResponse:
        """    
             This operation creates a Diagram Template which is used for creating diagrams for
             Teamcenter objects. A Diagram Template is nothing but a place holder for all the
             necessary information for creating a diagram. It holds the Application Domain which
             defines how Teamcenter objects will appear on the diagram, Transfer Mode used for
             traversing the given Teamcenter object, the Relation Rule used for finding out the
             relations between the objects to be shown on the diagram, the Stencil or Visio Template
             which has all the required shapes and the Property Map xml file which has the corresponding
             Teamcenter object mapping.  One can also specify if the interface shapes are to be
             hidden on the diagram created using this template. In such case, even if there are
             interface objects associated with the objects, they are not shown on the diagram.
             

Use Cases:

Use case 1:

             You can create a diagram template which will be used for creating diagrams. You can
             provide all the necessary information like the Application Domain, the Transfer mode,
             the Relation Rule, the Stencil/template and the property map file and chose if the
             interface shapes are not to be shown on the diagram. Once user opts to hide the shapes,
             it cannot be modified.
             

Use case 2:

             You can select an existing template and edit it. The Description, the Relation Rule
             can be modified.
             


Teamcenter Component:

             Diagram Management - Diagram Management
             
        :param InputData: 
                         holds the necessary information for creating a diagram template.
             
        :return: The created or updated Diagram Template revision object and the Service Data are
             returned. In case of any failures, ServiceData will return the error codes.
        """
        ...

