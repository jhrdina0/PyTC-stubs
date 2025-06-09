import System
import Teamcenter.Services.Strong.Allocations._2007_01.Allocation
import Teamcenter.Services.Strong.Allocations._2011_06.Allocation
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class AllocationRestBindingStub(AllocationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateAllocationContext(self, Input: Teamcenter.Services.Strong.Allocations._2007_01.Allocation.AllocationContextInput) -> Teamcenter.Services.Strong.Allocations._2007_01.Allocation.GetAllocationWindowResponse: ...
    def OpenAllocationWindow(self, AllocWindowInput: Teamcenter.Services.Strong.Allocations._2007_01.Allocation.AllocationWindowInfo, IcContext: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Allocations._2007_01.Allocation.GetAllocationWindowResponse: ...
    def AddAllocationLines(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, InputAllocationLines: list[Teamcenter.Services.Strong.Allocations._2007_01.Allocation.AllocationLineInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ChangeAllocatedBOMWindows(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, AddBOMWindowList: list[Teamcenter.Soa.Client.Model.Strong.BOMWindow], RemoveBOMWindowList: list[Teamcenter.Soa.Client.Model.Strong.BOMWindow]) -> Teamcenter.Services.Strong.Allocations._2007_01.Allocation.GetAllocationWindowResponse: ...
    def ChangeAllocationContext(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, AllocationContext: Teamcenter.Soa.Client.Model.Strong.AllocationMapRevision, AllocationRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule, IcContext: Teamcenter.Soa.Client.Model.Strong.ItemRevision) -> Teamcenter.Services.Strong.Allocations._2007_01.Allocation.GetAllocationWindowResponse: ...
    def ChangeICContext(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, IcContextRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CloseAllocationWindow(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, Force: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteAllocationLines(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, InputAllocationLines: list[Teamcenter.Soa.Client.Model.Strong.AllocationLine]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def FindAllocatedBOMViews(self, BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView) -> Teamcenter.Services.Strong.Allocations._2007_01.Allocation.GetAllocatedBOMViewResponse: ...
    def FindAllocationContexts(self, BomViews: list[Teamcenter.Soa.Client.Model.Strong.PSBOMView]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetBOMViews(self, AllocationContext: Teamcenter.Soa.Client.Model.Strong.AllocationMapRevision) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ModifyAllocationLines(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, InputAllocationLines: list[Teamcenter.Services.Strong.Allocations._2007_01.Allocation.AllocationLineInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SaveAllocationWindow(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateAllocationContext2(self, Input: Teamcenter.Services.Strong.Allocations._2011_06.Allocation.AllocationContextInput2) -> Teamcenter.Services.Strong.Allocations._2007_01.Allocation.GetAllocationWindowResponse: ...

class AllocationService:
    """
    
            The Allocation service exposes operations that are used to establish and maintain
            complex one to many, many to one and many to many relationships between items in
            the Teamcenter system. Common uses for allocations include requirements management,
            systems engineering, and other application domains that require these types of complex
            relationships. These operations can also be used in product configuration applications
            to ensure that design constraints and mandatory selections on product options are
            satisfied.
            

            This service provides the following allocation use cases for the specified set of
            Teamcenter product structures such as requirements, functional, and manufacturing
            structures.
            


Creation of new Allocation between one or more BOMLine objects
            of two or more product structures.
            
Modification of existing Allocation objects, AllocationContext.
            
Query Allocation objects and allocated product structures.
            
Deletion of Allocation objects.
            
Work with Allocation objects in Incremental Context change
            mode by setting incremental Change context object.
            

            .
            

Dependencies:

            StructureManagement
            


Library Reference:

TcSoaAllocationsStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> AllocationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateAllocationContext(self, Input: Teamcenter.Services.Strong.Allocations._2007_01.Allocation.AllocationContextInput) -> Teamcenter.Services.Strong.Allocations._2007_01.Allocation.GetAllocationWindowResponse:
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
    def OpenAllocationWindow(self, AllocWindowInput: Teamcenter.Services.Strong.Allocations._2007_01.Allocation.AllocationWindowInfo, IcContext: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Allocations._2007_01.Allocation.GetAllocationWindowResponse:
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
    def AddAllocationLines(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, InputAllocationLines: list[Teamcenter.Services.Strong.Allocations._2007_01.Allocation.AllocationLineInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def ChangeAllocatedBOMWindows(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, AddBOMWindowList: list[Teamcenter.Soa.Client.Model.Strong.BOMWindow], RemoveBOMWindowList: list[Teamcenter.Soa.Client.Model.Strong.BOMWindow]) -> Teamcenter.Services.Strong.Allocations._2007_01.Allocation.GetAllocationWindowResponse:
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
    def ChangeAllocationContext(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, AllocationContext: Teamcenter.Soa.Client.Model.Strong.AllocationMapRevision, AllocationRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule, IcContext: Teamcenter.Soa.Client.Model.Strong.ItemRevision) -> Teamcenter.Services.Strong.Allocations._2007_01.Allocation.GetAllocationWindowResponse:
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
    def FindAllocatedBOMViews(self, BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView) -> Teamcenter.Services.Strong.Allocations._2007_01.Allocation.GetAllocatedBOMViewResponse:
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
    def ModifyAllocationLines(self, AllocWindowInput: Teamcenter.Soa.Client.Model.Strong.AllocationWindow, InputAllocationLines: list[Teamcenter.Services.Strong.Allocations._2007_01.Allocation.AllocationLineInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def CreateAllocationContext2(self, Input: Teamcenter.Services.Strong.Allocations._2011_06.Allocation.AllocationContextInput2) -> Teamcenter.Services.Strong.Allocations._2007_01.Allocation.GetAllocationWindowResponse:
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

