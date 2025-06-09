import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CopyStableIDData3:
    """
    
            CopyStableIDData3 contains a map of copy stable ID values for design components within
            a subset.
            
    """
    def __init__(self, ) -> None: ...
    Subset: Teamcenter.Soa.Client.Model.Strong.POM_object
    """The subset which is the context for the copy stable ID values."""
    CopyStableIDMap: System.Collections.Hashtable
    """
            A map (BusinessObject, string) of design components, design features and other members
            of a subset to their copy stable ID within the subset.
            """

class ExpandStructureContent3:
    """
    
            ExpandStructureContent3 contains the expansion content for a given object in the
            starting scope of a structure expands operation. Resulting expansion content can
            be of several possible types; BOMLine objects and presented parents are returned
            in their own list, all other content is returned in the elementContent list. Copy
            stable ID values are used to identify the relationship of a design component to a
            subset or a subset to a workset revision; these values are included if the caller
            requested it.
            
    """
    def __init__(self, ) -> None: ...
    StartingObject: Teamcenter.Soa.Client.Model.ModelObject
    """The object from starting scope which resulted in the expansion of the returned content."""
    BomLineContent: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """Contains any BOMLine objects that resulted from the expansion."""
    ElementContent: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Contains any model element content that resulted from the expansion."""
    PresentedParentContent: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            Contains any presented parent content that were included because it was requested
            (via includePresentedParents) in the expansion
            controls.
            """
    CopyStableIDData: list[CopyStableIDData3]
    """
            A list of copy stable ID data (CopyStableIDData2).
            
copyStableIDMap is object of BoToStringMap.
            
copyStableIDMap parameter : Map of (BusinessObject, string)
            """
    SourceTargetMap: System.Collections.Hashtable
    """
            Reserved for future use.
            
sourceTargetMap id object of BoToBoMap.
            
sourceTargetMap parameter : Map of (BusinessObject, BusinessObject)
            """
    ContentObjInfoInContextMap: System.Collections.Hashtable
    """
contentObjInfoInContextMap id object of BoToBoMap.
            
contentObjInfoInContextMap parameter : Map
            of (BusinessObject, BusinessObject) giving
            the Cpd0InfoInContext Attribute group for
            each of the Design Subset Element's content. The content object is the key, attribute
            group object is the value.
            
            NOTE: This is populated only if the "startingObject"
            of this structure is a Design Subset Element
            """

class ExpandStructureControls3:
    """
    
            A set of controls for clients to stipulate the output of the expand processing.These
            controls can be set at the start of the expand, and remain constant for the duration
            of the expand, including any subsequent calls to nextExpandStructure3.
            
    """
    def __init__(self, ) -> None: ...
    LevelsToExpand: int
    """
            The number of levels to expand, where 0 signifies to expand all levels, 1 signifies
            to expand the next level only. Values other than 0 or 1 are not supported.
            """
    IncludePresentedParents: bool
    """If true, presented parents of design components will be added to the expand results."""
    IncludeCopyStableIDMaps: bool
    """If true, copy stable ID maps will be returned in the response."""
    IncludeSourceObjectForSubsets: bool
    """
            Specifies if source objects are to be returned with or without encoded in-context
            data for Sparse operations(Expand of Rlz0Composition or Rlz0Subset).
            It is also applied on the source objects returned as part of copyStableIDMap3,only in the case of expand of a Rlz0Composition
            or  Rlz0Subset.Default value is false.
            
            If false, source objects are returned with encoded in-context data.
            
            If true, source objects are returned without encoded in-context data.
            """
    SuggestedPageSize: int
    """
            Controls the average number of objects to return per call (to startExpandStructure
            and nextExpandStructure); if the value is out of bounds of the DefaultMaximumLoadSize
            site preference, then the closest bound of the site preference setting will be used.
            
Note: Returned BOMLine objects and element content are both considered
            to consume the page size, while presented parent content, copy stable ID map content
            and source to target map content do not.
            
Note: Calls to nextStructureExpand3 will increment the page size on
            subsequent calls by the value specified in the DefaultLoadCountIncreateRate site
            preference.
            
Note: A current internal maximum page size limit is set to 2000 objects and
            will override DefaultMaximumLoadSize preference if its value exceeds 2000 objects.
            """
    ExpandSubsetAsSaved: bool
    """Reserved for future use."""
    PreLoadVisualizationDatasets: bool
    """
            Pre load datasets used by visualization into the server so that they may be returned
            via property references on any Mdl0PositionedModelElement object. The default
            value is set to false. It is strongly recommended to set this value to true, if dataset
            references are put into the property policy for Mdl0PositionedModelElement
            objects.
            """
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            A reference to a configuration context object. It is used in limited circumstances
            within the expand; specifically it is used configure the children of expanded Cpd0DesignElements
            by effectivity only. The configuration context is ignored for other input types,
            and may be omitted if the starting scope contains only object of the other input
            types.
            """
    EffectivityFormulaOverlayMap: System.Collections.Hashtable
    """
            A map of (BusinessObject, string)
            
            Key: Source application model(Mdl0ApplicationModel).
            
            Value: The effectivity overlay information (string)which will be combined with effectivity
            configuration information criteria defined on the Rlz0Subset to further narrow
            the scope of content returned by the expand.
            """
    VariantFormulaOverlayMap: System.Collections.Hashtable
    """
            A map of (BusinessObject, string)
            
            Key: Source spplication model(Mdl0ApplicationModel).
            
            Value:The variant overlay information (string)which will be combined with variant
            configuration information criteria defined on the Rlz0Subset to further narrow
            the scope of content returned by the expand.
            """

class ExpandStructureResponse3:
    """
    
            This is the response for startExpandStructure3
            and nextExpandStructure3; it contains the
            result of the expansion for the input starting scope. If the expansion is only partially
            complete, the finished flag will be set to false and an expand cursor (expandCursor) is returned for input into a subsequent call to
            nextExpandStructure3; otherwise, the finished
            flag will be set to true. The service data contains any errors that occurred during
            the expansion.
            
    """
    def __init__(self, ) -> None: ...
    Content: list[ExpandStructureContent3]
    """Expanded content."""
    ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject
    """
            Cursor object to pass to subsquent call to nextExpandStructure3
            or stopExpandStructure3
"""
    Finished: bool
    """If true,there is no more content to return; otherwise false."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Returns any errors which occurred during expansion."""

class StructureExpand:
    """
    Interface StructureExpand
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def NextExpandStructure3(self, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> ExpandStructureResponse3:
        """    
             Continues the expansion of one or more worksets, subclasses of compositions,subsets,
             or design components using an expand cursor initially returned from startExpandStructure3. Results are paged back to the client, and
             subsequent calls to nextExpandStructure3
             may be required to get the entire set of expanded results. Note: Applications should
             call stopExpandStructure if they wish to
             no longer fetch additional remaining expand results (e.g. after user termination
             of expand).
             

Use Cases:

             See SOA documentation for startExpandStructure3
             for details about the usecase.
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param ExpandCursor: 
                         An expand cursor returns from nextExpandStructure3
             
        :return: .
        """
        ...
    def StartExpandStructure3(self, StartingScope: list[Teamcenter.Soa.Client.Model.ModelObject], Controls: ExpandStructureControls3) -> ExpandStructureResponse3:
        """    
             Start an expansion of one or more worksets,subclasses of compositions, subsets, or
             design components. Objects are expanded in the order listed. Results are paged back
             to the client and subsequent calls to nextExpandStructure3 may be required
             to get the entire set of expanded results. Note: Applications should call stopExpandStructure3
             if they wish to no longer fetch additional remaining expand results (e.g. after user
             termination of expand).
             

Use Cases:

             This API supports the navigation of workset content and presented children of design
             components. Expanded workset content includes item sub structure, subsets, and subset
             content. Subset content is made up of design components and design features previously
             configured and selected from a product design by execution of the subsets search
             recipe. Presented children of design components (Cpd0DesignElement) are found
             by reverse navigation of their presented parent (cpd0presented_parent)
             property.
             

Use Case 1: Expand Workset One Level
             
             Get the first level children of a workset. The results include any immediate occurrences
             of items in the workset and any subsets in the workset. All results are returned
             as BOMLine objects (note: subsets are returned via Cpd0SubsetLine objects).
             

Use Case 2: Get Presented Children of a Design Component
             

             Get the first level presented children of a design component. The results include
             all design components that reference the input design components as their presented
             parent. All results are returned as design component objects.
             

Use Case 3: Expand a Subset to get its Design Components and Design Features
             

             Get the content of a subset. The results include all design components and design
             features that were configured and selected last time the subset recipe was executed
             (replayed). All results are returned as design component or design feature objects.
             
             Set the subset(s) of interest as the starting scope of the expand; this can be done
             in two ways
             

             Method 1: via a subset line (Cpd0SubsetLine)
             
             Method 2: via a direct reference
             
             Note: Method 1 is the more commonly used scenario.
             

Use Case 4: Expand a subclass of Rlz0Composition object.
             

             Expansion of an Rlz0Composition object returns all the Rlz0Subset objects that it
             contains.
             

Use Case 5: Expand a Rlz0Subset object.
             

             Expansion of an Rlz0Subset object returns sparsely or dynamically realized
             model elements (Mdl0ModelElement) from source application model (Mdl0ApplicationModel).
             Unlike the concept of Full or Static Realization, model elements (Mdl0ModelElement)
             in the target application model (Mdl0ApplicationModel) are not new copies
             rather simple references to objects in source application model.
             

             Also, this API provides the support to expand appropriate sparse elements by applying
             effectivity and variant overlay strings for input Mdl0ApplicationModel that
             are used during the expansion of composition (Rlz0Composition) or subset (Rlz0Subset).
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param StartingScope: 
                         Note: <b>ImanItemLine</b> objects (other than Cpd0WorksetLine) are not a supported
                         type for starting scope. Application should use normal BOM expand API to process
                         <b>ImanItemLines</b>.
             
        :param Controls: 
                         A set of controls (<font face="courier" height="10">ExpandStructureControls3</font>)
                         which govern the expansion of objects.This includes expansion of objects which are
                         subclasses of <b>Rlz0Composition</b>.
             
        :return: 2. 279055 - The provided number of levels to expand is invalid. Valid values are
             0 or 1 for this operation.
        """
        ...

