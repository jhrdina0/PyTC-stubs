import Mes0.Services.Strong.Mes._2010_09.WorkInstructions
import Mes0.Services.Strong.Mes._2012_09.WorkInstructions
import Mes0.Services.Strong.Mes._2013_05.WorkInstructions
import System
import Teamcenter.Soa.Client
import typing

class WorkInstructionsRestBindingStub(WorkInstructionsService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    @typing.overload
    def LoadWorkInstructionDoc(self, LoadedInfo: list[Mes0.Services.Strong.Mes._2010_09.WorkInstructions.ObjectsReferenced]) -> Mes0.Services.Strong.Mes._2010_09.WorkInstructions.LoadedObjectsResponse: ...
    @typing.overload
    def LoadWorkInstructionDoc(self, LoadedInfo: list[Mes0.Services.Strong.Mes._2012_09.WorkInstructions.ObjectsReferenced]) -> Mes0.Services.Strong.Mes._2012_09.WorkInstructions.LoadedObjectsResponse: ...
    @typing.overload
    def LoadWorkInstructionDoc(self, LoadedInfo: list[Mes0.Services.Strong.Mes._2013_05.WorkInstructions.ObjectsReferenced]) -> Mes0.Services.Strong.Mes._2013_05.WorkInstructions.LoadedObjectsResponse: ...
    @typing.overload
    def SaveWorkInstructionDoc(self, SavedObjects: list[Mes0.Services.Strong.Mes._2010_09.WorkInstructions.SavedObjectInfo]) -> Mes0.Services.Strong.Mes._2010_09.WorkInstructions.SavedObjectsResponse: ...
    @typing.overload
    def SaveWorkInstructionDoc(self, SavedObjects: list[Mes0.Services.Strong.Mes._2012_09.WorkInstructions.SavedObjectInfo]) -> Mes0.Services.Strong.Mes._2012_09.WorkInstructions.SavedObjectsResponse: ...
    @typing.overload
    def SaveWorkInstructionDoc(self, SavedObjects: list[Mes0.Services.Strong.Mes._2013_05.WorkInstructions.SavedObjectInfo]) -> Mes0.Services.Strong.Mes._2013_05.WorkInstructions.SavedObjectsResponse: ...

class WorkInstructionsService:
    """
    
            The WorkInstructions service provides operations to load and save work instructions
            data in Manufacturing Process Planning application.
            
            The service provides following use cases for the Teamcenter manufacturing structures.
            

Load and save standard text document using one or more Mes0MEDCD,
            Mes0MEPF, Mes0MESymbol objects.
            
Load and save textual work instruction document using one or more
            Mes0MEDCD, Mes0MEPF, Mes0MESTXElementRevision objects.
            


            During the process of save it
            

Creates one or more Mes0MEDCD, Mes0MEPF objects for
            a BOPLine.
            
Relates Mes0MESymbol to Mes0MESTXElementRevision using
            a Mes0MESymbolRelation and Mes0MEWIAssets object to Mes0MESTXElementRevision,
            MEProcessRevision or MEOPRevision using Mes0MEWIAssetsRelation.
            
Relates Mes0MESTXElementRevision to MEProcessRevision
            or MEOPRevision.
            
Modifies existing Mes0MEDCD, Mes0MEPF and Mes0MEWIAssets
            objects.
            


            During the process of load it
            

Collects the Mes0MEWIAssets object to load the work instruction
            document.
            
Collects the Mes0MEDCD, Mes0MEPF and Mes0MESTXElementRevision
            and embeds them in the work instruction document and provides this document to the
            client.
            




Library Reference:

Mes0SoaMESStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> WorkInstructionsService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    @typing.overload
    def LoadWorkInstructionDoc(self, LoadedInfo: list[Mes0.Services.Strong.Mes._2010_09.WorkInstructions.ObjectsReferenced]) -> Mes0.Services.Strong.Mes._2010_09.WorkInstructions.LoadedObjectsResponse: ...
    @typing.overload
    def LoadWorkInstructionDoc(self, LoadedInfo: list[Mes0.Services.Strong.Mes._2012_09.WorkInstructions.ObjectsReferenced]) -> Mes0.Services.Strong.Mes._2012_09.WorkInstructions.LoadedObjectsResponse: ...
    @typing.overload
    def LoadWorkInstructionDoc(self, LoadedInfo: list[Mes0.Services.Strong.Mes._2013_05.WorkInstructions.ObjectsReferenced]) -> Mes0.Services.Strong.Mes._2013_05.WorkInstructions.LoadedObjectsResponse: ...
    @typing.overload
    def SaveWorkInstructionDoc(self, SavedObjects: list[Mes0.Services.Strong.Mes._2010_09.WorkInstructions.SavedObjectInfo]) -> Mes0.Services.Strong.Mes._2010_09.WorkInstructions.SavedObjectsResponse: ...
    @typing.overload
    def SaveWorkInstructionDoc(self, SavedObjects: list[Mes0.Services.Strong.Mes._2012_09.WorkInstructions.SavedObjectInfo]) -> Mes0.Services.Strong.Mes._2012_09.WorkInstructions.SavedObjectsResponse: ...
    @typing.overload
    def SaveWorkInstructionDoc(self, SavedObjects: list[Mes0.Services.Strong.Mes._2013_05.WorkInstructions.SavedObjectInfo]) -> Mes0.Services.Strong.Mes._2013_05.WorkInstructions.SavedObjectsResponse: ...

