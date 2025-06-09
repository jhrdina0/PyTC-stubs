import Fnd0.Services.Strong.Notification._2014_10.SubscriptionManagement
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class Accessors:
    def __init__(self, ) -> None: ...
    Groups: list[Teamcenter.Soa.Client.Model.Strong.Group]
    Roles: list[Teamcenter.Soa.Client.Model.Strong.Role]

class AttributeCriteria2:
    def __init__(self, ) -> None: ...
    LogicOperators: list[str]
    AttributeNames: list[str]
    MathOperators: list[str]
    AttributeValues: list[str]

class GetAttachEventDataResponse2:
    def __init__(self, ) -> None: ...
    Relations: list[Teamcenter.Soa.Client.Model.ModelObject]
    AttachmentTypes: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SubscriptionTemplate:
    def __init__(self, ) -> None: ...
    Name: str
    Description: str
    SubscribedObjectType: Teamcenter.Soa.Client.Model.ModelObject
    SubscribedObjectCriteria: AttributeCriteria2
    TargetObjectType: Teamcenter.Soa.Client.Model.ModelObject
    TargetObjectCriteria: AttributeCriteria2
    ClosureRule: Teamcenter.Soa.Client.Model.Strong.ClosureRule
    ValidAccessors: Accessors

class ModifySubscriptionTemplateInput:
    def __init__(self, ) -> None: ...
    SubscriptionTemplate: Teamcenter.Soa.Client.Model.Strong.Fnd0SubscriptionTemplate
    TemplateData: SubscriptionTemplate

class SaveAsSubscriptionInputData:
    def __init__(self, ) -> None: ...
    Subscription: Teamcenter.Soa.Client.Model.Strong.ImanSubscription
    Name: str

class SubscriptionTemplateResponse:
    def __init__(self, ) -> None: ...
    SubscriptionTemplates: list[Teamcenter.Soa.Client.Model.Strong.Fnd0SubscriptionTemplate]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SubscriptionManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateSubscriptionTemplates(self, Inputs: list[SubscriptionTemplate]) -> SubscriptionTemplateResponse: ...
    def GetApplicableSubscriptionTemplates(self, SubscribedObject: Teamcenter.Soa.Client.Model.ModelObject) -> SubscriptionTemplateResponse: ...
    def GetAttachEventData2(self, Target: Teamcenter.Soa.Client.Model.ModelObject) -> GetAttachEventDataResponse2: ...
    def ModifySubscriptionTemplates(self, Inputs: list[ModifySubscriptionTemplateInput]) -> SubscriptionTemplateResponse: ...
    def SaveAsSubscription(self, Input: SaveAsSubscriptionInputData) -> Fnd0.Services.Strong.Notification._2014_10.SubscriptionManagement.SubscriptionsResponse: ...
    def Unsubscribe(self, Subscriptions: list[Teamcenter.Soa.Client.Model.Strong.ImanSubscription]) -> Fnd0.Services.Strong.Notification._2014_10.SubscriptionManagement.SubscriptionsResponse: ...

