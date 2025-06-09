import System
import System.Collections
import Teamcenter.Services.Strong.Manufacturing._2010_09.Core
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FindNodeInContextInputInfo:
    """
    Input struct for the find node in context service
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """Client ID"""
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """The topline that defines the search scope."""
    Nodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The nodes to search."""
    ByIdOnly: bool
    """If true all abs occs with the same Id will be search for, if no exact apn is matched."""
    AllContexts: bool
    """
            If true then all contexts will be searched otherwise only the current context will
            be searched if no current context specified at the time then the context of the topline
            is used.
            """
    InContextLine: Teamcenter.Soa.Client.Model.ModelObject
    """A more specific scope to searh in."""
    RelationTypes: list[str]
    """A list of relation types, currently only FND_TraceLink relation is supported."""
    RelationDirection: int
    """
            The relation direction to search. The value includes 1(primary), 2(secondary) and
            0(primary and secondary). It is only valid if the relation types are given.
            """
    RelationDepth: int
    """
            The depth to search, -1 to search all levels and any other positive integer value
            to search up to that level. It is only valid if the relation types are given.
            """

class MatchObjectsAgainstVariantRulesArg:
    """
    
            This structure provides input parameters for the matchObjectsAgainstVariantRules
            operation.
            
    """
    def __init__(self, ) -> None: ...
    Objects: list[Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject]
    """
            The objects whose variant definition is to be checked against the set of variant
            rules or product variants. Currently only BOMLines are accepted.
            """
    VariantRules: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The variant rules or product variants which are to be applied consecutively to each
            object. The objects must be of type VariantRule
            or Mfg0BvrProductVariant, respectively.
            """

class MatchObjectsAgainstVariantRulesResponse:
    """
    The response structure for the matchObjectsAgainstVariantRules operation.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData object for this request."""
    Results: list[MatchObjectsAgainstVariantRulesResult]
    """
            A list of result structures; each entry corresponds to an entry in the MatchObjectsAgainstVariantRulesArg
            vector passed to the matchObjectsAgainstVariantRules operation.
            """

class MatchObjectsAgainstVariantRulesResult:
    """
    
            A set of data collected by the matchObjectsAgainstVariantRules operation for
            a specific MatchObjectsAgainstVariantRulesArg structure.
            
    """
    def __init__(self, ) -> None: ...
    Matrix: System.Collections.Hashtable
    """
            A map that holds for each of the runtime objects supplied in the MatchObjectsAgainstVariantRulesArg
            structure the matching variant rules or product variants.
            """
    Warnings: list[str]
    """
            A list of localized warning messages that describe inconsistencies in the configuration
            of the involved windows, if the variant configuration of a window does not satisfy
            the configuration of a supplied variant rule or product variant. The warnings are
            of the form "The window configuration for structure "<top line title>"" is
            missing the following variant rule/product variant(s): <rule-name>, ...".
            """

class Core:
    """
    Interface Core
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindNodeInContext(self, Input: list[FindNodeInContextInputInfo]) -> Teamcenter.Services.Strong.Manufacturing._2010_09.Core.FindNodeInContextResponse:
        """    
             Getting the related objects of the selected object from the target contexts according
             to the input information.
             
        :param Input: 
                         Input struct
             
        :return: The related objects of the input nodes are added to the response.
        """
        ...
    def MatchObjectsAgainstVariantRules(self, Args: list[MatchObjectsAgainstVariantRulesArg]) -> MatchObjectsAgainstVariantRulesResponse:
        """    
             This operation takes a list of pairs of runtime object and variant rule lists and
             determines for each object/variant rule combination of each pair whether the object
             is configured-in for the specified variant rule. Thereby it takes all aspects of
             an object into account that determine the visibility of the object, such as the variant
             conditions of the object itself and of all its parent objects as well as the conditions
             of any assigned object and that of its respective parent objects. The results will
             depend on the configuration state for IC, revision rule, effectivity etc of the implied
             windows, including reference windows.
             
             If a variant rule supplied in the arguments list is not matched by the variant configuration
             of any involved window a warning message will be added to the response structure,
             which indicates that the visibility check regarding the specific variant rule cannot
             be reliably performed because the configuration of the window contradicts the variant
             rule.
             
             This operation currently does not support modular variants. Only saved variant rules
             (business object VariantRule) for the classic variant model are accepted or
             alternatively,  product variants (type Mfg0BvrProductVariant) which are linked
             to VariantRule objects.
             

        :param Args: 
                         A list of structures, where each entry describes a list of runtime objects and a
                         list of variant rules or product variants that are matched against each other.
             
        :return: 300062: If there is no variant rule associated with a product variant.
        """
        ...

