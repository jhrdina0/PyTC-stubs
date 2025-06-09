import System
import Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest
import Teamcenter.Services.Strong.Svcrequest._2012_02.ServiceRequest
import Teamcenter.Soa.Client

class ServiceRequestRestBindingStub(ServiceRequestService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CancelRequest(self, Input: list[Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.CancelInput]) -> Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.CancelResponse: ...
    def DelegateRequestedActivity(self, Input: list[Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.DelegateInput]) -> Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.DelegateResponse: ...
    def GetSvcOfferingOrCatalogObjs(self, Input: list[Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.GetSvcOfferingOrCatalogInput]) -> Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.GetSvcOfferingOrCatalogResponse: ...
    def QualifyActivity(self, Input: list[Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.QualifyInput]) -> Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.QualifyResponse: ...
    def TimeAndCostRollup(self, Input: list[Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.TimeCostInput]) -> Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.TimeCostResponse: ...
    def DelegateRequestedActivity2(self, Input: list[Teamcenter.Services.Strong.Svcrequest._2012_02.ServiceRequest.DelegateRqstInput]) -> Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.DelegateResponse: ...
    def QualifyActivity2(self, Input: list[Teamcenter.Services.Strong.Svcrequest._2012_02.ServiceRequest.QualifyRqstInput]) -> Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.QualifyResponse: ...

class ServiceRequestService:
    """
    
            ServiceRequest service

Library Reference:

TcSoaSvcRequestStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ServiceRequestService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CancelRequest(self, Input: list[Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.CancelInput]) -> Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.CancelResponse:
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
    def DelegateRequestedActivity(self, Input: list[Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.DelegateInput]) -> Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.DelegateResponse:
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
    def GetSvcOfferingOrCatalogObjs(self, Input: list[Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.GetSvcOfferingOrCatalogInput]) -> Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.GetSvcOfferingOrCatalogResponse:
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
    def QualifyActivity(self, Input: list[Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.QualifyInput]) -> Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.QualifyResponse:
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
    def TimeAndCostRollup(self, Input: list[Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.TimeCostInput]) -> Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.TimeCostResponse:
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
    def DelegateRequestedActivity2(self, Input: list[Teamcenter.Services.Strong.Svcrequest._2012_02.ServiceRequest.DelegateRqstInput]) -> Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.DelegateResponse:
        """    
             This operation delegates Requested Activities to new or existing Service Requests.
             

Use Cases:

Use Case 1: Delegate Requested Activity to a new Service Request

             User delegates the Requested Activity to a delegated Service Request.
             
Use Case 2: Identify Service Request to address some Requested Activities

             User identifies an additional (delegated) Service Request to address some of the
             Requested Activities from the original Service Request.  Requested Activities from
             the first Service Request can be added to the additional Service Request.  During
             this operation, the user will be presented with an opportunity to identify the Requested
             Activities to be moved to the identified Service Request.
             


Teamcenter Component:

             Service Request Processing - This Component is intended to identify all Operations
             and Services under Service Request Processing.
             
        :param Input: 
                         The container of objects that are used to create Requested Activities.
             
        :return: The container of Delegate Service Requests that were created.
        """
        ...
    def QualifyActivity2(self, Input: list[Teamcenter.Services.Strong.Svcrequest._2012_02.ServiceRequest.QualifyRqstInput]) -> Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.QualifyResponse:
        """    
             This Operation qualifies and creates new Requested Activities.  Processing includes
             the creation of relations between the Requested Activity and the parent Service Request,
             the Product Physical Part, any selected Service Offerings and Activity Cost.
             

Use Cases:

Create and Relate Requested Activity to Service Request

             This use case allows the user to create a Requested Activity from the perspective
             of a Service Request.  A Requested Activity is created and the relationship between
             the Requested Activity and the Service Request is also created.
             
Create NonCatalog Requested Activity

             This use case allows a user to create a Requested Activity without an identified
             Service Offering.  The user identifies one of the Product physical parts from the
             parent Service Request for which the Requested Activity will be created.  If only
             one Product physical part is identified on the parent Service Request, then it is
             automatically designated as the Product physical part for the Requested Activity.
             
Create Relationship between Requested Activity and Service Offering

             The system creates the relationship between the Requested Activity and the Service
             Offering that identifies the standard service to be performed.
             
Create Requested Activity

             This use case allows the user to create the specific Requested Activities that identify
             the complete requested work scope of the Service Request.  Each Requested Activity
             identifies the work to be done, the Product Physical part, and optionally the impacted
             and problem physical part.  A Requested Activity can only be for one Product Physical
             Part.
             
Create Requested Activity based on Service Offering

             User creates a Requested Activity based on a Service Offering contained within the
             Service Catalog related to the Product Neutral Part.  The user identifies one of
             the Product physical parts from the parent Service Request for which the Requested
             Activity will be created.  If only one Product physical part is identified on the
             parent Service Request, then it is automatically designated as the Product physical
             part for the Requested Activity.  The user is presented with the available Service
             Offering for that Product Physical Part and selects the appropriate ones based on
             their need.  A Requested Activity is created for every Service Offering selected.
             The Requested Activity is related to both the Product Physical Part, and the Service
             Offering.  The narrative and initial time and cost estimates are copied from the
             Service Offering to the Requested Activity.
             
Requalify Requested Activity

             This use case allows the user to requalify the Service Offering that a Requested
             Activity is related to, or add a Service Offering if the Requested Activity is not
             related to a Service Offering.  There could be multiple Service Offerings that are
             identified as the services required to fulfill a particular Requested Activity. The
             system will create additional Requested Activities as necessary to accommodate the
             additional catalog based requests.  The user will be asked whether or not to update
             the Requested Activity with the narrative and time and cost estimates from the Service
             Offering.
             
Retrieve Available Service Offerings

             The available Service Offerings are retrieved and available to the user based on
             the physical part identified for the Requested Activity as the Product Physical Part.
             


Teamcenter Component:

             Service Request Processing - This Component is intended to identify all Operations
             and Services under Service Request Processing.
             
        :param Input: 
                         The container of objects that are used to create Requested Activities.
             
        :return: The container of Requested Activities that were created.
        """
        ...

