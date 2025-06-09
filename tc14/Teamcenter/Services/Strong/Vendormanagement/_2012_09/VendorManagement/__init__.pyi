import Teamcenter.Soa.Client.Model
import typing

class VendorRoleData:
    """
    This is the structure containing VendorRole information.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify the Partial Errors
            associated with this VendorRoleData input.
            """
    Description: str
    """Description of the object to be created."""
    RoleType: str
    """VendorRole type, it shall be Manufacturer,Supplier or Distributor"""
    Remove: bool
    """Flag to indicate VendorRole is to be added or removed."""

class VendorManagement:
    """
    Interface VendorManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddRemoveVendorRoles(self, VendorRoles: list[VendorRoleData], VendorRevRef: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation adds or removes set of roles to/from a VendorRevision. Typically
             a role can be assigned to a VendorRevision by adding a role form with different
             role specific information. OOTB VendorRevision can be assigned with 3 roles
             namely Distributor, Supplier and Manufacturer. All these role
             forms contain information about the Vendor based on the type of the role.
             Similarly a role can be revoked from a VendorRevision. When a Vendor
             is revised, the new revision inherits all the assigned roles to the previous VendorRevision.
             

Teamcenter Component:

             Vendor Management - Solution template that provides capability to manage vendor relation
             information.
             
        :param VendorRoles: 
                         It is a list of <font face="courier" height="10">VendorRoleData</font> structures
                         meant to hold data for <b>VendorRole</b> objects to be processed.
             
        :param VendorRevRef: 
                         Reference to the <b>VendorRevision</b> object in the context of which these roles
                         are to be processed.
             
        :return: 
        """
        ...

