import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CopyEBOPStructureResponse:
    """
    response structure for the service method copyEBOPStructure.
    """
    def __init__(self, ) -> None: ...
    CreatedICRevs: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """any newly created incremental change revisions"""
    CreatedFutureICRevs: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """any newly created future Incremental Change Revisions."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """the updated item(root) and any partial errors returned here."""
    UpdatedObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The updatedObject which is the itemrevision of the passed in item."""

class GetStructureContextLinesResponse:
    """
    Get toplines from the BomWindow setup by StructureContext and any selected bomlines.
    """
    def __init__(self, ) -> None: ...
    TopLines: System.Collections.Hashtable
    """
            Map of StructureContext to its toplines. For example, Product Structure and Process
            Structure top lines.
            """
    SelectedLines: System.Collections.Hashtable
    """
            Map of StructureContext to any selected child lines. Note: If the topline is selected
            this map will be empty.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Structure to capture any partial errors."""

class PasteDuplicateStructureResponse:
    """
    response structure of operation that clones the src objects before pasting.
    """
    def __init__(self, ) -> None: ...
    CreatedICRevs: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """any newly created Incremental Change Revisions."""
    CreatedFutureICRevs: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """any newly created future IC revs"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """service data returns the populated targetLines along with any partial errors."""
    NewChildLines: System.Collections.Hashtable
    """the map of targetline and the newly created lines under it."""

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def PasteDuplicateStructure(self, SrcLines: list[Teamcenter.Soa.Client.Model.ModelObject], TargetLines: list[Teamcenter.Soa.Client.Model.ModelObject], CopyRulesKey: str, CopyFutureEffectivity: bool) -> PasteDuplicateStructureResponse:
        """    
             clone the selected lines to each of the targetline supplied. The 2 input vectors
             are not related. Currently, this functionality is only for EBOP structures.
             
        :param SrcLines: 
                         input src lines which need to be cloned under the targetline(s). All of them must
                         be from the same structure.
             
        :param TargetLines: 
                         the targetline(s) under which the clones of the object underlying the srclines will
                         be created/pasted. These should be from the same structure.
             
        :param CopyRulesKey: 
                         name of the preference that will be used for cloning.
             
        :param CopyFutureEffectivity: 
                         flag to indicate whether future effectivities are to be created.
             
        :return: The return structure has any newly created IC revs along with the populated targetlines.
        """
        ...
    def CopyEBOPStructure(self, NewRoot: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject, ConfiguringEBOPWindow: Teamcenter.Soa.Client.Model.ModelObject, WorkingWindow: Teamcenter.Soa.Client.Model.ModelObject, CopyRulesKey: str, CopyFutureEffectivity: bool) -> CopyEBOPStructureResponse:
        """    
             Creates a clone of the supplied root of the configuringEBOPWindow under the rootObject
             specified.
             
        :param NewRoot: 
                         The newly created rootobject under which the structure will be cloned.
             
        :param ConfiguringEBOPWindow: 
                         The window with source BOP(GBOP/PBOP) item as root.
             
        :param WorkingWindow: 
                         optional window (the actual source window), from which the IncrementalChange Rev
                         is picked up. In addition the window settings like show unconfigured etc. are also
                         picked up.
             
        :param CopyRulesKey: 
                         The name of the preference which will be used for cloning rule to be used.
             
        :param CopyFutureEffectivity: 
                         if true, future ICRevs will be created appropriately, instead of all ICEs being cloned
                         to the currently active ICRev. Note that if this is true - it is expected that there
                         is an currently selected ICRev in the working window.
             
        :return: returns the input rootobject whose structure will be updated along with any created
             IC revs.
        """
        ...
    def GetStructureContextLines(self, ScList: list[Teamcenter.Soa.Client.Model.Strong.StructureContext]) -> GetStructureContextLinesResponse:
        """    Return the top lines and any selected lines if present.
        :param ScList: 
                         The list of StructureContexts for which toplines and selected lines are needed.
             
        :return: Return a map of Structure Context to Top Line and a map of Structure Context to selected
             child lines.
        """
        ...

