import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AddPartSolutionInputInfo:
    """
    
The information of added part is provided by way of the AddPartSolutionInputInfo
data structure.
    """
    def __init__(self, ) -> None: ...
    Values: list[OccNotesAttributes]
    """Vector of OccNotesAttributes for each added component"""
    Component: Teamcenter.Soa.Client.Model.Strong.Item
    """Component to be added"""
    Abe: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """BomLine to which the component is to be added"""
    ProdRevTags: list[Teamcenter.Soa.Client.Model.Strong.Item]
    """Vector of product revisions for each selected component"""
    AbeApnTag: Teamcenter.Soa.Client.Model.Strong.MEAppearancePathNode
    """Appearance Path Node for each added component"""
    ANves: list[Teamcenter.Soa.Client.Model.Strong.NamedVariantExpression]
    """Vector of authorized NVEs present on ABE"""
    Quantity: int
    """Quantity of part to be added"""

class AddPartSolutionResponse:
    """
    
The AddPartSolutionResponse structure represents one output vector
AddPartSolutionOutputInfo
and the service data.
    """
    def __init__(self, ) -> None: ...
    PartSolutionAPNs: list[Teamcenter.Soa.Client.Model.Strong.MEAppearancePathNode]
    """partSolutionAPNs"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData returned as response for retrieving add part to product information"""

class GetProductItemResponse:
    """
    
The GetProductItemResponse structure contains
a list of all Product Items found in the database and a ServiceData
object.
    """
    def __init__(self, ) -> None: ...
    Output: list[Teamcenter.Soa.Client.Model.Strong.Item]
    """A list of  all Product Items found in the database."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData object containing error codes
            and error messages in case of failure.
            """

class GetRemoveABEPartsResponse:
    """
    
The GetRemoveABEPartsResponse structure contains
the ServiceData object.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData containing error codes and
            error messages along with the indices for which the removePartsRelatedToABE
            operation fails.
            """

class OccNotesAttributes:
    """
    
The part data information about each component is provided by way of the
OccNotesAttributes
data structure.
    """
    def __init__(self, ) -> None: ...
    NoteType: str
    """Note type for selected component"""
    NoteText: str
    """Note text for selected component"""

class RemoveABEPartsInputInfo:
    """
    
The information to remove parts related to ABE is provided by way of the
RemoveABEPartsInputInfo data structure.
    """
    def __init__(self, ) -> None: ...
    AbeAPN: Teamcenter.Soa.Client.Model.Strong.MEAppearancePathNode
    """
            The reference to the Appearance Path Node of the Architecture Breakdown Element of
            which Part Solutions are to be removed. This is a mandatory attribute for the operation
            to succeed and cannot be null.
            """
    Topline: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            The reference to the topline to which Architecture Breakdown Element is linked. This
            is a mandatory attribute for the operation to succeed and cannot be null.
            """

class ReplacePartSolutionInputInfo:
    """
    
The information to replace part is provided by way of the
ReplacePartSolutionInputInfo
data structure.
    """
    def __init__(self, ) -> None: ...
    Values: list[OccNotesAttributes]
    """Vector of OccNotesAttributes for each added component"""
    Component: Teamcenter.Soa.Client.Model.Strong.Item
    """Component by which the replacement has been doing"""
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """Bomline to which the part is to be replaced"""
    AbeAPN: Teamcenter.Soa.Client.Model.Strong.MEAppearancePathNode
    """APN of the associated ABE"""
    ANves: list[Teamcenter.Soa.Client.Model.Strong.NamedVariantExpression]
    """Vector of authorized NVEs present on ABE"""
    SplitAndClone: bool
    """splitAndClone"""
    CarrySubstitutes: bool
    """carrySubstitutes"""

class ReplacePartSolutionResponse:
    """
    
The ReplacePartSolutionResponse structure represents one output vector
ReplacePartSolutionOutputInfo
and the service data.
    """
    def __init__(self, ) -> None: ...
    Component: list[Teamcenter.Soa.Client.Model.Strong.Item]
    """component"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData returned as response for retrieving replace part in product information"""

class ContextManagement:
    """
    Interface ContextManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddPartToProduct(self, Inputs: list[AddPartSolutionInputInfo]) -> AddPartSolutionResponse:
        """    
             get the required Information for add part to product.
             

Teamcenter Component:

             Platform Designer - Application to create and manage architecture breakdowns and
             product variability.
             
        :param Inputs: 
                         Vector of structure containing the required info to call add part to product
             
        :return: contains required info regarding the success of add part to product for the inputs
             provided.
        """
        ...
    def GetProductItemInfo(self) -> GetProductItemResponse:
        """    
             Returns a list of all Product Items found in the database. The following preferences
             can be used to define an object as a Product Item.
             
             The preference PortalDesignContextProductItemProperties is used to specify one or
             more of the following properties to be used to define the object as Product Item.
             Multiple properties could be specified at the same time and the algorithm will check
             all the specified property values to be satisfied in order to deem an object as a
             Product Item.
             

    object_type
             
    object_desc
             
    owning_group
             


             For Example: PortalDesignContextProductItemProperties = object_type,object_desc
             
             The preference PortalDesignContextProductItemProperties.<property_name>  is used
             to specify the value to be checked in order to determine whether the object is a
             Product Item. For example: PortalDesignContextProductItemProperties.object_type =
             CORP_Vehicle
             
             Only an object of type Item or its sub type could be defined as a Product
             Item. The operation will return empty if any other objects are specified.
             
             The default values are
             
             PortalDesignContextProductItemProperties = object_type, object_desc
             
             PortalDesignContextProductItemProperties.object_type=Item
             
             PortalDesignContextProductItemProperties.object_desc=Product
             

Use Cases:

             The getProductItemInfo operation is called
             when user wants to fetch all Product Items present in the database which are defined
             by setting the PortalDesignContextProductItemProperties preference.
             

Teamcenter Component:

             Platform Designer - Application to create and manage architecture breakdowns and
             product variability.
             
        :return: 
        """
        ...
    def RemovePartsRelatedToABE(self, Inputs: list[RemoveABEPartsInputInfo]) -> GetRemoveABEPartsResponse:
        """    
             Deletes all the related Part Solutions of an Architecture Breakdown Element (ABE).
             The links through which the Part solutions are related to the Architecture Breakdown
             Element are also removed.
             

Use Cases:

             The removePartsRelatedToABE operation is
             called when user wants to remove all part solutions related to Architecture Breakdown
             Element and their corresponding links. The user can specify the input Architecture
             Breakdown Element and top line to which the Architecture Breakdown Element is linked
             using RemoveABEPartsInputInfo object.
             

Teamcenter Component:

             Platform Designer - Application to create and manage architecture breakdowns and
             product variability.
             
        :param Inputs: 
                         The list of <font face="courier" height="10">RemoveABEPartsInputInfo</font> objects.
                         Each object contains all the required information to remove Part Solutions related
                         to the Architecture Breakdown Element along with configured Part Data information.
             
        :return: object and a partial error will be returned.
        """
        ...
    def ReplacePartInProduct(self, Inputs: list[ReplacePartSolutionInputInfo]) -> ReplacePartSolutionResponse:
        """    
             get the required Information for replace part in product.
             

Teamcenter Component:

             Platform Designer - Application to create and manage architecture breakdowns and
             product variability.
             
        :param Inputs: 
                         Vector of structure containing the required info to call replace part in product
             
        :return: contains required info regarding the success of replace part in product for the inputs
             provided.
        """
        ...

