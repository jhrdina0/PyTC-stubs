import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class NameAuthorizationList:
    """
    
            This structure holds the accessibility information for the given user and group combinations
            on the given applications or utilities.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[NameAuthorizationResponse]
    """
            A list of NameAuthorizationResponse objects one for each of the given application
            or utility.
            """
    PartialErrors: Teamcenter.Soa.Client.Model.ServiceData
    """
            Object that holds the partial errors that occurred while getting the accessibility
            on any of the given application or utility.
            """

class NameAuthorizationResponse:
    """
    
            This structure contains the name of the given application or utility, rule domain
            name and the derived verdict that indicates whether the user and group combination
            have accessibility on the application or utility or not.  True value for the verdict
            indicates the user have authorization access on the application or the utility. False
            value for the verdict indicates the user doesn't have authorization access on the
            application or the utility.
            
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Name of the application or the utility."""
    RuleDomain: str
    """Rule domain name."""
    Verdict: bool
    """Derived verdict for the given user and group combination on the application or utility."""

class NameInfo:
    """
    
            This structure contains the name of the application or utility and the rule domain
            that indicates whether the name is that of an application or that of a utility.
            
    """
    def __init__(self, ) -> None: ...
    Name: str
    """
            Name of an application or a utility whose accessibility for the given user need to
            be determined.
            """
    RuleDomain: str
    """The name of the rule domain. Valid rule domain  name is either Utility or Application."""

class Authorization:
    """
    Interface Authorization
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CheckAuthorization(self, User: Teamcenter.Soa.Client.Model.Strong.User, Group: Teamcenter.Soa.Client.Model.Strong.Group, InputNames: list[NameInfo]) -> NameAuthorizationList:
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

