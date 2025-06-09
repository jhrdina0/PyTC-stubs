import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DeleteNotificationRuleContainer:
    """
    The input information needed to delete an existing notification rule.
    """
    def __init__(self, ) -> None: ...
    Target: Teamcenter.Soa.Client.Model.ModelObject
    """The tag  of  the Schedule  or ScheduleTask."""
    Subscriber: Teamcenter.Soa.Client.Model.ModelObject
    """The tag of the subscriber."""
    RuleType: str
    """The type of rule to delete. Valid values-{ __Add_Task,__Delete_Task,__Near_Due,__Overdue,__Start_Date_Change,__Finish_Date_Change,__Status_Change,__Status_ChangeTo,__Priority_Change,__Priority_ChangeTo,__Work_Estimate_Change,__Work_Complete_Change,__Work_Ready,__User_Assigned}"""

class GetNotificationRuleContainer:
    """
    The input information needed to find all notifications for a particular task or
schedule.
    """
    def __init__(self, ) -> None: ...
    Target: Teamcenter.Soa.Client.Model.ModelObject
    """The tag of a Schedule or ScheduleTask."""
    Subscriber: Teamcenter.Soa.Client.Model.ModelObject
    """The tag of the subscriber."""

class MultiScheduleCopyResponse:
    """
    Container to hold multiple ScheduleCopyResponse objects.
    """
    def __init__(self, ) -> None: ...
    ScheduleResponse: list[ScheduleCopyResponse]
    """A collection of the schedule responses."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData."""

class NotificationRuleContainer:
    """
    The information needed for the creation of a single Notification rule.
    """
    def __init__(self, ) -> None: ...
    Target: Teamcenter.Soa.Client.Model.ModelObject
    """The tag of a schedule or task"""
    Subscriber: Teamcenter.Soa.Client.Model.ModelObject
    """
            The subscriber for this notification.  It is the Target object in the case of a notification
            or a User object in the case of a subscription.
            """
    NotificationSubject: str
    """Subject of the email. Valid value- can be empty string"""
    NotificationMessage: str
    """Message of the e-mail. Valid value- can be empty string"""
    Recipient: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The Users, groups, disciplines, or schedule members to be notified."""
    AdditionalEmails: str
    """A semi-colon separated list of e-mail addresses. Valid value - can be empty string"""
    NotificationCondition: str
    """
            The condition data for notifications that are triggered conditionally.  E.g.  Schedule
            Task near due. Valid value - can be empty string
            """
    RuleType: str
    """
            The type of rule to create. Valid values are {__Add_Task,__Delete_Task,__Near_Due,__Overdue,__Start_Date_Change,__Finish_Date_Change,__Status_Change,__Status_ChangeTo,__Priority_Change,__Priority_ChangeTo,__Work_Estimate_Change,__Work_Complete_Change,__Work_Ready,__User_Assigned
            }
            """
    Status: bool
    """Active or inactive status of the notification."""
    Update: bool
    """Attempting to update an existing rule."""

class NotificationRulesList:
    """
    A collection of the single NotificationRuleContainer objects.
    """
    def __init__(self, ) -> None: ...
    NotificationRules: list[NotificationRuleContainer]
    """The collection of Notification Rules."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData."""

class ScheduleCopyOptionsContainer:
    """
    The input information necessary to copy a schedule.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the new schedule."""
    Description: str
    """The description of the new schedule."""
    ScheduleToCopy: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The tag to the schedule to copy."""
    ResetWork: bool
    """
            Flag to indicate whether or not to reset the tasks' execution data (%, status,
            work complete, etc).
            """
    CopyBaselines: bool
    """Flag to indicate whether or not to copy baselines."""
    LoadOnResponse: bool
    """Flag to indicate whether or not to load the schedule in the response."""

class ScheduleCopyResponse:
    """
    
The response from a schedule copy call.  It includes all the data necessary to
load
that schedule.
    """
    def __init__(self, ) -> None: ...
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The schedule."""
    ScheduleTask: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    """The schedule tasks."""
    ResourceAssignment: list[Teamcenter.Soa.Client.Model.Strong.ResourceAssignment]
    """The task assignments."""
    TaskDependency: list[Teamcenter.Soa.Client.Model.Strong.TaskDependency]
    """The task dependencies."""
    Calendar: list[Teamcenter.Soa.Client.Model.Strong.TCCalendar]
    """The calendars asssociated with the schedule and its members."""
    CalendarEvent: list[Teamcenter.Soa.Client.Model.Strong.TCCalendarEvent]
    """The calendar events associated with the calendars."""

class TaskDeliverableContainer:
    """
    The input information for a single task deliverable.
    """
    def __init__(self, ) -> None: ...
    ScheduleTask: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The task which will contain this delievable. Tag of the task"""
    ScheduleDeliverable: Teamcenter.Soa.Client.Model.ModelObject
    """The ScheduleDeliverable to reference. Tag of schedule deliverable."""
    SubmitType: int
    """The submit type  (3=Don't submit, 0=submit as target, 1=submit as reference)."""

class ScheduleManagement:
    """
    Interface ScheduleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CopySchedules(self, ScheduleCopyContainer: list[ScheduleCopyOptionsContainer]) -> MultiScheduleCopyResponse:
        """    
             Makes a deep copy of the schedule with options to reset work and copy existing baselines.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param ScheduleCopyContainer: 
                         A collection of ScheduleCopyOptionsContainer structures.
             
        :return: It contains ScheduleCopyResponse structures partial errors and failures are also
             updated and returned through ServiceData of this object.
        """
        ...
    def CreateOrUpdateNotificationRules(self, NotificationsContainers: list[NotificationRuleContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Creates a list of notification rules for Schedule or ScheduleTask based
             on the notifications container. You use notifications to notify individuals, including
             yourself, of important events associated with selected objects. Notifications
             utilize Teamcenter mail and the Subscription Manager. To receive notifications
             and subscriptions, a system administrator must set the value of the Mail_server_name
             preference to a name of a valid mail server (this task needs only to be performed
             once). The e-mail address in the Person object for every user that's expected
             to receive a notification.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param NotificationsContainers: 
                         A collection of NotificationRuleContainers.
             
        :return: which contains references
             to the created and updated objects.
        """
        ...
    def CreateTaskDeliverableTemplates(self, TaskDeliverableData: list[TaskDeliverableContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Creates new task deliverable template and relates them to the task. This is done
             by going through each deliverable, checks if the user has write access on the specified
             task, and then checking if the task deliverable already exists for the task.  If
             it does not exist it will create an instance of the task deliverable and add to the
             list of task deliverables.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param TaskDeliverableData: 
                         A collection of <font face="courier" height="10">TaskDeliverableContainer</font>
                         structures that contain the schedule task, the schedule deliverable, and the submit
                         type.
             
        :return: 
        """
        ...
    def DeleteNotificationRules(self, NotificationRuleContainer: list[DeleteNotificationRuleContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Delete notification rules for Schedule or ScheduleTask based on the
             contents of the delete notifications container. After deleting the notification will
             rule, the users attached to that rule will not receive any more notifications for
             that specific action.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param NotificationRuleContainer: 
                         A collection of DeleteNotificationRuleContainers.
             
        :return: The reference to the tag of the deleted objects.
        """
        ...
    def GetNotificationRules(self, NotificationRuleContainer: list[GetNotificationRuleContainer]) -> NotificationRulesList:
        """    
             Get a list of notification rules for Schedule or ScheduleTask based
             on the notifications container. Use notifications to notify individuals, including
             yourself, of important events associated with selected objects. Notifications utilize
             Teamcenter mail and the Subscription Manager. To receive notifications and
             subscriptions, a system administrator must set the value of the Mail_server_name
             preference to a name of a valid mail server (this task needs only to be performed
             once). The e-mail address in the Person object for every user that's expected
             to receive a notification.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param NotificationRuleContainer: 

        :return: 
        """
        ...

