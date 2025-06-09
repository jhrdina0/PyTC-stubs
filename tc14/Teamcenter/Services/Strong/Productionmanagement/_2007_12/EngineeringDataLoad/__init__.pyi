import Teamcenter.Soa.Client.Model
import typing

class ImportFeatureDataResponse:
    """
    
The ImportFeatureDataResponse structure is returned from the importFeatureData.
This
has serviceData object with any errors that occurred during execution of the
operation
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service data"""

class RoutineAndFile:
    """
    
The RoutineAndFile structure is given as input to importFeatureData. This has
routine
revision tag for which the feature data is imported. It also has the details
required
for creating the excel dataset.
    """
    def __init__(self, ) -> None: ...
    RoutineRevision: Teamcenter.Soa.Client.Model.ModelObject
    """A MEInspection_Revision  object"""
    FmsFileTicket: str
    """
            File ticket of a XML file that contains feature data of the routineRevision
"""
    DatasetName: str
    """Name of the DPVExcel  dataset that the operation will create operation"""
    DatasetDescription: str
    """Optional information that gives the description of the dataset"""

class EngineeringDataLoad:
    """
    Interface EngineeringDataLoad
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ImportFeatureData(self, Input: list[RoutineAndFile]) -> ImportFeatureDataResponse:
        """    
             This operation uploads the feature data for a routine revision. A routine revision
             is an ItemRevision of the type MEInspection_Revision. This operation
             takes an FMS file ticket of an XML file containing engineering data of a routine,
             such as feature ID, feature name, feature attributes and specification limits, as
             an input. It creates a DPVExcel dataset under the routine revision with an
             IMAN_specification relation on successful
             execution of the operation. All the features and attributes in the XML file are included
             in the DPVExcel  dataset.
             

Use Cases:

             Import an XML file in Manufacturing Process Planner (MPP) application in the Teamcenter
             rich client by selecting a routine revision of type MEInspection_Revision
             and usinging the Tools|"Import Feature Data" menu option.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param Input: 
                         A list of feature import data. Each element has the routine revision object for which
                         the feature data is to be imported, the FMS file ticket for an XML file with feature
                         data for the routine revision,  the name of the <b>DPVExcel</b> dataset that is to
                         be attached to the routine revision, and a description of the <b>DPVExcel</b> dataset
             
        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...

