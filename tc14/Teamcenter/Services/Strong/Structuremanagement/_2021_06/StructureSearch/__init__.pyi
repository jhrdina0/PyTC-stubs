import System
import System.Collections
import Teamcenter.Services.Strong.Structuremanagement._2014_12.StructureSearch
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DataSetExpression:
    """
    Dataset criteria for the expansion
    """
    def __init__(self, ) -> None: ...
    RelationName: str
    RelatedObjAndNamedRefs: list[RelatedObjectTypeAndNamedRefs]
    """List of related object types and named references."""
    NamedRefHandler: int
    """
            Used to identify how named references will be processed.
            
            Valid values are:
            
            0: UseNamedRefsList -- Only the named references listed in the input RelatedObjectTypeAndNamedRefs
            struct are processed.
            
            1: NoNamedRefs -- No named references are to be processed. The input RelatedObjectTypeAndNamedRefs
            will be ignored.
            
            2: AllNamedRefs -- All named references are to be processed. The input RelatedObjectTypeAndNamedRefs
            will be ignored.
            
            3. PreferredJT -- Specialized code for selecting which named references to process
            is executed. This is intended for selecting the most appropriate JT files for visualization
            purposes. If related object is a DirectModel, RelatedObjectTypeAndNamedReferences
            contents will be ignored and only the preferred JT is returned. If related object
            is not Direct Model, named reference expansion will proceed as though namedRefHandler
            is UseNamedRefsList.
            """

class ExpandBOMLinesNamedReferenceInfo:
    """
    
This structure is used to identify the reference object corresponding to the
named
reference.
    """
    def __init__(self, ) -> None: ...
    NamedReferenceType: str
    """Type of reference object."""
    NamedReferenceName: str
    """Name of reference object."""
    ReferenceObject: Teamcenter.Soa.Client.Model.ModelObject
    """Object reference corresponding to the named reference."""
    FileTicket: str
    """FMS ticket used to retrieve the file in cases where referenceObject is a file."""

class ExpandBOMLinesObjects:
    """
    
Through this structure, the bom line, the objects attached to the bom line
object
are returned.
    """
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.ModelObject
    """BOMLine object reference where related objects are related."""
    RelatedObjects: list[ExpandBOMLinesRelatedObjectInfo]
    """List of object references attached to line with given relation."""

class ExpandBOMLinesRelatedObjectInfo:
    """
    
This structure is used to identify the reference object corresponding to the
named
reference.
    """
    def __init__(self, ) -> None: ...
    RelatedObject: Teamcenter.Soa.Client.Model.ModelObject
    """The resulting related object by following a relation specified in the DataSetExpression."""
    NamedRefList: list[ExpandBOMLinesNamedReferenceInfo]
    """List of named reference and reference object of relatedObject."""

class ExpandOptions:
    """
    Expansion Options for a given expansion
    """
    def __init__(self, ) -> None: ...
    DataSetInfoToLoad: list[DataSetExpression]
    """A list of Information to load related DataSet objects."""
    AdditionalInfo: Teamcenter.Services.Strong.Structuremanagement._2014_12.StructureSearch.AdditionalInfo
    """Currently not used, possible future usage."""

class ExpandResponse:
    """
    
Response SOA Structure for expansion results. It contains found objects and the
expansion
cursor that can be used in next expansion.
    """
    def __init__(self, ) -> None: ...
    ObjectsDone: int
    """Number of objects returned so far."""
    EstimatedObjectsLeft: int
    """Estimated number of objects left for one level expansion."""
    FoundObjects: list[Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject]
    """
            The next list of objects returned by the startExpandBOMLines or nextExpandBOMLines
            operation.
            """
    ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject
    """
SearchCursor object that tracks the expand results. This object is used to
            get the next set of results for this startExpandBOMLines operation.
            """
    ExtraObjects: list[ExtraObjects]
    """A list of Dataset objects for the lines returned."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data for any error information."""

class ExtraObjects:
    """
    It contains the datasets to be returned.
    """
    def __init__(self, ) -> None: ...
    ParentInfo: ExpandBOMLinesObjects
    """The parent information."""
    ChildrenInfo: list[ExpandBOMLinesObjects]
    """A list of infomation of the children that contain DataSet objects."""

class RelatedObjectTypeAndNamedRefs:
    """
    
This structure contains a related object type and the list of its named
references
to be processed.
    """
    def __init__(self, ) -> None: ...
    ObjectTypeName: str
    NamedReferenceNames: list[str]

class StructureSearch:
    """
    Interface StructureSearch
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def NextExpandBOMLines(self, PageSize: int, ExpandOptions: ExpandOptions, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> ExpandResponse:
        """    
             This operation gets the next set of objects from a previously executed expansion
             result. The results returned are based on the pageSize specified in the input. This
             API returns the same response structure as that of startExpandBOMLines.
             

Use Cases:

             This API is used in conjunction with startExpandBOMLines operation. startExpandBOMLines
             operation is a prerequisite for invoking nextExpandBOMLines. The expand cursor returned
             by the startExpandBOMLines is used to call nextExpandBOMLines operation. This operation
             could be called repeatedly by the caller, until all the expansion results are returned.
             

Dependencies:

             startExpandBOMLines
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param PageSize: 
                         The number of objects to be returned by the call. The real number of returned may
                         vary, but it is smaller than pageSize. The value will override loadCount in ExpandCursor.
             
        :param ExpandOptions: 
                         Expand options for the operation.
             
        :param ExpandCursor: 
                         The SearchCursor object that keeps track of the expansion results and the corresponding
                         indexes as of where the caller has consumed the results.
             
        :return: 214556Â Â Â Â Â Â Â Â Invalid relation to get associated
             objects.
        """
        ...
    def StartExpandBOMLines(self, BomLines: list[Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject], ExpandSettings: System.Collections.Hashtable, PageSize: int, ExpandOptions: ExpandOptions) -> ExpandResponse:
        """    
             This operation initiates a sequence of operations to expand BOMLine objects based
             on  filter information on BOMWindow and returns a list of BOMLine objects.
             Filter information could be a complex expression set that combines multiple simpler
             Expand terms in a logical sequence.
             
             Expansion is always executed within the scope of a BOMWindow under one or
             more BOMLine objects.
             
             The results of an expansion are returned one set at a time based on the pageSize.
             The ExpandResponse also contains a Cursor object that the caller uses to expand
             the next set of results by invoking the StructureManagement::StructureSearch::nextExpandBOMLines
             call.
             

Use Cases:

             1.    Expand all lines of a structure page by page by setting
             levels to 0 (expand all levels) and pageSize is 100. The operation will return the
             result breadth first.
             
             2.    Expand all lines of a structure by setting levels to 0
             (expand all levels) and pageSize is 0.
             
             3.    Expand all child lines of a list of lines by setting level
             to 1 and pageSize is 100.
             
             4.    Expand all child lines from the structure based on the
             given pageSize.
             
             The returned childlines may or may not contain specific datasets. For example, if
             dataset information is specified - dataset relation is IMAN_reference and
             dataset type is Text then the response will contain the specified datasets (if there
             are any).
             
             5.    Expand the child lines from the structure given the page
             size. The dataset information contains the minimum number of dataset objects to be
             returned. For example, dataset relation is given as IMAN_reference, dataset
             type is Text, expandRelatedObjects is 1 and min datasets to be returned is set to
             10. In this case, the response will contain only 10 specified datasets.
             
             6.     Expand the child lines from the structure given the page
             size. When dataset information specify the dataset relation and dataset type. In
             this case, the response will contain 0 datasets.
             
             7.    Expand the child lines defined by the Expand criteria (Expand
             criteria given in the BOM window) given the page size.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param BomLines: 
                         Input for executing the expansion.
             
        :param ExpandSettings: 
                         Â Â Â Â replay: List of stable IDs( Chain of clone stable ID from
                         TopBomline) on which replay to be performed.
             
        :param PageSize: 
                         Value: 0 means unlimited.
             
        :param ExpandOptions: 
                         Expand Options for the operation.
             
        :return: 214556Â Â Â Â Â Â Â Â Invalid relation to get associated
             objects.
        """
        ...
    def StopExpandBOMLines(self, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation stops further loading of objects from a previously executed expansion
             and clears all the memory allocated for the expansion operation. The expand cursor
             is deleted and the list of objects that are kept track by the expand cursor are removed
             from the server memory.
             
             The stopExpandBomlines does not unload any previously loaded objects. Also there
             is no locking or unlocking performed by the stopExpandBOMLines operation.
             

Use Cases:

             When an expansion is executed in structure and the expansion returns a large set
             of objects. The server process keeps the results of a expansion using a expand cursor
             object. At each nextExpandBOMLines operation, the results are further filtered and
             returned in batches specified by the load count. However, if the caller is not interested
             in consuming the expansion results further, then a stopExpandBOMLines could be called
             to release all the resources allocated for that expansion operation. This includes
             dropping the runtime expand cursor object and the list of lines kept track by the
             cursor. The cursor will be automatically deleted if it is exhausted.
             

Dependencies:

             nextExpandBOMLines, startExpandBOMLines
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param ExpandCursor: 
                         The SearchCursor for stopping the expansion.
             
        :return: 214556        Invalid cursor received.
        """
        ...

