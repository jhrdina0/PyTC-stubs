import System
import Teamcenter.Services.Strong.Core._2010_04.DataManagement
import Teamcenter.Services.Strong.Core._2015_07.DataManagement
import Teamcenter.Soa.Client.Model
import typing

class CreateAttachOut:
    """
    This is output structure for create operation including unique client identifier.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique client identifier"""
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of objects that were created."""
    Datasets: list[Teamcenter.Services.Strong.Core._2010_04.DataManagement.DatasetOutput]
    """
            List of output structure for created Dataset objects. Each element in the
            list contains a client id, the related Dataset object created, and the information
            needed to upload the Dataset object's named reference
            """

class CreateAttachResponse:
    """
    This is response object structure for the createAttachAndSubmitObjects operation
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateAttachOut]
    """List of output objects representing objects that were created"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data including partial errors that are mapped to the client id"""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateAttachAndSubmitObjects(self, Inputs: list[Teamcenter.Services.Strong.Core._2015_07.DataManagement.CreateIn2]) -> CreateAttachResponse:
        """    
             This is a generic operation for creation of business objects. This will also create
             any secondary (compound) objects that need to be created, assuming the CreateInput2
             for the secondary object is represented in the nested CreateInput2 object. e.g. Item
             is primary object that also creates an  Item Master and ItemRevision.
             ItemRevision in turn creates ItemRevision Master. The input for all
             these levels is passed in through the recursive CreateInput2 object.
             

             This operation also performs following tasks:
             

A list of file names can be passed in through the dataToBeRelated
             input of the CreateIn2 input object, and Dataset objects for the files will
             be created and related to the created business object. The information needed to
             subsequently upload the file contents will be passed back to the user in the CreateAttachResponse
             object.
             
Submit the created business object to a workflow process. The input
             for creating the workflow process is passed in through the workflowData input of
             CreateIn2 object.
             
Relate the created business object to the input target object.
             
If the created business object is under Item Revision Definition
             Configuration (IRDC) control, proposed file attachments are first evaluated against
             the object's IRDC settings to check if they are valid or not. Invalid files will
             be discarded. If the created business object is not under IRDC control, the files
             will simply be related to the created business object as Dataset objects.
             
Proposed file attachments to the created business object are specified
             as file names rather than unique ids of existing business objects. Empty Dataset
             objects are created and write tickets are fetched for the files that will be uploaded
             as named references.
             



Use Cases:

             Use Case 1: Create an Item object under IRDC control.
             

             The user wants to create and Item and its associated objects, and furthermore will
             set some of the create inputs so that the newly created object will be under Item
             Revision Definition Configuration (IRDC) control. No files or workflow inputs are
             provided.
             

             Use Case 2: Create an Item object under IRDC control and submit it to a workflow.
             

             As with Use Case 1, but the name of a workflow template is provided. After the Item
             object is created, it will be submitted to the specified workflow.
             

             Use Case 2: Create an Item object under IRDC control, attach files, and submit it
             to a workflow.
             

             As with Use Case 2, but a list of file names is provided. After the Item object is
             created, one Dataset object will be created for each file name and related to the
             ItemRevision. File tickets will be passed back to the user in the CreateAttachResponse
             object so that the files can be uploaded to the Dataset objects' named references.
             Then the newly created Item is submitted to the specified workflow.
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param Inputs: 
                         Each CreateIn2 object has a client id which can be used to map to any partial errors
                         in the ServiceData information returned in the output.
             
        :return: 33028 - The template (value) cannot be found.
        """
        ...

