import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AddOrUpdateChildrenToParentLineInfo:
    """
    Input structure for addOrUpdateChildrenToParentLine operation
    """
    def __init__(self, ) -> None: ...
    ParentLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            Parent BOMLine business object under which item or item element occurrences
            are added or modified.
            """
    ViewType: str
    """
            View Type string used for creating BOMView for parent BOMLine if it
            does not exist (NULL implies use default view type).
            """
    Items: list[ItemLineInfo]
    """Array of ItemLineInfo input structure."""
    ItemElements: list[ItemElementLineInfo]
    """Array of ItemElementLineInfo input structure"""

class AddOrUpdateChildrenToParentLineResponse:
    """
    Return structure for addOrUpdateChildrenToParentLine operation
    """
    def __init__(self, ) -> None: ...
    ItemLines: list[BOMLinesOutput]
    """Array of Output itemLines"""
    ItemelementLines: list[BOMLinesOutput]
    """Array of Output itemElementLines"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a common data strucuture used to return sets of Teamcenter Data Model object
            from a service request. This also holds services exceptions.
            """

class BaselineInput:
    """
    Input structure that holds information to create a new Baseline ItemRevision
    """
    def __init__(self, ) -> None: ...
    Dryrun: bool
    """
            To be set as 'true' if dryrun is to be performed, false if not. This is an optional
            element and the default value is false. Dry run option helps users to know of any
            possible errors without performing the actual baseline action. Choosing this option
            generates a report and can be accessed from the BaselineResponse.
            """
    ClientID: str
    """Identifier that helps the client to track the object(s) created"""
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Input ItemRevision object, that is to be baselined"""
    ViewType: str
    """View type name. To be provided if input ItemRevision has BOMViewRevision"""
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """RevisionRule object. To be provided if input ItemRevision has BOMViewRevision."""
    Precise: bool
    """
            Creates a precise baseline if set to true. If set to false, creates an imprecise
            baseline. Default value is false.
            """
    ReleaseProcess: str
    """Name of the workflow process template to be used for baselining."""
    Description: str
    """Description for baseline ItemRevision, optional"""
    BaselineJobName: str
    """
            Name to identify the job initiated during baseline. Operation will fail if a job
            name is not provided. In general job name is a combination of ItemId, Revision Id
            and ItemRevision Name property values.
            """
    BaselineJobDescription: str
    """Description for baseline job, optional"""

class BaselineOutput:
    """
    Refers to the output structure for baseline create operation.
    """
    def __init__(self, ) -> None: ...
    Dryrun: bool
    """
            BaselineOutput structure contains following elements
            
            dryrun - Dry run indicates that the operation will not create a baseline but it will
            only do the required validation. Boolean variable indicating if dry option was used.
            
"""
    ClientID: str
    """Client Identifier"""
    BaselineItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Created baseline ItemRevision object."""
    DryrunLogTicket: str
    """
            FMS ticket for dryrun log. Contains path to dry run report if dryrun flag is set
            to true.
            """

class BaselineResponse:
    """
    
            Output structure containing list of BaselineOutput
            structures and ServiceData with list of errors
            encountered during the Operation
            
    """
    def __init__(self, ) -> None: ...
    Output: list[BaselineOutput]
    """List of BaselineOutput structures"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """structure containing error codes and messages"""

class BOMLinesOutput:
    """
    This represents output structure for addOrUpdateChildrenToParentLine operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the object created."""
    Bomline: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The refers to BOMLine object."""

class ItemElementLineInfo:
    """
    
            This contains Item element Input structure for addOrUpdateChildrenToParentLine
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            Identifier that helps the client to track the object created. This is an optional
            parameter.
            """
    ItemElement: Teamcenter.Soa.Client.Model.ModelObject
    """Refers to the Item element object."""
    OccType: str
    """The occurrence type used for the child BOMLine creation objects."""
    ItemElementline: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            Refers to BOMLine object which represents itemElement for modification of
            properties (Used in case of update).
            """
    ItemElementLineProperties: System.Collections.Hashtable
    """Refers to the BomLineProperties struct."""

class ItemLineInfo:
    """
    Refers to Item input structure for addOrUpdateChildrenToParentLine operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            Identifier that helps the client to track the object created. This is an optional
            parameter.
            """
    Item: Teamcenter.Soa.Client.Model.ModelObject
    """Refers to Item object.(used in case of precise structure)"""
    ItemRev: Teamcenter.Soa.Client.Model.ModelObject
    """Refers to the ItemRevision object (used in case of imprecise structure)"""
    OccType: str
    """Refers to occurrence type used for the child BOMLine (occurrence) creation."""
    Bomline: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            Refers to BOMLine for modification of its properties (Used in case of update
            when clientId is empty).
            """
    ItemLineProperties: System.Collections.Hashtable
    """
            Refers BomLineProperties  struct which represents
            to property name/value pairs for additional properties.
            """

class RemoveChildrenFromParentLineResponse:
    """
    Return structure for removeChildrenFromParentLine operation
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData structure is used to return the updated parent BOMLine
            business objects whose children have been removed and can contain partial errors
            if the operations fails to create bom window. It also holds services exceptions.
            """

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateBaseline(self, Inputs: list[BaselineInput]) -> BaselineResponse:
        """    
             Creates a new Baseline ItemRevision based on a work in progress ItemRevision.
             If the input ItemRevision consists of a PSBOMViewRevision that represents
             a multi level structure, all components of the structure are baselined in a recursive
             fashion. If smart baseline option is enabled at the site, then components of the
             structure will be baselined only if they satisfy the criteria set forth by smart
             baseline feature. Released ItemRevision objects are not baselined, unless
             the specific name of ReleaseStatus object is mentioned in the preference Baseline_allowed_baserev_statuses.
             

Teamcenter Component:

             Baseline - Allows creation of a new baseline ItemRevision based on an input ItemRevision
             
        :param Inputs: 
                         Each of the structures , holds the <b>ItemRevision</b> to be baselined, <b>RevisionRule</b>
                         and valid <b>PSViewType</b> name to be used in case the <b>ItemRevision</b> has <b>BOMViewRevision</b>.
                         Dry run can be performed by providing value as 'true' for the dry run flag. In addition
                         to the above, user  needs to provide the Workflow template name to be used for baselining
                         and job name required to initialize the baseline workflow process.
             
        :return: sets of Teamcenter Data Model object from a service request. This also holds services
             exceptions. To process BaselineResponse:
        """
        ...
    def AddOrUpdateChildrenToParentLine(self, Inputs: list[AddOrUpdateChildrenToParentLineInfo]) -> AddOrUpdateChildrenToParentLineResponse:
        """    
             This operation takes item / item revision (depending on precise or
             imprecise structure) or a GDE. It takes view type to create a BOMView
             for the parent line in a product structure.  When the BOMLine for the item/item
             revision is provided and client id is empty, an update will be performed.
             

Use Cases:


User wants to update properties of two lines. He/She invokes the
             operation with the two lines and property values. The two lines will be updated with
             the specified property values.
             
User wants to create two lines with certain initial property values.
             He/she invokes the operation with the parent line, the two items to add and the initial
             property values. Two new lines will be created with the initial property values.
             
             



Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Inputs: 
                         This is a vector of AddOrUpdateChildrenToParentLineInfo. Each element of this vector
                         contains an input <b>BOMLine</b> which is going to get updated, view type e.g. CAEAnalysis,
                         MEProcess, MESetup, View, an array of ItemLineInfo and ItemElementLineInfo capturing
                         the details of children to be added or updated.
             
        :return: structures containing newly added Item BOMLines, Item Element Lines and ServiceData
             containing any created child bomline and the updated bomline object will be sent
             back in the standard ServiceData member lists of created objects and updated objects
             respectively. Any failures will be returned in the ServiceData list of partial errors.
        """
        ...
    def RemoveChildrenFromParentLine(self, Bomlines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> RemoveChildrenFromParentLineResponse:
        """    
             This operation allows developers to remove a BOMLine from an assembly /product
             structure. This operation takes vector of BOMLine business objects as input,
             which allows removal of multiple BOMLines from the structure in a single operation.
             

Use Cases:

             User wants to remove two lines. He/She invokes the operation with the lines, and
             the lines are removed.
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Bomlines: 
                         This is a vector of <i>Teamcenter::BOMLine</i> and contains all the <i>BOMLines</i>
                         that need to be deleted from an assembly/product structure
             
        :return: sets of Teamcenter Data Model object from a service request. This also holds services
             exceptions.
        """
        ...

