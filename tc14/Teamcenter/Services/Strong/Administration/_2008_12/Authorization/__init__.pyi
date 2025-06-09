import System
import Teamcenter.Services.Strong.Administration._2007_06.Authorization
import Teamcenter.Soa.Client.Model.Strong
import typing

class Authorization:
    """
    Interface Authorization
    """
    def __init__(self , *args: typing.Any) -> None: ...
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

