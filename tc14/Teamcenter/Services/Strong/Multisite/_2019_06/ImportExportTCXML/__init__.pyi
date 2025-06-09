import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class RemoteCheckinFailure:
    """
    Object specific detailed failure information.
    """
    def __init__(self, ) -> None: ...
    FailureObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of objects that have failed to check-in."""
    FailureCodes: list[int]
    """A list of failure codes for this operation."""
    FailureStrings: list[str]
    """A list of error strings corresponding to each error in failureCodes."""

class RemoteCheckinResponse:
    """
    
The RemoteCheckinResponse returns detailed partial failure information in
RemoteCheckinFailure
structures along with a ServiceData.
    """
    def __init__(self, ) -> None: ...
    FailureInfo: list[RemoteCheckinFailure]
    """
            A list of RemoteCheckinFailure structures. Each structure contains failure information
            for a specific business object that was supplied.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The standard ServiceData return."""

class RemoteCheckoutFailure:
    """
    Failure information  for specific objects that failed to remote check out.
    """
    def __init__(self, ) -> None: ...
    FailureObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of objects that have failed to check out."""
    FailureCodes: list[int]
    """A list of failure codes for the failureObjects."""
    FailureStrings: list[str]
    """A list of error strings corresponding to each error in failureCodes."""

class RemoteCheckoutResponse:
    """
    
The RemoteCheckoutResponse returns detailed partial failure information in
RemoteCheckoutFailure
structures along with a ServiceData.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The standard ServiceData return."""
    FailureInfos: list[RemoteCheckoutFailure]
    """
            A list of RemoteCheckoutFailure structures. Each structure contains failure information
            for a specific business object that was supplied.
            """

class ImportExportTCXML:
    """
    Interface ImportExportTCXML
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def RemoteCheckin(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], OptionSetName: str, SessionOptions: System.Collections.Hashtable, OverrideOptions: System.Collections.Hashtable) -> RemoteCheckinResponse: ...
    def RemoteCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], OptionSetName: str, SessionOptions: System.Collections.Hashtable, OverrideOptions: System.Collections.Hashtable) -> RemoteCheckoutResponse:
        """    
             The RemoteCheckout operation applies the Multi-Site check out operation to the business
             objects in the objects parameter.
             

Use Cases:

             In the Multi-Site federation, a user can share the business objects among the participating
             sites, the client shares business object(s) using the remote import or remote export
             functionality. This allows the creation of replica objects which are read-only copies
             of the master object. Multi-site supports a Remote Check-in Check-out feature which
             allows edits to replica objects. This operation supports the following use case.
             


The remote check out of replica business objects.  This allows edits
             to the replica objects. These changes are later saved to the owning site with the
             remote check in operation.
             



Teamcenter Component:

             Classic Multi-Site - Technology to replicate data across multiple instances of Tc.
             It allows for transfering the ownership of objects across different instance and
             tools to export and synchronize data.
             
        :param Objects: 
                         A list of replica <b>WorkspaceObject</b> class business objects.
             
        :param OptionSetName: 
                         The name of <b>TransferOptionSet</b> used for check out. The default option set is
                         used if not supplied.
             
        :param SessionOptions: 
                         checkOutDependentObject: Checks out additional dependent objects defined by the <b>TransferOptionSet</b>
                         if True. The default is False.
             
        :param OverrideOptions: 
                         A map (string, list of strings) of overrides to <b>TransferOptionSet</b>  specified
                         in optionSetName. The overrides available are specific to the <b>TransferOptionSet</b>.
                         The available <b>TransferOptionSet</b> overrides can be viewed in the PLMXML/TCXML
                         Export Import Administration application.
             
        :return: 
        """
        ...

