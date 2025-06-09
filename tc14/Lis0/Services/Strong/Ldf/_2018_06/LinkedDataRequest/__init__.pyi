import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class LdfFileSelectionDialogResponse:
    """
    
            Returns string for the URL with parameters for datasetUid, Acceptable MIME Types
            for dataset and Linked Object
            
    """
    def __init__(self, ) -> None: ...
    LdfFileSelectionDialogUrl: str
    """URL with parameters for datasetUid and LinkedObject"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """service data for partial errors"""

class LinkedDataRequest:
    """
    Interface LinkedDataRequest
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetLDFFileSelectionDialogService(self, LdfFileSelectionDialogInputMap: System.Collections.Hashtable) -> LdfFileSelectionDialogResponse:
        """    
             This operation creates dataset of given name and type. It will then build the URL
             for associated Remote File Selection Delegated UI with parameters of dataset UID,MIME
             types and the external UID. The remote system should use MIME types for File selection
             Filtering and use the external UID to search for the object to collect the remote
             files from.
             

Teamcenter Component:

             Linked Data Framework - Component for Linked Data Framework (LDF)
             
        :param LdfFileSelectionDialogInputMap: 
                         5.datasetUid
             
        :return: 121012: The URL request cannot be processed successfully.
        """
        ...

