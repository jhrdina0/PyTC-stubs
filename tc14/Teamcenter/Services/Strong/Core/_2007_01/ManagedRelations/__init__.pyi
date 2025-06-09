import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ComplyingReport:
    """
    Complying Report
    """
    def __init__(self, ) -> None: ...
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """Tag of the Parent"""
    Children: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of Children"""

class CreateManagedRelationInput:
    """
    This structure has all the information needed to create TraceLink managed relation.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """name"""
    Type: str
    """Type will decide what relation to be created"""
    PrimaryTagList: list[Teamcenter.Soa.Client.Model.ModelObject]
    """primaryTagList"""
    SecondaryTagList: list[Teamcenter.Soa.Client.Model.ModelObject]
    """secondaryTagList"""

class DefiningReport:
    """
    Defining Report
    """
    def __init__(self, ) -> None: ...
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """Tag of the Parent"""
    Children: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of Children"""

class ManagedRelationResponse:
    """
    Managed Relation Response
    """
    def __init__(self, ) -> None: ...
    ManagedRelationObjects: list[Teamcenter.Soa.Client.Model.Strong.TraceLink]
    """List of Managed Relation Objects"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The successful Object ids, partial errors and failures"""

class ModifySources:
    """
    Modify Sources
    """
    def __init__(self, ) -> None: ...
    AddSources: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of Sources to Add"""
    RemoveSources: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of Sources to Remove"""

class ModifyTargets:
    """
    Modify Targets
    """
    def __init__(self, ) -> None: ...
    AddTargets: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of Targets to Add"""
    RemoveTargets: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of Targets to Remove"""

class ModifyManagedRelationInput:
    """
    Modify Managed Relation Input
    """
    def __init__(self, ) -> None: ...
    RelationTag: Teamcenter.Soa.Client.Model.ModelObject
    """Tag of the Relation"""
    SetSourcesInput: ModifySources
    """Modify Sources Input"""
    SetTargetsInput: ModifyTargets
    """Modify Targets Input"""

class TraceabilityInfoInput:
    """
    Traceability Information Input
    """
    def __init__(self, ) -> None: ...
    InputTag: Teamcenter.Soa.Client.Model.ModelObject
    """Tag of the input"""
    ReportType: str
    """Report Type"""
    ReportDepth: int
    """Report Depth"""

class TraceabilityReportOutput:
    """
    Traceability Report Output
    """
    def __init__(self, ) -> None: ...
    DefiningTree: list[DefiningReport]
    """List of Defining Reports"""
    IndirectDefiningTree: list[DefiningReport]
    """List of Defining Reports (Indirect)"""
    ComplyingTree: list[ComplyingReport]
    """List of Complying Reports"""
    IndirectComplyingTree: list[ComplyingReport]
    """List of Complying Reports (Indirect)"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The successful Object ids, partial errors and failures"""

class ManagedRelations:
    """
    Interface ManagedRelations
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateRelation(self, Relationinfo: list[CreateManagedRelationInput]) -> ManagedRelationResponse:
        """    
             This operation will create new managed relation.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Relationinfo: 
                         input information required to create managed relation
             
        :return: has any created relation and the service data.Failure will be returned with input
             index and error message in the ServiceData.
        """
        ...
    def GetTraceReport(self, Input: TraceabilityInfoInput) -> TraceabilityReportOutput:
        """    
             This operation will create traceability report for the selected TC object.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Input: 
                         information required to create report
             
        :return: has traceability tree for the given TC object and the service data. Failure will
             be returned with input index and error message in the ServiceData.
        """
        ...
    def ModifyRelation(self, NewInput: list[ModifyManagedRelationInput]) -> ManagedRelationResponse:
        """    
             This operation will Edit the managed relation.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param NewInput: 
                         will have the modification info for given relation
             
        :return: will loadthe modified relation along with service data. Failure will be returned
             with input index and error message in the ServiceData.
        """
        ...

