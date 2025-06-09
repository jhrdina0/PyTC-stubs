import System
import System.Collections
import Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest
import Teamcenter.Soa.Client.Model.Strong
import typing

class SvcRqCreateInput:
    """
    Service Request create input
    """
    def __init__(self, ) -> None: ...
    StringProps: System.Collections.Hashtable
    """Property string name/value"""
    StringArrayProps: System.Collections.Hashtable
    """Property string array name/value"""
    BoolProps: System.Collections.Hashtable
    """Property boolean name/value"""
    BoolArrayProps: System.Collections.Hashtable
    """Property boolean array name/value"""
    DoubleProps: System.Collections.Hashtable
    """Property double name/value"""
    DoubleArrayProps: System.Collections.Hashtable
    """Property double array name/value"""
    DateProps: System.Collections.Hashtable
    """Property date name/value"""
    DateArrayProps: System.Collections.Hashtable
    """Property date array name/value"""
    IntProps: System.Collections.Hashtable
    """Property integer name/value"""
    IntArrayProps: System.Collections.Hashtable
    """Property integer array name/value"""
    TagProps: System.Collections.Hashtable
    """Property reference name/value"""
    TagArrayProps: System.Collections.Hashtable
    """Property reference array name/value"""
    FloatProps: System.Collections.Hashtable
    """attribute float name/value"""
    FloatArrayProps: System.Collections.Hashtable
    """attribute float array name/value"""

class DelegateRqstInput:
    """
    input for the delegate requested activities operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id"""
    PrimaryServiceRequest: Teamcenter.Soa.Client.Model.Strong.SRP0GnSrvRequestRevision
    """Primary Service Request"""
    NewDelegate: bool
    """New delegate request"""
    ItemData: SvcRqCreateInput
    """Item object"""
    ItemRevData: SvcRqCreateInput
    """Item revision object"""
    BoName: str
    """Business Object Name"""
    PerformsServiceRequest: Teamcenter.Soa.Client.Model.Strong.SRP0SrvRequestRevision
    """Perform Service Request"""
    RequestedActivities: list[Teamcenter.Soa.Client.Model.Strong.SRP0RqstActivityRevision]
    """Requested Activity Revision array"""

class QualifyRqstInput:
    """
    Requested Activity create input structure
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    Requalify: bool
    """If set to true, re qualify the Requested Activity."""
    BoName: str
    """Name of the business object being created"""
    ItemData: SvcRqCreateInput
    """item Data for parent Service Request, Product Physical Part and Service Offerings"""
    ItemRevData: SvcRqCreateInput
    """
            item Revision Data for parent Service Request, Product Physical Part and Service
            Offerings
            """

class ServiceRequest:
    """
    Interface ServiceRequest
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def DelegateRequestedActivity2(self, Input: list[DelegateRqstInput]) -> Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.DelegateResponse:
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
    def QualifyActivity2(self, Input: list[QualifyRqstInput]) -> Teamcenter.Services.Strong.Svcrequest._2010_04.ServiceRequest.QualifyResponse:
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

