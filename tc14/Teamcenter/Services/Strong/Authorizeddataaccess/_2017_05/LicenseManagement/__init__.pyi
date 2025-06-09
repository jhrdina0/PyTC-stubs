import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class LicenseInputDetails:
    """
    
            A Structure containing list of selected licenses and objects with the ead paragraph
            if there is any.
            
    """
    def __init__(self, ) -> None: ...
    SelectedLicenses: list[str]
    """
            List of license IDs of ADA licenses. These are strings of each with a maximum of
            128 bytes size.
            """
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            List of WorkspaceObject business objects to be either attached or detached
            from selected list of Licenses
            """
    EadParagraph: list[str]
    """
            List of authorizing paragraphs for the licenses being attached to WorkspaceObject
            business objects. These are strings with a maximum of 80 bytes size. The size of
            eadParagraph vector should match the size of the selectedLicenses (each entry in
            eadParagraph maps to corresponding entry in selectedLicenses). If a paragraph entry
            is not applicable for a specific license (paragraph entries are applicable only for
            licenses of ITAR type), then that entry can be left blank. System will ignore any
            paragraph entry if it is not applicable for a license to be attached. This is an
            optional parameter.
            """

class PropagationConfigurationContext:
    """
    
            PropagationConfigurationContext contains data which can be applied to attach to projects
            and detach from license operation.
            
    """
    def __init__(self, ) -> None: ...
    SelectedTopLevelObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Selected top level object in context of ACE ( Active Content Expericence ), if this
            object is passed we will fetch variant rule and revision rule.
            """
    VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule
    """

            The VariantRule in context of the assign to project  or attach to license operation.
            """
    RevisionRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """The RevisionRule associated with the assign to project or attach to license operation."""
    TypeOption: int
    """
            An integer indicating the type of Item or Item Revision, valid values are 0 for Item
            and 1 for Item Revision.
            """
    Depth: int
    """
            A number indicating how deep the traversal needs to be performed for a given structure,
            applicable only for structures.
            """

class LicenseAttachOrDetachInput:
    """
    
            A structure containing license to be attached or removed and propagation context
            information.
            
    """
    def __init__(self, ) -> None: ...
    AttachLicenseDetails: LicenseInputDetails
    """Structure containing data for attach license operation."""
    DetachLicenseDetails: LicenseInputDetails
    """Structure containing data for detach license operation."""
    ContextInfo: PropagationConfigurationContext
    """A structure of PropagationConfigurationContext."""
    ProcessAsynchronously: bool
    """
            Flag indicating if this operation needs to be processed in asynchronously. A value
            True means to process it asynchronously. If the value is not set or is set to False
            then processing happens synchronously in the same request.
            """

class LicenseManagement:
    """
    Interface LicenseManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AttachOrDetachLicensesFromObjects(self, LicenseAttachOrDetachInput: list[LicenseAttachOrDetachInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation attaches or detaches ADA_License objects to WorkspaceObject
             objects such as Item, ItemRevision, Dataset, etc. as specified
             in each LicenseAttachOrDetachInput. Optionally, this operation can set/update authorizing
             paragraph information for the ITAR licenses being attached. Users performing this
             operation will need IP_ADMIN privilege to both the workspace objects and the licenses
             being attached, if the licenses are of type IP or Exclude, while ITAR_ADMIN privilege
             is needed to both the workspace objects and the licenses being attached, if the licenses
             are of ITAR license type. If the user does not have necessary privilege to attach
             any licenses, or if there is any other error while attaching licenses, the errors
             are returned as partial errors in ServiceData.
             

Use Cases:


You can attach ADA_License business objects to classified
             WorkspaceObject business objects to grant access for users and/or groups listed on
             the licenses in context of structure configuration.
             
You can remove ADA_License business objects from classified
             WorkspaceObject business objects to revoke access for users and/or groups listed
             on the licenses in context of structure configuration.
             



Teamcenter Component:

             Authorized Data Access - Authorized Data Access (ADA) is a security solution that
             complements Access Manager rules to control access to sensitive data through the
             use of data classification, user clearance, and time bound authorizing documents
             (ADA Licenses).
             
        :param LicenseAttachOrDetachInput: 
                         A list containing attachOrDetachLicensesFromObjects.
             
        :return: 
        """
        ...

