import Cpd0.Services.Strong.Cpdcore._2011_06.StructureExpand
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExpandStructureContent2:
    """
    
ExpandStructureContent contains the expansion
            content for a given object in the starting scope of a structure expands operation.
            Resulting expansion content can be of several possible types; BOMLines and
            presented parents are returned in their own list, all other content is returned in
            the elementContent list.  Copy stable ID values are used to identify the relationship
            of a design component to a subset or a subset to a workset revision; these values
            are included if the caller requested it.
            
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
    CopyStableIDData: list[Cpd0.Services.Strong.Cpdcore._2011_06.StructureExpand.CopyStableIDData]
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
    ContentObjInfoInContextMap: System.Collections.Hashtable
    """
contentObjInfoInContextMap id object of BoToBoMap.
            
contentObjInfoInContextMap parameter : Map
            of (Teamcenter::BusinessObject, Teamcenter::BusinessObject) giving the Cpd0InfoInContext
            Attribute group for each of the Design Subset Element's content. The content object
            is the key, attribute group object is the value.
            
            NOTE: This is populated only if the "startingObject"
            of this structure is a Design Subset Element
            
"""

class ExpandStructureResponse2:
    """
    
            This is the response for startExpandStructure
            and nextExpandStructure; it contains the
            result of the expansion for the input starting scope.  If the expansion is only partially
            complete, the finished flag will be set to false and an expand cursor (expandCursor) is returned for input into a subsequent call to
            nextExpandStructure; otherwise, the finished flag will be set to true.  The service
            data contains any errors that occurred during the expansion.
            
    """
    def __init__(self, ) -> None: ...
    Content: list[ExpandStructureContent2]
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
    def NextExpandStructure2(self, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> ExpandStructureResponse2:
        """    
             Continues the expansion of one or more worksets, subsets, or design components using
             an expand cursor initially returned from startExpandStructure.
             Results are paged back to the client, and subsequent calls to nextExpandStructure may be required to get the entire set of expanded
             results.  Note: Applications should call stopExpandStructure
             if they wish to no longer fetch additional remaining expand results (e.g. after user
             termination of expand).
             

Use Cases:

             See SOA documentation for startExpandStructure
             for details about ExpandStructureResponse.
             

Dependencies:

             startExpandStructure2
             

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
    def StartExpandStructure2(self, StartingScope: list[Teamcenter.Soa.Client.Model.ModelObject], Controls: Cpd0.Services.Strong.Cpdcore._2011_06.StructureExpand.ExpandStructureControls) -> ExpandStructureResponse2: ...

