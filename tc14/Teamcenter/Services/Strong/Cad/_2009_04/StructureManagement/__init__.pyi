import System
import System.Collections
import Teamcenter.Services.Strong.Cad._2008_06.StructureManagement
import Teamcenter.Soa.Client.Model
import typing

class AttributesInfoForObject:
    """
    Contains classname and vector of AttributesInfos structure
    """
    def __init__(self, ) -> None: ...
    TopLineAttrThatRefersToObject: str
    """Name of the attribute that refers to the object"""
    AttrsToSet: list[AttributesInfos]
    """List of AttributesInfos"""

class AttributesInfos:
    """
    Contains name/values pair data to be set as attributes on the related object.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Attribute name"""
    Values: list[str]
    """Attribute values"""

class RelativeStructureParentInfo:
    """
    Contains information about the parent BOM line representation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller.  This ID is used to identify return data
            elements and partial errors associated with this input structure.  If clientId is not provided then it can be difficult to align the
            input with any returned errors.
            """
    Complete: bool
    """
            Flag that if true signifies that the structure represented in the input is the full
            representation of the structure under the input parent. Any other structure relations
            that exist in Teamcenter but are not represented in the input will be removed.
            """
    BomViewTypeName: str
    """
            The type of the BOM view to create under the parent bomViewTypeName
            object.  If not specified, CreateOrUpdateRelativeStructurePref
bomViewTypeName will be used as the default.
            """
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """
            Object reference of the Item Revision context assembly object to create or update
            the child occurrence.  This is a required input.  An error will be returned if a
            valid parent is not specified.
            """
    ChangeContext: Teamcenter.Soa.Client.Model.ModelObject
    """Designated for future implementation."""
    LastModifiedOfBVR: System.DateTime
    """
            Last modified date of BOM view revision (BVR) under the input parent.  This input is not required.  If this input date is different
            than the current last modified date and the overwriteForLastModDate
            preference is false the input will be ignored and processing will continue with the
            next input.  In this scenario, error 215033 will be returned.  If the dates are different
            and the overwriteForLastModDate preference
            is true, processing will continue with the current input.  In this scenario, error
            215034 will be returned.
            """
    Precise: bool
    """
            Flag for updating the BVR to precise (true) or imprecise (false).  Specifying precise
            as true means the child occurrences reference item revisions, whereas specifying
            precise as false (imprecise) means the child occurrences reference items.
            """
    SupportingClassAttrs: list[AttributesInfoForObject]
    """
            A list of object property names for the parent BOM line and attributes to set on
            the corresponding objects.  For example, supportingClassAttrs
topLineAttrThatRefersToObject could be set
            to the property name bl_bomview_rev and attrsToSet
            could include the attribute legacy_transform_factor with a value of 0.5 to
            set on the BOM view revision object.
            """

class CreateOrUpdateRelativeStructureInfo:
    """
    Input structure for createOrUpdateRelativeStructure.
    """
    def __init__(self, ) -> None: ...
    ParentInfo: RelativeStructureParentInfo
    """Parent info structure containing information about the parent BOM line representation."""
    ChildInfo: list[Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.RelativeStructureChildInfo2]
    """
            Child info structure for creating the occurrence or updating the occurrence attributes.
            If no child objects are specified and RelativeStructureParentInfo
complete is true, all existing child objects
            will be removed.  If no child objects are specified and RelativeStructureParentInfo
complete is false, the input is ignored.
            """

class CreateOrUpdateRelativeStructurePref:
    """
    Preference structure for createOrUpdateRelativeStructure.
    """
    def __init__(self, ) -> None: ...
    OverwriteForLastModDate: bool
    """
            Flag to check whether the structure needs to be updated if the input last modified
            date is different from the current last modified date of the object in Teamcenter.
            If false, but the RelativeStructureParentInfo
lastModifiedOfBVR input specified is different
            than the set modified date, partial error 215033 will be returned.
            """
    ContinueOnError: bool
    """
            Flag to indicate whether the operation should continue processing to the next input
            when an error is encountered.
            """
    BomViewTypeName: str
    """
            The default BOM view type to create or the view type of the child to be added to
            the parent BOMViewRevision This default value can be overridden for individual
            parent by specifying the bomViewTypeName
            in  RelativeStructureParentInfo parentInfo input. The default value can also be overridden for
            individual children by specifying the childBomViewType
            in the RelativeStructureChildInfo childInfo input.
            """
    CadOccIdAttrName: str
    """
            Represents the occurrence note type which holds the value for the CAD occurrence
            ID or this can be the PSOccurrenceThread UID if the integration does not use
            a note type.
            """
    ObjectTypes: list[str]
    """
            List of object types that the client is interested in.  If complete
            is true, object types or subtypes that exist in the structure in Teamcenter but are
            not in this list are removed.  If complete
            is true, but no objectTypes are specified,
            then all objects types or subtypes are removed from the existing structure in Teamcenter.
            If complete is false, objectTypes is ignored.
            """

class CreateOrUpdateRelativeStructureResponse:
    """
    
            The response from the createOrUpdateRelativeStructure
            operation.
            
    """
    def __init__(self, ) -> None: ...
    Output: System.Collections.Hashtable
    """Map of client IDs to MappedReturnData."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData.  This operation will populate
            the ServiceData with created occurrences,
            BOM views and BOM view revisions, updated occurrences and BOM view revisions, and
            any implicitly deleted occurrences.
            """

class MappedReturnData:
    """
    
            Map of returned data that is relevant to the created or updated occurrence for the
            given client ID.
            
    """
    def __init__(self, ) -> None: ...
    OccThread: Teamcenter.Soa.Client.Model.ModelObject
    """The occurrence thread for tracking the created or updated occurrence."""
    Occurrence: Teamcenter.Soa.Client.Model.ModelObject
    """The occurrence object that was created or updated."""
    Bvr: Teamcenter.Soa.Client.Model.ModelObject
    """The BOM view revision that was created or updated."""

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateRelativeStructure(self, Inputs: list[CreateOrUpdateRelativeStructureInfo], Pref: CreateOrUpdateRelativeStructurePref) -> CreateOrUpdateRelativeStructureResponse:
        """    
             This operation creates or updates the relative structure for the input parent assembly
             and child components.  The objects created or updated by this operation include a
             BOM view (BV), BOM view revision (BVR) and occurrence data (PSOccurrence,
             PSOccurrenceThread).
             

             Before creating the relative structure objects and relations, this operation will
             check that the structure to be created does not already exist.  If the occurrence
             exists but the input attribute values differ from those already set, an attempt is
             made to update the values.
             

             This operation assumes the input is in a bottom up format such that if any failures
             occur, the structure that is created will still be consumable.  For example:
             

             Parent assembly A, subassembly B and child C are input into this operation.  If the
             relative structure for subassembly B and child C is created successfully but an error
             occurs during the creation of the structure for assembly A and subassembly B, the
             client can still access the subassembly B, child C relative structure.
             

             No attempt is made in the operation to rearrange the input and process it in the
             correct order. One parent context object is processed at one time and it is assumed
             that all edits for a given parent context come in as one set of input.
             


Use Cases:

             Use Case 1:
             

             User adds an existing component to an existing assembly to create a relative occurrence.
             
             For this operation, the assembly is passed in as the parent and the component is
             passed in as the child.  The relative occurrence is created and a map of the input
             clientID to MappedReturnData
             is returned in output and the occurrence,
             BOM view and BOM view revision are returned as created objects in ServiceData.
             

             Use Case 2:
             

             User wants to update the position of the child component relative to the parent assembly.
             
             For this operation, the transform on the child occurrence information is updated
             with the new position relative to the parent.  The assembly is passed in as the parent
             and the component is passed in as the child.  The relative occurrence is updated
             and a map of the clientID to MappedReturnData is returned in output
             and the occurrence and BOM view revision are returned as updated objects in ServiceData.
             


Dependencies:

             createOrUpdateParts, createObjects
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Inputs: 
                         List of input structures that specify all the children to be added to the specified
                         parent assembly.
             
        :param Pref: 
                         The structure for setting specific preference input used by this operation.
             
        :return: 
        """
        ...

