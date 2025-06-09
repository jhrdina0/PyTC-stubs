import System
import System.Collections
import Teamcenter.Services.Strong.Structuremanagement._2014_12.StructureSearch
import Teamcenter.Services.Strong.Structuremanagement._2021_06.StructureSearch
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExpandResponse2:
    """
    The found objects and the expand cursor that can be used in next Expand.
    """
    def __init__(self, ) -> None: ...
    ObjectsDone: int
    """Number of objects returned so far."""
    EstimatedObjectsLeft: int
    """Estimated number of objects 0f the structure."""
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
    ExtraObjs: list[Teamcenter.Services.Strong.Structuremanagement._2021_06.StructureSearch.ExtraObjects]
    """A list of Dataset objects for the lines returned."""
    AdditionalInfo: Teamcenter.Services.Strong.Structuremanagement._2014_12.StructureSearch.AdditionalInfo
    """Currently not used."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service Data for any error information. Typically, this will contain errors about
            any malformed search recipes.
            """

class StructureSearch:
    """
    Interface StructureSearch
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def NextExpandBOMLines2(self, PageSize: int, ExpandOptions: Teamcenter.Services.Strong.Structuremanagement._2021_06.StructureSearch.ExpandOptions, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> ExpandResponse2: ...
    def StartExpandBOMLines2(self, BomLines: list[Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject], ExpandSettings: System.Collections.Hashtable, PageSize: int, ExpandOptions: Teamcenter.Services.Strong.Structuremanagement._2021_06.StructureSearch.ExpandOptions) -> ExpandResponse2:
        """    
             This operation initiates a sequence of operations to expand BOMLine objects
             based on  filter information on BOMWindow and returns a list of BOMLine
             objects. Filter information could be a complex expression set that combines multiple
             simpler Expand terms in a logical sequence.
             
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
             dataset information is specified - dataset relation is IMAN_reference and dataset
             type is Text then the response will contain the specified datasets (if there are
             any).
             
             5.    Expand the child lines from the structure given the page
             size. The dataset information contains the minimum number of dataset objects to be
             returned. For example, dataset relation is given as IMAN_reference, dataset type
             is Text, expandRelatedObjects is 1 and min datasets to be returned is set to 10.
             In this case, the response will contain only 10 specified datasets.
             
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
                         childrenThenDepthFirst: TRUE/FALSE, TRUE means expand children and then depth
                         first.
             
        :param PageSize: 
                         Value: 0 means unlimited.
             
        :param ExpandOptions: 
                         Expand Options for the operation.
             
        :return: 214560        Invalid named reference for DataSet objects.
        """
        ...

