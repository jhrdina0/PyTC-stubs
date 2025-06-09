import System
import Teamcenter.Soa.Client.Model
import typing

class AppearancePathInput:
    """
    
Input parameter to the ComputeAppearancePath service: holds a parent object and
a
vector of child paths (relative to the object) that we would like to compute the
AppearancePaths for.

If the childPaths is an empty vector, the service will return all the values for
all the children recursively.

    """
    def __init__(self, ) -> None: ...
    ParentObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The parent of the nodes that we would like to get the APN/ absOccUID. If the parent
            object does not have APN, it would be calculated as well.
            """
    ChildPaths: list[NodePath]
    """
            The paths to the children for which we would like to get the APN\ absOccUID values.
            The path is relative to the parent object.
            
            If this vector is empty, the return will include the value for all the children recursively.
            """

class AppearancePathResult:
    """
    Holds the values of the apnUID and absOccUID properties for the relevant input
    """
    def __init__(self, ) -> None: ...
    AbsOccUID: str
    """The value of bl_absocc_uid_in_topline_context property"""
    ApnUID: str
    """The value of bl_apn_uid_in_topline_context"""

class ComputeAppearancePathResponse:
    """
    Results for ComputeAppearancePath service
    """
    def __init__(self, ) -> None: ...
    Results: list[ComputeAppearancePathResult]
    """Data structure that holds the results"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds all the modified BO and the errors"""

class ComputeAppearancePathResult:
    """
    
Holds the input parent object and the matching results for the childPaths

The result for childPaths[i] is in childResults[i].
    """
    def __init__(self, ) -> None: ...
    ParentObject: Teamcenter.Soa.Client.Model.ModelObject
    """The object that was given in the input"""
    ChildResults: list[AppearancePathResult]
    """
            The result matching each index in childPaths in the ComputeAppearancePathInput.
            
            The results holds values for APN and AbcOccID
            """

class NodePath:
    """
    
This struct holds the path to the node to which we would like to comppute the
AppearancePath.

The path is a vector CloneStableID property (bl_occurrence_uid)
    """
    def __init__(self, ) -> None: ...
    ThreadIDs: list[str]
    """
            The path to the node for which we would like to compute the property values. The
            path is relative to the parent (starts from the parentObject).
            
            The path is given as a vector of strings which represent threadIDs (CloneStableID)
            
"""

class Model:
    """
    Interface Model
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ComputeAppearancePath(self, Input: AppearancePathInput) -> ComputeAppearancePathResponse:
        """    
             This service computes and returns the values for APNUID and AbsOccUID propertis.
             

             APN - bl_apn_uid_in_topline_context
             
             AbsOccUID - bl_absocc_uid_in_topline_context
             

             Input: parent object and a list of paths.
             
                      Each path starts reletively from
             the parent object.
             
                      In case the parent does not have
             APN, the service will calculate it to the parent as well.
             
             Response : vector of values of the adove propeties according to each path.
             

             If the input is BOMLine (and not Fnd0BOMLineLite) there might be performance issue
             due to the fact that the modified obejct would be put in the serviceData and the
             properties that will be brought for this object would be according to the PolicyFile
             (in this case the best practice is to use Dymanic Policy).
             

             Fnd0BOMLineLite does not have as much properties as BOMLine and therefore even if
             the input is large, not many properties would be calculated in the Policy File.
             



Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         A list of AppearancePathInput that holds parent objects and a list of paths for each
                         one. Each path represents a node for which we would like to get the values of the
                         prorperties.
             
        :return: If there was an error in generating these properties, the return value would be ""
             and the error would be added to the serviceData
        """
        ...

