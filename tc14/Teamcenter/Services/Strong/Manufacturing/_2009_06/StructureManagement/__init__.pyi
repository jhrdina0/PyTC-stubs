import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateOrUpdateAttachmentsData:
    """
    Structure to specify input data for createOrUpdateAttachments
    """
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            bomline - the top line of the attachment window. Optional if attLine is going to
            be specified.
            """
    AttLine: Teamcenter.Soa.Client.Model.Strong.CfgAttachmentLine
    """
            Parent attachment line-under which the new one will be created or updated. Overrides
            bomLine member if specified.
            """
    Objects: System.Collections.Hashtable
    """relation string to the workspaceobject secondaries map"""

class GetAttachmentLineChildrenResponse:
    """
    response of getAttachmentLineChildren method - a map of input line to it's children
    """
    def __init__(self, ) -> None: ...
    Lines: System.Collections.Hashtable
    """map of parent attachmentline to child lines."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """any partial errors to be returned."""

class GetBOMLineActivitiesResponse:
    """
    
            Response of getBOMLineActivities method. lines represent the activities for supplied
            bomline. servicesData to capture partialErrors.
            
    """
    def __init__(self, ) -> None: ...
    Lines: System.Collections.Hashtable
    """vector of bomline to activities map"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData object to capture partial errors."""

class GetBOMLineAttachmentsResponse:
    """
    
            Response of getBOMLineAttachments method. lines represent the attachmentlines for
            supplied bomline. servicesData to capture partialErrors.
            
    """
    def __init__(self, ) -> None: ...
    Lines: System.Collections.Hashtable
    """bomline to attachmentlines map"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData to capture partial errors."""

class GetStructureContextActivityLinesResponse:
    """
    
            return structure of getStructureContextActivityLinesResponse. lines has the map of
            sc to activitylines, and serviceData has partial errors.
            
    """
    def __init__(self, ) -> None: ...
    Lines: System.Collections.Hashtable
    """map of sc to activity lines"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """for reporting partial errors."""

class GetStructureContextTopLinesResponse:
    """
    
            response of getStructureContextTopLines methods. lines member has the map of StructureContext
            to it's toplines, and serviceData member has any partial errors.
            
    """
    def __init__(self, ) -> None: ...
    Lines: System.Collections.Hashtable
    """map of SC to it's lines"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData to hold partial errors"""

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateAttachments(self, Attachments: list[CreateOrUpdateAttachmentsData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             create or update attachments. The following properties are loaded automatically for
             the line:me_cl_object_name,me_cl_object_type,me_cl_object_desc and these for the
             workspaceobject:object_name, object_type, object_desc irrespective of policy files.
             
        :param Attachments: 
                         input either bomline or attachmentline (parent) and the relations and workspace objects
                         to be processed as attachments.
             
        :return: failures returned as partial failures in serviceData
        """
        ...
    def DeleteAttachments(self, Lines: list[Teamcenter.Soa.Client.Model.Strong.CfgAttachmentLine]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             remove the specified attachment lines. Only if these lines have a parent is this
             action performed.
             
        :param Lines: 
                         remove the specified lines from the parent attachment window.
             
        :return: partial errors retuned in the serviceData
        """
        ...
    def GetAttachmentLineChildren(self, Attlines: list[Teamcenter.Soa.Client.Model.Strong.CfgAttachmentLine]) -> GetAttachmentLineChildrenResponse:
        """    
             given a vector of input attachmentlines - for each - get the immediate level of child
             attachment lines. For each attachment line the following properties are available
             on client side automatically:me_cl_object_name, me_cl_object_type, me_cl_object_desc
             
        :param Attlines: 
                         input parent attachment lines
             
        :return: returns the child attachment lines for a given line.
        """
        ...
    def CloseAttachmentWindow(self, Lines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             close any attachment window that got created for the bomline during the soa session.
             This will only close the attachment windows that are created to support the attachment
             line soa calls.
             
        :param Lines: 
                         input bomlines for which the attachmentwindow has to be closed.
             
        :return: any partial errors are returned in the response
        """
        ...
    def GetBOMLineActivities(self, BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> GetBOMLineActivitiesResponse:
        """    
             given a bomline get it's activities (these activities are really the children of
             the root activity associated with the bomline). This assumes that the bomline is
             a bopline. The following properties are available on client side for each line irrespective
             of policy: al_activity_object_name, al_activity_time. If the actual attachments of
             these activity lines are desired - use the getProperties method of DataManagementService
             with al_object as the property name.
             
        :param BomLines: 
                         input vector of bomlines for which activities are needed.
             
        :return: returns a vector of a map of bomline to it's activities.
        """
        ...
    def GetBOMLineAttachments(self, Bomlines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], Filter: list[str]) -> GetBOMLineAttachmentsResponse:
        """    
             given a bomline get it's attachments. The follow properties are available on client
             side irrespective of policy: me_cl_object_name, me_cl_object_type, me_cl_object_desc
             
        :param Bomlines: 
                         list of input BOMLines
             
        :param Filter: 
                         optional relation filter to be used for attachments. The relation names specified
                         here are used as a filter on the attachmentwindow
             
        :return: returns a  map of bomline to attachments
        """
        ...
    def GetStructureContextActivityLines(self, Scs: list[Teamcenter.Soa.Client.Model.Strong.StructureContext]) -> GetStructureContextActivityLinesResponse:
        """    
             Given a vector of StructureContext objects, for each - get the activitylines that
             are attached to the SC by the relation - TC_SC_activities. Currently, this is only
             created during a population of WorkInstruction page by selecting an activity. The
             following properties are available to the client irrespective of policy: al_activity_object_name,
             al_activity_time
             
        :param Scs: 
                         list of input structurecontext objects
             
        :return: lines has the map of sc to activitylines, and serviceData has partial errors.
        """
        ...
    def GetStructureContextTopLines(self, Scs: list[Teamcenter.Soa.Client.Model.Strong.StructureContext]) -> GetStructureContextTopLinesResponse:
        """    
             method to get the toplines of specified StructureContext. Client is responsible for
             closing any windows that are returned during this call. The following properties
             are available irrespective of policy:bl_line_name
             
        :param Scs: 
                         input list of SC's
             
        :return: returns the response structure containing the map of StructureContext to it's lines
             and the response.
        """
        ...

