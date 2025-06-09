import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CancelInput:
    """
    The input for the cancel operation. It contains the request object to be
canceled.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique client identifier. This is a unique string supplied by the caller. This
            ID
            
            is used to identify return data elements and partial errors associated with this
            input structure.
            
"""
    Request: Teamcenter.Soa.Client.Model.Strong.SRP0GnSrvRequestRevision
    """
            The request object to be canceled. This object can be a Requested Activity,
            
            Primary Service Request or a Delegate Service Request.
            
"""

class CancelOut:
    """
    The request that was cancelled
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique client identifier"""
    Output: Teamcenter.Soa.Client.Model.Strong.SRP0GnSrvRequestRevision
    """the cancelled request"""

class CancelResponse:
    """
    
Structure containing vector of canceled objects and service data containing
partial
errors.
    """
    def __init__(self, ) -> None: ...
    Output: list[CancelOut]
    """Vector of cancelled objects"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted,or updated
            by the Service, plain objects, and error information.
            """

class DelegateInput:
    """
    Input for the delegate requested activities operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique client identifier"""
    PrimaryServiceRequest: Teamcenter.Soa.Client.Model.Strong.SRP0GnSrvRequestRevision
    """The primary service request"""
    NewDelegate: bool
    """Set to true if a new delegate is to be created"""
    DelegateStringProps: System.Collections.Hashtable
    """String properties for the new delegate service request"""
    DelegateDateProps: System.Collections.Hashtable
    """Date properties for the delegate service request"""
    DelegateContact: Teamcenter.Soa.Client.Model.ModelObject
    """Company contact object"""
    DelegateLocation: Teamcenter.Soa.Client.Model.ModelObject
    """Company Location object"""
    PerformsServiceRequest: Teamcenter.Soa.Client.Model.Strong.SRP0SrvRequestRevision
    """The service request to perform the requested activities"""
    RequestedActivities: list[Teamcenter.Soa.Client.Model.Strong.SRP0RqstActivityRevision]
    """The requested activities to delegate"""

class DelegateOut:
    """
    
Structure containing a list of output objects representing delegate service
requests
that were created.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    NewPerforms: Teamcenter.Soa.Client.Model.Strong.SRP0SrvRequestRevision
    """New Performs Service Requests"""
    CurrPerforms: list[Teamcenter.Soa.Client.Model.Strong.SRP0GnSrvRequestRevision]
    """This is a vector of service request that have been modified"""

class DelegateResponse:
    """
    
Structure containing a list of delegate service request objects and service data
containing partial errors.
    """
    def __init__(self, ) -> None: ...
    Output: list[DelegateOut]
    """Vector of delegate out objects"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted,or updated
            by the Service, plain objects, and error information.
            """

class GetSvcOfferingOrCatalogInput:
    """
    the input for the getServiceOfferingOrServiceCatalogObjs operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique client identifier"""
    QueryProps: System.Collections.Hashtable
    """String properties for the service offering query. Ex: "prop_name" = "prop_value""""
    PhysicalPart: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision
    """
            This is physical part to get the service catalogs from.If the vector of service catalogs
            is empty, this is used to find the service catalogs.
            """
    SvcCatalogs: list[Teamcenter.Soa.Client.Model.Strong.SRP0ServiceCatalog]
    """
            This is a vector of service catalogs to get the service offerings from. If this is
            empty then the operation will get the service catalogs from the physical part.
            """

class GetSvcOfferingOrCatalogOut:
    """
    The service catalogs or service offerings
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    SvcOfferings: list[Teamcenter.Soa.Client.Model.Strong.SRP0ServiceOffering]
    """This is a vector of service offerings"""
    SvcCatalogs: list[Teamcenter.Soa.Client.Model.Strong.SRP0ServiceCatalog]
    """This is a vector of service catalogs"""

class GetSvcOfferingOrCatalogResponse:
    """
    
GetSvcOfferingOrCatalogResponse structure
            contains a list of Service Catalog and Offering objects. It also
contains standard
            Service Data that contain partial errors.
    """
    def __init__(self, ) -> None: ...
    Output: list[GetSvcOfferingOrCatalogOut]
    """Vector of GetSvcOfferingOrCatalogOut objects"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted,or updated
            by the Service, plain objects, and error information.
            """

class QualifyInput:
    """
    Input for the qualifyActivity function
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique client identifier"""
    Requalify: bool
    """If set to true, requalify the requested activity."""
    RequestedActivity: Teamcenter.Soa.Client.Model.Strong.SRP0RqstActivityRevision
    """RequestedActivity"""
    StringProps: System.Collections.Hashtable
    """String properties for requested activity"""
    DateProps: System.Collections.Hashtable
    """Date properties"""
    ProductPhysicalPart: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision
    """Product Physical Element"""
    ServiceOfferings: list[Teamcenter.Soa.Client.Model.Strong.SRP0ServiceOffering]
    """A vector of service offerings"""
    ServiceRequest: Teamcenter.Soa.Client.Model.Strong.SRP0GnSrvRequestRevision
    """Service Request"""

class QualifyOut:
    """
    Vector of output objects representing objects that were created
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    Output: list[Teamcenter.Soa.Client.Model.Strong.SRP0RqstActivityRevision]
    """Vector of tags representing objects that were created"""

class QualifyResponse:
    """
    
Structure containing a vector of Requested Activity objects and Service Data
that
contains partial errors.
    """
    def __init__(self, ) -> None: ...
    Output: list[QualifyOut]
    """Vector of output objects representing objects that were created"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the Service, plain objects, and error information.
            """

class TimeCostInput:
    """
    Input for the time and cost rollup operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique client identifier. This is a unique string supplied by the caller. This
            ID
            
            is used to identify return data elements and partial errors associated with this
            input structure.
            
"""
    ServiceRequest: Teamcenter.Soa.Client.Model.Strong.SRP0SrvRequestRevision
    """
            The Service Request object whose time and cost information needs to be rolled
            
            up from its related Requested Activity(s).
            
"""

class TimeCostOut:
    """
    A map of time and cost rollup values
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique client identifier"""
    ServiceRequest: Teamcenter.Soa.Client.Model.Strong.SRP0SrvRequestRevision
    """Service Request"""
    TimeCostProps: System.Collections.Hashtable
    """The time and cost properties with rolled up values"""

class TimeCostResponse:
    """
    
Vector of time and cost objects representing time and cost that was rolled up to
the service request.
    """
    def __init__(self, ) -> None: ...
    Output: list[TimeCostOut]
    """Vector of time and cost values"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted,or updated
            by the Service, plain objects, and error information.
            """

class ServiceRequest:
    """
    Interface ServiceRequest
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CancelRequest(self, Input: list[CancelInput]) -> CancelResponse:
        """    
             This operation cancels a Primary Service Request and its associated Requested Activity(s)
             for each CancelInput supplied. The input
             can be a Primary Service Request, Delegate Service Request(s) or any of its Requested
             Activity(s) associated with the Primary Service Request through the Includes relationship.
             If the input parameter is a Primary Service Request, then the service request is
             canceled and the Closure attribute is set to Canceled state. Any Requested
             Activity(s) or Delegate Service Request(s) that are in the Requested state
             will also be automatically Canceled. The input parameter can also be a Requested
             Activity or a Delegate Service Request in which case, the Closure attribute is set
             to Canceled for the respective input supplied. If a requested activity is
             Open and is delegated to a service request, an attempt to cancel the Delegate
             Service Request will throw an appropriate warning message to the user using error
             code 246512. An attempt to cancel an object that is already canceled throws
             an appropriate warning message telling the user that the object is already canceled.
             A canceled Requested Activity cannot be delegated to a Service Request based on the
             condition SRP0IsRequestedActivityDelegateable. Similarly, a new Requested
             Activity cannot be created for a canceled Primary Service Request based on the condition
             SRP0IsRequestedActivityCreatable.
             

Use Cases:

Use case 1: Cancel Requested Activity

             This use case allows the user to cancel a Requested Activity based on the condition
             SRP0IsRequestedActivityCancelable where the Closure is Open and the
             Maturity is not in Executing state. The Closure will be set to Canceled.
             
Use case 2: Cancel Service Request

             This use case allows the user to cancel a Service Request based on the condition
             SRP0IsServiceRequestCancelable. The Closure attribute will be set to Canceled.
             A Service Request cannot be canceled if it is Executing. If a Service Request is
             canceled, any Requested Activities or Service Requests that are in the Requested
             State will also be canceled.
             


Teamcenter Component:

             Service Request Processing - This Component is intended to identify all Operations
             and Services under Service Request Processing.
             
        :param Input: 

        :return: 
        """
        ...
    def DelegateRequestedActivity(self, Input: list[DelegateInput]) -> DelegateResponse:
        """    
             Operation that delegates requested activities to new or existing service requests.
             

Teamcenter Component:

             Service Request Processing - This Component is intended to identify all Operations
             and Services under Service Request Processing.
             
        :param Input: 
                         input
             
        :return: returns delegate response
        """
        ...
    def GetSvcOfferingOrCatalogObjs(self, Input: list[GetSvcOfferingOrCatalogInput]) -> GetSvcOfferingOrCatalogResponse:
        """    
             This operation is used to get the service offerings or service catalogs that are
             related to the neutral part that a physical part is realized from.
             

Use Cases:

Retrieve Available Service Offerings

             Based on the physical part identified for the Requested Activity as the Product Physical
             Part, the available Service Catalogs and Service Offerings are retrieved and made
             available for the user to select.
             


Teamcenter Component:

             Service Request Processing - This Component is intended to identify all Operations
             and Services under Service Request Processing.
             
        :param Input: 
                         The physical part that is realized from the neutral part that the Service Catalogs
                         are related to.
             
        :return: structures
             and a standard Service Data.
        """
        ...
    def QualifyActivity(self, Input: list[QualifyInput]) -> QualifyResponse:
        """    
             Operation that creates new requested activities base on service offerings.
             

Teamcenter Component:

             Service Request Processing - This Component is intended to identify all Operations
             and Services under Service Request Processing.
             
        :param Input: 
                         input
             
        :return: Returns
        """
        ...
    def TimeAndCostRollup(self, Input: list[TimeCostInput]) -> TimeCostResponse:
        """    
             This operation rolls up time and cost information from the Requested Activity(s)
             to the Service Request. The input parameter is a Service Request and when a user
             edits or updates the estimated or actual time and cost information for a Requested
             Activity, the values get rolled up to the parent Service Request. A user logged in
             as an administrator can restrict certain users from being able to create the time
             and cost information.
             

             If the Requested Activity is catalog based and if the related Service Offering has
             estimated time and cost information, those estimated values are copied to the estimated
             time and cost values for the requested activity. These values can still be modified
             if required by the user. If the Requested Activity is noncatalog based, no initial
             cost estimates are created and a value can be entered if required. The time and cost
             for the Primary Service Request is automatically rolled up from the time and cost
             for all its related Requested Activity(s) in the Includes Activity folder.
             The time and cost for a Delegate Service Request is rolled up from its related Requested
             Activity(s) located in the Performs folder. The time and cost for Requested
             Activity(s) are not rolled up if they have the following values set for any of the
             properties as illustrated below:
             

Closure Value:Canceled
             
Maturity Value:Superseded
             
Disposition Value:Disapproved
             


             A user can change the settings for these properties value by modifying the condition
             SRP0IsRequestedActivityInvalidforRollup.
             

Use Cases:

Use Case1: Edit Actual Time and Cost of Requested Activity

             A user is allowed to enter the actual time and cost details for a Requested Activity.
             The ability to update time and cost information is controlled independently of the
             Requested Activity and limited to members of a specific group.
             
Use Case 2: Edit Estimated Time and Cost of Requested Activity

             This operation allows the user to indicate an estimated time and cost for a Requested
             Activity. If the Requested Activity was created from a Service Offering, the initial
             time and cost estimate should be copied from the Service Offering to the Requested
             Activity.
             
Use Case 3: Rollup Requested Activity Actuals to Service Request

             This use case is performed by the system. If the user updates an actual time or cost
             value on a Requested Activity, the system rolls that value up to the parent Service
             Request(s). The Primary Service Request should have a rollup of all of the activities
             that were requested. The Delegate Request should include all of the requested activities
             that are performed as part of that Service Request.
             
Use Case 4: Rollup Requested Activity Estimates to Service Request

             This use case is performed by the system. If a user updates an estimated time or
             cost value on a Requested Activity, the system rolls up that value up to the parent
             Service Request(s).
             
Use Case 5: View Time and Cost Information
             
A specific group of users are provided with the ability to view the time and
             cost information of all Service Request and Requested Activities.
             


Teamcenter Component:

             Service Request Processing - This Component is intended to identify all Operations
             and Services under Service Request Processing.
             
        :param Input: 
                         Object that is a Service Request.
             
        :return: 
        """
        ...

