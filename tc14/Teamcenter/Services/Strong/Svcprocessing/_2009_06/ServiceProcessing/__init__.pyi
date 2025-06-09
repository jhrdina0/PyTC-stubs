import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class StatusInput:
    """
    StatusInput
    """
    def __init__(self, ) -> None: ...
    TransElem: Teamcenter.Soa.Client.Model.Strong.TransactionElement
    """Business Object to change"""
    StringProps: System.Collections.Hashtable
    """Map containing string status property values"""

class SetTxnStatusInfo:
    """
    Input structure.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique client identifier. This is a unique string supplied by the caller. This
            ID
            
            is used to identify return data elements and partial errors associated with this
            input structure.
            
"""
    Data: StatusInput
    """
            Input data comprising of the transaction element and the approval attribute based
            on which the status is assigned.
            
"""

class SetTxnStatusOutput:
    """
    The output structure.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client track the object(s) created"""
    TransElemObjs: list[Teamcenter.Soa.Client.Model.Strong.TransactionElement]
    """Service data including partial errors that are mapped to the client id"""

class SetTxnStatusResponse:
    """
    Structure containing approval status and Service Data.
    """
    def __init__(self, ) -> None: ...
    Output: list[SetTxnStatusOutput]
    """This represents a vector of output objects"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects whose status for the approval attribute
            is set based on the input and error information returned based on validations performed.
            
"""

class ServiceProcessing:
    """
    Interface ServiceProcessing
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SetTxnElementStatus(self, Info: list[SetTxnStatusInfo]) -> SetTxnStatusResponse:
        """    
             This operation sets the status of the transaction element based on the SetTxnStatusInfo supplied. The SetTxnStatusInfo
             contains information for properties such as clientId
             and data. The value of the approval attribute
             is obtained and the corresponding transaction element status is set by calling the
             operation setTxnElementStatus.  This operation
             utilizes the input information which consists of the approval value, the transaction
             element type and name. The operation performs validations to ensure that all conditions
             are met and an attempt to approve an object that is already approved throws an appropriate
             error message to the user.
             

Teamcenter Component:

             Service Processing - This Component is intended to identify all Operations and Services
             under Service Processing.
             
        :param Info: 

        :return: 
        """
        ...

