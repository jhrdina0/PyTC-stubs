import System
import System.Collections
import Teamcenter.Services.Strong.Allocations._2007_01.Allocation
import Teamcenter.Soa.Client.Model.Strong
import typing

class AllocationContextInput2:
    """
    
            The AllocationContextInput2 structure represents all the data necessary for
            creating an Allocation Context. The basic attributes that are required by ITK are
            passed as named elements in the structure. It will be used by the revised SOA createAllocationContext2()
            which also handles extended attributes.
            
    """
    def __init__(self, ) -> None: ...
    Id: str
    """The ID of the AllocationMap object to be created. If empty, will be generated."""
    Name: str
    """The name of the AllocationMap object to be created. Optional input."""
    Type: str
    """
            The type of the AllocationMap object to be created. If type is not provided,
            the AllocationMap created will be of type AllocationMap.
            """
    Revision: str
    """The revision id for the AllocationRevisionMap object to be created."""
    OpenedBOMWindows: list[Teamcenter.Soa.Client.Model.Strong.BOMWindow]
    """
            List of BOMWindow business objects to be associated to the AllocationMap
            business object, where the created AllocationMap will be the context for the
            Allocations created between the BOMLines of these BOMWindows.
            """
    AttrValueMap: System.Collections.Hashtable
    """
            The map of  Attribute names and  value pairs to be used for AllocationMap
            business object creation of type string/string. The client calling this operation
            is responsible for converting the different property types (int , float, date etc)
            to string  using the appropriate to XXXString functions. Multi valued properties
            are represented with a comma separated string.
            """

class Allocation:
    """
    Interface Allocation
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateAllocationContext2(self, Input: AllocationContextInput2) -> Teamcenter.Services.Strong.Allocations._2007_01.Allocation.GetAllocationWindowResponse:
        """    
             The operation creates an AllocationMap object for the given name, id and attribute
             map input. This operation has Multi field key support for AllocationMap business
             object creation. The created AllocationMap object is saved to Teamcenter.
             It creates an AllocationWindow with the AllocationMapRevision object
             as context. It adds the input BOMWindow objects as the BOMWindow objects
             for the AllocationWindow. The created AllocationMap, AllocationRevision,
             AllocationWindow are returned as created objects list in ServiceData Element.
             

Use Cases:

Create AllocationMap object with Multi field key support

             The AllocationMap object can be created with full Multi field key support
             using this operation. If the business constant of MFK for the AllocationMap
             object has item_id and any other attribute, then the user can create AllocationMap
             with same item id as well.
             


Dependencies:

             createBOMWindows
             

Teamcenter Component:

             Allocations - Provides the functionality to map occurrences between two or more structures.
             Currently used in Mechatronics to map logical schematic structures to physical 3D
             structures.
             
        :param Input: 
                         An <b>AllocationMap</b> business object is created using the input using the id,
                         name, revision, type,<b> </b><b>BOMWindows</b>, extended attribute values provided
                         in attrValuemap.
             
        :return: business
             object are also returned as part of created objects list of the ServiceData element.
             Any errors during the operation will be returned as Partial Errors of the ServiceData
             element.
        """
        ...

