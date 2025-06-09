import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class RealizedContent:
    """
    realized content
    """
    def __init__(self, ) -> None: ...
    Realization: Teamcenter.Soa.Client.Model.Strong.Rlz0Realization
    """BusinessObject Reference to the realization Object that was updated"""
    AddedContent: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """
            A list of Model element (e.g design components, design control element) newly added
            to the workset model.
            """
    UpdatedContent: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """
            A list of Model element (e.g design components, design control element) that are
            updated in the workset model.
            """
    UnmappedEffectivityConditionsEncountered: bool
    """
            A list of design components where effectivity conditions are encountered in the realized
            item structure.
            """
    RemovedContent: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """
            A list of Model element (e.g design components, design control element) that are
            removed from the workset model.
            """

class UpdateWorksetSubsetContentInfo:
    """
    
            Realization to be updated, refreshing the realized content based on changes to the
            source data
            
    """
    def __init__(self, ) -> None: ...
    ReuseModelElement: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignSubsetElement
    """Design Subset element for which realization content to be updated."""
    ExecuteRecipe: bool
    """
            Flag indicating if the recipe whould be run as part of the realization update. If
            set to false the recipe will not be run, and the newer versions of source
            content used during last update will be used as selected input.
            """

class UpdateWorksetSubsetContentResponse:
    """
    
            Response to UpdateWorksetSubsetContentResponse
            contains a list of Realizations updated.
            
    """
    def __init__(self, ) -> None: ...
    RealizedContent: list[RealizedContent]
    """realized content"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contain a list of deleted Objects  and also list of any errors which occurred within
            the call.
            """

class Realization:
    """
    Interface Realization
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def UpdateWorksetSubsetContent(self, Input: list[UpdateWorksetSubsetContentInfo]) -> UpdateWorksetSubsetContentResponse:
        """    
             This operation is used to check for any updates in the source model(Product Design)
             that have occurred since the last realization update and reflects any of those changes
             correspondingly in the target model( Workset Model).  The list of added, updated,
             and removed content will be returned for each realization input.  If the executeRecipe flag is set to false, the recipe will not
             be reexecuted for a recipe based realizations.
             

Use Cases:

             A design subset element is used to represent a subset of product design in a workset.
             Design Components may be created by CAD applications or directly in the Teamcenter
             RAC user interface using the Collaborative Product Development application.
             

             This API supports workset authoring use cases; specifically, it is used when the
             user wishes to update the content of a subset by reexecuting its search recipe.
             

             Use Case : Update selected content of existing design subset elements 


             The following operation can be used for updating an existing design subset element
             in a workset
             

Design subset elements are found by the application by expanding
             a workset (see startStructureExpand operation).
             
The set of content referenced by design subset elements can be updated
             by reexecuting the search recipe. This is done by using the updateWorksetSubsetContent operation. The application specifies
             which design subset elements should have their set of selected content updated.
             
During the updateWorksetSubsetContent
             operation, the server will find the set of product design content that satisfies
             the search criteria.This set of objects will be updated on the design subset element,
             and will remain static until the next call to updateWorksetSubsetContent.
             
Note: The search recipe on design subset elements is normally changed
             using the setRecipes operation. The updateWorksetSubsetContent can be called after
             setRecipes in order to update the workset
             based on the new/modified search recipe.
             



Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param Input: 
                         set of realizations to update.
             
        :return: UpdateWorksetSubsetContentResponse contains a vector of set of design model elements.
        """
        ...

