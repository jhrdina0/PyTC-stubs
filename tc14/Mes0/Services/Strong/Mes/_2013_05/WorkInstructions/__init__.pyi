import Mes0.Services.Strong.Mes._2012_09.WorkInstructions
import System
import Teamcenter.Soa.Client.Model
import typing

class LoadedObjectInfo:
    """
    
            Conatins loaded targetObjects (MEProcessRevision,MEOPRevision or Mes0MESTXElementRevision)
            along with the elements of work instructions document i.e.(Mes0MEDCD, Mes0MEPF
            and Mes0MESymbol).
            
    """
    def __init__(self, ) -> None: ...
    TargetContext: Teamcenter.Soa.Client.Model.ModelObject
    """
            The context object (MEProcessRevision or MEOPRevision) to help client
            identify to whom these loaded information belongs.
            """
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The tag of the object loaded (Mes0MESTXElementRevision, MEProcessRevision
            or MEOPRevision).
            """
    WorkInstructionFile: str
    """
            File name of the work instructrion document located in the transient volume. If this
            is the first time this object is viewed in the editor a file will be created.
            """
    TargetObjectTransientId: str
    """A transient ID created by the server to identify the target object."""
    TopObjectDisplayName: str
    """The display name of the target object."""
    LoadedDCDs: list[Mes0.Services.Strong.Mes._2012_09.WorkInstructions.LoadedSubSTXInfo]
    """
            List of loaded Mes0MEDCD objects, could be direct Mes0MEDCDs belonging
            to the target object or / and Mes0MEDCDs to belonging to one of the Mes0MESTXElementRevision
            assigned to target object.
            """
    LoadedPFs: list[Mes0.Services.Strong.Mes._2012_09.WorkInstructions.LoadedSubSTXInfo]
    """
            List of loaded Mes0MEPFs, could be direct Mes0MEPFs belonging to the
            target object or Mes0MEPFs belongs to one of the Mes0MESTXElementRevision
            assigned to target object.
            """
    Symbols: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of all the Mes0MESymbol objects belonging to the target object."""
    LoadedSTXs: list[Mes0.Services.Strong.Mes._2012_09.WorkInstructions.LoadedSTXInfo]
    """
            List of loaded Mes0MESTXElementRevision elements added to the MEProcessRevision
            or MEOPRevision.
            """
    ReferencedObjectInfo: list[LoadedReferencedObjectInfo]
    """
            A list of structure LoadedReferencedObjectInfo holding transient ID i.e. the ID for
            the content control holding reference and referenced Dataset object in textual
            work instructions.
            """

class LoadedObjectsResponse:
    """
    LoadedObjectsResponse
    """
    def __init__(self, ) -> None: ...
    LoadedObjects: list[LoadedObjectInfo]
    """
            A vector of the load information for each targetObject and targetContext (each combination
            of targetObject and targetContext will have its own work instruction file and its
            own unique list of objects)
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class LoadedReferencedObjectInfo:
    """
    
            Structure to hold transient ID i.e. the ID for the content control holding reference
            and referencedObject in Textual Work Instructions.
            
    """
    def __init__(self, ) -> None: ...
    TransientId: str
    """Transient ID from client for referenced object."""
    ReferencedObject: Teamcenter.Soa.Client.Model.ModelObject
    """Referenced Object. These can be any datasets in Teamcenter."""

class ObjectsReferenced:
    """
    
            A list of objects and context which will give us a resulted document of the object
            configured according to the context.
            
    """
    def __init__(self, ) -> None: ...
    TargetContext: Teamcenter.Soa.Client.Model.ModelObject
    """
            A top line of the context we want the element to be configured according to it- if
            non supplied will use the referenceObject current context.
            """
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Object which has WorkInstruction Dataset it can be Mfg0BVROperation, Mfg0BVRProcess,
            MES0BVRStxElement.
            """

class SavedObjectInfo:
    """
    
            A structure consists of the edited object, the docx file related to it and all its
            modified objects in the current session.
            
    """
    def __init__(self, ) -> None: ...
    WorkInstructionFileTicket: str
    """File ticket of the work instruction file uploaded to the server."""
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The tag of the object edited (Mes0MESTXElementRevision, MEProcessRevision
            or MEOPRevision).
            """
    ModifiedDCDs: list[Mes0.Services.Strong.Mes._2012_09.WorkInstructions.SavedSubSTXInfo]
    """
            List of new or updated Mes0MEDCD objects ,could be direct Mes0MEDCDs
            belonging to the target object or / and Mes0MEDCDs to belonging to one of
            the Mes0MESTXElementRevision assigned to target object.This parameter can
            be empty.
            """
    ModifiedPFs: list[Mes0.Services.Strong.Mes._2012_09.WorkInstructions.SavedSubSTXInfo]
    """
            List of new\ updated Mes0MEPFs, could be direct Mes0MEPFs belonging
            to the target object or Mes0MEPFs  belongs to one of the Mes0MESTXElementRevision
            assigned to target object. This parameter can be empty.
            """
    Symbols: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            List of all the Mes0MESymbol objects belonging to the target object. This
            parameter can be empty.
            """
    ModifiedSTXs: list[Mes0.Services.Strong.Mes._2012_09.WorkInstructions.SavedSTXInfo]
    """
            List of new or modified Mes0MESTXElementRevision elements added to the MEProcessRevision
            or MEOPRevision. This can be empty in case the operation is called for saving
            standard text document or if work instruction document does not contain any Mes0MESTXElementRevision
            elements in it.
            """
    ReferencedObjectInfo: list[SavedReferencedObjectInfo]
    """
            A list of structure SavedReferencedObjectInfo  holding transient ID i.e. the ID for
            the content control holding reference and referenced Dataset object in textual
            work instructions. This can be empty if the save operation is for saving the standard
            text document or if the textual work instruction document does not contain any referenced
            Dataset.
            """

class SavedObjectsResponse:
    """
    SavedObjectsResponse
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class SavedReferencedObjectInfo:
    """
    
            Structure to hold transient ID i.e. the ID for the content control holding reference
            and referencedObject in Textual Work Instructions.
            
    """
    def __init__(self, ) -> None: ...
    TransientId: str
    """Transient ID from client for referenced object."""
    ReferencedObject: Teamcenter.Soa.Client.Model.ModelObject
    """This can be any Dataset in Teamcenter."""

class WorkInstructions:
    """
    Interface WorkInstructions
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def LoadWorkInstructionDoc(self, LoadedInfo: list[ObjectsReferenced]) -> LoadedObjectsResponse:
        """    
             This operation loads the work instructions document for a given target object (Mes0MESTXElementRevision,
             MEProcessRevision or MEOPRevision). It receives as input target object
             (Mes0MESTXElementRevision, MEProcessRevision or MEOPRevision)
             and context object (in case when Mes0MESTXElementRevision is being added to
             the MEProcessRevision or MEOPRevision).
             

Use Cases:

Use case 1: Load standard text document

             The user either loads the out of the box word template document or earlier saved
             standard text document in standard text view in client. To do this, the user selects
             the Mes0MESTXElementRevision in Manufacturing Process Planner application.
             The application either loads the empty template or collects Mes0MEDCD, a Mes0MEPF
             and Mes0MESymbol object related to Mes0MESTXElementRevision, embeds
             them in work instruction document and provides complete loaded standard text document
             to the client along with the model objects.
             
Use case 2: Load work instructions document

             The user either loads the out of the box word template document or earlier saved
             work instructions document in work instructions view in client. To do this, the user
             selects either MEProcessRevision or MEOPRevision in Manufacturing Process
             Planner application. The application loads the empty template or collects Mes0MEDCD,
             Mes0MEPF, Mes0MESymbol and Mes0MESTXElementRevision objects
             related to MEProcessRevision or MEOPRevision, embeds them in textual
             work instruction and provides complete loaded work instructions document to the client
             along with the model objects.
             
        :param LoadedInfo: 
                         A list of target objects (<b>Mes0MESTXElementRevision</b>, <b>MEProcessRevision</b>
                         or <b>MEOPRevision</b>), and context object (in case when <b>Mes0MESTXElementRevision</b>
                         is added to the <b>MEProcessRevision</b> or <b>MEOPRevision</b>).
             
        :return: 
        """
        ...
    def SaveWorkInstructionDoc(self, SavedObjects: list[SavedObjectInfo]) -> SavedObjectsResponse:
        """    
             This operation updates the work instructions for a given target object (Mes0MESTXElementRevision,
             MEProcessRevision or MEOPRevision). It receives as input work instructions
             file edited by the client application, with a list of modified model objects (Mes0MEDCD,
             Mes0MEPF) and their properties, and updates the work instructions model accordingly.
             The document is also modified with the internal IDs for all objects and save the
             data model.
             

Use Cases:

Use case 1: Save standard text document

             The user loads the out of the box word template document in standard text view in
             client. User creates one or more Mes0MEDCD, Mes0MEPF objects, embeds
             one or more Mes0MESymbol objects in standard text document and then perform
             save action. The application creates required objects in Teamcenter.
             
Use case 2: Save textual work instructions document

             The user loads the out of the box word template document in textual work instructions
             view in client. User creates one or more Mes0MEDCD, Mes0MEPF objects,
             embeds one or more standard text document and then perform save action. The application
             creates required objects in Teamcenter.
             
        :param SavedObjects: 
                         A list of target object (<b>Mes0MESTXElementRevision</b>, <b>MEProcessRevision</b>
                         or <b>MEOPRevision</b>), the work instruction document related to it and all its
                         modified objects (<b>Mes0MEDCD</b>, <b>Mes0MEPF</b>) in the current session.
             
        :return: 254005 - Work instruction document can not be saved for the target object supplied.
        """
        ...

