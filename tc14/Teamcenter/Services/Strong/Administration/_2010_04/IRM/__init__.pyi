import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AccessorTypesResponse:
    """
    
            This structure contains the internal names and corresponding display values for all
            the Accessor Types in Teamcenter.
            
    """
    def __init__(self, ) -> None: ...
    AccessorTypeNameInfos: list[DisplayNameInfo]
    """
            List of DisplayNameInfo objects containing the internal name and corresponding display
            name for each of the Accessor Types in Teamcenter.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Object that holds any partial errors that occur while getting the display names of
            the Accessor Types in Teamcenter.
            """

class DisplayNameInfo:
    """
    
            DisplayNameInfo structure holds the internal name and corresponding display name
            of objects like privilege, named ACL, Accessor type and Accessor Id.
            
    """
    def __init__(self, ) -> None: ...
    InternalName: str
    """
            String representing the internal name of an access privilege or a named ACL or an
            accessor type or an accessor.
            """
    DisplayName: str
    """
            String representing the display name of an access privilege or a named ACL or an
            accessor type or an accessor.
            """

class ACLInfo:
    """
    
            Structure to hold the ACE information for a single row in the effective ACL table
            like granted privileges, revoked privileges, Accessor Type name, Accessor Id and
            the ACL name. This structure holds both internal names and corresponding display
            values for the names of Accessor Type, Named ACL, Privilege and Accessor ID that
            constitutes a single ACE.
            
    """
    def __init__(self, ) -> None: ...
    GrantedPrivsInfo: list[DisplayNameInfo]
    """
            A list of objects containing the internal and display names of the access privileges
            that are granted to the user on a given business object.
            """
    RevokedPrivsInfo: list[DisplayNameInfo]
    """
            A list of  objects containing the internal and display names of the access privileges
            that are revoked to the user on a given business object.
            """
    AccessorTypeNameInfo: DisplayNameInfo
    """
            Object containing the internal and display names of the accessor type in the ACE
            that is applicable to the given business object and to the user.
            """
    AccessorIdInfo: DisplayNameInfo
    """
            Object containing the internal and display names of the accessor id in the ACE that
            is applicable to the given business object and to the user.
            """
    AclNameInfo: DisplayNameInfo
    """
            Object containing the internal and display names of the ACL in the ACE that is applicable
            to the given business object and to the user.
            """

class ACLInfoResponse:
    """
    
            This structure holds the list of effective ACL reports for each of the given business
            objects.  Each effective ACL report contains the business object and corresponding
            effective ACL information.
            
    """
    def __init__(self, ) -> None: ...
    AclInfosList: list[ACLInfos]
    """List of derived Effective ACL reports for each of the given business objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Object that holds the partial errors that occurred while deriving the effective ACL
            information for any of the given business objects.
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
    WorkSpaceObject: Teamcenter.Soa.Client.Model.ModelObject
    """The business object for which effective ACL was derived."""
    AclInfos: list[ACLInfo]
    """
            List of ACE objects returned from the server that make up the effective ACL for the
            business object.
            """

class ExtraProtectionInfo:
    """
    
            This structure contains the derived extra protection information corresponding to
            a single access privilege on a given business object for the given user.
            
    """
    def __init__(self, ) -> None: ...
    PrivilegeNameInfo: DisplayNameInfo
    """Object that holds the internal name and display name of the access privilege."""
    Verdict: bool
    """The verdict for the privilege for the user on the object."""
    Rules: list[str]
    """A list of access rules evaluated to arrive at the verdict for the privilege."""
    RuleEvaluation: list[str]
    """
            A list of access rule arrangements involved in arriving at the verdict. Arrangements
            means the order in which the rules are evaluated.
            """
    AclNameInfo: DisplayNameInfo
    """
            Object that holds the internal and display names of the named ACL. For object ACLs
            the internal name is "OBJECT".
            """
    AccessorTypeNameInfo: DisplayNameInfo
    """
            Object that holds the internal and display names of the accessor type name corresponding
            to the ACE that involved in arriving at the privilege verdict.
            """
    AccessorIdInfo: DisplayNameInfo
    """
            Object that holds the internal and display names of the accessor Id  corresponding
            to the ACE that involved in arriving at the privilege verdict.
            """

class ExtraProtectionInfoReport:
    """
    
            This structure holds the business object and corresponding derived extra protection
            information for all the access privileges for the given user.
            
    """
    def __init__(self, ) -> None: ...
    WorkSpaceObject: Teamcenter.Soa.Client.Model.ModelObject
    """
POM_object on which extra protection information is derived for the given
            user.
            """
    ExtraProtectionInfos: list[ExtraProtectionInfo]
    """The derived extra protection information corresponding to the single business object."""

class ExtraProtectionInfoResponse:
    """
    
            This structure contains list of extra protection reports one for of each of the given
            business objects for the given user.
            
    """
    def __init__(self, ) -> None: ...
    ExtraProtectionReports: list[ExtraProtectionInfoReport]
    """List of extra protection report objects one for each of the given business objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Object that holds the partial errors occurred while deriving extra protection  information
            of any of the given business objects.
            """

class PrivNamesInfoResponse:
    """
    
            This structure holds the internal and display names of all the Teamcenter access
            privileges.
            
    """
    def __init__(self, ) -> None: ...
    PrivNameInfos: list[DisplayNameInfo]
    """
            A list of DisplayNameInfo objects that holds internal name and display names of each
            Teamcenter privilege objects.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Object that holds any of the partial errors that occurred while getting the display
            names of the privileges in Teamcenter. But in fact this operation will not result
            in any errors as it is returning the names of existing privileges. Scope for any
            errors is very less.
            """

class IRM:
    """
    Interface IRM
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAccessorTypes(self) -> AccessorTypesResponse:
        """    
             This operation can be used to get the names of all the Accessor Types in Teamcenter.
             Accessor Types are used to configure access privileges for different accessors in
             Access Control List (ACL) table in Access Manager Application. Examples for the Accessor
             Types are "World", "User", "Group", and "Role in Group".  For more information on
             the Accessor Types please refer to the Access Manager guide in Teamcenter documentation.
             The returned names from this operation will include both internal names and corresponding
             client locale specific localized display names of the Accessor Types.  The display
             names of the Accessor Types are used for displaying in the User Interface.  Whereas,
             the internal names of the Accessor Types are used for internal processing of the
             rule tree evaluation.
             

Use Cases:

             In general wherever the Accessor Type names need to be displayed this operation can
             be used. At present following use cases in Teamcenter Rich Application Client (RAC)
             calls this operation.
             


Display the Accessor Type names in Extra Protection information dialog.
             
Display the Accessor Type names in Effective ACL dialog.
             



Teamcenter Component:

             Entitlement - It Maps IRM SOA services to BMIDE.
             
        :return: 
        """
        ...
    def GetEffectiveACLInfo2(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> ACLInfoResponse:
        """    
             This operation can be used to get the effective Access Control List (ACL) information
             for a list of business objects.  Effective ACL information displays the Access Control
             Entries (ACEs) that are applicable to the business object with respect to the user
             for whom access privileges are being evaluated on the object. Applicable ACEs are
             picked up from the ACLs that are configured against the Access Manager Rules which
             are evaluated to true for the given business object based on details like the object's
             type, object's class, object attributes, object status and project to which it is
             assigned.  By looking at the effective ACL table end user will be able to understand
             what privileges or granted, what privileges are denied for the user on the object
             and, what ACL and Accessor Type are involved in either granting or denying a particular
             access privilege. For more information on ACLs, ACEs, effective ACLs please refer
             to the Access Manager guide in Teamcenter.
             

Use Cases:

             ACL list dialog in Teamcenter Rich Application Client (RAC) calls this operation
             to get the effective ACL information.
             

Teamcenter Component:

             Entitlement - It Maps IRM SOA services to BMIDE.
             
        :param Objects: 
                         List of business objects for which effective ACLs need to be derived.  The business
                         object can be any <b>POM_object</b> like <b>Item</b>, <b>ItemRevision</b> and <b>Dataset</b>.
             
        :return: 
        """
        ...
    def GetPrivilegeNames(self) -> PrivNamesInfoResponse:
        """    
             This operation can be used to get the internal names and corresponding display values
             of all the access privileges in Teamcenter.  The display names of the privileges
             are used to display the privilege names in the User Interface in client specific
             locale.  Whereas, the internal privilege names are used for internal processing of
             the rule tree evaluation. Below is the list of access privileges in Teamcenter release
             10.0. For functional information on each of these privileges please refer to the
             Access Manager guide in Teamcenter documentation.
             

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
             

Use Cases:

             This operation can be used in general wherever the privilege names need to be displayed.
             At present following use cases in Teamcenter Rich Application Client (RAC) calls
             this operation.
             


Display the privilege names in Access dialog.
             
Display the privilege names in Extra Protection information dialog.
             
Display the privilege names in effective Access Control List (ACL)
             dialog.
             
Display the privilege tool tips in Named ACL panel.
             



Teamcenter Component:

             Entitlement - It Maps IRM SOA services to BMIDE.
             
        :return: 
        """
        ...
    def GetExtraProtectionInfo2(self, User: Teamcenter.Soa.Client.Model.Strong.User, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> ExtraProtectionInfoResponse:
        """    
             This operation can be used to get the additional access protection information for
             a given user on a set of business objects.  Additional protection information can
             be used to understand what Named ACL, what Accessor and what AM rule path are involved
             in arriving at the verdict for an access privilege on a given object for the given
             user. This helps the user to understand why a particular privilege on the given object
             is granted or denied for the given user.  At present this information is displayed
             only in RAC client in the "Extra Protection Information" dialog.  This operation
             supports localization of privilege names, ACL names and Accessor type names.
             

Use Cases:

             "Extra Protection Information" dialog in Teamcenter Rich Application Client (RAC)
             calls this operation.
             

Teamcenter Component:

             Entitlement - It Maps IRM SOA services to BMIDE.
             
        :param User: 
                         Teamcenter user object for whom extra protection information on the given business
                         objects need to be derived.
             
        :param Objects: 
                         List of business objects on which Extra protection information need to be derived
                         for the given user. The business objects can be any <b>POM_objects</b> like <b>Item</b>,
                         <b>ItemRevision</b> and <b>Dataset</b>.
             
        :return: 
        """
        ...

