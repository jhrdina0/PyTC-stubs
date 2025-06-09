import Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class MDOInitialNotification:
    """
    Trigger MDO notification information and its responses.
    """
    def __init__(self, ) -> None: ...
    NotificationObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """The actual Mdo0Notification object which is queried."""
    NotificationQualifier: str
    """
            The action that is performed on a ModelElement.The supported qualifiers are: create,
            replace, revise, remove.
"""
    DesignInstance: Teamcenter.Soa.Client.Model.Strong.POM_object
    """The design instance [Mdl0ModelElement] for which the notification is generated."""
    AcceptedResponses: list[MDONotificationDetails]
    """
            The list of MDO notifications [MDONotificationDetails] generated when impacted designs
            reacted to a trigger notification.
            """
    RejectedResponses: list[MDONotificationDetails]
    """
            The list of MDO notifications [MDONotificationDetails] generated when impacted designs
            rejects to a trigger notification
            """
    IgnoredResponses: list[MDONotificationDetails]
    """
            The list of MDO notifications [MDONotificationDetails] generated when impacted designs
            ignores / or has no impact to a trigger notification.
            """

class CreateNotificationOutput:
    """
    The searched create related MDO notifications are returned.
    """
    def __init__(self, ) -> None: ...
    CreateTriggerNotification: MDOInitialNotification
    """The trigger create related notification [MDOInitialNotification]."""
    InstanceThread: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
Mdo0MDInstance object to which the design instance for which the notification
            is generated is linked to.
            """
    LinkedInstances: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            The impacted design instances of the design instance for which the notification is
            generated.
            """
    MdoOutput: list[MDOOutput2]
    """
            List of Mdo0MDThread found for design instance of trigger notification. All
            the associated design artifacts will be part of MDOOutput2. The design artifacts
            will be of type WorkspaceObject.
            """

class DateInput:
    """
    Input date criteria to be used to filter queried initial trigger MDO notifications.
    """
    def __init__(self, ) -> None: ...
    FromDate: System.DateTime
    """
            From date input, any trigger MDO notification generated  from this date will be returned
            to user.
            """
    ToDate: System.DateTime
    """
            From date input, any trigger MDO notification generated till this date will be returned
            to user.
            """

class DesignArtifactInfo:
    """
    
            The design artifacts associated to MDThread object along with domain information
            will be returned.
            
    """
    def __init__(self, ) -> None: ...
    DesignArtifact: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The design artifact of an MDThread. The design artifacts will be of type WorkspaceObject."""
    Domain: str
    """The domain information of design artifact."""

class FilterForSearch:
    """
    Filter criteria for design artifacts.
    """
    def __init__(self, ) -> None: ...
    TypeObj: Teamcenter.Soa.Client.Model.Strong.ImanType
    """ImanType object  which is to be validated for compatible design artifacts."""
    AttributeValues: System.Collections.Hashtable
    """
            A map of attribute names and  values (string/string)to be used for filtering the
            compatible design artifacts.
            """
    Domain: str
    """Domain information which is to be validated for compatible design artifacts."""

class MDONotificationDetails:
    """
    Details about a generated MDO notification.
    """
    def __init__(self, ) -> None: ...
    NotificationQualifier: str
    """
            The action that is performed on a ModelElement.The supported qualifiers are: create,
            replace, revise, remove.
"""
    TriggeringComponent: Teamcenter.Soa.Client.Model.Strong.POM_object
    """Design instance for which the notification is generated."""
    Model: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            Parent design which can be an Mdl0ApplicationModel or parent BOMViewRevision
            [for future] object.
            """
    ObjectName: str
    """
            Object name of the design instance for which notification is generated. Used only
            for remove related MDO notification.
            """

class MDONotificationReactionData:
    """
    
            The design instance which is reacted to the trigger MDO notification and the action
            performed on the design instance.
            
    """
    def __init__(self, ) -> None: ...
    NotificationQualifier: str
    """
            The action that is performed on a ModelElement. For e.g.: create, replace, revise,
            remove, etc.
            """
    ReactedObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            The impacted design instance [Mdl0ModelElement] of the trigger MDO notification
            on which on relevant changes are made.
            """
    ObjectName: str
    """
            Object name of the design instance for which notification is generated. Used only
            for remove related MDO notification.
            """

class MDONotificationUpdateData:
    """
    Details about a reacted  MDO notification and what design changes are made.
    """
    def __init__(self, ) -> None: ...
    NotificationObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """The trigger Mdo0Notification for which the user wants to update the responses."""
    NotificationQualifier: str
    """
            The action that is performed on a ModelElement. Of trigger Mdo0Notification
            For e.g.: create, replace, revise, remove, etc.
            """
    ReactedResponses: list[MDONotificationReactionData]
    """List of objects the user has made relevant changes when reacted to a trigger notification."""
    IgnoreNotification: bool
    """
            If true, the user has no impact or ignoring a trigger notification and not making
            any changes in the impacted design instances.
            """

class MDONotificationUpdateInput:
    """
    Input structure for UpdateMDONotification operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    NotificationUpdateData: MDONotificationUpdateData
    """
            Input data about which Mdo0Notification the user has reacted and how the user
            has reacted.
            """

class MDOOutput2:
    """
    
            The searched MDThread object will be returned. Also all the associated design
            artifacts for the MDThread will be returned
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    MdoObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The created MDThread object or updated MDThread object."""
    AssociatedDesignArtifact: list[DesignArtifactInfo]
    """
            Design artifact information associated to the MDThread. The design artifacts
            will be of type WorkspaceObject.
            """

class MDOSearchOutput2:
    """
    
            The search results for each input are returned. For each input there can be a one
            or more of MDThread objects found.
            
    """
    def __init__(self, ) -> None: ...
    MdoOutput: list[MDOOutput2]
    """
            List of MDThread found for each search input. All the associated design artifacts
            will be part of MDOOutput2. The design artifacts will be of type WorkspaceObject.
            """

class ModifyNotificationOutput:
    """
    The searched modify related MDO notifications are returned.
    """
    def __init__(self, ) -> None: ...
    ModifyTriggerNotifications: list[MDOInitialNotification]
    """The trigger modify related notification [MDOInitialNotification]."""
    InstanceThread: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
Mdo0MDInstance object to which the design instance for which the notification
            is generated is linked to.
            """
    LinkedInstances: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            The impacted design instances of the design instance for which the notification is
            generated.
            """

class NotificationQueryInput:
    """
    Input structure for qryNotificationsByOriginDesign operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    DesignInstance: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            Input design instance for which all  the modify related Mdo0Notification has
            to be queried for MDinstance the design instance is part of.
            """
    ProjectContext: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            Input context for which all the modify related Mdo0Notification has to be
            queried.  For create related Mdo0Notification, notification will be filtered
            based on this input.
            """
    PerformCreateNotificationQueryAlso: bool
    """Input flag to query for create related Mdo0Notification."""
    FilterCompatibleArtifactByType: Teamcenter.Soa.Client.Model.Strong.ImanType
    """
            Input ImanType object to be used to filter compatible design artifacts of
            Mdo0MDThread while processing create related notification.
            """
    FilterModifyTriggerNotificationByType: Teamcenter.Soa.Client.Model.Strong.ImanType
    FilterByDesign: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            Input design object which is used to filter trigger Mdo0Notification object
            generated.
            """
    FilterByDomain: str
    """
            Input domain information which is used to filter the recommended design artifact
            of MDThread for create notification.
            """

class QryInputByDesignOrProject:
    """
    
            Input structure for qryNotificationsByDesignOrProject operation.
            
            TODO add dateCriteria
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    InputDesign: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            Input design object Mdl0ModelElement for which the initial trigger MDO notification
            has to be queried.
            """
    Project: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            Input project object TC_Project for which the initial trigger MDO notification
            has to be queried for all designs in the project.
            """
    DateCriteria: DateInput
    """
            Input date criteria. Trigger MDO notification generated for the specified date criteria
            will be filtered and returned to user.
            """

class QryNotificationByDesignResponse:
    """
    The searched trigger MDO notificationsfor the input design or project are returned.
    """
    def __init__(self, ) -> None: ...
    Output: list[QryOutputByDesignOrProject]
    """List of trigger MDO notification searched for the input design or project."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation."""

class QryNotificationOutputByDesign:
    """
    The searched trigger MDO notifications are returned.
    """
    def __init__(self, ) -> None: ...
    NotificationByDesignOutputs: list[MDOInitialNotification]
    """List of trigger MDO notifications generated for a design."""
    DesignObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """The design object for which the trigger MDO notifications are generated and queried."""

class QryOutputByDesignOrProject:
    """
    
            The searched create and modify related trigger MDO notifications for a design are
            returned.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    NotificationOutputs: list[QryNotificationOutputByDesign]
    """List of trigger MDO notification generated for a design or for all designs in a project."""

class QueryNotificationOutput:
    """
    The searched create and modify related MDO notifications are returned.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    CreateNotificationOutputs: list[CreateNotificationOutput]
    """List of create related MDO notification searched for the input."""
    ModifyNotificationOutputs: list[ModifyNotificationOutput]
    """List of modify related MDO notification searched for the input."""

class QueryNotificationResponse:
    """
    The searched MDO notifications for the input are returned.
    """
    def __init__(self, ) -> None: ...
    Output: list[QueryNotificationOutput]
    """List of MDO notification searched for the input."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation."""

class SearchForDesignArtifactInput2:
    """
    Input structure for searchForArtifactsUsingInstances2 operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the input, optional."""
    DesignInstances: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            List of Design instances (Mdl0ModelElement) for which compatible design instances
            are to be searched.
            """
    FilterByDomain: str
    """Domain information which is to be validated for compatible design artifacts."""

class SearchInput2:
    """
    Input structure for searchMDO2 operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    MdoCriteria: System.Collections.Hashtable
    """Input search criteria for MDThread object."""
    DesignArtifactInputs: Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.DesignArtifactInputsForSearch
    """
            Search input for design artifacts . This input is used for search of MDThread
            for single design artifact or combination of design artifacts. If more than one design
            artifact object is given as input, the search will return all the MDThread
            which has this set of design artifact associated with it. If design artifact criteria
            are provided, the MDThread search uses the design artifact criteria and MdThread
            criteria.
            """
    FilterCriteria: FilterForSearch
    """
            The criteria to be applied on compatible design artifacts of MDThread. Only
            compatible design artifacts satisfying the filter criteria will be returned as part
            of search output.
            """

class SearchMDO2Response:
    """
    
            The searched MDThread objects will be returned. Also all the associated design
            artifacts for the MDThread will be returned.
            
    """
    def __init__(self, ) -> None: ...
    MdoSearchOutput: MDOSearchOutput2
    """Search result for each search input."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation."""

class UpdateMDONotificationOutput:
    """
    The updated MDO notification and its Mdo0MDInstance are returned.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    NotificationObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """The trigger Mdo0Notification object which is updated."""
    InstanceThread: Teamcenter.Soa.Client.Model.Strong.POM_object

class UpdateMDONotificationResponse:
    """
    The updated MDO notifications for the input are returned.
    """
    def __init__(self, ) -> None: ...
    Output: list[UpdateMDONotificationOutput]
    """List of MDO notification updated for the input."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds any partial errors occurred during the operation."""

class MultiDisciplinaryDataMgt:
    """
    Interface MultiDisciplinaryDataMgt
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def QryNotificationsByDesignOrProject(self, Inputs: list[QryInputByDesignOrProject]) -> QryNotificationByDesignResponse:
        """    
             This operation queries for all create and modify MDO notifications for a design or
             for all designs in a project and ordered by date and grouped by design. This helps
             the users to know the sequence of action happened in a design or project. Date criteria
             can be provided as input to know the sequence of operation happened in a design between
             specific times.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Search criteria for <b>Mdo0Notification</b> object for create and modify notifications
                         for a design or project along with date criteria.
             
        :return: 
        """
        ...
    def QryNotificationsByImpactedDesign(self, Inputs: list[NotificationQueryInput]) -> QueryNotificationResponse: ...
    def QryNotificationsByOriginDesign(self, Inputs: list[NotificationQueryInput]) -> QueryNotificationResponse: ...
    def SearchForArtifactsUsingInstances2(self, Inputs: list[SearchForDesignArtifactInput2]) -> SearchMDO2Response: ...
    def SearchMDO2(self, SearchInputs2: list[SearchInput2]) -> SearchMDO2Response: ...
    def UpdateMDONotification(self, Inputs: list[MDONotificationUpdateInput]) -> UpdateMDONotificationResponse:
        """    
             This operation groups the create MDO notifications or modify MDO notifications based
             on the response from user. This operation is expected to be called by the designer
             to update the notification system, after the users reacts to a trigger notification
             either by ignoring the notification or performing a change to his design.
             

Use Cases:

             Compatible design artifacts are associated to MDThread using createOrUpdateMDO SOA
             operation.
             
             Design artifacts of MDThread are consumed in design.
             
             Impacted design instances of design are linked together using linkDesignInstances
             SOA operation.
             
             Design instances are modified [replace/revise/remove etc] in the design.
             
             MDO notification for design instance creation can be searched with filter criteria.
             
             MDO notification for modification can be search using design instance with filter
             criteria.
             
             User working on multi- discipline will make respective change in their design based
             on queried MDO notification
             
             User after reacting to a notification will update the MDO notification system with
             details about what relevant changes are made in impacted design. If a designer reacts
             to a MDO notification, the user will update the system by providing information about
             how the user has reacted and the original notification object for which the user
             reacted. The system will identify the MDO notification and process that and creates
             an accepted response for it and set it on original trigger MDO notification.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Input criteria for updating a <b>Mdo0Notification</b> object for create and modify
                         notifications for responses.
             
        :return: 
        """
        ...

