import Mdl0.Services.Strong.Modelcore._2011_06.Search
import Mdl0.Services.Strong.Modelcore._2013_05.Search
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GeomConstraintExpression:
    """
    Search expression structure for geometric constraint collection search.
    """
    def __init__(self, ) -> None: ...
    SourceElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """List of source Mdl0ModelElement whose GeomConstraint is to be searched."""
    ProcessCtrlFlag: int
    """
            An integer value between 0 to 15 (4 bits) which indicates how the search result of
            the source criteria are treated to fetch the related constraint data.
            
            The value sets the bits used for following flags (in same order of the list). Mainly
            values 5, 6, 7, 13, 14, 15 are needed by the users.
            

AppendRelatedBackgroundToResults
            
AppendRelatedForegroundToResults
            
TreatSourceAsBackground
            
TreatSourceAsForeground
            


            E.g.
            
            GCC1 (Geometric Constraints Collection 1)
            
            FG (Foreground)
            
            DE1.1
            
            BG (Background)
            
            DE2.1
            
            GCC2
            
            FG
            
            DE2.1
            
            DE4.1
            
            DE5.1
            
            BG
            
            DE3.1
            
            GCC3
            
            FG
            
            DE2.2
            
            DE6.1
            
            DE7.1
            
            BG
            
            DE3.1
            

            Input:  DE2.1 and mdl0processCtrlFlag=5
            
            Output : DE2.1,DE4.1 and DE5.1
            
            Explanation :  Search should find GCC2 where DE2.1 is a fore ground member. Then
            append the other foreground members(DE4.1 and DE5.1) of the GCC to result.
            """
    SourceCriteria: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchDef
    """Source Search Criteria on which the constraint search term is to be applied."""

class GeomConstraintExpressionInput:
    """
    Geometric Constraint Collection Expression Input - Request Structure.
    """
    def __init__(self, ) -> None: ...
    GeomConstraintExpression: GeomConstraintExpression
    """Search expression object for geometric constraint collection search."""
    Clientid: str
    """
            A unique string sent by the calling function, so that the output Search Expression
            object could be mapped back to the input.
            """

class SearchExpressionSet2:
    """
    Building block to build complex search expressions.
    """
    def __init__(self, ) -> None: ...
    SearchOperator: str
    SearchExpression: Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchExpression
    """
            Search Expressions to be executed. In case of more than one an OR operator is assumed
            between these expressions. Either one of the properties will be populated: i.e. searchOperator and searchExpressionSets
            or the searchExpression, in a structure.
            """
    SearchExpressionSets: list[SearchExpressionSet2]
    """List of search expressions combined by the search operator."""
    GroupName: str
    """
            Optional name for a group expression.
            
            A group expression has both a searchOperator
            and a non-empty searchExpressionSets.
            
            If groupName is the empty string, the group
            has not been named.
            """

class SearchRecipe2:
    """
    Recipe for executing the Search
    """
    def __init__(self, ) -> None: ...
    Scope: Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchScope
    """Scope of Search  Model, search types"""
    ConfigDetails: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ConfigurationDetail]
    """
            List of Configuration information to apply. Configuration information specifies the
            RevisionRule and optional effectivity and variant configuration.
            
            Configuration information is required for Universal configuration and optional for
            Partition configuration. If more than one list member specifies Universal configuration,
            the last one is used. If more than one list member specifies Partition configuration,
            the last one is used.
            """
    SearchExpression: SearchExpressionSet2
    """Expression set to be evaluated  search criteria"""

class RecipeData2:
    """
    
            This data structure associates a search recipe to its recipe container. It is used
            to save search recipes against a recipe container.
            
    """
    def __init__(self, ) -> None: ...
    RecipeContainer: Teamcenter.Soa.Client.Model.ModelObject
    """
            Object reference to a recipe container. This object could be either of
            

Mdl0SubsetDefinition

Cpd0DesignSubsetInstance

Ptn0Partition

Mdl0BaselineDefinition


"""
    Recipe: SearchRecipe2
    """
            Associated Search Recipe. The Search Recipe is defined by the SearchRecipe2 data
            structure, which has the following contents:
            

scope   Scope of the Search
            (Application Model, search types).
            
configDetails   Configuration
            information used in the search (RevisionRule and optional effectivity and
            variant configuration).
            
searchExpression   Top level
            SearchExpressionSet2 that could be any level
            deep and defines a complex search recipe by combining the elemental Search Expressions
            created by createSearchExpressions operation.
            

"""

class RecipeResponse2:
    """
    Response for a Get Recipe Call. Returns the search recipe attached to a RecipeContainer.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service Data for error information. The following are errors thrown by the getRecipes2 operation in the ServiceData structure:
            
Mdl0Model_invalid_recipe_container (278017)
            The recipe container object passed as input is not a valid recipe container object.
            The recipe container has to be one of Mdl0SubsetDefinition, Ptn0Partition
            or Cpd0DesignSubsetInstance.
            
MDL0MODEL_invalid_recipe_to_load (278027)
            The recipe container object has a search recipe that is not a valid object. The
            search criteria objects are of class ApprSearchCriteria (and its subtypes)
            and if these are combined in a fashion that is not readable by the CPD application
            then this error would be thrown
            
"""
    SearchRecipes: list[RecipeData2]
    """
            Recipe Data for the given RecipeContainer objects. The RecipeData2 structure returns the following information:
            

recipeContainer  The reference
            to the RecipeContainer object from which the recipe is retrieved .
            
recipe   The SearchRecipe2 data structure that returns the scope, configuration
            details and the search expression set that represents the stored search recipe.
            

"""

class SearchExpressionInput:
    """
    Input Data Structure to create the Group of Elemental Search Expressions
    """
    def __init__(self, ) -> None: ...
    ProximitySearchExpressions: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ProximitySearchExpressionInput]
    """
            Input for creating Proximity Search Expressions. Contains reference to a set of <font
            face=&quot;courier&quot; height=&quot;10&quot;>ModelElements</font>
            (that are targets) and the proximity distance.
            """
    BoxZoneExpressions: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.BoxZoneExpressionInput]
    """
            input for creating box zone search expressions. Contains the Min and Max coordinated
            of a test Box definition.
            """
    PlaneZoneExpressions: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.PlaneZoneExpressionInput]
    """
            input for creating plane zone search expressions. Contains a point in the plane and
            the normal vector definition.
            """
    SavedQueryExpressions: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.SavedQueryExpressionInput]
    """
            input for creating saved query search expressions. Contains reference to a stored
            saved query object and a coordinated list of entries and values to be used in the
            saved query. Some queries may contain empty list for entries and values (depends
            on the definition of the Saved Query). Wildcards are accepted for values in the Saved
            Query.
            """
    ClosureQueryExpression: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ClosureQueryExpressionInput]
    """
            Closure Query Expression  that traverses results using a closure rule  Not implemented
            in Tc9.1.0 or Tc10.1.0.
            """
    OptionSetExpressions: list[Mdl0.Services.Strong.Modelcore._2013_05.Search.OptionSetExpressionInput]
    """
            Option Set Expression that defines the Transfer Option Set and option values that
            are used traverse the closure defined for the Transfer Option Oet
            """
    GeomConstraintExpressions: list[GeomConstraintExpressionInput]
    """
            input for creating geometric constraint collection search expressions. Contains an
            integer flag that indicates how the search result is treated to fetch the related
            constraint data and reference to source search criteria on which the constraint search
            term is to be applied.
            """
    IncludeElements: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ModelElementInput]
    """
            References to elements to be included into the search results. The server creates
            a Search Expression for this input as well, so that it could be combined with other
            search expressions in a search recipe.
            """
    ExcludeElements: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ModelElementInput]
    """
            Reference to elements that should be explicitly excluded in the search results. Again
            a search expression is returned for the exclude elements so that it could be combined
            with other search expressions in a search recipe.
            """

class Search:
    """
    Interface Search
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AggregateRecipes(self, RecipeContainers: list[Teamcenter.Soa.Client.Model.ModelObject]) -> RecipeResponse2:
        """    
             Return the aggregate recipe for each given recipe container. Recipe containers are
             not modified by this operation; however the aggregate recipes returned are suitable
             for storage using the operation setRecipes2.
             
                 
             
             For an Mdl0BaselineDefinition recipe container, the aggregate recipe is formed
             from the baseline definition recipe and the recipe of each supporting baseline (see
             relation Mdl0SupportingBaseline) in the following way:
             

             1. The aggregate recipe is set to a copy of the baseline definition recipe.
             

             2. Each supporting recipe is assigned a name using the display name of its owning
             Mdl0Baseline.
             

             3. For each supporting recipe group:
             
             If the aggregate group contains one or more recipe groups which match the assigned
             name: the contents of each group is replaced with a copy of the supporting recipe.
             
             Else: the aggregate group is appended to the recipe, using a recipe group with the
             assigned name.
             

             4. New groups are appended using the OR operator.
             

             For all other recipe containers the aggregate recipe is identical to the recipe returned
             by operation getRecipes2.
             


Use Cases:

             A user is constructing an aggregate baseline from a number of supporting baselines.
             Construction has now finished on the supporting baselines, and the user wishes to
             pull the recipes from the supporting baselines into the aggregate baseline. Call
             the aggregateRecipes operation to pull the
             recipes together, confirm any changes with the user, then call the setRecipes2 operation to save the changes.
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param RecipeContainers: 
                         Reference to <b>RecipeContainer</b> objects. The input vector could contain any Teamcenter
                         object that exhibits a <b>RecipeContainer</b> behavior.
             
        :return: 
        """
        ...
    def CreateSearchExpressions(self, SearchExpInput: SearchExpressionInput) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchExpressionResponse:
        """    
             This operation creates the elemental search expressions that could be combined using
             logical operators to build up a complex search recipe in CPD application. The createSearchExpressions
             operation could be used to create multiple search expressions at the same time. The
             following types of expressions could be created by this operation
             

Bounding Box Expression (Mdl0SearchBoxZone)
             
Plane Zone Expression (Mdl0SearchPlaneZone)
             
Proximity Expression (Mdl0SearchProximity)
             
Saved Query Expression (Mdl0SearchSavedQuery)
             
Geometric Constraint Expression (Mdl0SearchGeomConstraint)
             
Include Content Expression (Mdl0SearchSlctContent)
             
Exclude Content Expression (Mdl0SearchGroup)
             



Use Cases:

             The createSearchExpressions is a required operation before an executeSearch or setRecipes
             call is made. This operation creates the runtime Search Definition objects based
             on the input search expression data structures. The intent of this operation is to
             create all the individual elemental search expressions so that they could be combined
             using logical operators (AND/OR/NOT) to create a complex search recipe.
             

Dependencies:

             createSearchExpressions
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param SearchExpInput: 
                         Search Expression Input Structure
             
        :return: SearchExpressionResponse data structure that returns the Search Expression objects
             created for the given Search Expression Input data structures.
        """
        ...
    def GetRecipes2(self, RecipeContainers: list[Teamcenter.Soa.Client.Model.ModelObject]) -> RecipeResponse2:
        """    
             This operation retrieves the stored recipe against a set of recipe container objects.
             The persistent objects used to store the search recipe in Teamcenter are objects
             that do not have lifecycle by itself, so they are always associated to objects that
             exhibit the RecipeContainer behavior. In the current CPD application there are four
             objects that exhibit RecipeContainer behavior. They are:
             

             Mdl0SubsetDefinition:  object to store a search recipe (without the results).
             
             Ptn0Partition:   A dynamic partition that executes the search recipe to find
             its members.
             
             Cpd0DesignSubsetInstance:  A realization object that takes a subset of a Product
             Design and instantiates into a Workset.
             
Mdl0BaselineDefinition: object to store a search recipe (without the results)
             for use an Mdl0BaselineRevision.
             

             The retrieved recipe from the recipe container is translated to the data structures
             defined in the search operation and then it is presented back to the caller.
             

Use Cases:

             This operation supports the use case of retrieving a stored search recipe from Teamcenter
             DB against a recipe container object. The retrieved recipe could be re-executed by
             calling the executeSearch operation.
             


Dependencies:

             getRecipes2
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param RecipeContainers: 
                         reference to RecipeContainer Objects. The input vector could contain any Teamcenter
                         object that exhibits a RecipeContainer behavior.
             
        :return: 
        """
        ...
    def SetRecipes2(self, RecipeInputs: list[RecipeData2]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation saves a search recipe as persistent objects in Teamcenter. The stored
             recipe could be retrieved using getRecipes2
             operation. This is a bulk operation, i.e. it can store multiple complex search recipes
             in a single call.
             
             The persistent objects used to store the search recipe in Teamcenter are objects
             that do not have lifecycle by itself, so they are always associated to objects that
             exhibit the RecipeContainer behavior. In the current CPD application there
             are four objects that exhibit RecipeContainer behavior. They are:
             

Mdl0SubsetDefinition: object to store a search recipe (without the results).
             


             Ptn0Partition: A dynamic partition that executes the search recipe to find its
             members.
             


             Cpd0DesignSubsetInstance: A realization object that takes a subset of a Product
             Design and instantiates into a Workset.
             


             Mdl0BaselineDefinition: object to store a search recipe (without the results)
             for use with historical dataan Mdl0BaselineRevision.
             

             Note that the recipe is deleted when its container object is deleted.
             

Use Cases:

             The setRecipes2 operation is used to save
             search recipes against a Recipe Container object. Apart from capturing the logical
             combination of search expressions, the setRecipes2
             operation also stores the current configuration conditions against the RecipeContainer
             object (including RevisionRule and optional effectivity and variant configuration),
             except in the case of Ptn0Partition object. Ptn0Partition object does
             not provide a persistence mechanism for the configuration conditions and it uses
             the configuration set in the current CPD application.
             
             The search recipes are stored as ApprSearchCriteria objects in Teamcenter
             and ApprSearchCriteria object hierarchy has a subclass to store each Search
             expression separately.
             


Dependencies:

             convertEffectivityExpressions, createOrUpdateConfigurations, createSearchExpressions
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param RecipeInputs: 
                         List of Recipe Data that should be set for specific Container Objects
             
        :return: 
        """
        ...

