import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AdditionalInfo:
    """
    a generic structure to capture additional information.
    """
    def __init__(self, ) -> None: ...
    IntMap: System.Collections.Hashtable
    """A map (string/list of integers) of generic key to integer values."""
    DblMap: System.Collections.Hashtable
    """A map (string/list of doubles) of generic key to double values."""
    StrMap: System.Collections.Hashtable
    """A map (string/list of strings) of generic key to string values."""
    ObjMap: System.Collections.Hashtable
    """
            A map (string/list of BusinessObjects) of generic key to  BusinessObject
            values.
            """
    DateMap: System.Collections.Hashtable
    """A map (string/list of dates) of generic key to date values."""

class BaseIceInfo:
    """
    
BaseIceInfo structure details the changes in Incremental Change context for each
Incremental Change Element.
    """
    def __init__(self, ) -> None: ...
    TypeOfIce: int
    """
            Type of incremental change.
            

1 means data has been added in context of incremental change.
            
2 means data has been removed in context of incremental change.
            

"""
    HowConfigured: str
    """
            detail of how the incremental change is configured. If howConfigured
            is empty, it means the incremental change element is not configured.
            """
    IcRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            incremetal change revision object which is referenced by the incremental change element
            associated with the change.
            """
    Ice: Teamcenter.Soa.Client.Model.Strong.IncrementalChangeElement
    """
            incremental change element associated with the change on the bomline. This change
            can be because of structural changes, attachment changes, predecessor changes or
            activity changes associated with the bomline.
            """
    AffectedObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The object affected by the change. It can be one of the following types (not full
            list):
            

PSOccurrence
            
Datasets
            
Folders
            
Forms
            
Activities
            
AbsOccData
            

"""
    AttributeName: str
    """Name of the attribute associated with the change"""
    AttributeDisplayName: str
    """Display name of the attribute whose value changed."""
    AttributeValue: str
    """Value of the attribute after change in Incremental change context."""
    PredecessorName: str
    """name of predecessor."""
    PredecessorSequence: str
    """Sequence number of predecessor."""
    UnitRange: str
    """unit range text. Empty if not unit effectivity."""
    DateRange: str
    """date range text if date effectivity is used."""
    AbsoccRootLine: str
    """The context line name in which the change occurred"""
    AuxiliaryData: AdditionalInfo
    """
            A generic structure of keys and vectors of values (integer,double,object,string,date
            types) for passing additional metadata regarding the nature of incremental change.
            """

class EndItemUnitData:
    """
    
EndItemUnitData structure captures information about unit based effectivity. The
search will track changes between the start Unit and end Unit for the specified
End
Item. All 3 must be valid for successful usage.
    """
    def __init__(self, ) -> None: ...
    StartUnit: int
    """The start unit. Valid values must be 0 or greater."""
    EndUnit: int
    """The end Unit. Valid values must be greater than startUnit."""
    EndItem: Teamcenter.Soa.Client.Model.ModelObject
    """
Item or ItemRevision representing the end item corresponding to the
            start and end unit range.
            """

class DateEffectivityData:
    """
    
DateEffectivtyData structure captures information about date based effectivity.
The
search will track changes between the start Date and end Date. End Date must be
greater
than start Date.
    """
    def __init__(self, ) -> None: ...
    StartDate: System.DateTime
    """The start date of the range to search in."""
    EndDate: System.DateTime
    """The end date of the range to search in."""

class OccurrenceEffectivitySearchInfo:
    """
    
OccurrenceEffectivitySearchInfo structure contains information for scoping the
Occurrence
Effectivity parameters used for tracking changes in structure based on
OccurrenceEffectivity.
    """
    def __init__(self, ) -> None: ...
    IsUnitData: bool
    """If true unit data is being provided as opposed to date information."""
    UnitData: EndItemUnitData
    """
            The details for searching changes based on unit information ( start Unit, end Unit
            and the end Item for the Unit effectivity).
            """
    DateEffectivityData: DateEffectivityData
    """The details for searching changes based on date (start Date and end Date)."""

class StatusData:
    """
    
StatusData structure contains filtering criterion for release status objects
associated
with the change.
    """
    def __init__(self, ) -> None: ...
    ListOfStatus: list[str]
    """
            A list of status names like Pending, TCM Released etc. to be used to filter based
            on status names
            """
    SinceDate: System.DateTime
    """The date on or after which the status objects are created."""

class RevisionEffectivitySearchInfo:
    """
    
RevisionEffectivitySearchInfo structure contains information for scoping the
Revision
Effectivity  parameters used for tracking changes in structure based on
RevisionEffectivity.
    """
    def __init__(self, ) -> None: ...
    OwningUser: str
    """The owning user of the incremental change revision object(s) to search for."""
    OwningGroup: str
    """The owning group of the incremental change revision object(s) to search for."""
    Statuses: StatusData
    """The details for status names and their start date."""
    IsUnitData: bool
    """If true unit data is being provided as opposed to date information."""
    UnitData: EndItemUnitData
    """
            The details for searching changes based on unit information ( start Unit, end Unit
            and the end Item for the Unit effectivity).
            """
    DateEffectivityData: DateEffectivityData
    """The details for searching changes based on date (start Date and end Date)."""

class ICFilterCriteria:
    """
    
ICFilterCriteria structure captures information about filtering criteria of
incremental
change contexts.
    """
    def __init__(self, ) -> None: ...
    OwningUser: str
    """The owning user of the incremental change revision object(s) to search for."""
    OwningGroup: str
    """The owning group of the incremental change revision object(s) to search for."""
    Statuses: StatusData
    """The details for status names and their start date."""
    Intents: list[str]
    """
            A list of intents associated with Incremental Change contexts that should included
            in the search. These strings must be valid Intent names in Teamcenter.
            """
    IncludedICRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    """
            A list of ItemRevision objects representing preselected incremental change
            contexts to be used for seaching incremental change elements. This list is merged
            with the results of the other search parameters.
            """
    ExcludedICRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    """
            A list of ItemRevision objects representing preselected incremental change
            contexts to be excluded from the search
            """

class ICSearchInfo:
    """
    
ICSearchInfo structure contains information for scoping the Incremental Change
contexts
to be intersected while searching for Incremental Change Elements tracking the
changes
in the structure.
    """
    def __init__(self, ) -> None: ...
    IsUnitData: bool
    """If true unit data is being provided as opposed to date information."""
    UnitData: EndItemUnitData
    """
            The details for searching changes based on unit information ( start Unit, end Unit
            and the end Item for the Unit effectivity).
            """
    DateEffectivityData: DateEffectivityData
    """The details for searching changes based on date (start Date and end Date)."""
    IcFilterCriteria: ICFilterCriteria
    """
            The details for searching Incremental change contexts. It is only relevant for Incremental
            Change
            """

class ChangeTrackerInput:
    """
    
ChangeTrackerInput structure contains a vector of ChangeTrackerDataTypes
representing
the type of change to track (any unique combination of IncrementalChange,
RevisionEffectivity, OccurrenceEffectivity), a vector of BOMLine objects
that are used for scoping the data (only lines below the scope are considered
for
change tracking), and a structure representing the selection criteria for
Incremental
Change. Currently, only Incremental Change based changes are trackable.
    """
    def __init__(self, ) -> None: ...
    DataTypes: list[str]
    """
            Types of changes to be tracked. A unique of set of ChangeTrackerDataTypes (IncrementalChange,RevisionEffectivity,OccurrenceEffectivity).
            Currently, only IncrementalChange is supported.
            """
    SelectedLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of scope lines below which the changes are to be tracked. Currently, must
            be BOMLine objects or their subtypes.
            """
    OccEffInfo: OccurrenceEffectivitySearchInfo
    """
            Occurrence effectivity selection criterion. Captures information about range of units/dates
            to be considered while searching for Occurrence effectivities.
            """
    RevEffInfo: RevisionEffectivitySearchInfo
    """
            Revision effectivity selection criterion. Captures information about range of units/dates/statuses
            to be considered while searching for Revision effectivities.
            """
    IcInfo: ICSearchInfo
    """
            Incremental change context selection criterion. Captures information about range
            of units/dates/intents/statuses to be considered while searching for IncrementalChanges.
            """

class LineIceInfo:
    """
    
LineIceInfo structure details the changes in Incremental Change context for each
BOMLine.
    """
    def __init__(self, ) -> None: ...
    Line: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The configured changed line."""
    IceChanges: list[BaseIceInfo]
    """A list of changes in the line based on Incremental Change."""
    ConfiguredCompetingIces: list[BaseIceInfo]
    """
            A list of incremental change elements that are configured - yet not selectable. The
            best candidate appears in iceChanges. Currently not supported and all ice elements
            appear under iceChanges.
            """

class OccEffInfo:
    """
    
OccEffInfo structure details the changes in OccurrenceEffectivity context
for each PSOccurrence configured by OccurrenceEffectivity.
    """
    def __init__(self, ) -> None: ...
    ChangeType: int
    """
            Type of occurrence change. Currently, there is only one type of change supported.
            

1 means data has been configured based on OccurrenceEffectivity.
            

"""
    Occurrence: Teamcenter.Soa.Client.Model.ModelObject
    """The object which is configured by OccurrenceEffectivity."""
    Effectivity: str
    """detail of occurrence effectivity."""
    AuxiliaryData: AdditionalInfo
    """
            A generic structure of keys and vectors of values (integer,double,object,string,date
            types) for passing additional metadata regarding the nature of incremental change.
            """

class LineOccInfo:
    """
    Details the changes in Occurrence Effectivity context for each BOMLine.
    """
    def __init__(self, ) -> None: ...
    Line: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The line affected by OccurrenceEffectivity."""
    OccChanges: OccEffInfo
    """Details of changes in the line based on OccurrenceEffectivity."""

class RevEffInfo:
    """
    
RevEffInfo structure details the changes in RevisionEffectivity context for
each ItemRevision configured by RevisionEffectivity.
    """
    def __init__(self, ) -> None: ...
    ChangeType: int
    """
            Type of revision change. Currently, there is only one type of change supported.
            

1 means data has been configured based on RevisionEffectivity.
            

"""
    Revision: Teamcenter.Soa.Client.Model.ModelObject
    """The object which is configured by RevisionEffectivity."""
    HowConfigured: str
    """detail of how the revision is configured."""
    UnitRange: str
    """unit range text if unit effectivity is used."""
    DateRange: str
    """date range text if date effectivity is used."""
    AuxiliaryData: AdditionalInfo
    """
            A generic structure of keys and vectors of values (integer,double,object,string,date
            types) for passing additional metadata regarding the nature of incremental change.
            """

class LineRevInfo:
    """
    Details the changes in Revision Effectivity context for each BOMLine.
    """
    def __init__(self, ) -> None: ...
    Line: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The line affected by RevisionEffectivity."""
    RevChanges: RevEffInfo
    """Details of changes in the line based on RevisionEffectivity."""

class StructureChangesResponse:
    """
    
StructureChangesResponse structure contains a vector of
structureChangesResponseElement,
the size of which matches the input ChangeTrackerInput vector
    """
    def __init__(self, ) -> None: ...
    ResponseElements: list[StructureChangesResponseElement]
    """A list of StructureChangesResponseElement structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data capturing partial errors using the input array index as client id."""

class StructureChangesResponseElement:
    """
    
StructureChangesResponseElement returns the changed lines and removed lines. The
removed lines are configured in removed lines. Should treat the removed lines
with
caution as they won't show up in the configured bom.
    """
    def __init__(self, ) -> None: ...
    AddedLines: list[LineIceInfo]
    """A list of changed lines."""
    RemovedLines: list[LineIceInfo]
    """
            A list of configured removed lines. This is separate even though it is a change,
            to allow the clients to treat the removed lines carefully ( no selection synchronization
            for example).
            """
    VisibleLinesByOccEff: list[LineOccInfo]
    """A list of changed lines in context of Occurrence Effectivity."""
    InvisibleLinesByOccEff: list[LineOccInfo]
    """A list of unconfigured changed lines in context of Occurrence Effectivity."""
    VisibleLinesByRevEff: list[LineRevInfo]
    """A list of changed lines in context of Revision Effectivity."""
    InvisibleLinesByRevEff: list[LineRevInfo]
    """A list of unconfigured changed lines in context of Revision Effectivity."""

class StructureSearch:
    """
    Interface StructureSearch
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetStructureChanges(self, ChangeTrackerInput: list[ChangeTrackerInput]) -> StructureChangesResponse:
        """    
             This operation searches for delta changes in the structure based on different search
             criteria. The BOMLine objects directly or indirectly affected by changes done in
             Incremental Change context or revision effectivity context or occurrence effectivity
             context that are configured in are returned. The caller must supply the BOMLine object(s)
             that determines the scope for the search in addition to search parameters like intent,
             release status names, and one of unit range or date range. The lines returned are
             those that are configured by the current revision rule. All the BOMLines created/found
             will be returned as part of ServiceData along with incremental changes elements (
             in case of IncrementalChange context), or ItemRevisions ( in case of Revision
             effectivity/Occurrence effectivity). All partial errors are grouped by the index
             of the input vector. This operation should be consided when the scope will not yield
             too many expandlines lines below.
             

Use Cases:

             A user wants to find a set of incremental changes of a particular type and with a
             specific unit effectivity.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param ChangeTrackerInput: 
                         The type of change to be tracked ( <b>IncrementalChange</b>,   <b>RevisionEffectivity</b>,
                         or <b>OccurrenceEffectivity</b> or modified time) and the scoping BOMLine objects
                         and the selection criteria for Incremental Change elements ( only relevant when Incremental
                         Change context is specified ).
             
        :return: 
        """
        ...

