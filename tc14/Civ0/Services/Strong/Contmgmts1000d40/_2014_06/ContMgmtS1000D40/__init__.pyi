import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class BrexData:
    """
    Return data for each BrexInput passed into brexValidation SOA.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """The client ID (matches the clientId in BrexInput)."""
    IsValid: bool
    """True if the BREX validation succeeded for this Data Module."""

class BrexInput:
    """
    Input paramaters for the brexValidation SOA.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """The client ID"""
    BusinessObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The Civ0DM40Revision, Civ0PM40Revision, Civ0DML40Revision or
            Civ0DDN40Revision object to run BREX validation on.  This can be NULL if an
            XML file is passed in via dmTransientFileReadTicket.
            """
    DmTransientFileReadTicket: str
    """
            An S1000D 4.X/5.X Data Module XML file to validate against the BREX Data Module.
            If this is empty, the businessObject is used.
            """
    BrexFileReadTicket: str
    """
            The BREX XML file to use for BREX validation.  If this is an empty string, the BREX
            XML file that is referenced in the Data Module's XML is used.  The operation uses
            the brexDmRef in the Data Module's XML, construct the Data Module Code from that,
            and search the data base for a Civ0DM40Revision object with that item_id.
            """

class BrexResponse:
    """
    The return data for brexValidation SOA.
    """
    def __init__(self, ) -> None: ...
    Data: list[BrexData]
    """A list of objects that contain the BREX validation status."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data for this operation call."""
    LogTransientFileReadTicket: str
    """
            The file ticket of the log file for the BREX validation of the Data Module(s).  This
            is used for a synchronous call.
            """

class BulkImportData:
    """
    Return data for matching BulkImportInputInfo for call to bulkImport SOA.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """The client ID (matches the clientId in BulkImportInputInfo)."""
    WasSuccessful: bool
    """True if the import was successful.  False if it failed."""

class BulkImportInputInfo:
    """
    File to be imported and arguments for import.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """The client ID."""
    KeyValueArgs: System.Collections.Hashtable
    """
            This is a map of key value pairs (string, string).  This will contain the parameters
            used to control the bulk import.
            

"type" - Either "SNS" or "DMRL"
            

"""
    TransientFileReadTicket: str
    """The file ticket of the file to be imported."""
    BusinessObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The selected Ctm0BOMLine, Civ0SNSRootNode, Civ0SNSRootNodeRevision,
            Ctm0SNSNode or Ctm0SNSNodeRevision.  Will be ignored if the type is
            "SNS".  If the type is "DMRL", the created Data Modules will be related to the corresponding
            SNS nodes.
            """

class BulkImportResponse:
    """
    Return data for call to bulkImport SOA.
    """
    def __init__(self, ) -> None: ...
    Data: list[BulkImportData]
    """This contains the import status of the file."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data for this operation call."""

class IncrementalDeliveryData:
    """
    
            Used by IncrementalDeliveryResponse; contains the file ticket for the zip file created
            for the delivery.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """The client ID (matches the clientId in IncrementalDeliveryInputInfo)."""
    DeliveryFileTicket: str
    """The file ticket for the zip file created for the delivery."""

class IncrementalDeliveryInputInfo:
    """
    Input object for incrementalDelivery().
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """The client ID."""
    BusinessObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            This will contain the Ctm0BOMLine, Civ0DML40Revision or Civ0DML40
            object used for the incremental delivery.
            """
    KeyValueArgs: System.Collections.Hashtable
    """
            Map of key value pairs.  This will contain the parameters used to control the incremental
            delivery.
            

"skddispfrom_building" - Value of Dispatch From Building
            
"skddispfrom_city" - Value of Dispatch From City
            
"skddispfrom_country" - Value of Dispatch From Country
            
"skddispfrom_dept" - Value of Dispatch From Department
            
"skddispfrom_div_name" - Value of Dispatch From Division Name
            
"skddispfrom_email" - Value of Dispatch From Email
            
"skddispfrom_ent_name" - Value of Dispatch From Company Name
            
"skddispfrom_ent_unit" - Value of Dispatch From Company Unit
            
"skddispfrom_fax" - Value of Dispatch From Fax
            
"skddispfrom_firstname" - Value of Dispatch From First Name
            
"skddispfrom_internet" - Value of Dispatch From Web Address
            
"skddispfrom_jobtitle" - Value of Dispatch From Job Title
            
"skddispfrom_lastname" - Value of Dispatch From Last Name
            
skddispfrom_phone" - Value of Dispatch From Telephone
            
"skddispfrom_pobox" - Value of Dispatch From Postal Box
            
"skddispfrom_postcode" - Value of Dispatch From Postal Code
            
"skddispfrom_province" - Value of Dispatch From Province
            
"skddispfrom_room" - Value of Dispatch From Room
            
"skddispfrom_state" - Value of Dispatch From State
            
"skddispfrom_street" - Value of Dispatch From Street
            
"skddispfrom_zip" - Value of Dispatch From Zip Code
            
"skddispto_building" - Value of Dispatch To Building
            
"skddispto_city" - Value of Dispatch To City
            
"skddispto_country" - Value of Dispatch To Country
            
"skddispto_dept" - Value of Dispatch To Department
            
"skddispto_div_name" - Value of Dispatch To Division Name
            
"skddispto_email" - Value of Dispatch To Email
            
"skddispto_ent_name" - Value of Dispatch To Enterprise Name
            
"skddispto_ent_unit" - Value of Dispatch To Enterprise Unit
            
"skddispto_fax" - Value of Dispatch To Fax
            
"skddispto_firstname" - Value of Dispatch To First Name
            
"skddispto_internet" - Value of Dispatch To Web Address
            
"skddispto_jobtitle" - Value of Dispatch To Job Title
            
"skddispto_lastname" - Value of Dispatch To Last Name
            
"skddispto_phone" - Value of Dispatch To Telephone
            
"skddispto_pobox" - Value of Dispatch To Postal Box
            
"skddispto_postcode" - Value of Dispatch To Postal Code
            
"skddispto_province" - Value of Dispatch To Province
            
"skddispto_room" - Value of Dispatch To Room
            
"skddispto_state" - Value of Dispatch To State
            
"skddispto_street" - Value of Dispatch To Street
            
"skddispto_zip" - Value of Dispatch To Zip
            

"""

class IncrementalDeliveryResponse:
    """
    Return data for the call to incrementalDelivery().
    """
    def __init__(self, ) -> None: ...
    Data: list[IncrementalDeliveryData]
    """
            The data returned.  This will contain the file ticket for the zip file created for
            the delivery.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data for this operation call."""

class SNSData:
    """
    
            This will contain the properties and values that will be used to pre-populate the
            create dialog.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """The client ID (matches the clientId in SNSInput)."""
    DefaultValueMap: System.Collections.Hashtable
    """
            This is a map of key value pairs (string, string).  This contains the properties
            and values that will be used to pre-populate the create dialog
            


"civ0LangTagRef" - Value from the selected object's root node
            
"civ0ModelID" - Value from the selected object's root node
            
"civ0SDC" - Value from the selected object's root node
            
"civ0DisCodeV" - Value from the selected object's root node
            
"civ0ItemLoc" - Value from the selected object's root node
            
"civ0SecurityClass" - Value from the selected object's root node
            
"civ0Orig" - Value from the selected object's root node
            
"civ0OrigName" - Value from the selected object's root node
            
"civ0RPC" - Value from the selected object's root node
            
"civ0RPCName" - Value from the selected object's root node
            
"civ0FromDivName" - Value from the selected object's root node
            
"civ0FromStreet" - Value from the selected object's root node
            
"civ0FromPOBox" - Value from the selected object's root node
            
"civ0FromCity" - Value from the selected object's root node
            
"civ0FromState" - Value from the selected object's root node
            
"civ0FromZip" - Value from the selected object's root node
            
"civ0FromProvince" - Value from the selected object's root node
            
"civ0FromPostCode" - Value from the selected object's root node
            
"civ0FromCountry" - Value from the selected object's root node
            
"civ0SystemCode" - Value from the selected object's system node
            
"civ0SubSystemCode" - Value from the selected object's subsystem
            node
            
"civ0AssemblyCode" - Value from the selected object's assembly code
            node
            
"civ0DisCode" - Value from the selected object's root disassembly
            code node
            

"""

class SNSInput:
    """
    A SNS node.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """The client ID."""
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The selected BOM Line of a Ctm0SNSNodeRevision."""
    KeyValueArgs: System.Collections.Hashtable
    """
            Map of key value pairs. This will contain the parameters used to control the retrieval
            of SNS default values.
            
"""

class SNSResponse:
    """
    Return data for a call to getSNSDefaultValues SOA.
    """
    def __init__(self, ) -> None: ...
    Data: list[SNSData]
    """
            The data returned.  This will contain the properties and values that will be used
            to pre-populate the create dialog.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data for this SOA call."""

class ContMgmtS1000D40:
    """
    Interface ContMgmtS1000D40
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def BrexValidation(self, Input: list[BrexInput], IsAsync: bool) -> BrexResponse:
        """    
             This operation runs BREX (Business Rules EXchange) validation on S1000D 4.X/5.X Data
             Modules.  BREX validation is an additional layer of validation beyond the basic validation
             provided by the S1000D XML Schemas. The S1000D XML Schemas have hundreds of elements
             and attributes that are optional, the BREX Data Module specifies which of these are
             optional or required for the current project. Furthermore, it allows for valid values
             for elements and attributes to be specified within the Data Module.
             

Teamcenter Component:

             Content Management - New Content Management module that provides the capability to
             create/reuse/manage compound documents based on SGML/XML in Tc.
             
        :param Input: 
                         A list of objects that contain the files or object to run the BREX validation on.
             
        :param IsAsync: 
                         If true, the call is asyncrounous.
             
        :return: 
        """
        ...
    def BulkImport(self, Input: list[BulkImportInputInfo]) -> BulkImportResponse:
        """    
             This operation perfoms a bulk import of S1000D 4.X/5.X Data Modules or an SNS (Standard
             Number System) structure into content management
             

Teamcenter Component:

             Content Management - New Content Management module that provides the capability to
             create/reuse/manage compound documents based on SGML/XML in Tc.
             
        :param Input: 
                         A list of files to be imported and arguments for import.
             
        :return: 
        """
        ...
    def GetSNSDefaultValues(self, Input: list[SNSInput]) -> SNSResponse:
        """    
             This gets the default values for the Data Module using the selected SNS node.  This
             is used to pre-populate the create dialog within Content Management.
             

Teamcenter Component:

             Content Management - New Content Management module that provides the capability to
             create/reuse/manage compound documents based on SGML/XML in Tc.
             
        :param Input: 
                         A list of select SNS nodes.
             
        :return: 
        """
        ...
    def IncrementalDelivery(self, Input: list[IncrementalDeliveryInputInfo]) -> IncrementalDeliveryResponse:
        """    
             This operation provides an incremental delivery of a Data Module List. These deliveries
             will be compared to previous deliveries and only deliver S1000D 4.X/5.X Data Modules
             that have changed since the last delivery. The Data Modules that will be delivered
             will be packaged in an S1000D 4.X/5.X Data Dispatch Note as this is the mechanism
             used in S1000D for a delivery. This new Data Dispatch Note will be related to the
             Data Module List.
             

Teamcenter Component:

             Content Management - New Content Management module that provides the capability to
             create/reuse/manage compound documents based on SGML/XML in Tc.
             
        :param Input: 
                         A vector of IncrementalDeliveryInputInfo objects.
             
        :return: 
        """
        ...

