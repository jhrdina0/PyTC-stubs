import Ptn0.Services.Strong.Partition._2011_06.PartitionManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FailedMemberErrorStructure:
    """
    
            FailedMemberErrorStructure structure contains the clientId of the input BOMLine
            and errorVal structure which stores all the information about the error.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Input clientId for which error is reported."""
    ErrorVal: Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.ErrorValuesStruct
    """Stores all the data about the error which occurred while updating the member."""

class IsPartitionableInputInfo:
    """
    
            IsPartitionableInputInfo structure contains the Ptn0Partition and the BOMLine
            objects to be added to the Ptn0Partition.
            
    """
    def __init__(self, ) -> None: ...
    Partition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """Ptn0Partition for which the BOMLine objects are to be added."""
    CsidPaths: list[OccThreadPathInformation]
    """A list of CSID path for the BOMLine objects that need to be added to the Ptn0Partition."""

class IsPartitionableOutputInfo:
    """
    
            IsPartitionableOutputInfo structure contains a Ptn0Partition and the verdicts
            for the BOMLine objects that need to be added as a member of the Ptn0Partition.
            
    """
    def __init__(self, ) -> None: ...
    Partition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """Ptn0Partition object for which the errors are reported."""
    PartitionMemberInfo: list[PartitionMemberInformation]
    """
            A list of the client identifiers of the BOMLine and the corresponding flag
            that indicates whether the BOMLine can be added as a member of the Ptn0Partition.
            """

class IsPartitionableResponse:
    """
    
            IsPartitionableResponse structure contains the verdict that indicates whether the
            BOMLine objects can be added as members to the Ptn0Partition.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[IsPartitionableOutputInfo]
    """
            A list containing a combination of Ptn0Partition object and the corresponding
            list of verdicts for BOMLine objects that indicate if the BOMLine objects
            can be added as members of the Ptn0Partition.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains any errors that might have occurred as part of the service invocation."""

class OccThreadPathInformation:
    """
    OccThreadPathInformation structure represents the details of clientId, OccThreadPath.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client track the objects."""
    OccThreadPath: str
    """
            CSID path for the BOMLine objects that need to be added or removed from the
            Partition.
            """

class PartitionMemberInformation:
    """
    
            partitionMemberInformation structure contains the client identifiers of the input
            BOMLine and the corresponding flag that indicates whether the BOMLine
            can be added as a member of the Ptn0Partition.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Input clientId for which error is reported."""
    IsPartitionable: bool
    """
            True if BOMLine can be added as a member of the Ptn0Partition, False
            otherwise.
            """

class UpdateMembersInBOMWindowInputInfo:
    """
    
            UpdateMembersInBOMWindowInputInfo structure represents the details of Ptn0Partition
            object, OccThreadPathInformation structure and OperationCode.
            
    """
    def __init__(self, ) -> None: ...
    Partition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """Ptn0Partition for which the BOMLine objects are to be added or removed."""
    OccThreadPathInfo: list[OccThreadPathInformation]
    """
            A list of CSID path for the BOMLine objects that need to be added or removed
            from the Ptn0Partition.
            """
    Opcode: str
    """
            Operation to perform on the partition. This parameter can be any one of the following
            values:
            
            ADD_MEMBER : Add BOMLine to input partition.
            
            REMOVE_MEMBER : Remove BOMLine from input partition.
            """

class UpdateMembersInBOMWindowOutputInfo:
    """
    
            UpdateMembersInBOMWindowOutputInfo structure contains a Ptn0Partition and
            errors for BOMLine objects that could not be added or removed from the Ptn0Partition.
            
    """
    def __init__(self, ) -> None: ...
    Partition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """Ptn0Partition object for which the errors are reported."""
    FailedMemberInfo: list[FailedMemberErrorStructure]
    """
            A list of the client identifiers of the failed BOMLine objects and the corresponding
            error that occurred while performing the update member operation.
            """

class UpdateMembersInBOMWindowResponse:
    """
    Contains the list of UpdateMembersInBOMWindowOutputInfo object and serviceData structures.
    """
    def __init__(self, ) -> None: ...
    Output: list[UpdateMembersInBOMWindowOutputInfo]
    """
            A list of Ptn0Partition objects and errors for BOMLine objects that
            could not be added or removed from the Ptn0Partition.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains any errors that might have occurred as part of the service invocation."""

class PartitionManagement:
    """
    Interface PartitionManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def IsPartitionable(self, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision, BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView, IsPartitionableInputInfo: list[IsPartitionableInputInfo]) -> IsPartitionableResponse: ...
    def UpdateMembersInBOMWindow(self, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision, BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView, UpdateMembersInBOMWindowInputInfo: list[UpdateMembersInBOMWindowInputInfo]) -> UpdateMembersInBOMWindowResponse:
        """    
             This operation updates the given input Ptn0Partition with the BOMLine
             objects supplied. BOMLine objects can be added or removed for the given Ptn0Partition.
             The user performing this operation needs ADD_CONTENT or REMOVE_CONTENT access privilege
             on the Ptn0Partition or WRITE access privilege on the BOMLine, depending
             upon ownership of the member. If the user does not have the required privileges or
             if any of the validations fail, then the operation returns an error in ServiceData
             along with the failed BOMLine objects and error code for each of the failed
             BOMLine objects in the UpdateMemberInBomWindowResponse structure.
             

Use Cases:

Use case 1: Add Members to Partition


             User creates a Partition Breakdown with Ptn0Partition objects. The user can
             add single or multiple BOMLine objects to the input Ptn0Partition objects.
             

Use case 2: Remove Members from Partition


             User creates a Partition Breakdown with Ptn0Partition objects. The user can
             remove single or multiple BOMLine objects  from input Ptn0Partition
             objects.
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param ConfigurationContext: 
                         ConfigurationContext used to configure the <b>BOMWindow</b>.
             
        :param ItemRevision: 
                         The <b>ItemRevision</b> for the top line of the <b>BOMWindow</b>.
             
        :param BomView: 
                         The <b>PSBOMView</b> to be used when creating the <b>BOMWindow</b>, or NULL to use
                         the default view.
             
        :param UpdateMembersInBOMWindowInputInfo: 
                         A list of input <b>Ptn0Partition</b> objects, OccThreadPathInformation structure
                         and OpCode.
             
        :return: 
        """
        ...

