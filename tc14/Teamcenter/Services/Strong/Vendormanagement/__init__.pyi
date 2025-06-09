import System
import Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement
import Teamcenter.Services.Strong.Vendormanagement._2008_06.VendorManagement
import Teamcenter.Services.Strong.Vendormanagement._2012_02.VendorManagement
import Teamcenter.Services.Strong.Vendormanagement._2012_09.VendorManagement
import Teamcenter.Services.Strong.Vendormanagement._2016_09.VendorManagement
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class VendorManagementRestBindingStub(VendorManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateOrUpdateBidPackages(self, Properties: list[Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.BidPackageProps], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.CreateBidPacksResponse: ...
    def CreateOrUpdateLineItems(self, Properties: list[Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.LineItemProps], BidPackage: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateOrUpdateVendorParts(self, Properties: list[Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.VendorPartProperties], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.CreateVendorPartsResponse: ...
    def CreateOrUpdateVendors(self, Properties: list[Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.VendorProperties], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.CreateVendorsResponse: ...
    def DeleteLineItems(self, Input: list[Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.LineItemProps], BidPackage: Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.BidPackageProps) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteVendorRoles(self, Input: list[Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.VendorProperties]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteVendors(self, Input: list[Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.VendorProperties]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ChangeVendor(self, Input: list[Teamcenter.Services.Strong.Vendormanagement._2008_06.VendorManagement.ChangeVendorInputInfo]) -> Teamcenter.Services.Strong.Vendormanagement._2008_06.VendorManagement.ChangeVendorResponse: ...
    def GetVendorPartsWithSelRule(self, Input: list[Teamcenter.Services.Strong.Vendormanagement._2008_06.VendorManagement.GetVendorPartsWithSelRuleInputInfo]) -> Teamcenter.Services.Strong.Vendormanagement._2008_06.VendorManagement.GetVendorPartsWithSelRuleResponse: ...
    def CreateOrUpdateLineItemsWithType(self, Properties: list[Teamcenter.Services.Strong.Vendormanagement._2012_02.VendorManagement.LineItemPropertiesWithType], BidPackage: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def AddRemoveVendorRoles(self, VendorRoles: list[Teamcenter.Services.Strong.Vendormanagement._2012_09.VendorManagement.VendorRoleData], VendorRevRef: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateVendorParts(self, Properties: list[Teamcenter.Services.Strong.Vendormanagement._2016_09.VendorManagement.VendorPartProperties2]) -> Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.CreateVendorPartsResponse: ...

class VendorManagementService:
    """
    
            The Vendor Management service exposes operations that are used to
address Vendor
            Management related functionalities. Common uses of this service are
to create, modify
            and delete Vendor Management complex objects through different
operations.

            This service provides following Vendor Management use cases.

Create or update of BidPackage, Vendor Part, Vendor, BidPackage Line
            Item,

Deletion of BidPackage Line Item, Vendor,

Change Vendor of an existing Vendor Part,

Fetching Vendor Parts based on a selection rule,

Add or remove Vendor roles to or from a Vendor.

Library Reference:

TcSoaVendormanagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> VendorManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateOrUpdateBidPackages(self, Properties: list[Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.BidPackageProps], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.CreateBidPacksResponse:
        """    
             This service operation creates or updates a group of BidPackage, BidPackageRevision
             objects. This operation allows the user to find or create a set of BidPackage
             objects based on the input data. The service first tries to find the existence of
             the specified BidPackage or BidPackageRevision. If the specified BidPackage
             objects exist and any of the input attribute values differ from those already set,
             the BidPackage objects will be updated.
             

Teamcenter Component:

             Vendor Management - Solution template that provides capability to manage vendor relation
             information.
             
        :param Properties: 
                         A list of <font face="courier" height="10">BidPackageProps</font> structures which
                         are used to create or update <b>BidPackage</b> objects.
             
        :param Container: 
                         A parent object reference with which the created <b>BidPackage</b> objects will be
                         associated.
             
        :param RelationType: 
                         A relation name to be used for associating the <b>BidPackage</b> to its parent.
             
        :return: 
        """
        ...
    def CreateOrUpdateLineItems(self, Properties: list[Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.LineItemProps], BidPackage: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service operation creates or updates a group of BidPackageLineItem objects
             in the context of the mentioned BidPackage. This operation allows the user
             to find or create a set of BidPackageLineItem objects based on the input data.
             It first tries to find the existence of the specified BidPackageLineItem for
             the specified BidPackage. If the specified BidPackageLineItem is found,
             then its corresponding data will be updated. Otherwise, it will create the specified
             BidPackageLineItem and associate it to the specified BidPackageRevision.
             If the specified BidPackageLineItem objects exist and any of the input attribute
             values differ from those already set, the BidPackageLineItem objects will
             be updated.
             

             The operation is now deprecated. It is now replaced by Teamcenter::Soa::Vendormanagement::VendorManagement::createOrUpdateLineItemsWithType.


Teamcenter Component:

             Vendor Management - Solution template that provides capability to manage vendor relation
             information.
             
        :param Properties: 
                         A list of <font face="courier" height="10">LineItemProps</font> structures which
                         are used to create or update <b>BidPackageLineItem</b> objects.
             
        :param BidPackage: 
                         Reference to the <b>BidPackageRevision</b> object which will be used to associate
                         the created <b>BidPackageLineItem</b> objects.
             
        :return: 
        """
        ...
    def CreateOrUpdateVendorParts(self, Properties: list[Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.VendorPartProperties], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.CreateVendorPartsResponse:
        """    
             This service operation creates or updates a group of VendorPart objects or
             CommericialPart objects. The choice could be either CommercialPart
             or VendorPart only. This operation allows the user to update or create a set
             of CommercialPart objects or VendorPart objects based on the input
             data. It first tries to find the existence of the specified VendorPart or
             VendorPartRevision. If the specified parts are found, those parts will be
             updated with the specified values. Otherwise new parts will be created.
             
             The choice for type of part is given through data member type of VendorPartProperties structure. Only 'ManufacturerPart'
             and 'CommercialPart' are valid types.
             
Behavior for CommercialPart:  The service will create the CommercialPart
             and CommercialPartRevision and it will associate the created CommercialPart
             to the specified parent (container). It also associates the part to the specified
             Vendor object if given.
             
Behavior for ManufacturerPart:  The service will create the ManufacturerPart
             and ManufacturerPartRevision and will associate the part to the specified
             Vendor object. It also associates the created ManufacturerPart to the
             CommercialPart if specified.
             

Teamcenter Component:

             Vendor Management - Solution template that provides capability to manage vendor relation
             information.
             
        :param Properties: 

        :param Container: 
                         A parent object reference with which the created parts will be associated.
             
        :param RelationType: 
                         A relation name to be used for associating the <b>Vendor</b> to its parent.
             
        :return: 
        """
        ...
    def CreateOrUpdateVendors(self, Properties: list[Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.VendorProperties], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.CreateVendorsResponse:
        """    
             This service operation creates or updates a group of Vendor, VendorRevision
             Objects and VendorRole objects. It allows the user to update or create a set
             of Vendor objects based on the input data. The service first tries to find
             the existence of the specified Vendor or VendorRevision or VendorRole.
             If the service is able to find any of those objects, then those objects will be updated.
             If the service is not able to find those objects, then those objects will be created.
             If the Vendor exists, but VendorRevision does not, then VendorRevision
             and VendorRole (and VendorRole form) will be created. If the specified
             Vendor object and its associated objects exist and any of the input attribute
             values differ from those already set, the Vendor and its associated objects
             will be updated.
             

Teamcenter Component:

             Vendor Management - Solution template that provides capability to manage vendor relation
             information.
             
        :param Properties: 

        :param Container: 
                         A parent object reference to which the created <b>Vendor</b> objects will be associated.
             
        :param RelationType: 
                         A relation name to be used for associating the <b>Vendor</b> to its parent.
             
        :return: 
        """
        ...
    def DeleteLineItems(self, Input: list[Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.LineItemProps], BidPackage: Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.BidPackageProps) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service operation deletes the BidPackageLineItem objects associated with
             a specific BidPackageRevision. The BidPackageLineItem objects to be
             deleted are searched with their names provided through the input data structures
             LineItemProps. Hence there will be one entry
             in the input vector 'input' per BidPackageLineItem to be deleted. There will
             be one call each for every BidPackageRevision for which BidPackageLineItem
             objects are to be deleted.
             

Teamcenter Component:

             Vendor Management - Solution template that provides capability to manage vendor relation
             information.
             
        :param Input: 
                         List of <font face="courier" height="10">LineItemProps</font> structures which denote
                         the exact <b>BidPackageLineItem</b> to be deleted. Out of all the members of this
                         structure, name is needed to be populated as it will be used as the key for search
                         within specified <b>BidPackage</b> Context.
             
        :param BidPackage: 
                         This is reference to <font face="courier" height="10">BidPackageProps</font> structure
                         used to define context to look for <b>BidPackageLineItem</b> objects. ItemId and
                         RevId need to be populated for this structure to accurately define the <b>BidPackageRevision</b>,
                         which will be used to look for <b>BidPackageLineItem</b> objects to be deleted.
             
        :return: 
        """
        ...
    def DeleteVendorRoles(self, Input: list[Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.VendorProperties]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service operation deletes specified VendorRole objects attached with
             VendorRevision objects mentioned through VendorProperties
             data structure. VendorRevision is specified through vendor ID and Revision
             name in VendorProperties. The combination
             to be specified thus is 'vendorId + revId + roleType'. So, this
             combination denotes that there will be one instance of VendorProperties
             per VendorRole to be deleted. In case of VendorRevision is not found
             based on the Id and Revision key, this operation will return an error.
             

Teamcenter Component:

             Vendor Management - Solution template that provides capability to manage vendor relation
             information.
             
        :param Input: 
                         The input is a list of <font face="courier" height="10">VendorProperties</font> structures.
                         There will be an entry for each of the <b>VendorRole</b> objects to be deleted.
             
        :return: 
        """
        ...
    def DeleteVendors(self, Input: list[Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.VendorProperties]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service operation deletes Vendor objects and associated VendorRevision
             objects and VendorRole objects. When provided with the input in the form of
             VendorProperties structure, the operation
             finds the specified Vendor objects and deletes them. VendorRole objects
             will also be deleted along with the associated VendorRevision objects and
             Vendor objects.
             

Teamcenter Component:

             Vendor Management - Solution template that provides capability to manage vendor relation
             information.
             
        :param Input: 
                         A list of <font face="courier" height="10">VectorProperties</font> structures which
                         are used to search for <b>Vendor</b> objects for deletion operation.
             
        :return: 
        """
        ...
    def ChangeVendor(self, Input: list[Teamcenter.Services.Strong.Vendormanagement._2008_06.VendorManagement.ChangeVendorInputInfo]) -> Teamcenter.Services.Strong.Vendormanagement._2008_06.VendorManagement.ChangeVendorResponse:
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
    def GetVendorPartsWithSelRule(self, Input: list[Teamcenter.Services.Strong.Vendormanagement._2008_06.VendorManagement.GetVendorPartsWithSelRuleInputInfo]) -> Teamcenter.Services.Strong.Vendormanagement._2008_06.VendorManagement.GetVendorPartsWithSelRuleResponse:
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
    def CreateOrUpdateLineItemsWithType(self, Properties: list[Teamcenter.Services.Strong.Vendormanagement._2012_02.VendorManagement.LineItemPropertiesWithType], BidPackage: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service operation creates or updates a group of BidPackageLineItem objects
             and any subtype of it in the context of the mentioned BidPackage. This operation
             allows the user to find or create a set of BidPackageLineItem objects based
             on the input data. It first tries to find the existence of the specified BidPackageLineItem
             for the specified BidPackage. If the specified BidPackageLineItem is
             found, then the its data will be updated. Otherwise, it will create the specified
             BidPackageLineItem and associate it to the specified BidPackageRevision.
             If the specified BidPackageLineItem objects exist and any of the input attribute
             values differ from those already set, they will be updated.
             

Teamcenter Component:

             Vendor Management - Solution template that provides capability to manage vendor relation
             information.
             
        :param Properties: 

        :param BidPackage: 
                         Reference to the <b>BidPackageRevision</b> object which will be used to associate
                         the created <b>BidPackageLineItem</b> objects.
             
        :return: 
        """
        ...
    def AddRemoveVendorRoles(self, VendorRoles: list[Teamcenter.Services.Strong.Vendormanagement._2012_09.VendorManagement.VendorRoleData], VendorRevRef: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def CreateVendorParts(self, Properties: list[Teamcenter.Services.Strong.Vendormanagement._2016_09.VendorManagement.VendorPartProperties2]) -> Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.CreateVendorPartsResponse:
        """    
             This operation creates a set of ManufacturerPart objects of given type based
             on input data.This operation is applicable for bulk creation of Vendor Part objects.
             

Use Cases:

             Create Vendor Parts in bulk,when Vendor is already created and CompanyLocation can
             be available with Vendor.
             

Teamcenter Component:

             Vendor Management - Solution template that provides capability to manage vendor relation
             information.
             
        :param Properties: 
                         A list of VendorPartProperties2 structures which are used to create ManufacturerPart
                         objects. The information about each ManufacturerPart to be processed is provided
                         by the way of VendorPartProperties2 structure.
             
        :return: 229028 - A Part name must be provided to create the Vendor Part.
        """
        ...

