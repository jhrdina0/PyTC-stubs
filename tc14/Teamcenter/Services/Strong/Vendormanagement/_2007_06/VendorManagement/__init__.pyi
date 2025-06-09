import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BidPackageProps:
    """
    
The information about each BidPackage to be processed is provided by way of
the BidPackageProps data structure.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify the Partial Errors
            associated with this BidPackageProps input.
            """
    ItemId: str
    """Id to create BidPackage, generated if the string is empty."""
    Name: str
    """Name for the BidPackage. Default name generated if left empty."""
    Type: str
    """Object Type to be created. It is BidPackage."""
    RevId: str
    """Revision Id to create BidPackageRevision. Generated if left empty."""
    Description: str
    """Description of the object to be created."""

class CreateBidPacksOutput:
    """
    
The information about each BidPackage object output after creation is provided
by  way of the CreateVendorsOutput data structure.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify the Partial Errors
            associated with input.
            """
    BidPackage: Teamcenter.Soa.Client.Model.Strong.BidPackage
    """Model Object pointing to the BidPackage created."""
    BidPackageRev: Teamcenter.Soa.Client.Model.Strong.BidPackageRevision
    """Model Object poinitng to the BidPackageRevision created."""

class CreateBidPacksResponse:
    """
    
The CreateBidPacksResponse structure represents
the output vector CreateBidPacksOutput and
standard Teamcenter ServiceData structure
instance.
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateBidPacksOutput]
    """
            A list of CreateBidPacksOutput structures.
            Each entry represents a BidPackage created or updated.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard ServiceData structure. It contains
            typical potential errors as mentioned in throws and failures along with the clientIds.
            """

class CreateVendorPartsOutput:
    """
    
The information about each VendorPart object output after creation is provided
by way of the CreateVendorPartsOutput data
structure.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify the Partial Errors
            associated with input.
            """
    VendorPart: Teamcenter.Soa.Client.Model.Strong.Part
    """Model Object pointing to the VendorPart created."""
    VendorPartRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Model Object poinitng to the VendorPart revision created."""

class CreateVendorPartsResponse:
    """
    
The CreateVendorPartsResponse structure represents
the list of CreateVendorPartsOutput and Standard
Teamcenter ServiceData.
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateVendorPartsOutput]
    """
            Output is list of CreateVendorPartsOutput
            data structures, each of them representing a new VendorPart created.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard ServiceData structure. It contains
            partial errors and failures along with the clientIds.
            """

class CreateVendorsOutput:
    """
    
The information about each Vendor object output after creation is provided
by way of the CreateVendorsOutput data structure.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """A unique string supplied by the caller."""
    Vendor: Teamcenter.Soa.Client.Model.Strong.Vendor
    """Vendor Object created or updated."""
    VendorRev: Teamcenter.Soa.Client.Model.Strong.VendorRevision
    """VendorRevision Object created or Updated."""

class CreateVendorsResponse:
    """
    
The CreateVendorsResponse structure represents
the output vector CreateVendorsOutput and
the ServiceData.
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateVendorsOutput]
    """
            A list of CreateVendorsOutput structures.
            Each of them represents a Vendor created or updated.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard ServiceData structure. It contains
            partial errors and failures along with the clientIds.
            """

class LineItemProps:
    """
    
The information about each BidPackageLineItem to be processed is provided
by way of the LineItemProps data structure.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Name of the BidPackageLineItem to be created."""
    Description: str
    """Description of the BidPackageLineItem Object."""
    Liccname: str
    """Name of the LineItemConfigContext to be created."""
    Liccdesc: str
    """
            Description for the LineItemConfigContext
            object to be created.
            """
    Partid: str
    """Id of the part to be associated with BidPackageLineItem."""
    Viewtype: str
    """PSViewType to be associated with LineItemConfigContext."""
    Quantity: int
    """Quantity to be created for BidPackageLineItem."""
    RevRule: str
    """Revision rule to be associated with LineItemConfigContext."""
    VarRule: str
    """Variant rule to be associated with LineItemConfigContext."""
    ClosureRule: str
    """Closure rule to be associated with LineItemConfigContext."""
    Quote: Teamcenter.Soa.Client.Model.ModelObject
    """Model Object for Quote to be added to BidPackageLineItem."""

class VendorPartProperties:
    """
    
The information about each VendorPart to be processed is provided by way of
the VendorPartProperties data structure.
    """
    def __init__(self, ) -> None: ...
    PartId: str
    """
            Id for part to be created, mandatory for ManufacturerPart objects but generated
            for CommercialPart objects if the string is empty. Output PartId in case of
            ManufacturerPart will contain the provided partId and provided VendorId.
            """
    Name: str
    """Name of the Part object to be created."""
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify the Partial Errors
            associated with this VendorPartProperties
            input.
            """
    Type: str
    """
            Object type to be created. Only ManufacturerPart and CommercialPart
            are valid.
            """
    RevId: str
    """Revision Id specified for create. Generated if the string is empty."""
    Description: str
    """Description of the VendorPart."""
    Vendorid: str
    """
Vendor Id to be associated with Part. Vendor Id is optional for CommercialPart
            but mandatory for ManufacturerPart.
            """
    Commercialpartid: str
    """Id of CommercialPart to be associated with ManufacturerPart."""
    Commercialpartrevid: str
    """
CommercialPartRevision Id to be associated with ManufacturerPart. If
            blank, ManufacturerPart is attached with the CommercialPart instead.
            """
    IsDesignReq: bool
    """Flag to decide if the design is required."""
    Uom: Teamcenter.Soa.Client.Model.ModelObject
    """Unit of Measure for Model Object."""
    Makebuy: int
    """Make Buy Value for Part. The value could be either Make or Buy."""

class VendorProperties:
    """
    
The information about each Vendor to be processed is provided by way of the
VendorProperties data structure.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify the Partial Errors
            associated with this VendorProperties input.
            """
    ItemId: str
    """Item Id of the Vendor. Generated if the string is empty."""
    Name: str
    """Name of the Vendor. Default name is generated if kept empty."""
    Type: str
    """Object type to be created."""
    RevId: str
    """VendorRevision Id specified for create. Generated if the string is empty."""
    Description: str
    """Description of the Vendor."""
    RoleType: str
    """
            Type of VendorRole. It can be Manufacturer,Supplier, Distributor or
            blank.
            """
    CertifiStatus: str
    """Vendor Certification status like Gold,Silver etc."""
    VendorStatus: str
    """Vendor status like Preferred,Approved etc."""

class VendorManagement:
    """
    Interface VendorManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateBidPackages(self, Properties: list[BidPackageProps], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> CreateBidPacksResponse:
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
    def CreateOrUpdateLineItems(self, Properties: list[LineItemProps], BidPackage: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def CreateOrUpdateVendorParts(self, Properties: list[VendorPartProperties], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> CreateVendorPartsResponse:
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
    def CreateOrUpdateVendors(self, Properties: list[VendorProperties], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> CreateVendorsResponse:
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
    def DeleteLineItems(self, Input: list[LineItemProps], BidPackage: BidPackageProps) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def DeleteVendorRoles(self, Input: list[VendorProperties]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def DeleteVendors(self, Input: list[VendorProperties]) -> Teamcenter.Soa.Client.Model.ServiceData:
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

