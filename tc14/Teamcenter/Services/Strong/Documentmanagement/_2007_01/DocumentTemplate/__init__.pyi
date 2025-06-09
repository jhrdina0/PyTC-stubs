import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FileTicket:
    """
    The FileTicket struct.
    """
    def __init__(self, ) -> None: ...
    FileName: str
    """The file name."""
    Ticket: str
    """The FMS download ticket."""

class GetTemplateInput:
    """
    
            This structure defines the list of search criteria used to find the appropriate DMTemplates
            for the calling application.
            
    """
    def __init__(self, ) -> None: ...
    Application: str
    """The name of the calling application."""
    Version: str
    """The version of the application. Optional."""
    TemplateType: str
    """An application defined type value for different templates."""
    TemplateUnits: str
    """The measurement units that the application uses."""
    CreateItemType: str
    """The item Type to be created using the template files."""
    NameReferenceName: str
    """The named reference name for the thumbnail file."""
    Relation: str
    """The relation to the thumbnail dataset."""

class GetTemplateOutput:
    """
    The GetTemplateOutput struct.
    """
    def __init__(self, ) -> None: ...
    TemplateRev: Teamcenter.Soa.Client.Model.ModelObject
    """The document template revision."""
    TemplateName: str
    """The document template name."""
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """The thumbnail dataset associated with the template."""
    FileTicket: FileTicket
    """The file ticket for the FMS download of the thumbnail file."""

class GetTemplatesResponse:
    """
    The GetTemplateOutput struct.
    """
    def __init__(self, ) -> None: ...
    Output: list[GetTemplateOutput]
    """The list of references to struct GetTemplateOutput."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The Service Data. Partial errors and failures are updated and returned through this
            object.
            """

class DocumentTemplate:
    """
    Interface DocumentTemplate
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetTemplates(self, Input: GetTemplateInput) -> GetTemplatesResponse:
        """    
             This operation is intended to support applications with a Microsoft Office style
             template system, where the user chooses to create a new document, and the application
             presents the user with a selection of different templates to use to create the document.
             The calling application inputs its search criteria, and getTemplates returns the
             list of DMTemplate objects that match the criteria. The DMTemplate is a business
             object that is used to control the template files provided during Create.
             

             The search criteria are:
             

The name of the calling application. DMTemplate objects are application
             specific.
             
The version number of the calling application. Optional.
             
The desired measurement type; e.g. inches or metric. Used for CAD
             applications.
             
The type of Item that will be created using the DMTemplate file.
             
An application defined type value.
             



             The operation returns a list of DMTemplate names and thumbnail images that can be
             used by the application to present a choice to the user. Once the user selects a
             DMTemplate to use in the creation of the new object, the application can get the
             files for the selected DMTemplate using the expandPrimaryObjects operation.
             

Use Cases:

Get a list of templates for creating a new object.


             The user decides to create a new ItemRevision in a CAD application. The application
             calls this operation and receives a list of template names and thumbnails to display
             to the user. The user selects a template and the application retrieves the template
             files using the expandPrimaryObjects operation. The application then creates the
             new ItemRevision and attaches copies of the template files.
             

Dependencies:

             expandPrimaryObjects
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param Input: 
                         The search parameters for the application specific DMTemplate objects.
             
        :return: 
        """
        ...

