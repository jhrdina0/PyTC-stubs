import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class SaveAsInput:
    """
    This structure is used to capture the inputs required for savingof a business object.
    """
    def __init__(self, ) -> None: ...
    BoName: str
    """Business object type name"""
    StringProps: System.Collections.Hashtable
    """
            Map of string property names to values (string,
            string)
            """
    StringArrayProps: System.Collections.Hashtable
    """
            Map of string array property names to values (string,
            vector<string>)
            """
    DoubleProps: System.Collections.Hashtable
    """
            Map of double property names to values (string,
            double)
            """
    DoubleArrayProps: System.Collections.Hashtable
    """
            Map of double array property names to values (string,
            vector<double>)
            """
    FloatProps: System.Collections.Hashtable
    """Map of float property names to values (string, float)"""
    FloatArrayProps: System.Collections.Hashtable
    """
            Map of float array property names to values (string,
            vector<float>)
            """
    IntProps: System.Collections.Hashtable
    """Map of int property names to values (string, int)"""
    IntArrayProps: System.Collections.Hashtable
    """
            Map of int array property names to values (string,
            vector<int>)
            """
    BoolProps: System.Collections.Hashtable
    """
            Map of boolean property names to values (string,
            bool)
            """
    BoolArrayProps: System.Collections.Hashtable
    """
            Map of boolean array property names to values (string,
            vector<bool>)
            """
    DateProps: System.Collections.Hashtable
    """
            Map of DateTime property names to values (string,
            DateTime)
            """
    DateArrayProps: System.Collections.Hashtable
    """
            Map of DateTime array property names to values (string,
            vector<DateTime>)
            """
    TagProps: System.Collections.Hashtable
    """
            Map of BusinessObject property names to values (string,
            BusinessObject)
            """
    TagArrayProps: System.Collections.Hashtable
    """
            Map of BusinessObject array property names to values (string, vector<BusinessObject>)
            """

class DeepCopyData:
    """
    DeepCopyData definition
    """
    def __init__(self, ) -> None: ...
    AttachedObject: Teamcenter.Soa.Client.Model.ModelObject
    """Other side object"""
    PropertyName: str
    """Name of relation type or reference property for which DeepCopy rule is configured"""
    PropertyType: str
    """
            enumeration value indicating if DeepCopyRule is configured for Relation or Reference
            property
            """
    CopyAction: str
    """DeepCopy action [NoCopy, CopyAsReference, CopyAsObject or Select]"""
    IsTargetPrimary: bool
    """Flag indicating if target object is primary or secondary"""
    IsRequired: bool
    """If this flag is false, the copy action can be dynamicaly changed by user"""
    CopyRelations: bool
    """
            This is a Boolean representing whether the Properties on the Relation if any in the
            Relation that exists between
            """
    SaveAsInputTypeName: str
    """SaveAsInput type name"""
    ChildDeepCopyData: list[DeepCopyData]
    """Vector of DeepCopy data for the secondary objects on the other side"""
    SaveAsInput: SaveAsInput
    """
            SaveAsInput field to capture user inputs on the SaveAs dialog. NOTE: This field is
            unused in the getSaveAsDesc operation. It is used in the saveAsObjects operation
            """

class ObjectInfo:
    """
    
            This structure holds object information of parent object of trace link in Report
            structure.
            
    """
    def __init__(self, ) -> None: ...
    ContextName: str
    """
            This parameter will hold the name of context for source or target object of Trace
            Link.
            """
    DisplayObj: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            If the Trace Link is created on the occurrence then this variable will represent
            the object to show in the Trace Report.
            """
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """
            This object represent any Business Object in Teamcenter on which Trace Link
            is created
            """
    BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView
    """This field represents the BOM View of context line for the Trace Link."""

class Report:
    """
    
            This structure holds information each trace link report with information of parent
            object, and its children associated with trace link relation.
            
    """
    def __init__(self, ) -> None: ...
    Parent: ObjectInfo
    """Parent object of trace link."""
    Children: list[ObjectInfo]
    """list of all child objects for the parent with trace link relation"""

class SaveAsIn:
    """
    
SaveAsIn structure contains the object to
            be saved and the corresponding DeepCopyData
            of the attached objects of the object to be saved.
            
    """
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """Target object being saved as"""
    SaveAsInput: SaveAsInput
    """SaveAsInput (user input from SaveAs dialog) for the targetobject being saved as"""
    DeepCopyDatas: list[DeepCopyData]
    """DeepCopyData of the objects attached to the targetobject"""

class SaveAsObjectsResponse:
    """
    
            This structure contains a vector corresponding to the input target objects that holds
            mapping between the original objects and the saved objects.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[SaveAsOut]
    """SaveAsout vector"""
    SaveAsTrees: list[SaveAsTree]
    """
            List of the input target objects that holds mapping between the original objects
            and the copied  objects.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data containing created objects, errors, etc"""

class SaveAsOut:
    """
    
            This structure contains information for SaveAs
            operation including unique target object.
            
    """
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """BusinessObject name"""
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Input data for SaveAs Operation"""

class SaveAsTree:
    """
    This structure contains tree structure for SaveAs.
    """
    def __init__(self, ) -> None: ...
    OriginalObject: Teamcenter.Soa.Client.Model.ModelObject
    """Original object being saved as"""
    ObjectCopy: Teamcenter.Soa.Client.Model.ModelObject
    """
            Object copy after SaveAs. This could be NULL
            if no copy was made or same as original object if the copy is a reference to the
            original
            """
    ChildSaveAsNodes: list[SaveAsTree]
    """Nested information for next level of the tree"""

class TraceabilityInfoInput:
    """
    
            Information required to generate a trace report, it includes objects for which this
            trace report should be generated, type of trace report, if indirect trace link included,
            and type of base relation of trace link.
            
    """
    def __init__(self, ) -> None: ...
    SelectedObjs: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of objects on which to generate the Trace Report."""
    ReportType: int
    """
            Type of Report that is defining, complying, or both. Below are
            
                            allowed
            values
            
                            1
            for Complying Report
            
                            2
            for Defining Report
            
                            3
            for Complete Report
            """
    ReportDepth: int
    """
            Level to which Trace Report should be generated. The allowed value is any number
            greater than zero.
            """
    IsIndirectTraceReportNeeded: bool
    """
            If this variable is true then only Indirect Trace Report will be
            
            included in the final Trace Report.
            """
    RelationTypeName: str
    """
            The Trace Report will be generated for this type of relations, the type should be
            FND_TraceLink or its subtype.
            """

class TraceabilityReportOutput:
    """
    
            TraceabilityReportOutput structure holds information about generated trace reports
            with defining and complying trace trees with selected objects and its persistent
            objects, including service data.
            
    """
    def __init__(self, ) -> None: ...
    TraceReports: list[TraceReport]
    """
            This member holds all the Trace Reports user has asked for. This is vector of
            
            TraceReport type of structures.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data."""

class TraceReport:
    """
    
            This structure holds information about generated trace reports with defining and
            complying trace trees with selected objects, and its persistent objects.
            
    """
    def __init__(self, ) -> None: ...
    DefiningTree: list[Report]
    """Represents the Defining Tree in the Trace Report giving all defining trace link details."""
    IndirectDefiningTree: list[Report]
    """Represents an Indirect Defining Tree in the Trace  Report."""
    ComplyingTree: list[Report]
    """
            Represents the Complying Tree in the Trace Report giving all complying trace link
            details.
            """
    IndirectComplyingTree: list[Report]
    """Represents an Indirect Complying Tree in the Trace Report"""
    SelectedObject: Teamcenter.Soa.Client.Model.ModelObject
    """Represents selected object for which Trace Report generated."""
    PersistentObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Represents persistent object for the selected object for which Trace Report generated."""

class ValidateRevIdsInfo:
    """
    
            Input structure for validateRevIds operation.
            It contains the revision id to be validated along with information about the object
            and object type.
            
    """
    def __init__(self, ) -> None: ...
    RevId: str
    """Input Revision id to be validated."""
    ItemObject: Teamcenter.Soa.Client.Model.Strong.Item
    """
Item object for which revision id needs to be validated. For new a Item
            to be created this property must be set to null.
            """
    ItemType: str
    """String describing the type of the Item for which the identifier is being validated."""

class ValidateRevIdsOutput:
    """
    
            This structure contains the modified revision id and enum status of the id.  Valid
            values for the enums are Valid (ids are valid), Invalid (ids are not valid), Modified
            (ids are not ideal but can be used if the user really wants them), Override (ids
            are not valid, silently replace with modified ones), and Duplicate (ids are already
            allocated in the system).
            
    """
    def __init__(self, ) -> None: ...
    ModRevId: str
    """Modified rev id if specified by Naming Rules/Revision Naming Rules."""
    RevIdStatus: str
    """
            Status of the revision id represented as a ValidateRevIdsStatus
            enum.
            """

class ValidateRevIdsResponse:
    """
    
            Response structure for validateRevIds service
            operation.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[ValidateRevIdsOutput]
    """
            List of ValidateRevIdsOutput structures,
            which contain the modified revision id and the validation status of the input revision
            id.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard ServiceData structure. It contains
            partial errors and failures along with the clientIds.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ValidateRevIds(self, Inputs: list[ValidateRevIdsInfo]) -> ValidateRevIdsResponse:
        """    
             Validates and/or modifies the Revision Id based on the naming rules/revision naming
             rules and user exit callbacks.
             

Use Cases:

             This operation is generally used to validate revision id before providing it as input
             for create, revise and save-as operations.
             

Teamcenter Component:

             Core Naming Rules - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Naming
             Rules and Revision Naming Rules.
             
        :param Inputs: 
                         A list of <font face="courier" height="10">ValidateRevIdsInfo</font> structures,
                         each of which contain revId/itemObject/itemType that have to be validated.
             
        :return: (This list may be incomplete, and is subject to change without notice.)
        """
        ...
    def SaveAsObjects(self, SaveAsIn: list[SaveAsIn]) -> SaveAsObjectsResponse:
        """    
             This operation is generic operation for saving of Business Objects. It will also
             save any secondary objects that also need to be saved based on deep copy rule information
             

Use Cases:

             Client constructs the SaveAs dialog for a Business Object using OperationDescriptor.getSaveAsDesc operation.  The information
             returned by that operation allows client to construct the SaveAs dialogs and DeepCopy
             panels for user input. Once the user input is received, client can make subsequent
             invocation to this (DataManagement.saveAsObjects)
             operation to execute SaveAs on the object.
             

Dependencies:

             getSaveAsDesc
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param SaveAsIn: 
                         Input data containing target object and DeepCopyData of the attached objects
             
        :return: . The Partial Error includes
             the index of the failed element from the input vector.
        """
        ...
    def GetTraceReport(self, Input: TraceabilityInfoInput) -> TraceabilityReportOutput:
        """    
             This operation will generate a Trace Report on the objects selected by user.  User
             will get information about complying as well as defining objects which are connected
             to selected object using  FND_TraceLink or its subtype of GRM relation.
             

             Trace links can be between following objects:
             

                     1.    Between
             occurrences of an ItemRevision

                     2.    Between
             ItemRevisions

                     3.    Between
             Items

                     4.    Between
             any two WorkspaceObject.
             

             If indirect trace report flag is set to true during this operation, then user
             will get trace report for ItemRevision if selected object is Occurrence,
             and trace report for Items if selected objects is ItemRevision in addition
             to direct trace report for the selected object.
             


Use Cases:

             Suppose user created trace link between Requirement R1 as start point and R2 as end
             point and creates trace link from Requirement R3 as start and R1 as end point.
             
             When user runs traceability report on R1 requirement he will get R2 object as complying
             object and R3 will come as defining object.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Input: 
                         A TraceabilityInfoInput structure to generate a Trace Report.This input structure
                         holds selected objects for which trace report needs to be generated, trace report
                         type, if indirect report required, and base relation type.
             
        :return: TraceabilityReportOutput structure holds vector of trace reports which gives the
             trace tree of defining and complying objects, including indirect tree if isIndirectTraceReportNeeded
             is true, and any failure is return in service data.
        """
        ...

