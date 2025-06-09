import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ACLInfo:
    """
    
            Structure to hold the ACE information for a single row in the effective ACL table
            like granted privileges, revoked privileges, Accessor Type name, Accessor Id and
            the ACL name.
            
    """
    def __init__(self, ) -> None: ...
    GrantedNames: list[str]
    """Names access privilege that are granted to the user on a given object."""
    RevokedNames: list[str]
    """Names access privilege that are revoked to the user on a given object."""
    AccessorType: str
    """
            The name of the accessor type in the ACE that is applicable to the given business
            object and to the user.
            """
    AccessorId: str
    """
            The name of the accessor id in the ACE that is applicable to the given business object
            and to the user.
            """
    NamedACL: str
    """
            The name of the name of the ACL in the ACE that is applicable to the given business
            object and to the user.  Name for the object ACL is "ORBJECT".
            """

class ACLInfos:
    """
    
            This structure holds the business object and corresponding effective ACL information
            derived through access rule evaluation.  Each effective ACL contains a list of ACE
            objects. Each ACE object is a single row in the effective ACL table that contains
            information like granted privileges, revoked privileges, Accessor Type name, Accessor
            Id and the ACL name.
            
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The business object for which effective ACL was derived."""
    AclInfos: list[ACLInfo]
    """
            List of ACE objects returned from the server that make up the effective ACL for the
            business object.
            """

class CheckAccessorPrivilegesResponse:
    """
    
            A list of privilegeReport objects for each of the given business objects and each
            given privilege. Each PrivilegeReport object contains the business object and verdicts
            for all the given privileges.
            
    """
    def __init__(self, ) -> None: ...
    PrivilegeReports: list[PrivilegeReport]
    """A list of PrivilegeReport objects one for each of the given business object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Object that holds the partial errors that resulted while determining the privileges
            on a business object through access rules evaluation.
            """

class GetACLInfoResponse:
    """
    
            This structure holds the list of effective ACL reports for each of the given business
            objects.  Each effective ACL report contains the business object and corresponding
            effective ACL information.
            
    """
    def __init__(self, ) -> None: ...
    AclInfoList: list[ACLInfos]
    """List of derived Effective ACL reports for each of the given business objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Object that holds the partial errors that occurred while getting the effective ACL
            information for any of the given business objects.
            """

class GetProtectionReportResponse:
    """
    
            This structure contains list of extra protection reports one for of each of the given
            business objects for the given user.
            
    """
    def __init__(self, ) -> None: ...
    ProtectionReports: list[ProtectionReport]
    """List of extra protection report objects one for each of the given business objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Object that holds the partial errors occurred while deriving extra protection  information
            of any of the given business objects.
            """

class Privilege:
    """
    
            This structure holds the name of the given privilege and its verdict that indicates
            if the privilege is granted or denied.
            
    """
    def __init__(self, ) -> None: ...
    PrivilegeName: str
    """The name of the access privilege."""
    Verdict: bool
    """Value true means the privilege is granted and false means the privilege is denied."""

class PrivilegeReport:
    """
    
            This structure holds the business object for which access privileges are successfully
            evaluated and corresponding privileges information. Privilege information includes
            the privilege name and corresponding verdict for each of the given privileges.
            
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """
            Business object on which access privileges are evaluated successfully  for the given
            groupMember.
            """
    PrivilegeInfos: list[Privilege]
    """
            A list of evaluated access privileges and corresponding verdicts for the given groupMember
            on the business object.
            """

class PrivilegeSettingInput:
    """
    
            This structure holds the object on which access privileges need to be modified and
            the sets of granted, denied and unset privileges for the given accessor type.
            
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """POM_application_object or a named ACL."""
    Grant: list[str]
    """A list of access privilege names that need to be granted."""
    Revoke: list[str]
    """A list of access privilege names that need to be denied."""
    Unset: list[str]
    """A list of access privilege names that need to be unset."""

class Protection:
    """
    
            This structure contains the derived extra protection information corresponding to
            a single access privilege on a given business object for the given user.
            
    """
    def __init__(self, ) -> None: ...
    Privilege: str
    """The name of the access privilege."""
    Verdict: bool
    """
            True or false. True means the privilege is granted and false means the privilege
            is denied.
            """
    Rules: list[str]
    """A list of access rules evalued to arrive at the verdict for the privilege."""
    RuleEvaluation: list[str]
    """A list of access rule arrangements involved in arriving at the verdict."""
    Acl: str
    """
            The name of the named ACL that is used to determine the verdict for this privilege.
            For object ACLs the name is "OBJECT".
            """
    AccessorType: str
    """
            The accessor type name corresponding to the ACE that involved in arriving at the
            privilege verdict.
            """
    AccessorId: str
    """The name of the accessor that is used in the ACE that is used to determine the privilege."""

class ProtectionReport:
    """
    
            This structure holds the business object and corresponding derived extra protection
            information for all the access privileges for the given user.
            
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """
POM_object on which extra protection information is derived for the given
            user.
            """
    Protections: list[Protection]
    """The derived extra protection information corresponding to the single business object."""

class IRM:
    """
    Interface IRM
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CheckAccessorsPrivileges(self, GroupMember: Teamcenter.Soa.Client.Model.ModelObject, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], PrivilegeNames: list[str]) -> CheckAccessorPrivilegesResponse:
        """    
             This operation gets the verdicts for the given access privileges for the given GroupMember
             on the given set of business objects.  This operation finds the accessors for the
             combination of given groupMember's user, role and group and then uses the list of
             found accessors to determine the verdicts for the given access privileges for the
             given GroupMember on the given business objects. The business objects can
             be any POM_object.  Privilege Names must be internal names of the Access
             Manager AM_Privilege objects.  If a privilege object with any of the
             given names does not exist in the system then this operation will return the error
             525101.  However, evaluation of the valid privilege names will continue. Following
             are the list of valid privilege names. For functional description about these privileges
             please refer to the Access Manager guide in Teamcenter documentation.
             

             ADD_CONTENT
             
             ASSIGN_TO_PROJECT
             
             Administer_ADA_Licenses
             
             BATCH_PRINT
             
             CHANGE
             
             CHANGE_OWNER
             
             CICO
             
             COPY
             
             DELETE
             
             DEMOTE
             
             DIGITAL_SIGN
             
             EXPORT
             
             IMPORT
             
             IP_ADMIN
             
             IP_Classifier
             
             ITAR_ADMIN
             
             ITAR_Classifier
             
             MARKUP
             
             PROMOTE
             
             PUBLISH
             
             READ
             
             REMOTE_CICO
             
             REMOVE_CONTENT
             
             REMOVE_FROM_PROJECT
             
             SUBSCRIBE
             
             TRANSFER_IN
             
             TRANSFER_OUT
             
             TRANSLATION
             
             UNMANAGE
             
             WRITE
             
             WRITE_ICOS
             

Teamcenter Component:

             Entitlement - It Maps IRM SOA services to BMIDE.
             
        :param GroupMember: 
                         The <b>GroupMember</b> whose access privileges on the given business objects need
                         to be determined.
             
        :param Objects: 
                         The list of business objects on which access privileges are being evaluated for the
                         given groupMember. The business object can be any <b>POM_object</b>.
             
        :param PrivilegeNames: 
                         This is a list of valid Access Manager   privilege names whose verdicts for the given
                         groupMember on the given business objects need to be determined. The privilege names
                         must be the internal names.
             
        :return: is returned
             for invalid privilege name, while the remaining privileges are evaluated.
        """
        ...
    def GetEffectiveACLInfo(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetACLInfoResponse:
        """    
             This operation can be used to get the effective Access Control List (ACL) information.
             Effective ACL information displays the Access Control Entries (ACEs) that are applicable
             to the business object with respect to the user for whom access privileges are being
             evaluated on the object. Applicable ACEs are picked up from the ACLs that are configured
             against the Access Manager Rules which are evaluated to true for the given object
             based on the object's type, class, attributes, status and project to which it is
             assigned to etc.  By looking at the effective ACL table end user will be able to
             understand what privileges or granted, what privileges are denied for the user on
             the object and, what ACL and Accessor Type are involved in either granting or denying
             a particular access privilege. This operation can be used to get all the information
             required to render the effective ACL table. Limitation with this operation is it
             does not support localization. Hence all the strings returned by this or internal
             values. For more information on ACLs, ACEs, effective ACLs please refer to the Access
             Manager guide in Teamcenter.
             

Use Cases:

             ACL list dialog in Teamcenter Rich Application Client (RAC) used to call this operation
             to get the effective ACL information before it was replaced with the new operation
             getEffectiveACLInfo2 that supports localization of ACL names, Accessor type names
             and privilege names.
             

Teamcenter Component:

             Entitlement - It Maps IRM SOA services to BMIDE.
             
        :param Objects: 
                         List of business objects for which effective ACLs need to be derived. The business
                         object can be any <b>POM_object</b> like <b>Item</b>, <b>ItemRevision</b> and <b>Dataset.</b>

        :return: 
        """
        ...
    def RemoveAccessor(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], AccessorType: str, AccessorId: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation removes the specified accessors from the given objects. Objects in
             the given list can be either AM_ACL (named Access Control List) objects or
             POM_application_object. If the object is a named ACL then the Access Control
             Entry (ACE)  from the named ACL is removed.  If the object is a POM_application_object
             then object ACL entry with the specified accessor type and accessor id is removed.
             Objects on which given accessor is removed successfully are returned in the updated
             list of the ServiceData.  Objects on which accessor removal resulted in an error
             are returned in the list of failures in the ServiceData.  Invalid accessor type and
             accessor ID will result in error code 525120.
             

Use Cases:

             Modifying a Named ACL or removing an object ACL from Teamcenter Rich Application
             Client (RAC) calls this operation.
             

Teamcenter Component:

             Entitlement - It Maps IRM SOA services to BMIDE.
             
        :param Objects: 
                         List of named ACLs or <b>POM_objects</b> from which the access control entry with
                         specified accessor type and accessor id need to be removed.
             
        :param AccessorType: 
                         Name of the accessor type in the ACE that need to be removed.
             
        :param AccessorId: 
                         Name of the accessor ID in the ACE that need to be removed.  Accessor ID is basically
                         argument value to the accessor type. Not all accessor types have argument value.
                         Hence, accessor id can be null.
             
        :return: .
        """
        ...
    def SetPrivileges(self, PrivilegeSettings: list[PrivilegeSettingInput], AccessorType: str, AccessorId: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation can be used to grant or deny a set of privileges to the specified
             accessor type and accessor id on the given object.  Either a named Access Control
             List (ACL) or a POM_application_object can be submitted as input to this operation.
             If the object is a POM_application_object then an object ACL will be added
             on the object. If the object is a named ACL then an ACE entry is either modified
             or added to the named ACL. For invalid Accessor type and Accessor Id this operation
             will return the error 525101.
             

Use Cases:


Updating named ACL objects by either modifying existing ACE entries
             or by adding new ACE entries for the specified accessor.
             
Adding new object ACLs on a POM_application_object for the
             specified accesor.
             



Teamcenter Component:

             Entitlement - It Maps IRM SOA services to BMIDE.
             
        :param PrivilegeSettings: 
                         A list of PrivilegeSettingInput objects one for each of the given objects on which
                         privileges need to be modified.
             
        :param AccessorType: 
                         The name of the accessor type for which privileges need to be modified.
             
        :param AccessorId: 
                         The argument value to the accessor type. Not all accessor types take argument value.
                         Hence, accessor id can be null.
             
        :return: 
        """
        ...
    def GetExtraProtectionInfo(self, User: Teamcenter.Soa.Client.Model.Strong.User, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetProtectionReportResponse:
        """    
             This operation can be used to get the additional access protection information for
             a given user on a set of business objects.  Additional protection information can
             be used to understand what Named ACL, what Accessor and what AM rule path are involved
             in arriving at the verdict for an access privilege on a given object for the given
             user. This helps the user to understand why a particular privilege on the given object
             is granted or denied for the given user.  This operation does not support localization.
             Hence all the strings returned by this operation are internal values.  This operation
             is replaced by a new operation getExtraProtectionInfo2 that supports localization.
             

Use Cases:

             Extra Protection Information dialog in Teamcenter Rich Application Client (RAC) used
             to call this operation before it was replaced with the new operation getExtraProtectionInfo2
             that supports localization.
             

Teamcenter Component:

             Entitlement - It Maps IRM SOA services to BMIDE.
             
        :param User: 
                         List of business objects on which Extra protection information need to be derived
                         for the given user. The business objects can be any <b>POM_objects</b> like <b>Item</b>,
                         <b>ItemRevision</b> and <b>Dataset</b>.
             
        :param Objects: 
                         Teamcenter user object for whom extra protection information on the given business
                         objects need to be derived.
             
        :return: 
        """
        ...

