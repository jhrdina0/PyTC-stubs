import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class AddAssociationInput:
    """
    BOMLines for the contexts to be associated
    """
    def __init__(self, ) -> None: ...
    AssociateToContext: Teamcenter.Soa.Client.Model.ModelObject
    """target (primary) context to associate (link) to."""
    AddedContexts: list[AssociatedContextInfo]
    """vector of contexts info that are going to be associated(added) to the target."""

class AssociateAndAllocateInput:
    """
    
            Input for the automatic allocation commands such as automaticAssociateAndAllocate,
            associateAndAllocatePreview and associateAndAllocateByPreview command.
            
    """
    def __init__(self, ) -> None: ...
    SourceProductBOP: Teamcenter.Soa.Client.Model.ModelObject
    """Source Product BOP for which allocate command was called"""
    TargetPlantBOPLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Target Plant BOP's lines to which the allocation is to be done."""
    ReferenceProductBOP: Teamcenter.Soa.Client.Model.ModelObject
    """Reference Product BOP according to which allocation is to be done."""

class FileTicket:
    """
    To represent a file ticket and its original file name.
    """
    def __init__(self, ) -> None: ...
    Ticket: str
    """The FMS file Ticket."""
    FileName: str
    """The original file name."""

class AssociateAndAllocateResponse:
    """
    
            Response for the automatic allocation commands such as automaticAssociateAndAllocate,
            and associateAndAllocateByPreview.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data will hold partial errors, warnings  and errors, if any."""
    LogFileTicket: FileTicket
    """
            File Ticket Containing the UID and file name for the Log File generated for this
            command.
            """

class AssociatedContextInfo:
    """
    AssociatedContextInfo
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """
            context  The added (source) context that should be associated (linked) associate
            to target context (associateToContext parameter).
            """
    RelationName: str
    """
            relationName  The relation to use to connect. If the string is empty then the relation
            defined as default will be used. It should be possible to define the default association
            relation for each pair of types.
            """

class AssociateOutput:
    """
    Associated BOMLines to the input context
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """Input context"""
    AssociatedContextsInfo: list[AssociatedContextInfo]
    """
            vector of pairs of contexts and relation name that are associated with the input
            context
            """

class AssociationResponse:
    """
    
            Contains a list of items tags representing the associated BOMLines with the given
            context.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[AssociateOutput]
    """A vector of BOMLines associated to the input context"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Partial errors mapped to the client id"""

class AutomaticAllocatePreviewResponse:
    """
    Response for the automatic allocation commands automaticAllocatePreview.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data will hold partial errors, warnings  and errors, if any."""
    PreviewFileTicket: FileTicket
    """
            File Ticket Containing the UID and file name for the CSV File generated for preview
            during this command.
            """
    AllocationMap: System.Collections.Hashtable
    """Map of allocations from the source structure to the target structure."""

class ConnectObjectResponse:
    """
    ConnectObjectResponse
    """
    def __init__(self, ) -> None: ...
    NewObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """new BOMLines, created as a result of connection operation under the new target BOMLines"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""

class GeneralInfo:
    """
    
            Holds all additional flags that are needed for the connect like quantity (number
            of occurrences),  copy predecessor flag, copy occurrence type from the source flag,
            propagate XForm flag.
            
    """
    def __init__(self, ) -> None: ...
    StringProps: System.Collections.Hashtable
    """Map containing string property values"""
    StringArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""
    DoubleProps: System.Collections.Hashtable
    """Map containing string property values"""
    DoubleArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""
    FloatProps: System.Collections.Hashtable
    """Map containing string property values"""
    FloatArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""
    IntProps: System.Collections.Hashtable
    """Map containing string property values"""
    IntArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""
    BoolProps: System.Collections.Hashtable
    """Map containing string property values"""
    BoolArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""
    DateProps: System.Collections.Hashtable
    """Map containing DateTime property values"""
    DateArrayProps: System.Collections.Hashtable
    """Map containing DateTime array property values"""
    TagProps: System.Collections.Hashtable
    """Map containing string property values"""
    TagArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""

class SourceInfo:
    """
    contains all needed information in order to connect source BOMLines to the target
    """
    def __init__(self, ) -> None: ...
    SourceObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """BOMLines to connect the target"""
    RelationType: str
    """
            occurrence type for new assigned line. If its empty  server will use the default
            occurrence type
            """
    RelationName: str
    """
            The relation for the connect. If the string is empty then the default relation will
            be defined and used by the server
            """
    AdditionalInfo: GeneralInfo
    """
            Holds all additional flags that are needed for connect like quantity (number of occurrences),
            copy predecessor flag, copy occurrence type from the source flag, propagate XForm
            flag. Can be easily extended without changing the signature of the SOA
            """

class ConnectObjectsInputData:
    """
    A list of ConnectInput BOMLines for the nodes to be connect
    """
    def __init__(self, ) -> None: ...
    TargetObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            BOMLines to connect with. Can be a vector as a result of the multiple selection of
            the targets
            """
    SourceInfo: SourceInfo
    """all needed information in order to connect source BOMLines to the target"""

class DisconnectFromOriginInputData:
    """
    Input structure for DisconnectFromOrigin Command
    """
    def __init__(self, ) -> None: ...
    LineToDisconnect: Teamcenter.Soa.Client.Model.ModelObject
    """Plant BOP or Product BOP line that needs to be disconnected from their origin."""
    IsRecursive: bool
    """
            Flag specifying whether the sub-processes and sub-operations are to be disconnected
            recursively.
            """

class GetAssociatedContextsInputData:
    """
    GetAssociatedContextsInputData
    """
    def __init__(self, ) -> None: ...
    AssociateToContext: Teamcenter.Soa.Client.Model.ModelObject
    """associateToContext"""
    RelationName: list[str]
    """relationName"""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddAssociatedContexts(self, Input: list[AddAssociationInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Generic operation for setting different kinds of associations. It could be between
             Plant BOP and Product BOP (Leading Plant BOP in the future), Product (root) and Process
             (root) structures, regular Plant (Workarea) (root) and Process (root) structures,
             EBOM-MBOM. For now we will use it as threshold for Plant BOP and Product BOP. Other
             types are defined as target. This SOA will be used for add operation. Remove/disconnect
             (future) will be implemented in separate SOA.
             
        :param Input: 
                         list of AddAssociationInput BOMLines for the contexts to be associated.
             
        :return: ServiceData
        """
        ...
    def AssociateAndAllocateByPreview(self, Input: AssociateAndAllocateInput, AllocationMap: System.Collections.Hashtable) -> AssociateAndAllocateResponse:
        """    
             This function is the second function call in case a preview is required for automatic
             allocation this function does the actual allocation from Source Product BOP to a
             Target Plant BOP on the basis of a Reference Product BOP. This is done by passing
             the allocation map back to the server which we recived in the  automaticAllocatePreview
             command. This function also associates the Source Product BOP with the Target Plant
             BOP in case they are not associated. This function can throw the following exceptions,
             Reference Product BOP is not linked to the Target Plant BOP and Some allocation from
             the source structure to the target structure were unsuccessful please see the log
             for more details. Both these error messages will have the severity level of error.
             
        :param Input: 
                         Input specifying source, target and reference objects.
             
        :param AllocationMap: 
                         Map of allocations from the source structure to the target structure.
             
        :return: Response containing the log file ticket and service data.
        """
        ...
    def AutomaticAllocatePreview(self, Input: AssociateAndAllocateInput) -> AutomaticAllocatePreviewResponse:
        """    
             This function is the first function call in case a preview is required for automatic
             allocation from Source Product BOP to a Target Plant BOP on the basis of a Reference
             Product BOP. This function finds the allocated lines from the reference product BOP
             to the Plant BOP and equivalent lines in the source Product BOP and generates a preview
             for the automatic allocation in CSV format . Also this function returns an allocationMap,
             which needs to be sent back to server in case the user wants to go ahead with the
             allocation , for which it calls the second server call associateAndAllocateMap command
             . This function can throw the following exceptions, Reference Product BOP is not
             linked to the Target Plant BOP . This error messages will have severity level of
             error.
             
        :param Input: 
                         Input specifying source, target and reference objects.
             
        :return: Response containing allocation map, CSV file ticket and service data.
        """
        ...
    def AutomaticAssociateAndAllocate(self, Input: AssociateAndAllocateInput) -> AssociateAndAllocateResponse:
        """    
             This function is a single call function that does the allocation from Source Product
             BOP to a Target Plant BOP on the basis of a Reference Product BOP. This function
             finds the allocated lines from the reference product BOP to the Plant BOP and equivalent
             lines in the source Product BOP and does the allocation from the Source Product BOP
             to the Target Plant BOP in a single call. This function also associates the Source
             Product BOP with the Target Plant BOP in case they are not associated. This function
             can throw the following exceptions, Reference Product BOP is not linked to the Target
             Plant BOP and Some allocation from the source structure to the target structure were
             unsuccessful please see the log for more details. Both these error messages will
             have the severity level of error.
             
        :param Input: 
                         Input specifying source, target and reference objects.
             
        :return: Response containing the service data and log file path.
        """
        ...
    def ConnectObjects(self, Input: list[ConnectObjectsInputData]) -> ConnectObjectResponse:
        """    
             Generic operation for connecting MFG nodes       int        quantityNum - number
             of BOMLines to create (used in paste special). Default value is 1. int        occurrenceNumber
             - for packed lines. Number of occurrences to create (used in paste special). Default
             value is 1. int        findNumber - find number. Always passed by client.
             
        :param Input: 
                         A list of ConnectInput BOMLines for the nodes to connect
             
        :return: Generic operation for connecting MFG nodes
        """
        ...
    def DisconnectFromOrigin(self, InputVector: list[DisconnectFromOriginInputData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Disconnects objects and their children from their origin relation. Origin relation
             is created when the objects are assigned from the Product BOP/Generic BOP to the
             Plant BOP/Product BOP. This functionality removes the origin relation created during
             the assignment. Also this functionality can be called recursively for the processes
             below. This functionality can return an error in the following conditions, the object
             on which disconnect function was called called does not have an origin in case of
             non-recursive calls. This error will have a severity level of information. And This
             functionality is not available on this type of object only ProcessAreas, WorkAreas,
             Partitions, Processes and Operations type objects are expected.
             
        :param InputVector: 
                         Vector of DisconnectFromOriginInputData specifying the lines to be disconnected and
                         whether the children are to be recursively disconnected too.
             
        :return: Service data containing the errors that occurred during the disconnect command.
        """
        ...
    def GetAssociatedContexts(self, Input: list[GetAssociatedContextsInputData]) -> AssociationResponse:
        """    Returns associated contexts with the input context.
        :param Input: 
                         input
             
        :return: Returns associated contexts with the input context
        """
        ...

