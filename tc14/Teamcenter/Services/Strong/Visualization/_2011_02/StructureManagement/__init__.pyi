import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateVisSCInfo:
    """
    
Input structure used for creating VisStrucutreContext objects based on the
given inputs.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            
"""
    ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            A reference to an existing ConfigurationContext object that contains a portion
            of the configuration to be used by the output VisStructureContext object.
            
"""
    TopLine: Teamcenter.Soa.Client.Model.ModelObject
    """
            Object reference of type BOMView or BOMViewRevision that is the topline
            of the configuration.
            
"""
    OccurrencesList: list[str]
    """
            List of UID chain strings representing  the occurrences to be included in the structure
            recipe. If not supplied then the output VisStructureContext object will not
            have its
            
            occurrence_list property set. This will be interpreted as the top line was
            selected BOMLine for this configuration recipe.
            
"""
    StaticStructureFile: Teamcenter.Soa.Client.Model.ModelObject
    """IMANFile reference to the PLMXML static representation of the structure, (optional)."""

class CreateVisSCOutput:
    """
    
The output structure that contains the references to the created
VisStructureContext
object along with the corresponding clientId.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unique string supplied by the caller used to match the output to the supplied
            input.
            """
    StructureRecipe: Teamcenter.Soa.Client.Model.Strong.VisStructureContext
    """
VisStructureContext object that records the configuration recipe based on
            the input configuration objects
            
"""

class CreateVisSCResponse:
    """
    Response structure for the createVisSC operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateVisSCOutput]
    """
            List of CreateVisSCOutput structures containing
            the VisStructureContext objects created based on the input configuration objects.
            
"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class CreateVisSCsFromBOMsInfo:
    """
    
Input structure used for creating VisStrucutreContext objects based on the
given BOMWindows and specific occurrenses within those BOMWindows.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            
"""
    OccurrencesList: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """
            List of BOMLines representing  the occurrences to be included in the structure
            recipe.
            """
    StaticStructureFile: Teamcenter.Soa.Client.Model.ModelObject
    """
IMANFile reference to the PLMXML static representation of the structure. If
            not supplied then the associated property of the VisStructureContext will
            not be set. [optional]
            
"""

class CreateVisSCsFromBOMsOutput:
    """
    
The output structure that contains the references to the created
VisStructureContext
objects along with the corresponding clientId.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unique string supplied by the caller used to match the output to the supplied
            input.
            """
    StructureRecipe: Teamcenter.Soa.Client.Model.Strong.VisStructureContext
    """
VisStructureContext object that records the configuration recipe of the BOMWindow
            that contains the input BOMLines

"""

class CreateVisSCsFromBOMsResponse:
    """
    
Response structure for the createVisSCsFromBOMs
operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateVisSCsFromBOMsOutput]
    """
            List of CreateVisSCsFromBOMsOutput structures
            containing the VisStructureContext object that records the configuration recipe
            of the BOMWindow from which the input BOMLines belong.
            
"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the Service, plain objects, and error information.
            """

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateVisSC(self, Info: list[CreateVisSCInfo]) -> CreateVisSCResponse:
        """    
             This operation takes a list of ConfigurationContext/top line object pairs
             and creates a VisStructureContext object based on that input. The user may
             optionally supply a list of occurrences in the form of UID chains and a file reference
             for the static PLMXML representation of the configuration. If an occurrence list
             or a static structure file are supplied they will be set as properties on the VisStructureContext
             object. The list of occurrences can be used to populate/expand any BOMWindows
             that are subsequently created using the output VisStructureContext object.
             

Use Cases:

             When the user desires to create a single persistent object that records a particular
             configuration recipe and the caller already has the component objects that make up
             the configuration. This case might occur if the configuration elements of a BOMWindow
             were captured but the BOMWindow was then deleted. This is often the case when
             using the Teamcenter Thin Client.
             


             The createVisSC operation requires input configuration objects and their top lines.
             Therefore, these objects must have been obtained based on some previous configuration
             scenario.
             


Teamcenter Component:

             Teamcenter Visualization - Application to allow view and markup of multicad product
             structure that has a jt representation.
             
        :param Info: 

        :return: object that records the
             configuration recipe.
        """
        ...
    def CreateVisSCsFromBOMs(self, Info: list[CreateVisSCsFromBOMsInfo]) -> CreateVisSCsFromBOMsResponse:
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
             configuration recipe and the recorded occurrence chains would be used to populate/expand
             the constructed BOMWindow with specific BOMLines. For example, this
             operation is used when sending selected BOMLines from the Structure Manager
             to Teamcenter Visualization and also to capture the configuration recipe for storage
             in Vis Sessions.
             

             Visualization pruned launch use case
             

User opens a structure in Structure Manager (SM)/Multi Structure
             Manager (MSM)/Manufacturing Process Planner (MPP), and configures it
             
User selects some lines they want to send to visualization as a pruned
             structure
             
System calls createVisSCsFromBOMs to record the selected lines and
             the configuration of the BOM to send
             



             The createVisSCsFromBOMs operation is called with input BOMLines from an existing
             BOMWindow. Therefore, the BOMWindow must have already been created
             and populated with at least a top line.
             

Teamcenter Component:

             Teamcenter Visualization - Application to allow view and markup of multicad product
             structure that has a jt representation.
             
        :param Info: 

        :return: 
        """
        ...

