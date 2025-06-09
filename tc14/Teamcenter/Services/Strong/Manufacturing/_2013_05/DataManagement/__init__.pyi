import System
import Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement
import Teamcenter.Soa.Client.Model
import typing

class Data:
    """
    The structure specifies details of the attribute value.
    """
    def __init__(self, ) -> None: ...
    DataType: str
    """
            Type of the data. Valid types are "Boolean", "Character", "Integer", "Double", "String",
            "Tag" and "Date". Corresponding list in this structure need to be populated based
            on the data type string.
            """
    BoolAttributes: list[bool]
    """The list of Boolean values."""
    CharAttributes: str
    """
            The string representing the list of characters. Each character in the string is a
            value of the attribute.
            """
    IntegerAttributes: list[int]
    """The list of integer values."""
    DoubleAttributes: list[float]
    """The list of double values."""
    StringAttributes: list[str]
    """The list of string values."""
    TagAttributes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The list of business objects."""
    DateAttributes: list[System.DateTime]
    """The list of dates."""

class AttributeDetailsStruct:
    """
    The structure specifyies the attributes and its value.
    """
    def __init__(self, ) -> None: ...
    AttributeName: str
    """The string representing the name of the valid attribute which needs to be edited."""
    AttributeValueDetails: Data
    """The structure specifying details of the attribute value."""

class ObjectAttributesInput:
    """
    
            The input structure contains object(s) to be edited and the details of the attributes
            or relations which need to be edited.
            
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """
            The business object representing the BOM line. Attributes of the objects attached
            to this BOM line will be edited.
            """
    AttachedObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The business object attached to the BOM line. Attributes of this object are
            edited.
            """
    AttributeDetails: list[AttributeDetailsStruct]
    """
            List of the structure attributeDetailsStruct specifying the attributes and their
            value.
            """

class SyncStudyInput:
    """
    
            The Mfg0BvrStudy objects to synchronize and the direction to synchronize (to/from
            the study).
            
    """
    def __init__(self, ) -> None: ...
    Study: Teamcenter.Soa.Client.Model.ModelObject
    """The Mfg0BvrStudy objects to synchronize"""
    Direction: bool
    """The direction to synhronize (true = from BOP, false = to BOP)"""

class SyncStudyResponse:
    """
    The FMS file ticket to the log file for the study synchronization.
    """
    def __init__(self, ) -> None: ...
    LogFileTicket: str
    """The fmd ticket to the log file"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard Service Data"""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateAttachments(self, Input: list[Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement.CreateIn]) -> Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement.CreateResponse:
        """    
             This service operation creates the attachment objects for a business object(s).
             
             The operation considers the Incremental Change applied on the window of the object
             for which attachment is to be created.
             
             The operation takes following inputs.
             

clientId - Unique client Identifier.
             
context - The business objects of the BOM Line. The
             IC applied on the window of this line is considered while creating the attachment.
             
target - The business object which is used as primary object
             to connect the newly created object.
             
relation name - The name of the relation used to connect the
             target.
             
data - Input data for create operation.
             



Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         A list of CreateIn objects representing the Create Input for Business Objects to
                         be created.
             
        :return: 
        """
        ...
    def SetAttributes(self, Input: list[ObjectAttributesInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service operation sets the attributes of objects attached to the business object(s).
             For example, if some attributes of a Form attached to an Item needs
             to be edited, this operation can be used.
             
             The operation considers the Incremental Change applied on the window of the object
             whose attachment is to be edited.
             
             The operation takes the business objects of the BOMLine and its attached object
             which is to be edited. Along with that, it takes the name(s) of attributes  and their
             corresponding values to be set.
             
             This operation can set multiple attributes of multiple attached objects.
             


Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         The input structure contains object(s) to be edited and the details of the attributes
                         or relations which need to be edited.
             
        :return: 
        """
        ...
    def SyncStudyAndSource(self, Input: list[SyncStudyInput]) -> SyncStudyResponse:
        """    
             This operation synchronizes a Simulation Study with the source BOP structure it is
             associated with.
             
        :param Input: 
                         The Mfg0BvrStudy objects to synchronize and the direction to synchronize (to/from
                         the study).
             
        :return: The FMS file ticket to the log file for the study synchronization.
        """
        ...

