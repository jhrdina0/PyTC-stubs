import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetMembersInBOMWindowBulkInputInfo:
    """
    
            GetMembersInBOMWindowBulkInputInfo structure represents the details of BOMWindow
            object, PartitionInfo structure and content PersistenceMode.
            
    """
    def __init__(self, ) -> None: ...
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """BOMWindow object."""
    PartitionInfo: list[PartitionInfo]
    """A list of structure containing clientID and Ptn0Partition objects."""
    ContentPersistenceMode: str
    """
            The content persistence mode. This parameter can be any one of the four following
            values:
            
            BOM_MODE_STATIC Used when user want to get only static members.
            
            BOM_MODE_DYNAMIC Used when user want to get only dynamic members.
            
            BOM_MODE_ALL Used when user want to get both static and dynamic members.
            
            BOM_MODE_AUTO Used when members are returned depending on the default persistence
            mode of the Partition.
            
            For now, only BOM_MODE_STATIC value is supported.
            """

class GetMembersInBOMWindowOutputInfo:
    """
    
            GetMembersInBOMWindowOutputInfo structure contains clientId and a list of member
            BOMLine objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client track the objects."""
    MemberList: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """A list of member BOMLine objects for the input Ptn0Partition object."""

class GetMembersInBOMWindowResponse:
    """
    
            Contains list of GetMembersInBOMWindowOutputInfo object and serviceData structures.
            Input Ptn0Partition object information along with their members are returned
            via GetMembersInBOMWidowOutputInfo object. If the input parameters are invalid, the
            errors are returned in the serviceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetMembersInBOMWindowOutputInfo]
    """
            A list of GetMembersInBOMWindowOutputInfo objects for corresponding list of input
            GetMembersInBOMWindowInputInfo object.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains the list of all BusinessObject objects that make up the output, as
            well as any errors that might have occurred as part of the service invocation.
            """

class GetPartitionsForBOMLineIpInfo:
    """
    
            GetPartitionsForBOMLineIpInfo structure represents the details of BOMWindow
            object, Ptn0PartitionScheme object and OccThreadPathInfo structure.
            
    """
    def __init__(self, ) -> None: ...
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """BOMWindow object."""
    PartitionScheme: Teamcenter.Soa.Client.Model.Strong.Ptn0PartitionScheme
    """
Ptn0PartitionScheme as another search criteria for the service, user can give
            NULL value for this parameter,  the search scope will be BOMWindow itself.
            """
    OccThreadPathInfo: list[OccThreadPathInfo]
    """A list of CSID path for BOMLine objects whose Partitions needs to be returned."""

class GetPartitionsForBOMLineMemInfo:
    """
    
            GetPartitionsForBOMLineMemInfo structure contains a Ptn0Partition object that
            contains an object provided as input to this operation.
            
    """
    def __init__(self, ) -> None: ...
    Partition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """A Ptn0Partition containing an input object."""
    IsPseudoMember: bool
    """If true, the input object is a pseudo-member of the Ptn0Partition."""

class GetPartitionsForBOMLineOpInfo:
    """
    
            GetPartitionsForBOMLineOpInfo structure contains clientId and list of GetPartitionsForBOMLineMemInfo
            structure.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client track the objects."""
    MemberInfo: list[GetPartitionsForBOMLineMemInfo]
    """A list of Ptn0Partition objects containing the input objects."""

class GetPartitionsForBOMLineResponse:
    """
    
            The response for the operation getPartitionsForBOMLine. Contains the objects provided
            as input to the operation and the Ptn0Partition objects containing the input
            objects.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetPartitionsForBOMLineOpInfo]
    """
            A list of input objects and the Ptn0Partition objects containing the input
            objects.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains the list of all BusinessObject objects that make up the output, as
            well as any errors that might have occurred as part of the service invocation.
            """

class GetSchemesInBOMViewOutputInfo:
    """
    
            GetSchemesInBOMViewOutputInfo structure contains the list of partition schemes which
            are output of operation and input PSBOMView object to which the schemes belong
            If there are no schemes attached to PSBOMView then it returns empty Ptn0PartitionScheme
            list.
            
    """
    def __init__(self, ) -> None: ...
    BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView
    """PSBOMView object which was input to the operation."""
    PartitionSchemes: list[Teamcenter.Soa.Client.Model.Strong.Ptn0PartitionScheme]
    """A list of Ptn0PartitionScheme objects that are defined under the view."""

class GetSchemesInBOMViewResponse:
    """
    
            Output contains list of Partition Scheme and input PSBOMView objects. Service
            data is populated with the list of all BusinessObject objects that make up
            the output, as well as any errors that might have occurred as part of the service
            invocation.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetSchemesInBOMViewOutputInfo]
    """
            A list of PSBOMView objects and the Ptn0PartitionScheme objects under
            the view.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains the list of all BusinessObject objects that make up the output, as
            well as any errors that might have occurred as part of the service invocation.
            """

class GetTopLevelPtnsInBOMViewInputInfo:
    """
    
            GetTopLevelPtnsInBOMViewInputInfo structure represents the details of BOMView, Partition
            scheme and Configuration context, for which top level Partitions are to be returned.
            
    """
    def __init__(self, ) -> None: ...
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
ConfigurationContext object which configures the output top level Partitions
            with the effectivity condition or revision rule attached to it.
            """
    BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView
    """PSBOMView object for which the top-level Partitions are to be returned."""
    PartitionScheme: Teamcenter.Soa.Client.Model.Strong.Ptn0PartitionScheme
    """Ptn0PartitionScheme object for which the top-level Partitions are to be returned."""

class GetTopLevelPtnsInBOMViewOutputInfo:
    """
    
            GetTopLevelPtnsOutputInfo structure represents the list of top-level Partitions returned
            corresponding to an input Partition Scheme supplied.
            
    """
    def __init__(self, ) -> None: ...
    ParitionScheme: Teamcenter.Soa.Client.Model.Strong.Ptn0PartitionScheme
    """
            Input Ptn0PartitionScheme to which this structures output partitions belong
            to.
            """
    TopLevelPartitions: list[Teamcenter.Soa.Client.Model.Strong.Ptn0Partition]
    """
            Top level Ptn0Partition objects that get configured as per the provided Configuration
            Context, Partition Scheme and BOMView.
            """

class GetTopLevelPtnsInBOMViewResponse:
    """
    
            GetTopLevelPtnsInBOMViewResponse structure represents the list of GetTopLevelPtnsInBOMViewOutputInfo
            consisting of the top-level Partitions, their corresponding scheme structure and
            also the errors via serviceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetTopLevelPtnsInBOMViewOutputInfo]
    """
            A list of GetTopLevelPtnsInBOMViewOutputInfo structures for corresponding list of
            input GetTopLevelPtnsInBOMViewInputInfo structures.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains the list of all BusinessObject objects that make up the output, as
            well as any errors that might have occurred as part of the service invocation.
            """

class OccThreadPathInfo:
    """
    OccThreadPathInfo structure represents the details of clientId, OccThreadPath.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client track the objects."""
    OccThreadPath: str
    """CSID path for BOMLine objects whose Partitions needs to be returned."""

class PartitionInfo:
    """
    PartitionInfo structure contains the details of clientID, Ptn0Partition object.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client track the Ptn0artition objects."""
    Partition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """Ptn0Partition object for which the members are to be returned."""

class PartitionManagement:
    """
    Interface PartitionManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetMembersInBOMWindow(self, Inputs: list[GetMembersInBOMWindowBulkInputInfo]) -> GetMembersInBOMWindowResponse: ...
    def GetPartitionsForBOMLine(self, Inputs: list[GetPartitionsForBOMLineIpInfo]) -> GetPartitionsForBOMLineResponse: ...
    def GetSchemesInBOMView(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.PSBOMView]) -> GetSchemesInBOMViewResponse: ...
    def GetTopLevelPartitionsInBOMView(self, Inputs: list[GetTopLevelPtnsInBOMViewInputInfo]) -> GetTopLevelPtnsInBOMViewResponse: ...

