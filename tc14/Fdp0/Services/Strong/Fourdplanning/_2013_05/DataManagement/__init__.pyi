import System
import Teamcenter.Soa.Client.Model
import typing

class CreateOrUpdateProcessToTaskRelationInfo:
    """
    
            Input structure for createOrUpdateProcessToTaskRelation.
            
            It contains the process or task as target objects and the objects to add & delete
            the relation with.
            
    """
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The input object (MEProcess or ScheduleTask) on which relation needs
            to be created or updated.
            """
    ObjectsToAdd: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            If targetObject is a MEProcess, this will be list of ScheduleTask
            which needs to be related to the MEProcess and viceversa.
            """
    ObjectsToDelete: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            If targetObject is a MEProcess, this will be list of ScheduleTasks
            with which relation needs to be deleted and viceversa.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateProcessToTaskRelation(self, Inputs: list[CreateOrUpdateProcessToTaskRelationInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation takes the source, target and naming information as input and creates
             a process structure based on that.
             

Teamcenter Component:

             FourD Planning - This Teamcenter component deals with specific requirements related
             to Ship Building Industry.        Which includes enhancements to structure search
             to support 4D search  i.e. search along a time line.
             
        :param Inputs: 
                         Vector of CreateOrUpdateProcessToTaskRelationInfo structure.
             
        :return: - Delete relation operation failed.
        """
        ...

