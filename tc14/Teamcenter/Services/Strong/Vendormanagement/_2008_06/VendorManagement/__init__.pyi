import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ChangedPartStatus:
    """
    
This structure contains the status of VendorPart objects and remarks from
the operation.
    """
    def __init__(self, ) -> None: ...
    OldPartStr: str
    """Id of old VendorPart."""
    NewPartStr: str
    """Id of new VendorPart created."""
    Notes: str
    """
            Remarks (notes) corresponding to the each change Vendor operation. e.g. Success,
            Failure.
            """

class ChangeVendorInputInfo:
    """
    
Input structure containing Vendor to change, VendorPart to change and
destination new Vendor.
    """
    def __init__(self, ) -> None: ...
    VendorToChange: Teamcenter.Soa.Client.Model.Strong.Vendor
    """
            This is Object pointing to the Vendor to change. If this input is specified,
            all the related VendorPart objects are processed for change Vendor
            operation. This input takes precedence over VendorPart objects input.
            """
    VendorParts: list[Teamcenter.Soa.Client.Model.Strong.Item]
    """VendorPart objects to be processed for change Vendor operation."""
    NewVendor: Teamcenter.Soa.Client.Model.Strong.Vendor
    """The new Vendor to be attached to the part."""

class ChangeVendorResponse:
    """
    
Response structure for the changeVendor operation
contains statuses member. It is a list of ChangeVendorStatus
structures.
    """
    def __init__(self, ) -> None: ...
    Statuses: list[ChangeVendorStatus]
    """
            List of ChangeVendorStatus structures. There
            is an entry per entry in input structure.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard ServiceData structure. It contains
            partial errors and failures along with the clientIds.
            """

class ChangeVendorStatus:
    """
    
This is the structure containing a list of structures for each VendorPart
statuses.
    """
    def __init__(self, ) -> None: ...
    ChangedStatus: list[ChangedPartStatus]
    """This is the structure containing a list of statuses for change Vendor operation."""

class GetVendorPartsWithSelRuleInputInfo:
    """
    A structure of CommercialPartRevision and condition name.
    """
    def __init__(self, ) -> None: ...
    ComPartRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            Selected CommercialPartRevision object from BOM. This revision is used for
            searching the related VendorPart objects based on selection rule.
            """
    ConditionName: str
    """
            The name of the condition in Teamcenter which is used as a selection rule while finding
            the VendorPart objects. The service operation will try and search for a valid
            selection rule based on the condition name. If this input is given as an empty string,
            the default selection rule is used which is governed by the preference VMS_vendor_part_selection_rule.
            """

class GetVendorPartsWithSelRuleResponse:
    """
    
The response structure containing VendorPartData
structure which in turn stores information about found VendorPart objects.
    """
    def __init__(self, ) -> None: ...
    PartData: list[VendorPartData]
    """
            The output structure, which is essentially a list of VendorPartData
            structures returned. Each of them will contain relation and part information for
            each VendorPart found.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard Teamcenter service response data."""

class VendorPartAndRel:
    """
    Structure containing a VendorPart object and its relation object to a
CommercialPart.
    """
    def __init__(self, ) -> None: ...
    VendorPart: Teamcenter.Soa.Client.Model.Strong.Item
    """VendorPart object."""
    VmRepresentRel: Teamcenter.Soa.Client.Model.Strong.ImanRelation
    """
            Each of these VendorPart objects are related to the input CommercialPartRevision
            with a relation called VMRepresents. This object represents an instance of
            that relation.
            """

class VendorPartData:
    """
    
Structure containing a filtered list of relation and part information for each
VendorPart
objects.
    """
    def __init__(self, ) -> None: ...
    PartAndRel: list[VendorPartAndRel]
    """
            It is the vector of VendorPartAndRel objects
            holding the information of individual VendorPart objects and relation of input
            CommercialPartRevision with each of them.
            """

class VendorManagement:
    """
    Interface VendorManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ChangeVendor(self, Input: list[ChangeVendorInputInfo]) -> ChangeVendorResponse:
        """    
             This service operation can be called on either a VendorPart or a Vendor.
             

             For VendorPart: It creates a new copy of VendorPart with the new Vendor
             information. This newly created VendorPart is associated to the new revision
             of the CommercialPart of the old VendorPart.
             
             For Vendor: All VendorPart objects related with given Vendor
             are taken into consideration. Each of these VendorPart objects are then processed
             as mentioned above.
             

             This operation shows old and new part id with the information of the success or failure.
             

Typical Client Usage: 

             Typical usage involves two Vendor objects and a VendorPart created with either one
             of them.
             

VendorManagementService vmService =
             
             VendorManagementService.getService(session);
             
             ChangeVendorInputInfo[]chanProps = new ChangeVendorInputInfo[1];
             
             ChangeVendorInputInfo changeProps = new ChangeVendorInputInfo();
             
             ChangeVendorResponse response = null;
             
             changeProps.newVendor = (TCComponentVendor)newVendor;
             
             changeProps.vendorParts=selectedParts;
             
             chanProps[0] = changeProps;
             

             response = vmService.changeVendor( chanProps );



Teamcenter Component:

             Vendor Management - Solution template that provides capability to manage vendor relation
             information.
             
        :param Input: 
<ul>
<li type="disc">vendorToChangeÂ Â Â Â This is Object pointing to
                         the Vendor to change. If this input is specified, all the related VendorPart objects
                         are processed for change Vendor operation. This input takes precedence over VendorPart
                         objects input.
                         </li>
<li type="disc">vendorPartsÂ Â Â Â VendorPart objects to be processed
                         for change Vendor operation.
                         </li>
<li type="disc">newVendorÂ Â Â Â The new Vendor to be attached to
                         the part.
                         </li>
</ul>

        :return: 
        """
        ...
    def GetVendorPartsWithSelRule(self, Input: list[GetVendorPartsWithSelRuleInputInfo]) -> GetVendorPartsWithSelRuleResponse:
        """    
             This service operation returns VendorPart objects  associated with the given
             CommercialPartRevision  based on the selection rule set for the VendorPart
             objects in Structure Manager. If no value is given for the selection rule, it is
             read  from the preference VMS_vendor_part_selection_rule. Typical OOTB selection
             rules provided are showAllVendorParts and showPreferredVendorPartsOnly.
             First selection rule is to show all related VendorPart objects and later
             is used to show the related VendorPart objects carrying preferred status.
             

Teamcenter Component:

             Vendor Management - Solution template that provides capability to manage vendor relation
             information.
             
        :param Input: 
                         List of <font face="courier" height="10">GetVendorPartsWithSelRuleInputInfo</font>
                         structures containing <b>CommercialPartRevision</b> objects to be used as input to
                         find related <b>VendorPart</b> objects.  It also contains condition name string.
             
        :return: objects.
        """
        ...

