import Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement
import Teamcenter.Soa.Client.Model
import typing

class VendorPartProperties2:
    """
    
The information about each ManufacturerPart to be processed is provided by
way of the VendorPartProperties2 data structure.
    """
    def __init__(self, ) -> None: ...
    PartId: str
    """
            Id of ManufacturerPart to be created, if not specified or blank then operation will
            generate the partId.
            """
    PartName: str
    """Part Name of the ManufacturerPart to be created."""
    PartType: str
    """Object type to be created. Only "ManufacturerPart" is valid type."""
    RevId: str
    """Revision Id specified for create. Generated if the string is empty."""
    VendorObj: Teamcenter.Soa.Client.Model.ModelObject
    """Vendor object to be associated with ManufacturerPart."""
    CompanyLocationObj: Teamcenter.Soa.Client.Model.ModelObject
    """
CompanyLocation object to be associated with ManufacturerPart. If null,
            then no location will be associated with ManufacturerPart object.
            """
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify the Partial Errors
            associated with input.
            """

class VendorManagement:
    """
    Interface VendorManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateVendorParts(self, Properties: list[VendorPartProperties2]) -> Teamcenter.Services.Strong.Vendormanagement._2007_06.VendorManagement.CreateVendorPartsResponse:
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

