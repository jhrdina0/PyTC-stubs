import System
import Teamcenter.Soa.Client.Model
import typing

class GetReservationHistoryResponse:
    """
    GetReservationHistoryResponse
    """
    def __init__(self, ) -> None: ...
    Histories: list[ReservationHistory]
    """Reservation history."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Objects which are queried successfully are added to the ServiceData plain list."""

class ReservationHistory:
    """
    Reservation history.
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """Object of reservation history."""
    Events: list[ReservationHistoryEvent]
    """Sequence of history events, earliest first."""

class ReservationHistoryEvent:
    """
    Single event in reservation history.
    """
    def __init__(self, ) -> None: ...
    DateTime: str
    """Date and time of event."""
    User: str
    """User name."""
    Activity: str
    """Event type.  "Check-Out"/"Check-In"/"Cancel Check-Out"."""
    ChangeId: str
    """change id as provided during checkout operation."""
    Comment: str
    """User comment"""

class Reservation:
    """
    Interface Reservation
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CancelCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation cancels a check-out for a set of previously checked-out business objects.
             The objects will be restored to the pre-check-out state. Only one user can perform
             a cancel check-out transaction on the object if the user has enough privilege on
             the object.  This action may be applied to remote checked out objects, and will cancel
             the check-out and records the cancel check-out transaction event. Cancel checkout
             is not supported for some of the business objects for e.g. - Item, BOMView,BOMViewRevision,
             Schedule.
             

Dependencies:

             checkout
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         A list of objects to be canceled for previously check-out.
             
        :return: 
        """
        ...
    def Checkin(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation checks-in a set of previously checked-out business objects. This operation
             takes care of all complex business logic involved to check-in passed in business
             objects.  Each input object is verified that it is locally owned, site owned, and
             not transferred to another user after the checkout was performed. This operation
             validates precondition defined per type in COTS object and site customization and
             performs basic check-in. Dataset, ItemRevision and many other business
             object types have their own business logic for check-in. This operation calls underlying
             checkin method of those individual objects.
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         Set of previously checked-out valid business objects. (e.g. <b>Dataset</b>, <b>Item</b>,
                         <b>ItemRevision</b> )
             
        :return: 
        """
        ...
    def Checkout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Comment: str, ChangeId: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation checks  out a set of business objects with given comment and change
             identifier. Only one user can perform a check-out transaction on the object. The
             user must have sufficient  privilege on the object or the check out will fail. This
             operation allows for remote check-out and records the check-out transaction event.
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         A list of business objects to be checked out.
             
        :param Comment: 
                         A comment describing the reason for the check-out.  An empty string is allowed.
             
        :param ChangeId: 
                         A string value to identify the change.  Empty string allowed.
             
        :return: 
        """
        ...
    def GetReservationHistory(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetReservationHistoryResponse:
        """    
             This operation gets the reservation history for a set of business objects, such as
             Dataset, Item, ItemRevision and many other business object types.
             An object which has never been checked out will have a valid reservation history
             with an empty sequence of events.
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         A list of business objects to query for reservation history.
             
        :return: 
        """
        ...

