import System
import System.Collections
import Teamcenter.Services.Strong.Cad._2007_01.DataManagement
import Teamcenter.Services.Strong.Cad._2007_01.StructureManagement
import Teamcenter.Services.Strong.Cad._2007_06.StructureManagement
import Teamcenter.Services.Strong.Cad._2007_09.StructureManagement
import Teamcenter.Services.Strong.Cad._2007_12.DataManagement
import Teamcenter.Services.Strong.Cad._2007_12.StructureManagement
import Teamcenter.Services.Strong.Cad._2008_03.DataManagement
import Teamcenter.Services.Strong.Cad._2008_03.StructureManagement
import Teamcenter.Services.Strong.Cad._2008_06.DataManagement
import Teamcenter.Services.Strong.Cad._2008_06.StructureManagement
import Teamcenter.Services.Strong.Cad._2009_04.StructureManagement
import Teamcenter.Services.Strong.Cad._2010_09.DataManagement
import Teamcenter.Services.Strong.Cad._2011_06.DataManagement
import Teamcenter.Services.Strong.Cad._2012_09.DataManagement
import Teamcenter.Services.Strong.Cad._2013_05.StructureManagement
import Teamcenter.Services.Strong.Cad._2014_10.DataManagement
import Teamcenter.Services.Strong.Cad._2016_03.DataManagement
import Teamcenter.Services.Strong.Cad._2016_03.StructureManagement
import Teamcenter.Services.Strong.Cad._2016_09.StructureManagement
import Teamcenter.Services.Strong.Cad._2018_06.StructureManagement
import Teamcenter.Services.Strong.Cad._2019_06.StructureManagement
import Teamcenter.Services.Strong.Cad._2020_01.AppSessionManagement
import Teamcenter.Services.Strong.Cad._2023_06.StructureManagement
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AppSessionManagementRestBindingStub(AppSessionManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateOrUpdateSavedSession(self, SessionsToCreateOrUpdate: list[Teamcenter.Services.Strong.Cad._2020_01.AppSessionManagement.SessionInfo]) -> Teamcenter.Services.Strong.Cad._2020_01.AppSessionManagement.CreateOrUpdateSessionResponse: ...
    def OpenSavedSession(self, SessionsToOpen: list[Teamcenter.Soa.Client.Model.ModelObject], Filter: Teamcenter.Services.Strong.Cad._2020_01.AppSessionManagement.OpenSavedSessionFilter) -> Teamcenter.Services.Strong.Cad._2020_01.AppSessionManagement.OpenSessionResponse: ...

class AppSessionManagementService:
    """
    
            This service provides operations to manage the session in a client application. The
            service provides operation using which the applications can save the session (i.e.
            what are the product structures and documents that were opened) and open the session.
            

Dependencies:

            DataManagement, StructureManagement, DataManagement
            


Library Reference:

TcSoaCadStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> AppSessionManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateOrUpdateSavedSession(self, SessionsToCreateOrUpdate: list[Teamcenter.Services.Strong.Cad._2020_01.AppSessionManagement.SessionInfo]) -> Teamcenter.Services.Strong.Cad._2020_01.AppSessionManagement.CreateOrUpdateSessionResponse:
        """    
             This operation creates or updates a session data model that captures product structure
             configuration rules, non structure object references (e.g. 2D drawings), and application
             specific data (e.g. markups, snaphsots) from a visualization enabled application.
             The session model is either a Fnd0WorksetRevision Object or a Fnd0AppSession(Session)
             Object referencing objects opened in client applications. The operation returns unique,
             copy stable ids for all the objects referenced by the session for persistence of
             it into CAD session files. Client specific objects can be associated to Fnd0AppSession
             with GRM relations or as sub class Fnd0ProductSessionData where the fnd0OwningObject
             property is referencing Fnd0AppSession.
             

Use Cases:

             The user may have opened multiple product structures, applied search filters on them
             and along with  it  may have opened other objects like Dataset or Form.
             The user then issues a save session command to capture the state of the session so
             that it can be restored for continuation of work or to share it other users with
             review markups.
             

             The mechanism for a client application(CAD) which captures the CAD related session
             setting in a session file and saves the opened products, documents and its state
             in Teamcenter as session, contains steps as below.
             

             User creates a Session
             

User opens product structures, Dataset, creates a review markup
             and saves the session.
             
Client application creates a Dataset that will contain the
             session assets information like Markup, Snapshot etc. using createDatasets or using BaseObjectAttachInfo.baseObjectToCreateOrUpdate.
             
The client application then invokes the createOrUpdateSavedSession
             where the input are the objects that were opened in the session and Dataset
             containing session assets. This step creates the session object and associates the
             input objects to the session with relevant relations as per the data model. Associated
             Dataset and ImanFile objects are then accessible to other authorized
             clients through the PLM system.
             



             User updates a Session
             

User searches for the Fnd0AppSession or Fnd0WorksetRevision
             he has saved.
             
Opens it in the client application that supports opening of Fnd0AppSession
             or Fnd0WorksetRevision.
             
The client application invokes openSavedSession
             operation which returns the objects associated to the session with its corresponding
             stable Ids.
             
The application restores his session as persisted by the Fnd0AppSession
             or Fnd0WorksetRevision.
             
User now closes some documents, opens new documents and/or modifes
             existing objects. For Fnd0WorksetRevision, the only supported updates are
             adding new product structures to the session, removing product structures, or updating
             the desired configuration or filtering of a product structure which is already in
             the session.
             
User now issues a command to save the session
             
The application invokes createOrUpdateSavedSession
             operation to update the object association to the session by identifying the association
             via stable Id.
             



Note: As a best practice, for a Fnd0AppSession but not Fnd0WorksetRevision
             session, if the configuration or search recipe of a product structure in an existing
             session is changed and saved by the user it is recommended that the application removes
             the the product structure from the session and adds the changed product structure
             to the session with the same stableId or using a new stable id.
             

Teamcenter Component:

             Teamcenter Visualization - Application to allow view and markup of multicad product
             structure that has a jt representation.
             
        :param SessionsToCreateOrUpdate: 
                         A list of <font face="courier" height="10">SessionInfo</font> data structures. Each
                         of the struct element is identified by a unique identifier assigned by the client
                         and holds information about the session that needs to be created or updated, list
                         of Teamcenter object information that will be associated to the session.
             
        :return: 
        """
        ...
    def OpenSavedSession(self, SessionsToOpen: list[Teamcenter.Soa.Client.Model.ModelObject], Filter: Teamcenter.Services.Strong.Cad._2020_01.AppSessionManagement.OpenSavedSessionFilter) -> Teamcenter.Services.Strong.Cad._2020_01.AppSessionManagement.OpenSessionResponse:
        """    
             This operation is used to open the documents and product structures that were saved
             to a session object using createOrUpdateSavedSession.
             For product structures, the configuration rules persisted with the session are used
             to recreate the correct BOM system configuration in effect when the session was last
             authored.  The client can either open all the documents and product structures associated
             to the session or selectively open by providing OpenSavedSessionFilter.
             The session object type that can be opened by this operation is Fnd0AppSession.
             

Use Cases:

             The user may have opened multiple product structures, applied search filters on them
             and along with  it  may have opened other objects like Dataset or Form.
             The user then issues a save session command to capture the state of the session so
             that it can be restored for continuation of work or share it other users with review
             markups.
             

             The mechanism for a client application(CAD) which captures the CAD related session
             setting in a session file and saves the opened products, documents and its state
             in Teamcenter as session, contains steps as below.
             

             1.    User opens product structures, Dataset, creates
             a review markup and saves the session.
             
             2.    Client application creates a Dataset that will contain
             the session assets information like Markup, Snapshot etc. using createDatasets. The client application then invokes the createOrUpdateSavedSession where the input are
             the objects that were opened in the session and Dataset containing session
             assets. This step creates the session object and associates the input objects to
             the session with relevant relations as per the data model. Associated Dataset
             and ImanFile objects are then accessible to other authorized clients through
             the PLM system.
             
             3.    Another user could search for the session created in step
             2 and issue a command in the application to open the session. The client application
             now invokes this operation to get all the objects and product structures that were
             associated to the session and present it to the user the way he persisted those in
             Teamcenter. The stable Id that uniquely identifies the association of a product structure
             or object to the session is also returned so that it can used to update the session
             when the user modifies the session.
             

Teamcenter Component:

             Teamcenter Visualization - Application to allow view and markup of multicad product
             structure that has a jt representation.
             
        :param SessionsToOpen: 
                         A list of <font face="courier" height="10">Teamcenter::BusinessObject</font> session
                         object that are to be opened. Valid session object is <b>Fnd0AppSession</b>.
             
        :param Filter: 
                         The filter to apply on the type of object and product structures that the client
                         application is interested in opening.
             
        :return: 
        """
        ...

class DataManagementRestBindingStub(DataManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    @typing.overload
    def CreateOrUpdateParts(self, Info: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.PartInfo]) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.CreateOrUpdatePartsResponse: ...
    @typing.overload
    def CreateOrUpdateParts(self, Info: list[Teamcenter.Services.Strong.Cad._2007_12.DataManagement.PartInfo2], Pref: Teamcenter.Services.Strong.Cad._2007_12.DataManagement.CreateOrUpdatePartsPref) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.CreateOrUpdatePartsResponse: ...
    @typing.overload
    def CreateOrUpdateParts(self, Info: list[Teamcenter.Services.Strong.Cad._2008_03.DataManagement.PartInfo3], Pref: Teamcenter.Services.Strong.Cad._2007_12.DataManagement.CreateOrUpdatePartsPref) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.CreateOrUpdatePartsResponse: ...
    @typing.overload
    def CreateOrUpdateParts(self, PartInput: list[Teamcenter.Services.Strong.Cad._2008_06.DataManagement.PartInfo], Pref: Teamcenter.Services.Strong.Cad._2007_12.DataManagement.CreateOrUpdatePartsPref) -> Teamcenter.Services.Strong.Cad._2008_06.DataManagement.CreateOrUpdatePartsResponse: ...
    @typing.overload
    def CreateOrUpdateParts(self, PartInput: list[Teamcenter.Services.Strong.Cad._2010_09.DataManagement.PartInfo], Pref: Teamcenter.Services.Strong.Cad._2007_12.DataManagement.CreateOrUpdatePartsPref) -> Teamcenter.Services.Strong.Cad._2008_06.DataManagement.CreateOrUpdatePartsResponse: ...
    @typing.overload
    def CreateOrUpdateParts(self, PartInput: list[Teamcenter.Services.Strong.Cad._2012_09.DataManagement.PartInfo], Pref: Teamcenter.Services.Strong.Cad._2007_12.DataManagement.CreateOrUpdatePartsPref) -> Teamcenter.Services.Strong.Cad._2008_06.DataManagement.CreateOrUpdatePartsResponse: ...
    def CreateOrUpdateRelations(self, Info: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.CreateOrUpdateRelationsInfo], Complete: bool, Pref: Teamcenter.Services.Strong.Cad._2007_01.DataManagement.CreateOrUpdateRelationsPref) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.CreateOrUpdateRelationsResponse: ...
    def ExpandGRMRelations(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExpandGRMRelationsPref) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExpandGRMRelationsResponse: ...
    def ExpandPrimaryObjects(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExpandPrimaryObjectsPref) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExpandPrimaryObjectsResponse: ...
    def GenerateAlternateIds(self, Input: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.GenerateAlternateIdsProperties]) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.GenerateAlternateIdsResponse: ...
    def GetAllAttrMappings(self) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.GetAllAttrMappingsResponse: ...
    def GetAttrMappingsForDatasetType(self, Info: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.GetAttrMappingsForDatasetTypeCriteria]) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.GetAttrMappingsForDatasetTypeResponse: ...
    def GetAvailableTypes(self, Classes: list[str]) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.GetAvailableTypesResponse: ...
    def ResolveAttrMappingsForDataset(self, Info: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ResolveAttrMappingsForDatasetInfo]) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ResolveAttrMappingsForDatasetResponse: ...
    @typing.overload
    def ExpandFoldersForCAD(self, Folders: list[Teamcenter.Soa.Client.Model.Strong.Folder], Pref: Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExpandFolderForCADPref) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExpandFoldersForCADResponse: ...
    @typing.overload
    def ExpandFoldersForCAD(self, Folders: list[Teamcenter.Soa.Client.Model.Strong.Folder], Pref: Teamcenter.Services.Strong.Cad._2008_06.DataManagement.ExpandFolderForCADPref2) -> Teamcenter.Services.Strong.Cad._2008_06.DataManagement.ExpandFoldersForCADResponse2: ...
    def ResolveAttrMappings(self, Info: list[Teamcenter.Services.Strong.Cad._2008_03.DataManagement.ResolveAttrMappingsInfo]) -> Teamcenter.Services.Strong.Cad._2008_03.DataManagement.ResolveAttrMappingsResponse: ...
    def GetAllAttrMappings2(self) -> Teamcenter.Services.Strong.Cad._2011_06.DataManagement.GetAllAttrMappingsResponse: ...
    def GetAttrMappings(self, Filter: list[Teamcenter.Services.Strong.Cad._2014_10.DataManagement.GetAttrMappingsFilter]) -> Teamcenter.Services.Strong.Cad._2014_10.DataManagement.GetAttrMappingsResponse: ...
    def CreateOrUpdateModelViewPalette(self, MvPaletteInfo: list[Teamcenter.Services.Strong.Cad._2016_03.DataManagement.ModelViewPaletteInfo]) -> Teamcenter.Services.Strong.Cad._2016_03.DataManagement.CreateOrUpdateMVPaletteResponse: ...
    def CreateOrUpdateModelViewProxies(self, MvProxyInfos: list[Teamcenter.Services.Strong.Cad._2016_03.DataManagement.ModelViewProxyInfo], UpdatedOwningModels: list[Teamcenter.Services.Strong.Cad._2016_03.DataManagement.OwningModelAndCadLmd]) -> Teamcenter.Services.Strong.Cad._2016_03.DataManagement.CreateOrUpdateModelViewProxiesResponse: ...

class DataManagementService:
    """
    
            The CAD DataManagement  service allows clients to create and expand Teamcenter data.
            Specifically, there are operations to support creating the CAD part concept (
            Item, ItemRevision, and Dataset ) createOrUpdateParts and
            createOrUpdateRelations. There are operations to expand data that CAD integrations
            are interested in ( expandFoldersForCAD and expandPrimaryObjects ).  There are also
            operations to work with the Teamcenter attribute mapping  functionality ( getAllAttrMappings,
            getAttrMappingsForDatasetType, resolveAttrMappings ).
            
            This service supports the following use cases for Teamcenter product structure:
            

Creation of CAD concept of Part ( Item/ItemRevision/Dataset
            ) as well as accompanying data such as named references and ancillary forms
            
Retrieving folder contents that CAD integrations are typically interested
            in : Item objects, ItemRevision objects, and Dataset objects
            
Retrieving attribute mappings for reading and writing CAD part mapped
            attributes
            




Library Reference:

TcSoaCadStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DataManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    @typing.overload
    def CreateOrUpdateParts(self, Info: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.PartInfo]) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.CreateOrUpdatePartsResponse: ...
    @typing.overload
    def CreateOrUpdateParts(self, Info: list[Teamcenter.Services.Strong.Cad._2007_12.DataManagement.PartInfo2], Pref: Teamcenter.Services.Strong.Cad._2007_12.DataManagement.CreateOrUpdatePartsPref) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.CreateOrUpdatePartsResponse: ...
    @typing.overload
    def CreateOrUpdateParts(self, Info: list[Teamcenter.Services.Strong.Cad._2008_03.DataManagement.PartInfo3], Pref: Teamcenter.Services.Strong.Cad._2007_12.DataManagement.CreateOrUpdatePartsPref) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.CreateOrUpdatePartsResponse: ...
    @typing.overload
    def CreateOrUpdateParts(self, PartInput: list[Teamcenter.Services.Strong.Cad._2008_06.DataManagement.PartInfo], Pref: Teamcenter.Services.Strong.Cad._2007_12.DataManagement.CreateOrUpdatePartsPref) -> Teamcenter.Services.Strong.Cad._2008_06.DataManagement.CreateOrUpdatePartsResponse: ...
    @typing.overload
    def CreateOrUpdateParts(self, PartInput: list[Teamcenter.Services.Strong.Cad._2010_09.DataManagement.PartInfo], Pref: Teamcenter.Services.Strong.Cad._2007_12.DataManagement.CreateOrUpdatePartsPref) -> Teamcenter.Services.Strong.Cad._2008_06.DataManagement.CreateOrUpdatePartsResponse: ...
    @typing.overload
    def CreateOrUpdateParts(self, PartInput: list[Teamcenter.Services.Strong.Cad._2012_09.DataManagement.PartInfo], Pref: Teamcenter.Services.Strong.Cad._2007_12.DataManagement.CreateOrUpdatePartsPref) -> Teamcenter.Services.Strong.Cad._2008_06.DataManagement.CreateOrUpdatePartsResponse: ...
    def CreateOrUpdateRelations(self, Info: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.CreateOrUpdateRelationsInfo], Complete: bool, Pref: Teamcenter.Services.Strong.Cad._2007_01.DataManagement.CreateOrUpdateRelationsPref) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.CreateOrUpdateRelationsResponse:
        """    
createOrUpdateRelations creates or updates
             GRM relations between existing objects in Teamcenter. If the complete flag is set and a filter is supplied, then any relation
             types that exist for primary objects in the info that are listed in the filter, but
             the relations are not sent in the input, those relations will be deleted.
             

Use Cases:

             The user wishes to relate two objects in Teamcenter. The user specifies the primary
             and secondary objects, the type of relation to be created and any optional data the
             user wants added to the relation.
             
             The user wishes to modify the user data on the relationship between two objects.
             The user specifies the primary and secondary objects and the existing relationship.
             The user also specifies the new user data to be placed on the relationship.
             
             The user wishes to relate two objects in Teamcenter and remove any existing relationships
             between the objects. The user specifies the primary and secondary objects, the type
             of relation to be created and any optional data the user wants added to the relation.
             The user also sets the complete option to
             true to delete the existing relationships that pass the supplied filter, but does
             not send those existing relationships in the input.  For example, there is an item
             revision and a dataset related with an IMAN_specification relationship in Teamcenter
             and the user wants to change this to an IMAN_Rendering relationship. The user can
             specify the item revision and the dataset, specify the new relationship is IMAN_Rendering
             and set the complete flag. With the filter
             specifying the relation type of IMAN_specification and the object type as dataset.
             This will delete the current relationship and create the new one.
             


Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Info: 
                         A list of <font face="courier" height="10">CreateOrUpdateRelationsInfo</font>

        :param Complete: 
                         A flag to check whether any existing relations that pass the filter needs to be deleted.
             
        :param Pref: 
                         A list of <font face="courier" height="10">RelationAndTypesFilter2</font> structure.
             
        :return: .
        """
        ...
    def ExpandGRMRelations(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExpandGRMRelationsPref) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExpandGRMRelationsResponse:
        """    
             Returns the secondary objects related to the input object for the given list of relation
             names and other side object types filter. If no relation names or other side objects
             types are provided in the input, then all related objects will be returned. In addition,
             for performance, if an Item is the output of the expansion, then its associated Item
             Revisions and the Datasets for those Item Revisions will be returned. Similarly,
             if an Item Revision is the output of the expansion, then its associated Datasets
             will be returned. However this additional expansion is controlled through the expItemRev
             flag.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Objects: 
                         A list of object references of objects of interest
             
        :param Pref: 
                         A ExpandGRMRelationsPref structure
             
        :return: contains a list of ExpandGRMRelationsOutput structures (which contain information
             about the input TcEng Object, filtered Otherside related objects and the relationName
             they are related). Failures and error message are in the ServiceData.
        """
        ...
    def ExpandPrimaryObjects(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExpandPrimaryObjectsPref) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExpandPrimaryObjectsResponse:
        """    
             Returns the secondary objects related to the input object for the given list of relation
             names and other side object types filter. If no relation names or other side objects
             types are provided in the input, then all related objects will be returned. In addition,
             for performance, if an Item is the output of the expansion, then its associated Item
             Revisions and the Datasets for those Item Revisions will be returned. Similarly,
             if an Item Revision is the output of the expansion, then its associated Datasets
             will be returned. However this additional expansion is controlled through the expItemRev
             flag.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Objects: 
                         A list of input TcEng object references and filter and expand preferences
             
        :param Pref: 
                         A ExpandPrimaryObjectsPref structure
             
        :return: contains a list of ExpandPrimaryObjectsOutput structures (which contain information
             about the input TcEng Object, filtered Otherside related objects and the relation/property
             Name they are related). Failures and error message are in the ServiceData.
        """
        ...
    def GenerateAlternateIds(self, Input: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.GenerateAlternateIdsProperties]) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.GenerateAlternateIdsResponse:
        """    
             Generate a list of alternate ids. An alternate id is a displayable id for an Item
             or ItemRevision that is controlled by the user via display rules. The client
             creates Identifiers that contain the various alternate ids to be displayed.
             Each Identifier is controlled by a display rule. When a display rule is active
             then the appropriate alternate id is displayed.
             

Use Cases:

             The client defines several alternate ids for a part. One alternate id is for the
             manufacturer of the part( this would be their part number ), another would be for
             a customer ( their part number ) and maybe one for a second customer ( again, another
             part number ). This service allows the client to invoke the user exit USER_new_alt_id.
             This exit will be called once for each count specified in the input using the data
             passed in as parameters.
             

Dependencies:

             getContextsAndIdentifierTypes
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Input: 
                         A list of <font face="courier" height="10">GenerateAlternateIdsProperties</font>.
             
        :return: Contains the map of index to list of ids generated. The index refers to the input
             data in the input list.
        """
        ...
    def GetAllAttrMappings(self) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.GetAllAttrMappingsResponse:
        """    
             Retrieves all CAD attribute mapping definitions. Additionally, if a CadAttributeMappingDefinition
             object has a path that includes a GRM or NR part, the associated PropertyDescriptor
             and any attached ListOfValues objects will be returned.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :return: 
        """
        ...
    def GetAttrMappingsForDatasetType(self, Info: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.GetAttrMappingsForDatasetTypeCriteria]) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.GetAttrMappingsForDatasetTypeResponse:
        """    
             This operation retrieves the CAD attribute mapping definitions for one or more dataset
             type and item type combinations.  If a CadAttributeMappingDefinition
             object has a path that includes a Generic Relationship Manager (GRM) or named reference
             part, the associated property descriptor and any attached ListOfValues
             (LOV) objects will be returned.
             

             Since this operation returns existing Teamcenter attribute mappings, please reference
             the Teamcenter help section on creating attribute mappings.
             


Use Cases:

             User needs to have attribute mappings defined in Teamcenter.
             

             For this operation, the dataset object type is passed as input. The client application
             uses the list of returned attribute mapping definitions to present the CAD attributes
             to the user that correspond to the correct Teamcenter attributes.
             


Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Info: 
                         A list of dataset and item types used to get a specific set of attribute mapping
                         definitions from the all of the attribute mapping definitions in Teamcenter.
             
        :return: 
        """
        ...
    def GetAvailableTypes(self, Classes: list[str]) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.GetAvailableTypesResponse:
        """    
             Finds types implemented by the given input class name.
             

Use Cases:

             User selects File New Item and is presented with a list of creatable item types.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Classes: 
                         A list of the classes to return subtypes for
             
        :return: with original input class string mapped to error message.
        """
        ...
    def ResolveAttrMappingsForDataset(self, Info: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ResolveAttrMappingsForDatasetInfo]) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ResolveAttrMappingsForDatasetResponse:
        """    
             Retrieves CAD attribute mapped properties for one or more datasets.
             

Use Cases:

             User does a FileOpen of Teamcenter Item or Dataset (CAD Part).  CAD properties mapped
             to Teamcenter attribute values are shown in the Part attribute display.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Info: 
                         An array of <font face="courier" height="10">ResolveAttrMappingsForDatasetInfo</font>
                         structures each containing a <b>Dataset</b> object reference, an optional item revision,
                         and a list of corresponding CAD Attribute Mapping Definitions to be resolved for
                         the dataset. The optional item revision is recommended for improved performance in
                         cases where resolution of the mapping string would otherwise require a relation query
                         to find the item revision.
             
        :return: 
        """
        ...
    @typing.overload
    def ExpandFoldersForCAD(self, Folders: list[Teamcenter.Soa.Client.Model.Strong.Folder], Pref: Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExpandFolderForCADPref) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExpandFoldersForCADResponse: ...
    @typing.overload
    def ExpandFoldersForCAD(self, Folders: list[Teamcenter.Soa.Client.Model.Strong.Folder], Pref: Teamcenter.Services.Strong.Cad._2008_06.DataManagement.ExpandFolderForCADPref2) -> Teamcenter.Services.Strong.Cad._2008_06.DataManagement.ExpandFoldersForCADResponse2: ...
    def ResolveAttrMappings(self, Info: list[Teamcenter.Services.Strong.Cad._2008_03.DataManagement.ResolveAttrMappingsInfo]) -> Teamcenter.Services.Strong.Cad._2008_03.DataManagement.ResolveAttrMappingsResponse:
        """    
             Retrieves CAD attribute mapped properties for item revisions or datasets.  Attribute
             Mapping is a scheme whereby Teamcenter attributes can be retrieved or set via a defined
             path to the attribute from the starting object, usually a dataset.  For example,
             a mapped attribute can be defined in the client integration with a particular name
             ATTR1.  Using Teamcenter attribute mapping, the customizer can define a path named
             ATTR1 from a starting point item revision type or dataset type to the actual attribute
             that holds the value for ATTR1. The client integration then can access the attribute
             using the attribute mapping title ATTR1 and the starting point object.
             
             For more information about Attribute Mapping including examples with syntax, please
             consult the "Configuring attribute mapping section" of the Application Administration
             Guide in Teamcenter Online Help.
             

Use Cases:

             A user performs a File Open operation on an existing Teamcenter dataset.  The client
             integration has defined an attribute mapping in Teamcenter for that Dataset type.
             The resolveAttrMappings call performed as a part of the File Open, sends the mapping
             definition, defined by the mapping title, and the Dataset as input.  The operation
             traverses from the input Dataset to the mapped property which in this case resides
             on the Datasets parent Item Revision.  The operation will return the item revision
             and the mapped property name such that the client integration can retrieve the property
             value from the item revision.  The value is then displayed in the attribute data
             for the dataset in the client integration.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Info: 
                         An array of ResolveAttrMappingsInfo structures each containing a <b>Dataset</b> object
                         reference, an optional item revision, and a list of corresponding CAD Attribute Mapping
                         Definitions to be resolved for the dataset.
             
        :return: 
        """
        ...
    def GetAllAttrMappings2(self) -> Teamcenter.Services.Strong.Cad._2011_06.DataManagement.GetAllAttrMappingsResponse:
        """    
             This operation retrieves all CAD attribute mapping definitions. If a CadAttributeMappingDefinition object has a path that includes
             a Generic Relationship Manager (GRM) or named reference part, the associated property
             descriptor and any attached ListOfValues
             (LOV) objects will be returned. This operation also returns LOV attachments category
             information to be used in object based conditions.
             

             Since this operation returns existing Teamcenter attribute mappings, please reference
             the Teamcenter help section on creating attribute mappings.
             


Use Cases:

             User needs to have attributes set on an object in Teamcenter.
             

             For this operation, the client application uses the list of returned attribute mapping
             definitions to present the correct CAD attributes to the user that correspond to
             the correct Teamcenter attributes including property descriptor information about
             the Teamcenter attributes.
             


Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :return: 
        """
        ...
    def GetAttrMappings(self, Filter: list[Teamcenter.Services.Strong.Cad._2014_10.DataManagement.GetAttrMappingsFilter]) -> Teamcenter.Services.Strong.Cad._2014_10.DataManagement.GetAttrMappingsResponse:
        """    
             This operation retrieves all CAD attribute mapping definitions or only the definitions
             that match the dataset and item type combinations included in the input filter.
             CadAttributeMappingDefinition objects are returned with the associated business
             object name and property descriptor name.  The business object name and property
             descriptor name can be used to get the PropertyDescription
             object from the client-side Meta Model, ClientMetaModel.
             The PropertyDescription object can then
             be used to access any needed property descriptor information, such as attached ListOfValues (LOV) objects.
             

             Since this operation returns existing Teamcenter attribute mappings, please reference
             the Teamcenter help section on creating attribute mappings.
             


Use Cases:

             User needs to have attributes set on an object in Teamcenter.
             

             For this operation, the client application uses the list of returned attribute mapping
             definitions to present the correct CAD attributes to the user that correspond to
             the correct Teamcenter attributes including property descriptor information about
             the Teamcenter attributes.
             


Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Filter: 
                         The input filter for narrowing the attribute mapping definitions returned in the
                         response. All of the attribute mappings defined in Teamcenter are returned when no
                         filter is specified.
             
        :return: 
        """
        ...
    def CreateOrUpdateModelViewPalette(self, MvPaletteInfo: list[Teamcenter.Services.Strong.Cad._2016_03.DataManagement.ModelViewPaletteInfo]) -> Teamcenter.Services.Strong.Cad._2016_03.DataManagement.CreateOrUpdateMVPaletteResponse:
        """    
             Creates, updates or deletes a model view palette (Fnd0ModelViewPalette) object
             and its groups. The model view palette supports Visualization tools in creating and
             managing model view groups (Fnd0ModelViewGroup) during creation of a Disclosure
             object (an Item or Workset that discloses installation assembly designs). The disclosed
             model view proxy objects may be grouped by this operation.
             
             Using this API, applications can create and update a list of objects in bulk. Providing
             better context and fewer calls from the CAD clients than otherwise would be achieved
             using standard object create and update service operations.
             

Use Cases:

             This API supports the following use cases
             

Use Case 1: Creation of Model View Palette and Model View Groups for a Design
             Disclosure


             The operation can be used for supporting creation of a disclosure object. The disclosure
             object will most commonly be a Workset (Cpd0Workset subtype) but may also
             be a specific type of ItemRevision. The actual disclosure object may be pre-existing
             but would not be acting as a disclosure until this operation creates and attaches
             the desired list of disclosed Model View Proxy references.
             

             The purpose of a design disclosure is to act as a 3D equivalent of a 2D drawing of
             individual installation assemblies (IA.) This disclosure object will collect all
             geometry needed to show both the IA and its assembly PMI. After the various PMI and
             Model Views within the disclosure have been created, they must be "disclosed".
             

             To be considered as disclosed by a disclosure object, a Model View Proxy must be
             referenced by a Model View Group (Fnd0ModelViewGroup)that is referenced by
             a Model View Palette (Fnd0ModelViewPalette) that is associated to the disclosure
             object.
             

             The paletteIsComplete input must be set to
             true for creation of a Model View Palette, as it makes no sense to be false.
             

Use Case 2: Update of Model View Palette and Model View Groups for a Design Disclosure

             If groupsToDelete is set then see Use case
             3 for details, else if paletteIsComplete
             is set to true, then the system will:
             
             1) Process groupsAndProxies, creating or
             updating various Groups.
             
             2) Check the existing Group list on the Palette to determine if any existing Groups
             in the current Palette list are not in the input groupsAndProxies
             input. If so, then set aside such existing Groups for deletion.
             
             3) Set the list of existing and newly created Groups (from step 1 above) onto the
             Palette.
             
             4) Now delete the now unreferenced Groups (from step 2) if any.
             

             If paletteIsComplete is set to false, the system will:
             
             1) process groupsAndProxies, creating or updating various Groups.
             
             2) Again, if groupsToDelete is set then see Use case 3 for details. This must be
             done before re-ordering the Palette's sequence of Groups in order for the input sequence
             order values to be understood correctly by the system.
             
             3) Set the list of existing and newly created Groups (from step 1 above) onto the
             Palette list of Groups (using any specified newOrderSequenceNumber if one was given.
             If any newOrderSequenceNumber is within the range of existing Groups, and that existing
             Group is not in the groupsAndProxies being given a new sequence number, then the
             existing group being replaced in that sequence number will be set aside to be placed
             at the end of the sequence.
             
             4) Now place any set-aside (due to be pushed out of place or being given a sequence
             value of 0) Groups at the end of the Palette's list of Groups.
             


             Use Case 3: Delete of existing Model View Palette and/or specific Groups within the
             Palette
             

             To delete an entire Palette and all its Groups, the caller will simply send both
             the disclosure and the deletePalette flag.
             
             The system will :
             

Verify write permission on the disclosure object in order to proceed.
             
Remove the relation between the disclosure object and the Model View
             Palette.
             
Delete the Model View Palette
             
Delete all the Model View Groups that were previously referenced
             by the Model View Palette
             



             To delete only specified Groups out of all those currently existing on a Palette,
             the caller will send the Groups to delete in the groupsToDelete list.
             
             The system will:
             

Note: write permission on the Model View Palette is required.
             
Remove all the specified Model View Groups from the reference list
             on the Model View Palette, preserving the order among the remaining Model View Groups
             referenced by the Palette.
             
Delete the now unreferenced Model View Groups.
             



Teamcenter Component:

             Disclosure - Component that is used to represent the 3D equivalent of the 2D drawing.
             
        :param MvPaletteInfo: 
                         The model view palette information describing the details of the palette (<b>Fnd0ModelViewPalette</b>)
                         and model view groups (<b>Fnd0ModelViewGroup</b>) to be created or updated or deleted.
             
        :return: 
        """
        ...
    def CreateOrUpdateModelViewProxies(self, MvProxyInfos: list[Teamcenter.Services.Strong.Cad._2016_03.DataManagement.ModelViewProxyInfo], UpdatedOwningModels: list[Teamcenter.Services.Strong.Cad._2016_03.DataManagement.OwningModelAndCadLmd]) -> Teamcenter.Services.Strong.Cad._2016_03.DataManagement.CreateOrUpdateModelViewProxiesResponse:
        """    
             Creates, updates or deletes a set of model view proxy (Fnd0ModelViewProxy)
             objects. Supports CAD tools in creating and managing model view proxy objects during
             Part save. The model view proxy objects are each a proxy for a master model view
             in the Part's CAD file.
             
             Using this API, applications can create and update proxy objects in bulk, with better
             context and less calls from CAD clients than may otherwise be achieved using standard
             object create and update SOAs.
             

Use Cases:

             This API supports the following use cases:
             
             Use Case 1: Creation of new model view proxy

             The following operation can be used for creating model view proxies for specified
             owning objects (usually ItemRevisions.)
             

Model view proxies have a model view CAD Id (fnd0ModelViewIdCAD)
             which Id is unique within the set of model view proxies associated to the same owning
             object.
             
During the model view proxies initial creation (but not during a
             subsequent save-as or revise), a clone stable ID is generated which can help in identifying
             equivalent proxy objects for cases where the fnd0ModelViewIdCAD wasn't tracked
             but rather the proxy object itself.
             
An optional thumbnail file may be identified that a CAD tool has
             generated for the actual CAD model view.
             
During the operation, the server creates and saves the new model
             view proxies in context of an already existing owning object. The operation returns
             the new objects to the caller.
             



             Use Case 2: Update of existing model view proxy

             The following operation can be used for updating existing model view proxies.
             

Model View Proxies are found by applications via the fnd0OwnedModelViews
             property of workspaceObject objects.
             
The existing model view proxies can be updated using operation createOrUpdateModelViewProxies.
             The application specifies which model view proxies are to be updated.  Note: the
             business object type (boType) and owning
             object (owningModel) do not need to be set
             on the input because they are already known to the model view proxy and cannot be
             changed.  The application sets changed property values.
             



             Use Case 3: Delete of existing model view proxy

             The operation can be used for deleting existing model view proxies due to either
             the CAD designer removing the actual model view or due to a decision that there is
             no need for that model view to have a proxy any longer.
             

Model View Proxies are found by applications via the fnd0OwnedModelViews
             property of certain types of WorkspaceObject objects (currently this property
             is only available at  ItemRevision ).
             
The existing model view proxies can be deleted using operation createOrUpdateModelViewProxies.
             The application specifies which model view proxies are to be modified (modelView) and that they are to be deleted (deleteProxy set to true.)  The server will attempt to delete the
             model view proxy and if successful, the deleted object list will be updated on the
             ServiceData of the response.
             



Teamcenter Component:

             Disclosure - Component that is used to represent the 3D equivalent of the 2D drawing.
             
        :param MvProxyInfos: 
                         The input list of model view proxy information describing the details of the proxies
                         to be created or updated.
             
        :param UpdatedOwningModels: 
                         The input list of model view owners which have had their CAD model views updated.
                         After <font face="courier" height="10">mvProxyInfos</font> has been processed, all
                         proxies associated to these specified owning models will have their CAD last modified
                         date updated to be in sync with a provided date time. This is optional, if no <b>OwningModelAndCADLMD</b>
                         is provided, then no automatic setting of CAD last modified date will be done.
             
        :return: object.
        """
        ...

class StructureManagementRestBindingStub(StructureManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateBOMWindows(self, Info: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateBOMWindowsInfo]) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateBOMWindowsResponse: ...
    @typing.overload
    def CreateOrUpdateAbsoluteStructure(self, Info: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateAbsoluteStructureInfo], BomViewTypeName: str, Complete: bool, Pref: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateAbsoluteStructurePref) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateAbsoluteStructureResponse: ...
    @typing.overload
    def CreateOrUpdateAbsoluteStructure(self, Info: list[Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.CreateOrUpdateAbsoluteStructureInfo2], BomViewTypeName: str, Complete: bool, Pref: Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.CreateOrUpdateAbsoluteStructurePref2) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateAbsoluteStructureResponse: ...
    @typing.overload
    def CreateOrUpdateAbsoluteStructure(self, AbsOccInfos: list[Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.CreateOrUpdateAbsoluteStructureInfo3], BomViewTypeName: str, Complete: bool, Pref: Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.CreateOrUpdateAbsoluteStructurePref3) -> Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.CreateOrUpdateAbsoluteStructureResponse2: ...
    @typing.overload
    def CreateOrUpdateRelativeStructure(self, Inputs: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateRelativeStructureInfo], BomViewTypeName: str, Complete: bool, Pref: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateRelativeStructurePref) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateRelativeStructureResponse: ...
    @typing.overload
    def CreateOrUpdateRelativeStructure(self, Inputs: list[Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.CreateOrUpdateRelativeStructureInfo2], BomViewTypeName: str, Complete: bool, Pref: Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.CreateOrUpdateRelativeStructurePref2) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateRelativeStructureResponse: ...
    @typing.overload
    def CreateOrUpdateRelativeStructure(self, Inputs: list[Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.CreateOrUpdateRelativeStructureInfo3], BomViewTypeName: str, Complete: bool, Pref: Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.CreateOrUpdateRelativeStructurePref3) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateRelativeStructureResponse: ...
    @typing.overload
    def CreateOrUpdateRelativeStructure(self, Inputs: list[Teamcenter.Services.Strong.Cad._2009_04.StructureManagement.CreateOrUpdateRelativeStructureInfo], Pref: Teamcenter.Services.Strong.Cad._2009_04.StructureManagement.CreateOrUpdateRelativeStructurePref) -> Teamcenter.Services.Strong.Cad._2009_04.StructureManagement.CreateOrUpdateRelativeStructureResponse: ...
    @typing.overload
    def CreateOrUpdateRelativeStructure(self, Inputs: list[Teamcenter.Services.Strong.Cad._2013_05.StructureManagement.CreateOrUpdateRelativeStructureInfo4], Pref: Teamcenter.Services.Strong.Cad._2009_04.StructureManagement.CreateOrUpdateRelativeStructurePref) -> Teamcenter.Services.Strong.Cad._2009_04.StructureManagement.CreateOrUpdateRelativeStructureResponse: ...
    @typing.overload
    def DeleteAssemblyArrangements(self, Info: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteAssemblyArrangementsInfo], BomViewTypeName: str) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteAssemblyArrangementsResponse: ...
    @typing.overload
    def DeleteAssemblyArrangements(self, Info: list[Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.DeleteAssemblyArrangementsInfo2], BomViewTypeName: str, Pref: Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.DeleteAssemblyArrangementsPref) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteAssemblyArrangementsResponse: ...
    @typing.overload
    def DeleteRelativeStructure(self, Inputs: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteRelativeStructureInfo], BomViewTypeName: str, Pref: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteRelativeStructurePref) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteRelativeStructureResponse: ...
    @typing.overload
    def DeleteRelativeStructure(self, Inputs: list[Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.DeleteRelativeStructureInfo2], BomViewTypeName: str, Pref: Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.DeleteRelativeStructurePref2) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteRelativeStructureResponse: ...
    @typing.overload
    def DeleteRelativeStructure(self, Inputs: list[Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.DeleteRelativeStructureInfo3], BomViewTypeName: str, Pref: Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.DeleteRelativeStructurePref2) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteRelativeStructureResponse: ...
    @typing.overload
    def ExpandPSAllLevels(self, Input: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.ExpandPSAllLevelsInfo, Pref: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.ExpandPSAllLevelsPref) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.ExpandPSAllLevelsResponse: ...
    @typing.overload
    def ExpandPSAllLevels(self, Info: Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSAllLevelsInfo, Pref: Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSAllLevelsPref) -> Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSAllLevelsResponse2: ...
    @typing.overload
    def ExpandPSOneLevel(self, Input: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.ExpandPSOneLevelInfo, Pref: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.ExpandPSOneLevelPref) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.ExpandPSOneLevelResponse: ...
    @typing.overload
    def ExpandPSOneLevel(self, Info: Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSOneLevelInfo, Pref: Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSOneLevelPref) -> Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSOneLevelResponse2: ...
    def GetRevisionRules(self) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.GetRevisionRulesResponse: ...
    def CloseBOMWindows(self, BomWindows: list[Teamcenter.Soa.Client.Model.Strong.BOMWindow]) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CloseBOMWindowsResponse: ...
    def GetVariantRules(self, ItemRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.GetVariantRulesResponse: ...
    def GetConfiguredItemRevision(self, Inputs: list[Teamcenter.Services.Strong.Cad._2007_06.StructureManagement.GetConfiguredItemRevisionInfo]) -> Teamcenter.Services.Strong.Cad._2007_06.StructureManagement.GetConfiguredItemRevisionResponse: ...
    def CreateOrUpdateClassicOptions(self, InputObjects: list[Teamcenter.Services.Strong.Cad._2007_06.StructureManagement.CreateUpdateClassicOptionsInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateOrUpdateVariantConditions(self, InputObjects: list[Teamcenter.Services.Strong.Cad._2007_06.StructureManagement.CreateOrUpdateVariantCondInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteClassicOptions(self, InputObjects: list[Teamcenter.Services.Strong.Cad._2007_06.StructureManagement.DelClassicOptionsInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteVariantConditions(self, InputObjects: list[Teamcenter.Services.Strong.Cad._2007_06.StructureManagement.DeleteVariantCondInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateOrUpdateVariantConditions2(self, InputObjects: list[Teamcenter.Services.Strong.Cad._2007_09.StructureManagement.CreateOrUpdateVariantCondInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def QueryClassicOptions(self, InputRevisions: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.ClassicOptionsResponse: ...
    def QueryVariantConditions(self, InputBomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.VariantConditionResponse: ...
    def AskChildPathBOMLines(self, Input: list[Teamcenter.Services.Strong.Cad._2008_03.StructureManagement.AskChildPathBOMLinesInfo]) -> Teamcenter.Services.Strong.Cad._2008_03.StructureManagement.AskChildPathBOMLinesResponse: ...
    def GetAbsoluteStructureData(self, AbsOccDataQualInfos: list[Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.AbsOccQualifierInfo], AbsOccDataPref: Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.AbsOccDataPref) -> Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.GetAbsoluteStructureDataResponse: ...
    def CreateVariantRules(self, Input: list[Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.CreateVariantRulesInfo]) -> Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.CreateVariantRulesResponse: ...
    def ReconfigureBOMWindows(self, Info: list[Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ReconfigureBOMWindowsInfo]) -> Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ReconfigureBOMWindowsResponse: ...
    def SaveBOMWindows(self, BomWindows: list[Teamcenter.Soa.Client.Model.Strong.BOMWindow]) -> Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.SaveBOMWindowsResponse: ...
    def AskChildPathBOMLines2(self, Input: list[Teamcenter.Services.Strong.Cad._2008_03.StructureManagement.AskChildPathBOMLinesInfo]) -> Teamcenter.Services.Strong.Cad._2013_05.StructureManagement.AskChildPathBOMLinesResponse2: ...
    def CreateBOMWindows2(self, Info: list[Teamcenter.Services.Strong.Cad._2013_05.StructureManagement.CreateWindowsInfo2]) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateBOMWindowsResponse: ...
    def FindModelViewsInStructure(self, Disclosure: Teamcenter.Soa.Client.Model.ModelObject, StructureScope: list[Teamcenter.Soa.Client.Model.ModelObject], ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, WithDisclosureIntent: list[str], Options: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Cad._2016_03.StructureManagement.FindModelViewsInStructureResponse: ...
    def ContinueFindModelViews(self, SearchID: str, StopFind: bool) -> Teamcenter.Services.Strong.Cad._2016_09.StructureManagement.FindModelViewsResponse: ...
    def ContinueReconcilePalette(self, ReconcilePaletteInput: Teamcenter.Services.Strong.Cad._2016_09.StructureManagement.NextReconcilePaletteInput) -> Teamcenter.Services.Strong.Cad._2016_09.StructureManagement.ReconcilePaletteResponse: ...
    def StartFindModelViews(self, FindInput: Teamcenter.Services.Strong.Cad._2016_09.StructureManagement.FindModelViewsInput) -> Teamcenter.Services.Strong.Cad._2016_09.StructureManagement.FindModelViewsResponse: ...
    def StartReconcilePalette(self, ReconcilePaletteInput: Teamcenter.Services.Strong.Cad._2016_09.StructureManagement.ReconcilePaletteInput) -> Teamcenter.Services.Strong.Cad._2016_09.StructureManagement.ReconcilePaletteResponse: ...
    def WriteAssemblyConfigurationDetails(self, BomWindow: Teamcenter.Soa.Client.Model.ModelObject, OptionSetName: str) -> Teamcenter.Services.Strong.Cad._2018_06.StructureManagement.AssemblyConfigurationResponse: ...
    def CreateOrReConfigureBOMWindows(self, Info: list[Teamcenter.Services.Strong.Cad._2019_06.StructureManagement.CreateWindowsInfo3]) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateBOMWindowsResponse: ...
    def ExpandPSOneLevel2(self, Info: Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSOneLevelInfo, Prefs: Teamcenter.Services.Strong.Cad._2023_06.StructureManagement.ExpandPSOneLevelPref) -> Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSOneLevelResponse2: ...

class StructureManagementService:
    """
    
            Contains StructureManagement Services
            


Library Reference:

TcSoaCadStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> StructureManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateBOMWindows(self, Info: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateBOMWindowsInfo]) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateBOMWindowsResponse:
        """    
             Creates a BOMWindow and sets the input Item Revision as the top line.  Can be used
             to create the BOMLine for input to Expand Product Structure services.  All BOMLines
             under this window are unpacked.  To use the Teamcenter default unitNo or use your
             input RevisionRule with no changes, you must set unitNo to -1 in RevisionRuleEntryProps::unitNo.
             If it is not specified, your input rule will function as a modified/transient revision
             rule with a unitNo of 0.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Info: 
                         Input is an item or item Revision object
             
        :return: Output is the created BOMWindow object and top line BOMLine object representing the
             item or item revision
        """
        ...
    @typing.overload
    def CreateOrUpdateAbsoluteStructure(self, Info: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateAbsoluteStructureInfo], BomViewTypeName: str, Complete: bool, Pref: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateAbsoluteStructurePref) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateAbsoluteStructureResponse: ...
    @typing.overload
    def CreateOrUpdateAbsoluteStructure(self, Info: list[Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.CreateOrUpdateAbsoluteStructureInfo2], BomViewTypeName: str, Complete: bool, Pref: Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.CreateOrUpdateAbsoluteStructurePref2) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateAbsoluteStructureResponse: ...
    @typing.overload
    def CreateOrUpdateAbsoluteStructure(self, AbsOccInfos: list[Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.CreateOrUpdateAbsoluteStructureInfo3], BomViewTypeName: str, Complete: bool, Pref: Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.CreateOrUpdateAbsoluteStructurePref3) -> Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.CreateOrUpdateAbsoluteStructureResponse2: ...
    @typing.overload
    def CreateOrUpdateRelativeStructure(self, Inputs: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateRelativeStructureInfo], BomViewTypeName: str, Complete: bool, Pref: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateRelativeStructurePref) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateRelativeStructureResponse: ...
    @typing.overload
    def CreateOrUpdateRelativeStructure(self, Inputs: list[Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.CreateOrUpdateRelativeStructureInfo2], BomViewTypeName: str, Complete: bool, Pref: Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.CreateOrUpdateRelativeStructurePref2) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateRelativeStructureResponse: ...
    @typing.overload
    def CreateOrUpdateRelativeStructure(self, Inputs: list[Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.CreateOrUpdateRelativeStructureInfo3], BomViewTypeName: str, Complete: bool, Pref: Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.CreateOrUpdateRelativeStructurePref3) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateRelativeStructureResponse: ...
    @typing.overload
    def CreateOrUpdateRelativeStructure(self, Inputs: list[Teamcenter.Services.Strong.Cad._2009_04.StructureManagement.CreateOrUpdateRelativeStructureInfo], Pref: Teamcenter.Services.Strong.Cad._2009_04.StructureManagement.CreateOrUpdateRelativeStructurePref) -> Teamcenter.Services.Strong.Cad._2009_04.StructureManagement.CreateOrUpdateRelativeStructureResponse: ...
    @typing.overload
    def CreateOrUpdateRelativeStructure(self, Inputs: list[Teamcenter.Services.Strong.Cad._2013_05.StructureManagement.CreateOrUpdateRelativeStructureInfo4], Pref: Teamcenter.Services.Strong.Cad._2009_04.StructureManagement.CreateOrUpdateRelativeStructurePref) -> Teamcenter.Services.Strong.Cad._2009_04.StructureManagement.CreateOrUpdateRelativeStructureResponse: ...
    @typing.overload
    def DeleteAssemblyArrangements(self, Info: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteAssemblyArrangementsInfo], BomViewTypeName: str) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteAssemblyArrangementsResponse: ...
    @typing.overload
    def DeleteAssemblyArrangements(self, Info: list[Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.DeleteAssemblyArrangementsInfo2], BomViewTypeName: str, Pref: Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.DeleteAssemblyArrangementsPref) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteAssemblyArrangementsResponse: ...
    @typing.overload
    def DeleteRelativeStructure(self, Inputs: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteRelativeStructureInfo], BomViewTypeName: str, Pref: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteRelativeStructurePref) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteRelativeStructureResponse: ...
    @typing.overload
    def DeleteRelativeStructure(self, Inputs: list[Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.DeleteRelativeStructureInfo2], BomViewTypeName: str, Pref: Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.DeleteRelativeStructurePref2) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteRelativeStructureResponse: ...
    @typing.overload
    def DeleteRelativeStructure(self, Inputs: list[Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.DeleteRelativeStructureInfo3], BomViewTypeName: str, Pref: Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.DeleteRelativeStructurePref2) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteRelativeStructureResponse: ...
    @typing.overload
    def ExpandPSAllLevels(self, Input: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.ExpandPSAllLevelsInfo, Pref: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.ExpandPSAllLevelsPref) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.ExpandPSAllLevelsResponse: ...
    @typing.overload
    def ExpandPSAllLevels(self, Info: Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSAllLevelsInfo, Pref: Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSAllLevelsPref) -> Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSAllLevelsResponse2: ...
    @typing.overload
    def ExpandPSOneLevel(self, Input: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.ExpandPSOneLevelInfo, Pref: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.ExpandPSOneLevelPref) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.ExpandPSOneLevelResponse: ...
    @typing.overload
    def ExpandPSOneLevel(self, Info: Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSOneLevelInfo, Pref: Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSOneLevelPref) -> Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSOneLevelResponse2: ...
    def GetRevisionRules(self) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.GetRevisionRulesResponse:
        """    
             The GetRevisionRules service gets all the persistent revision rules in the database.
             It along with the revision rules returns its runtime configuration properties status
             of being fixed or not.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :return: 
        """
        ...
    def CloseBOMWindows(self, BomWindows: list[Teamcenter.Soa.Client.Model.Strong.BOMWindow]) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CloseBOMWindowsResponse:
        """    
             Closes a BOMWindow.  Must be used to close the BOMWindow created during Create BOM
             Window after calls to Expand Product Structure services are complete.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param BomWindows: 
                         The BOMWindow to close
             
        :return: the uids of the BOMWindow.
        """
        ...
    def GetVariantRules(self, ItemRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.GetVariantRulesResponse:
        """    
             The GetVariantRules service gets all the variant rules in the database for the given
             Item Revision. To get Product Configurator authored variant rules, value of preference
             PSM_default_configurator_context must be true.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param ItemRevs: 
                         List of object references of ItemRevisions to get variant rules for
             
        :return: GetVariantRulesResponse which contains a map of input Item Revision to list of to
             list of Variant Rule objects for that Item Revision
        """
        ...
    def GetConfiguredItemRevision(self, Inputs: list[Teamcenter.Services.Strong.Cad._2007_06.StructureManagement.GetConfiguredItemRevisionInfo]) -> Teamcenter.Services.Strong.Cad._2007_06.StructureManagement.GetConfiguredItemRevisionResponse:
        """    
             Finds the revision of the given item / item revision that is configured when the
             given revision rule is used to configure the given item / item revision.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Inputs: 
                         A list of GetConfiguredItemRevisionInfo structures, each of which contain a item
                         or item revision object and revision rule.
             
        :return: contains a ServiceData and a list of GetConfiguredItemRevisionOutput, each of which
             contain the configured item revision and list of GetConfiguredItemRevisionInfo structures,
             each of which contain the input object and revision rule. Any failure will be returned
             via ServiceData with original input object mapped to error message.
        """
        ...
    def CreateOrUpdateClassicOptions(self, InputObjects: list[Teamcenter.Services.Strong.Cad._2007_06.StructureManagement.CreateUpdateClassicOptionsInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             In the Create mode this operation creates a new option(s), with given option values,
             and declares them against the given ItemRevision object. In the update mode
             following operations can be performed with the given option
             

1.    Replace the current text value for the
             specified index with a new string from option revision.
             
2.    Add a new value to the option revision.
             
3.    Remove an existing value from the option
             revision.
             



Use Cases:

             This operation will be used when user wants to create classic variant options for
             a given BOMLine object(s). This also can be used to update an Option
             

a) adding a new value
             
b) removing an existing value
             
c) replace an existing value by new value.
             



Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param InputObjects: 
                         Refers to the list of CreateUpdateClassicOptionsInput struct, which are used to create
                         a new variant option or update an existing variant option.
             
        :return: 
        """
        ...
    def CreateOrUpdateVariantConditions(self, InputObjects: list[Teamcenter.Services.Strong.Cad._2007_06.StructureManagement.CreateOrUpdateVariantCondInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is to create or update (depending on the Operation) a variantCondition ( which
             is variant expression of type load if) for a BOMLine object.
             

Use Cases:

             This operation will be used when user wants to create a new or update an existing
             classic variant condition for a given BOMLine objects.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param InputObjects: 
                         This has the list of <font face="courier" height="10">CreateOrUpdateVariantCondInput</font>
                         struct, which are used to create a new variant condition or update an existing variant
                         condition.
             
        :return: 
        """
        ...
    def DeleteClassicOptions(self, InputObjects: list[Teamcenter.Services.Strong.Cad._2007_06.StructureManagement.DelClassicOptionsInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Delete option deletes the option and all the values associated with it.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param InputObjects: 
                         A list of DelClassicOptionsInput structures, each of which contains a bomline tag,
                         and list of options. If the option exists then it will be deleted.
             
        :return: ServiceData:Any failure will be returned via ServiceData with original input object
             mapped to error message.
        """
        ...
    def DeleteVariantConditions(self, InputObjects: list[Teamcenter.Services.Strong.Cad._2007_06.StructureManagement.DeleteVariantCondInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service will be used to delete the variant Condition(load_if) associated with
             a BOMLine If the variant condition exists then it will be deleted. Failure will be
             with client id and error message in the ServiceData.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param InputObjects: 
                         Consists of the clientId and the BOMLine for which we need to delete the variant
                         Condition
             
        :return: ServiceData
        """
        ...
    def CreateOrUpdateVariantConditions2(self, InputObjects: list[Teamcenter.Services.Strong.Cad._2007_09.StructureManagement.CreateOrUpdateVariantCondInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is to create or update (depending on the Operation) a variantCondition ( which
             is variant expression of type load if) for a BOMLine object.
             

Use Cases:

             This operation will be used when user wants to create a new or update an existing
             classic variant condition for a given BOMLine objects.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param InputObjects: 
                         This has the list of <font face="courier" height="10">CreateOrUpdateVariantCondInput</font>
                         struct, which are used to create a new variant condition or update an existing variant
                         condition.
             
        :return: 
        """
        ...
    def QueryClassicOptions(self, InputRevisions: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.ClassicOptionsResponse:
        """    
             This operation is to find classic variant options defined on an ItemRevision
             object(s).
             

Use Cases:

             The user can use this operation to find all the classic variant options defined on
             given ItemRevision object. The option and values can be used for configuration
             or creating other related objects like variant conditions, constraint (defaults,
             derived defaults and rule checks) rules or VariantRule objects.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param InputRevisions: 
                         This is list of <b>ItemRevision</b> object on which variant options are to be queried.
             
        :return: with original input object(s)
             if any.
        """
        ...
    def QueryVariantConditions(self, InputBomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Services.Strong.Cad._2007_12.StructureManagement.VariantConditionResponse:
        """    
             This operation is to find a variant condition value ( load if - this is a type of
             variant expression represents variant condition) for a BOMLine object.
             

Use Cases:

             The user needs variant condition defined on the BOMLine object, for display
             or editing purpose.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param InputBomLines: 
                         This has the list of <b>BOMLine</b> objects, on which variant condition are defined.
             
        :return: 
        """
        ...
    def AskChildPathBOMLines(self, Input: list[Teamcenter.Services.Strong.Cad._2008_03.StructureManagement.AskChildPathBOMLinesInfo]) -> Teamcenter.Services.Strong.Cad._2008_03.StructureManagement.AskChildPathBOMLinesResponse:
        """    
             Given one or more sets of product structure information containing child paths specified
             by PS Occurrence Thread chains, this method returns the corresponding BOM Lines.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Input: 
                         Specifies sets of product structure information each containing parent BOM line,
                         based on a BOM Window opened by the client, and one or more child paths specified
                         as an ordered set of PS Occurrence Thread UIDs. BOM configuration is managed by the
                         BOM Window. Input client IDs must be unique for all input.
             
        :return: map of input PS Occurrence Thread UIDs, specified as child paths in the input, to
             the corresponding BOMLines. BOMLine objects are returned as Service Data plain objects
             to inflate properties. Partial failures can result for each child path or product
             structure being evaluated and can be associated with the input by the input client
             ID.
        """
        ...
    def GetAbsoluteStructureData(self, AbsOccDataQualInfos: list[Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.AbsOccQualifierInfo], AbsOccDataPref: Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.AbsOccDataPref) -> Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.GetAbsoluteStructureDataResponse:
        """    
             This operation retrieves the absolute occurrence override information for the given
             qualifier. The input accepts the relation override that needs to be expanded. In
             case of finding the overrides based on the used arrangement within the structure,
             the client is expected to provide bvr of sub assembly in the input. ParentBVR |--(Arr1)
             |--(Arr2) | |________childBVR1 |           |-----(Arr3) |           |-----(Arr4)
             |           |_____________childBVR2 |                                    |----(Arr5)
             |                                    |----(Arr6) |_____ childBVR2 |----(Arr5) |----(Arr6)
             If Arr1 uses Arr3 which in turn uses Arr5, to determine the overrides by Arr3 and
             Arr5 qualifier the client is expected to send childbvr1 and childbvr2 as inputs along
             with the parentBVR.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param AbsOccDataQualInfos: 
                         List of qualifying information for overrides
             
        :param AbsOccDataPref: 
                         Preference on which relation overrides to expand and the preferred objects of type
                         to return
             
        :return: Contains the  overrides and service data information.
        """
        ...
    def CreateVariantRules(self, Input: list[Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.CreateVariantRulesInfo]) -> Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.CreateVariantRulesResponse:
        """    
             This operation creates the saved VariantRule objects for classic variant options.
             

Use Cases:

             This operation is used to create VariantRule object and save them, which can
             be used later for BOM variant configuration.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param Input: 
                         This has the list of <font face="courier" height="10">CreateVariantRulesInfo</font>
                         struct, which are used to create a new <b>VariantRule</b> object.
             
        :return: 
        """
        ...
    def ReconfigureBOMWindows(self, Info: list[Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ReconfigureBOMWindowsInfo]) -> Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ReconfigureBOMWindowsResponse:
        """    
             This operation takes a list of BOMWindow objects and updates the contents
             of the windows (i.e. configuration) by applying the supplied RevisionRule
             and variant configuration information.  If the RevisionRuleEntryProps::unitNo is set to -1 then it considers default unitNo
             or use the input RevisionRule object with no changes. If no value specified
             for RevisionRuleEntryProps::unitNo, then the input RevisionRule object used as modified/transient
             rule with unitNo as 0. If the value of preference PSM_enable_product_configurator
             is set to true, then Product Configurator variant rule will be honored.
             

Use Cases:

             This operation is used to reconfigure the BOMWindow with new or modified RevisionRule
             and VariantRule information.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param Info: 
                         This contains a list of <font face="courier" height="10">ReconfigureBOMWindowsInfo</font>
                         struct objects which has <b>BOMWindow</b> objects and corresponding <b>RevisionRule</b>
                         object and <b>VariantRule</b> object or <b>StoredOptionSet</b> object information.
             
        :return: 
        """
        ...
    def SaveBOMWindows(self, BomWindows: list[Teamcenter.Soa.Client.Model.Strong.BOMWindow]) -> Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.SaveBOMWindowsResponse:
        """    
             This operation can be used by a client developer to save any modifications made to
             a Teamcenter product structure through its runtime artifacts. A Teamcenter product
             structure is a persistent parent child composition and clients often deal with runtime
             artifacts of this persistent model. The runtime artifacts are primarily represented
             by BOMLine business objects and BOMWindow business objects along with
             the BOMLine properties. Modifications to the product structure are typically
             bulked up on the client and tracked through the BOMWindow. Once it is established
             that changes to a product structure can be saved this operation can be called passing
             in a handle to the BOMWindows that need to be saved.
             

Use Cases:

             In a typical usage of the saveBOMWindows operation, a client developer already has
             a Teamcenter product structure loaded with the runtime artifacts created. This means
             that the client developer has/creates handles to a BOMWindow, and BOMLine
             business objects that are part of that BOMWindow. Given this pre disposition,
             typical interaction with the client may involve addition of a new BOMLine
             or removal of a BOMLine, creation/removal of In Structure associations etc.
             In such cases, the changes to the product structure are tracked on the BOMWindow
             and when the changes are ready to be persisted, the client developer calls the saveBOMWindows
             operation.
             


Dependencies:

             createOrUpdateRelativeStructure
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param BomWindows: 
                         References to the <b>BOMWindow</b> business objects that need to be saved after structure
                         modifications.
             
        :return: 
        """
        ...
    def AskChildPathBOMLines2(self, Input: list[Teamcenter.Services.Strong.Cad._2008_03.StructureManagement.AskChildPathBOMLinesInfo]) -> Teamcenter.Services.Strong.Cad._2013_05.StructureManagement.AskChildPathBOMLinesResponse2:
        """    
             This operation returns the BOMLine objects corresponding to input sets of
             child paths.
             

             The child path is defined by an ordered set of PSOccurrenceThread UIDs, starting
             from the top level assembly to a child node. The child node can be an immediate child
             or can be multi-level deep.
             

             This operation will return the BOMLine for each input child path. If a particular
             child path no longer exists in the Teamcenter product structure, there will be no
             entry for that input child path in the output AskChildPathClientIdToBOMLineMap.
             

             This operation works on existing BOM windows. The BOM window must have been created
             prior to using this operation.
             

Use Cases:

             If the client has a previously saved list of PSOccurrenceThread paths of a
             product structure, a new BOM window for the top level Item can be created and all
             the BOM line objects corresponding to the leaf node of the PSOccurrenceThread
             paths can be queried through this operation.
             

Dependencies:

             createBOMWindows
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Input: 
                         Specifies sets of product structure information each containing parent <b>BOMLine</b>
                         object, based on a BOM window opened by the client and one or more child paths specified
                         as an ordered set of <b>PSOccurrenceThread</b> UIDs. BOM configuration is managed
                         by the BOM window. Input client IDs must be unique for all input. The output <b>BOMLine</b>
                         objects are mapped to the input client IDs and the input child path UID.
             
        :return: 
        """
        ...
    def CreateBOMWindows2(self, Info: list[Teamcenter.Services.Strong.Cad._2013_05.StructureManagement.CreateWindowsInfo2]) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateBOMWindowsResponse:
        """    
             Creates a list of window and sets the respective input ItemRevision as the
             top line. This operation can be used to set multiple saved variant rules or single
             stored option set to the window. For setting Product Configurator authored varaint
             rule on the window, value of preference PSM_enable_product_configurator must be true.It
             can be used to set certain window property, if sent as a part of input. It can be
             used to create the BOMLine for input to Expand Product Structure services.
             All BOMLines under this window are unpacked.  To use the Teamcenter default
             unitNo or use your input RevisionRule with no changes, you must set unitNo to -1
             in RevisionRuleEntryProps::unitNo.  If it is not specified, your input rule will
             function as a modified/transient revision rule with a unitNo of 0. All BOMLines
             under this window will be shown or hide depending upon the values set in map bomWinPropFlagMap.
             

Use Cases:

             This operation creates a list of window and sets the respective input Item revision
             as the top line. This operation can be used to set multiple saved variant rules or
             single stored option set to the window.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param Info: 
                         list of objects containing window creation information
             
        :return: 
        """
        ...
    def FindModelViewsInStructure(self, Disclosure: Teamcenter.Soa.Client.Model.ModelObject, StructureScope: list[Teamcenter.Soa.Client.Model.ModelObject], ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, WithDisclosureIntent: list[str], Options: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Cad._2016_03.StructureManagement.FindModelViewsInStructureResponse: ...
    def ContinueFindModelViews(self, SearchID: str, StopFind: bool) -> Teamcenter.Services.Strong.Cad._2016_09.StructureManagement.FindModelViewsResponse:
        """    
             Continues a search for model views that was started by the startFindModelViews
             operation. The input searchID specifies which
             partial find to continue.
             

Dependencies:

             startFindModelViews
             

Teamcenter Component:

             Disclosure - Component that is used to represent the 3D equivalent of the 2D drawing.
             
        :param SearchID: 
                         A unique identifier passed by the client in order to identify the find partial results
                         to continue searching from where the previous operation (whether <b>startFindModelViews</b>
                         or <b>continueFindModelViews</b> ) left off.
             
        :param StopFind: 
                         If true, the find associated to the input <font face="courier" height="10">searchID</font>
                         will be terminated instead of returning any further results. If false, the state
                         of the find is cleaned up and the given <font face="courier" height="10">searchID</font>
                         may no longer be used as input into the <b>continueFindModelViews</b> operation..
             
        :return: contains
             an invalid value (either never valid or the find has finished or been stopped by
             the client.)
        """
        ...
    def ContinueReconcilePalette(self, ReconcilePaletteInput: Teamcenter.Services.Strong.Cad._2016_09.StructureManagement.NextReconcilePaletteInput) -> Teamcenter.Services.Strong.Cad._2016_09.StructureManagement.ReconcilePaletteResponse:
        """    
             This operation continues the reconciliation of Fnd0ModelViewProxy object references
             in a Fnd0ModelViewPalette object for a given product structure and configuration.
             The Fnd0ModelViewProxy objects are authored and managed by  CAD applications,
             and their lifecycle is delegated to their CAD owning model's lifecycle.  As the CAD
             owning models are updated, so are their Fnd0ModelViewProxy objects.  However,
             the Fnd0ModelViewPalette objects that reference these Fnd0ModelViewProxy
             objects are not automatically updated during CAD model update in all cases, because
             there are times when this update needs to be carefully controlled by users.  Consequently,
             the Fnd0ModelViewPalette can get out of synchronization with the structure
             it is attached to.  This service operation is provided to help reconcile differences
             between the loaded structure configuration and an existing Fnd0ModelViewPalette
             in a user controlled manner.  It provides the caller with information about which
             Fnd0ModelViewProxy objects should be removed and which should be replaced
             by analyzing the current configured structure and comparing it to what was found
             in an existing Fnd0ModelViewPalette.
             
             The Fnd0ModelViewPalette contains Fnd0ModelViewProxy object references
             for  components belonging to the product structure. When the components in the structure
             gets revised, cloned, removed, or a model view is deleted or unpublished, or when
             the structure configuration gets changed, the Fnd0ModelViewPalette needs to
             be reconciled against the current structure in order to get the proper Fnd0ModelViewProxy
             objects corresponding to the updated structure. Using this operation, a list of Fnd0ModelViewProxy
             objects that need to be replaced or removed for a given Fnd0ModelViewPalette
             can be identified, retrieved, and presented to user, so that the user can carefully
             control the update of the Fnd0ModelViewPalette for the various update use
             cases.
             
             This operation is designed in such a way that the caller can use it in a threaded
             operation and display results in batches instead of waiting for the entire reconciliation
             process to be complete which may take a fair amount of time for large structures.
             Before invoking this this operation, the startReconcilePalette
             operation should have been invoked for the same clientID.
             
Note: The reconcile process has to be closed by the caller using the continueReconcilePalette operation with stopReconcile as true. For example the caller calls startReconcilePalette operation followed by continueReconcilePalette operation. Once the finished variable
             is returned as true in the response the caller calls continueReconcilePalette
             with stopReconcile as true so that the resources
             are freed up in the server.
             

Use Cases:

             The operation supports the following use cases.
             
Use Case 1 :  Update a Fnd0ModelViewPalette per informal engineering
             change (i.e. overwrite)
             
             1.An authoring user creates a detailed design in a CAD application.  The user creates
             and publishes Model Views describing the design details. The Model Views are persisted
             in Teamcenter as Fnd0ModelViewProxy objects using the operation createOrUpdateModelViewProxies.
             
             2.The authoring user opens a configured product structure in a visualization enabled
             Teamcenter application and finds the published Fnd0ModelViewProxy objects
             in the product structure using the operation findModelViewsInStructure.
             
             3.The authoring user selects a limited subset of the Fnd0ModelViewProxy objects
             found, adds them to a Palette, organizes them for presentation by re-ordering and
             grouping, and creates a Fnd0ModelViewPalette object in Teamcenter which references
             Fnd0ModelViewProxy objects using the operation createOrUpdateModelViewPalette.
             
             4.A reviewing user opens the product structure configuration along with the Fnd0ModelViewPalette
             into a visualization enabled Teamcenter application, reviews each Model View for
             accuracy, creates review comments for changes that need to be made, and submits those
             changes to the CAD Designer that authored the original detailed design.
             
             5.The authoring user receives the review comments from various reviewing users, and
             uses the CAD application to make changes to the CAD model(s) such as add or remove
             components, reposition or change parts, add, delete, or change model views, publish
             or unpublish model views, etc.  The updated CAD models are saved to Teamcenter along
             with updated Fnd0ModelViewProxy objects using the operation createOrUpdateModelViewProxies.  Since this is informal change,
             the CAD models are typically overwritten as opposed to revised.
             
             6.The authoring user opens the configured product structure with attached Fnd0ModelViewPalette
             created in step 3 in a visualization enabled Teamcenter application, and some of
             the Fnd0ModelViewProxy objects referenced by the Fnd0ModelViewPalette
             are no longer valid relative to the current structure due to the CAD model changes.
             The user invokes the palette reconcile action which triggers the operation startReconcilePalette followed by continueReconcilePalette. The results are displayed to the user
             providing information on which Fnd0ModelViewProxy objects are still valid,
             which need to be replaced, and which need to be removed in order to update the Palette.
             The results are streamed to the client  in batches, so the user is updated on progress
             and can choose to stop the reconcile operation at any time.
             
             7.The authoring user updates the Fnd0ModelViewPalette per the changes suggested
             by this operation, and saves the palette updates using the operation createOrUpdateModelViewPalette.
             

Use Case 2: Update a Fnd0ModelViewPalette to a different structure
             configuration
             
             1.The user opens a structure configuration different from that used to author the
             original Fnd0ModelViewPalette (per use case 1), and sends this to the visualization
             enabled palette authoring tool in Teamcenter.
             
             2.The user opens the Fnd0ModelViewPalette and invokes the palette reconcile
             action which triggers the operation startReconcilePalette
             followed by continueReconcilePalette. The
             results are displayed to the user providing which Fnd0ModelViewProxy objects
             cannot be found, which are still valid, which need to be replaced, and which need
             to be removed in order to reconcile the Palette to the current structure configuration.
             The results are streamed to the client  in batches, so the user is updated on progress
             and can choose to stop the reconcile operation at any time.
             
             3.The authoring user updates the Fnd0ModelViewPalette per the changes suggested
             by the operation, and saves the palette updates using the operation createOrUpdateModelViewPalette. The updated structure configuration
             information used for the updated palette is stored with the palette.
             

Use Case 3 : Update a Fnd0ModelViewPalette per formal engineering change
             (i.e. Revise)
             
             1.The user of a CAD application makes changes to the CAD model(s) representing the
             detailed design such as revising components, add, delete, or change model views,
             publish or unpublish model views, etc during revise of a detailed design.  The revised
             CAD models are saved to Teamcenter, where new and updated Fnd0ModelViewProxy
             objects are published using the operation createOrUpdateModelViewProxies
             and Teamcenter deep copy rules come into play.
             
             2.The user opens the configured product structure with attached Fnd0ModelViewPalette
             (see use case 1) in a visualization enabled Teamcenter application, and some of the
             Fnd0ModelViewProxy objects referenced by the Fnd0ModelViewPalette are
             no longer valid due to the revised CAD model(s).  Some of the Fnd0ModelViewProxy
             objects in the Fnd0ModelViewPalette are from previous revisions of the revised
             components, others cannot be found. The user invokes the palette reconcile action
             which triggers the operation startReconcilePalette
             followed by continueReconcilePalette. The
             results are displayed to the user providing information on which Fnd0ModelViewProxy
             objects are still valid, which need to be replaced with Fnd0ModelViewProxy
             objects on new revisions of the CAD models, and which need to be removed in order
             to update the Palette.  The results are streamed to the client  in batches, so the
             user is updated on progress and can choose to stop and restart the reconcile operation
             at any time.
             
             3.The user updates the Fnd0ModelViewPalette per the changes suggested by this
             operation, and saves the updated palette using the operation createOrUpdateModelViewPalette.
             

Dependencies:

             createOrUpdateModelViewPalette, createOrUpdateModelViewProxies, findModelViewsInStructure,
             startReconcilePalette
             

Teamcenter Component:

             Disclosure - Component that is used to represent the 3D equivalent of the 2D drawing.
             
        :param ReconcilePaletteInput: 
                         Input that contains the reconciliation state identifier and the <b>Fnd0ModelViewProxy</b>
                         if they have to prioritized for reconciliation.
             
        :return: 
        """
        ...
    def StartFindModelViews(self, FindInput: Teamcenter.Services.Strong.Cad._2016_09.StructureManagement.FindModelViewsInput) -> Teamcenter.Services.Strong.Cad._2016_09.StructureManagement.FindModelViewsResponse:
        """    
             Finds Model View Proxy (Fnd0ModelViewProxy) objects associated to any objects
             within the specified structure. This operation is most often used when creating a
             disclosure object.
             

             Objects that act as a disclosure are Items or Worksets that have a relation of Fnd0DisclosingObject
             to the actual design objects being disclosed and hence intend to have a list of disclosed
             Model View Proxy objects.
             

             Used in conjunction with the continueFindModelViews operation. If the preference
             MVFindMinNodeCount has a value, that value is the minimum number of structure
             nodes to search before returning with finished
             as false.
             

Use Cases:

             This API supports the following use cases:
             
             Use Case 1: Creation of a new design disclosure


             The operation can be used for supporting creation of a disclosure object. The disclosure
             object will most commonly be a Workset (Cpd0Workset subtype) but may also
             be a specific type of Item Revision. The actual disclosure object may be pre-existing
             but would not be acting as a disclosure until this operation creates and attaches
             the desired list of disclosed model view references.
             

             The purpose of a design disclosure is to act as a 3D equivalent of a 2D drawing.
             This disclosure object will collect all geometry including background geometry if
             necessary and PMI needed to show all views describing the detailed design for the
             object being disclosed. The disclosure content may be organized into the following
             item revisions or subsets (depending on the disclosure type):
             
             Foreground content - actual installation assembly reference
             
             Background content - context of a product into which the installation assembly is
             used.
             
             Separately collected geometry - such as welds between the foreground and background
             objects.
             

             To create the correct model view list (see the createOrUpdateModelViewPalette
             service operation), the client and user must first find candidate model view proxies
             from which to choose the necessary proxies to disclose.
             

             During the operation, a designer would create a Workset to collect all geometry needed
             to support  installation assembly PMI. It is done to collect assemblies being installed
             and where they are being installed so that PMI and model views associated with this
             combination can be authored and then disclosed. The following types of geometry may
             be collected in a single Workset:
             
             Foreground Subset
             
             Background Subset
             
ItemRevision (Weld Collector)
             

             Multiple CAD Designers will be concurrently authoring PMI and Model Views (MVs) for
             disclosure at multiple levels of the sub-assemblies under the installation assembly.
             All the MVs authored at this time are undisclosed. However, some of them will be
             marked as a candidates for disclosure.
             
             Owning model (ItemRevision) must exist prior to creating the MV proxy in teamcenter
             by a new service operation createOrUpdateModelViewProxies. The owing model
             will be specified as a request parameter for each MV proxy.
             

             A visualization user begins Disclosure authoring by retrieving the above mentioned
             collector workset and making sure it has disclosing object (Fnd0DisclosingObject)
             relations to the actual installation item revisions whose design is being disclosed.
             They will then use the startFindModelViews operation followed by the continueFindModelViews
             operation to find model views that are marked as candidates for disclosure and then
             use a third operation (createOrUpdateModelViewPalette) to create the list
             of actually disclosed model views to be persisted for the Disclosure being updated.
             
             Note:
             
             Candidate Disclosed Model Views will be retrievedfrom all structure nodes that are
             not suppressed or children of suppressed nodes, and then filtered only by any provided
             values in the withDisclosureIntents.
             

Teamcenter Component:

             Disclosure - Component that is used to represent the 3D equivalent of the 2D drawing.
             
        :param FindInput: 
                         The inputs needed to start a find operation on one or more objects that support model
                         views.
             
        :return: 215300 - Invalid request since startingScopes and disclosure are both not provided.
        """
        ...
    def StartReconcilePalette(self, ReconcilePaletteInput: Teamcenter.Services.Strong.Cad._2016_09.StructureManagement.ReconcilePaletteInput) -> Teamcenter.Services.Strong.Cad._2016_09.StructureManagement.ReconcilePaletteResponse:
        """    
             This operation starts the reconciliation of Fnd0ModelViewProxy object references
             in a Fnd0ModelViewPalette object for a given product structure and configuration.
             The Fnd0ModelViewProxy objects are authored and managed by  CAD applications,
             and their lifecycle is delegated to their CAD owning model's lifecycle.  As the CAD
             owning models are updated, so are their Fnd0ModelViewProxy objects.  However,
             the Fnd0ModelViewPalette objects that reference these Fnd0ModelViewProxy
             objects are not automatically updated during CAD model update in all cases, because
             there are times when this update needs to be carefully controlled by users.  Consequently,
             the Fnd0ModelViewPalette can get out of synchronization with the structure
             it is attached to. This service operation is provided to help reconcile differences
             between the loaded structure configuration and an existing Fnd0ModelViewPalette
             in a user controlled manner.  It provides the caller with information about which
             Fnd0ModelViewProxy objects should be removed and which should be replaced
             by analyzing the current configured structure and comparing it to what was found
             in an existing Fnd0ModelViewPalette.
             
             The Fnd0ModelViewPalette contains Fnd0ModelViewProxy object references
             for  components belonging to the product structure. When the components in the structure
             gets revised, cloned, removed, or a model view is deleted or unpublished, or when
             the structure configuration gets changed, the Fnd0ModelViewPalette needs to
             be reconciled against the current structure in order to get the proper Fnd0ModelViewProxy
             objects corresponding to the updated structure.  Using this operation, a list of
             Fnd0ModelViewProxy objects that need to be replace or removed for a given
             Fnd0ModelViewPalette can be identified, retrieved and presented to user, so
             that the user can carefully control the update of the Fnd0ModelViewPalette
             for the various update use cases.
             
             This operation is designed in such a way that the caller can use it in a threaded
             operation and display results in batches instead of waiting for the entire reconciliation
             process to be complete which may take a fair amount of time for large structures.
             This operation is thus supplemented by continueReconcilePalette
             operation.
             
Note: The reconcile process has to be closed by the caller using the continueReconcilePalette operation with stopReconcile as true. For example the caller calls startReconcilePalette operation followed by continueReconcilePalette operation. Once the finished variable
             is returned as true in the response the caller calls continueReconcilePalette
             with stopReconcile as true so that the resources
             are freed up in the server.
             

Use Cases:

             The operation supports the following use cases.
             
Use Case 1 : Update a Fnd0ModelViewPalette per informal engineering
             change (i.e. overwrite)
             
             1. An authoring user creates a detailed design in a CAD application.  The user creates
             and publishes Model Views describing the design details. The Model Views are persisted
             in Teamcenter as Fnd0ModelViewProxy objects using the operation createOrUpdateModelViewProxies.
             
             2. The authoring user opens a configured product structure in a visualization enabled
             Teamcenter application and finds the published Fnd0ModelViewProxy objects
             in the product structure using the operation findModelViewsInStructure.
             
             3. The authoring user selects a limited subset of the Fnd0ModelViewProxy objects
             found, adds them to a Palette, organizes them for presentation by re-ordering and
             grouping, and creates a Fnd0ModelViewPalette object in Teamcenter which references
             Fnd0ModelViewProxy objects using the operation createOrUpdateModelViewPalette.
             
             4. A reviewing user opens the product structure configuration along with the Fnd0ModelViewPalette
             into a visualization enabled Teamcenter application, reviews each Model View for
             accuracy, creates review comments for changes that need to be made, and submits those
             changes to the CAD Designer that authored the original detailed design.
             
             5. The authoring user receives the review comments from various reviewing users,
             and uses the CAD application to make changes to the CAD model(s) such as add or remove
             components, reposition or change parts, add, delete, or change model views, publish
             or unpublish model views, etc.  The updated CAD models are saved to Teamcenter along
             with updated Fnd0ModelViewProxy objects using the operation createOrUpdateModelViewProxies.  Since this is informal change,
             the CAD models are typically overwritten as opposed to revised.
             
             6. The authoring user opens the configured product structure with attached Fnd0ModelViewPalette
             created in step 3 in a visualization enabled Teamcenter application, and some of
             the Fnd0ModelViewProxy objects referenced by the Fnd0ModelViewPalette
             are no longer valid relative to the current structure due to the CAD model changes.
             The user invokes the palette reconcile action which triggers the operation startReconcilePalette followed by continueReconcilePalette. The results are displayed to the user
             providing information on which Fnd0ModelViewProxy objects are still valid, which
             need to be replaced, and which need to be removed in order to update the Palette.
             The results are streamed to the client  in batches, so the user is updated on progress
             and can choose to stop the reconcile operation at any time.
             
             7. The authoring user updates the Fnd0ModelViewPalette per the changes suggested
             by this operation, and saves the palette updates using the operation createOrUpdateModelViewPalette.
             

Use Case 2: Update a Fnd0ModelViewPalette to a different structure
             configuration
             
             1.The user opens a structure configuration different from that used to author the
             original Fnd0ModelViewPalette (per use case 1), and sends this to the visualization
             enabled palette authoring tool in Teamcenter.
             
             2.The user opens the Fnd0ModelViewPalette and invokes the palette reconcile
             action which triggers the operation startReconcilePalette
             followed by continueReconcilePalette. The
             results are displayed to the user providing which Fnd0ModelViewProxy objects
             cannot be found, which are still valid, which need to be replaced, and which need
             to be removed in order to reconcile the Palette to the current structure configuration.
             The results are streamed to the client  in batches, so the user is updated on progress
             and can choose to stop the reconcile operation at any time.
             
             3.The authoring user updates the Fnd0ModelViewPalette per the changes suggested
             by the operation, and saves the palette updates using the operation createOrUpdateModelViewPalette. The updated structure configuration
             information used for the palette update is stored with the palette.


             Use Case 3 : Update a Fnd0ModelViewPalette per formal engineering change
             (i.e. Revise)
             
             1.The user of a CAD application makes changes to the CAD model(s) representing the
             detailed design such as revising components, add, delete, or change model views,
             publish or unpublish model views, etc during revise of a detailed design.  The revised
             CAD models are saved to Teamcenter, where new and updated Fnd0ModelViewProxy
             objects are published using the operation createOrUpdateModelViewProxies
             and Teamcenter deep copy rules come into play.
             
             2.The user opens the configured product structure with attached Fnd0ModelViewPalette
             (see use case 1) in a visualization enabled Teamcenter application, and some of the
             Fnd0ModelViewProxy objects referenced by the Fnd0ModelViewPalette are
             no longer valid due to the revised CAD model(s).  Some of the Fnd0ModelViewProxy
             objects in the Fnd0ModelViewPalette are from previous revisions of the revised
             components, others cannot be found. The user invokes the palette reconcile action
             which triggers the operation startReconcilePalette
             followed by continueReconcilePalette. The
             results are displayed to the user providing information on which Fnd0ModelViewProxy
             objects are still valid, which need to be replaced with Fnd0ModelViewProxy
             objects on new revisions of the CAD models, and which need to be removed in order
             to update the Palette.  The results are streamed to the client  in batches, so the
             user is updated on progress and can choose to stop and restart the reconcile operation
             at any time.
             
             3.The user updates the Fnd0ModelViewPalette per the changes suggested by this
             operation, and saves the updated palette using the operation createOrUpdateModelViewPalette.
             

Dependencies:

             createOrUpdateModelViewPalette, createOrUpdateModelViewProxies, findModelViewsInStructure
             

Teamcenter Component:

             Disclosure - Component that is used to represent the 3D equivalent of the 2D drawing.
             
        :param ReconcilePaletteInput: 
                         Input that contains the <b>Fnd0ModelViewPalette</b> or <b>Fnd0ModelViewProxy</b>
                         that needs to be reconciled and the configuration information.
             
        :return: 
        """
        ...
    def WriteAssemblyConfigurationDetails(self, BomWindow: Teamcenter.Soa.Client.Model.ModelObject, OptionSetName: str) -> Teamcenter.Services.Strong.Cad._2018_06.StructureManagement.AssemblyConfigurationResponse: ...
    def CreateOrReConfigureBOMWindows(self, Info: list[Teamcenter.Services.Strong.Cad._2019_06.StructureManagement.CreateWindowsInfo3]) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateBOMWindowsResponse: ...
    def ExpandPSOneLevel2(self, Info: Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSOneLevelInfo, Prefs: Teamcenter.Services.Strong.Cad._2023_06.StructureManagement.ExpandPSOneLevelPref) -> Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSOneLevelResponse2: ...

