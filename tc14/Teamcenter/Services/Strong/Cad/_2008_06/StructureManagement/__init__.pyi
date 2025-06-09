import System
import System.Collections
import Teamcenter.Services.Strong.Cad._2007_01.StructureManagement
import Teamcenter.Services.Strong.Cad._2007_12.StructureManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AbsOccAttachment2:
    """
    
            Contains an override object which is attached as the override data and a relationTypeName to relate the AbsOccData
            to the object.
            
    """
    def __init__(self, ) -> None: ...
    OverrideObject: Teamcenter.Soa.Client.Model.ModelObject
    """The object which is attached as the override data."""
    RelationTypeName: str
    """
            Relation name or property name to relate AbsOccData
            to object.
            """

class DatasetInfo:
    """
    
            Contains clientId, Dataset object reference for update, Name attribute value, basisName,
            description, Type attribute value, lastModifiedOfDataset, ID attribute value, datasetRev,
            createNewVersion flag, namedReferencePreference, dataList, datasetFileInfos, and
            List of NamedReferenceObjectInfos.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller.  This ID is used to identify return data
            elements and partial errors associated with this input structure.  If clientId is not provided then it can be difficult to align the
            input with any returned errors.
            """
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            The dataset object reference.  This input can be null for create, but it is required
            for update.
            """
    Name: str
    """The dataset name attribute value."""
    BasisName: str
    """The basis name attribute value.  This is used when the name is null or blank."""
    Description: str
    """The dataset description attribute value."""
    Type: str
    """The dataset type name."""
    LastModifiedOfDataset: System.DateTime
    """Last modified date of the dataset."""
    Id: str
    """The dataset ID attribute value."""
    DatasetRev: str
    """The dataset revision attribute value."""
    CreateNewVersion: bool
    """Flag that if true signifies a new version of the dataset should be created."""
    NamedReferencePreference: str
    """
            The preference name which holds the list of named references to delete from one dataset
            version to the next.
            """
    DataList: list[NameValueStruct]
    """The attribute name and values to set on the dataset."""
    DatasetFileInfos: list[DatasetFileInfo]
    """List of dataset file information."""
    NamedReferenceObjectInfos: list[NamedReferenceObjectInfo]
    """List of dataset named reference information."""

class AbsOccCreateDatasetAttachmentInfo:
    """
    Dataset information for attaching a dataset to the absolute occurrence.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller.  This ID is used to identify return data
            elements and partial errors associated with this input structure.  If clientId is not provided then it can be difficult to align the
            input with any returned errors.
            """
    DatasetInfo: DatasetInfo
    """The information used to create or update the dataset."""
    RelationTypeName: str
    """The relation type used for the dataset attached to the absolute occurrence."""
    CreateIfFound: bool
    """
            Flag to specify whether to create, update or attach the specified dataset if the
            supplied type and relation already exist as an override.
            """

class FormInfo:
    """
    Form information for the occurrence.
    """
    def __init__(self, ) -> None: ...
    FormObject: Teamcenter.Soa.Client.Model.Strong.Form
    """
            The form object reference.  This input can be null for create, but it is required
            for update.
            """
    Name: str
    """The form name attribute value."""
    Description: str
    """The form description attribute value."""
    FormType: str
    """The form type name."""
    Attributes: list[NameValueStruct]
    """The attributes to be set or updated on the form."""

class AbsOccCreateFormAttachmentInfo:
    """
    Form information for attaching a form to the absolute occurrence.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller.  This ID is used to identify return data
            elements and partial errors associated with this input structure.  If clientId is not provided then it can be difficult to align the
            input with any returned errors.
            """
    FormInfo: FormInfo
    """The information used to create or update the form."""
    RelationTypeName: str
    """The relation type used for the form attached to the absolute occurrence."""
    CreateIfFound: bool
    """
            Flag to specify whether to create, update or attach the specified form if the supplied
            type and relation already exist as an override.
            """

class AbsOccDataGRMExpansionInfo:
    """
    
            Contains a relationName and secondary objects attached as a override with the given
            relation.
            
    """
    def __init__(self, ) -> None: ...
    RelationName: str
    """The relation name found for the override."""
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The secondary objects attached as a override with the given relation."""

class AbsOccDataInfo2:
    """
    Detailed attribute information for the occurrence.
    """
    def __init__(self, ) -> None: ...
    OverridesToSet: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.AttributesInfo]
    """List of attribute information to set as overrides for the occurrence."""
    OverridesToRemove: list[str]
    """
            List of attribute names that will be unset or removed as overrides for the occurrence.
            For example, to remove a transform override, add the attribute name for the transform
            to this list.
            """
    AsRequired: bool
    """Used to set the quantity as required occurrence flag."""
    OccTransform: list[float]
    """Positioning information for the occurrence."""
    OccNotes: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.OccNote]
    """List of note information for the occurrence."""
    Attachments: list[AbsOccAttachment2]
    """Attachments to add to the occurrence."""
    AttachmentsToUnattach: list[AbsOccAttachment2]
    """Attachments to remove from the occurrence."""
    DatasetAttachments: list[AbsOccCreateDatasetAttachmentInfo]
    """Dataset attachments to create or update for the occurrence."""
    FormAttachments: list[AbsOccCreateFormAttachmentInfo]
    """Form attachments to create or update for the occurrence."""
    ClientIdOfUsedArrangement: str
    """Client ID of the used arrangement created for this absolute occurrence."""
    UsedArr: Teamcenter.Soa.Client.Model.Strong.AssemblyArrangement
    """Reference of existing used arrangement for this absolute occurrence."""
    BoundingBoxInfo: list[BoundingBoxInfo]
    """
            No longer used. Bounding Box information is now passed in through datasetAttachments.
            """

class AbsOccDataPref:
    """
    
            Contains a filter that needs to be applied when expanding a GRM override and the
            filter that needs to be applied on the data that is returned based on the qualifier.
            
    """
    def __init__(self, ) -> None: ...
    RelationFilterInfos: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.RelationAndTypesFilter]
    """The filter that needs to be applied when expanding a GRM override."""
    QualifierFilter: str
    """
            The filter that needs to be applied on the data that is returned based on the qualifier.
            Legal values are : None IncludeBvrOnlyQualifyingOverrides IncludeBvrAndUpperQualifyingOverrides
"""

class AbsOccInfo2:
    """
    Attribute information for the occurrence.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller.  This ID is used to identify return data
            elements and partial errors associated with this input structure.  If clientId is not provided then it can be difficult to align the
            input with any returned errors.
            """
    AbsOcc: Teamcenter.Soa.Client.Model.Strong.AbsOccurrence
    """Absolute occurrence object reference.  This input can be null for create."""
    CadOccIdPath: list[str]
    """Path of CAD occurrence IDs that identify or find the BOM line."""
    AbsOccData: AbsOccDataInfo2
    """Override data to set for the absolute occurrence."""

class AbsOccQualifierInfo:
    """
    Contains the context BVR for which the overrides are to be retrieved and an upperQualifier.
    """
    def __init__(self, ) -> None: ...
    QualifyingBVR: Teamcenter.Soa.Client.Model.Strong.PSBOMViewRevision
    """The context BVR for which the overrides are to be retrieved."""
    UpperQualifier: Teamcenter.Soa.Client.Model.ModelObject
    """Context object of the override (such as Arrangement)."""

class DataOverrideInfo:
    """
    Contains overrideData and GRM override information.
    """
    def __init__(self, ) -> None: ...
    OverrideData: Teamcenter.Soa.Client.Model.Strong.AbsOccData
    """
            The AbsOccData object, which has information about qualifier, absolute ocuurence
            and override information.
            """
    ExpandedOverrides: list[AbsOccDataGRMExpansionInfo]
    """The GRM override information if the AbsOccData is of type AbsOccGRMAnchor."""

class AbsOccStructureDataInfo:
    """
    
            Contains the list of apn and occurrence thread path that the override are applied.
            The occurrence thread paths that are returned & dataOverrideInfo.
            
    """
    def __init__(self, ) -> None: ...
    OccThreadPaths: list[ApnToThreadPathStruct]
    """
            The list of apn and occurrence thread path that the override are applied. The occurrence
            thread paths that are returned for the given override are in top down order. Since
            the operation returns unconfigured data, the client needs to match the thread paths
            in previously expanded context with the returned ones to determine the exact override.
            """
    DataOverrideInfo: DataOverrideInfo
    """dataOverrideInfo"""

class ApnToThreadPathStruct:
    """
    
            Contains the appearance path node and the occurrence thread path corresponding to
            the apn.
            
    """
    def __init__(self, ) -> None: ...
    Apn: Teamcenter.Soa.Client.Model.Strong.MEAppearancePathNode
    """The appearance path node"""
    OccThreadPath: list[Teamcenter.Soa.Client.Model.Strong.PSOccurrenceThread]
    """The occurrence thread path corresponding to the apn"""

class BoundingBox:
    """
    Holds the boundingbox co-ordinates  information.
    """
    def __init__(self, ) -> None: ...
    Xmin: float
    """BoundingBox x-coordinate min value in double"""
    Ymin: float
    """BoundingBox y-coordinate min value in double"""
    Zmin: float
    """BoundingBox z-coordinate min value in double"""
    Xmax: float
    """BoundingBox x-coordinate max value in double"""
    Ymax: float
    """BoundingBox y-coordinate max value in double"""
    Zmax: float
    """BoundingBox z-coordinate max value in double"""

class BoundingBoxInfo:
    """
    
            BoundingboxInfo contains boundingbox information and dataset to which it will be
            attached.This Dataset member corresponds to the AbsOccAttachment.overrideObject member
            to which to apply Bounding Box information.
            
    """
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Dataset object to apply BoundingBox info to"""
    BoundingBoxVector: list[BoundingBox]
    """List of xyz coordinate info for Dataset bounding"""

class CommitDatasetFileInfo:
    """
    Contains basic information for a file to be uploaded to a dataset.
    """
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """The dataset object reference."""
    CreateNewVersion: bool
    """Flag that if true signifies a new version of the file should be created."""
    DatasetFileTicketInfos: list[DatasetFileTicketInfo]
    """List of dataset file ticket information."""

class CreateOrUpdateAbsoluteStructureInfo3:
    """
    Input structure for createOrUpdateAbsoluteStructure.
    """
    def __init__(self, ) -> None: ...
    LastModifiedOfBVR: System.DateTime
    """
            Last modified date of BOM view revision (BVR) under the input contextItemRev.  This input is not required.  If this input date
            is different than the current last modified date and the overwriteForLastModDate
            preference is false the input will be ignored and processing will continue with the
            next input.  In this scenario, error 215033 will be returned.  If the dates are different
            and the overwriteForLastModDate preference
            is true, processing will continue with the current input.  In this scenario, error
            215034 will be returned.
            """
    ContextItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            Item revision object reference of the context assembly to create or validate the
            occurrence.  This is a required reference input.
            """
    BvrAbsOccInfo: list[AbsOccInfo2]
    """List of absolute occurrence information for the BVR qualified overrides."""
    ArrAbsOccInfo: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.AssemblyArrangementInfo]
    """
            List of assembly arrangement information for the BVR or arrangement qualified overrides.
            This input is not required.
            """

class CreateOrUpdateAbsoluteStructurePref3:
    """
    Preference structure for createOrUpdateAbsoluteStructure.
    """
    def __init__(self, ) -> None: ...
    OverwriteForLastModDate: bool
    """
            Flag to check whether the BOM view revision will be updated if the input last modified
            date is different from the current last modified date of the object in Teamcenter.
            If false, but the CreateOrUpdateAbsoluteStructureInfo3
lastModifiedOfBVR input specified is different
            than the set modified date, partial error 215033 will be returned.
            """
    OverridesToSynchronize: list[str]
    """
            The attributes that the client is synchronizing when the complete
            flag is true. These are the attribute names that the client is interested in. Any
            override properties not in this list will not be deleted when complete is true.
            """
    RelationFilters: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.RelationAndTypesFilter]
    """
            The relation overrides that the client is synchronizing when the complete flag is true.  For instance if a relation filter of IMAN_reference
            relation name and DirectModel relationTypeName is specified and an override of type is in the
            existing structure but not specified in the input, then it will be deleted.
            """
    CadOccIdAttrName: str
    """
            Identifies the BOM line attribute that is used to identify relative occurrences to
            update.
            """

class CreateOrUpdateAbsoluteStructureResponse2:
    """
    
            The response from the createOrUpdateAbsoluteStructure
            operation.
            
    """
    def __init__(self, ) -> None: ...
    AbsOccOutput: System.Collections.Hashtable
    """
            Map of input clientId to the created, updated
            or found absolute occurrence.
            """
    AsmArrangementOutput: System.Collections.Hashtable
    """
            Map of input clientId to the created or updated
            assembly arrangement.
            """
    FormOutput: System.Collections.Hashtable
    """Map of input client id to the created form."""
    DatasetOutput: list[DatasetOutput]
    """Information for the created or updated dataset."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData.  This operation will populate
            the ServiceData with created or updated occurrences,
            arrangements, datasets or forms. Created forms are added as plain objects.
            """

class CreateOrUpdateRelativeStructureInfo3:
    """
    
            Contains lastModifiedOfBVR,a parent ItemRevision object, list of type RelativeStructureChildInfo
            and a  boolean value to specify BVR precision.
            
    """
    def __init__(self, ) -> None: ...
    LastModifiedOfBVR: System.DateTime
    """
            Last Modified Date of BVR.  Used for comparison with current last modified date for
            overwrite determination.
            """
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """
            Object reference of the context assembly for create or update of the child occurrence,
            required input reference.
            """
    ChildInfo: list[RelativeStructureChildInfo2]
    """List of type RelativeStructureChildInfo"""
    Precise: bool
    """Flag for updating the BVR to precise(true)/imprecise(false)"""

class CreateOrUpdateRelativeStructurePref3:
    """
    
            Contains overwriteForLastModDate, continueOnError,cadOccIdAttrName and a list of
            object types.
            
    """
    def __init__(self, ) -> None: ...
    OverwriteForLastModDate: bool
    """
            Flag to check whether BVR needs to be modified, if input last modified date is different
            from actual.
            """
    ContinueOnError: bool
    """Flag to continue with process on encountering error."""
    CadOccIdAttrName: str
    """
            String representing the occurrence note type which holds the value for the CAD occurrence
            id or PSOccurrenceThread uid
            """
    ObjectTypes: list[str]
    """
            List of object types that the client is interested in, such that if the overall structure
            in Teamcenter contains object types or subtypes not in this list, that structure
            will not be deleted if this operation is complete.
            """

class CreateVariantRulesInfo:
    """
    
            Contains the input for creating a new VariantRule object and to be associated
            with a ItemRevision object.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """Identifier that helps the client to track the object(s) created."""
    VruleName: str
    """Refers to VariantRule object name."""
    VruleDescription: str
    """Refers to VariantRule object description."""
    Rev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            The ItemRevision object on which the VariantRule object to be created
            and attached.
            """
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """
            The parent object tag to which the VariantRule object is associated. This
            is optional and if NULL, VariantRule object will be associated with ItemRevision
            object.
            """
    Relation: str
    """
            The relation used to associate the VariantRule object to ItemRevision
            object or parent.
            """
    Options: list[OptionsInfo]
    """
            Refers to a list of OptionsInfo struct, which
            has the classic variant option details.
            """

class CreateVariantRulesResponse:
    """
    
            This contains response for createVariantRules
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the service and error information if any.
            """
    Output: list[VariantRulesOutput]
    """
            Refers to a list of VariantRulesOutput struct
            objects, which in turn refers to newly created VariantRule objects.
            """

class DatasetFileInfo:
    """
    
            Contains clientId, fileName, namedReferencedName, boolean flags isText, allowReplace,
            and boundingBoxesAvailable as well as list of BoundingBoxes.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller.  This ID is used to identify return data
            elements and partial errors associated with this input structure.  If clientId is not provided then it can be difficult to align the
            input with any returned errors.
            """
    FileName: str
    """
            The name of file to be uploaded.  Only the file name should be specified; the path
            should not be included.
            """
    NamedReferencedName: str
    """The name of the reference to use from the dataset to this file.  This input is required."""
    IsText: bool
    """Flag that if true signifies the file is a text file."""
    AllowReplace: bool
    """Flag that if true signifies the file can be overwritten."""
    BoundingBoxesAvailable: bool
    """Flag that if true signifies bounding box information is available."""
    BoundingBoxes: list[BoundingBox]
    """List of bounding boxes, which hold the bounding box coordinate information."""

class DatasetFileTicketInfo:
    """
    Contains basic information for a file to be uploaded to a dataset.
    """
    def __init__(self, ) -> None: ...
    DatasetFileInfo: DatasetFileInfo
    """Member of type DatasetFileInfo."""
    Ticket: str
    """FMS ticket to use in file upload."""

class DatasetOutput:
    """
    Created or updated dataset and file upload information.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller.  This ID is used to identify return data
            elements and partial errors associated with this input structure.  If clientId is not provided then it can be difficult to align the
            input with any returned errors.
            """
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """The dataset object reference of the created or updated dataset."""
    CommitInfo: list[CommitDatasetFileInfo]
    """Information for a file to be uploaded to a dataset."""

class DeleteRelativeStructureInfo3:
    """
    Information to delete relative structures.
    """
    def __init__(self, ) -> None: ...
    LastModifiedOfBVR: System.DateTime
    """
            Last modified date of BOM view revision under the input parent.  This input is not required.  If this input date is different
            than the current last modified date and the overwriteForLastModDate
            input preference is false the input will be ignored and processing will continue
            with the next input.  In this scenario, error 215033 will be returned.  If the dates
            are different and the overwriteForLastModDate
            input preference is true, processing will continue with the current input and the
            BVR will be modified.  In this scenario, error 215034 will be returned.
            """
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """
            The item revision context assembly from which the child occurrences are to
            be removed.  This is a required input.  An error will be returned if a valid parent
            is not specified.
            """
    ChildInfo: list[str]
    """
            List of identifiers of the relative occurrences to be deleted. This is the CAD occurrence
            ID or PSOccurrenceThread UID that uniquely identifies the occurrence under
            a particular context item revision.
            """

class ExpandPSAllLevelsInfo:
    """
    Contains parentBomLines & excludeFilter.
    """
    def __init__(self, ) -> None: ...
    ParentBomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """List of parent bom lines that needs to be expanded"""
    ExcludeFilter: str
    """
            Filter to exclude the type of BOMLines. Valid values are: None2 -- Returns all information
            about the structure. ExcludeOverridden2 -- Excludes structure or property values
            that are removed by AbsOccs substitution. ExcludeICHistory2 -- Excludes structure
            (or property values) that are configured out by ICs. ExcludeGDEs2 -- Excludes lines
            that are GDEOccurrences. ExcludeImanItemLines2 -- Excludes any lines that are ImanItemLines.
            """

class ExpandPSParentData:
    """
    
            Through this structure, the parent bom line , the object of the bom line and the
            objects attached to the bom line object are returned.
            
    """
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """BOMline object reference of the parent"""
    ObjectOfBOMLine: Teamcenter.Soa.Client.Model.ModelObject
    """Object that the parent represents"""
    ParentRelatedObjects: list[ExpandPSRelatedObjectInfo]
    """List of object references attached to parent with given relation"""

class ExpandPSAllLevelsOutput:
    """
    
            Structure containing ExpandPSParentData2 corresponding to the parent and a list of
            ExpandPSData of the children
            
    """
    def __init__(self, ) -> None: ...
    Parent: ExpandPSParentData
    """ExpandPSParentData member"""
    Children: list[ExpandPSData]
    """List of ExpandPSData children found for this parent."""

class ExpandPSAllLevelsPref:
    """
    
            More than one filtering criteria can be specified using this which is nothing but
            a list of  RelationAndTypesFilter
            
    """
    def __init__(self, ) -> None: ...
    ExpItemRev: bool
    """Flag to check for expanding the item revision further"""
    Info: list[RelationAndTypesFilter]
    """
            List of the relation name and the types of objects of the given relation to return
            along with the children
            """
    IncludeOccurrenceTypes: list[str]
    """
            List of Occurrence Types that needs to be included when the expansion of the BOM
            takes place.
            """
    ExcludeOccurrenceTypes: list[str]
    """
            List of Occurrence Types that needs to be excluded when the expansion of the BOM
            takes place.
            """

class ExpandPSAllLevelsResponse2:
    """
    A list of ExpandPSAllLevelsOutput2 so that a set of parent BOMLines can be expanded.
    """
    def __init__(self, ) -> None: ...
    Output: list[ExpandPSAllLevelsOutput]
    """List of ExpandPSAllLevelsOutput1 which contains ExpandPSParentData and list of ExpandPSData"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the Service, plain objects, and error information. For this service, all objects
            are returned to the plain objects group. Error information will also be returned
            mapped to input object.
            """

class ExpandPSData:
    """
    
            Through this structure, the child bom line , the object of the bom line and the object
            attached to the bom line object are returned.
            
    """
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """BOMline object reference of the children"""
    ObjectOfBOMLine: Teamcenter.Soa.Client.Model.ModelObject
    """Object that the child represents"""
    RelatedObjects: list[ExpandPSRelatedObjectInfo]
    """List of objects attached to children with given relation"""

class ExpandPSNamedReferenceInfo:
    """
    
            This structure is used to identify the reference object corresponding to the named
            reference.
            
    """
    def __init__(self, ) -> None: ...
    NamedReferenceType: str
    """type of reference object."""
    NamedReferenceName: str
    """name of reference object."""
    ReferenceObject: Teamcenter.Soa.Client.Model.ModelObject
    """Object reference corresponding to the named reference."""
    FileTicket: str
    """FMS ticket used to retrieve the file in cases where referenceObject is a file."""

class ExpandPSOneLevelInfo:
    """
    Contains the parent BOM lines whose children are to be expanded.
    """
    def __init__(self, ) -> None: ...
    ParentBomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """List of parent BOM lines to be expanded."""
    ExcludeFilter: str
    """
            A filter used to identify the type of BOM lines to exclude. Valid values are: None2
            -- Returns all information about the structure. ExcludeOverridden2 -- Excludes structure
            or property values that are removed by AbsOccs subsititution. ExcludeICHistory2 --
            Excludes structure that are configured out by ICs. ExcludeGDEs2 -- Excludes lines
            that are GDEOccurrences. ExcludeImanItemLines2 -- Excludes lines that are ImanItemLines.
            """

class ExpandPSOneLevelOutput:
    """
    
            Used to return a parent bomline and its related data, and a list of bomlines and
            related data that share that parent.
            
    """
    def __init__(self, ) -> None: ...
    Parent: ExpandPSParentData
    """parent data member"""
    Children: list[ExpandPSData]
    """list of children returned for the parent"""

class ExpandPSOneLevelPref:
    """
    
            Contains a list of filtering criteria (RelationAndTypesFilter) used in a product
            structure expand operation.
            
    """
    def __init__(self, ) -> None: ...
    ExpItemRev: bool
    """Flag indicating whether to return related object(s)."""
    Info: list[RelationAndTypesFilter]
    """
            List of the relation name and the related object types to return along with the children.
            If no RelationAndTypesFilter is supplied (info is empty), and expItemRev is true,
            then all related object types are to be accepted.
            """
    IncludeOccurrenceTypes: list[str]
    """
            List of Occurrence Types that needs to be included when the expansion of the BOM
            takes place.
            """
    ExcludeOccurrenceTypes: list[str]
    """
            List of Occurrence Types that needs to be excluded when the expansion of the BOM
            takes place.
            """

class ExpandPSOneLevelResponse2:
    """
    Is the response object returned in a product structure one level expand operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[ExpandPSOneLevelOutput]
    """List of ExpandPSOneLevelOutput structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the Service, plain objects, and error information. For this service, all objects
            are returned to the plain objects group. Error information will also be returned.
            """

class ExpandPSRelatedObjectInfo:
    """
    This structure associates a related object, named references and reference objects.
    """
    def __init__(self, ) -> None: ...
    RelatedObject: Teamcenter.Soa.Client.Model.ModelObject
    """The resulting related object by following a relation specified in the ExpandPSOneLevelPref"""
    NamedRefList: list[ExpandPSNamedReferenceInfo]
    """List of named reference and reference object of relatedObject."""

class GetAbsoluteStructureDataResponse:
    """
    Contains list of overrides and serviceData.
    """
    def __init__(self, ) -> None: ...
    Overrides: list[AbsOccStructureDataInfo]
    """List of overrides"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains populated plain object list and partial errors."""

class NamedReferenceObjectInfo:
    """
    Contains clientId, Object reference, namedReferenceName, typeName and dataNameValuePairs.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique identifier to track the related object."""
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """Object reference of the object for update, null for create"""
    NamedReferenceName: str
    """
            The Named Reference from the dataset to this object, required. NamedReference values
            are defined for each Dataset type. The customer can add more values as needed. To
            get a current list of valid Named Reference values the programmer can either use
            BMIDE or can call the SOA Core service getDatasetTypeIno.
            """
    TypeName: str
    """Type of the object to be created. Required for object creation only."""
    DataNameValuePairs: list[NameValueStruct]
    """List of NameValueStruct."""

class NameValueStruct:
    """
    Contains name and list of value strings.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Attribute name to set"""
    Values: list[str]
    """Attribute value to set"""

class OptionsInfo:
    """
    This contains classic variant option information.
    """
    def __init__(self, ) -> None: ...
    OptionName: str
    """Refers to classic variant option name."""
    OptionValue: str
    """Refers to classic variant option value."""
    AssocRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            Refers to the ItemRevision object on which the classic variant options are
            defined.
            """

class ReconfigureBOMWindowsInfo:
    """
    
            This contains the list of BOMWindow objects and corresponding corresponding
            RevisionRule object and VariantRule object or StoredOptionSet
            object information.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """Used to track the object(s) created"""
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """The BOMWindow object which needs to be reconfigured."""
    ObjectForConfigure: Teamcenter.Soa.Client.Model.ModelObject
    """Refers to an VariantRule object or StoredOptionSet object information."""
    RevRuleConfigInfo: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.RevisionRuleConfigInfo
    """
            Refers to an RevisionRuleConfigInfo struct
            object.
            """

class ReconfigureBOMWindowsOutput:
    """
    Contains updated BOMWindow along with the corresponding clientIds.
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """clientID"""
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """The reconfigured BOMWindow"""

class ReconfigureBOMWindowsResponse:
    """
    
            This contains the response for the reconfigureBOMWindows
            operation.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[ReconfigureBOMWindowsOutput]
    """
            This contains list of ReconfigureBOMWindowsOutput
            struct object, which returns the BOMWindow which has updated configuration.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the service and error information if any.
            """

class RelatedObjectTypeAndNamedRefs:
    """
    
            This structure contains a related object type and the list of its named references
            to be processed.
            
    """
    def __init__(self, ) -> None: ...
    ObjectTypeName: str
    """objectTypeName"""
    NamedReferenceNames: list[str]
    """namedReferenceNames"""

class RelationAndTypesFilter:
    """
    
            This structure contains a relation name and a list of related object types and its
            named references (RelatedObjectTypeAndNamedReferences).  Together they are used to
            filter objects passed back in a product structure expand operation.
            
    """
    def __init__(self, ) -> None: ...
    RelationName: str
    """Relation name."""
    RelatedObjAndNamedRefs: list[RelatedObjectTypeAndNamedRefs]
    """List of related object types and named references."""
    NamedRefHandler: str
    """
            An enumeration used to identify how named references will be processed. Valid values
            are: NoNamedRefs -- No named references are to be processed. The input RelatedObjectTypeAndNamedRefs
            will be ignored. AllNamedRefs -- All named references are to be processed. The input
            RelatedObjectTypeAndNamedRefs will be ignored. UseNamedRefsList -- Only the named
            references listed in the input RelatedObjectTypeAndNamedRefs struct are processed.
            PreferredJT -- Specialized code for selecting which named references to process is
            executed. This is intended for selecting the most appropriate JT files for visualization
            purposes. If related object is a DirectModel, RelatedObjectTypeAndNamedReferences
            contents will be ignored and only the preferred JT is returned. If related object
            is not Direct Model, named reference expansion will proceed as though namedRefHandler
            is UseNamedRefsList.
            """

class RelativeStructureChildInfo2:
    """
    Contains information about the child structure.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller.  This ID is used to identify return data
            elements and partial errors associated with this input structure.  If clientId is not provided then it can be difficult to align the
            input with the output or any returned errors.
            """
    CadOccId: str
    """
            The CAD occurrence ID or PSOccurrenceThread UID is used to uniquely identify
            the occurrence under a particular context item revision or General Design Element
            (GDE) for update.  The cadOccId can be null
            for create.  A valid cadOccId must be passed
            when this operation is called with the RelativeStructureParentInfo
complete input set to true. If a valid cadOccId is not supplied when complete is set to true, this operation creates a new occurrence
            and any data associated against an existing occurrence is removed/lost.  This parameter
            depends on the CreateOrUpdateRelativeStructurePref
cadOccIdAttrName preference for finding the
            existing BOM line.
            """
    Child: Teamcenter.Soa.Client.Model.ModelObject
    """
            The child object for the occurrence creation.  Only item revision and General Design
            Element (GDE) are supported.  If the child occurrence exists, but the input child
            object is different than the existing child object, the existing child will be replaced
            by the input child.  Existing children are found referencing the occurrence found
            by the cadOccId input.
            """
    OccInfo: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.RelOccInfo
    """The property information for this occurrence."""

class SaveBOMWindowsResponse:
    """
    Contains the response for the saveBOMWindows operation.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Any failures will be returned in the ServiceData list of partial errors."""

class VariantRulesOutput:
    """
    
            This contains output data for createVariantRules
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the object(s) created."""
    Vrule: Teamcenter.Soa.Client.Model.Strong.VariantRule
    """Refers to newly created VariantRule object."""

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateAbsoluteStructure(self, AbsOccInfos: list[CreateOrUpdateAbsoluteStructureInfo3], BomViewTypeName: str, Complete: bool, Pref: CreateOrUpdateAbsoluteStructurePref3) -> CreateOrUpdateAbsoluteStructureResponse2:
        """    
             This operation creates or updates absolute occurrences on an existing relative structure.
             The structure will be configured with revision rule set in the preference TC_config_rule_name
             before any configuration changes are applied. The objects created or updated can
             include an absolute occurrence, assembly arrangement and datasets and are added to
             the ServiceData as created or updated objects.  Created forms are added as plain
             objects and updated forms are added as updated objects.
             

             Before creating the absolute occurrence or assembly arrangement, this operation will
             check whether either already exists.  If the occurrence or arrangement exists but
             the input attribute values differ from those already set, an attempt is made to update
             the values.
             
             This operation assumes the input is in a bottom up format such that if any failures
             occur, the structure that is updated will still be consumable.  For example:
             

             Parent assembly A and occurrence C are input into this operation along with subassembly
             B and occurrence D.  If occurrence D is updated successfully on subassembly B but
             an error occurs during the update of occurrence C on assembly A, the client can still
             access subassembly B.
             

             For objects of type dataset and form, this operation can create or update a new object
             instance and attach it as an override on the absolute occurrence.  For all object
             types, existing objects can be attached or removed as an override on the absolute
             occurrence.
             

             To help reduce the client overhead of sending all override information during a complete
             synchronization and avoid accidental removal of overrides coming from other clients,
             this operation allows the client to provide only the attributes it is interested
             in syncing when the complete flag is set to true.  For more information on complete
             synchronization, see the description for the complete input parameter.
             

             One parent context object is processed at a time and it is assumed that all edits
             for a given parent context come in as one set of input.
             

Use Cases:

             Use case 1:
             

             User adds an override to an existing assembly to create an absolute occurrence.
             

             For this operation, the assembly is passed in as the contextItemRev
             and the override, such as new transformation data to position a component in an assembly,
             is passed in as the absolute occurrence.  The absolute occurrence is created and
             a map of the input clientID to AbsOccurrence
             is returned in absOccOutput and the occurrence
             is returned as created objects in ServiceData.
             

             Use case 2:
             

             User adds an override with a new dataset to an existing assembly to create an absolute
             occurrence with an attached dataset.
             

             For this operation, the assembly is passed in as the contextItemRev
             and the override with information for the new dataset is passed in as the absolute
             occurrence information.  The absolute occurrence and new dataset are created and
             a map of the input clientID to AbsOccurrence
             is returned in absOccOutput and the created
             dataset is returned in datasetOutput.  The
             occurrence and dataset are returned as created objects in ServiceData.
             


Dependencies:

             createOrUpdateParts, createOrUpdateRelativeStructure
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param AbsOccInfos: 
                         List of information related to the absolute occurrences that need to be created or
                         updated.
             
        :param BomViewTypeName: 
                         The BOM view (BV) type used to find the existing BOM view.
             
        :param Complete: 
                         Flag that if true signifies that the absolute occurrences represented in <font face="courier" height="10">absOccInfos</font> are the full representation of all the overrides under
                         the input <font face="courier" height="10">contextItemRev</font>. Any other overrides
                         that exist in Teamcenter but are not represented in the input will be removed.  This
                         may also be referred to a complete sync of the occurrence.
             
        :param Pref: 
                         The structure for setting specific preference input used by this operation.
             
        :return: 
        """
        ...
    def CreateOrUpdateRelativeStructure(self, Inputs: list[CreateOrUpdateRelativeStructureInfo3], BomViewTypeName: str, Complete: bool, Pref: CreateOrUpdateRelativeStructurePref3) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateRelativeStructureResponse:
        """    
             This is the overloaded function for Cad::_2007_12::StructureManagement::createOrUpdateRelativeStructure.
             It differs by allowing the parent member of the structure CreateOrUpdateRelativeStructureInfo
             to be a ModelObject instead of a strongly typed Item Revision object and makes the
             child member of the RelativeStructureChildInfo to a ModelObject instead of strongly
             typed Item Revision. This is to allow structures with GDE elements to be edited with
             this service. Create or update the relative structure objects and relations for the
             input model. The service first attempts to check for the presence of duplicate context
             objects and then validate the existence of the structure to be created. If any of
             the objects exist but the input attribute values that differ from those already set,
             an attempt is made to update the values if possible. This service assumes the input
             is in a bottom-up format such that if any failures occur, the structure that is created
             will be consistent. No attempt is made in the service to rearrange the input and
             process it in the correct order. As we process one parent context object at one time,
             it is assumed that all edits for a given parent context come in as one set of input.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Inputs: 
                         List of input structures that defines all the occurrence for a given parent
             
        :param BomViewTypeName: 
                         Type of BOMView to create
             
        :param Complete: 
                         Flag that if true signifies that the structure represented in the input is the full
                         representation of the structure under the input parent. Any other structure relations
                         that exist in Teamcenter but are not represented here will be removed.
             
        :param Pref: 
                         Preference structure specific for this service
             
        :return: Output is an explicit response consisting of a map of input clientId string to created
             or updated or found occurrence thread reference.
        """
        ...
    def DeleteRelativeStructure(self, Inputs: list[DeleteRelativeStructureInfo3], BomViewTypeName: str, Pref: Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.DeleteRelativeStructurePref2) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteRelativeStructureResponse:
        """    
             This operation deletes one or more first level children of a parent assembly.  The
             children, or occurrences, to be deleted are specified by the CAD occurrence ID or
             PSOccurrenceThread UID.  The last modified date of the BOM view revision (BVR)
             can also be specified for comparison against the last modified date in Teamcenter
             to ensure the occurrence has not changed outside of this client context and control
             if the BVR is actually modified and the occurrence deleted by this operation.
             

Use Cases:

             User deletes an existing relative occurrence from an existing assembly.
             

             For this operation, the assembly is passed in as the parent and the occurrence ID
             is passed in as the child information.  The relative occurrence is removed from the
             parent assembly and the ID of the deleted occurrence is added to the ServiceData
             list of deleted objects.
             

Dependencies:

             createOrUpdateRelativeStructure
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Inputs: 
                         List of input structures that specify the parent and first level children to be deleted.
             
        :param BomViewTypeName: 
                         The BOM view<b> </b>(BV) type used to find the existing BOM view.
             
        :param Pref: 
                         The structure for setting specific preference input used by this operation.
             
        :return: 
        """
        ...
    def ExpandPSAllLevels(self, Info: ExpandPSAllLevelsInfo, Pref: ExpandPSAllLevelsPref) -> ExpandPSAllLevelsResponse2:
        """    
             This is the overloaded function for Cad::_2007_01::StructureManagement::expandPSAllLevels.
             The member itemRevOfBOMLine of ExpandPSData and ExpandPSParentData is renamed as
             objectOfBOMLine and its type is changed from Item Revision to ModelObject. Also the
             datasets and parentDatasets member of ExpandPSData and ExpandPSParentData structures
             respectively are renamed to relatedObjects and type changed to ModelObject instead
             of Dataset. This is to support structures with GDE elements to be returned from the
             expansion. Finds the children at all levels given parent BOMLines. Also if required
             gets the objects of given type and relation that are attached to the parent and children.
             In addition to the above, the expansion of the Product Structure can be filtered
             for a given occurrence type/s which can be included and/or excluded from the expansion.
             In addition to the above the following additional functionality has been added: 1.
             The operation is not limited to return related objects of dataset type only.  Expansion
             of attached objects to the BOM line object is determined by a filtering mechanism
             where the criteria is set by: relation name, related object type, and named references.
             2.  This operation allows for expansion to reference object associated to a named
             reference.  Typically this is a file.  An FMS ticket will be returned to provide
             access to this file. 3.  Where a named reference points to a file, this operation
             allows for specific logic in choosing which files are returned.  This is determined
             by the input parameter NamedRefHandler (included in the info object).
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Info: 
                         Input of ExpandPSAllLevelsInfo which contains parent bom lines and a filter of the
                         type of bom lines to exclude.
             
        :param Pref: 
                         of a ExpandPSAllLevelsPref which contains a list of relation name and the types of
                         objects of the given relation to return along with the children.
             
        :return: list of ExpandPSData which contains parent BOMLines, chilrens and object of given
             type and relation attached to them. All objects found are added to the ServiceData
             list of plain objects. Objects that fail the expansion are returned in the list of
             partial errors in the ServiceData
        """
        ...
    def ExpandPSOneLevel(self, Info: ExpandPSOneLevelInfo, Pref: ExpandPSOneLevelPref) -> ExpandPSOneLevelResponse2:
        """    
             This operation will expand one level of a product structure and return the resulting
             BOM lines. If required, it will return objects of a given relation and type that
             are attached to the parent and child BOM lines. Additionally, if specified in the
             preference, this will return only BOM Lines of a given particular occurrence type
             and exclude occurrence types of a given type. This operation differs from the operation
             Teamcenter.Soa.Cad._2007_01.StructureManagement.expandPSOneLevel in the following
             ways: 1.  The operation is not limited to return related objects of dataset type
             only.  Expansion of attached objects to the BOM line object is determined by a filtering
             mechanism where the criteria is set by: relation name, related object type, and named
             references. 2.  This operation allows for expansion to reference object associated
             to a named reference.  Typically this is a file.  An FMS ticket will be returned
             to provide access to this file. 3.  Where a named reference points to a file, this
             operation allows for specific logic in choosing which files are returned.  This is
             determined by the input parameter NamedRefHandler (included in the info object).
             4.  The resulting Product Structure expansion can be limited to a certain Occurrence
             Types.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Info: 
                         The list of parent BOM lines to expand, a filter that describes what child BOM lines
                         are excluded in the expansion, and a filter that describes what named references
                         are included in the expansion.
             
        :param Pref: 
                         A flag for expanding BOM line object further and a list describing the relation name,
                         related object type and named references that help define the expansion criteria.
                         Also, this preference can accommodate  a list of occurrence types to include and
                         exclude BOM Lines from the Product Structure expansion.
             
        :return: The response contains a structure of parent BOM line and its related data, and a
             list of child BOM lines and related data. All objects found are added to the ServiceData
             list of plain objects. Objects that fail the expansion are returned in the list of
             partial errors in the ServiceData.
        """
        ...
    def GetAbsoluteStructureData(self, AbsOccDataQualInfos: list[AbsOccQualifierInfo], AbsOccDataPref: AbsOccDataPref) -> GetAbsoluteStructureDataResponse:
        """    
             This operation retrieves the absolute occurrence override information for the given
             qualifier. The input accepts the relation override that needs to be expanded. In
             case of finding the overrides based on the used arrangement within the structure,
             the client is expected to provide bvr of sub assembly in the input. ParentBVR |--(Arr1)
             |--(Arr2) | |________childBVR1 |           |-----(Arr3) |           |-----(Arr4)
             |           |_____________childBVR2 |                                    |----(Arr5)
             |                                    |----(Arr6) |_____ childBVR2 |----(Arr5) |----(Arr6)
             If Arr1 uses Arr3 which in turn uses Arr5, to determine the overrides by Arr3 and
             Arr5 qualifier the client is expected to send childbvr1 and childbvr2 as inputs along
             with the parentBVR.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param AbsOccDataQualInfos: 
                         List of qualifying information for overrides
             
        :param AbsOccDataPref: 
                         Preference on which relation overrides to expand and the preferred objects of type
                         to return
             
        :return: Contains the  overrides and service data information.
        """
        ...
    def CreateVariantRules(self, Input: list[CreateVariantRulesInfo]) -> CreateVariantRulesResponse:
        """    
             This operation creates the saved VariantRule objects for classic variant options.
             

Use Cases:

             This operation is used to create VariantRule object and save them, which can
             be used later for BOM variant configuration.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param Input: 
                         This has the list of <font face="courier" height="10">CreateVariantRulesInfo</font>
                         struct, which are used to create a new <b>VariantRule</b> object.
             
        :return: 
        """
        ...
    def ReconfigureBOMWindows(self, Info: list[ReconfigureBOMWindowsInfo]) -> ReconfigureBOMWindowsResponse:
        """    
             This operation takes a list of BOMWindow objects and updates the contents
             of the windows (i.e. configuration) by applying the supplied RevisionRule
             and variant configuration information.  If the RevisionRuleEntryProps::unitNo is set to -1 then it considers default unitNo
             or use the input RevisionRule object with no changes. If no value specified
             for RevisionRuleEntryProps::unitNo, then the input RevisionRule object used as modified/transient
             rule with unitNo as 0. If the value of preference PSM_enable_product_configurator
             is set to true, then Product Configurator variant rule will be honored.
             

Use Cases:

             This operation is used to reconfigure the BOMWindow with new or modified RevisionRule
             and VariantRule information.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param Info: 
                         This contains a list of <font face="courier" height="10">ReconfigureBOMWindowsInfo</font>
                         struct objects which has <b>BOMWindow</b> objects and corresponding <b>RevisionRule</b>
                         object and <b>VariantRule</b> object or <b>StoredOptionSet</b> object information.
             
        :return: 
        """
        ...
    def SaveBOMWindows(self, BomWindows: list[Teamcenter.Soa.Client.Model.Strong.BOMWindow]) -> SaveBOMWindowsResponse:
        """    
             This operation can be used by a client developer to save any modifications made to
             a Teamcenter product structure through its runtime artifacts. A Teamcenter product
             structure is a persistent parent child composition and clients often deal with runtime
             artifacts of this persistent model. The runtime artifacts are primarily represented
             by BOMLine business objects and BOMWindow business objects along with
             the BOMLine properties. Modifications to the product structure are typically
             bulked up on the client and tracked through the BOMWindow. Once it is established
             that changes to a product structure can be saved this operation can be called passing
             in a handle to the BOMWindows that need to be saved.
             

Use Cases:

             In a typical usage of the saveBOMWindows operation, a client developer already has
             a Teamcenter product structure loaded with the runtime artifacts created. This means
             that the client developer has/creates handles to a BOMWindow, and BOMLine
             business objects that are part of that BOMWindow. Given this pre disposition,
             typical interaction with the client may involve addition of a new BOMLine
             or removal of a BOMLine, creation/removal of In Structure associations etc.
             In such cases, the changes to the product structure are tracked on the BOMWindow
             and when the changes are ready to be persisted, the client developer calls the saveBOMWindows
             operation.
             


Dependencies:

             createOrUpdateRelativeStructure
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param BomWindows: 
                         References to the <b>BOMWindow</b> business objects that need to be saved after structure
                         modifications.
             
        :return: 
        """
        ...

