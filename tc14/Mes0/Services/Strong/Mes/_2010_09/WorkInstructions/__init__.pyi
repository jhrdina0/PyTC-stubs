import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class CreateInput:
    """
    
            CreateInput structure used to capture the inputs required for creation of a business
            object. This is a recursive structure containing the CreateInput(s) for any secondary
            (compounded) objects that might be created (e.g Item also creates ItemRevision and
            ItemMasterForm, etc.)
            
    """
    def __init__(self, ) -> None: ...
    Type: str
    """Business Object type name"""
    StringProps: System.Collections.Hashtable
    """Map containing string property values"""
    StringArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""
    DoubleProps: System.Collections.Hashtable
    """Map containing string property values"""
    DoubleArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""
    FloatProps: System.Collections.Hashtable
    """Map containing string property values"""
    FloatArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""
    IntProps: System.Collections.Hashtable
    """Map containing string property values"""
    IntArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""
    BoolProps: System.Collections.Hashtable
    """Map containing string property values"""
    BoolArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""
    DateProps: System.Collections.Hashtable
    """Map containing DateTime property values"""
    DateArrayProps: System.Collections.Hashtable
    """Map containing DateTime array property values"""
    TagProps: System.Collections.Hashtable
    """Map containing string property values"""
    TagArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""
    CompoundCreateInput: System.Collections.Hashtable
    """CreateInput for compounded objects"""

class LoadedObjectInfo:
    """
    LoadedObjectInfo
    """
    def __init__(self, ) -> None: ...
    TargetContext: Teamcenter.Soa.Client.Model.ModelObject
    """
            we pass this parameter together with the targetObject parameter back to the client
            to help him identify to whom these loaded information belongs
            """
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            we pass this parameter together with the targetContext parameter back to the client
            to help him identify to whom these loaded information belongs
            """
    WorkInstructionFile: str
    """
            file name of the docx file located in the transient volume, If this is the first
            time this object is viewed in the editor a file will be created (and an appropriate
            error will be supplied)
            """
    TargetObjectTransientId: str
    """A transient ID created by the server to identify the top object."""
    TopObjectDisplayName: str
    """The display name of the target object."""
    LoadedDCDs: list[LoadedSubSTXInfo]
    """
            a Vector containing all the available DCDs in this workInstruction document, could
            be direct DCDs attached to the TargetObject and\or DCDs assigned to one of its assigned
            STXs
            """
    LoadedPFs: list[LoadedSubSTXInfo]
    """
            a Vector containing all the available PFs in this workInstruction document, could
            be direct PFs attached to the TargetObject or PFs assigned to one of its assigned
            STXs
            """
    Symbols: list[Teamcenter.Soa.Client.Model.ModelObject]
    """list of symbols attached to the targetObject"""
    LoadedSTXs: list[LoadedSTXInfo]
    """
            a Vector containing the assigned STX elementss in the operation\process workinstruction
            document
            """

class LoadedObjectsResponse:
    """
    LoadedObjectsResponse
    """
    def __init__(self, ) -> None: ...
    LoadedObjects: list[LoadedObjectInfo]
    """
            a vector of the Load Information for each TargetObject and TargetContext (each combination
            of TargetObject and TargetContext will have it's own WorkInstruction file and its
            own unique list of objects)
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""

class LoadedSTXInfo:
    """
    LoadedSTXInfo
    """
    def __init__(self, ) -> None: ...
    TransientId: str
    """
            the transient ID of the assigned Stx element (In this case we don't need to generate
            a transient ID and can use the OccurrenceThreadStable ID of the Stx element).
            """
    WorkInstructionFile: str
    """
            the work instruction file name in the transient volume for this element, the client
            will compose the entire work instruction document by pasting the content of this
            file in the operation\process workinstruction file (the client will find the exact
            paste location by using the transient ID)
            """
    StxObjectData: Teamcenter.Soa.Client.Model.ModelObject
    """the mes0ObjectData  property of the mes0BVRSTXElement object"""
    Symbols: list[Teamcenter.Soa.Client.Model.ModelObject]
    """list of symbols attached to this Stx element."""

class LoadedSubSTXInfo:
    """
    LoadedSubSTXInfo
    """
    def __init__(self, ) -> None: ...
    TransientId: str
    """the transient ID of the assigned DCD\PF element"""
    ObjectData: CreateInput
    """A createInput object holding the appropriate DCD\PF Form attributes"""
    ObjectType: str
    """the type of the DCD\PF Form Object attached to this DCD\PF element"""
    OwningObjectTransientId: str
    """
            for example for a DCD assigned to an operation it's the operation object transientId,
            DCD\PF assigned to an STX and the STX is assigned to an operation is the STX transientId
            """
    PersistentId: str
    """
            A persistent identifier for the DCD\PF object, will not be used by the client (the
            client will pass it to the server through the save functionality)
            """

class ObjectsReferenced:
    """
    
            a list of objects and context which will give us a resulted document of the object
            configured according to the context
            
    """
    def __init__(self, ) -> None: ...
    TargetContext: Teamcenter.Soa.Client.Model.ModelObject
    """
            a top line of the context we want the element to be configured according to it- if
            non supplied will use the referenceObject current context
            """
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Object which has WorkInstruction Dataset it can be Mfg0BVROperation, Mfg0BVRProcess,
            MES0BVRStxElement
            """

class SavedObjectInfo:
    """
    
            a struct consist of the edited object, the docx file related to it and all its modified
            objects in the current session.
            
    """
    def __init__(self, ) -> None: ...
    WorkInstructionFile: str
    """
            File ticket number used by client to upload the file to PLM. Server implementation
            will use this ticket number to get the filepath of the uploaded file
            """
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            the tag of the object edited (it could be the Stx or Operation\Process). Input should
            be of type ImanItemBOPLine
            """
    ModifiedDCDs: list[SavedSubSTXInfo]
    """
            list of new\ updated DCDs ,could be direct DCDs belonging to the target Object or\and
            DCDs to belongs to one of the STXs assigned to target object
            """
    ModifiedPFs: list[SavedSubSTXInfo]
    """
            list of new\ updated PFs, could be direct PFs belonging to the target Object or (not
            as in modifiedDCDs case)PFs  belongs to one of the STXs assigned to target object
            """
    Symbols: list[Teamcenter.Soa.Client.Model.ModelObject]
    """of all the symbols belonging to the target object."""
    ModifiedSTXs: list[SavedSTXInfo]
    """list of new Stx elements add to the process\operation"""

class SavedObjectsResponse:
    """
    SavedObjectsResponse
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""

class SavedSTXInfo:
    """
    struct containing new STXs
    """
    def __init__(self, ) -> None: ...
    TransientId: str
    """a Unique transient ID for new STX"""
    StxObjectData: Teamcenter.Soa.Client.Model.ModelObject
    """the mes0StxObjectData property of the assigned line"""

class SavedSubSTXInfo:
    """
    struct containing  new\ updated DCD\PF info
    """
    def __init__(self, ) -> None: ...
    TransientId: str
    """a Unique transient ID for new DCD\PF"""
    PersistentId: str
    """
            A persistent identifier for the DCD\PF object (the client will get it through the
            load functionality)
            """
    OwningObjectTransientId: str
    """
            for example for a DCD assigned to an operation it's the operation object transientId
            (the client got it in the load functionality),PF\DCD assigned to an STX and the STX
            is assigned to an operation is the STX transientId
            """
    ObjectData: CreateInput
    """the runtime object for the DCD\PF Form object"""

class WorkInstructions:
    """
    Interface WorkInstructions
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def LoadWorkInstructionDoc(self, LoadedInfo: list[ObjectsReferenced]) -> LoadedObjectsResponse:
        """    
             This SOA returns for each given object in a given context its work instructions the
             work instruction document with the data for all the model objects it contains.
             
        :param LoadedInfo: 
                         a list of objects and context which will give us a resulted document of the object
                         configured according to the context
             
        :return: this session loaded object ServiceData will have the following errors 1) NewWIFileError:
             will be used when a WI file was not found. In that case a new file is created 2)
             ObjectNotFoundInStructureError  -if an object is reference in the dataset but not
             found in the structure 3) TextNotfoundInStructureError : if a Text element ID not
             t appear in the WI dataset attributes. 4) AnotherWIRevsionConfiguredError : when
             configuring the reference object according to the TargetContext will result in a
             different revision.
        """
        ...
    def SaveWorkInstructionDoc(self, SavedObjects: list[SavedObjectInfo]) -> SavedObjectsResponse:
        """    
             This service updates the work instructions for a given target object. It receives
             as input a WI file edited by the client application, with a list of modified model
             objects and their properties, and updates the WI model accordingly. The document
             will also be modified with the internal IDs for all objects, and be saved together
             with the target object.
             
        :param SavedObjects: 
                         vector of modified objects
             
        :return: The service data will return the following errors: 1) SavingDenied When a permission
             problem will restrict you from saving any of the data elements involve in the save.
        """
        ...

