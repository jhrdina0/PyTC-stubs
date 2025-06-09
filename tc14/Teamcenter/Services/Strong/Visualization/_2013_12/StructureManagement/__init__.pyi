import System
import System.Collections
import Teamcenter.Services.Strong.Visualization._2011_02.StructureManagement
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateVisSCsFromBOMsInfo:
    """
    
Input structure used for creating VisStrucutreContext objects based on the
given BOMWindows and specific occurrences within those BOMWindows.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    OccurrencesList: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """
            List of BOMLines representing the occurrences to be included in the structure
            recipe.
            """
    StaticStructureFile: Teamcenter.Soa.Client.Model.Strong.ImanFile
    """
IMANFile reference to the PLMXML static representation of the structure. If
            not supplied then the associated property of the VisStructureContext will
            not be set. [optional]
            """
    CreateVisSCOptions: System.Collections.Hashtable
    """
            A list of options that are to be considered when creating VisStructureContext
            objects during the execution of this operation. This list of options is represented
            by a map of string option names to string option values. The values are represented
            as a list of strings. The size of this list is dependent on the particular option
            being defined.
            """

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateVisSCsFromBOMsWithOptions(self, Info: list[CreateVisSCsFromBOMsInfo], GlobalOptions: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Visualization._2011_02.StructureManagement.CreateVisSCsFromBOMsResponse:
        """    
             This operation takes a list of BOMLines (the occurrences list) and returns
             the VisStructureContext objects representing the configuration state of the
             BOMWindow (referred to as the configuration recipe). This configuration includes:
             

The occurrence UID chains for the input/selected BOMLines
             up to but not including the top line.
             
Optional IMANFile reference to the PLMXML static representation
             of the BOMWindow.
             



             This service supports both the interoperation of selected BOMLines from the
             Teamcenter Rich Client to Teamcenter Visualization and also the capture/persistence
             of the configuration recipe for a particular BOMWindow. The occurrence list
             records the selected BOMLines at the time of interoperation and can be used
             in later operations to populate/expand a BOMWindow with those same occurrences.
             

Use Cases:

             When the user desires to create a persistent object that records the configuration
             recipe of a particular BOMWindow. The resulting VisStructureContext
             object would assumedly be used to later reconstruct a BOMWindow with the same
             configuration recipe and the recorded UID occurrence chains would be used to populate/expand
             the constructed BOMWindow with specific BOMLines. For example, this
             operation is used when sending selected BOMLines from the Structure Manager
             to Teamcenter Visualization and also to capture the configuration recipe for storage
             in Vis Sessions.
             

             Visualization pruned launch use case
             

User opens a structure in Structure Manager (SM)/Multi Structure
             Manager (MSM)/Manufacturing Process Planner (MPP), and configures it
             
User selects some lines they want to send to visualization as a pruned
             structure
             
System calls createVisSCsFromBOMsWithOptions to record the selected
             lines and the configuration of the BOM to send
             



             Visualization session save use case
             

1.    User performs Visualization pruned launch
             use case and loads occurrences into visualization
             
2.    User creates some authored visualization
             content (e.g. snapshots, motions, etc)
             
3.    User saves session to Teamcenter
             
4.    System calls createRecipesFromBOMs operation
             to capture the configuration and any pruning information as a VisStructureContext
             object.  UID of object returned.
             
5.    System writes the VisStructureContext
             object reference into the visualization session data
             
6.    System saves the visualiation session dataset
             to Teamcenter, and relates it to the VisStructureContext object created by
             the service
             



             Visualization Technical Illustration and 3D Markup save use cases
             
             Similar to session save use case, except saving a different data type.  Uses this
             service to create the recipe for the authored visualization data in the Teamcenter
             data model.
             

             Use Case Dependencies:
             
             The createVisSCsFromBOMsWithOptions operation is called with input BOMLines
             from an existing BOM Window. Therefore, the BOMWindow must have already been
             created and populated with at least a top line.
             

Teamcenter Component:

             Teamcenter Visualization - Application to allow view and markup of multicad product
             structure that has a jt representation.
             
        :param Info: 

        :param GlobalOptions: 
                         The list of global options the caller wishes to provide to the operation. These options
                         apply to each <b>VisStructureContext</b> object that is created as a result of this
                         operation (as opposed to the options present in the <i>info</i> input parameter that
                         only apply to that given <b>VisStructureContext</b>). This list of options is represented
                         by a map of string option names to string option values. The values are represented
                         as a list of strings. The size of this list is dependent on the particular option
                         being defined.
             
        :return: 
        """
        ...

