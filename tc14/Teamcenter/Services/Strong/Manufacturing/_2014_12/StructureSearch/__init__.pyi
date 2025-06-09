import System
import System.Collections
import Teamcenter.Services.Strong.Manufacturing._2009_10.StructureSearch
import Teamcenter.Soa.Client.Model
import typing

class AdditionalInfo:
    """
    
            a generic structure to capture additional information.

intMapÂ Â Â Â A map of string to a list of integers.

dblMapÂ Â Â Â A map of string to a list of doubles.

strMapÂ Â Â Â A map of string to a list of strings.

objMapÂ Â Â Â A map of string to a list of BusinessObjects.

dateMapÂ Â Â Â A map of string to a list of dates.

    """
    def __init__(self, ) -> None: ...
    IntMap: System.Collections.Hashtable
    """A map (string/list of integers) of generic key to integer values."""
    DblMap: System.Collections.Hashtable
    """A map (string/list of doubles) of generic key to double values."""
    StrMap: System.Collections.Hashtable
    """A map (string/list of strings) of generic key to string values."""
    ObjMap: System.Collections.Hashtable
    """
            A map (string/list of BusinessObjects) of generic key to  BusinessObject
            values.
            """
    DateMap: System.Collections.Hashtable
    """A map (string/list of dates) of generic key to date values."""

class KeyValuePair:
    """
    A generic name/value pair construct.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """name of a key"""
    Value: str
    """property value."""

class AssignmentRecipeSearchCriteria:
    """
    search criteria
    """
    def __init__(self, ) -> None: ...
    ObjectTypes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """the types of objects to search."""
    LogicalDesignator: KeyValuePair
    """name, value attributes of logicalDesignator"""
    Refinements: list[Teamcenter.Services.Strong.Manufacturing._2009_10.StructureSearch.MFGSearchRefinementSet]
    """refinements on the search"""
    AbsoccAttributes: list[KeyValuePair]
    """KeyValue Pairs for each attribute on AbsOccurrence to be used in search."""

class CreateOrUpdateAssignmentRecipeInputElem:
    """
    
An element defining the content and context for attaching the recipe to be used
to
populating child nodes.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """name of the recipe."""
    RecipeAnchorOrRecipe: Teamcenter.Soa.Client.Model.ModelObject
    """
            The anchor to which the recipe definition will be attached after creation of recipe,
            or the recipe to be updated.
            """
    SearchContextSC: Teamcenter.Soa.Client.Model.ModelObject
    """
            The object containing the details of search fields supported by cacheless search.
            Currently, this must be a StructureSearchContext with details of cacheless search
            attributes.
            """
    AdditionalSearchCriteria: AssignmentRecipeSearchCriteria
    """additional search criteria with manufacturing aspects."""
    AppKey: str
    """
            A unique key used for choosing the right resolver object. Currently, only supports
            Mfg0AssignmentRecipe
            """

class CreateOrUpdateAssignmentRecipeResp:
    """
    
CreateOrUpdateAssignmentRecipeResp structure contains a list of AdditionalInfo
elements,
the size of which matches the input element list. It also includes the standard
serviceData
object. Each element contains the recipe object ( stringToObjVector with key
"CreatedObject"
or "UpdatedObject" and value being the Mfg0MEMBOMRECIPE). In case there is
a failure - the element content will be empty - and the serviceData will have
the
details of the failure for that particular element.

    """
    def __init__(self, ) -> None: ...
    Info: list[AdditionalInfo]
    """
            A list of AdditionalInfo structures. If recipe is created, the objMap member will
            have the key "CreatedObject" with the value being the Mfg0MEMBOMRecipe object.
            If recipe is updated the objMap member will have the key "UpdatedObject". The strMap
            member will have the "Name" key with the value being a element of size one having
            the name of the recipe.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""

class GetAssignmentRecipesResp:
    """
    
GetAssignmentRecipesResp structure contains a list of AdditionalInfo elements,
the
size of which matches the input recipeAnchor list. It also includes the standard
serviceData object.
    """
    def __init__(self, ) -> None: ...
    Info: list[AdditionalInfo]
    """
            A list of AdditionInfo structures. If the recipe is found objMap member will have
            the key "Recipe" and the Mfg0MEMBOMRecipe objects as the values, the strMap
            will have "Name" for key and the corresponding names of the recipes, the objMap will
            have "Anchor" to indicate the BOMLine object owning the recipe.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data capturing partial errors using the input array index as client id."""

class ResolveAssignmentRecipeInputElement:
    """
    Element decribing the input for resolveAssignmentRecipe.
    """
    def __init__(self, ) -> None: ...
    RecipeAnchor: Teamcenter.Soa.Client.Model.ModelObject
    """
            The object on or below which the recipe should be resolved. Currently, only BOMLine
            objects are supported.
            """
    RecipeObjs: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of recipe objects that are a subset of recipes attached to recipeAnchor. If
            this list is not empty there is no search performed on recipeAnchor to get any recipe
            objects for resolve. Currently, this object must be of type Mfg0MEMBOMRecipe.
            """
    SearchScopes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The Engineering BOM (EBOM) scopes to resolve the objects to be assigned to skeletal
            Manufacturing BOM (MBOM). Currently, only the root scope ( EBOM root ) BOMLine
            is supported.
            """
    ReResolve: bool
    """
            If true force resolve by eliminating previous result. Should be true unless, already
            resolved lines are being asked for.
            """
    RemovePreviouslyResolved: bool
    """If true, any previously resolved lines are removed."""
    Recursive: bool
    """If true, recursively resolve under the given recipe anchor"""
    GenerateLog: bool
    """
            If true, generates a log file with details of the resolved lines for given recipe
            under a parent line.
            """
    AppKey: str
    """
            The application key to decide which resolver to use. Currently, only key supported
            is Mfg0AssignmentRecipe.
            """

class ResolveAssignmentRecipeResp:
    """
    
ResolveAssignmentRecipeResp structure contains a list of AdditionalInfo
elements,
the size of which matches the input element list. It also includes the standard
serviceData
object.
    """
    def __init__(self, ) -> None: ...
    Info: list[AdditionalInfo]
    """
            A list of AdditionInfo structures. The names of the resolved recipes appear under
            the "Recipe" key of strMap. Each value in this strMap is a further key into objMap
            and the values for those are the resolved BOMLine objects. Any BOMLine
            objects that are manually assigned from EBOM to MBOM appear under the objMap key
            "Manual", with the values being the BOMLine objects that were manually assigned.
            If "generateLog" is true in the input then a file ticket is generated under the "LogFileTicket"
            key of strMap of the first element in this list.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData to caputre partial errors."""

class StructureSearch:
    """
    Interface StructureSearch
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateAssignmentRecipe(self, Input: list[CreateOrUpdateAssignmentRecipeInputElem]) -> CreateOrUpdateAssignmentRecipeResp:
        """    
             This operation creates or updates the search recipe on a Manufacturing BOM (MBOM)
             node. The recipe is used to automatically resolve Engineering BOM (EBOM) lines under
             the MBOM node with the recipe. If recipe is updated after a prior resolve there must
             be a subsequent call to resolve the new recipe using the resolveAssignmentRecipe.
             The operation will throw an ServiceException if the Teamcenter database schema does
             not have the recipe constructs. It requires the recipe to be provided as a SearchStructureContext
             object (capturing structure search parameters) and/or key-value pairs of AbsOccurrence
             attributes.
             

Use Cases:

             There is a need to automatically consume Engineering BOM (EBOM) nodes under a phantom
             Manufacturing BOM (MBOM) node based on search criteria provided by Structure Search.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         A list of input elements specifying the details of the recipe to be created and attached
                         to a given node.
             
        :return: 
        """
        ...
    def DeleteAssignmentRecipes(self, Recipes: list[Teamcenter.Soa.Client.Model.ModelObject], RecipeAnchors: list[Teamcenter.Soa.Client.Model.ModelObject], ContextForRemovingResolvedObjs: Teamcenter.Soa.Client.Model.ModelObject, AppKey: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes the given explit recipe (Mfg0MEMBOMRecipe) objects.
             Optionally, can delete all recipe objects attached to the recipeAnchors ( BOMLine
             Objects). If the contextForRemovingResolvedObjs is provided, the resolved lines will
             be removed unless those are resolved by other recipes too. Pass NULL for this parameter
             if resolved lines are not to be cleaned up.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Recipes: 
                         A list of <b>Mfg0MEMBOMRecipe</b> objects to be deleted.
             
        :param RecipeAnchors: 
                         A list of  <b>BOMLine</b> objects for which recipes are to be deleted.
             
        :param ContextForRemovingResolvedObjs: 
                         An optional BOMWindow object to indicate resolved lines are to be deleted too.
             
        :param AppKey: 
                         The name of the Application to identify the resolver in the server. Currently, only
                         allowed value is Mfg0AssignmentRecipe.
             
        :return: 
        """
        ...
    def GetAssignmentRecipes(self, RecipeAnchors: list[Teamcenter.Soa.Client.Model.ModelObject], RecipeNames: list[str], AppKey: str) -> GetAssignmentRecipesResp:
        """    
             This operation get the recipe (Mfg0MEMBOMRecipe) objects attached to the underlying
             ItemRevisions of the recipeAnchors. Currently, only BOMLine objects can be
             specified as recipeAnchors.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param RecipeAnchors: 
                         A list of  <b>BOMLine</b> Objects for which recipes are to be obtained.
             
        :param RecipeNames: 
                         An optional list of recipeNames to search for recipes under the specified recipeAnchors.
             
        :param AppKey: 
                         The name of the Application to identify the resolved in the server. Currently, only
                         allowed value is Mfg0AssignmentRecipe.
             
        :return: 
        """
        ...
    def ResolveAssignmentRecipe(self, Input: list[ResolveAssignmentRecipeInputElement]) -> ResolveAssignmentRecipeResp:
        """    
             This operation resolves the saved search recipe on a Manufacturing BOM (MBOM) node.
             The recipe is used to automatically resolve Engineering BOM (EBOM) lines under the
             MBOM node with the recipe. The operation will throw an ServiceException if the Teamcenter
             database schema does not have the recipe constructs.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         A list of ResolveAssignmentRecipeInputElement structures each detailing the node
                         on which the recipe is to be resolved.
             
        :return: 
        """
        ...

