import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class DeepCopyDataInput:
    """
    Input structure for getDeepCopyData operation
    """
    def __init__(self, ) -> None: ...
    Operation: str
    """This is the operation types such as SaveAs,Revise, etc."""
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """object reference to get the deepcopydata"""

class GetDeepCopyDataResponse:
    """
    getDeepCopyData Response
    """
    def __init__(self, ) -> None: ...
    DeepCopyInfoMap: System.Collections.Hashtable
    """Map of the DeepCopy data"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Creates a list of Datasets and creates the specified relation type between created
            Dataset and input container object.
            """

class OperationDescriptor:
    """
    Interface OperationDescriptor
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDeepCopyData(self, DeepCopyDataInput: list[DeepCopyDataInput]) -> GetDeepCopyDataResponse:
        """    
             This operation returns information required to perform SaveAs on a Business Object
             instance.
             

Use Cases:

             Client constructs the SaveAs dialog for a Business Object using this operation. The
             information returned by this operation allows a client to construct the SaveAs dialogs
             and the DeepCopy panels for user input. Once the user input is received, client can
             make subsequent invocation to the DataManagement.saveAsObjects
             operation to execute SaveAs on the object.
             

Dependencies:

             saveAsObjects
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param DeepCopyDataInput: 
                         A list of DeepCopyDataInput structures which contains an object, and operation type.
             
        :return: as a partial error
        """
        ...

