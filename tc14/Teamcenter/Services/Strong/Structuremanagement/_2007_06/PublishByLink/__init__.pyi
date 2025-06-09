import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CompletenessCheckInputData:
    """
    
Contains string mentioning which action be performed on input BOMLine
representing
Part.
    """
    def __init__(self, ) -> None: ...
    Action: str
    """
            string representing action to be performed on BOMLine. Valid values are VerifyPartStructInteractive and ClearCompletenessCheckResults. The Completeness check is performed
            with action string is VerifyPartStructInteractive.
            The Completeness check is cleared if string is ClearCompletenessCheckResults.
            """
    Bomline: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
BOMLine representing Part structure for which Completeness Check has
            to be performed.
            """

class CompletenessCheckOutput:
    """
    
Contains set of Complete, Incomplete and Skipped BOMLines for CompletenessCheck.
Integer based index points output to corresponding input.
    """
    def __init__(self, ) -> None: ...
    InputIndex: int
    """Integer pointing to input. Useful to map output with input."""
    CompleteLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """BOMLines that satisfy Completeness criteria."""
    IncompleteLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """BOMLines that do not satisfy Completeness criteria."""
    SkippedLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """BOMLines for which Completeness criteria do not apply."""

class CompletenessCheckResponse:
    """
    
CompletenessCheckResponse containing list
            of CompletenessCheckOutput and ServiceData.  CompletenessCheckOutput
            contains list of Complete, Incomplete and Skipped BOMLines and
integer to
            map with input BOMLine. ServiceData
            contains any error that might have occurred during operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[CompletenessCheckOutput]
    """
CompletenessCheckOutput containing Complete,
            Incomplete and Skipped BOMLine objects. The integer inputIndex maps to index
            of input BOMLine to map output and input.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData contains partial error (if any)"""

class FindSourceOutput:
    """
    
Contains source BOMLine and integer based index to point output to corresponding
input.
    """
    def __init__(self, ) -> None: ...
    InputIndex: int
    """Integer pointing to input. Useful to map output with input."""
    SourceLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            Source BOMLine for input target BOMLine and source BOMWindow.
            Source BOMLine and Target BOMLine are associated via PublishLink.
            """

class FindSourceResponse:
    """
    
Contains FindSourceOutput containing source
BOMLine and index to map to source BOMLine to corresponding input target
BOMLine.
    """
    def __init__(self, ) -> None: ...
    Output: list[FindSourceOutput]
    """
FindSourceOutput containing source BOMLine
            and integer index to map source BOMLine to input target BOMLine.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
ServiceData with plain objects containing
            source BOMLine and partial errors.
            """

class FindTargetsOutput:
    """
    
Contains target BOMLines and integer based index to point output to
corresponding
input.
    """
    def __init__(self, ) -> None: ...
    InputIndex: int
    """Integer pointing to input. Useful to map output with input."""
    TargetLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """
            Target BOMLine for given source BOMLine and target BOMWindow.Target
            BOMLine and Source BOMLine are associated via PublishLink.
            """

class FindTargetsResponse:
    """
    
Contains FindTargetsOutput containing target
BOMLine objects and index to map to target BOMLine to corresponding
source.
    """
    def __init__(self, ) -> None: ...
    Output: list[FindTargetsOutput]
    """
FindTargetsOutput containing target BOMLine
            for input source BOMLine and integer index to map target BOMLine to
            input source BOMLine.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
ServiceData with plain objects containing
            target BOMLine objects and partial errors.
            """

class GetSourceTopLevelOutput:
    """
    
Contains context PSBOMView of the source of PublishLink for given input
target BOMLine. Integer based index points PSBOMView to corresponding
input.
    """
    def __init__(self, ) -> None: ...
    InputIndex: int
    """Integer pointing to input. Useful to map output with input."""
    TopLevelBomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView
    """PSBOMView of the source of PublishLink."""

class GetSourceTopLevelResponse:
    """
    
GetSourceTopLevelResponse contains vector
            of GetSourceTopLevelOutput and ServiceData.
    """
    def __init__(self, ) -> None: ...
    Output: list[GetSourceTopLevelOutput]
    """
GetSourceTopLevelOutput  containing PSBOMView
            in which context targets were added and integer index to map PSBOMView to
            input BOMLine.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
ServiceData containing partial error and
            PSBOMView in plain objects list.
            """

class LineAndWindow:
    """
    
Contains source BOMLine and target BOMWindow in which associated target
BOMLine of PublishLink to look for.
    """
    def __init__(self, ) -> None: ...
    Line: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """Source BOMLine object."""
    Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """Target BOMWindow object."""

class LogicallyEquivalentLinesOutput:
    """
    
Contains logically equivalent BOMLines from input BOMWindow and BOMLine.
The integer based index points equivalent line to input BOMLine.
    """
    def __init__(self, ) -> None: ...
    InputIndex: int
    """Integer pointing to input BOMLine. Useful to map output with input."""
    Lines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """Logically equivalent BOMLine objects."""

class LogicallyEquivalentLinesResponse:
    """
    
LogicallyEquivalentLinesResponse contains
            vector of LogicallyEquivalentLinesOutput
            and ServiceData.
    """
    def __init__(self, ) -> None: ...
    Output: list[LogicallyEquivalentLinesOutput]
    """
LogicallyEquivalentLinesOutput with equivalent
            BOMLine objects  for input BOMLine pointed by integer inputIndex.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
ServiceData with equivalent BOMLines
            in plain objects and partial errors.
            """

class PublishLinkInfo:
    """
    Required data to create a PublishLink like name, type, source and target
BOMLines.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """object_name to be set on the PublishLink."""
    Type: str
    """Valid type to set on the PublishLink's object_type."""
    Source: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """BOMLine object."""
    Targets: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """List of BOMLine objects."""

class PublishDataInfo:
    """
    
Contains PublishLinkInfo and dataFlags. Each bit of dataFlags
denotes what data to be published.
    """
    def __init__(self, ) -> None: ...
    LinkInfo: PublishLinkInfo
    """
PublishLinkInfo containing information to
            create PublishLink.
            """
    DataFlags: int
    """dataFlags representing what data to be published."""

class PublishLinkOutput:
    """
    
Contains PublishLink created by the operation and integer based index points
PublishLink to corresponding input.
    """
    def __init__(self, ) -> None: ...
    InputIndex: int
    """Integer pointing to input. Useful to map output with input."""
    PublishLink: Teamcenter.Soa.Client.Model.Strong.PublishLink
    """PublishLink object created during the operation."""

class PublishLinksResponse:
    """
    
PublishLinksResponse contains list of PublishLinkOutput structures and
ServiceData.
    """
    def __init__(self, ) -> None: ...
    Output: list[PublishLinkOutput]
    """
PublishLinkOutput containing PublishLink
            to which targets were added and integer index to map PublishLink to input
            BOMLine
"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
ServiceData with created objects and partial
            errors.
            """

class SourceAndTargets:
    """
    
Input structure that contains BOMLine objects representing source and targets
of PublishLink
    """
    def __init__(self, ) -> None: ...
    Source: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """BOMLine as source for PublishLink object"""
    Targets: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """BOMLine objects as target for PublishLink object"""

class PublishByLink:
    """
    Interface PublishByLink
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddTargets(self, Input: list[SourceAndTargets]) -> PublishLinksResponse:
        """    
             Adds AbsOccViewQualifier of target BOMLine objects to the existing
             PublishLink of input source BOMLine. The operation also saves updated
             PublishLink.
             

             Following validations are performed during operation and failures are reported in
             ServiceData.
             


PublishLink exists with source as input source and user has
             access to it.
             
Item type of source and target BOMLine as per PUBLISH_AlignableSourceTypes
             and PUBLISH_AlignableTargetTypes preference respectively.
             
No PublishLink exists with target as input target.
             
Logical identity of all target BOMLine is same.
             
Logical identity of source and target BOMLines is same.
             



Use Cases:

             Add in-context occurrence as target to an existing PublishLink for given source.
             

Dependencies:

             createLinks
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Input: 
<font face="courier" height="10">SourceAndTargets</font> containing source <b>BOMLine</b>
                         and corresponding target <b>BOMLine</b> objects.
             
        :return: 
        """
        ...
    def CompletenessCheck(self, Input: list[CompletenessCheckInputData]) -> CompletenessCheckResponse:
        """    
             Recursively evaluates completeness for BOMLine objects having underlying component
             as Part.  A BOMLine which requires positioned designed is marked as
             complete if underlying PartRevision has primary representation OR BOMLine
             has source associated via PublishLink object. If a BOMLine does not
             need positioned designed then such BOMLine is marked as complete as well.
             This operation also supports recursively clearing completeness results.
             

             If required the BOM is expanded internally. In case of packed BOMLines, if
             any of the BOMLine is incomplete then that packed line is marked as incomplete.
             


Use Cases:


Recursively perform completeness check for Part structure.
             
Recursively clears completeness check for Part structure.
             



Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Input: 
                         String representing action to be performed on corresponding <b>BOMLine</b>.
             
        :return: 
        """
        ...
    def CreateLinks(self, LinkInfos: list[PublishLinkInfo]) -> PublishLinksResponse:
        """    
             Creates PublishLink between AbsOccurrenceViewQualifier of source and
             target BOMLines. The dataFlags attribute
             of the PublishLink is set to 0 as no data was published. The operation also
             saves new PublishLink object.
             

             Following validations are performed during operation and failures are reported in
             ServiceData.
             


Item type of source and target BOMLine as per PUBLISH_AlignableSourceTypes
             and PUBLISH_AlignableTargetTypes preference respectively.
             
Type name is a valid TCType name.
             
PSBOMView of the source is local.
             
No PublishLink exists with source as input source.
             
No PublishLink exists with target as input target.
             



Use Cases:

             Perform in-context association between occurrences of two structures.
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param LinkInfos: 
                         Contains information to create <b>PublishLink</b>.
             
        :return: 
        """
        ...
    def FindLinesWithSameLogicalIdentity(self, Input: list[LineAndWindow]) -> LogicallyEquivalentLinesResponse:
        """    
             Finds logically equivalent BOMLines in BOMWindow for list of input
             BOMLines.
             

BOMLines are said to be identical if their AbsoluteOccurrence objects
             have same Usage Address and Positioned Designator.
             

Use Cases:

             Find equivalent BOMLine objects and associate them.
             

Dependencies:

             createLinks
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Input: 
<font face="courier" height="10">LineAndWindow</font> containing <b>BOMLine</b> for
                         which equivalent <b>BOMLine</b>s to be searched in corresponding input <b>BOMWindow</b>.
             
        :return: 
        """
        ...
    def FindSourceInWindow(self, Input: list[LineAndWindow]) -> FindSourceResponse:
        """    
             Finds source of the PublishLink in source BOMWindow for input target
             BOMLine objects. Source is returned as BOMLine.
             


Use Cases:

             Determine if BOMWindow has source for input target BOMLine objects.
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Input: 
<font face="courier" height="10">LineAndWindow</font> containing target <b>BOMLine</b>
                         and <b>BOMWindow</b> in which source of <b>PublishLink</b> to search.
             
        :return: 
        """
        ...
    def FindTargetsInWindow(self, Input: list[LineAndWindow]) -> FindTargetsResponse:
        """    
             Finds target of the PublishLink in target BOMWindow for input source
             BOMLine objects. Targets are returned as BOMLine objects.
             

Use Cases:


Determine if BOMWindow has targets for input source BOMLine.
             
Find targets for source of PublishLink and subsequently use
             found target BOMLine objects to delete links.
             



Dependencies:

             deleteTargetsFromLink
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Input: 
<font face="courier" height="10">LineAndWindow</font> containing source <b>BOMLine</b>
                         and <b>BOMWindow</b> in which target of <b>PublishLink</b> to search.
             
        :return: 43119 No Publish Link exists for the source.
        """
        ...
    def PublishData(self, PublishDataInfos: list[PublishDataInfo]) -> PublishLinksResponse:
        """    
             Copies Absolute Transformation Matrix and/or
             JT from source BOMLine to target BOMLine objects. If a PublishLink
             does not exist for source and target then a new PublishLink is created with
             input dataFlags. In case if PublishLink already exists then dataFlags of the
             PublishLink object is updated.
             

             Input dataFlags is used to determine which
             data has to be copied. Unless context was explicitly set - the data on target BOMLines
             is stored in-context of top BOMLine of the target BOMWindow.
             

             The DirectModel Dataset is attached with Rendering relation. If the target
             BOMLine is an assembly then PLMXML file is created based on RevisionRule
             of the source BOMWindow and attached to target BOMLine as Text
Dataset with Rendering relation. In case, in-context Dataset with Rendering
             relation already exists then that is replaced with the new one. The BOMWindow
             is saved after attaching the Dataset.
             

             Below validations are performed during operation and failures are reported in ServiceData.
             


dataFlags contains a valid
             value.
             
Target BOMLine requires positioned design.
             
Item type of source and target BOMLine as per PUBLISH_AlignableSourceTypes
             and PUBLISH_AlignableTargetTypes preference respectively.
             
Type name is a valid TCType name.
             
PSBOMView of the source is local.
             
No PublishLink exists other than source and target as in input.
             



Use Cases:

             Perform in-context association between occurrences of two structures and copy Absolute Transformation Matrix and/or JT from source
             to target BOMLine objects.
             

Dependencies:

             createLinks
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param PublishDataInfos: 
<font face="courier" height="10">PublishDataInfo</font> containing information to
                         create <b>PublishLink</b> and <font face="courier" height="10">dataFlag</font> to
                         determine which attributes should be copied to target <b>BOMLine</b>s.
             
        :return: 
        """
        ...
    def DeleteLinkForSource(self, Sources: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Finds and deletes PublishLink for input source BOMLine objects.
             

Use Cases:

             Delete PublishLink.
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Sources: 
                         Set of source <b>BOMLine</b> objects for which <b>PublishLink</b> to be deleted.
             
        :return: 43111 Invalid source as input.
        """
        ...
    def DeleteTargetsFromLink(self, Targets: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Deletes AbsOccViewQualifier of target BOMLines from the existing PublishLink.
             If the target being removed is the last one for PublishLink then PublishLink
             is also deleted. Otherwise operation saves updated PublishLink.
             

             Following validations are performed during operation.
             


             PublishLink exists whose target as input
             


Use Cases:

             Detach target BOMLine from PublishLink.
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Targets: 
                         Target <b>BOMLine</b> objects which need to be removed from existing <b>PublishLink</b>.
             
        :return: 
        """
        ...
    def GetSourceTopLevel(self, Targets: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> GetSourceTopLevelResponse:
        """    
             Finds source of PublishLink for given target BOMLine. For the source
             of the PublishLink finds context PSBOMView.
             

Use Cases:

             Find context PSBOMView for the source of PublishLink.
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Targets: 
<b>BOMLine</b>s for which source has to be found in order to determine context <b>PSBOMView</b>.
             
        :return: 43112 Invalid target as input.
        """
        ...

