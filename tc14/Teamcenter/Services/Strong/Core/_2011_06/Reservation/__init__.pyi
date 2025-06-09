import System
import Teamcenter.Soa.Client.Model
import typing

class OkToCheckoutResponse:
    """
    
            This structure contains the list and ServiceData
            objects. The list contains verdict true or false for passed in object indicating
            if object can be checked out or not. ServiceData
            contains error at index where it occurred for each input object.
            
    """
    def __init__(self, ) -> None: ...
    Verdict: list[bool]
    """
            A list indicating if the input business object can be checked out. "true"
            indicates the object may be checked out. "false" indicates the object may
            not be checked out.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains the partial errors for any objects for which the okToCheckout
            validation failed.
            """

class Reservation:
    """
    Interface Reservation
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def OkToCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> OkToCheckoutResponse:
        """    
             This operation determines whether or not the input objects may be checked out given
             the type of object, access rules, and current checkout state of the object.
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         The list of objects which should be validated for Checkout.
             
        :return: The possible partial error 32053 is returned if the object's type is not supported
             by the check out facility.
        """
        ...

