import System
import Teamcenter.Services.Strong.Systemsengineering._2011_06.FunctionalModeling
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class FunctionalModelingRestBindingStub(FunctionalModelingService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def DeleteFunctionStructure(self, Input: list[Teamcenter.Services.Strong.Systemsengineering._2011_06.FunctionalModeling.DeleteFunctionStructInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class FunctionalModelingService:
    """
    
            The FunctionalModeling service provides operations to manage
Functional Modeling
            structures. At present the service provides operation to delete an
entire functional
            structure.

            The FunctionalModeling service can be used to support the following:

Delete an entire Functional structure including all the interfaces
            and relations.

Library Reference:

TcSoaSystemsEngineeringStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> FunctionalModelingService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def DeleteFunctionStructure(self, Input: list[Teamcenter.Services.Strong.Systemsengineering._2011_06.FunctionalModeling.DeleteFunctionStructInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes a BOMLine object and optionally deletes its entire
             BOM structure. It not only deletes the structure relations but also deletes the objects
             underlying the BOM lines. If user chooses to delete the entire BOM structure, the
             structure is traversed and every node is validated for deletion. If the Teamcenter
             business object is released or referenced or there are more than one revisions of
             it, it cannot be deleted.
             

Teamcenter Component:

             Systems Engineering - Application to construct Systems Engineering view of the product
             
        :param Input: 
                         holds the required information to delete a line or structure.
             
        :return: 
        """
        ...

