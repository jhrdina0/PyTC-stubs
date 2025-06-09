import System
import Teamcenter.Soa.Client.Model
import typing

class ImportExportOptionsInfo:
    """
    
The ImportExportOptionsInfo structure holds the name-value pairs of
import/export
option(s). Value can be single or multiple valued. The import/export options
influence
the business object import/export and has default value.
    """
    def __init__(self, ) -> None: ...
    OptionName: str
    """
            The name of the option. Valid values are as per below table.
            

            Supported ImportExportOptionsInfo options:
            

                          Option
            Name                
            Description                                                            
            Default value
            
            opt_exp_prot_obj        Set this option to False so process will stop when exporting
            import
            
            or export protected workspace objects.
            False
            
            opt_do_struct           Set this option to TRUE to Transfer site ownership of the
            Top-Level
            
            item only and export all components with no site ownership
            transfer.
            
            Applicable only if transfer_ownership is true.
            False
            
            opt_trans_prot_comp     Set this option to TRUE to exclude all components that have
            no
            
            TRANSFER_OUT/TRANSFER_IN privilege at owning site
            
            for site ownership transfer.
            
            Applicable only if transfer_ownership is true.
            False
            
            opt_exp_prot_comp       Set this option to TRUE to exclude all components that have
            no export
            
            and/or import privileges granted at the owning site.
            False
            
                    
            
            opt_entire_bom             Set
            this option to TRUE to export all components if the item selected is an assembly.
                 False
            
            opt_all_ds_files         Set this option
            to TRUE to export all dataset files.                                    
            True
            
            opt_all_ds_vers         Set this option to
            TRUE to export all dataset versions                                     
            True
            
            opt_folder_contents     Set this option to TRUE to export objects
            in folder.                                     
            False
            
            opt_de_rlz_item         Set this option to
            TRUE to send BOM structure and CPD structure together                 
            False
            
            opt_workset_rlz_de         Set this option
            to TRUE to send Design Element with Workset and subset                     
            False
            
            opt_cpd_p2s_skip         Set this option
            to True to exclude all Reference Geometry/Connected Element
            
                                    relations
            from Cpd0DesignElement.                                                        
            True
            
            transfer_ownership      Set this option to True to transfer site
            ownership of selected objects.                    
            False
            
            owning_user                Set
            the owning user for objects at remote site                                            
            None
            
            owning_group            Set
            the owning group for objects at the remote site                                        
            None
            
            include_modified_only     Include only objects that have been
            modified since the last transfer are exported.
            
                                    Mutually
            exclusive with the  transfer_ownership option.                                
            False
            
            include_relations       List of relations which will be included
            in export.
            
                                    The
            relation must be passed by Teamcenter relation name
            
                                    and
            be supported for include processing by the option set.                                
            None
            
            exclude_relations        List of relations
            which will be excluded in export.
            
                                    The
            relation must be passed by Teamcenter relation name
            
                                    and
            be supported for exclude processing by the option set.                                
            None
            
                    
            

            Item Options, only one may be passed.
            
            Option Name                            
            Description                                                                                                                                    
            Value(s)
            
            opt_rev_select                         
            Process all revisions.                                                                                                                         
            allItemRevisions
            
            opt_rev_select                            
            Process only the latest revision regardless of release status.                                                                    
            latestRevisionOnly
            
            opt_rev_select                         
            Process only the latest revision regardless of release status.                                                                    
            latestWorkingRevisionOnly
            
            opt_rev_select                         
            Process only the latest working revision. If there is none, then process the latest
            released                                
            latestWorkingAnyOnly
            
            opt_rev_select                         
            Process only the latest released revision.                                                                                                
            latestReleasedRevisionOnly
            
            opt_rev_select                         
            Process only the selected revision. Applicable only if an ItemRevision is the target.                                        
            selectedRevisionsOnly
            
            opt_rev_select                         
            Process only revisions with a specific release status. Supported release statuses
            are defined in the option set.       First value=specificStatusOnly
            Second value=Release Status Name
            """
    OptionValue: list[str]
    """A list of values for the optionName."""

class RemoteExportFailurePerOperation:
    """
    Returns failures from all sites during export of objects.
    """
    def __init__(self, ) -> None: ...
    Sites: list[str]
    """A list of sites by name for this operation."""
    FailuresPerOperation: list[RemoteExportFailurePerSite]
    """A list of failure information from sites."""

class RemoteExportFailurePerSite:
    """
    
This structure returns failures encountered during export to a site.

The following errors may be returned in the RemoteExportFailurePerSite
structure.

96001 - The bulk "Iman Export Record" (IXR) creation or update has failed during
the TC XML based multisite operation.

96002 - The "Export Commit" process has failed during the TC XML based multisite
operation.

96003 - The processing callback function is not set for the TC XML based
multisite
operation.

96004 - The "Export Record" could not be created during the TC XML based
multisite
operation.

96005 - The "Export Record" could not be created during the TC XML based
multisite
operation due to an invalid value for the attribute

96023 - An error has been encountered during the access of the volume during the
TC XML based operation.

96024 - An invalid input data was found while updating the fast synchronization
tables
during the TC XML based operation. Please refer to the log files for details.

96025 - The save of "Iman Export Record" (IXR) has encountered partial errors
during
the TC XML based multisite operation. Please refer to the log files for details.

96026 - The conversion of the input parameters of the utility to its
representative
Option Set has failed.

    """
    def __init__(self, ) -> None: ...
    FailureCodes: list[int]
    """A list of failure codes for this operation."""
    FailureObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of objects that have failed to export."""
    FailureStrings: list[str]
    """A list of error strings for this operation."""

class RemoteExportInfo:
    """
    
The RemoteExportInfo structure takes an option set name and export options as
input.
The option set and options will affect the final state of the exported objects
at
the target sites. There is system default option set and additional option sets
may
be created by the administrator.  When the option set and options are not
specified
in the RemoteExportInfo structure, the system default option set and default
options
will be used.
    """
    def __init__(self, ) -> None: ...
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of target objects."""
    TargetSites: list[str]
    """A list of target sites by site name."""
    OptionSetName: str
    """Name of option set used for export."""
    Reason: str
    """The reason for export. It may be empty."""
    ExportOptions: list[ImportExportOptionsInfo]
    """A list of export options."""

class RemoteExportResponse:
    """
    
The RemoteExportResponse returns detailed partial failure information in
RemoteExportFailurePerOperation
structures along with a ServiceData.

This operation can return errors from different sites and each target object may
have different errors. The RemoteExportFailurePerOperation structure will be
used
to report failures instead of the ServiceData to allow for the detailed
reporting
of site specific errors.  The RemoteExportFailurePerOperation structure will
report
what which site the errors are returned from. The list
RemoteExportFailurePerSite
structures will return errors for a specific target object(s).

    """
    def __init__(self, ) -> None: ...
    FailureInfo: list[RemoteExportFailurePerOperation]
    """The partial failure information specfic to site."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The Service Data return. The objects sucessfully exported are added to the Plain
            objects list.
            """

class RemoteImportFailurePerOperation:
    """
    This structure returns all the failures during import for a set of objects
    """
    def __init__(self, ) -> None: ...
    Sites: list[str]
    """A list of sites by name for this set of failure data."""
    FailuresPerOperation: list[RemoteImportFailurePerSite]
    """A list of failure information from sites."""

class RemoteImportFailurePerSite:
    """
    
following errors may be returned in the RemoteImportFailurePerSite structure.

96001 - The bulk "Iman Export Record" (IXR) creation or update has failed during
the TC XML based multisite operation.

96002 - The "Export Commit" process has failed during the TC XML based multisite
operation.

96003 - The processing callback function is not set for the TC XML based
multisite
operation.

96004 - The "Export Record" could not be created during the TC XML based
multisite
operation.

96005 - The "Export Record" could not be created during the TC XML based
multisite
operation due to an invalid value for the attribute

96023 - An error has been encountered during the access of the volume during the
TC XML based operation.

96024 - An invalid input data  was found while updating the fast synchronization
tables during the TC XML based operation. Please refer to the log files for
details.

96025 - The save of "Iman Export Record" (IXR) has encountered partial errors
during
the TC XML based multisite operation. Please refer to the log files for details.

96026 - The conversion of the input parameters of the utility to its
representative
Option Set has failed.

    """
    def __init__(self, ) -> None: ...
    FailureCodes: list[int]
    """A list of failure codes for this operation."""
    FailureObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of objects that have failed to import"""
    FailureStrings: list[str]
    """A list of error strings for this operation."""

class RemoteImportInfo:
    """
    
The RemoteImportInfo structure takes an option set name and export options as
input.
The option set and options will affect the final state of the exported objects
at
the target sites. There is system default option set and additional option sets
may
be created by the administrator. When the option set and options are not
specified
in the RemoteExportInfo structure, the system default option set and default
options
will be used. Please find the default option values in the list of supported
options
below.

The targeted objects can be of two types.

1.Â Â Â Â A replica PomObject which has been previously imported
into the local site

2.Â Â Â Â A PublishedObject which is proxy for remote object. This
object must minimally contain UID and the owning site information.

    """
    def __init__(self, ) -> None: ...
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of target objects."""
    OptionSetName: str
    """Name of option set used for import."""
    Reason: str
    """The reason for this import. It may be empty."""
    ImportOptions: list[ImportExportOptionsInfo]
    """A list of import options."""

class RemoteImportResponse:
    """
    
The RemoteImportResponse returns detailed partial failure information in
RemoteImportFailurePerOperation
structures along with a ServiceData.

This operation can return errors from different sites and each target object may
have different errors per site.  The RemoteImportFailurePerOperation structure
will
be used to report failures instead of the ServiceData to allow for the detailed
reporting
of site specific errors.  The RemoteImportFailurePerOperation structure will
report
what which site the errors are returned from. The list
RemoteImportFailurePerSite
structures will return errors for a specific target object(s).

    """
    def __init__(self, ) -> None: ...
    FailureInfo: list[RemoteImportFailurePerOperation]
    """The partial failure information specfic to site."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The Service Data return. Objects sucessfully imported will be added to the Updated
            object list.
            """

class RemoteImportUIDInfo:
    """
    
The RemoteImportUIDInfo structure takes an option set name and export options as
input. The option set and options will affect the final state of the exported
objects
at the target sites. There is system default option set and additional option
sets
may be created by the administrator. When the option set and options are not
specified
in the RemoteExportInfo structure, the system default option set and default
options
will be used.
    """
    def __init__(self, ) -> None: ...
    ObjectUIDs: list[str]
    """A list of target objects in UID form."""
    OwningSiteIds: list[int]
    """A list of owning sites by site ids for each object in objectUIDs"""
    OptionSetName: str
    """Name of option set used for import."""
    Reason: str
    """The reason for this import. It may be empty."""
    ImportOptions: list[ImportExportOptionsInfo]
    """A list of import options."""

class ImportExportTCXML:
    """
    Interface ImportExportTCXML
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def RemoteExport(self, Rinfos: list[RemoteExportInfo]) -> RemoteExportResponse:
        """    
             This operation exports targeted objects from the local site to the target sites using
             the Multi-Site TCXML payload. The target objects are specified in the RemoteExportInfo
             structure. The options also specified in this structure affect the final state of
             the exported objects at the target sites. The objects must be owned at the local
             site.
             

Use Cases:

             In the Multi-Site federation user can share the business objects among the participating
             sites, the client shares business object(s) using the remote import or remote export
             functionality. This operation supports the following use case.
             
             The remote export (i.e. push) of business objects owned at the local site to the
             target site. The business object will exist at the target site either a replica or
             local object depending on options at the conclusion of the operation.
             

Teamcenter Component:

             Classic Multi-Site - Technology to replicate data across multiple instances of Tc.
             It allows for transfering the ownership of objects across different instance and
             tools to export and synchronize data.
             
        :param Rinfos: 
                         A list   objects along with information related to the export operation.
             
        :return: 95023Â Â Â Â  Multisite TIE import failures reported by some remote
             sites, please find details in the syslog.
        """
        ...
    def RemoteImport(self, Rinfos: list[RemoteImportInfo]) -> RemoteImportResponse:
        """    
             The remoteImport operation imports targeted objects from their source site to the
             local site using the Multi-Site TCXML payload. The inputs include various options
             which will affect the final state of the Business Objects at the local site.
             

Use Cases:

             In the Multi-Site federation user can share the business objects among the participating
             sites, the client shares business object(s) using the remote import or remote export
             functionality. This operation supports the following use case.
             
             The remote import (i.e. pull) of business objects owned at the target site to the
             local site. The business object will exist at the local site as either a replica
             or local object depending on options at the conclusion of the operation. They will
             be updated if they already exist in the local site.
             

Teamcenter Component:

             Classic Multi-Site - Technology to replicate data across multiple instances of Tc.
             It allows for transfering the ownership of objects across different instance and
             tools to export and synchronize data.
             
        :param Rinfos: 
                         A list of objects along with information related to the import operation.
             
        :return: 
        """
        ...
    def RemoteImportByUID(self, Rinfos: list[RemoteImportUIDInfo]) -> RemoteImportResponse:
        """    
             The remoteImport operation imports targeted objects from their source site to the
             local site using the Multi-Site TCXML payload. The inputs include various options
             which will affect the final state of the Business Objects at the local site.
             

Use Cases:

             In the Multi-Site federation user can share the business objects among the participating
             sites, the client shares business object(s) using the remote import or remote export
             functionality. This operation supports the following use case.
             
             The remote import (i.e. pull) of business objects owned at the target site to the
             local site. The business object will exist at the local site as either a replica
             or local object depending on options at the conclusion of the operation. They will
             be updated if they already exist in the local site.
             


Teamcenter Component:

             Classic Multi-Site - Technology to replicate data across multiple instances of Tc.
             It allows for transfering the ownership of objects across different instance and
             tools to export and synchronize data.
             
        :param Rinfos: 
                         A list of objects along with information related to the import operation.
             
        :return: 
        """
        ...

