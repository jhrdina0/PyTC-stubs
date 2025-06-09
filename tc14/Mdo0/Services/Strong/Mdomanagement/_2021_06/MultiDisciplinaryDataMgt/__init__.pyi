import Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt
import Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class MDIAssociationInfo:
    """
    Mdo0MDInstance association input for operation.
    """
    def __init__(self, ) -> None: ...
    DesignInstanceFor4G: Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.InstanceDataFor4G
    """
            The 4G design instance for which the Mdo0MDInstance association with the mdo0NeedsValidation
            set to true is to be identified and returned.
            """
    BvrDesignInstance: Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.BVRInstanceData
    """
            The Product Structure assembly instance for which the Mdo0MDInstance associations
            with the mdo0NeedsValidation set to true is to be identified.
            """

class MDInstanceData2:
    """
    
            The Mdo0MDInstance and the linked design instances with needs validation status
            captured as true on association.
            
    """
    def __init__(self, ) -> None: ...
    MdiObject: Teamcenter.Soa.Client.Model.Strong.Mdo0MDInstance
    """The Mdo0MDInstance object to which the instance is linked to."""
    InstancesFor4G: list[Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.InstanceDataFor4G]
    """
            A list of linked 4G design instances with needs validation set as true. Design Instance
            will be of Mdl0ModelElement or its subclasses.
            """
    InstancesForBVR: list[Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.BVRInstanceData]
    """
            A list of linked Product structure assembly instances with needs validation set as
            true.
            """

class MDTAssociationInfo:
    """
    Mdo0MDThread association input for operation.
    """
    def __init__(self, ) -> None: ...
    QueryAllMDOLinks: bool
    """
            If true, all  Mdo0MDTAssociation which has mdo0NeedsValidation attribute set
            to true are to be searched and returned.
            """
    InputMDO: Teamcenter.Soa.Client.Model.Strong.Mdo0MDThread
    """
            The Mdo0MDThread object for which all Mdo0MDTAssociation which has
            mdo0NeedsValidation set to true is to be identified and returned.
            """
    InputDesignArtifact: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The design artifact for which the Mdo0MDTAssociations with the mdo0NeedsValidation
            set to true is to be identified and returned. Design artifact is of type: WorkspaceObject.
            The supported types are defined in type constant Mdo0ValidMDTAssocTypes. Out of the
            box supported types are Item, ItemRevision, Lbr0LibraryElement.
"""

class NeedsValidationLinkInput2:
    """
    Input structure for queryNeedsValidationLink2 operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    MdtAssoInfo: MDTAssociationInfo
    """
            The Mdo0MDThread association related information for which mdo0NeedsValidation
            set as true is to be identified.
            """
    MdiAssoInfo: MDIAssociationInfo
    """
            The Mdo0MDInstance association related information for which mdo0NeedsValidation
            set as true is to be identified.
            """

class NeedsValidationLinkOutput2:
    """
    
            The design artifact and design instance associations which have needs validation
            status set as true on association is searched and returned.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    MdoLinkOutput: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.MDOOutput]
    """
            A list of Mdo0MDThread association which has mdo0NeedsValidation set to true
            on association.
            """
    MdiLinkOutput: list[MDInstanceData2]
    """
            A list of Mdo0MDInstance association which has mdo0NeedsValidation set to
            true on association.
            """

class NeedsValidationLinkResponse2:
    """
    Return structure for the operation.
    """
    def __init__(self, ) -> None: ...
    LinkQueryOutput: list[NeedsValidationLinkOutput2]
    """
            A list of output data which contains the design artifact and design instance associations
            with mdo0NeedsValidation status captured as true.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains any partial errors occurred during the operation."""

class UpdatedLinksOutput2:
    """
    
            The Mdo0MDThread, Mdo0MDInstance objects whose associations are updated
            will be returned.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    MdiObject: Teamcenter.Soa.Client.Model.Strong.Mdo0MDInstance
    """
            The Mdo0MDInstance object for which the mdo0IsValidated attribute on Mdo0HasInstanceAssociation
            object is updated to true.
            """
    MdoObject: Teamcenter.Soa.Client.Model.Strong.Mdo0MDThread
    """
            The Mdo0MDThread object for which the mdo0IsValidated attribute on Mdo0MDTAssociation
            object is updated to true.
            """

class UpdateLinkStatusToValidatedInput2:
    """
    Input structure for UpdateLinksToValidated2 operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    MdiDataForUpdate: MDInstanceData2
    """
            The input Mdo0MDInstance object and design instance objects for which Mdo0HasInstanceAssociation
            objects are identified and its mdo0IsValidated attribute is updated to true.
            """
    MdoDataForUpdate: Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.MDOOutput
    """
            The input Mdo0MDThread object and design artifact objects for which Mdo0MDTAssociation
            objects are identified and its mdo0IsValidated attribute is updated to true.
            """

class UpdateLinksToValidatedResponse2:
    """
    
            The Mdo0MDThread, Mdo0MDInstance objects whose associations are updated
            will be returned.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[UpdatedLinksOutput2]
    """
            A list of output data which contains the updated Mdo0MDThread and Mdo0MDInstance
            object.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains any partial errors occurred during the operation."""

class MultiDisciplinaryDataMgt:
    """
    Interface MultiDisciplinaryDataMgt
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def QueryNeedsValidationLink2(self, QueryInputs: list[NeedsValidationLinkInput2]) -> NeedsValidationLinkResponse2: ...
    def UpdateLinksToValidated2(self, Inputs: list[UpdateLinkStatusToValidatedInput2]) -> UpdateLinksToValidatedResponse2: ...

