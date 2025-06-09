import System
import Teamcenter.Soa.Client.Model
import typing

class ContainsRenderableFilesResponse:
    """
    
            Contains Renderable Files Response structure consisting of a list of renderable files
            and the service data.
            
    """
    def __init__(self, ) -> None: ...
    ObjectsWithRenderableFiles: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of objects (from selectedObjects)
            that contain renderable files.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard return; includes any error information."""

class PrintOrRender:
    """
    Interface PrintOrRender
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ContainsRenderableFiles(self, SelectedObjects: list[Teamcenter.Soa.Client.Model.ModelObject], RenderFormat: str) -> ContainsRenderableFilesResponse:
        """    
             Checks to see if selectedObjects contains
             any files that can be rendered to the renderFormat
             using the Dispatcher Render Management translator.
             

Use Cases:

             This operation is intended to be called to determine the visibility of commands such
             as the "Generate PDF" one-step command.
             

             Generate PDF (one-step command): The user selects one or more Dataset or ItemRevision
             (or sub-type) objects in Active Workspace.  The containsRenderableFiles
             operation is called by the Active Workspace client framework to determine if there
             are any files within selectedObjects that
             can be rendered to pdf.  If any renderable files are found, then the "Generate PDF"
             command becomes visible.  If no renderable files are found, then the "Generate PDF"
             command remains hidden.
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param SelectedObjects: 
                         The list of objects selected by the user. Valid selected objects include <b>Dataset</b>
                         and <b>ItemRevision</b> (or sub-type) objects.
             
        :param RenderFormat: 
                         The render file format. The value may be any output file format supported by Teamcenter
                         Visualization Convert and Print (VVCP), such as <i>pdf</i> or <i>tif</i>.
             
        :return: 259010: <render format> is not a supported render format.
        """
        ...
    def RenderFilesSubmitRequest(self, SelectedObjects: list[Teamcenter.Soa.Client.Model.ModelObject], RenderFormat: str, SaveRenderedFiles: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Submits a Render Management Dispatcher request to render the files within the selected
             objects to the specified file format without requiring any Item Revision Document
             Control (IRDC) forms to be defined in Business Modeler Integrated Development Environment
             (BMIDE).
             

Use Cases:

             Generate PDF:
             
             The user selects one or more Dataset or ItemRevision (or sub-type)
             objects in Active Workspace.  The containsRenderableFiles
             operation is called to determine if there are any files in the selected objects that
             can be rendered to pdf.  If any renderable files are found, the "Generate PDF" one-step
             command becomes visible.  If the user clicks on the "Generate PDF" command, the renderFilesSubmitRequest operation is called to
             submit a Render Management Dispatcher request to render the valid files within the
             selected objects to pdf.  When the files have been rendered, an alert notification
             will be sent to inform the user that the rendering is complete.
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param SelectedObjects: 
                         The list of objects selected by the user. Valid selected objects include <b>Dataset</b>
                         and <b>ItemRevision</b> (or sub-type) objects.
             
        :param RenderFormat: 
                         The render file format. The value may be any output file format supported by Teamcenter
                         Visualization Convert and Print (VVCP), such as <i>pdf</i> or <i>tif</i>.
             
        :param SaveRenderedFiles: 
                         Specifies if the rendered files should be saved in <b>Dataset</b> objects.
             
        :return: <Business Object name> cannot be updated
             for released <Business Object type> <Business Object name>.
        """
        ...

