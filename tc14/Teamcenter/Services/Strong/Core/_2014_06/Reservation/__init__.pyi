import System
import Teamcenter.Soa.Client.Model
import typing

class Reservation:
    """
    Interface Reservation
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def BulkCancelCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation cancels a check-out for a set of previously checked-out business objects
             in bulk. The objects will be restored to the pre-check-out state. Only one user can
             perform a cancel check-out transaction on the object if the user has enough privilege
             on the object. This action may be applied to remote checked-out objects, and will
             cancel the check-out and records the cancel check-out transaction event. Cancel checkout
             is not supported for some of the business objects for e.g. - Item, BOMView,BOMViewRevision,
             Schedule.
             

Dependencies:

             bulkCheckout, checkout
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         A list of objects which are in the checked-out state.(e.g. Dataset, Item, ItemRevision
                         )
             
        :return: 
        """
        ...
    def BulkCheckin(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation checks-in a set of previously checked-out business objects in bulk.
             This operation takes care of all complex business logic involved to check-in passed
             in business objects. Each input object is verified that it is locally owned, site
             owned, and not transferred to another user after the checkout was performed. This
             operation validates precondition defined per type in COTS object and site customization
             and performs basic check-in. Dataset, ItemRevision and many other business object
             types have their own business logic for check-in. This operation calls underlying
             checkin method of those individual objects.
             

             Note: If the business object ItemRevision is checked out using reservation type "RES_RESERVE_BULK_WITH_DELAY_DEEP_COPY"
             and if the given object is not modified after it was checked out using this reservation
             type then the checkin opetation performed on this object will not increase the sequence
             number of the ItemRevision business object
             


Dependencies:

             bulkCheckout, checkout
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         A list of objects which are in the checked-out state.
             
        :return: 
        """
        ...
    def BulkCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Comment: str, ChangeId: str, ReservationType: int) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation checks out a set of business objects with given comment and, change
             identifier in bulk fashion. Only one user can perform a check-out transaction on
             the object. The user must have sufficient privilege on the object or the checkout
             will fail. This operation allows for remote check-out and records the check-out transaction
             event. In the case where the reservationType is RES_RESERVE_BULK_WITH_DELAY_DEEP_COPY,
             this operation checks out business objects without creating the backup copy of the
             reserved objects. The backup copy will be created on demand when the reserved object
             is modified. This operation is faster than the checkout operation.
             

Use Cases:

             The object can be reserved to gain exclusive rights so that no other user can modify
             it while the reserver is modifying the given object.
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         A list of business objects to be checked out.
             
        :param Comment: 
                         A comment describing the reason for the check-out. An empty string is allowed.
             
        :param ChangeId: 
                         The ID of the change. Empty string allowed.
             
        :param ReservationType: 
<ul>
<li type="disc">RES_EXCLUSIVE_RESERVE for checking out business objects  and create
                         with the backup copy of the reserved objects to  maintaining its their states before
                         the chekcout
                         </li>
<li type="disc">RES_RESERVE_BULK_WITH_DELAY_DEEP_COPY for bulk checking out business
                         objects without creating the backup copy of the reserved objects. maintaining its
                         state before the chekcout. The backup copy will be created on demand when the reserved
                         object is modified.  This reservation type is of checkout operation is faster than
                         the reservation type : one with "RES_EXCLUSIVE_RESERVE".
                         </li>
</ul>

        :return: 
        """
        ...

