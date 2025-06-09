import System
import Teamcenter.Services.Strong.Administration._2006_03.IRM
import Teamcenter.Services.Strong.Administration._2007_01.UserManagement
import Teamcenter.Services.Strong.Administration._2007_06.Authorization
import Teamcenter.Services.Strong.Administration._2007_06.PreferenceManagement
import Teamcenter.Services.Strong.Administration._2008_03.IRM
import Teamcenter.Services.Strong.Administration._2010_04.DisciplineManagement
import Teamcenter.Services.Strong.Administration._2010_04.IRM
import Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement
import Teamcenter.Services.Strong.Administration._2012_09.UserManagement
import Teamcenter.Services.Strong.Administration._2012_10.IRM
import Teamcenter.Services.Strong.Administration._2014_10.UserManagement
import Teamcenter.Services.Strong.Administration._2015_03.UserManagement
import Teamcenter.Services.Strong.Administration._2015_07.UserManagement
import Teamcenter.Services.Strong.Administration._2016_03.UserManagement
import Teamcenter.Services.Strong.Administration._2016_10.UserManagement
import Teamcenter.Services.Strong.Administration._2017_05.GroupManagement
import Teamcenter.Services.Strong.Administration._2017_05.RoleManagement
import Teamcenter.Services.Strong.Administration._2017_05.UserManagement
import Teamcenter.Services.Strong.Administration._2018_11.IRM
import Teamcenter.Services.Strong.Administration._2018_11.OrganizationManagement
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class AuthorizationRestBindingStub(AuthorizationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CheckAuthorization(self, User: Teamcenter.Soa.Client.Model.Strong.User, Group: Teamcenter.Soa.Client.Model.Strong.Group, InputNames: list[Teamcenter.Services.Strong.Administration._2007_06.Authorization.NameInfo]) -> Teamcenter.Services.Strong.Administration._2007_06.Authorization.NameAuthorizationList: ...
    def CheckAuthorizationAccess(self, User: Teamcenter.Soa.Client.Model.Strong.User, Group: Teamcenter.Soa.Client.Model.Strong.Group, Role: Teamcenter.Soa.Client.Model.Strong.Role, InputNames: list[Teamcenter.Services.Strong.Administration._2007_06.Authorization.NameInfo]) -> Teamcenter.Services.Strong.Administration._2007_06.Authorization.NameAuthorizationList: ...

class AuthorizationService:
    """
    
            This service provides operations that are mainly used to accomplish authorization
            functionality related use cases.  Authorization functionality in Teamcenter enables
            administrators to configure rules that allow non system administration group members
            to access administration applications in authoring mode or run system administration
            utilities. Authorization rules can be configured on applications or utilities for
            individual groups or role-in-group accessors.  Users that belong to these configured
            groups or role-in-group accessors can then open an admin application in authoring
            mode or run an admin utility through command line. This service provides operations
            to accomplish following use cases.
            


Getting authorization rules for a set of accessors (Group and Role
            in the Group).
            
Setting authorization rules for a set of accessors (Group and Role
            in the Group).
            
Checking authorization for given user, group and role combination
            on given set of applications and utilities.
            
Checking authorization for given user and group combination on given
            set of applications and utilities.
            




Library Reference:

TcSoaAdministrationStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> AuthorizationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CheckAuthorization(self, User: Teamcenter.Soa.Client.Model.Strong.User, Group: Teamcenter.Soa.Client.Model.Strong.Group, InputNames: list[Teamcenter.Services.Strong.Administration._2007_06.Authorization.NameInfo]) -> Teamcenter.Services.Strong.Administration._2007_06.Authorization.NameAuthorizationList:
        """    
             This operation can be used to get authorization access on the given applications
             and utilities for the given user and group combination. Rule domain specifies accessibility
             need to be checked on an application or on a utility. Valid values for the domain
             are "utility" and "application".  If some other string is specified as rule domain
             this operation will return error code 290006.  However accessibility check
             for correct domain names will continue. Following are the valid application names
             and utility names for this operation. For more information on authorization rules
             please refer to Authorization guide in Teamcenter documentation.
             

List of application IDs:

             Organization
             
             Business_Modeler_IDE
             
             Access_Manager
             
             Archive_Restore
             
             Setup_Wizard
             
             Workflow_Designer
             
             PLMXML_Import_Export
             
             Project
             
             Subscription_Monitor
             
             Classification_Admin
             
             Report_Designer
             
             Application_Configuration
             
             EIntegrator_Admin
             
             Audit_Manager
             
             Authorization
             
             Schema_Editor
             
             Appearance_Configuration
             
             ADA License
             

List of utility IDs:

             data_share
             
             export_recovery
             
             database_verify
             
             update_project_data
             
             data_sync
             
             dsa_util
             
             import_export_business_rules
             
             purge_invalid_subscriptions
             
             create_change_types
             
             fsc_admin
             
             ada_util
             

Use Cases:

             To check user's accessibility
             


While opening an admin application.
             
While running an admin utility.
             



Teamcenter Component:

             Authorization - This component consists of the Client and Enterprise Tier code and
             constructs that support Authorization functionality including such things as the
             Rich Client Authorization Application plus SOA, ITK and Preferences.
             
        :param User: 
                         User object whose access on the given applications or utilities need to be determined.
             
        :param Group: 
                         The <b>Group</b> to which the user belongs to.
             
        :param InputNames: 
                         A list of NameInfo objects.
             
        :return: that indicates invalid rule
             domain value is given for the authorization rule will be returned by this operation
             if an invalid value is specified for the rule domain.
        """
        ...
    def CheckAuthorizationAccess(self, User: Teamcenter.Soa.Client.Model.Strong.User, Group: Teamcenter.Soa.Client.Model.Strong.Group, Role: Teamcenter.Soa.Client.Model.Strong.Role, InputNames: list[Teamcenter.Services.Strong.Administration._2007_06.Authorization.NameInfo]) -> Teamcenter.Services.Strong.Administration._2007_06.Authorization.NameAuthorizationList:
        """    
             This operation can be used to get authorization access on the given applications
             and utilities for the given user, group and role combination. Rule domain specifies
             accessibility need to be checked on an application or on a utility. Valid values
             for the domain are "utility" and "application".  If some other string is specified
             as rule domain this operation will return error code 290006.  However accessibility
             check for correct domain names will continue. Following are the valid application
             names and utility names for this operation. For more information on authorization
             rules please refer to Authorization guide in Teamcenter documentation.
             

List of application IDs:

             Organization
             
             Business_Modeler_IDE
             
             Access_Manager
             
             Archive_Restore
             
             Setup_Wizard
             
             Workflow_Designer
             
             PLMXML_Import_Export
             
             Project
             
             Subscription_Monitor
             
             Classification_Admin
             
             Report_Designer
             
             Application_Configuration
             
             EIntegrator_Admin
             
             Audit_Manager
             
             Authorization
             
             Schema_Editor
             
             Appearance_Configuration
             
             ADA License
             

List of utility IDs:

             data_share
             
             export_recovery
             
             database_verify
             
             update_project_data
             
             data_sync
             
             dsa_util
             
             import_export_business_rules
             
             purge_invalid_subscriptions
             
             create_change_types
             
             fsc_admin
             
             ada_util
             
             attribute_export
             

Use Cases:

             To check user's accessibility.
             


While opening an admin application.
             
While running an admin utility
             



Teamcenter Component:

             Authorization - This component consists of the Client and Enterprise Tier code and
             constructs that support Authorization functionality including such things as the
             Rich Client Authorization Application plus SOA, ITK and Preferences.
             
        :param User: 
                         User object whose access on the given applications or utilities need to be determined.
             
        :param Group: 
                         The <b>Group</b> to which the user belongs to.
             
        :param Role: 
<b>Role</b> in group to which the user belongs to.
             
        :param InputNames: 
                         A list of NameInfo objects.
             
        :return: that indicates invalid rule
             domain value is given for the authorization rule will be returned by this operation
             if an invalid value is specified for the rule domain.
        """
        ...

class DisciplineManagementRestBindingStub(DisciplineManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetDiscipline(self, DisciplineName: str) -> Teamcenter.Services.Strong.Administration._2010_04.DisciplineManagement.GetDisciplineResponse: ...

class DisciplineManagementService:
    """
    
            This service provides operations to manage Discipline objects in Organization application.
            Use cases include addition of new Discipline objects, modification of existing Discipline
            objects, and removal of existing Discipline objects. It also allows users to retrieve
            Discipline object information and find Discipline objects. It currently supports
            following operations:
            


Retrieve existing Discipline objects.
            




Library Reference:

TcSoaAdministrationStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DisciplineManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetDiscipline(self, DisciplineName: str) -> Teamcenter.Services.Strong.Administration._2010_04.DisciplineManagement.GetDisciplineResponse:
        """    
             This operation gets the Discipline object with given name. If no discipline
             object is found with the given name, the returned discipline object would be null.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param DisciplineName: 
                         This parameter specifies the name of the discipline object to be found.
             
        :return: in the ServiceData.
        """
        ...

class GroupManagementRestBindingStub(GroupManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def AddChildGroups(self, ChildGroupsToGroupStructs: list[Teamcenter.Services.Strong.Administration._2017_05.GroupManagement.AddChildGroupsToGroupStructure]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class GroupManagementService:
    """
    
            This service provides operations to manage Group business objects in an Organization
            application. The Group management functionality enables administrators to add groups
            to parent group.
            


Library Reference:

TcSoaAdministrationStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> GroupManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def AddChildGroups(self, ChildGroupsToGroupStructs: list[Teamcenter.Services.Strong.Administration._2017_05.GroupManagement.AddChildGroupsToGroupStructure]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Adds new groups and existing groups as child groups to specified Group objects.
             If groups are new, then they will be created first before they are added.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param ChildGroupsToGroupStructs: 
<b>Group</b> objects to be created and/or to be added to<b> </b>a <b>Group</b> object
                         as child groups.
             
        :return: 
        """
        ...

class IRMRestBindingStub(IRMService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CheckAccessorsPrivileges(self, GroupMember: Teamcenter.Soa.Client.Model.ModelObject, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], PrivilegeNames: list[str]) -> Teamcenter.Services.Strong.Administration._2006_03.IRM.CheckAccessorPrivilegesResponse: ...
    def GetEffectiveACLInfo(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Administration._2006_03.IRM.GetACLInfoResponse: ...
    def RemoveAccessor(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], AccessorType: str, AccessorId: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetPrivileges(self, PrivilegeSettings: list[Teamcenter.Services.Strong.Administration._2006_03.IRM.PrivilegeSettingInput], AccessorType: str, AccessorId: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetExtraProtectionInfo(self, User: Teamcenter.Soa.Client.Model.Strong.User, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Administration._2006_03.IRM.GetProtectionReportResponse: ...
    def ActivateUsers(self, ActivateUser: list[Teamcenter.Services.Strong.Administration._2008_03.IRM.ActivateUserInput]) -> Teamcenter.Services.Strong.Administration._2008_03.IRM.LicenseStatusResponse: ...
    def DeactivateUsers(self, DeactivateUser: list[Teamcenter.Services.Strong.Administration._2008_03.IRM.DeactivateUserInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetAccessorTypes(self) -> Teamcenter.Services.Strong.Administration._2010_04.IRM.AccessorTypesResponse: ...
    def GetEffectiveACLInfo2(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Administration._2010_04.IRM.ACLInfoResponse: ...
    def GetPrivilegeNames(self) -> Teamcenter.Services.Strong.Administration._2010_04.IRM.PrivNamesInfoResponse: ...
    def GetExtraProtectionInfo2(self, User: Teamcenter.Soa.Client.Model.Strong.User, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Administration._2010_04.IRM.ExtraProtectionInfoResponse: ...
    def GetAMImpactedObjects(self, FilterByIndexedStatus: bool) -> Teamcenter.Services.Strong.Administration._2012_10.IRM.AMImpactedObjectsResponse: ...
    def GetSessionValues(self) -> Teamcenter.Services.Strong.Administration._2012_10.IRM.GetSessionValuesResponse: ...
    def GetSessionInfoFromTicket(self, SessionInfoTicket: str) -> Teamcenter.Services.Strong.Administration._2018_11.IRM.GetSessionInfoFromTicketResponse: ...
    def GetSessionInfoTicket(self) -> Teamcenter.Services.Strong.Administration._2018_11.IRM.GetSessionInfoTicketResponse: ...

class IRMService:
    """
    
            This service provides operations that are mainly used to accomplish Access Manager
            related use cases.  Access Manager provides the functionality to configure site wide
            access control on the Teamcenter business data. Artifacts like Access Manager Conditions,
            Access Control Lists (ACLs), Access Control Entries (ACEs), Accessor Types and Access
            Privileges are used to configure the data access control in Access Manager.  Accessor
            Types and Privileges are also used to configure individual Object based access control.
            Access Manager Rules can be configured to control access on any POM_object.
            However Access Manager Rules are mostly applied for POM_application_objects
            such as Item, ItemRevision and Dataset in real time. Following
            are the use cases that are supported by the operations in this service.
            


Fetching Extra Protection details on a set of business objects for
            the given accessors.
            
Fetching effective ACL information on a set of business objects for
            the given accessors.
            
Fetching access privileges on a set of business objects for the given
            accessors.
            
Modifying the privileges or Access Control Entries (ACEs) on an object
            ACL or a Named ACL.
            
Getting the Named ACLs of different types. Teamcenter provides 3
            types of named ACLs.</br>1-Rule based ACLs - Used in AM rule configuration.</br>2-Work
            Flow ACLs - Used in Workflow tasks.</br>3-Project ACLs - Used to configure access
            on Project objects.
            
Getting list of Accessor Types.
            
Getting the access privilege names including both internal and display
            value.
            




Library Reference:

TcSoaAdministrationStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> IRMService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CheckAccessorsPrivileges(self, GroupMember: Teamcenter.Soa.Client.Model.ModelObject, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], PrivilegeNames: list[str]) -> Teamcenter.Services.Strong.Administration._2006_03.IRM.CheckAccessorPrivilegesResponse:
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
    def GetEffectiveACLInfo(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Administration._2006_03.IRM.GetACLInfoResponse:
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
    def SetPrivileges(self, PrivilegeSettings: list[Teamcenter.Services.Strong.Administration._2006_03.IRM.PrivilegeSettingInput], AccessorType: str, AccessorId: str) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def GetExtraProtectionInfo(self, User: Teamcenter.Soa.Client.Model.Strong.User, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Administration._2006_03.IRM.GetProtectionReportResponse:
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
    def ActivateUsers(self, ActivateUser: list[Teamcenter.Services.Strong.Administration._2008_03.IRM.ActivateUserInput]) -> Teamcenter.Services.Strong.Administration._2008_03.IRM.LicenseStatusResponse:
        """    
             This operation can be used to activate user(s) based on the number of allowed active
             author or consumer licenses. If not enough licenses are available, this operation
             will return corresponding error code for the given license level. This operation
             activates only the user and not the Group Members corresponding to the user.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param ActivateUser: 
                         A list of ActivateUserInput objects with user and license level to set.
             
        :return: 
        """
        ...
    def DeactivateUsers(self, DeactivateUser: list[Teamcenter.Services.Strong.Administration._2008_03.IRM.DeactivateUserInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deactivates given users and transfers ownership of the objects owned
             by the users to be deactivated to new users if the new users are specified. The users
             deactivated successfully are added in the updated object list of the service data.
             If new users and groups are specified to take the ownership of the objects owned
             by the deactivated users, then the new users and groups are added in the updated
             object list as well after ownership is successfully transferred. This operation requires
             system administration privilege.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param DeactivateUser: 
                         A list of users objects to be deactivated.
             
        :return: .
        """
        ...
    def GetAccessorTypes(self) -> Teamcenter.Services.Strong.Administration._2010_04.IRM.AccessorTypesResponse:
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
    def GetEffectiveACLInfo2(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Administration._2010_04.IRM.ACLInfoResponse:
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
    def GetPrivilegeNames(self) -> Teamcenter.Services.Strong.Administration._2010_04.IRM.PrivNamesInfoResponse:
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
    def GetExtraProtectionInfo2(self, User: Teamcenter.Soa.Client.Model.Strong.User, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Administration._2010_04.IRM.ExtraProtectionInfoResponse:
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
    def GetAMImpactedObjects(self, FilterByIndexedStatus: bool) -> Teamcenter.Services.Strong.Administration._2012_10.IRM.AMImpactedObjectsResponse:
        """    
             This operation lists the business objects whose read access is impacted by the changes
             in Access Manager (AM) rule tree. The rule tree changes considered are limited
             to those made after the previous call to this operation. This operation is usually
             called periodically and the objects whose read access privilege is modified due to
             the changes to AM rule tree between the previous call and the current one
             are determined and returned. Optionally, this operation returns the set of objects
             which is the intersection of objects impacted by AM rule changes and objects
             previously indexed. Previously indexed objects are stored in ACCT_TABLE table.
             
             AM rule configuration changes need re-login to refresh the in memory rule registry
             cache. Hence, until re-login after the AM rule changes, this operation will
             return ZERO objects.
             

Teamcenter Component:

             Entitlement - It Maps IRM SOA services to BMIDE.
             
        :param FilterByIndexedStatus: 
                         If true, only the objects previously indexed are included in the response
             
        :return: 
        """
        ...
    def GetSessionValues(self) -> Teamcenter.Services.Strong.Administration._2012_10.IRM.GetSessionValuesResponse:
        """    
             This operation gets all the session information in the form of key values map.  Each
             key corresponds to particular session attribute like user, roles, groups,
             project teams, and licenses.  For each entry in the keys array, the
             corresponding entry in the values array contains the values for that specific session
             attribute. Session information returned from this SOA operation is used during read
             expression evaluation in external clients to determine the READ privilege
             to the current logged in user on the indexed Teamcenter data.
             

Teamcenter Component:

             Entitlement - It Maps IRM SOA services to BMIDE.
             
        :return: 
        """
        ...
    def GetSessionInfoFromTicket(self, SessionInfoTicket: str) -> Teamcenter.Services.Strong.Administration._2018_11.IRM.GetSessionInfoFromTicketResponse:
        """    
             This operation gets all the session information in the form of key values map only
             if valid sessionInfoTicket is provided by client. Each key corresponds to particular
             session attribute like user, roles, groups, project teams, and licenses. For each
             entry in the keys array, the corresponding entry in the values array contains the
             values for that specific session attribute. Session information returned from this
             operation is used during read expression evaluation in external clients to determine
             the READ privilege to the current logged in user on the indexed Teamcenter data.
             

Use Cases:

             VDS (Visualization Data Server) has no user concept or connection authentication
             by design. TC SessionInfo passed to VDS clients after valid Teamcenter login but
             no validation is done by VDS today. Due to this shortcoming VDS is potential for
             spoofing, user session hacking and session reuse. To overcome this issue two new
             service operations are proposed and will be used. Calling client VDS uses getSessionInfoTicket
             operation to get encrypted (tamper proof) data packet and preserves the encrypted
             string. VDS calls SOA GetSessionInfoFromTicket with this ticket to get back the user
             session information. GetSessionInfoFromTicket returns back the session information
             only if the ticket is not expired.
             

Teamcenter Component:

             Entitlement - It Maps IRM SOA services to BMIDE.
             
        :param SessionInfoTicket: 
                         ticket
             
        :return: 
        """
        ...
    def GetSessionInfoTicket(self) -> Teamcenter.Services.Strong.Administration._2018_11.IRM.GetSessionInfoTicketResponse:
        """    
             This operation returns User, Group, Session Info, Site identifier and Ticket Expiry
             Time in the form of an encrypted string. Encrypted string ticket returned from this
             operation is used by getSessionInfoFromTicket operation to retrieve the session info.
             

Use Cases:

             VDS has no user concept or connection authentication by design. Teamcenter session
             information is passed to VDS clients after valid Teamcenter login but no validation
             is done by VDS today. Due to this shortcoming VDS is potential for spoofing, user
             session hacking and session reuse. To overcome this issue 2 new service operations
             are proposed and will be used. Calling client VDS uses getSessionInfoTicket to get
             encrypted (tamper proof) data packet and preserves the encrypted string. VDS client
             calls getSessionInfoFromTicket with this ticket to get back the user session information.
             getSessionInfoFromTicket returns back the session information only if the ticket
             is not expired and valid.
             

Teamcenter Component:

             Entitlement - It Maps IRM SOA services to BMIDE.
             
        :return: 
        """
        ...

class OrganizationManagementRestBindingStub(OrganizationManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetUserConsentStatement(self) -> Teamcenter.Services.Strong.Administration._2018_11.OrganizationManagement.UserConsentStatement: ...
    def RecordUserConsent(self, UserConsent: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class OrganizationManagementService:
    """
    
            This service provides operations to manage organization structure in Organization
            application. Use cases include addition of new groups and new roles, modification
            of existing groups and roles, removal of existing groups and roles. It also allows
            users to retrieve organization structure information such as organization structure,
            group information and role information for a user and groups with a specific role,
            etc. It currently supports following operation:
            


Retrieve group structure with a specific role.
            




Library Reference:

TcSoaAdministrationStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> OrganizationManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetUserConsentStatement(self) -> Teamcenter.Services.Strong.Administration._2018_11.OrganizationManagement.UserConsentStatement: ...
    def RecordUserConsent(self, UserConsent: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class PreferenceManagementRestBindingStub(PreferenceManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def SetPreferences(self, SetPrefInput: list[Teamcenter.Services.Strong.Administration._2007_06.PreferenceManagement.PreferencesSetInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def LockSitePreferences(self) -> bool: ...
    def UnlockSitePreferences(self) -> bool: ...
    def RefreshPreferences(self) -> bool: ...
    def DeletePreferenceDefinitions(self, PreferenceNames: list[str], DeleteAllCustomDefinitions: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeletePreferencesAtLocations(self, DeletePreferencesAtLocationIn: list[Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.PreferencesAtLocationIn]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetPreferences(self, PreferenceNames: list[str], IncludePreferenceDescriptions: bool) -> Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.GetPreferencesResponse: ...
    def GetPreferencesAtLocations(self, GetPreferenceAtLocationIn: list[Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.PreferencesAtLocationIn], IncludePreferenceDescriptions: bool) -> Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.GetPreferencesAtLocationsResponse: ...
    def ImportPreferencesAtLocationDryRun(self, ImportPreferences: Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.ImportPreferencesAtLocationDryRunIn) -> Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.ImportPreferencesAtLocationDryRunResponse: ...
    def ImportPreferencesAtLocations(self, ImportPreferenceIn: Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.ImportPreferencesAtLocationsIn) -> Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.PreferenceResponseWithFileTicket: ...
    def RemoveStalePreferenceInstancesAtLocations(self, Locations: list[Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.PreferenceLocation]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetPreferences2(self, PreferenceInput: list[Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.SetPreferences2In]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetPreferencesAtLocations(self, SetPreferenceIn: list[Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.SetPreferencesAtLocationsIn]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetPreferencesDefinition(self, PreferenceInput: list[Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.SetPreferencesDefinitionIn]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RefreshPreferences2(self, PreferenceNames: list[str], IncludePreferenceDescriptions: bool) -> Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.GetPreferencesResponse: ...

class PreferenceManagementService:
    """
    
            Contains PreferenceManagement Services
            


Library Reference:

TcSoaAdministrationStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> PreferenceManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def SetPreferences(self, SetPrefInput: list[Teamcenter.Services.Strong.Administration._2007_06.PreferenceManagement.PreferencesSetInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Sets the values for session or non-session preferences.
             

             Session preferences are preferences as seen from the current logged-in user.
             
             Non-session preferences are preferences that are normally not accessible to the current
             logged-in user.
             

             To set a non-session preference, a target object must be specified in the PreferencesSetInput structure. For user preferences, only the
             value of preference is stored in the database. The description of user preference
             is never stored in the database.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param SetPrefInput: 
                         Details of the preferences to be set.
             
        :return: Success is defined by the Partial Errors list in the service data object returned.
             Only Pass/Fail is returned in the error list. <br /><br />The error stack
             can contain the following error: <br /><ul><ul><li type="disc">1713:
             if the scope parameter of the <font face="courier" height="10">PreferencesSetInput</font>
             structure is set to "<b>SITE</b>" and an object is added to the structure.</li><li>1771:
             If one of the values is incompatible with a preference of type Integer.</li><li>1772:
             If one of the values is incompatible with a preference of type Double.</li><li>1773:
             If one of the values is incompatible with a preference of type Date.</li><li>1774:
             If one of the values is incompatible with a preference of type Logical.</li></ul></ul>
        """
        ...
    def LockSitePreferences(self) -> bool:
        """    
             Locks the Site preferences stored in the database.
             

             This can be used by system administrators only. It is not mandatory to lock Site
             preferences to make changes, but it ensures exclusive write accesses when necessary.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :return: 
        """
        ...
    def UnlockSitePreferences(self) -> bool:
        """    
             Releases the lock set on the site preferences stored in the database. The locking
             comes from the call to lockSitePreferences operation. Only the user who locked the
             site preferences is allowed to unlock them. As of Teamcenter 11.6, due to the re-architecture
             of preferences from XML storage to database objects, this operation is no longer
             required. So it is deprecated.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :return: 
        """
        ...
    def RefreshPreferences(self) -> bool:
        """    
             Refreshes the preference values stored in the server cache, so that they are synchronized
             with the latest values.
             

             This situation might happen when the preferences for a given user are being changed
             in 2 different sessions, or when an administrator is making changes to the Site /
             Role or Group preferences.
             
             <Calling the refreshPreferences operation will retrieve the updated values.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :return: 
        """
        ...
    def DeletePreferenceDefinitions(self, PreferenceNames: list[str], DeleteAllCustomDefinitions: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Deletes the definition and all value instances of the specified preferences.
             
             Since preferences will not be differentiated as Custom or COTS going forward, the
             input parameter deleteAllCustomDefinitions will not be used when performing this
             operation.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param PreferenceNames: 
                         The list of names for the preference definitions to delete.
             
        :param DeleteAllCustomDefinitions: 
                         Not used.
             
        :return: 
        """
        ...
    def DeletePreferencesAtLocations(self, DeletePreferencesAtLocationIn: list[Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.PreferencesAtLocationIn]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Deletes the given preference instances at the specified location only.
             
             This operation takes a list of PreferencesAtLocationIn
             structures representing the preferences to delete and the location.
             
             The location is a PreferenceLocation structure,
             which contains 2 mutually exclusive parameters:
             
             1. The location parameter, for which values can be for this specific operation:
             

"Site": The preference will be deleted from current site location.
             
"Group": The preference will be deleted for the group of the
             logged-in user.
             
"Role": The preference will be deleted for the role of the
             logged-in user.
             
"User": The preference will be deleted for the logged-in user.
             


             2. The object parameter, which represents the User, Role or Group
             where to delete the values. This is to be used when the target is for the non-logged-in
             user.
             

Use Cases:

             A preference instance is present at the user level, and it needs to be removed.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param DeletePreferencesAtLocationIn: 
                         A list of preferences at a given location.
             
        :return: 
        """
        ...
    def GetPreferences(self, PreferenceNames: list[str], IncludePreferenceDescriptions: bool) -> Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.GetPreferencesResponse:
        """    
             Retrieves the values for the preferences specified in the list of names, as seen
             by the current logged-in user, based on current application context. If there are
             no values in current application context, values are retrieved from default application
             context if exists.
             
             If the list is empty or its first value is equal to "*", all the preferences as seen
             by the logged-in user will be returned (not only the preference instances created
             by the logged-in user).
             

Use Cases:

             Retrieving the value for a series of preferences.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param PreferenceNames: 
                         If the list is empty or its first value is equal to "*", all the preferences visible
                         by the logged-in user will be returned (not only the preference instances created
                         by the logged-in user).
             
        :param IncludePreferenceDescriptions: 
                         Decides if the preference descriptions will be included in the response. Valid values
                         are true (descriptions are added) or false (no description). This offers flexibility
                         to decide the important information to the caller and reduce the size of the response
                         payload.
             
        :return: 
        """
        ...
    def GetPreferencesAtLocations(self, GetPreferenceAtLocationIn: list[Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.PreferencesAtLocationIn], IncludePreferenceDescriptions: bool) -> Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.GetPreferencesAtLocationsResponse:
        """    
             Retrieves the values for the specified preferences and locations.The input structure
             contains:
             
A vector preference names. If the list is empty or its first element is "*",
             all the preferences for the specified locations (and only for preference instances
             at this location) are being returned.
             
A PreferenceLocation  structure, which
             contains 2 mutually exclusive parameters:The location parameter, for which
             values can be for this specific operation:"Site": The
             preference will be retrieved either as overwritten or as an out-of-the-box (OOTB)
             value (whichever gives a value first).
             
"Group": The preference will be retrieved for the group of the logged-in
             user.
             
"Role": The preference will be retrieved for the role of the logged-in
             user.
             
"User": The preference will be retrieved for the logged-in user.
             


 The object parameter, which represents the User, Role
             or Group where to retrieve the values. This is to be used when the target
             is for the non-logged-in user.
             





Use Cases:

             1. The logged-in user needs to know the preference value given at her/his Role or
             Group level.
             
             2. The logged-in user needs to know the preference value given by another user, or
             a Role/Group than hers/his.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param GetPreferenceAtLocationIn: 
                         The desired list of preferences for a given location.
             
        :param IncludePreferenceDescriptions: 
                         Decides if the preference descriptions will be included in the response. Valid values
                         are true (descriptions are added) or false (no description). This offers flexibility
                         to decide the important information to the caller and reduce the size of the response
                         payload.
             
        :return: 
        """
        ...
    def ImportPreferencesAtLocationDryRun(self, ImportPreferences: Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.ImportPreferencesAtLocationDryRunIn) -> Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.ImportPreferencesAtLocationDryRunResponse:
        """    
             Pretends to import the preferences from the input file into the specified location.
             On the contrary to the import operation, the dry run operates on one location at
             a time. The objective is to gather information on what would be the final result
             for proceeding with the real import operation.  This operation takes a vector of
             structure representing the preferences and the location where to import. The valid
             values for the location parameter in the PreferenceLocation structure are: Site,
             Group, Role, User. The Site value means that the preference will be imported for
             the entire organization. Group or Role means that the value will be imported for
             the Group or Role of the current logged-in user. It is also possible to import for
             the non-current user.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param ImportPreferences: 
                         A structure that contains all the parameters for the import operation
             
        :return: 
        """
        ...
    def ImportPreferencesAtLocations(self, ImportPreferenceIn: Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.ImportPreferencesAtLocationsIn) -> Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.PreferenceResponseWithFileTicket:
        """    
             Imports the preferences from the input file into the specified locations.  This operation
             takes a vector of structure representing the preferences and the location where to
             import. The valid values for the location parameter in the PreferenceLocation structure
             are: Site, Group, Role, User. The Site value means that the preference will be imported
             for the entire organization. Group or Role means that the value will be imported
             for the Group or Role of the current logged-in user. It is also possible to import
             for the non-current user.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param ImportPreferenceIn: 
                         A structure that contains all the parameters for the import operation
             
        :return: A <font face="courier" height="10">PreferenceResponseWithFileTicket</font>
             structure, which contains:<ol><li>A file ticket to the report file (generated
             by the import operation) in the transient volume uploaded by the client. If the operation
             is called to import at several locations, all the report informations are gathered
             in the same file. </li><li>A ServiceData structure, which contains errors
             at indexes where errors have occurred. The following partial errors will be returned
             at the same index as the input structure:<ul type="circle"><li>1700:
             If the preference does not exist. </li><li>1725: If the logged-in user
             does not have the requested permission to carry-out the operation. </li><li>1751:
             If the specified object information does not correspond to any <b>User</b>,
             <b>Role</b> or <b>Group</b>. </li><li>1752: If
             both an object and a location are specified for an entry. </li><li>1753:
             if the specified location is invalid. </li></ol>
        """
        ...
    def RemoveStalePreferenceInstancesAtLocations(self, Locations: list[Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.PreferenceLocation]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Since the preference manager utility has a cleanup mode that does the same thing
             as removeStalePreferenceInstancesAtLocations-_2012_09-PreferenceManagementService.
             There is no need of a SOA operation to achieve this.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param Locations: 
                         The locations where to remove the stale preference instances.
             
        :return: structure, which will not contain
             any error.
        """
        ...
    def SetPreferences2(self, PreferenceInput: list[Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.SetPreferences2In]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Allows the logged-in user to set the values for the given preferences for the logged-in
             user.
             
             Values can only be given to preferences already defined in the system and for which
             the protection scope allows the user to give a value. Otherwise, the operation will
             return an error for this preference.
             
             Preference name and values are specified in input structure SetPreferences2In.
             


Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param PreferenceInput: 
                         A list of preference names and values.
             
        :return: 
        """
        ...
    def SetPreferencesAtLocations(self, SetPreferenceIn: list[Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.SetPreferencesAtLocationsIn]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Sets the values for the specified preferences and locations. The input
             PreferenceLocation structure (within the
             SetPreferencesAtLocationsIn structure) contains
             2 mutually exclusive parameters: The location parameter, for which values
             can be for this specific operation: "Site": The preference
             will be set for the entire organization.
             
"Group": the preference will be set for the group of the logged-in user.
             
"Role": The preference will be set for the role of the logged-in user.
             
"User": The preference will be set for the logged-in user.
             


 The object parameter, which represents the User, Role or Group
             where to set the values. This is to be used when the target is for the non-logged-in
             user. Note that the caller must have permission to set the preference values for
             the specified object.
             



Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param SetPreferenceIn: 
                         A list of preference definition, values and the location where to set the information.
             
        :return: 
        """
        ...
    def SetPreferencesDefinition(self, PreferenceInput: list[Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.SetPreferencesDefinitionIn]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Allows system administrators to create the definitions for new preferences, or to
             modify existing preference definitions. If the preferences do not exist, it sets
             the definitions and values for the specified preferences. If the preferences already
             exist (i.e. they have been defined already), it modifies them.
             

             This is a system administrator level operation. The intent is that only the system
             administrator should create a preference. However, this could be needed from non-directly-related
             user interactions. Therefore, the decision to make a call to this operation is delegated
             to its caller. This operation takes a list of SetPreferencesDefinitionIn
             structures, which contains a PreferenceDefinition
             structure. This structure can be simplified in case of preference modifications.
             

             Its parameters are:
             


category: The category where the preference is stored. If
             the input string is empty, the parameter will not be taken into account. However,
             in case the preference has not been created yet, it will be assumed that the preference
             will go under the "General" category. If the string is not empty, and if the category
             does not exists in the system already, new category would be created and the preference
             would go under this category.  
             




description: The textual explanation of what the preference
             does. If the input string is empty, the parameter will not be taken into account. 
             




type: The preference type. Valid values are:
             


                                     0:
             String preference.
             
                                     1:
             Logical preference.
             
                                     2:
             Integer preference.
             
                                     3:
             Double preference.
             
                                     4:
             Date preference.
             
                             If
             the preference does not exist, this piece of information will be needed. If the preference
             exists and if the value is provided and if a preference instance already exist with
             the old type and the conversion from the old type to the new one is not possible
             and an error would be returned. 
             


protectionScope: The level at which the preference is protected.
             Valid values are:                        
             


                                     "User":
             All users can provide a value for the preference.
             
                                     "Role":
             Only system and group administrators can provide a value.
             
                                     "Group":
             Only system and group administrators can provide a value.
             
                                     "Site":
             Only system administrators can provide a value.
             
                                     "System":
             Only system administrators can provide a value. Furthermore, the protection scope
             cannot be changed from then on. If the preference does not exist, this information
             is mandatory. If the preference exists and the protection scope string is empty,
             the parameter will not be taken into account. If the  preference exists and the protection
             scope string is not empty, the code will consider this to be a modification. 
             

isEnvEnabled: Status if the preference value can be set through
             an environment variable, in which case it will come from that location first. This
             piece of information will always be taken into consideration.
             




isOOTBPreference: Not used for this operation.
             



Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param PreferenceInput: 
                         A list of preference definitions.
             
        :return: 
        """
        ...
    def RefreshPreferences2(self, PreferenceNames: list[str], IncludePreferenceDescriptions: bool) -> Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.GetPreferencesResponse: ...

class RoleManagementRestBindingStub(RoleManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def AddRolesToGroup(self, RoleGroupStructs: list[Teamcenter.Services.Strong.Administration._2017_05.RoleManagement.AddRolesToGroupStructure]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RemoveRolesFromGroup(self, RoleGroupStructs: list[Teamcenter.Services.Strong.Administration._2017_05.RoleManagement.RoleGroupStructure]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class RoleManagementService:
    """
    
            This service provides operations to manage Role business objects in an Organization
            application. The Role management functionality enables administrators to create new
            roles, add or remove them from groups.
            


Library Reference:

TcSoaAdministrationStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> RoleManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def AddRolesToGroup(self, RoleGroupStructs: list[Teamcenter.Services.Strong.Administration._2017_05.RoleManagement.AddRolesToGroupStructure]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Adds new Roles and existing Roles to the specified Group objects. If the roles
             are new, it will create them first before they are added.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param RoleGroupStructs: 
                         A list of structures of <b>Role</b> object to be created and/or to be added to a
                         <b>Group</b> object.
             
        :return: 10182: The role name is used by another role.
        """
        ...
    def RemoveRolesFromGroup(self, RoleGroupStructs: list[Teamcenter.Services.Strong.Administration._2017_05.RoleManagement.RoleGroupStructure]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class UserManagementRestBindingStub(UserManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateDisciplines(self, Disciplines: list[Teamcenter.Services.Strong.Administration._2007_01.UserManagement.CreateDisciplinesIn]) -> Teamcenter.Services.Strong.Administration._2007_01.UserManagement.CreateDisciplinesResponse: ...
    def GetUserGroupMembers(self, InputObjects: list[Teamcenter.Services.Strong.Administration._2012_09.UserManagement.GetUserGroupMembersInputData]) -> Teamcenter.Services.Strong.Administration._2012_09.UserManagement.GetUserGroupMembersResponse: ...
    def SetGroupMemberProperties(self, InputObjects: list[Teamcenter.Services.Strong.Administration._2012_09.UserManagement.GroupMemberInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def MakeUser(self, Arguments: list[str], BatchFileFmsTicket: str, EnableStandardOutput: bool, EnableStandardError: bool) -> Teamcenter.Services.Strong.Administration._2014_10.UserManagement.MakeUserResponse: ...
    def SetUserProfileProperties(self, UserProfileInputs: list[Teamcenter.Services.Strong.Administration._2015_03.UserManagement.UserProfileProperties]) -> Teamcenter.Services.Strong.Administration._2015_03.UserManagement.UserProfilePropertiesResponse: ...
    def CreateOrUpdateUser(self, UserInputs: list[Teamcenter.Services.Strong.Administration._2015_07.UserManagement.CreateOrUpdateUserInputs]) -> Teamcenter.Services.Strong.Administration._2015_07.UserManagement.CreateOrUpdateUserResponse: ...
    def DeleteUser(self, UserInput: list[Teamcenter.Services.Strong.Administration._2016_03.UserManagement.DeleteUsersInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetCurrentCountryPageInfo(self) -> Teamcenter.Services.Strong.Administration._2016_10.UserManagement.GetCurrentCountryPageInfoResponse: ...
    def SaveAndValidateCurrentCountry(self, Selectedcountry: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def AddUsersAsGroupMembers(self, UserRoleGroupStructs: list[Teamcenter.Services.Strong.Administration._2017_05.UserManagement.AddUsersAsGroupMembersStructure]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RemoveGroupMembers(self, UserRoleGroupStructs: list[Teamcenter.Services.Strong.Administration._2017_05.UserManagement.UserRoleGroupStructure]) -> Teamcenter.Services.Strong.Administration._2017_05.UserManagement.UserManagementResponse: ...

class UserManagementService:
    """
    
            This service provides operations to manage User business objects and create
            Discipline objects in Organization application. The User management functionality
            enables administrators to create new users, modify existing users and delete users
            as well as retrieving user information. Discipline creation functionality allows
            system administrators to add new Discipline objects to the system. It currently supports
            following operation:
            


Create new Discipline objects.
            




Library Reference:

TcSoaAdministrationStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> UserManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateDisciplines(self, Disciplines: list[Teamcenter.Services.Strong.Administration._2007_01.UserManagement.CreateDisciplinesIn]) -> Teamcenter.Services.Strong.Administration._2007_01.UserManagement.CreateDisciplinesResponse:
        """    
             This operation creates a list of new Discipline objects based on the list
             of CreateDisciplineIn objects. If  parent group is specified in the CreateDisciplinesIn
             object, the discipline objects would be added into the group. This operation requires
             system administration or group administration privilege.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param Disciplines: 
                         A list of CreateDisciplinesIn objects to specify initial data for the new discipline
                         objects and parent group. A new discipline object is created for each CreateDisciplinesIn
                         object in the list.
             
        :return: .
        """
        ...
    def GetUserGroupMembers(self, InputObjects: list[Teamcenter.Services.Strong.Administration._2012_09.UserManagement.GetUserGroupMembersInputData]) -> Teamcenter.Services.Strong.Administration._2012_09.UserManagement.GetUserGroupMembersResponse:
        """    
             This operation retrieves information of all group members for a list of users specified
             in the list of GetUserGroupMembersInputData inputs. The information includes Group
             object, Role object, User object, status, group admin privilege, and default role
             flag of the user group members. The returned results could contain information only
             for the active group members of the user or both active and inactive group members
             of the user depending on option includeInactive setting in GetUserGroupMembersInputData.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param InputObjects: 
                         A list of GetUserGroupMembersInputData objects. Each GetUserGroupMembersInputData
                         specifies the specified matching User object and option flag to include inactive
                         group members.
             
        :return: A list of group member information for each requested User object. The following
             partial errors may be returned. - 10214 The source User object is null. - 10034 Fails
             to get  group members for a given user.
        """
        ...
    def SetGroupMemberProperties(self, InputObjects: list[Teamcenter.Services.Strong.Administration._2012_09.UserManagement.GroupMemberInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation updates the properties on one or more GroupMembers.The following properties
             may be updated: membership_data_source, ga,default_role, status.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param InputObjects: 
                         A list of GroupMember objects and the desired property values.
             
        :return: The modified GroupMember objects are returned in the Updated list of the ServiceData.
        """
        ...
    def MakeUser(self, Arguments: list[str], BatchFileFmsTicket: str, EnableStandardOutput: bool, EnableStandardError: bool) -> Teamcenter.Services.Strong.Administration._2014_10.UserManagement.MakeUserResponse:
        """    
             This operation executes the make_user utility on the Teamcenter server with the specified
             command line arguments and optional batch input file. The make_user utility runs
             with the same user and group as the current session user.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param Arguments: 
                         A list of command line arguments for the make_user utility. These arguments are specified
                         in the same format as in the make_user utility. All make_user command line arguments
                         are supported except "<i>-u=</i>", "<i>-p=</i>", "<i>-g=</i>", "<i>-pf=</i>" and
                         "<i>-file=</i>". If unsupported arguments are specified, they are ignored.
             
        :param BatchFileFmsTicket: 
                         FMS transient file ticket for a make_user batch input file. To run make_user with
                         a batch input file, the client must first upload the file to Teamcenter transient
                         volume using FMS, and pass the resulting FMS transient file ticket as this input
                         parameter. If the ticket is not empty, the file is passed to the make_user utility
                         using the <i>-file=file_path</i> argument.
             
        :param EnableStandardOutput: 
                         If true, the standard output from the make_user utility is returned as an FMS file
                         ticket. If false, the output is discarded.
             
        :param EnableStandardError: 
                         If true, the standard error output from the make_user utility is returned as an FMS
                         file ticket. If false, the error output is discarded.
             
        :return: 
        """
        ...
    def SetUserProfileProperties(self, UserProfileInputs: list[Teamcenter.Services.Strong.Administration._2015_03.UserManagement.UserProfileProperties]) -> Teamcenter.Services.Strong.Administration._2015_03.UserManagement.UserProfilePropertiesResponse:
        """    
             This operation sets the given properties on the Fnd0CustomUserProfile of the
             specified User. A new Fnd0CustomUserProfile object will be created
             if it does not already exist and the fnd0custom_user_profile property of the
             User will be set to the newly created Fnd0CustomUserProfile object.
             

Use Cases:

             Use Case 1: Set the properties for a User who does not have a Custom User Profile
             object.
             
             Use Case 2: Set the properties for a User who has a Custom User Profile object.
             


Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param UserProfileInputs: 
                         List of UserProfileProperties
             
        :return: 
        """
        ...
    def CreateOrUpdateUser(self, UserInputs: list[Teamcenter.Services.Strong.Administration._2015_07.UserManagement.CreateOrUpdateUserInputs]) -> Teamcenter.Services.Strong.Administration._2015_07.UserManagement.CreateOrUpdateUserResponse: ...
    def DeleteUser(self, UserInput: list[Teamcenter.Services.Strong.Administration._2016_03.UserManagement.DeleteUsersInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes User objects from Teamcenter. The objects owned by
             the user can be deleted or keep and transfer their ownership to a new user. This
             operation requires system administration privilege.
             

Use Cases:

             Use Case 1: Delete User with given user id.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param UserInput: 
                         List of Users that need to be deleted.
             
        :return: 
        """
        ...
    def GetCurrentCountryPageInfo(self) -> Teamcenter.Services.Strong.Administration._2016_10.UserManagement.GetCurrentCountryPageInfoResponse:
        """    
             This operation retrieves current configuration of country selection. The configuration
             is a list of selectable countries, the initial country to be displayed, and a customer
             configurable confidentiality statement.
             

Use Cases:

             This will be used for both RAC and AW to populate their current country selection
             pages.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :return: 
        """
        ...
    def SaveAndValidateCurrentCountry(self, Selectedcountry: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def AddUsersAsGroupMembers(self, UserRoleGroupStructs: list[Teamcenter.Services.Strong.Administration._2017_05.UserManagement.AddUsersAsGroupMembersStructure]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Adds new Users and existing Users as Group Members under the given Group objects
             with specific Role object. If a User is new, it will be created first
             before it is added as GroupMember. This operation requires system administration
             privilege or Group administration privilege. Specified Role objects must be
             an existing Role in the Group.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param UserRoleGroupStructs: 
                         A list of <b>User</b> objects and their <b>GroupMember</b> roles in the <b>Group</b>.
             
        :return: 10528:  Create user failed - This error is shown when there is a failure creating
             new user due to any internal errors. Administrator will have to look at system log
             in order to find the root cause of the error.
        """
        ...
    def RemoveGroupMembers(self, UserRoleGroupStructs: list[Teamcenter.Services.Strong.Administration._2017_05.UserManagement.UserRoleGroupStructure]) -> Teamcenter.Services.Strong.Administration._2017_05.UserManagement.UserManagementResponse:
        """    
             This operation removes group members for specified User objects under given
             Group objects with specified Role objects. This operation requires
             system administration privilege or group administration privilege. Input should not
             have null User, Group and Role objects.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param UserRoleGroupStructs: 
                         List of structures of <b>User</b> and associated <b>Role</b> and <b>Group</b> objects.
             
        :return: ) are NULL.
        """
        ...

