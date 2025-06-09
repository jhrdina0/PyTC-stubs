import Teamcenter.Soa.Client.Model
import typing

class LicAdminInput:
    """
    Key pair used to perform a licensing action.
    """
    def __init__(self, ) -> None: ...
    FeatureKey: str
    """The product as listed in the license file (e.g. teamcenter_author)."""
    LicensingAction: str

class Session:
    """
    Interface Session
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def LicenseAdmin(self, LicAdminInput: list[LicAdminInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation provides licensing related operations such as check-out and check-in
             of a license feature key.
             

Teamcenter Component:

             Licensing - Provides the capability to assign and monitor licenses such that the
             users (an individual; a system; a module etc.) of teamcenter can be limited to use
             the capabilities that they have privileges for
             
        :param LicAdminInput: 
                         A list of feature key and action pairs. This allows multiple license keys to be checked
                         out in one service operation call.
             
        :return: 
        """
        ...

