import System
import Teamcenter.Soa.Client.Model
import typing

class CandidateTool:
    """
    
            Specifies the candidate tools for the Operation or Process where Tool Requirement
            is assigned.
            
    """
    def __init__(self, ) -> None: ...
    ParentObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Specifies the Operation of type Mfg0BvrOperation or Process of type Mfg0BvrProcess
            where Tool Requirement is assigned.
            """
    Tools: list[Tool]
    """Specifies the candidate tools matching the search criteria of the Tool Requirement."""

class CandidateToolsForToolRequirement:
    """
    Specifies the candidate tools for the Tool Requirement
    """
    def __init__(self, ) -> None: ...
    CandidateTools: list[CandidateTool]
    """Structure with member as Operation or Process and the candidate tools."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data will hold warnings and errors. if any."""

class ResolveDataInfo:
    """
    
            Input structure specifying the Operation or Process. the Tool Requirement that is
            to be resolved. the Tool with which Tool requirement resolve against and the tool
            source from where tool is to be picked.
            
    """
    def __init__(self, ) -> None: ...
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """
            Specifies the Operation of type Mfg0BvrOperation or Process of type Mfg0BvrProcess
            under which Tool requirement is assigned.
            """
    TrObject: Teamcenter.Soa.Client.Model.ModelObject
    """Specifies the Tool Requirement of type Mfg0BVRToolRequirement that is to be resolved."""
    ToolObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Tool of type Mfg0BvrResource that matches the search criteria of the Tool Requirement
            and against which it is going to be resolved.
            """
    ToolSource: str
    """
            Specifies the source from where the tool is to be fetched. The possible values are
            LIBRARY & WORKAREA and ALL which specify that the tool is to be fetched respectively
            from only library only workarea or workarea and library. Note that in the case of
            ALL the preference is given to the workarea over the library.
            """

class Tool:
    """
    
            Specifies the candidate tools with members as the Tool Requirement and the tools
            that match the search criteria of Tool Requirement.
            
    """
    def __init__(self, ) -> None: ...
    TrObject: Teamcenter.Soa.Client.Model.ModelObject
    """Specifies the Tool Requirement of type Mfg0BVRToolRequirement."""
    ToolObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            Specifies the candidate tools of type Mfg0BvrResource matching the search criteria
            of the Tool Requirement.
            """

class ToolRequirementInput:
    """
    
            Input structure specifying the Operation or Process. the Tool Requirement for which
            candidate tools are to be fetched and the tool source from where tools are to be
            fetched.
            
    """
    def __init__(self, ) -> None: ...
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """
            Specifies the Operation of type Mfg0BvrOperation or Process of type Mfg0BvrProcess
            under which Tool requirement is assigned.
            """
    TrObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Specifies the Tool Requirement of type Mfg0BVRToolRequirement for which candidate
            tools are to be fetched.
            """
    ToolSource: str
    """
            Specifies the source from where the tools are to be fetched.  The possible values
            are Library & WorkArea and All. Which specify that the tools are to be fetched
            respectively from library and workarea. Only library and only workarea.
            """

class ToolRequirementResponse:
    """
    Specifies the Tool Requirements that are assigned to an Operation or Process.
    """
    def __init__(self, ) -> None: ...
    ToolRequirements: list[ToolRequirementResult]
    """Specifies the Tool Requirements."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data will hold warnings and errors. if any."""

class ToolRequirementResult:
    """
    Specifies the Tool Requirements that are assigned to an Operation or Process.
    """
    def __init__(self, ) -> None: ...
    ParentObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Specifies the Operation of type Mfg0BvrOperation or Process of type Mfg0BvrProcess
            to which Tool requirement is assigned.
            """
    ToolRequirements: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            Specifies the Tool Requirement of type Mfg0BVRToolRequirement that are assigned to
            the Operation or Process.
            """

class Model:
    """
    Interface Model
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetCandidateToolsForToolRequirement(self, ResolveObjects: list[ToolRequirementInput]) -> CandidateToolsForToolRequirement:
        """    
             Gets the candidate tools against which Tool Requirement could be resolved. The candidate
             tools are fetched based on the search criteria specified on the Tool Requirement.
             The input parameter tool source specifies the source from where candidate tools are
             supposed to be fetched.  The candidate tool can be fetched only in the Plant BOP.
             
        :param ResolveObjects: 
                         Input structure specifying Operation. Tool Requirement for which candidate tools
                         are to be fetched. And tool source from where tools are to be fetched.
             
        :return: Specifies the candidate tools that match the search criteria of the Tool requirement.
             Further resolveToolRequirement  could be used to resolve the TR with one of the candidate
             tools.
        """
        ...
    def GetToolRequirements(self, ParentObject: list[Teamcenter.Soa.Client.Model.ModelObject], ToolRequirementStatus: list[str]) -> ToolRequirementResponse:
        """    
             Fetches the Tool Requirement for the given operation or process. Based on the status
             of the Tool Requirement. either all. resolved or unresolved Tool Requirements are
             returned. The respective options for the status are ALL. RESOLVED and UNRESOLVED.
             Note that the Tool requirement assigned to child operation or process is not considered.
             
        :param ParentObject: 
                         Specifies the Operation of type Mfg0BvrOperation or Process of type Mfg0BvrProcess.
             
        :param ToolRequirementStatus: 
                         Specifies the status of the Tool requirement. The possible values are ALL &amp; RESOLVED
                         and UNRESOLVED. RESOLVED indicates that the Tool Requirement is resolved against
                         the Tool. This option is relevant only for the Plant BOP where it is allowed to resolve
                         the Tool Requirement.  UNRESOLVED indicates that the Tool Requirement is not resolved
                         ALL includes both resolved and unresolved Tool Requirement.
             
        :return: Specifies the Tool Requirements of type Mfg0BVRToolRequirement that are assigned
             to an Operation or Process
        """
        ...
    def ResolveToolRequirement(self, ResolveObjects: list[ResolveDataInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Resolves the Tool Requirement with the provided tool. As a result the Tool is assigned
             to the Tool Requirement and to the Operation for which Tool Requirement is defined.
             This resolve operation  is allowed only in the Plant BOP.
             
        :param ResolveObjects: 
                         Specifies the data required for resolving the Tool requirement.
             
        :return: Service data will hold partial errors & warnings and errors. if any.
        """
        ...
    def UpdateFlows(self, Input: list[Teamcenter.Soa.Client.Model.ModelObject], IsSubHierarchies: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Updates flows between the children of input object(s) based on Find number value.
             Input objects should be an instance of BOM line. This service does not return any
             resulting or affected objects. The client needs to update cache of affected objects
             manually(children of the input object are affected ). If isSubHierarchies parameter
             is true, flows are recursively updated for all children.
             
        :param Input: 
                         Should be a vector of BOM lines. This is a scope of update flow command.
             
        :param IsSubHierarchies: 
                         If isSubHierarchies parameter is true, flows are recursively updated for all children.
             
        :return: Returns error message(s) if any generated during update flow execution. Please note
             service data will not return any resulting objects.
        """
        ...

