import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class Reservation:
    """
    Interface Reservation
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def TransferCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], UserId: Teamcenter.Soa.Client.Model.Strong.User) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation transfers the previously checked-out business objects to the user
             given from input. This operation takes care of all complex business logic involved
             in transfer checked-out based on passed in objects. Each input object is verified
             that it is valid for transferring its checkout.
             
             This operation validates precondition defined per type in COTS object and site customization
             before performing transfer checked-out objects to the target user. Dataset,
             ItemRevision and many other business object types have their own business
             logic for transfer check-out. This operation calls underlying transfer checkout method
             of those individual objects.
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         A list of the previously checked-out Teamcenter objects (e.g. <b>Dataset</b>, <b>Item</b>,
                         <b>ItemRevision</b> ) to transfer the checkout.
             
        :param UserId: 
                         The Teamcenter user id to who checked-out has to be transferred to.
             
        :return: 
        """
        ...

