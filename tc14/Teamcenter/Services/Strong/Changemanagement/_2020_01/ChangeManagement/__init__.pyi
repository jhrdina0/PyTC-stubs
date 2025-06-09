import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class DeepCopyData:
    """
    
            DeepCopyData stores the deep copy information that will be copied via derive operation.
            It also stores the nested deep copy data at the next level.
            
    """
    def __init__(self, ) -> None: ...
    AttachedObject: Teamcenter.Soa.Client.Model.ModelObject
    """The related object to be deep copied."""
    DeepCopyProperties: System.Collections.Hashtable
    """deepCopyProperties."""
    OperationInputType: str
    """Object type name of the operation being perfomed."""
    ChildDeepCopyData: list[DeepCopyData]
    """
            A list of DeepCopyData for the objects of the relation or reference property objects
            of the attached object.
            """
    InputProperties: System.Collections.Hashtable
    """
            Map to provide input property names and values of attached object. These property
            values will be applied on propagated objects. Map of property name(key) and property
            values(values) (string, list of strings) in string format of attached object, to
            be set on copied object of attached object. The calling client is responsible for
            converting the different property types (int, float, date .etc) to a string using
            the appropriate toXXXString functions in the SOA client framework Property class.
            """

class DerivePropertyValueInput:
    """
    
            This map is of property name (as key) and a vector of property values input, business
            object in string format, property name values map and compund derive input. The business
            object is a simple string. The property name values is a list of strings to support
            both single valued and multi valued properties of types. The calling client is responsible
            for converting the different property types (like integer, double, date, etc) to
            a string using the appropriate to< type >String function (e.g. toIntString
            and toDateString) in the client framework's Property class. The compound derive input
            is another type of def of property value input data structure.
            
    """
    def __init__(self, ) -> None: ...
    BoName: str
    """The buisness object name to which the properties belong."""
    PropertyNameValues: System.Collections.Hashtable
    """Map of property name values."""
    CompoundDeriveInput: System.Collections.Hashtable
    """Vector of derive property value input."""

class DeriveInput:
    """
    
            Structure that contains multiple Change Items object to be derived, a structure containing
            property name and values to be propagated,  Deep Copy Data, a flag to automatically
            submit to workflow or not, a workflow template name and a flag to propagate relations
            or not.
            
    """
    def __init__(self, ) -> None: ...
    SelectedObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of Problem Report or Change Request objects to be derived."""
    DerivePropertyData: DerivePropertyValueInput
    """
            A map of property name (as key) and property values (as value) in string format.
            Each value is a list of strings to support both single valued and multi valued properties
            of types. The calling client is responsible for converting the different property
            types (like integer, double, date, etc) to a string using the appropriate to<
            type >String function (e.g. toIntString and toDateString) in the client framework's
            Property class.
            """
    DeepCopyDatas: list[DeepCopyData]
    """A list of DeepCopyData to be propagated to the derived Change Item objects."""
    SubmitToWorkflow: bool
    """
            This is used to indicate whether the derived Change Item object will be automatically
            submitted to Workflow. If true will submit the derived object to designated workflow
            template, otherwise the derived object will not be submitted to workflow.
            """
    WorkflowTemplateName: str
    """
            The workflow template name to be executed, if not informed, the default workflow
            template will be used.
            """
    PropagateRelation: bool
    """
            If TRUE will propagate the relation defined in Deep Copy Rule, if FALSE will not
            propagate the relations.
            """

class ChangeManagement:
    """
    Interface ChangeManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def DeriveChangeItems(self, DeriveInput: DeriveInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...

