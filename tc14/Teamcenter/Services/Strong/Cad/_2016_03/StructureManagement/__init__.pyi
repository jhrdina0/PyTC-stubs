import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FindModelViewsInStructureResponse:
    """
    
            The response contains any found model view proxies ( FndModelViewProxy) and
            the structure location at which they were found. Also, if the "compareWithMVList"
            option is set to true, then an additional list of model view proxies that are currently
            disclosed but appear to no longer be relevant is returned.
            
            Any errors are returned in the serviceData.
            
    """
    def __init__(self, ) -> None: ...
    ModelViewsByStructureNodes: list[StructureNodeResults]
    """
            A list of proxy objects found for various nodes in the structure - the structure
            nodes may be bomlines, item revisions or design elements depending on the type of
            structure starting scope and disclosure type.
            """
    UnfoundFromModelViewList: list[Teamcenter.Soa.Client.Model.Strong.Fnd0ModelViewProxy]
    """
            The model view proxy objects (Fnd0ModelViewProxy) that are currently associated
            to the specified disclosure but are not found in the given startingScope.
            Note that if the startingScope is not the
            disclosure, that the missing proxy objects may still be present in a disclosure elsewhere
            in its structure. This list is only populated if the compareWithMVList option
            is set to true.
            """
    PossibleMatching: System.Collections.Hashtable
    """
            Map (Fnd0ModelViewProxy, Fnd0ModelViewProxy) of possible matching proxies
            that are equivalent. The keys are proxies in an associated MVList (associated to
            the input structure object or disclosure) that are no longer precisely in the structure
            with the given configuration. The values are the system suggested new proxies that
            are equivalent. This map is only populated if compareWithMVList option is
            set to true.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains a list of any errors which occurred during the operation."""

class StructureNodeResults:
    """
    
            Identifies a list (containing at least one) of model view proxies (Fnd0ModelViewProxy)
            that were found for a particular structure node. Assisting context information (csIdContextOccurrence) may be provided to help
            locate the structure node.
            
    """
    def __init__(self, ) -> None: ...
    StructureNode: Teamcenter.Soa.Client.Model.ModelObject
    """
            A node of the structure for which model views have been found. The structure node
            could either be a BOMLine or for some cases of Workset structure, a
            model element (Mdl0ModelElement).
            """
    ResultingViews: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            List of model view proxies (Fnd0ModelViewProxy) found for the particular structure
            node.
            """
    CsIdContextOccurrence: Teamcenter.Soa.Client.Model.ModelObject
    """
            Contains either the subset in which the structure node resides (either Cpd0SubsetLine
            or Cpd0DesignSubsetElement.) or the startingScope
ItemRevision or BOMLine if multiple startingScope
            values were provided. This object gives context to the associated clonestableIdChain value(s).
            """
    ClonestableId: list[str]
    """
            A list of one or more clone stable occurrence id values used to help locate the structureNode within the csIdContextoccurrence.
            The clone stable occurrence id values are may be ordered from a given startingScope - which is repeated in the StructureNodeResults as the csIdContextOccurrence.
            

            Alternatively, if a Workset is given as a startingScope,
            the csIdContextOccurrence may be a subset
            in the Workset, and only a single cs_id value for the structureNode would be needed since a given model element (Mdl0ModelElement)
            in a subset (Cpd0DesignSubsetElement) can be identified by such a single clone
            stable id.
            

            Also, if the resultingViews are found directly
            off a startingScope, then the csIdContextOccurrence and structureNode
            will both be the startingScope and the clonestableIdChain will be empty as no expansion
            was used to find the resultingViews.
            """

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindModelViewsInStructure(self, Disclosure: Teamcenter.Soa.Client.Model.ModelObject, StructureScope: list[Teamcenter.Soa.Client.Model.ModelObject], ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, WithDisclosureIntent: list[str], Options: System.Collections.Hashtable) -> FindModelViewsInStructureResponse: ...

