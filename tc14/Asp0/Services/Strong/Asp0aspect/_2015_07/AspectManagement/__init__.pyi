import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExpandAspectsInfo:
    """
    
            A set of inputs, each containing the information needed to execute an expansion of
            a set of aspects to child aspects and possibly related aspects in different aspect
            schemes within the same application model.
            
    """
    def __init__(self, ) -> None: ...
    StartingNodes: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """
            A set of aspects (Asp0Aspect) or engineering objects (Mdl0ModelElement)
            (e.g.any model element that is aspected) for which    an expansion
            is desired.
            """
    ExpansionSemantic: int
    """
            Identifies a specified type of expand or    navigation that is
            desired for the given startingNodes.
            
            Supported values:
            

0 = ChildAspects (startingNodes
            contains aspects for which child aspects are desired),
            
1 = WhereAspected (starting
            Nodes are model elements that are expected to have aspects),
            
2 = OtherSchemeAspects (starting
            Nodes contains aspects from one scheme; resulting content will be aspects in other
            schemes that reference the same model elements as engineering objects.)
            

"""
    ExpandOptionsFlags: System.Collections.Hashtable
    """
            Option map of string to Boolean.
            
            Supported values: IncludeParentChain. When
            IncludeParentChain is set to True, aspect parents up to the top level aspect collector or unassigned
            collector are added to the plain object list in the serviceData
            returned and hence client will be able to quickly access them from any child aspects
            that are returned.
            
            Note: unless specified explicitly, the behaviors of any expand options are only applied
            to resulting nodes, not starting nodes.
            
"""
    ExpandOptions: System.Collections.Hashtable
    """
            Optional map of string to string that specify options to apply to the given expansionSemantic expand.
            
            Supported values:
            
            Key: IncludeAspectsFromSchemes, Values: AllSchemes or comma separated list of Asp0AspectScheme
            type names if only selective Schemes are to be used.
            
            Example: IncludeAspectsFromSchemes = Asp0SchemeFunctional,Asp0SchemeLogical would result
            in Asp0Aspect objects from Asp0SchemeLogical and Asp0SchemePhysical
            to be returned in the response.
            
            Example: IncludeAspectsFromSchemes = AllSchemes
            would result in Asp0Aspect objects from all the schemes in the model to be
            returned in the response.
            """
    LevelsToExpand: int
    """
            The number of levels to expand, where 0    signifies to expand
            all levels, 1 signifies expand the next level only. Values other than 0 or 1 are
            not supported. A value is required.
            """

class ExpandAspectsResponse:
    """
    
            For each starting object and a desired type of expansion, a list of resulting aspects
            will be returned. If there is any exception during the expand of a particular aspect
            or engineering object starting node, the error will be added to the ServiceData object
            and returned as a partial error.
            
    """
    def __init__(self, ) -> None: ...
    ExpandContent: list[ExpandResult]
    """
            Contains aspects from the expansion. They are correlated to the input ExpandAspectsInfo structure by the startingNode (an Mdl0ModelElement)
            and an expansionSemantic.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains any exceptions that occurred. For performance, the service data will be
            populated with all parent aspects if the IncludeParentChain
            expand option is set. This will allow clients to navigate via    
            the Asp0Parent reference on the returned aspects without additional service
            calls.
            """

class ExpandResult:
    """
    
            List of aspect (Asp0Aspect) from the expansion and an expansionSemantic

    """
    def __init__(self, ) -> None: ...
    ExpansionSemantic: int
    """
            The specified type of expand or navigation that resulted in this ExpandResult.
            
            Supported values are:
            

0 = ChildAspects (startingNodes
            contains aspects for which child aspects are desired),
            
1 = WhereAspected (starting
            Nodes are model elements that are expected to have aspects),
            
2 = OtherSchemeAspects (starting
            Nodes contains aspects from one scheme; resulting content will be aspects in other
            schemes that reference the same model elements as engineering objects.)
            

"""
    StartingNode: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """
            The aspect (Asp0Aspect) or engineering object (Mdl0ModelElement) (e.g.any
            model element that is aspected) for which this result is relevant.
            """
    ResultingAspects: list[Teamcenter.Soa.Client.Model.Strong.Asp0Aspect]
    """
            A list of aspects that resulted from the expansionSemantic
            being ChildAspects or WhereAspected.    
            """
    AspectsFromIncludedSchemes: list[Teamcenter.Soa.Client.Model.Strong.Asp0Aspect]
    """
            A list of aspects that resulted either from the expansionSemantic
            being Sibling or IncludeAspectsFromSchemes
            expand option was set.
            """

class GetAspectSchemesInModelOutputInfo:
    """
    
            Output structure contains the list of aspect schemes which are output of SOA operation
            and input application model to which schemes belongs.
            
    """
    def __init__(self, ) -> None: ...
    Model: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """An input Mdl0ApplicationModel."""
    AspectSchemes: list[Teamcenter.Soa.Client.Model.Strong.Asp0AspectScheme]
    """
            List of aspect schemes (Asp0AspectScheme) objects found in the application
            model(model).If no aspect schemes have yet been created in the application model,this
            list will be empty.
            """

class GetAspectSchemesResponse:
    """
    
            Output contains a list of aspect schemes for each requested application model. Service
            data is populated with any exceptions that occurred while performing the operation.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetAspectSchemesInModelOutputInfo]
    """A list of aspect schemes found per requested model."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains any exceptions that occurred while performing the operation."""

class AspectManagement:
    """
    Interface AspectManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExpandAspects(self, AspectExpandInfo: list[ExpandAspectsInfo]) -> ExpandAspectsResponse:
        """    
             This operation allows various types of desired expand and navigation operations on
             aspect and aspect-related model elements (these aspected model elements are also
             called engineering objects.)
             
             If the same input starting node is requested more than once for a given expansion
             semantic, a warning is given and the redundant input is skipped.
             
             If the same input starting node is requested more than once but with different expansion
             semantics, then multiple ExpandResult structures
             will be returned, one for each requested expansion semantic.
             


Use Cases:

             For each input ExpandAspectsInfo:
             
             1. Expand from one aspect to child aspects.
             
             2. Expand from one aspect to other aspects in different aspect schemes in which
             the resulting aspects are related to the same model element as the input aspect.
             
             3. While expanding, include the set of aspect parents at all levels for the resulting
             aspects.
             
             This use case is needed because the parent aspects and the associated engineering
             objects provide context for a given aspect in a particular scheme.
             
IncludeParentChain set to True enables this use case.
             
             4. Expand from one engineering object or model element to its aspects in various
             specified aspect schemes.
             


Dependencies:

             getAspectSchemesInModel
             

Teamcenter Component:

             Aspect Infrastructure Support - Teamcenter component for asp0aspect template
             
        :param AspectExpandInfo: 
                         A set of inputs, each containing the information needed to execute an expansion of
                         a set of aspects to child aspects and possibly related aspects in different aspect
                         schemes within the same application model.
             
        :return: 
        """
        ...
    def GetAspectSchemesInModel(self, InputModels: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel]) -> GetAspectSchemesResponse: ...

