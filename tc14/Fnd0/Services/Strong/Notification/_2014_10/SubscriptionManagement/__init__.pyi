import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ActionHandler:
    """
    
            Each handler will have an ImanActionHandler that describes the function to
            execute, and its own set of parameters.  These parameters are made up as a list of
            strings.  Not all handlers require parameters, but they should be present in the
            correct format if the handler expects them.  There will be no validation of the parameters
            when the Subscription is being created or modified.
            
            In the case of the default notification handler, the parameters should contain a
            list of the users to receive the e-mail.
            
    """
    def __init__(self, ) -> None: ...
    Handler: Teamcenter.Soa.Client.Model.Strong.ImanActionHandler
    """The ImanActionHandler functionality to execute when the Subscription is processed."""
    Parameters: list[str]
    """List of values to be passed to the handler during execution."""

class AttributeComparison:
    """
    
            The overall attribute criteria for a Subscription can be made up of multiple individual
            attribute comparisons.  Each attribute comparison specifies the attribute on the
            target object to check, the value to compare it against and how to do the comparison.
            
    """
    def __init__(self, ) -> None: ...
    MathOperator: str
    """
            The math operator to use when comparing the attribute to the specified value. The
            MathOperators enum comprises of these values: EqualTo, NotEqualTo, GreaterThan, LessThan,
            GreaterThanEqualTo, LessThanEqualTo.
            """
    AttributeName: str
    """The name of the attribute on the target object to compare against."""
    AttributeValue: str
    """The string value to compare against."""

class AttributeCriteria:
    """
    
            If attribute criteria are specified on a Subscription, these criteria will be evaluated
            when the Subscription is being processed.  This processing involves comparing values
            in the criteria to the attribute values on the target object using a math operator,
            such as >, < or =.  Multiple attribute comparisons are then grouped using logic
            operators such as AND and OR.  Each AttributeCriteria represents a single
            attribute comparison and the logical operator to use when comparing it to the previous
            AttributeCriteria entry.
            
    """
    def __init__(self, ) -> None: ...
    LogicOperator: str
    """
            The logic operator to use when comparing each AttributeCriteria to the next.
            Processing will be done in order.  The first value in this list will be ignored.
            """
    AttributeComparison: AttributeComparison
    """A single attribute comparison."""

class FindSubscriptionsCriteriaInput:
    """
    Contains all the input criteria required to search for Subscriptions.
    """
    def __init__(self, ) -> None: ...
    Target: Teamcenter.Soa.Client.Model.ModelObject
    """
            The object to monitor for the specified event type.  This can also be Business Object
            type for class based Subscriptions.
            """
    Subscriber: Teamcenter.Soa.Client.Model.Strong.User
    """The User that is subscribing to the event."""
    EventType: Teamcenter.Soa.Client.Model.Strong.ImanEventType
    """Type of event that will trigger the subscription."""
    Handlers: list[Teamcenter.Soa.Client.Model.Strong.ImanActionHandler]
    """An ordered list of handlers to execute when processing the Subscription."""
    Condition: Teamcenter.Soa.Client.Model.Strong.Condition
    """
            The Condition to evaluate when processing this Subscription.  Only valid for
            class based Subscriptions.  Can be NULL.
            """

class GetSubscriptionsCriteriaInput:
    """
    Contains all the input criteria required to search for Subscriptions.
    """
    def __init__(self, ) -> None: ...
    Target: Teamcenter.Soa.Client.Model.ModelObject
    """
            The object to monitor for the specified event type.  This can also be Business Object
            type for class based ImanSubscription.  May be NULL.
            """
    Subscriber: Teamcenter.Soa.Client.Model.Strong.User
    """The User that is subscribing to the event.  May be NULL."""
    EventType: Teamcenter.Soa.Client.Model.Strong.ImanEventType
    """Type of event that will trigger the subscription.  May be NULL."""
    Handlers: list[Teamcenter.Soa.Client.Model.Strong.ImanActionHandler]
    """The handlers to execute when processing the Subscription.  May be an empty list."""
    ExecTimeBefore: System.DateTime
    """Upper limit of the Subscription execution time."""
    ExecTimeAfter: System.DateTime
    """Lower limit of the Subscription execution time."""
    ExecImmediately: bool
    """If true, do not search for Subscriptions with an execution time."""
    ExpDateBefore: System.DateTime
    """Upper limit of the Subscription expiration date."""
    ExpDateAfter: System.DateTime
    """Lower limit of the Subscription expiration date."""
    NoExpDate: bool
    """If true, do not search for Subscriptions with an expiration date."""

class NotificationDefinition:
    """
    
            For e-mail notification handlers, a NotificationDefinition must be specified.  This
            structure describes the content of the e-mail to be sent as part of the notification
            Subscription.  This includes the subject, message and object properties to display
            in the message.  The recipients of the message are included in the HandlerParameters
            specified in the Subscription definition.
            
    """
    def __init__(self, ) -> None: ...
    Subject: str
    """The subject of the notification e-mail."""
    Message: str
    """The message body of the notification e-mail."""
    PropertyNames: list[str]
    """
            List of properties to include in the notification e-mail.  The values of these properties
            will be taken from the target object at the time the handler is executed.  These
            properties are not required.
            """

class SubscriptionInput:
    """
    
            Contains all the input criteria required to create a single object or class based
            Subscription.  The main inputs include the target object, subscriber, event type
            and action handler list.
            

            The notification should be included if the IMAN_Smtp_Mail_Notify handler is
            used.
            

    """
    def __init__(self, ) -> None: ...
    Target: Teamcenter.Soa.Client.Model.ModelObject
    """
            The object to monitor for the specified event type.  This can also be Business Object
            type for class based ImanSubscription.
            """
    Subscriber: Teamcenter.Soa.Client.Model.Strong.User
    """The User that is subscribing to the event."""
    EventType: Teamcenter.Soa.Client.Model.Strong.ImanEventType
    """Type of event that will trigger the subscription."""
    Handlers: list[ActionHandler]
    """
            An ordered list of handlers to execute when processing the Subscription.  Handlers
            will be executed in the order they appear in this list.  Duplicates are not allowed.
            Each handler specified will also have its own set of handler parameters that will
            be passed to the handler during its execution.
            """
    Condition: Teamcenter.Soa.Client.Model.Strong.Condition
    """
            The Condition to evaluate when processing this Subscription.  Only valid for
            class based Subscriptions.  Can be NULL.
            """
    Criteria: list[AttributeCriteria]
    """
            Attribute criteria to process when the Subscription is being executed.  If these
            attribute values match those of the object, the Subscription will apply.  Each entry
            in the list will be compared to the next using the logicOperator of the next
            value.  The logicOperator of the first entry will not be used.  Can be empty.
            """
    RevisionOption: str
    """Indicates the type of Item Revision objects that will apply to the Subscription."""
    ExecutionTime: System.DateTime
    """
            The time of day when the Subscription should be processed.  Setting NULLDATE will
            cause the handlers to be run as soon as resources are available.
            """
    ExpirationDate: System.DateTime
    """
            The date when the Subscription expires and will no longer be processed.  Setting
            NULLDATE will cause the Subscription to never expire.
            """
    Notification: NotificationDefinition
    """
            Specifies the parameters to be used when sending the notification e-mail.  Should
            be present for notification handlers.  Can be NULL for all non-notification handlers.
            """

class ModifySubscriptionInput:
    """
    
            Contains the Subscription object to modify and all of the input values to set on
            the Subscription.  Supports both object and class based Subscriptions.
            
    """
    def __init__(self, ) -> None: ...
    Subscription: Teamcenter.Soa.Client.Model.Strong.ImanSubscription
    """The ImanSubscription object to modify."""
    NewSubscriptionValues: SubscriptionInput
    """The new values to set on the Subscription."""

class SubscriptionsResponse:
    """
    List of the ImanSubscription objects from the operation.
    """
    def __init__(self, ) -> None: ...
    Subscriptions: list[Teamcenter.Soa.Client.Model.Strong.ImanSubscription]
    """List of the Subscription objects from the operation."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Returned service data."""

class SubscriptionManagement:
    """
    Interface SubscriptionManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateSubscriptions(self, Inputs: list[SubscriptionInput]) -> SubscriptionsResponse:
        """    
             This operation creates multiple object or class based Subscriptions based on the
             provided inputs. A Subscription allows a specified piece of functionality to be executed
             whenever an event occurs on the target object. Inputs to this operation will allow
             the target object to be specified, along with the event to monitor. The functionality
             the execute is specified by an array of ImanActionHandler objects. These handlers
             will be executed in the order they are specified in the Subscription definition.
             The most common handler would be IMAN_Smtp_Mail_Notify, which is used to send
             an e-mail when the event is triggered. If this handler is specified, the notification
             object should also be included as input.
             

             This operation also creates class based Subscriptions. This is done by passing a
             type object as the target object.  Class based Subscriptions will apply to all objects
             of the specified type. These can be filtered down at execution time by specifying
             a condition or attribute criteria as input. The Condition or attribute criteria
             will be evaluated against the object on which the event occurred, and the handler
             will only be executed if the Condition evaluates to TRUE.  Conditions
             and attribute criteria only apply for class based Subscriptions.  Attribute criteria
             are made up of a list of attributes and the values to compare them against off the
             target object.  Each of these comparisons can be logically combined.
             


Use Cases:

Object Based Subscription:

             The client creates an object based Subscription in order to trigger functionality
             when a specific event occurs against the object. An example of this would be subscribing
             to the "Check Out" event for a given object. Any time the object is checked out,
             the handler functionality will be executed. Most often, this functionality will send
             the given user an e-mail notification.
             

Class Based Subscription:

             The client creates a class based Subscription in order to trigger functionality when
             a specific event occurs against any object of the given type. An example of this
             would be subscribing to the "Check Out" event for an ItemRevision objects.
             Any time the object is checked out, the handler functionality will be executed. Most
             often, this functionality will send the given user an e-mail notification.
             

             Class based subscriptions allow a Condition or attribute criteria to be specified
             as part of the definition. This allows the events to be filtered to a smaller level.
             Any time the event occurs against the given object of the specified type, the Condition
             will be evaluated against the object. If the Condition or attribute criteria
             evaluate to true, the event is posted and the handlers are executed. An example Condition
             would only evaluate to true if the object is part of a specific Project.  Attribute
             criteria can also be specified and will be evaluated when the Subscription is being
             processed.  If the attribute criteria values do not match, the Subscription will
             be rejected.  Both attribute criteria and a Condition can not be specified
             at the same time.
             

Teamcenter Component:

             Subscription Management - Application in Teamcenter that allows users to subscribe
             to a certain events on business objects.
             
        :param Inputs: 
                         A set of SubscriptionInput data structures that provide the input parameters needed
                         for defining the Subscriptions.  Each input provides all the parameters needed for
                         a single Subscription definition.
             
        :return: 78019:Â Â Â Â Could not create the Subscription with the given criteria.
        """
        ...
    def FindSubscriptions(self, Input: FindSubscriptionsCriteriaInput) -> SubscriptionsResponse:
        """    
             This operation queries for all Subscriptions that meet the input criteria.  A variety
             of input parameters are allowed, including target, event type, subscriber, condition
             and handlers.
             

Use Cases:

             The client is searching for a previously created Subscription against a given object
             or type.
             

Teamcenter Component:

             Subscription Management - Application in Teamcenter that allows users to subscribe
             to a certain events on business objects.
             
        :param Input: 
                         A variety of Subscription criteria that provides the input parameters needed for
                         defining finding Subscriptions.
             
        :return: 
        """
        ...
    def GetSubscriptions(self, Input: GetSubscriptionsCriteriaInput) -> SubscriptionsResponse:
        """    
             This operation queries for all Subscriptions that meet the input criteria.  A variety
             of input parameters are allowed, including target, event type, subscriber and handler.
             This is intended to return a larger number of Subscriptions based on a small set
             of input criteria.  Most of the parameters can be empty, and will not be considered
             as part of the query.
             

Use Cases:

             The client is searching for all Subscriptions created for a given user against a
             given object.
             

Teamcenter Component:

             Subscription Management - Application in Teamcenter that allows users to subscribe
             to a certain events on business objects.
             
        :param Input: 
                         A variety of Subscription criteria that provides the input parameters needed for
                         defining finding Subscriptions.
             
        :return: 
        """
        ...
    def ModifySubscriptions(self, Inputs: list[ModifySubscriptionInput]) -> SubscriptionsResponse:
        """    
             This operation modifies existing ImanSubscriptions.  All values specified
             in the inputs replace the values on the ImanSubscription in the database.
             Each modification is verified to insure that a duplicate ImanSubscription
             is not created.
             

Use Cases:

             An existing Subscription needs to have one or more of its values modified.
             

Teamcenter Component:

             Subscription Management - Application in Teamcenter that allows users to subscribe
             to a certain events on business objects.
             
        :param Inputs: 
                         The input parameters for the modification.
             
        :return: 
        """
        ...

