import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FetchNextChildrenCursor:
    """
    
FetchNextChildrenCursor structure is the
            information about the current result is returned. It is used to track the result
            being returned in pages.
            
    """
    def __init__(self, ) -> None: ...
    Cursor: Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject
    """
Ptn0ExpandCursor object that tracks the expand results. This object is used
            to get the next set of results for this operation.
            """
    IsFinished: bool
    """If true, the whole result is returned; otherwise, part of it is returned."""
    EstimatedElementsLeft: int
    """Number of estimated objects remaining in the result."""

class GetAllChildPtnInAppModelInInfo:
    """
    
GetAllChildPtnInAppModelInInfo structure
            represents the Mdl0ApplicationModel object, configuration context, maximum level
            count, maximum children count and number of Ptn0Partition children to be returned
            in this operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    InputAppModel: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """A Mdl0ApplicationModel object supplied to this operation as an input."""
    MaxLevelCount: int
    """Number that specifies maximum levels to get children. Zero indicates all levels."""
    MaxChildCount: int
    """Number that specifies maximum children count. Zero indicates all children."""
    LoadCount: int
    """
            Specifies the number of objects to be fetched from the result set. If the loadCount is zero (or more than the number of objects left in
            the result set) then returns all the objects in the result set.
            """
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            A ConfigurationContext object, to filter out the configured Ptn0Partition
            objects.
            """

class GetAllChildPtnInAppModelOutInfo:
    """
    
GetAllChildPtnInAppModelOutInfo structure
            contains clientId, a map of Mdl0ApplicationModel object to the list of Ptn0PartitionSchemes,
            a map of Ptn0PartitionScheme object to list of top level Ptn0Partition,
            a map of parent Ptn0Partition object to list of Ptn0Partition objects,
            expanded level count, flag to specify whether the children list is truncated depending
            upon input value of maximum children count, expanded level count and cursor maintaining the index in result.
            
            Input parameter loadCount specifies the number
            of children (Ptn0Partition) objects to include in GetAllChildPtnInAppModelOutInfo
            for this operation. The caller could invoke getAllChildPtnInAppModel
            operation to get the remaining Ptn0Partition objects or use the stopGetChildren operation if no more results of the expand are
            desired (e.g. user-initiated abort).
            
            If the loadCount is zero or more that the
            number of Ptn0Partition objects in result, whole result is returned in this
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the GetAllChildPtnInAppModelInInfo.clientId.
            This is used by the caller to identify this data structure with the source input
            data.
            """
    AppModelSchemesMap: System.Collections.Hashtable
    """
            A map (Mdl0ApplicationModel, list (Ptn0PartitionSchemes))  of input
            Mdl0ApplicationModel object to list of Ptn0PartitionSchemes object.
            """
    SchemesPartitionMap: System.Collections.Hashtable
    """
            A map (Ptn0PartitionScheme, list (Ptn0Partition))  of Ptn0PartitionScheme
            object to list of top level Ptn0Partition object.
            """
    ParentChildPartitionMap: System.Collections.Hashtable
    """
            A map (Ptn0Partition , list (Ptn0Partition)) of parent Ptn0Partition
            object to list of children Ptn0Partition objects.
            """
    ChildPartitionListTruncated: bool
    """
            If true, the child Ptn0Partition object list is truncated. This value depends
            up on the input maximum children count that is supplied as an input parameter.
            """
    ExpandedLevelCount: int
    """
            Number of Partition levels that were traversed while executing this operation. This
            value depends up on the maximum level count that is supplied as input parameter.
            """
    Cursor: FetchNextChildrenCursor
    """
            This is containing the information about the result returned so far.
            
            Flag isFinished is indicating whether the
            result is completely returned.
            """

class GetAllChildPtnInAppModelResponse:
    """
    
            ntains list of GetAllChildPtnInAppModelOutInfo
            objects and serviceData structure. If the
            input parameters are invalid, the errors are returned in the serviceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetAllChildPtnInAppModelOutInfo]
    """
            A list of GetAllChildPtnInAppModelOutInfo
            objects for corresponding list of input GetAllChildPtnInAppModelInInfo
            object.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains the list of all BusinessObject objects that make up the output, as
            well as any errors that might have occurred as part of the service invocation.
            """

class GetNextChildPtnInAppModelInInfo:
    """
    
GetNextChildPtnInAppModelInInfo structure
            contains the clientId, FetchNextChildrenCursor
            and load count. This operation returns the next page of result maintained in cursor.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    Cursor: FetchNextChildrenCursor
    """
            The information about the results returned so far.
            
            The isFinished element is set to true when
            the complete results have been returned.
            """
    LoadCount: int
    """
            The number of objects to be returned from the result set. If the loadCount is zero (or more than the number of objects left in
            the result set) then returns all the objects in the result set.
            """

class GetNextChildPtnInAppModelOutInfo:
    """
    
GetNextChildPtnInAppModelOutInfo structure
            contains clientId, a map of parent Ptn0Partition object to list of Ptn0Partition
            objects, expanded level count, flag to specify whether the children list is truncated
            depending upon input value of maximum children count, expanded level count and cursor maintaining the index in result.
            
            Input parameter loadCount specifies the number
            of children Ptn0Partition objects to include in GetNextChildPtnInAppModelOutInfo
            for this operation. User need to invoke getAllChildPtnInAppModel
            operation to get the remaining Ptn0Partition objects.
            
            If the loadCount is zero or more that the
            number of Ptn0Partition objects in result, whole result is returned in this
            operation only.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the objects."""
    ParentChildPartitionMap: System.Collections.Hashtable
    """
            A map (Ptn0Partition, list (Ptn0Partition)) of parent Ptn0Partition
            object to list of children Ptn0Partition objects.
            """
    ChildPartitionListTruncated: bool
    """
            If true, the child Ptn0Partition object list is truncated. This value depends
            up on the input maximum children count that is supplied as an input parameter.
            """
    ExpandedLevelCount: int
    """
            Number of Partition levels that were traversed while executing this operation. This
            value depends up on the maximum level count that is supplied as input parameter.
            """
    Cursor: FetchNextChildrenCursor
    """
            The information about the results returned so far.
            
            The isFinished element is set to true when
            the complete results have been returned.
            """

class GetNextChildPtnInAppModelResponse:
    """
    
            Contains list of GetNextChildPtnInAppModelOutInfo
            objects and serviceData structure. If the
            input parameters are invalid, the errors are returned in the serviceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetNextChildPtnInAppModelOutInfo]
    """
            A list of GetNextChildPtnInAppModelOutInfo
            objects for corresponding list of input GetNextChildPtnInAppModelInInfo
            object.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains the list of all BusinessObject objects that make up the output, as
            well as any errors that might have occurred as part of the service invocation.
            """

class StopGetChildrenResponse:
    """
    
            Contains flag with true value indicating the successful deletion of the cursor and removal of server memory allocated by the getAllChildPtnInAppModel operation.
            
    """
    def __init__(self, ) -> None: ...
    IsFinished: bool
    """
            If true, a successful deletion of the cursor
            and removal of server memory allocated by the getAllChildPtnInAppModel
            operation.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data for any error information."""

class PartitionManagement:
    """
    Interface PartitionManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAllChildPtnInAppModel(self, Inputs: list[GetAllChildPtnInAppModelInInfo]) -> GetAllChildPtnInAppModelResponse: ...
    def GetNextChildPtnInAppModel(self, Inputs: list[GetNextChildPtnInAppModelInInfo]) -> GetNextChildPtnInAppModelResponse: ...
    def StopGetChildren(self, Cursor: FetchNextChildrenCursor) -> StopGetChildrenResponse: ...

