import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class LOVAttachment:
    """
    Structure to hold property and its LOV attachment.
    """
    def __init__(self, ) -> None: ...
    PropName: str
    """Name of the property to  which LOV attachment return."""
    Lov: Teamcenter.Soa.Client.Model.Strong.ListOfValues
    """Attached LOV object."""

class LOVAttachmentsInput:
    """
    
            A structure holding objects and common properties for which LOV attachments are to
            be returned.
            
    """
    def __init__(self, ) -> None: ...
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Instances of any business object for which LOV attachments are being evaluated."""
    Properties: list[str]
    """
            Names of common properties for which LOV attachments to be returned for each instance
            in objects
"""

class LOVAttachmentsResponse:
    """
    LOV attachments for the given object properties.
    """
    def __init__(self, ) -> None: ...
    LovAttachments: System.Collections.Hashtable
    """A list of objects and its properties and associated LOV attachments."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class LOV:
    """
    Interface LOV
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetLOVAttachments(self, ObjectStructArray: list[LOVAttachmentsInput]) -> LOVAttachmentsResponse:
        """    
             Returns valid LOV attachments for the properties of each object passed in as input.
             It may return LOV or null based on condition validations. If none of the conditions
             evaluated to be True, then no LOV attachment is returned for the property
             of an instance.
             

Teamcenter Component:

             List of Values (LOV) - Component to define lists of values and to associate them
             with attributes and properties.  Associations can be stored in the database (persistent)
             or independently associated for each Teamcenter session (run time).
             
        :param ObjectStructArray: 
                         LOV attachments are evaluated for each property of the structure LOVAttachmentsInut
                         based on each object in <font face="courier" height="10">objects</font> list.
             
        :return: Returns LOV attachments currently attached to properties.
        """
        ...

