import Teamcenter.Soa.Client.Model
import typing

class LineItemPropertiesWithType:
    """
    
The information about each BidPackageLineItem to be processed is provided
by way of the LineItemPropertiesWithType
data structure.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Name of the BidPackageLineItem to be created."""
    Description: str
    """Description of the BidPackageLineItem Object."""
    Liccname: str
    """Name of the LineItemConfigContext to be created."""
    Liccdesc: str
    """Description of the LineItemConfigContext to be created."""
    Partid: str
    """Id of the part to be associated with BidPackageLineItem."""
    Viewtype: str
    """PSView Type to be associated with LineItemConfigContext."""
    Quantity: int
    """Quantity to be created for BidPackageLineItem."""
    RevRule: str
    """Revision rule to be associated with LineItemConfigContext."""
    VarRule: str
    """Variant rule to be associated with LineItemConfigContext."""
    ClosureRule: str
    """Closure rule to be associated with LineItemConfigContext."""
    Quote: Teamcenter.Soa.Client.Model.ModelObject
    """Quote form to be added to BidPackageLineItem."""
    BpliTypeName: str
    """Name of the type of the BidPackageLineItem to be used."""

class VendorManagement:
    """
    Interface VendorManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateLineItemsWithType(self, Properties: list[LineItemPropertiesWithType], BidPackage: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData:
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

