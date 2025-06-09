import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CopyStableIDData:
    """
    
CopyStableIDData contains a map of copy stable ID values for design components within
            a subset.
            
    """
    def __init__(self, ) -> None: ...
    Subset: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignSubsetElement
    """The subset which is the context for the copy stable ID values."""
    CopyStableIDMap: System.Collections.Hashtable
    """
            A map of design components, design features and other members of a subset to their
            copy stable ID within the subset.
            
copyStableIDMap is object of BoToStringMap.
            
copyStableIDMap parameter : Map of (Teamcenter::BusinessObject, std::string)
            """

class ExpandStructureContent:
    """
    
ExpandStructureContent contains the expansion
            content for a given object in the starting scope of a structure expands operation.
            Resulting expansion content can be of several possible types; BOMLines and
            presented parents are returned in their own list, all other content is returned in
            the elementContent list.  Copy stable ID values are used to identify the relationship of
            a design component to a subset or a subset to a workset revision; these values are
            included if the caller requested it.
            
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
    CopyStableIDData: list[CopyStableIDData]
    """
            A list of copy stable ID data (CopyStableIDData).
            
copyStableIDMap is object of BoToStringMap.
            
copyStableIDMap parameter : Map of (Teamcenter::BusinessObject, std::string)
            """
    SourceTargetMap: System.Collections.Hashtable
    """
            Reserved for future use.
            
sourceTargetMap id object of BoToBoMap.
            
sourceTargetMap parameter : Map of (Teamcenter::BusinessObject,Teamcenter::BusinessObject)
            """

class ExpandStructureControls:
    """
    
            A set of controls for clients to stipulate the output of the expand processing.
            These controls can be set at the start of the expand, and remain constant for the
            duration of the expand, including any subsequent calls to nextExpandStructure.
            
    """
    def __init__(self, ) -> None: ...
    LevelsToExpand: int
    """
            The number of levels to expand, where 0 signifies to expand all levels, 1 signifies
            to expand the next level only.  Values other than 0 or 1 are not supported.
            """
    IncludePresentedParents: bool
    """If true, presented parents of design components will be added to the expand results."""
    IncludeCopyStableIDMaps: bool
    """
            If true, copy stable ID maps will be returned
            in the response.
            """
    IncludeSourceObjectForSubsets: bool
    """Reserved for future use."""
    SuggestedPageSize: int
    """
            Controls the average number of objects to return per call (to startExpandStructure and nextExpandStructure);
            if the value is out of bounds of the DefaultMaximumLoadSize
            site preference, then the closest bound of the site preference setting will be used.
            
Note: Returned BOMLines and element content are both considered to
            consume the page size, while presented parent content, copy stable ID map content
            and source to target map content do not.
            
Note: Calls to nextStructureExpand
            will increment the page size on subsequent calls by the value specified in the DefaultLoadCountIncreateRate site preference.
            
Note: A current internal maximum page size limit is set to 2000 objects and
            will override DefaultMaximumLoadSize preference
            if its value exceeds 2000 objects.
            
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
            A reference to a configuration context object.  It is used in limited circumstances
            within the expand; specifically it is used configure the children of expanded Cpd0DesignElements
            by effectivity only.The configuration context is ignored for other input types, and
            may be omitted if the starting scope contains only object of the other input types.
            """

class ExpandStructureResponse:
    """
    
            This is the response for startExpandStructure
            and nextExpandStructure; it contains the
            result of the expansion for the input starting scope.  If the expansion is only partially
            complete, the finished flag will be set to false and an expand cursor (expandCursor) is returned for input into a subsequent call to
            nextExpandStructure; otherwise, the finished
            flag will be set to true.  The service data contains any errors that occurred during
            the expansion.
            
    """
    def __init__(self, ) -> None: ...
    Content: list[ExpandStructureContent]
    """expanded content"""
    ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject
    """
            Cursor object to pass to subsquent call to nextExpandStructure
            or stopExpandStructure.
            """
    Finished: bool
    """Set to true when there is no more content to return; false, otherwise."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Returns any errors which occurred during expansion."""

class StructureExpand:
    """
    Interface StructureExpand
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def NextExpandStructure(self, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> ExpandStructureResponse:
        """    
             Continues the expansion of one or more worksets, subsets, or design components using
             an expand cursor initially returned from startExpandStructure.
             Results are paged back to the client, and subsequent calls to nextExpandStructure may be required to get the entire set of expanded
             results.  Note: Applications should call stopExpandStructure
             if they wish to no longer fetch additional remaining expand results (e.g. after user
             termination of expand).
             

Use Cases:

             See SOA documentation for startExpandStructure for details about ExpandStructureResponse.
             

Dependencies:

             startExpandStructure
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param ExpandCursor: 
                         An expand cursor returns from <font face="courier" height="10">startExpandStructure</font>

        :return: .
        """
        ...
    def StartExpandStructure(self, StartingScope: list[Teamcenter.Soa.Client.Model.ModelObject], Controls: ExpandStructureControls) -> ExpandStructureResponse:
        """    
             Start an expansion of one or more worksets, subsets, or design components.   Objects
             are expanded in the order listed.  Results are paged back to the client and subsequent
             calls to nextExpandStructure may be required
             to get the entire set of expanded results.  Note: Applications should call stopExpandStructure if they wish to no longer fetch
             additional remaining expand results (e.g. after user termination of expand).
             

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
             

             Get the configuration to be used on the workset. This is accomplished by the following
             steps::
             

Open a BOM window (BOMWindow);
             
Apply a revision rule to the window
             
Set the workset or workset revision as the top line in the window
             
Use the top line as a starting scope of startStructureExpand





Set the number of levels to expand (levelsToExpand)
             to 1
             
Set other expansion control flags, as needed
             
Initiate the expand using the startStructureExpand
             operation
             
Determine if the expansion is complete by testing the finished flag
             in the response.
             
If the expansion is not complete, use the nextStructureExpand
             operation to retrieve the next batch of expansion results from the Teamcenter; or
             use the stopStructureExpand operation if
             no more results of the expand are desired (e.g. user initiated abort).
             



Use Case 2: Get Presented Children of a Design Component 


             Get the first level presented children of a design component. The results include
             all design components that reference the input design components as their presented
             parent. All results are returned as design component objects.
             

Set the design components of interest as the starting scope of the
             expand
             
Set any expansion control flags, as needed
             
Initiate the expand using the startStructureExpand
             operation
             
Determine if the expansion is complete by testing the finished flag
             in the response.
             
If the expansion is not complete, use the nextStructureExpand
             operation to retrieve the next batch of expansion results from the Teamcenter; or
             use the stopStructureExpand operation if
             no more results of the expand are desired (e.g. user initiated abort).
             




Use Case 3: Expand a Subset to get its Design Components and Design Features


             Get the content of a subset. The results include all design components and design
             features that were configured and selected last time the subset recipe was executed
             (replayed). All results are returned as design component or design feature objects.
             
             Set the subset(s) of interest as the starting scope of the expand; this can be done
             in two ways
             

Method 1: via a subset line (Cpd0SubsetLine)
             

Get a Cpd0SubsetLine object from a previous expansion.
             
Set it as a starting scope for an expand.
             


Method 2: via a direct reference


Get a reference to a subset (Cpd0DesignSubsetElement)
             
Set it as a starting scope for an expand.
             


             Note: Method 1 is the more commonly used scenario.
             


Set any expansion control flags, as needed
             
Initiate the expand using the startStructureExpand
             operation
             
Determine if the expansion is complete by testing the finished flag
             in the response.
             
If the expansion is not complete, use the nextStructureExpand
             operation to retrieve the next batch of expansion results from the Teamcenter; or
             use the stopStructureExpand operation if
             no more results of the expand are desired (e.g. user initiated abort).
             



Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param StartingScope: 

        :param Controls: 
                         A set of controls (<font face="courier" height="10">ExpandStructureControls</font>)
                         which govern the expansion of objects.
             
        :return: ).
        """
        ...
    def StopExpandStructure(self, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> bool:
        """    
             Terminates an expansion initially started by a call to startExpandStructure.
             Clients should only call this operation when there are still results to return, as
             indicated by the finished flag being set
             to false in the last response from either startExpandStructure or nextExpandStructure operations.
             

Use Cases:

             See SOA documentation for startExpandStructure for use cases involving this
             operation.
             

Dependencies:

             startExpandStructure
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param ExpandCursor: 
                         An expand cursor initially returned from <font face="courier" height="10">startExpandStructure</font>

        :return: Return value is always false.
        """
        ...

