import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AdditionalProperties:
    """
    
The structure containing information of additional properties.

Valid properties are:

email_subject: Subject of email address which needed to be sent.

email_message: Text of email address which needed to be sent.

email_recipients: External email address who also needs to be notified.

condition: Additional rule condition like how many days before user should be
notified.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of additional property."""
    Values: list[str]
    """A list of values for the property."""

class BaselineTaskInfo:
    """
    Contains information about the baselineTask.
    """
    def __init__(self, ) -> None: ...
    BaselineTask: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The baseline ScheduleTask object."""
    Properties: System.Collections.Hashtable
    """Map (string, string) of baseline task property names and their values."""

class LoadBaselineResponse:
    """
    
Response of the load baseline operation, containing information about the loaded
baseline tasks.
    """
    def __init__(self, ) -> None: ...
    BaselineTasksInfo: System.Collections.Hashtable
    """
            Map (string, BaselineTaskInfo) of original ScheduleTask UID and its baseline task
            information.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData."""

class LoadBaselinesInfo:
    """
    
Information required to load the baseline tasks of a Schedule baseline based on
a
source Schedule and load options
    """
    def __init__(self, ) -> None: ...
    SourceSchedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The Schedule for which the baseline needs to be loaded."""
    BaselineSchedules: list[Teamcenter.Soa.Client.Model.Strong.Schedule]
    """A list of baseline Schedule objects to load."""
    ScheduleTasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    """
            A list of ScheduleTask objects, in the source Schedule, for which the
            respective baseline tasks are to be returned.
            """
    LoadOptions: System.Collections.Hashtable
    """
            A map (string, string) of options for loading Schedule Baseline. Valid options (key
            : value) are:
            
            loadBaselineTasks : true/false (Set true to return the baseline tasks; false otherwise)
            
            loadCompleteBaseline : true/false (Set true to return information of all the baseline
            tasks in the schedule baseline; Set false or do not specify this option to return
            the baseline task information of only the input ScheduleTask objects.)
            """

class NotificationRuleInfo:
    """
    
The information needed for the creation of a single Notification or subscription
rule.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the rule."""
    Target: Teamcenter.Soa.Client.Model.ModelObject
    """The Schedule or ScheduleTask."""
    Subscriber: Teamcenter.Soa.Client.Model.ModelObject
    """
            The subscriber for this notification. It is same as target object in case of notification
            or a User object in the case of subscription.
            """
    Recipient: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of UID of User, Resource Pool, Discipline, or Schedule Member
            to be notified.
            """
    RuleType: str
    Status: bool
    """
            If true, notification will be sent when event is triggered; otherwise, notification
            will not be sent.
            """
    Update: bool
    """
            If true, the update on the existing notification rule is performed; otherwise, a
            new notification rule is created.
            """
    ListOfAdditionalProperties: list[AdditionalProperties]
    """
            A collection of AdditionalProperties structures. Each AdditionalProperties structure
            holds property name and value for notification rules.
            """

class ScheduleManagement:
    """
    Interface ScheduleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateNotificationRules(self, NotificationRuleInfos: list[NotificationRuleInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Creates a list of notification rules for Schedule or ScheduleTask objects
             based on the notification rule info structure. The notification rules are used to
             notify individuals, including yourself, of important events associated with selected
             objects. Notifications utilize Teamcenter mail and the Subscription Manager. To receive
             notifications and subscriptions, a system administrator must set the value of the
             Mail_server_name preference to a name of a valid mail server (this task needs only
             to be performed once). The e-mail address in the Person object for every user
             that's expected to receive a notification.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param NotificationRuleInfos: 
                         createOrUpdateNotificationRules
             
        :return: 230316: Invalid target object is provided for Notification operation.
        """
        ...
    def LoadBaselines(self, LoadBaselinesInfo: LoadBaselinesInfo) -> LoadBaselineResponse:
        """    
             Loads the information about the baseline tasks of the given ScheduleTask objects
             based on the source Schedule and the baseline Schedule objects.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param LoadBaselinesInfo: 
                         Information about the <b>Schedule</b> baseline to load.
             
        :return: 230504: The schedule baseline to load is invaliddoes not belong to the source schedule.
        """
        ...

