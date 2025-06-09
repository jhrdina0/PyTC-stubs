import Fnd0.Services.Strong.Notification._2014_10.SubscriptionManagement
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DateRange:
    def __init__(self, ) -> None: ...
    FromDate: System.DateTime
    ToDate: System.DateTime

class EventObject:
    def __init__(self, ) -> None: ...
    ClientId: str
    BusinessObject: Teamcenter.Soa.Client.Model.ModelObject

class ExecutionPeriod:
    def __init__(self, ) -> None: ...
    ExecutionTime: System.DateTime
    ExecutionDay: str
    Frequency: str

class FindSubscriptionsInput2:
    def __init__(self, ) -> None: ...
    Target: Teamcenter.Soa.Client.Model.ModelObject
    Subscriber: Teamcenter.Soa.Client.Model.Strong.User
    EventType: Teamcenter.Soa.Client.Model.Strong.ImanEventType
    Handlers: list[Fnd0.Services.Strong.Notification._2014_10.SubscriptionManagement.ActionHandler]
    Condition: Teamcenter.Soa.Client.Model.Strong.Condition
    Name: str
    ExecutionTimeRange: DateRange
    ExpirationDateRange: DateRange
    NoExpDate: bool
    NotificationPriority: str
    IsActive: int
    Frequency: str
    ExecutionDay: str
    Notifier: Teamcenter.Soa.Client.Model.Strong.User
    TemporaryNotifierDateRange: DateRange

class GetAssignEventDataResponse:
    def __init__(self, ) -> None: ...
    ReleaseStatus: list[Teamcenter.Soa.Client.Model.Strong.TaskType]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetAttachEventDataResponse:
    def __init__(self, ) -> None: ...
    Relations: list[Teamcenter.Soa.Client.Model.Strong.ImanRelation]
    AttachmentTypes: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetEventTypesResponse:
    def __init__(self, ) -> None: ...
    ClientId: str
    AuditableEventTypes: list[Teamcenter.Soa.Client.Model.Strong.ImanEventType]
    SubscribableEventTypes: list[Teamcenter.Soa.Client.Model.Strong.ImanEventType]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetSubscribableTypesResponse:
    def __init__(self, ) -> None: ...
    TypeInfoList: list[SubscribableTypeInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetSubscriptionInputResponse:
    def __init__(self, ) -> None: ...
    EventTypes: list[Teamcenter.Soa.Client.Model.Strong.ImanEventType]
    Handlers: list[Teamcenter.Soa.Client.Model.Strong.ImanActionHandler]
    AttributeCriteria: list[Fnd0.Services.Strong.Notification._2014_10.SubscriptionManagement.AttributeCriteria]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SubscriptionInput2:
    def __init__(self, ) -> None: ...
    Target: Teamcenter.Soa.Client.Model.ModelObject
    Subscriber: Teamcenter.Soa.Client.Model.Strong.User
    Name: str
    EventType: Teamcenter.Soa.Client.Model.Strong.ImanEventType
    Handlers: list[Fnd0.Services.Strong.Notification._2014_10.SubscriptionManagement.ActionHandler]
    Condition: Teamcenter.Soa.Client.Model.Strong.Condition
    Criteria: list[Fnd0.Services.Strong.Notification._2014_10.SubscriptionManagement.AttributeCriteria]
    RevisionOption: str
    ExecutionPeriod: ExecutionPeriod
    ExpirationDate: System.DateTime
    Notification: Fnd0.Services.Strong.Notification._2014_10.SubscriptionManagement.NotificationDefinition
    NotificationPriority: str
    IsActive: bool

class ModifySubscriptionsInput2:
    def __init__(self, ) -> None: ...
    SubscriptionObject: Teamcenter.Soa.Client.Model.Strong.ImanSubscription
    NewSubscriptionValues: SubscriptionInput2

class SubscribableTypeInfo:
    def __init__(self, ) -> None: ...
    Type: Teamcenter.Soa.Client.Model.ModelObject
    TypeName: str
    Parents: list[str]

class TransferNotificationInput:
    def __init__(self, ) -> None: ...
    Subscriptions: list[Teamcenter.Soa.Client.Model.Strong.ImanSubscription]
    Notifier: Teamcenter.Soa.Client.Model.Strong.User
    NotificationDateRange: DateRange

class SubscriptionManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateSubscriptions(self, Inputs: list[SubscriptionInput2]) -> Fnd0.Services.Strong.Notification._2014_10.SubscriptionManagement.SubscriptionsResponse: ...
    def FindSubscriptions(self, Input: FindSubscriptionsInput2) -> Fnd0.Services.Strong.Notification._2014_10.SubscriptionManagement.SubscriptionsResponse: ...
    def GetAssignEventData(self) -> GetAssignEventDataResponse: ...
    def GetAttachEventData(self, Target: Teamcenter.Soa.Client.Model.ModelObject) -> GetAttachEventDataResponse: ...
    def GetEventTypes2(self, Input: list[EventObject]) -> GetEventTypesResponse: ...
    def GetSubscribableTypes(self, ChildTypeOption: str) -> GetSubscribableTypesResponse: ...
    def GetSubscriptionInput(self, Input: Teamcenter.Soa.Client.Model.ModelObject) -> GetSubscriptionInputResponse: ...
    def ModifySubscriptions(self, Inputs: list[ModifySubscriptionsInput2]) -> Fnd0.Services.Strong.Notification._2014_10.SubscriptionManagement.SubscriptionsResponse: ...
    def TransferNotifications(self, Input: TransferNotificationInput) -> Fnd0.Services.Strong.Notification._2014_10.SubscriptionManagement.SubscriptionsResponse: ...

