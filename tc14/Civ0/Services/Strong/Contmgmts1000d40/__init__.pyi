import Civ0.Services.Strong.Contmgmts1000d40._2014_06.ContMgmtS1000D40
import System
import Teamcenter.Soa.Client

class ContMgmtS1000D40RestBindingStub(ContMgmtS1000D40Service):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def BrexValidation(self, Input: list[Civ0.Services.Strong.Contmgmts1000d40._2014_06.ContMgmtS1000D40.BrexInput], IsAsync: bool) -> Civ0.Services.Strong.Contmgmts1000d40._2014_06.ContMgmtS1000D40.BrexResponse: ...
    def BulkImport(self, Input: list[Civ0.Services.Strong.Contmgmts1000d40._2014_06.ContMgmtS1000D40.BulkImportInputInfo]) -> Civ0.Services.Strong.Contmgmts1000d40._2014_06.ContMgmtS1000D40.BulkImportResponse: ...
    def GetSNSDefaultValues(self, Input: list[Civ0.Services.Strong.Contmgmts1000d40._2014_06.ContMgmtS1000D40.SNSInput]) -> Civ0.Services.Strong.Contmgmts1000d40._2014_06.ContMgmtS1000D40.SNSResponse: ...
    def IncrementalDelivery(self, Input: list[Civ0.Services.Strong.Contmgmts1000d40._2014_06.ContMgmtS1000D40.IncrementalDeliveryInputInfo]) -> Civ0.Services.Strong.Contmgmts1000d40._2014_06.ContMgmtS1000D40.IncrementalDeliveryResponse: ...

class ContMgmtS1000D40Service:
    """
    
            This service provides S1000D specific functionality.  It allows users to run a Business
            Rules EXchange (BREX) validation on S1000D 4.X/5.X Data Modules.  Furthermore, it
            provides default values based on the selected Standard Number System (SNS) node.
            These values will be used to create new Data Modules in the RAC by pre-populating
            the create dialog.  It also provides incremental delivery options for S1000D 4.X/5.X
            Data Module Lists and bulk import of SNS structures and data management requirement
            lists.
            


Library Reference:

Civ0SoaContMgmtS1000D40Strong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ContMgmtS1000D40Service:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def BrexValidation(self, Input: list[Civ0.Services.Strong.Contmgmts1000d40._2014_06.ContMgmtS1000D40.BrexInput], IsAsync: bool) -> Civ0.Services.Strong.Contmgmts1000d40._2014_06.ContMgmtS1000D40.BrexResponse:
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
    def BulkImport(self, Input: list[Civ0.Services.Strong.Contmgmts1000d40._2014_06.ContMgmtS1000D40.BulkImportInputInfo]) -> Civ0.Services.Strong.Contmgmts1000d40._2014_06.ContMgmtS1000D40.BulkImportResponse:
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
    def GetSNSDefaultValues(self, Input: list[Civ0.Services.Strong.Contmgmts1000d40._2014_06.ContMgmtS1000D40.SNSInput]) -> Civ0.Services.Strong.Contmgmts1000d40._2014_06.ContMgmtS1000D40.SNSResponse:
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
    def IncrementalDelivery(self, Input: list[Civ0.Services.Strong.Contmgmts1000d40._2014_06.ContMgmtS1000D40.IncrementalDeliveryInputInfo]) -> Civ0.Services.Strong.Contmgmts1000d40._2014_06.ContMgmtS1000D40.IncrementalDeliveryResponse:
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

