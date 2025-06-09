import System
import Teamcenter.Soa.Client.Model
import typing

class CallToRemoteSiteResponse:
    """
    CallToRemoteSiteResponse
    """
    def __init__(self, ) -> None: ...
    MsgIDs: list[str]
    """msgIDs"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""

class NamesAndValues:
    """
    The NamesAndValues structure represents a generic name-value pair.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the session option."""
    Value: str
    """The value of the session option."""

class OwningSiteAndObjs:
    """
    Vector of object and it's owning site. These objects need to be remote imported
    """
    def __init__(self, ) -> None: ...
    OwningSiteId: int
    """owningSiteId"""
    Objs: list[Teamcenter.Soa.Client.Model.ModelObject]
    """objs"""

class ImportExport:
    """
    Interface ImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetRemoteSites(self, SiteType: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation returns a list of sites registered for the requested type of transfer.
             

Teamcenter Component:

             TcXMLimportexportengine - Capability to import and export XML that follows the TC
             Business Object Model. No hardcoded transformation is done. Transformations when
             needed are supported by the mapper component
             
        :param SiteType: 
<ul>
<li type="disc"> Offline       GMS Sites participating in briefcase transfer
                         </li>
</ul>

        :return: List of sites of particular type is returned in the plain list of the ServiceData.
        """
        ...
    def RequestExportToRemoteSites(self, Reason: str, Sites: list[Teamcenter.Soa.Client.Model.ModelObject], Objects: list[Teamcenter.Soa.Client.Model.ModelObject], OptionSet: Teamcenter.Soa.Client.Model.ModelObject, OptionNameAndValues: list[NamesAndValues], SessionOptionNamesAndValues: list[NamesAndValues]) -> CallToRemoteSiteResponse:
        """    
             This operation exports objects to specified sites using Global Multisite.
             

Use Cases:

             This operation gets invoked from RAC when user does following actions from Navigator
             or structure manager
             
             1>    Tools->Export->To Remote Site Via Global Services.
             
             2>    Tools->Export->To PDX
             
             3>    Tools->Export->To Briefcase
             


Teamcenter Component:

             TcXMLimportexportengine - Capability to import and export XML that follows the TC
             Business Object Model. No hardcoded transformation is done. Transformations when
             needed are supported by the mapper component
             
        :param Reason: 
                         The reason for remote export. This has limit of 240.
             
        :param Sites: 
                         A list of sites to which object(s) need to be exported.
             
        :param Objects: 
                         Objects to be exported
             
        :param OptionSet: 
                         A reference to <b>TransferOptionSet</b> object which is selected by the user. This
                         object holds the list of options and their default values which can influence the
                         contents of the exported briefcase or PDX or on-line export.
             
        :param OptionNameAndValues: 
                         This is the list of options and values that user has overridden from the <b>TransferOptionSet</b>
                         object specified above. E.g option name 'opt_all_ds_files' (Export all dataset files)
                         has default value as True in Transfer option set. If use does not want to export
                         all dataset he can override it to false.
             
        :param SessionOptionNamesAndValues: 
                         This is the list of session options and values (options which are not part of the
                         option set). E.g 1) If user wants to run export in dry run mode then session option
                         'dry_run' needs to be specified and its value should be 'True'. 2)If user wants to
                         export unconfigured variants then 'processUnconfiguredVariants' should be set to
                         'True'.
             
        :return: 
        """
        ...
    def RequestImportFromRemoteSites(self, Reason: str, OwningSitesAndObjs: list[OwningSiteAndObjs], OptionSet: Teamcenter.Soa.Client.Model.ModelObject, OptionNamesAndValues: list[NamesAndValues], SessionOptionNamesAndValues: list[NamesAndValues]) -> CallToRemoteSiteResponse:
        """    
             This operation imports objects to specified sites using Global Multisite.
             

Use Cases:

             This operation is not in use.
             

Teamcenter Component:

             TcXMLimportexportengine - Capability to import and export XML that follows the TC
             Business Object Model. No hardcoded transformation is done. Transformations when
             needed are supported by the mapper component
             
        :param Reason: 
                         The reason of Import. This has limit of 240 characters.
             
        :param OwningSitesAndObjs: 
                         A list of owning site and corresponding objects that need to be imported.
             
        :param OptionSet: 
                         A reference to <b>TransferOptionSet</b> object which is selected by the user. This
                         object holds the list of options and their default values which can influence the
                         result of import.
             
        :param OptionNamesAndValues: 
                         This is the list of options and values that user has overridden from the <b>TransferOptionSet</b>
                         object specified above.
             
        :param SessionOptionNamesAndValues: 
                         This is the list of session options and values (options which are not part of the
                         option set).
             
        :return: 
        """
        ...

