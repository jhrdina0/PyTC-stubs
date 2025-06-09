import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateChangeLineageInputData:
    """
    Input data for creation of lineage.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    SolutionItems: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """
            List of WorkspaceObject which are referred as Solution Items for the ChangeNoticeRevision.
            All the solution items must belong to same ChangeNoticeRevision.
            """
    ImpactedItems: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """
            List of WorkspaceObject which are referred as Impacted Items for the ChangeNoticeRevision.
            All the impacted items must belong to same ChangeNoticeRevision.
            """

class CreateChangeLineageOutput:
    """
    Change Lineage output.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the CreateChangeLineageInputData.clientId. This can be
            used by the caller to identify this data structure with the source input data.
            """
    Relations: list[Teamcenter.Soa.Client.Model.Strong.ImanRelation]
    """A list of created relations."""

class CreateChangeLineageResponse:
    """
    Change Lineage creation response.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data."""
    Output: list[CreateChangeLineageOutput]
    """Change Lineage output."""

class DeleteChangeLineageInputData:
    """
    
            DeleteChangeLineageInputData structure contains clientId to uniquely identify the
            input, an object reference that can be used to point to the ChangeNoticeRevision
            and list to hold any number of business objects for which change lineage has to be
            deleted.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Input string to uniquely identify the input."""
    ChangeNoticeRev: Teamcenter.Soa.Client.Model.Strong.ChangeItemRevision
    """The ChangeNoticeRevision associated with the lineage to be deleted."""
    Objects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """A list of objects for which the related lineage will be deleted."""

class ChangeManagement:
    """
    Interface ChangeManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateChangeLineage(self, Input: list[CreateChangeLineageInputData]) -> CreateChangeLineageResponse:
        """    
             This operation creates CMSolutionToImpacted relation between all the Solution
             Items and all the Impacted Items for a ChangeNoticeRevision and then assign
             a group ID to them. To determine the group ID, the CMSolutionToImpacted relations
             are traversed for ChangeNoticeRevision and then find the largest group ID
             number present for this ChangeNoticeRevision in context. The new group ID
             is the next incremented number. This group number is assigned to all the CMSolutionToImpacted
             relations created for the input data.
             
             Each CreateChangeLineageInputData input will have new group id assigned for the relations
             created for that group.
             

             Note: Solution Items and Impacted Items are the objects which are attached to ChangeNoticeRevision
             using CMHasSolutionItem and CMHasImpactedItem relation respectively.
             

Use Cases:

             User selects Solution Items and Impacted Items for a ChangeNoticeRevision
             and create lineage between them.
             

Teamcenter Component:

             Change Management - This feature provides support for proposing changes to a product
             and managing the entire lifecycle of the changes. With this feature ItemRevision
             objects may be related to ChangeItemRevision objects as Problem, Impacted, or Solution
             items.
             
        :param Input: 
                         Input data for creating lineage. A unique group id will be assigned for each input
                         data.
             
        :return: .
        """
        ...
    def DeleteChangeLineage(self, Inputs: list[DeleteChangeLineageInputData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes the change lineage by deleting the relations between a group
             of solution items and their respective impacted items that are associated with the
             lineage group. Each DeleteChangeLineageInputData structure passed as input will have
             the clientId to uniquely identify each input, the ChangeNoticeRevision and
             the list of objects for which the lineage has to be deleted. Lineage group is determined
             for each object and all the relations belonging to the same lineage group will be
             deleted.
             

Use Cases:

             For a ChangeNoticeRevision, change lineage creation is the ability to relate a group
             of solution items with their respective impacted items and designate an associated
             lineage group. This operation allows deleting change lineage.
             

Teamcenter Component:

             Change Management - This feature provides support for proposing changes to a product
             and managing the entire lifecycle of the changes. With this feature ItemRevision
             objects may be related to ChangeItemRevision objects as Problem, Impacted, or Solution
             items.
             
        :param Inputs: 
                         A list of DeleteChangeLineageInputData structures each of which contains clientId
                         to uniquely identify each input, an object reference to the <b>ChangeNoticeRevision</b>
                         and a list to hold business objects for which change lineage has to be deleted.
             
        :return: 
        """
        ...

