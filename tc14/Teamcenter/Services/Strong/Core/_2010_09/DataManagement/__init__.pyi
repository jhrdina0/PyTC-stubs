import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateOrUpdateStaticTableDataResponse:
    """
    Contains Creation or updation response for Static table.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """SOA Service Data."""
    StaticTableObject: Teamcenter.Soa.Client.Model.Strong.Fnd0StaticTable
    """StaticTable Object"""

class EventObject:
    """
    
            The EventObject structure represents required
            parameter to get event type names for the businessObject.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique identifier supplied by the caller. This ID is client's way of identifying
            event list.  This is a required parameter. If nothing is to be passed to clientId;
            assign an empty String object. Assigning NULL to clientId is not allowed.
            """
    BusinessObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The Business Object for which the valid Auditable and Subscribable event type list
            is to be retrieved. This is a required parameter.
            """

class EventTypesOutput:
    """
    
            The EventTypesOutput structure represents
            the outputs, auditableEvents and subscribableEvents, which are vectors of auditable
            event type names and subscribable event type names.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client unique identifier which is passed back for tracking the operation status."""
    AuditableEvents: list[str]
    """The list of Auditable event type names."""
    SubscribableEvents: list[str]
    """The list of Subscribable event type names"""

class EventTypesResponse:
    """
    
            The EventTypesResponse structure represents
            the output response returning  a vector  of EventTypesOutput
            with partial errors wrapped in  serviceData, if any.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[EventTypesOutput]
    """
            A vector of EventTypesOutput structures packaged
            in custom response. Success is defined by the return of the ifailError for getEventTypes on each of the businessObject.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Partial failures will be returned in the ServiceDate for each failed processing.
            Error encountered while processing post event on element in the set is reported as
            partial errors and processing continues for the remaining elements in the input set.
            """

class NameValueStruct1:
    """
    This structure contains property name and value pairs for each property.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Name of the property"""
    Values: list[str]
    """Values of the property"""

class PostEventObjectProperties:
    """
    
            The PostEventObjectProperties structure represents
            required parameters to post event on primaryObject when event eventTypeName occurs.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique identifier supplied by the caller. This ID is used to identify return PostEventOutput
            and partial errors assocaited with this input structure. This is optional, provide
            empty String for null or optional value i.e. new String[0].
            """
    PrimaryObject: Teamcenter.Soa.Client.Model.ModelObject
    """The Business Object on which the event has occurred. This is a required parameter."""
    SecondaryObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Secondary object should be passed when an event involves two objects, primaryObject
            and secondaryObject and writing the secondaryObject details conveys complete Audit
            information. Example, attaching license to Item. This is optional, provide null value
            for optional value.
            """
    PropertyCount: int
    """
            The propertyCount is the count of properties that user wants to be written  to Audit
            log. If the propertyCount is 0 the propertyNames and propertyValues will be ignored
            and treated as NULL values. This is optional and default value is 0.
            """
    PropertyNames: list[str]
    """
            The propertyNames is the list of property names to be written to audit log. The total
            number of properties to write depends on the propertyCount value. This is optional,
            provide empty String for null or optional value i.e. new String[0].
            """
    PropertyValues: list[str]
    """
            The propertyValues is the list of property values to be written to audit log for
            each of the propertyNames. The total number of properties to write depends on the
            propertyCount and propertyNames value. Any of these values if not specified will
            treat propertyValues as NULL.  This is optional, provide empty String for null or
            optional value i.e. new String[0].
            """
    ErrorCode: int
    """
            Specify error code when failure of an event is to be recorded in audit log. This
            is optional and default value is 0.
            """
    ErrorMessage: str
    """
            Specify error message when failure of an event is to be recorded in audit log. This
            is optional, you should provide empty String object for null or optional value i.e.
            new String[0].
            """

class PostEventOutput:
    """
    
            The PostEventOutput structure represents
            the output success or failure for each of the PostEventObjectProperties
            structure in ifailError  for the assocaited clientId.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client unique identifier which is passed back for tracking the operation status."""
    IfailError: int
    """The error code, if any. Packaged in the custom output response."""

class PostEventResponse:
    """
    
            The PostEventResponse structure represents
            the output returning a vector of PostEventOutput
            with partial errors wrapped in serviceData, if any.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[PostEventOutput]
    """
            A vector of PostEventOutput structures packaged
            in custom response. Success is defined by the return of the ifailError for post event
            on each of the primaryObject.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Partial failures will be returned in the Service Data for each failed processing.
            Error encountered while processing post event on element in the set is reported as
            partial errors and processing continues for the remaining elements in the input set.
            """

class PropInfo:
    """
    
            This structure holds information about Teamcenter object & its timestamp and
            list of property name/value pair information.
            
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """business object"""
    VecNameVal: list[NameValueStruct1]
    """Vector of property information"""
    Timestamp: System.DateTime
    """Timestamp of the object when object was exported to clients."""

class RowData:
    """
    Row Data
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """clientId"""
    RowObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """Row Object"""
    RowType: str
    """RowType"""
    RowAttrValueMap: System.Collections.Hashtable
    """Row Attribute Value Pair Map"""

class SetPropertyResponse:
    """
    
            response structure for setProperties operation. It returns the information about
            overwritten objects.
            
    """
    def __init__(self, ) -> None: ...
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """This is the service data. It contains the updated objects and their properties."""
    ObjPropMap: System.Collections.Hashtable
    """
            Additional information to be communicated to client such as objects and props those
            are overwritten. This map can be empty if no overwritten object found or with QUERY
            option is not an input to the service operation.
            """

class StaticTableDataResponse:
    """
    StaticTableDataResponse
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by caller.
            
            This ID is used to identify return data elements and partial errors associated with
            this input structure.
            
"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class StaticTableInfo:
    """
    Static Table Info
    """
    def __init__(self, ) -> None: ...
    TableType: str
    """type of table created/updated e.g. TableProperties"""
    TableObject: Teamcenter.Soa.Client.Model.Strong.Fnd0StaticTable
    """Fnd0StaticTable object"""

class VerifyExtensionInfo:
    """
    
            The required information in which to validate an extension exists on an operation
            for a specific type.
            
    """
    def __init__(self, ) -> None: ...
    TypeName: str
    """The name of the type in which to check the operations."""
    OperationName: str
    """The name of the operation in which to check for the containing extension."""
    ExtensionName: str
    """The name of the extension to check."""
    ExtensionType: int
    """The extension type to check: 0=All, 1=PreCondition, 2=PreAction, 3=PostAction, 4=BaseAction"""

class VerifyExtensionResponse:
    """
    The result of the Verify Extension method.
    """
    def __init__(self, ) -> None: ...
    Output: list[bool]
    """Returns True if extension exists otherwise False."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """This data structure provides service data for associated information."""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SetProperties(self, Info: list[PropInfo], Options: list[str]) -> SetPropertyResponse:
        """    
             This operation is provided to update Teamcenter object instances for the given name/value
             pairs. This operation works for all supported property value types. Each object need
             to be passed with its property name/value pairs.Passing options are not mandatory,
             empty list is allowed. When no options are provided, it just updates
             the objects as per the inputs. Alternatively you can pass following valid options
             to control updating the data.
             

QUERY: option is used to define the overall behavior of object
             properties setting from Excel Live and Word Live. Once this option is passed, server
             honours the preference value of TC_setProperties. Please see the Preferences and
             Environment Variables Reference documentation for preference TC_setProperties for
             more information.
             


             Note:It must be the 0th element when set as in the option list.
             

ENABLE_PSE_BULLETIN_BOARD: To enable the generation of PSE
             bulletin board events. These events are processed through Bulletin board callback
             mechanism.
             


        :param Info: 
                         List of PropInfo structure which consists of information about the objects and the
                         property values to set.
             
        :param Options: 
<ul>
<li type="disc"><b>ENABLE_PSE_BULLETIN_BOARD</b> To enable the generation of PSE
                         bulletin board events.
                         </li>
</ul>

        :return: Response structure for set Properties SOA.
        """
        ...
    def VerifyExtension(self, ExtensionInfo: list[VerifyExtensionInfo]) -> VerifyExtensionResponse:
        """    This operation checks if an extension exists on an operation of a specific type.
        :param ExtensionInfo: 
                         The specific type, operation and extension information required to verify an extension
                         exists.
             
        :return: If extension exists.
        """
        ...
    def CreateOrUpdateStaticTableData(self, StaticTableInfo: StaticTableInfo, RowProperties: list[RowData]) -> CreateOrUpdateStaticTableDataResponse:
        """    
             This creates a new Table along with Rows or updates an existing Table with rows and
             their values based on input StaticTableInfo and created Table rows are added to the
             Table. ServiceData is updated with newly created/updated Table.
             

Use Cases:

             This operation is used to create/update the data for TableProperties objects of Fnd0StaticTable
             object. When user selects Cdm0DataReqItemRevision object, the attribute cdm0EventsList
             is displayed in the summary as well as on View/Edit Properties menu in RAC. The attribute
             cdm0EventsList is type referenced to Fnd0StaticTable.
             
             User can add the data in columns for each row of the table or adds rows to the table
             or deletes rows. After creation/updation of the table, user saves the object which
             invokes this SOA operation.
             

Dependencies:

             getStaticTableData
             

Teamcenter Component:

             Contract Data Management - Provides functionality to save or retrieve Event List
             data for Data Requirement Item Revision
             
        :param StaticTableInfo: 
                         This represents static table object that needs to be created/updated.
             
        :param RowProperties: 
                         Vector of RowData where each element is of type TableProperties
             
        :return: (This list may be incomplete, and is subject to change without notice.)
        """
        ...
    def GetEventTypes(self, Input: list[EventObject]) -> EventTypesResponse:
        """    
             The getEventTypes operation retrieves the valid Auditable and Subscribable
             events for each of the businessObject in the input EventObject
             vector. When an event is auditable, you can audit actions on Teamcenter objects when
             that event happens on the businessObject. When an event is Subscribable, that means
             subscriptions can be created for that event. Partial failures, if any, will be returned
             in the serviceData.
             

Teamcenter Component:

             Subscription Management - Application in Teamcenter that allows users to subscribe
             to a certain events on business objects.
             
        :param Input: 
                         A vector of <font face="courier" height="10">EventObject</font> structure consisting
                         of list of Business Objects, for which the valid auditable and subscribable events
                         are to be fetched.
             
        :return: Output is a vector of eventsOutput structures packaged in a custom response. Partial
             failures will be returned in the ServiceData as a map of client id to error message.
        """
        ...
    def PostEvent(self, Input: list[PostEventObjectProperties], EventTypeName: str) -> PostEventResponse:
        """    
             This operation will post an event for each of the Teamcenter business objects in
             the input list, with all the supplied information: secondaryObject,
             properties to be logged, and the error details. . Partial failures will be returned
             in the serviceData.
             

Use Cases:

             Most events are posted by Teamcenter server logic. Use this operation to make an
             event known only to your client code recorded in Audit Manager or supported by Subscription
             Manager.
             
Use Case1: Auditing events
             
             This operation helps auditing Teamcenter objects history by logging audit records
             when event eventTypeName occurs on primaryObject.
             

When site preference TC_audit_manager is set to ON and no Audit Definition
             exists for object type primaryObject and the eventTypeName, no audit records will
             be logged. Audit Definitions are Audit Manager Application configurations and can
             be viewed in Audit Manager Application.
             
When site preference TC_audit_manager is set to ON and Audit Definition
             exists for object type primaryObject and the eventTypeName, audit records will be
             logged with all the information provided in the structure PostEventObjectProperties
             
No audit records are written when preference TC_audit_manager is
             set to OFF or if the event posted is not defined as Auditable.
             




             Use Case2: Subscription Notifications    
             
             the site preference TC_subscription is set to ON , users can create subscriptions
             for notifications for certain events on Teamcenter Objects  The event posted must
             be described as subscribable and there should also exist an associated subscription
             object for the notification to occur.
             

Teamcenter Component:

             Subscription Management - Application in Teamcenter that allows users to subscribe
             to a certain events on business objects.
             
        :param Input: 
                         A vector of <font face="courier" height="10">ObjectProperties</font> structure. Each
                         structure consists of Primary Business Object, a manadatory parameter, on which event
                         has occurred, any secondary object to post its information, along with any additional
                         properties and the values and error code while performing the event.
             
        :param EventTypeName: 
                         Name of the event. This is a mandatory parameter and should be a valid auditable
                         or subscribable event mapped for the primary object. List of valid event types could
                         be found using command line utility: install_event_types
             
        :return: )
             if any. Success is defined by the return of ifailError for post event on each Business
             Object, primaryObject. If error is encountered while processing post event on elements
             in the set, it is reported as partial errors and processing continues for the remaining
             elements in the input set. Partial failures will be returned in the  serviceData.
        """
        ...
    def GetStaticTableData(self, StaticTable: Teamcenter.Soa.Client.Model.Strong.Fnd0StaticTable) -> StaticTableDataResponse:
        """    
             Returns a list of objects of type TableProperties which are associated with Fnd0StaticTable
             object. Fnd0StaticTable object has an attribute fnd0StaticTableData which
             is an array of TableProperties objects.  Any failures will be returned with
             the input object mapped to the error message in the ServiceData list of partial errors.
             

Use Cases:

             This operation is used to get the data for attribute fnd0StaticTableData of Fnd0StaticTable
             object. Attribute fhd0StaticTableData is an array of TableProperties objects. When
             user selects Cdm0DataReqItemRevision object, the attribute cdm0EventsList
             is displayed in the summary as well as on View/Edit Properties menu in RAC. The attribute
             cdm0EventsList is Typed Reference to Fnd0StaticTable object.
             

Dependencies:

             createOrUpdateStaticTableData
             

Teamcenter Component:

             Contract Data Management - Provides functionality to save or retrieve Event List
             data for Data Requirement Item Revision
             
        :param StaticTable: 
                         StaticTable
             
        :return: 
        """
        ...

