import Cpd0.Services.Strong.Cpdcore._2011_06.Realization
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class SubsetContentInfo:
    """
    
            Realization to be updated, refreshing the realized content based on changes to the
            source data.
            
    """
    def __init__(self, ) -> None: ...
    Subset: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """A WorkspaceObject for which realization content is to be updated."""
    ExecuteRecipe: bool
    """
            If true, the recipe would be run as part of the realization update. If false,
            the recipe will not be run and the newer versions of source content used during last
            update will be used as selected input.
            """

class SubsetContentsResponse:
    """
    
            Response contains a list of Realizations updated. The serviceData
            contains an added, updated or deleted objects and it also contains a list of any
            errors which occurred within the call.
            
    """
    def __init__(self, ) -> None: ...
    RealizedContent: list[Cpd0.Services.Strong.Cpdcore._2011_06.Realization.RealizedContent]
    """Realized content."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contain a list of added, update or deleted Objects and also list of any errors within
            the call.
            """

class Realization:
    """
    Interface Realization
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def UpdateSubsetsContent(self, SubsetContentInfos: list[SubsetContentInfo]) -> SubsetContentsResponse:
        """    
             This operation is used to check for any updates in the source model i.e. Cpd0CollaborativeDesign
             that have occurred since the last realization update. The list of added, updated,
             and removed content will be returned for each realization input. If the executeRecipe flag is false, the recipe will not be re-executed
             for a recipe based realizations.
             

             This API supports updating content of Cpd0SubsetItemRevision or Cpd0DesignSubsetElement.
             

Cpd0DesignSubsetElement is used to represent a subset of Cpd0CollaborativeDesign
             in a Cpd0Workset. Cpd0DesignSubsetElement objects may be created by
             CAD applications or directly in the Teamcenter RAC user interface using the Collaborative
             Product Development application.
             

Cpd0SubsetItemRevision is a subclass of ItemRevision used to represent
             a subset of Cpd0CollaborativeDesign. Cpd0SubsetItem can be created
             independent of Cpd0Workset. It cannot be a child of Cpd0Workset but
             it can be child of an Item.
             

             The content in a Cpd0SubsetItemRevision will be manifested as traditional
             BOMViewRevision structure upon recipe execution. The mapping functionality
             creates occurrences below the Cpd0SubsetItemRevision in one-to-one correspondence
             with Cpd0DesignElement corresponding to content selected by Cpd0SubsetItemRevision.
             

Use Cases:

             It is used when the user wishes to update the content of a Cpd0SubsetItemRevision
             or Cpd0DesignSubsetElement objects by re-executing its search recipe.
             

             Use Case1 : Update selected content of existing Cpd0SubsetItemRevision or
             Cpd0DesignSubsetElement objects.
             

             The following operation can be used for updating an existing WorkspaceObject
             objects.
             

             The set of content referenced by WorkspaceObject objects can be updated by
             re-executing the search recipe. The application specifies which WorkspaceObject
             objects should have their set of selected content updated.
             
             During the updateSubsetsContent operation,
             the server will find the set of Cpd0CollaborativeDesign content that satisfies
             the search criteria.This set of objects will be updated on the WorkspaceObject
             objects and will remain static until the next call to updateSubsetsContent
             operation.
             
             The search recipe on WorkspaceObject objects is normally changed using the
             setRecipes operation. The updateSubsetsContent can be called after setRecipes in order to update the WorkspaceObject based
             on the new or modified search recipe.
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param SubsetContentInfos: 
                         A list of <font face="courier" height="10">SubsetContentInfo</font> structure. Each
                         structure specifies the <b>WorkspaceObject</b> to be updated.
             
        :return: 
        """
        ...

