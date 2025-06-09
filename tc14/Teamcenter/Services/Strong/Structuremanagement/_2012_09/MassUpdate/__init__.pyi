import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class MassUpdateAffectedInput:
    """
    This structure provides a set of input values for the massGetAffectedParents
operation.
    """
    def __init__(self, ) -> None: ...
    Target: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Item Revision to base the where used search on."""
    Change: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The change item revision object to record mass update results in."""
    Operation: int
    """
            Operation type used to help identify type of filtering to use when searching for
            impacted parent parts.
            """

class MassUpdateAffectedOutput:
    """
    This structure provides a set of output values for the massGetAfectedParents
operation.
    """
    def __init__(self, ) -> None: ...
    Parent: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """This is the impacted parent part that references the target part."""
    Selectable: bool
    """This indicates if the impacted parent part is selectable for mass update or not."""
    SelectableComment: str
    """This text informs why the impacted parent part is not selectable."""

class MassUpdateAffectedResponse:
    """
    This structure contains all the results from the massGetAffectedParents
operation.
    """
    def __init__(self, ) -> None: ...
    MassUpdateAffectedOutputs: list[MassUpdateAffectedOutput]
    """This is a vector of MassUpdateAffectedOutput structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data to handle partial errors."""

class MassUpdateExecuteECNoutput:
    """
    This structure provides a set of output values for the massUpdateExecutionECN
operation.
    """
    def __init__(self, ) -> None: ...
    ChangeItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            Change item revision used for mass update execution on the ECN change management
            process.
            """
    Markup: Teamcenter.Soa.Client.Model.Strong.Fnd0Markup
    """Markup on ChangeItemRev that was processed during the ECN CM process."""
    MarkupChanges: list[Teamcenter.Soa.Client.Model.Strong.Fnd0MarkupChange]
    """This is a vector of markup changes that was processed during the ECN CM process."""

class MassUpdateExecuteECNresponse:
    """
    This structure provides output for the massUpdateExecutionECN operation.
    """
    def __init__(self, ) -> None: ...
    Outputs: list[MassUpdateExecuteECNoutput]
    """This is a vector of MassUpdateExecuteECNoutput structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data for partial errors."""

class MassUpdateExecuteECRinput:
    """
    This structure provides a set of input values for the massUpdateExecutionECR
operation.
    """
    def __init__(self, ) -> None: ...
    ExecutionMode: int
    """
            This defines the ECR execution being performed 1=one time execute, 2=save as markup
            and 3=remove markup.
            """
    Operation: int
    """The mass update operation type being executed."""
    Target: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Part that is being replaced or removed."""
    AddToProblem: bool
    """Add the target part to the problem folder."""
    AddToSolution: bool
    """Add the newItem to solution folder."""
    NewItem: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The part that is doing the replacing or being added."""
    Change: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The change item revision object to record mass update results in."""
    MarkupChange: Teamcenter.Soa.Client.Model.Strong.Fnd0MarkupChange
    """
            The markup change to remove from the markup and the change item revision object impacted
            folder.
            """
    Parents: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    """A vector of impacted parent parts that reference the target part."""
    SParents: list[bool]
    """
            A vector of bools that indicate if the impacted parent parts are selectable or not
            for mass update.
            """

class MassUpdateExecuteECRoutput:
    """
    This structure provides a set of output values for the massUpdateExecutionECR
operation.
    """
    def __init__(self, ) -> None: ...
    Parent: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The impacted parent part that references the target part."""
    Status: int
    """
            This indicates if the impacted parent part was successful or not during the massUpdateExecutionECR
            operation.
            """
    StatusComment: str
    """
            Detailed status text on why the impacted parent part succeded or failed to process
            correctly.
            """

class MassUpdateExecuteECRresponse:
    """
    This structure provides output for the massUpdateExecutionECR operation.
    """
    def __init__(self, ) -> None: ...
    Outputs: list[MassUpdateExecuteECRoutput]
    """This is a vector of MassUpdateExecuteECRoutput structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data for partial errors."""

class MassUpdate:
    """
    Interface MassUpdate
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def MassGetAffectedParents(self, Input: list[MassUpdateAffectedInput]) -> MassUpdateAffectedResponse:
        """    
             This operation will call ITK PS__masschange_get_parents to get all the affected impacted
             parent parts and there selectablility for mass update.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         The input is a vector of MassUpdateAffectedInput structures.
             
        :return: The results of the ITK PS__masschange_get_parents are returned by this SOA operation.
        """
        ...
    def MassUpdateExecutionECR(self, Input: list[MassUpdateExecuteECRinput]) -> MassUpdateExecuteECRresponse:
        """    
             This operation will call one of three ITKs: execute mode=1 calls PS__PS__masschange_onetime,
             execute mode=2 calls PS__masschange_authorize_add and execute mode=3 calls PS__masschange_authorize_remove.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         This is a vector of MassUpdateExecuteECRinput structures.
             
        :return: The results from the three ITKs PS__PS__masschange_onetime, PS__masschange_authorize_add
             and PS__masschange_authorize_remove is return.
        """
        ...
    def MassUpdateExecutionECN(self, ChangeItemRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> MassUpdateExecuteECNresponse:
        """    
             This operation will call ITK PS__masschange_execute which will process all the change
             item revision markup changes recorded during the ECR CM process.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param ChangeItemRevs: 
                         A vector of mass update change item revisions to be executed during the ECN CM process.
             
        :return: The results of the ITK PS__masschange_execute will be return.
        """
        ...

