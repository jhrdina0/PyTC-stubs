import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AllocationContextInput:
    """
    
            The AllocationContextInput structure represents all the data necessary for
            creating an Allocation Context. The basic attributes that are required by ITK are
            passed as named elements in the structure.
            
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
            Allocations created between the BOMLine objects of these BOMWindow
            objects.
            """

class AllocationLineInfo:
    """
    
            The AllocationLineInfo structure represents all of the data necessary to construct
            the AllocationLine object. The basic attributes that are required by ITK are
            passed as named elements in the structure.
            
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The AllocationLine name for creation, optional if empty, generated on server."""
    Type: str
    """
            The AllocationLine type, if empty then the default type Allocation
            is used.
            """
    Reason: str
    """The AllocationLine reason, optional."""
    FromBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """AllocateFrom BOMLine objects, required."""
    ToBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """AllocateTo BOMLine objects, required."""

class AllocationLineInput:
    """
    
            The AllocationLineInput structure contains all the elements necessary for
            the identifying an AllocationLine object, including AllocationLineInfo
            structure as well as an object reference to the AllocationLine itelf.
            
    """
    def __init__(self, ) -> None: ...
    AllocationLine: Teamcenter.Soa.Client.Model.Strong.AllocationLine
    """AllocationLine object which needs to be modified."""
    AllocationLineInfo: AllocationLineInfo
    """
AllocationLineInfo element containing all information necessary for modification
            of the AllocationLine object.
            """

class AllocationWindowInfo:
    """
    
            The AllocationWindowInfo structure represents all of the data necessary for
            opening an AllocationWindow. The basic attributes that are required by ITK
            are passed as named elements in the structure.
            
    """
    def __init__(self, ) -> None: ...
    AllocationContext: Teamcenter.Soa.Client.Model.Strong.AllocationMapRevision
    """
            AllocationContext Object, can be AllocationMap or AllocationMapRevision
            businessobject.
            """
    AllocationRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """Allocation Rule."""
    OpenedBOMWindows: list[Teamcenter.Soa.Client.Model.Strong.BOMWindow]
    """Keep track of opened BOM Window"""

class GetAllocatedBOMViewInfo:
    """
    
            The GetAllocatedBOMViewInfo structure is used as a mapping between the AllocationMap

            object and its corresponding allocated BOMView Objects.
            
    """
    def __init__(self, ) -> None: ...
    AllocationMap: Teamcenter.Soa.Client.Model.Strong.AllocationMap
    """AllocationMap business object."""
    AllocatedBOMViewObjects: list[Teamcenter.Soa.Client.Model.Strong.PSBOMView]
    """A list of PSBOMView business objects associated to the AllocationMap object."""

class GetAllocatedBOMViewResponse:
    """
    
            The GetAllocatedBOMViewResponse structure contains a list of the structure
            GetAllocatedBOMViewInfo and Service Data. Any errors are reported in ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    AllocatedBOMViewInfo: list[GetAllocatedBOMViewInfo]
    """
            Structure which contains the AllocationMap business object and a list of associated
            PSBOMView objects.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData."""

class GetAllocationWindowResponse:
    """
    
            The GetAllocationWindowResponse structure represents the current state of
            the BOMWindow as well as the list of AllocationLine objects contained
            in said BOMWindow.
            
    """
    def __init__(self, ) -> None: ...
    AllocationWindow: Teamcenter.Soa.Client.Model.Strong.AllocationWindow
    """The Business Object corresponding to the AllocationWindow."""
    AllocationLines: list[Teamcenter.Soa.Client.Model.Strong.AllocationLine]
    """AllocationLine objects for the modified AllocationWindow."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            ServiceData contains the created AllocationMap, AllocationMapRevision,
            and AllocationWindow  created in the created objects of list of the ServiceData
            Element. Any errors occurred during the operation will be returned in the Partial
            errors of the ServiceData element.
            """

class Allocation:
    """
    Interface Allocation
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateAllocationContext(self, Input: AllocationContextInput) -> GetAllocationWindowResponse:
        """    
             This operation is used to create an AllocationMap and AllocationMapRevision
             object  from the  AllocationContextInput structure. AllocationContextInput
             consists of Name, id, Revision, type, list  of BOM (Bill of Material) Windows for
             which allocations has to be created. In this operation, it will create an AllocationMapRevision
             and sets it window to said context.
             

Use Cases:

             Allocation allows to map one or more BOMLine objects of two or more product
             structures. An AllocationMap is a business object that specifies how two structures
             are tied together by a set of allocations that exist between two structures. Defining
             such an AllocationMap needs allocation context which is carried out by this
             operation.
             


Teamcenter Component:

             Allocations - Provides the functionality to map occurrences between two or more structures.
             Currently used in Mechatronics to map logical schematic structures to physical 3D
             structures.
             
        :param Input: 
                         Structures containing the details of the <b>AllocationMap</b> and <b>AllocationMapRevision</b>
                         object to be created.
             
        :return: 
        """
        ...
    def OpenAllocationWindow(self, AllocWindowInput: AllocationWindowInfo, IcContext: Teamcenter.Soa.Client.Model.ModelObject) -> GetAllocationWindowResponse:
        """    
             The operation creates an AllocationWindow for the given allocation context
             object. After creating the AllocationWindow object, the operation opens the
             AllocationWindow and sets the RevisionRule and the incremental change
             context on the opened AllocationWindow. The operation finds all the configured
             AllocationLine objects corresponding to the given BOMWindow objects and returns
             them to the user along with the AllocationWindow object.
             

Use Cases:

             The AllocationWindow is usually created and opened to find different allocations
             between two or more BOM View objects. For example the user wants to find various
             functions defined in the functional model of a product allocated to different ECUs
             in the logical model. In this case an AllocationWindow for given allocation
             context is created and opened. All the function to ECU allocations relevant to the
             opened functional and logical model for the given revision rule and incremental change
             context are fetched and displayed to the user in the form of AllocationLine
             objects.
             

Dependencies:

             createAllocationContext
             

Teamcenter Component:

             Allocations - Provides the functionality to map occurrences between two or more structures.
             Currently used in Mechatronics to map logical schematic structures to physical 3D
             structures.
             
        :param AllocWindowInput: 
                         An <i>AllocationWindowInfo</i> object, which contains the allocation context, <b>RevisionRule</b>
                         and the list of relevant <b>BOMWindow</b> objects.
             
        :param IcContext: 
                         An Optional parameter which is a reference to the incremental change context object.
             
        :return: 
        """
        ...
    def AddAllocationLines(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, InputAllocationLines: list[AllocationLineInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation is used to create new AllocationLine objects between BOMLine
             objects of different product structures. This operation needs an AllocationWindow
             object with an associated AllocationMapRevision object, for which AllocationLine
             will be created and a list of structure AllocationLineInfo which consists
             of name, type and reason for creation AllocationLine with from and to BOMLines
             from different structure. This operation will return created AllocationLine
             objects in the service data as created objects. If BOMLine is same for source
             and target, then error will be reported and stored as service data error.
             

Use Cases:

AllocationLine is a runtime representation of an Allocation object
             as well as it provides runtime properties. It will maintain sources and targets information
             for Allocation. When you want traceability between different aspects of a product,
             you can use this operation to create AllocationLine objects.
             

Dependencies:

             createAllocationContext
             

Teamcenter Component:

             Allocations - Provides the functionality to map occurrences between two or more structures.
             Currently used in Mechatronics to map logical schematic structures to physical 3D
             structures.
             
        :param AllocWindowInput: 
<b>AllocationWindow</b> Object for which <b>AllocationLine</b> objects are to be
                         added.
             
        :param InputAllocationLines: 
                         A list of <i>AllocationLineInfo</i> structures which have information of <b>AllocationLine</b>
                         objects which user wants to create.
             
        :return: 
        """
        ...
    def ChangeAllocatedBOMWindows(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, AddBOMWindowList: list[Teamcenter.Soa.Client.Model.Strong.BOMWindow], RemoveBOMWindowList: list[Teamcenter.Soa.Client.Model.Strong.BOMWindow]) -> GetAllocationWindowResponse:
        """    
             The operation allows modifying the BOMWindow business objects associated to
             the AllocationWindow while working with Allocation functionality. Allows user
             to add new BOMWindow objects to the AllocationWindow and remove any
             existing BOMWindow objects from the AllocationWindow. Once the BOMWindow
             objects associated are modified, the AllocationLine objects for the context
             of AllocationWindow are returned to the client. Any errors encountered will
             be returned as part of partial errors in ServiceData element.
             

Use Cases:

To modify the BOMWindows associated to an AllocationWindow

             While working in allocation functionality, if the user wants to work with an additional
             product structure in addition to one which is opened already, or to close some unwanted
             product structure, the user can achieve this using this operation by providing the
             required BOMWindow business objects in addBOMWindowList and removeBOMWindowList.
             


Dependencies:

             openAllocationWindow
             

Teamcenter Component:

             Allocations - Provides the functionality to map occurrences between two or more structures.
             Currently used in Mechatronics to map logical schematic structures to physical 3D
             structures.
             
        :param AllocWindowInput: 
<b>AllocationWindow</b> business object for which the <b>BOMWindow</b> objects have
                         to be modified by adding any new <b>BOMWindows</b> or removing any existing <b>BOMWindow</b>
                         objects.
             
        :param AddBOMWindowList: 
                         List of <b>BOMWindow</b> objects which have to be added to <b>AllocationWindow</b>
                         input. It is an optional input.
             
        :param RemoveBOMWindowList: 
                         List of <b>BOMWindow</b> objects which have to be removed from <b>AllocationWindow</b>
                         input. It is an optional input.
             
        :return: is returned as updated objects of ServiceData element. Any
             errors during the operation will be returned as Partial Errors of ServiceData element.
        """
        ...
    def ChangeAllocationContext(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, AllocationContext: Teamcenter.Soa.Client.Model.Strong.AllocationMapRevision, AllocationRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule, IcContext: Teamcenter.Soa.Client.Model.Strong.ItemRevision) -> GetAllocationWindowResponse:
        """    
             This operation is used to change the context object an AllocationMapRevision
             business object of the input AllocationWindow. This operation requires AllocationMapRevision
             object which user wants to set on AllocationWindow. This operation also sets
             the RevisionRule for AllocationWindow and Incremental Change object
             for the AllocationWindow.
             

Use Cases:

             Sets a new allocation context, Incremental Change context, RevisionRule for
             an AllocationWindow and reloads the allocations for the given set context.
             

Teamcenter Component:

             Allocations - Provides the functionality to map occurrences between two or more structures.
             Currently used in Mechatronics to map logical schematic structures to physical 3D
             structures.
             
        :param AllocWindowInput: 
<b>AllocationWindow</b> Object which is associated to an <b>AllocationMapRevision</b>
                         object which user wants to change.
             
        :param AllocationContext: 
<b>AllocationMapRevision</b> object which user wants to set on input <b>AllocationWindow</b>.
             
        :param AllocationRule: 
<b>RevisionRule</b> to be set on <b>AllocationWindow</b> and load the allocations
                         accordingly.
             
        :param IcContext: 
                         Incremental Change Context object to be set on the <b>AllocationWindow</b> (optional).
             
        :return: 
        """
        ...
    def ChangeICContext(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, IcContextRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Sets the Incremental Change context for an AllocationWindow. Used to
             set a new Incremental Change context or remove the already set Incremental Change
             context set on an AllocationWindow. Once the Incremental Change is set, the
             AllocationLine objects for the context of AllocationWindow is returned
             to the client.
             

Use Cases:

Use case 1:  Set a new Incremental Change Context on Allocation
             Window


Set a new Incremental Change context for the AllocationWindow.
             When the Incremental Change context is set on an AllocationWindow, the changes
             made to the AllocationWindow like adding a new Allocation, deleting any existing
             Allocation or modifying any Allocation will be captured in the IC context set. This
             Incremental Change context can be used later to get all the modification made for
             the given Incremental Change context object.
             



Use Case 2:  Remove the Incremental Change Context set on Allocation
             Window


Remove any set Incremental Change context for the AllocationWindow.
             By passing an NULL input to the operation for Incremental Change context will
             unset the Incremental Change and there after any modifications made to AllocationWindow
             will not be captured incrementally.
             



Dependencies:

             openAllocationWindow
             

Teamcenter Component:

             Allocations - Provides the functionality to map occurrences between two or more structures.
             Currently used in Mechatronics to map logical schematic structures to physical 3D
             structures.
             
        :param AllocWindowInput: 
<b>AllocationWindow</b> object for which Incremental changes like adding an new allocation,
                         removing an existing allocation, or modifying an allocation has  to be captured.
             
        :param IcContextRev: 
                         Incremental Change Revision object which is set on <b>AllocationWindow</b> . If <i>NULL</i>
                         is provided as the input, and the <b>AllocationWindow</b> has any Incremental Change
                         context set, it will be removed.
             
        :return: object for which the Incremental Change object is set is returned as part of updated
             Object of the ServiceData element.  Any errors during the operation will be returned
             as Partial Errors of the ServiceData element.
        """
        ...
    def CloseAllocationWindow(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, Force: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation closes the AllocationWindow and returns the unique identifier
             string of the AllocationWindow business Object in the deleted object list
             of ServiceData.
             

Use Cases:

Use case 1: Close Allocation Window after create 


Create new AllocationWindow, and adding allocations between
             multiple product structure and save, modify further and the AllocationWindow
             will be closed. Any unsaved Allocation changes will not be saved to Teamcenter
             before close.
             



Use case 2: Close Allocation Window after Open


Open an AllocationWindow using an existing AllocationMapRevsion
             object. Add necessary Allocation objects, modify any existing Allocation
             objects, delete any unwanted Allocation. Save the AllocationWindow. Close
             the AllocationWindow. Any unsaved Allocation changes will not be saved
             to Teamcenter when the AllocationWindow closes.
             



Dependencies:

             createAllocationContext
             

Teamcenter Component:

             Allocations - Provides the functionality to map occurrences between two or more structures.
             Currently used in Mechatronics to map logical schematic structures to physical 3D
             structures.
             
        :param AllocWindowInput: 
<b>AllocationWindow</b> object which has changes has to be saved.
             
        :param Force: 
                         For future use.
             
        :return: business object will
             be returned as part of the deleted object list of the ServiceData element. Any errors
             during the operation will be returned as Partial Errors of the ServiceData element.
        """
        ...
    def DeleteAllocationLines(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, InputAllocationLines: list[Teamcenter.Soa.Client.Model.Strong.AllocationLine]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation is used to delete AllocationLine objects created between BOMLine
             objects of different product structures. This operation needs an AllocationWindow
             object with an associated AllocationMapRevision object, also a list of AllocationLine
             objects which  are going to be deleted. This operation will return deleted AllocationLine
             objects unique identifier string in the service data as deleted objects. The deletion
             of AllocationLine objects are only allowed  on a Teamcenter Master site and
             if this operation is attempted from a Replica site then an error will be reported
             and stored as a service data error. If the AllocationWindow has any Incremental
             Context object set, the deletion of AllocationLine will be captured in the
             IncrementalChange business object.
             

Use Cases:

AllocationLine is a runtime representation of an Allocation object
             as well as it provides runtime properties. It will maintain source and target information
             for an Allocation. Use this operation to delete Allocation between different
             aspects of a product.
             

Dependencies:

             createAllocationContext
             

Teamcenter Component:

             Allocations - Provides the functionality to map occurrences between two or more structures.
             Currently used in Mechatronics to map logical schematic structures to physical 3D
             structures.
             
        :param AllocWindowInput: 
<b>AllocationWindow</b> Parent object  from which to remove <b>AllocationLine</b>
                         objects.
             
        :param InputAllocationLines: 
                         A list of <b>AllocationLine</b> objects to be deleted from the <b>AllocationWindow</b>.
             
        :return: 
        """
        ...
    def FindAllocatedBOMViews(self, BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView) -> GetAllocatedBOMViewResponse:
        """    
             The operation identifies all the PSBOMView BusinessObjects that are associated
             to the input PSBOMView Business Object in context of any AllocationMap
             object.
             

Use Cases:

Find any BOMViews which are associated to the input BOMView for Allocation functionality

             One or more BOMViews in the Product Structure are mapped using Allocation functionality
             in context of the AllocationMap object. Allocation objects are created
             between the BOMLine objects of a ProductStructure. If the user needs to identify
             the PSBOMView object which has any allocations associated with the input PSBOMView
             , the operation returns such associated PSBOMView Objects.
             


Dependencies:

             createAllocationContext
             

Teamcenter Component:

             Allocations - Provides the functionality to map occurrences between two or more structures.
             Currently used in Mechatronics to map logical schematic structures to physical 3D
             structures.
             
        :param BomView: 
<b>PSBOMView</b> business object for which associated <b>PSBOMView</b> business object
                         in context of <b>AllocationMap</b> object are to be returned.
             
        :return: 
        """
        ...
    def FindAllocationContexts(self, BomViews: list[Teamcenter.Soa.Client.Model.Strong.PSBOMView]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation identifies the AllocationMap Business objects which are used
             as context for the given input PSBOMView Business objects.
             

Use Cases:

Find AllocationMap objects which are used as context for input PSBOMView
             objects for Allocation functionality

             Two or more PSBOMView of Product Structure are mapped using Allocation
             functionality in context of AllocationMapRevision object. Allocation
             objects are created between the BOMLine objects of ProductStructure. If user
             needs to identify for a given list of PSBOMView objects what are all the AllocationMap
             Business Objects which are used as context, the operation returns such AllocationMapRevision
             Objects.
             


Dependencies:

             createAllocationContext
             

Teamcenter Component:

             Allocations - Provides the functionality to map occurrences between two or more structures.
             Currently used in Mechatronics to map logical schematic structures to physical 3D
             structures.
             
        :param BomViews: 
                         List of <b>PSBOMView</b> objects, for which the Allocation context has to be returned.
             
        :return: 
        """
        ...
    def GetBOMViews(self, AllocationContext: Teamcenter.Soa.Client.Model.Strong.AllocationMapRevision) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             In allocation functionality in context of an AllocationMapRevision object,
             allocations are created between  two or more product structures. This operation returns
             the PSBOMView objects associated to the given AllocationMapRevision
             object.
             

Use Cases:

             For the given AllocationMapRevision object, the PSBOMView objects associated
             to the AllocationWindow object to create allocations are identified and returned.
             

Dependencies:

             createAllocationContext
             

Teamcenter Component:

             Allocations - Provides the functionality to map occurrences between two or more structures.
             Currently used in Mechatronics to map logical schematic structures to physical 3D
             structures.
             
        :param AllocationContext: 
<b>AllocationMapRevision</b> object for which the associated <b>PSBOMView</b> objects
                         are to be identified.
             
        :return: as context
             is returned in the plain objects of ServiceData. Any errors during the operation
             will be returned in the Partial Errors of ServiceData element.
        """
        ...
    def ModifyAllocationLines(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, InputAllocationLines: list[AllocationLineInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation is used to modify AllocationLine objects created between BOMLine
             objects of different product structures which are already present in an AllocationWindow.
             This operation needs an AllocationWindow object with an associated AllocationMapRevision
             object, for which AllocationLine will be modified for source or target BOMLine
             objects and a list of structure AllocationLineInput which consists of AllocationLine
             object and structure AllocationLineInfo. An AllocationLineInfo object information
             like from and to BOMLine objects are used for this modification purpose. This
             operation will return the modified AllocationLine objects in the service data
             as updated objects. If the BOMLine is the same for both source and target,
             then an error will be reported and stored as a service data error.
             

Use Cases:

AllocationLine is a runtime representation of an Allocation object
             as well as it provides runtime properties. It will maintain source and target information
             for an Allocation. Use this operation to modify AllocationLine objects
             between different aspects of a product.
             

Dependencies:

             createAllocationContext
             

Teamcenter Component:

             Allocations - Provides the functionality to map occurrences between two or more structures.
             Currently used in Mechatronics to map logical schematic structures to physical 3D
             structures.
             
        :param AllocWindowInput: 
<b>AllocationWindow</b> parent object for which the <b>AllocationLine</b> objects
                         be modified.
             
        :param InputAllocationLines: 
                         A list of <b>AllocationLine</b> object inputs and their attributes to be modified.
             
        :return: 
        """
        ...
    def SaveAllocationWindow(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Saves any modifications made in the AllocationWindow. Newly created Allocation
             objects will be saved to Teamcenter. Allocation objects which are deleted
             will be removed from Teamcenter. Any modification made to the Allocation will be
             updated in Teamcenter. If any new Incremental Change objects were created in this
             AllocationWindow, they will be saved to Teamcenter. If any AllocationLine
             objects are removed and if it is part of an Incremental Change object, it will be
             removed from Teamcenter. All changes made in the AllocationWindow will be
             saved and after save the AllocationLine objects of the AllocationWindow
             will be returned to the client.
             

Use Cases:

Use case 1: Save Allocation Window after create and add allocations


After creation of a new AllocationWindow new AllocationLine
             objects can be added. After creating necessary allocations, the AllocationWindow
             is saved to save the changes to Teamcenter.
             



Use case 2: Save Allocation Window after open and modification


After creation of a new AllocationWindow or opening an existing
             AllocationWindow, new AllocationLine objects can be added, existing
             allocations can be removed or modified for both source and target. After making necessary
             changes, the AllocationWindow is saved to save the changes to Teamcenter.
             



Dependencies:

             createAllocationContext
             

Teamcenter Component:

             Allocations - Provides the functionality to map occurrences between two or more structures.
             Currently used in Mechatronics to map logical schematic structures to physical 3D
             structures.
             
        :param AllocWindowInput: 
<b>AllocationWindow</b> object for which changes are to be saved.
             
        :return: object
             for which the save is performed will be returned as an updated object of the ServiceData
             element. Any errors during the operation will be returned as Partial Errors of the
             ServiceData element.
        """
        ...

