import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetOccKinematicsInfoInput:
    """
    
Input containing context and scope for which the occurrence kinematics
information
of resource occurrence Mfg0MEResourceRevision or ItemRevision is required
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            Root BOMLine in Bill of Equipment structure representing Mfg0BvrWorkarea.
            The operation processes scope within the context.
            """
    Scope: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
BOMLine representing Mfg0BvrWorkarea object under context. The operation
            processes resource occurrence under the scope to get occurrence kinematics information.
            The scope can be empty, in this case context is treated as scope.
            """

class GetOccurrenceKinematicsInfoResponse:
    """
    Response for getOccurrenceKinematicsInformation operation.
    """
    def __init__(self, ) -> None: ...
    OccurrenceKinematicInfo: list[OccurrenceKinematicsInfo]
    """
            A list containing information about BOMLine representing occurrence of Mfg0MEResourceRevision
            or ItemRevision and ImanFile having occurrence kinematics information
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Teamcenter Services structure used to return status of the operation."""

class OccurrenceKinematicsInfo:
    """
    
Response containing information about context BOMLine representing
Mfg0BvrWorkarea,
scope BOMLine representing Mfg0BvrWorkarea , a map with key as BOMLine
representing occurrence of Mfg0MEResourceRevision or ItemRevision and
the value as ImanFile having occurrence kinematics information.
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """Root BOMLine in Bill of Equipment structure representing Mfg0BvrWorkarea"""
    Scope: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
BOMLine representing Mfg0BvrWorkarea object under context. The operation
            processes resource occurrence under the scope to get occurrence kinematics information
            """
    ResourceLineInformation: System.Collections.Hashtable
    """
            A map (BOMLine, ImanFile) containing information about BOMLine representing
            the occurrence of MFg0MEResourceRevision or ItemRevision as key and
            corresponding ImanFile as value which contains the kinematics information
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetOccurrenceKinematicsInformation(self, OccKinematicsInfoinput: list[GetOccKinematicsInfoInput]) -> GetOccurrenceKinematicsInfoResponse:
        """    
             In Line Designer (LD) and Process Simulate (PS), resource occurrence has specific
             poses and joint values. This operation retrieves occurrence kinematics information
             of Mfg0MEResourceRevision or ItemRevision from Bill of Equipment structure
             for the given scope Mfg0BvrWorkarea and context Mfg0BvrWorkarea acting
             as a root of the structure
             

Use Cases:

             Line Designer or Process Simulate user wants to get the occurrence kinematics information
             for occurrence of Mfg0MEResourceRevision or ItemRevision from Bill
             of Equipment structure
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param OccKinematicsInfoinput: 
                         Input structure containing context and scope for which the occurrence kinematics
                         information of resource occurrence is required
             
        :return: 253180: The input context is invalid. Context should be root line of the Bill of
             Equipment structure.
        """
        ...
    def SetOccurrenceKinematicsInformation(self, OccInfoInputMap: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             In Line Designer (LD) and Process Simulate (PS), resource occurrence used has specific
             poses and joint values. This operation creates a relation between AbsOccData
             and Mfg0OccKinematicsInfo using relation Mfg0OccKinematicsRel. The
             occurrence kinematics information is stored as an XML reference on the dataset Mfg0OccKinematicsInfo


Use Cases:

             Line Designer or Process Simulate user wants to set the occurrence kinematics information
             for occurrence of Mfg0MEResourceRevision or ItemRevision


Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param OccInfoInputMap: 
                         A map <b>(BOMLine, Dataset)</b> containing <b>BOMLine</b> representing the occurrence
                         of <b>Mfg0MEResourceRevision</b> or <b>ItemRevision</b> and the dataset <b>Mfg0OccKinematicsInfo</b>
                         having occurrence kinematics information.
             
        :return: in the Bill of Equipment structure.
        """
        ...

