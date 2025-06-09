import System
import System.Collections
import Teamcenter.Services.Strong.Cad._2007_01.StructureManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateWindowsInfo3:
    """
    
            Main input structure that defines Item or ItemRevision of the top line
            in the BOMWindow. In the input, the BOMWindow is mutually exclusive
            with Item, ItemRevision and PSBOMView. If BOMWindow and
            Item, ItemRevision and PSBOMView objects are sent it will be
            considered as re-configure with BOMWindow. In the input, either revRuleConfigInfo
            object and objectsForConfigure object (variant rules or saved option set) or configContext
            object is required, the effGrpRevList object is used to re-configure BOMWindow
            if configContext object is not provided.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the objects created."""
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """BOMWindow object to be reconfigured. Must be NULLTAG when creating a new window."""
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """
Item for top line of new window, or NULLTAG if itemRev is specified. Must
            be NULLTAG when reconfiguring an existing window.
            """
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
ItemRevision for top line of new window, or NULLTAG if item is specified in
            which case the default revision will be used. Must be NULLTAG when reconfiguring
            an existing window.
            """
    BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView
    """
PSBOMView to be used when creating a new window, or NULLTAG to use the default
            view. Must be NULLTAG when reconfiguring an existing window.
            """
    RevRuleConfigInfo: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.RevisionRuleConfigInfo
    """Structure with information about RevisionRuleConfigInfo."""
    ObjectsForConfigure: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of VariantRule or StoredOptionSet stored option set object to
            set on this window.
            """
    ActiveAssemblyArrangement: Teamcenter.Soa.Client.Model.Strong.AssemblyArrangement
    """Active AssemblyArrangement of the BOMWindow."""
    ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """ConfigurationContext object reference."""
    EffGrpRevList: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    """
            A list of Fnd0EffectivityGrp  objects, effGrpRevList is used along with BOMwindow
            and to configure or re-configure them.
            """
    BomWinPropFlagMap: System.Collections.Hashtable

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrReConfigureBOMWindows(self, Info: list[CreateWindowsInfo3]) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateBOMWindowsResponse: ...

