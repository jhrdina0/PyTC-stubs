import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AdditionalInfo2:
    """
    A structure containg the maps to capture the additional information.
    """
    def __init__(self, ) -> None: ...
    StrToDateVectorMap: System.Collections.Hashtable
    """A map of string to list of dates."""
    StrToDoubleVectorMap: System.Collections.Hashtable
    """A map of string to list if doubles."""
    StrToStrVectorMap: System.Collections.Hashtable
    """A map of string to list if strings."""
    StrToObjVectorMap: System.Collections.Hashtable
    """A map of string to list of business object."""
    StrToIntVectorMap: System.Collections.Hashtable
    """A map of string to list of integers."""

class CopyRecursivelyConfigurationInfo:
    """
    Structure containing configuration information.
    """
    def __init__(self, ) -> None: ...
    RevisionRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """
            The RevisionRule with which the template BOMWindow is configured for
            cloning.
            """
    VariantRules: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of variant rules to configure the BOMWindow for cloning. List can contain
            either StoredOptionSet or VariantRule. Both type of variant rules are
            not supported in the same list. If the list is empty all the SVRs created on the
            BOMWindow are carried over to the new BOMWindow.
            """
    CopySuppressedLines: bool
    """If true, the  suppressed lines are carried to the cloned structure otherwise not."""
    CopyFutureEffectivities: bool
    """If true, the furture effectivites are carried to the cloned structure otherwise not."""
    AdditionalInfo: AdditionalInfo2
    """A generic structure to be used to capture additional information."""

class CopyRecursivelyTemplateInfo:
    """
    Structure with the information about the template and rule to be used for
cloning.
    """
    def __init__(self, ) -> None: ...
    ObjectToClone: Teamcenter.Soa.Client.Model.ModelObject
    """
            The object to be cloned. The valid object types are: Mfg0BvrPart, Mfg0BvrWorkarea,
            Mfg0BvrProcess and Mfg0BvrOperation.
            """
    CloningRule: str
    """The preference name holding the list of caluses to be  used for cloning."""
    ReferenceWindow: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
BOMWindow  from where the objects are referred during cloning. If NULL, the
            objects are referred from the template BOMWindow.
            """
    AdditionalInfo: AdditionalInfo2
    """Structure for additional information. Reserved for future use."""

class CopyRecursivelyNewObjectInfo:
    """
    Structure containing information about the cloned object.
    """
    def __init__(self, ) -> None: ...
    NewName: str
    """The name of cloned BOMLine object."""
    NewDescription: str
    """The description of cloned object."""
    NewId: str
    """Id of cloned BOMLine object."""
    NewrevId: str
    """The revision id of cloned object."""
    PasteTarget: Teamcenter.Soa.Client.Model.ModelObject
    """
            The target BOMLine object under which the cloned object is created. If NULL,
            the cloned object is created as new root in a new BOMWindow object.
            """
    AdditionalInfo: AdditionalInfo2
    """Any additional information.Reserved for future use."""

class CopyRecursivelyInputInfo:
    """
    
Holds information about the original structure to be cloned, BOMWindow
configuration
used to clone the structure and the information for the cloned structure.
    """
    def __init__(self, ) -> None: ...
    TemplateInfo: CopyRecursivelyTemplateInfo
    """Structure with the information about the template and rule to be used for cloning."""
    ConfigurationInfo: CopyRecursivelyConfigurationInfo
    """Structure containing configuration information."""
    NewObjectInfo: CopyRecursivelyNewObjectInfo
    """Structure containing information about the cloned object."""

class CopyRecursivelyResponse:
    """
    
The response is a structure containing the map of template object and the item
revision
of cloned object, a fms file ticket that captures logs.
    """
    def __init__(self, ) -> None: ...
    DataMap: System.Collections.Hashtable
    """
            A Map <BusinessObject, BusinessObject> contains the input object which has
            been cloned as key and the item revision of the cloned object as value.
            """
    LogFileTicket: str
    """The FMS ticket for the transient file that captures the log of cloning operation."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The standard service data."""

class PasteDuplicateInput:
    """
    
A structure containing source BOMLine and target BOMLine as input for
pasteDuplicateStructure operation.
    """
    def __init__(self, ) -> None: ...
    SourceLine: Teamcenter.Soa.Client.Model.ModelObject
    """Source BOMLine to be cloned."""
    TargetLine: Teamcenter.Soa.Client.Model.ModelObject
    """Target BOMLine under which the cloned source BOMLine is to be pasted"""

class PasteDuplicateStructureOutput:
    """
    
A structure containing the target BOMLine, the new child BOMLine created
under this target and the index of corresponding source BOMLine in the input.
    """
    def __init__(self, ) -> None: ...
    SrcLineIndex: int
    """Index of the source BOMLine in the input data."""
    TargetLine: Teamcenter.Soa.Client.Model.ModelObject
    """Target BOMLine under which the new cloned BOMLine is pasted."""
    NewChildLine: Teamcenter.Soa.Client.Model.ModelObject
    """
            New BOMLine which is cloned from the source BOMLine and is pasted under
            the target BOMLine.
            """

class PasteDuplicateStructureResponse:
    """
    Response for pasteDuplicateStructure operation.
    """
    def __init__(self, ) -> None: ...
    PasteDuplicateOutput: list[PasteDuplicateStructureOutput]
    """
            The target BOMLine, the new child BOMLine created under this target
            and the index of corresponding source BOMLine in the input.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Partial errors as part of the serviceData."""

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CopyRecursively(self, CopyInput: list[CopyRecursivelyInputInfo]) -> CopyRecursivelyResponse: ...
    def PasteDuplicateStructure(self, PasteDuplicateInput: list[PasteDuplicateInput], CopyRulesKey: str, NotifyEvents: bool) -> PasteDuplicateStructureResponse: ...

