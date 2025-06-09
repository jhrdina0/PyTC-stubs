import Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetContentInput1:
    """
    
GetContentInput1 structure represents the
            parameters required to open requirement in MSWord.
    """
    def __init__(self, ) -> None: ...
    ObjectToProcess: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """Fulltext object that user want to view."""
    ApplicationFormat: str
    """
            For viewing and editing content without template this parameter should be MSWordXML.
            
            For viewing and editing object by applying template this parameter should be MSWordXMLLive.
            

"""
    TemplateId: str
    """This parameter is not used currently."""
    ApplyTemplates: bool
    """
            For viewing and editing content without template this parameter should be false.
            
            For viewing and editing object by applying template this parameter should be true.
            """

class RequirementsManagement:
    """
    Interface RequirementsManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetRichContent(self, Inputs: list[GetContentInput1]) -> Teamcenter.Services.Strong.Requirementsmanagement._2007_01.RequirementsManagement.GetRichContentResponse:
        """    
             The SOA operation is responsible for retrieving contents of objects of type SpecElement.
             It can be used to view content of SpecElement in word. SOA also provides capability
             to view contents by applying default templates.
             

Use Cases:

             User can open requirements in word using default templates or they can open content
             (body text) in word for view and edit purpose.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Inputs: 
                         A list of structures containing the required information to open requirement content
                         in word.
             
        :return: A vector of transientFileReadTickets containing the document having rich text is
             returned to the user.
        """
        ...

