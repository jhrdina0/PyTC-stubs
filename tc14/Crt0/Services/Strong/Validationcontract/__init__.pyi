import Crt0.Services.Strong.Validationcontract._2015_03.VCManagement
import Crt0.Services.Strong.Validationcontract._2020_12.VCManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model.Strong

class VCManagementRestBindingStub(VCManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetContractDefnDetails(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.Crt0VCDefnRevision]) -> Crt0.Services.Strong.Validationcontract._2015_03.VCManagement.ContractDefnResponse: ...
    def CreateVerificationRequest(self, Input: list[Crt0.Services.Strong.Validationcontract._2020_12.VCManagement.CreateVerificationRequestInputData]) -> Crt0.Services.Strong.Validationcontract._2020_12.VCManagement.CreateVerificationRequestResponse: ...

class VCManagementService:
    """
    
            The VCManagement service exposes operations to manage Contract Definitions and Validation
            Contracts.
            

            The service provides the following use cases to manage Validation Contracts
            

            Get the details of Contract Definition object
            



Library Reference:

Crt0SoaValidationContractStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> VCManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetContractDefnDetails(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.Crt0VCDefnRevision]) -> Crt0.Services.Strong.Validationcontract._2015_03.VCManagement.ContractDefnResponse:
        """    
             This operation retrieves the details of the input Contract Definitions by reading
             the attached Contract Package. The operation will return the details only if the
             package is valid.
             

             For a Contract Package to be valid:
             

It must adhere to the Contract schema. The schema can be found in
             the dataset "Crt0ContractPkgSchema" which gets deployed to Teamcenter database during
             installation of the "Validation Contract" feature.
             
Business objects used in the package must exist in Teamcenter.
             
Property names used in the package must exist in Teamcenter.
             



Teamcenter Component:

             Validation Contract - This component is used to manage data for Validation Contract.
             
        :param Inputs: 
                         Vector of inputs for getting details of the Contract Definition object
             
        :return: 
        """
        ...
    def CreateVerificationRequest(self, Input: list[Crt0.Services.Strong.Validationcontract._2020_12.VCManagement.CreateVerificationRequestInputData]) -> Crt0.Services.Strong.Validationcontract._2020_12.VCManagement.CreateVerificationRequestResponse: ...

