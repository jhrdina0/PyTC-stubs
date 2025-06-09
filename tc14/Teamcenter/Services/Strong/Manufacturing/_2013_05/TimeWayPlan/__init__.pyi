import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class Data:
    """
    The structure holds the property value.
    """
    def __init__(self, ) -> None: ...
    DataType: str
    """
            Type of the data. Valid types are "Boolean", "Character", "Integer", "Double", "String",
            "Tag" and "Date". One of the data in this structure need to be accessed based on
            the data type string.
            """
    BoolProperties: list[bool]
    """The list of Boolean values."""
    CharProperties: str
    """
            The string representing the list of characters. Each character in the string is a
            value of the property.
            """
    IntegerProperties: list[int]
    """The list of integer values."""
    DoubleProperties: list[float]
    """The list of double values."""
    StringProperties: list[str]
    """The list of string values."""
    TagProperties: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The list of business objects."""
    DateProperties: list[System.DateTime]
    """The list of dates."""

class ProductImageInfo:
    """
    
The input structure contains object(s) for which product image is to be set, the
business object of the dataset  representing the image and the product Bill Of
Processes
(BOP) context.
    """
    def __init__(self, ) -> None: ...
    TargetObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The list of business objects for which the product image is to be set.
            
            The valid types are as follows
            

Mfg0BvrProcessStation - process station.
            
Mfg0BvrProcessLine - process line.
            
Mfg0BvrProcessArea - process area.
            
Mfg0BvrPlantBOP - plant Bill Of Processes (BOP).
            

"""
    ContextProductBOP: Teamcenter.Soa.Client.Model.ModelObject
    """
            The business object representing the top line of the Product Bill Of Processes(BOP).
            This Product BOP is the context for which the product image is set with the targetObjects
            and is of type MEProductBOPRevision.
            
            This could be NULL provided that there is only one product BOP linked to the plant
            BOP. In case multiple product BOPs are linked then corresponding error will be reported.
            """
    ImageDataset: Teamcenter.Soa.Client.Model.ModelObject
    """
            The business object of the dataset representing the product image. The same product
            image will be common for all the objects in the input parameter targetObjects.
            """

class TwpInfo:
    """
    Structure contains the object and its corresponding Time Way Plan (TWP)
information.
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """
            The object for which information is fetched.
            
            The valid types are
            

Mfg0BvrProcessStation - process station
            
Mfg0BvrProcessLine - process line
            
Mfg0BvrProcessArea - process area
            
Mfg0BvrPlantBOP - plant bill of process (BOP) or
            
Mfg0BvrOperation - operation.
            

"""
    DetailedInfo: System.Collections.Hashtable
    """
            The map of string which is a data identifier and its corresponding Data.
            
            Description of valid strings and its data
            
                "Operations": Represents the operations executed under the
            station.
            
                "ExecutionPositions": Represents the execution positions
            for the object of TwpInfo stucture.
            
                "Direction": Represents the direction of the station in the
            plant.
            
                "ProductImage": Represents the product image for the station.
            
                "PlantCarpet": Represents the carpet diagram of the plant.
            
                "TWPLocationForms": Represents the business objects of the
            TWP Location form associated with the station.
            
"""

class TwpInfoInput:
    """
    
The input structure contains object(s) for which information is required, the
list
of string specifying what information is required and the product Bill Of
Process
(BOP) context. The object can be process station(s), process line(s), process
area(s),
or plant BOP.
    """
    def __init__(self, ) -> None: ...
    RequestedObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The list of business object for which TWP information is required. The valid types
            are process station, process line, process area or plant Bill Of Process (BOP).
            """
    ContextProductBOP: Teamcenter.Soa.Client.Model.ModelObject
    """
            The business object representing the top line of the Product Bill Of Process (BOP).
            This Product BOP is the context for which TWP information is fetched and is of type
            MEProductBOPRevision   .
            
            This could be NULL provided that there is only one product BOP linked to the plant
            BOP. In case multiple product BOPs are linked then corresponding error will be reported.
            """
    RequiredData: list[str]
    """
            List of string specifying what information is required.
            
            The valid options are:
            
                OperationDetails: To fetch the operation details of
            given station.
            
            Response will consist of information about all the operations under the given station,
            the allocated time for those operations and their execution position. Other station
            related information such as length, width, X-Y Coordinates specifying its location
            in plant, orientation and direction will also be part of response.
            
                ExecutionPositions : To fetch the execution positions
            of the given station.
            
            Other station related information such as length, width, X-Y Coordinates specifying
            its location in plant, orientation and direction will also be part of response.
            
                ProductImage : To fetch the product image which will
            be displayed on the station in TWP view.
            
                PlantCarpet : To fetch the carpet image of the plant.
            This image is shown in the TWP view as plant layout.
            
"""

class TwpResponse:
    """
    
The response contains a structure of the TWP data and the ServiceData. The
possible
errors reported are:

Â Â Â Â 251048 - The Plant Bill Of Process (BOP) is linked to multiple
Product BOPs. Please select one of the Product BOP as context.

Â Â Â Â 251049 - The input Product Bill Of Process (BOP) and Plant
BOP are not linked.

    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data containing partial errors if any."""
    InfoMap: System.Collections.Hashtable
    """
            A map of business objects for which TWP information is requested and its corresponding
            TWP information.
            """

class TimeWayPlan:
    """
    Interface TimeWayPlan
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetTWPInformation(self, Input: TwpInfoInput) -> TwpResponse:
        """    
             This service operation fetches the Time Way Plan (TWP) information. The operation
             takes objects from the plant Bill of Processes (BOP) for which TWP information is
             required, the list of strings specifying what information is required and the context
             product BOP. The object can be process station(s), process line(s), process area(s),
             or plant BOP. The list of string will have values "OperationDetails", "ExecutionPositions",
             "ProductDiagram", and "PlantCarpet" based on which response will contain the information.
             These values will be applicable to all the objects for which TWP information is required.
             

             This information is used to display the Time Way Plan view.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         The input structure contains object(s) for which information is required, the list
                         of string specifying what information is required and the product Bill Of Process
                         (BOP) context. The object can be process station(s), process line(s), process area(s),
                         or plant BOP.
             
        :return: Â Â Â Â 251050 - No Product Bill Of Process (BOP) is associated with
             the Plant BOP.
        """
        ...
    def SetProductImage(self, Input: list[ProductImageInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service operation sets a product image for the given input object. The operation
             takes objects from the plant Bill Of Processes (BOP) for which the product image
             is to be set, the business object of the context product BOP, and the business object
             of the dataset representing the product image. The object   from the plant BOP for
             which product image is to be set can be process station(s), process line(s), process
             area(s), or plant BOP.
             
             This operation will create a relation between the object from the plant BOP input
             object and  the dataset business object in context of the input product BOP.
             
             The specified product image is displayed on the station in the Time Way Plan (TWP)
             view.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         The input structure contains object(s) for which product image is to be set, the
                         business object of the dataset  representing the image and the product Bill Of Processes
                         (BOP) context. The object can be process station(s), process line(s), process area(s),
                         or plant BOP.
             
        :return: 
        """
        ...

