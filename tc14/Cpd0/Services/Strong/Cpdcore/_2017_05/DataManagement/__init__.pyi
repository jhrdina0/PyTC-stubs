import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class SubsetItemData:
    """
    
            This structure contains the required information that can be returned to service
            caller such as instantiated objects, removed objects and added objects for a particular
            container object provided/created.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string supplied by the caller. It can be empty if SubsetItemInfo
            do not have clientID populated.
            """
    SubsetItem: Teamcenter.Soa.Client.Model.Strong.Cpd0AbsSubsetItm
    """The Cpd0SubsetItem created."""
    SubsetItemRevision: Teamcenter.Soa.Client.Model.Strong.Cpd0AbsSubsetItmRevision
    """The Cpd0SubsetItemRevision created."""
    SubsetItemInstance: Teamcenter.Soa.Client.Model.Strong.Cpd0SubsetItemInstance
    """The Cpd0SubsetItemInstance created."""
    AppendedSourceElementList: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """Contains list of appended source elements."""
    RemovedSourceElementList: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """Contains list of removed source elements."""

class SubsetItemInfo:
    """
    
SubsetItemInfo is used as input to describe
            create or update request for a Cpd0SubsetItemRevision. New Cpd0SubsetItemRevision
            objects require creation of Cpd0SubsetItem and Cpd0SubsetItemInstance
            objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify returned SubsetItemData elements and Partial Errors associated
            with this input SubsetItemInfo. This is an
            optional argument.
            """
    Element: Teamcenter.Soa.Client.Model.Strong.Cpd0AbsSubsetItmRevision
    """Existing Cpd0AbsSubsetItmRevision that needs to be updated."""
    BoType: str
    """
            If specified, a new Cpd0SubsetItem is created. This value is required for
            creating new a Cpd0SubsetItem and must be a valid subtype of Cpd0SubsetItem.
            For an update of an existing Cpd0SubsetItemRevision, this value should be
            empty.
            """
    ViewType: str
    """
BOMView type. If empty, the system preference 4G_SubsetItem_view_type
            is used to get the view type.
            """
    SourceModel: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The Cpd0CollaborativeDesign from which content is being instanced. Optional
            for update use case.
            """
    Transform: list[float]
    """
            Absolute transform which positions the shape in the coordinate system of the Cpd0CollaborativeDesign
            (units in meters), empty = identity, otherwise contains 16 doubles in the following
            order: { r00, r10, r20, p0, r01, r11, r21, p1, r02, r12, r22, p2, t0, t1, t2, s },
            where the letter prefix signifies the following:
            

r a rotation component
            
p a perspective component
            
t a translation component
            
s the inverse scale
            

"""
    AttrInfo: System.Collections.Hashtable
    ApplyTargetPropertiesToElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """
            A list of business objects to which target properties needs to be applied from the
            associated Cpd0SubsetDefaults object. This parameter is optional.
            """
    AppendSourceElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """
            A list of business objects to be append from sourceModel
            into the Cpd0SubsetItemRevision i.e. the list of objects to be appended from
            sourceModel into Cpd0SubsetItemRevision.
            """
    RemoveSourceElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """
            A list of business objects to be removed from the Cpd0SubsetItemRevision.
            It is expected that this parameter contains the complete list of presented parent
            Cpd0DesignElements and the actual Cpd0DesignElements to be removed
            unless removechildrenautomicatlly is set
            to true.
            """
    UpdateRecipeForAppendsAndRemoves: bool
    """
            If true, the recipes include/exclude elements criteria will be modified accordingly
            based on appendSourcElements and removeSourceElements input arguments.
            """
    SubsetDef: Teamcenter.Soa.Client.Model.Strong.Mdl0SubsetDefinition
    """
            The Cpd0SubsetDefinition business object. Instead of explicitly passing Cpd0DesignElement
            to be added or removed in a Cpd0SubsetItemRevision, user can choose to pass
            a Cpd0SubsetDefinition as an input such that all the Cpd0DesignElements
            fulfilling the recipe criteria will be instanced into Cpd0SubsetItemRevision.
            """
    RemoveChildrenAutomatically: bool
    """
            If true, the children of Cpd0DesignElements specified in removeSourceElements input parameter will be removed from Cpd0SubsetItemRevision
            also. If false, it is expected that removeSourceElements
            contains complete hierarchy of Cpd0DesignElements to be removed.
            """
    GuardObjLastModifiedDate: bool
    """
            If true, the update of Cpd0DesignElement to check last modified date
            to avoid data overwrites.
            """
    ObjLastModifiedDateGuard: System.DateTime
    """
            Modification date guard is used if guardObjLastModifiedDate
            is set to true. Object update will abort if the last modified date of the
            object is greater than objLastModifiedDateGuard.
            """

class SubsetItemsResponse:
    """
    
            The response contains information about Cpd0SubsetItemRevision created or
            updated & its clientId. It also contains
            a list of appended and removed Cpd0DesignElements from the Cpd0SubsetItemRevision.
            The serviceData contains a list of added,
            updated, or deleted objects and it also contains a list of any errors which occurred
            within the call.
            
    """
    def __init__(self, ) -> None: ...
    SiData: list[SubsetItemData]
    """
            A list of Cpd0SubsetItemRevision data which has one to one correspondence
            with input SubsetItemInfo.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Added, updated, deleted object data plus any error information."""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateSubsetItems(self, SubsetItemInfos: list[SubsetItemInfo]) -> SubsetItemsResponse:
        """    
             This operation creates or updates Cpd0SubsetItemRevision based on input structure
             SubsetItemInfo. A Cpd0SubsetItemRevision
             is a subclass of ItemRevision used to represent a subset of Cpd0CollaborativeDesign.
             

             A Cpd0DesignElement represents the use of a standard part design, a design
             component, or a design assembly in a product. A reuse Cpd0DesignElement
             instances the assembly into a Cpd0CollaborativeDesign and the subordinates
             which result by the realization process using the Collaborative Product Development
             application.
             

Reuse, subordinate, and shape Cpd0DesignElement classes
             all represent occurrences of Items in the Cpd0CollaborativeDesign.
             As such they can be mapped to PSOccurrence in a structure below the new Cpd0SubsetItemRevision.
             Cpd0DesignFeature and Cpd0DesignElement having a categories promissory and modelreuse are not supported.
             

Cpd0SubsetItem can be created independent of Cpd0Workset. It cannot
             be a child of Cpd0Workset but it can be child of an Item.
             

             The content in a Cpd0SubsetItemRevision will be manifested as traditional
             BOMViewRevision structure upon recipe execution. The mapping functionality
             creates occurrences below the Cpd0SubsetItemRevision in one-to-one correspondence
             with Cpd0DesignElement corresponding to content selected by Cpd0SubsetItemRevision.    
             

             The search recipe on Cpd0SubsetItemRevision is normally changed using the
             setRecipes operation. The createOrUpdateSubsetItems supports limited recipe modification
             indirectly by adding lists of Cpd0DesignElements for inclusion or exclusion
             from the current search recipe stored on the  Cpd0SubsetItem.
             

Use Cases:

             This API supports the Cpd0SubsetItemRevision authoring use cases. New Cpd0SubsetItemRevision
             objects require creation of a new Cpd0SubsetItem and Cpd0SubsetItemInstance
             objects.
             

             Use Case 1: Creation of new Cpd0SubsetItem


             Pre condition: Cpd0DesignElement exist in a Cpd0CollaborativeDesign.
             
             The following operation can be used for creating Cpd0SubsetItems


New Cpd0SubsetItem can be created using the createOrUpdateSubsetItems operation.
             
After the Cpd0SubsetItem is created, the application may save
             a search recipe on the Cpd0SubsetItemRevision using the setRecipes operation.
             



             Use Case 2: Update of existing Cpd0SubsetItemRevision


             The following operation can be used for updating an existing Cpd0SubsetItemRevision.
             

Cpd0SubsetItemRevision can be updated using the createOrUpdateSubsetItems operation. The application specifies
             which Cpd0SubsetItemRevisions are to be updated.
             
The application sets changed property values.
             



Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param SubsetItemInfos: 
                         A list of <font face="courier" height="10">SubsetItemInfo</font> structure. Each
                         structure specifies the <b>Cpd0SubsetItemRevision</b> to be created or updated.
             
        :return: 
        """
        ...

