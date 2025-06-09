import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class MappedFeature:
    """
    
The MappedFeature structure has a couple of features that are mapped and the
attributes
that are common to them
    """
    def __init__(self, ) -> None: ...
    FeatureId1: str
    """Integer identifier for first feature"""
    FeatureId2: str
    """Integer identifier for second feature"""
    FeatureAttrCode: list[str]
    """
            List of attribute code values that are common to featureId1
            and featureId2

"""

class MappedFeatureResponse:
    """
    
The MappedFeatureResponse structure represents the map which has the information
of mapped feature data.for a client Id
    """
    def __init__(self, ) -> None: ...
    MappedFeatureData: System.Collections.Hashtable
    """
            A Map between the clientId as key and a list
            of mapped features as value. The  clientId
            key identifies two routine revisions for which the mapped feature information is
            provided in the MappedFeature structure.
            Each MappedFeature structure has two features
            that are mapped and a list of attribute codes that are common to them
            
"""
    PartialErrors: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class RoutineSetInfo:
    """
    The RoutineSetInfo structure has the routines whose mapped features need to be
retrieved
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A key provided as input that is unique and associated with the two routine revisions
            in the RoutineSetInfo structure. This key
            is used in the output MappedFeatureMap parameter
            to identify the routine revisions with the associated feature map information. The
            routine revision information is not used in the output and the clientId is used in
            its place. It is the responsibility of the user  to ensure that the clientId is unique
            """
    Routine1: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """First routine revision"""
    Routine2: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Second routine revision"""

class EngineeringDataQuery:
    """
    Interface EngineeringDataQuery
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetMappedFeatureData(self, Request: list[RoutineSetInfo]) -> MappedFeatureResponse:
        """    
             This operation returns a set of mapped features for each pair of routine revisions
             in the request list. For each pair of routine revisions, the mapped feature information
             maps a subset of features in the second routine to features in the first routine
             revision. This map information is for features and not feature attributes. If one
             feature is mapped to another feature, then all the common attribute codes between
             the two features are mapped that is, there is no way to map select attribute codes
             under a feature).
             

Use Cases:

             The DPV Reporting & Analysis client application in standalone Teamcenter lifecycle
             visualization queries Teamcenter for mapped features between two routine revisions.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param Request: 
                         A list of routine set information structures. Each structure contains a <font face="courier" height="10">clientId</font> and a pair of routine revisions for which the mapped
                         feature information is requested. The <font face="courier" height="10">clientId</font>
                         is a unique integer and a key that represents the pair of routine revisions in the
                         structure. It is the responsibility of the user to ensure that the <font face="courier" height="10">clientId</font> is unique
             
        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...

