import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FindAffectedCCsOutput:
    """
    
The output object for FindAffectedCCs SOA.

This object contains a list of FindAffectedOutputObject. This vector represents
all
of the queried objects and all of the affected CCs.
    """
    def __init__(self, ) -> None: ...
    AffectedObjects: list[FindAffectedOutputObject]
    """
            Each vector node inside "affectedObjects" includes  a quaried item and a single Collaboration
            Context. For example, if CC1 (Collaboration Context) and CC2 (Collaboration Context)
            contain inside their process structures both item1 and item 2 and the two items are
            quaried for affected Collaboration Contexts, the output will be as follows:
            
            1. Item1, CC1
            
            2. Item1, CC2
            
            3. Item2, CC1
            
            4. Item2, CC2
            

            Each of the items is represented by two vector nodes, one vector node for each relation
            to a CC.
            """

class FindAffectedCCsResponse:
    """
    A list of output objects and a service data.
    """
    def __init__(self, ) -> None: ...
    Output: list[FindAffectedCCsOutput]
    """
            The output data includes the affected CCs and the items which is related to each
            CC.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data output."""

class FindAffectedOutputObject:
    """
    The output object which contains the queried object and one of it's related CCs
    """
    def __init__(self, ) -> None: ...
    QueryObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The item queried for affected CCs."""
    AffectedCC: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """One of the affected CCs of the query item."""

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindAffectedCCs(self, Objects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]) -> FindAffectedCCsResponse:
        """    
             This operation finds all of the Collaboration Contexts which contain a process structure,
             which contains the input objects (e.g. Item, MEWorkArea, METool, MEProcess or MEOperation).
             The input objects must be of type Item or ItemRevision (BOMLine objects are not valid
             input objects).
             

Dependencies:

             whereReferenced
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Objects: 
                         The items to find their Collaboration Contexts (as a reference).
             
        :return: 300070: If Where Referenced operation fails for the input object.
        """
        ...

