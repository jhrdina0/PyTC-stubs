import System
import Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DecomposeOutput2:
    """
    
            The DecomposeOutput2 struct is used to hold the data returned by the decomposeContentWithMetaData
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique client identifier"""
    TopicRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The root topic or publication revision of decomposed content."""
    DecomposedMetaDataReadTicket: str
    """
            The decomposed meta data xml transient file read ticket. The file contains information
            about the items and relationships created during decompose.
            """

class DecomposeResponse2:
    """
    
            Return value for the decompose operation. It contains decompose output as well as
            ServiceData which contains partial errors.
            
    """
    def __init__(self, ) -> None: ...
    DecomposeOutput2: list[DecomposeOutput2]
    """A vector of Decomposed Output structs."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data."""

class ContentManagement:
    """
    Interface ContentManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def DecomposeContentWithMetaData(self, Inputs: list[Teamcenter.Services.Strong.Contmgmtbase._2011_06.ContentManagement.DecomposeInput]) -> DecomposeResponse2:
        """    
             The decompose operation breaks up the XML based on its schema into smaller XML segments.
             The XML segments are then stored as Datasets that are attached to DC_Topic
             or DC_Publication objects in Teamcenter. If an XML is decomposed for the first
             time, for example through the import operation, then new DC_Topic or DC_Publication
             objects are created to hold the Datasets. Otherwise the Datasets attached
             to existing objects are updated with any new content.
             

Use Cases:

Use case 1: Edit and Save

             After the user finishes editing a document created with a composeContent call, user
             can save the changes back into Teamcenter Content Management. To save the changes
             they can call decomposeContent with a keyValueArgs entry Type = Save_from_edit.This
             will decompose the edited document, compare it with the original composed document
             and update the database with any changes.
             
Use case 2: Import or receive a translation

             After a topic has been translated, user can import the translation in to Teamcenter
             Content Management. To import a translation the user can call this operation with
             a keyValueArgs entry Type = Translation_receive. This will add or update a translation
             in the entered language for the Topic that was translated.
             
Use case 3: Import an XML Document

             Users can import a new Topic or Publication into Teamcenter Content Management. To
             import a new Topic or Publication into the database, the user can call decomposeContent
             with a keyValueArgs entry Type = Import.
             
Use case 4: Import DITA map

             Users can import a DITA Map into Teamcenter Content Management. To import a new DITA
             map into the database, the user can call decomposeContent with a keyValueArgs entry
             Type = ImportDitaMap.
             

Dependencies:

             composeContent
             

Teamcenter Component:

             Content Management - New Content Management module that provides the capability to
             create/reuse/manage compound documents based on SGML/XML in Tc.
             
        :param Inputs: 
                         A vector of DecomposeInput structs. Each item in the vector represents an XML file
                         that will be decomposed. See DecomposeInput for more details.
             
        :return: 239175: A reference cannot be created to a topic that doesn't exist
        """
        ...

