import System
import System.Collections
import Teamcenter.Services.Strong.Classification._2007_01.Classification
import Teamcenter.Services.Strong.Classification._2009_10.Classification
import Teamcenter.Services.Strong.Classification._2011_06.Classification
import Teamcenter.Services.Strong.Classification._2011_12.Classification
import Teamcenter.Services.Strong.Classification._2015_03.Classification
import Teamcenter.Services.Strong.Classification._2015_10.Classification
import Teamcenter.Services.Strong.Classification._2016_03.Classification
import Teamcenter.Services.Strong.Classification._2016_09.Classification
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class ClassificationRestBindingStub(ClassificationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateClassificationObjects(self, ClsObjs: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.ClassificationObject]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.CreateClassificationObjectsResponse: ...
    def DeleteClassificationObjects(self, ClsObjTags: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def FindClassifiedObjects(self, IcoTags: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.FindClassifiedObjectsResponse: ...
    def GetAttributesForClasses(self, ClassIds: list[str]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.GetAttributesForClassesResponse: ...
    def GetChildren(self, GroupOrClassIds: list[str]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.GetChildrenResponse: ...
    def GetClassDescriptions(self, ClassIds: list[str]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.GetClassDescriptionsResponse: ...
    def GetClassificationObjects(self, ClsObjTags: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.GetClassificationObjectsResponse: ...
    def GetFileIds(self, Criteria: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.GetFileIdCriteria]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.GetFileIdsResponse: ...
    def GetKeyLOVs(self, KeyLOVIds: list[str]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.GetKeyLOVsResponse: ...
    def GetParents(self, ChildIds: list[str]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.GetParentsResponse: ...
    def GetPartFamilyTemplates(self, ClsClassIds: list[str]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.GetPartFamilyTemplatesResponse: ...
    def Search(self, SearchCriteria: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.SearchClassAttributes]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.SearchResponse: ...
    def SearchByInstanceId(self, InstanceIdQueries: list[str]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.SearchByInstanceIdResponse: ...
    def SearchForClasses(self, Criteria: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.SearchForClassesCriteria]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.SearchForClassesResponse: ...
    def UpdateClassificationObjects(self, ClsObjs: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.ClassificationObject]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.UpdateClassificationObjectsResponse: ...
    def FindClassificationObjects(self, WsoIds: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.FindClassificationObjectsResponse: ...
    def CreateOrUpdateKeyLOVs(self, KeyLOVsInput: list[Teamcenter.Services.Strong.Classification._2009_10.Classification.KeyLOVDefinition2]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetAttributesForClasses2(self, ClassIds: list[str]) -> Teamcenter.Services.Strong.Classification._2009_10.Classification.GetAttributesForClassesResponse2: ...
    def GetKeyLOVs2(self, KeyLOVIds: list[str]) -> Teamcenter.Services.Strong.Classification._2009_10.Classification.GetKeyLOVsResponse2: ...
    def AutoComputeAttributes(self, IcoId: str, Wso: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject, ClassId: str, ViewId: str, InputAttrs: System.Collections.Hashtable, UnitSystem: int, Mode: int) -> Teamcenter.Services.Strong.Classification._2009_10.Classification.AutoComputeAttributesResponse: ...
    def DeleteChildrenInHierarchy(self, OptionsInput: list[Teamcenter.Services.Strong.Classification._2011_06.Classification.HierarchyInfoAndOptions]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetLibraryHierarchy(self, LibraryValues: list[str]) -> Teamcenter.Services.Strong.Classification._2011_06.Classification.GetLibraryHierarchyResponse: ...
    def GetClassificationObjectInfo(self, IcoUids: list[str], AttributeIds: list[int], GetOptimizedValues: bool, FetchDescriptor: bool, Locale: str) -> Teamcenter.Services.Strong.Classification._2011_12.Classification.ClassificationInfoResponse: ...
    def GetKeyLOVsForDependentAttributes(self, DependencyAttributeStruct: list[Teamcenter.Services.Strong.Classification._2015_03.Classification.DependencyAttributeStruct]) -> Teamcenter.Services.Strong.Classification._2015_03.Classification.GetDependencyKeyLOVsResponse: ...
    def GetClassDefinitions(self, ClassIDs: list[str]) -> Teamcenter.Services.Strong.Classification._2015_10.Classification.GetClassDefinitionsResponse: ...
    def ConvertValues(self, ValueConversionInputs: list[Teamcenter.Services.Strong.Classification._2016_03.Classification.ValueConversionInput]) -> Teamcenter.Services.Strong.Classification._2016_03.Classification.ConvertValuesResponse: ...
    def GetChildrenExtended(self, ClassObjects: list[Teamcenter.Soa.Client.Model.ModelObject], FilterForWriteAccess: bool, Options: int) -> Teamcenter.Services.Strong.Classification._2016_03.Classification.GetChildrenExtendedResponse: ...
    def SearchClassesExtended(self, SearchCriterias: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.SearchAttribute], SortAttributes: list[int], FilterForWriteAccess: bool, Options: int) -> Teamcenter.Services.Strong.Classification._2016_03.Classification.SearchClassesExtendedResponse: ...
    def FindValues(self, FindValueInputs: list[Teamcenter.Services.Strong.Classification._2016_09.Classification.FindValueInput]) -> Teamcenter.Services.Strong.Classification._2016_09.Classification.FindValuesResponse: ...

class ClassificationService:
    """
    
            The Classification service helps achieve
            different classification operations and utilizes a classification hierarchy to categorize
            your company's product data. The service allows users to create classification objects
            and associate them to workspace objects in order to classify the workspace objects.
            Classification service can also be
            used to perform add, update, or delete operations on the classification hierarchy
            and retrieve information about the hierarchy.
            
            The Classification service contains
            operations to achieve the following:
            

Create classification objects and optionally attach them to workspace
            objects
            
Update existing classification objects
            
Delete existing classification objects
            
Get information on classification objects
            
Search for classification objects and classified objects
            
Get information on classification class hierarchies
            
Get children information for a classification class in a hierarchy
            
Get parent's information for a classification class in a hierarchy
            
Delete classification class hierarchy
            
Get detailed information for a classification class
            
Get information on classification class attributes
            
Search for classification classes
            
Create or update classification key-LOV objects
            
Get information on classification key-LOV objects
            
Get part family templates information associated with a class
            

            .
            

Dependencies:

            DataManagement
            


Library Reference:

TcSoaClassificationStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ClassificationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateClassificationObjects(self, ClsObjs: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.ClassificationObject]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.CreateClassificationObjectsResponse:
        """    
             Creates one or more classification objects and (optionally) attach them to a workspace
             object, thus classifying it. When the Classification objects are not associated with
             any workspace object, they would act as standalone Classification objects. A classification
             object is also called ICO
             

Use Cases:

             User wants to classify a workspace object or create a standalone classification object
             (ICO) in Teamcenter. This operation can be combined with other operations like createItems()
             to create workspace object and then associate the workspace object to the classification
             object. Before creating a classification object, a classification class hierarchy
             should already be created by the classification admin user in Teamcenter. This hierarchy
             should include a storage class (a class that allows instances to be created and associated
             to it) for which the classification objects need to be created. Values of any attributes
             associated with classification objects can also be populated.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClsObjs: 
                         List of structure containing information about the classification object(ICO) that
                         needs to be created including its attribute values. It also includes the classification
                         class information for which classification object will be created &amp; information
                         on workspace object being classified.
             
        :return: 
        """
        ...
    def DeleteClassificationObjects(self, ClsObjTags: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Deletes one or more classification objects permanently. A classification object is
             also called ICO. The classified workspace object associated with the ICO will not
             be deleted
             

Use Cases:

             User needs to delete classification objects. It is typically called when after creating
             or searching the classification objects, user decides that the returned objects are
             not needed anymore
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClsObjTags: 
                         Unique Business Object(s) representing the classification object(s) to be deleted.
             
        :return: 
        """
        ...
    def FindClassifiedObjects(self, IcoTags: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.FindClassifiedObjectsResponse:
        """    
             Finds the workspace objects (WSO) associated with input Teamcenter classification
             objects. A classification object is also called ICO. Each ICO can have only one workspace
             object associated with it.
             

Use Cases:

             When user need to find workspace objects based on classification objects (ICO) that
             were created when workspace objects were classified.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param IcoTags: 
                         List of classification object (ICO) Business Objects, whose corresponding   workspace
                         objects need to be found
             
        :return: 
        """
        ...
    def GetAttributesForClasses(self, ClassIds: list[str]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.GetAttributesForClassesResponse:
        """    
             Provides information on class attributes for the classification classes based on
             input classification class ids. Detailed information about class attributes is provided
             & includes class attribute name, description, format, unit system, minimum/maximum
             value & configuration set
             

Use Cases:

             When user wants to view details of all class attributes associated with a classification
             class. This operation is similar to getAttributesForClasses2(), but provides information
             in a slightly different format. Typically, the information about class attributes
             is used to determine which classification class a workspace object shall be classified
             into
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClassIds: 
                         Identifier for the classification class whose attribute information is requested.
             
        :return: 
        """
        ...
    def GetChildren(self, GroupOrClassIds: list[str]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.GetChildrenResponse:
        """    
             Gets the information about immediate children in classification hierarchy for given
             group or class identifier(s).
             
             Returns a GetChildrenResponse structure
             containing:
             

Retrieved child classes in the ServiceData
             list of plain objects
             
Any failures with Class ID mapped to the error message in the ServiceData list of partial errors.
             



Use Cases:

             User wants to get details of all groups or classes that lie under a particular group
             or class in a classification class hierarchy.
             

             Returns a GetChildrenResponse structure
             containing:
             

Retrieved child classes in the ServiceData
             list of plain objects
             
Any failures with Class ID mapped to the error message in the ServiceData list of partial errors.
             



Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param GroupOrClassIds: 
                         Unique ID(s) of the classification class or group whose immediate children need to
                         be determined in the classification class hierarchy
             
        :return: 
        """
        ...
    def GetClassDescriptions(self, ClassIds: list[str]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.GetClassDescriptionsResponse:
        """    
             Gets detailed information about a classification class based on classification class
             ID. This information includes class type, parent, name, description, unit system
             and user data associated with the class.  It also includes a count of children, number
             of classification views & number of instances of classification objects associated
             with the classification class. Information can also be obtained on any documents
             such as images & icons attached to the classification class.
             

Use Cases:

             When user need details of classification classes. These details can help user decide
             whether to classify a workspace object in particular classification classes.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClassIds: 
                         List of unique identifiers for classification classes whose details are needed.
             
        :return: 
        """
        ...
    def GetClassificationObjects(self, ClsObjTags: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.GetClassificationObjectsResponse:
        """    
             Looks for specified classification objects. If they are found, then detailed information
             about those objects is provided. A classification object is also called ICO
             

Use Cases:

             When user need to find an existing classification object to either view or update
             its details. It can be followed by operations like updateClassificationObjects()
             or deleteClassificationObjects() to
             update or delete the classification objects.
             
             The operation findClassificationObjects()
             can be used to get the list of classification objects, associated with workspace
             objects. Then, this operation getClassificationObjects()
             is used to get the detailed information on the classification objects.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClsObjTags: 
                         The classification object(s) for which detailed information is required.
             
        :return: 
        """
        ...
    def GetFileIds(self, Criteria: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.GetFileIdCriteria]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.GetFileIdsResponse:
        """    
             Gets the file information from any dataset that is associated with workspace object(s).
             The dataset type can be specified along with the relation used when it is attached
             to a workspace object. Information corresponding to a particular file inside a dataset
             can be retrieved.
             

Use Cases:

             User wants to get information about files inside a dataset that is associated with
             workspace objects (WSO). Typically it will be used to get and view the  image or
             icon files associated with datasets attached to workspace objects.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param Criteria: 
                         List of structures containing information on the workspace objects (WSO) to which
                         the datasets are attached, the type of datasets, relation in which dataset is attached
                         to the WSO, and the named reference inside the dataset. All this information can
                         be used to get to a particular file inside a dataset
             
        :return: 
        """
        ...
    def GetKeyLOVs(self, KeyLOVIds: list[str]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.GetKeyLOVsResponse:
        """    
             Gets the information for classification key-LOVs  based on given ID(s). Information
             such as key-LOV's name, display options, and key and value entries can be obtained.
             A key-LOV is a list of values used in classification. The key-LOVs are used to define
             one or more values that can be set for classification dictionary attributes
             

             Typical format of a key-LOV -
             

                 <key-LOV ID>:<key-LOV Name>
             
                 <Key10>:<Value10>
             
                 <Key20>:<Value20>
             

             Example of a key-LOV
             

             - 33381:Design Categories
             
                 Des1:Bearing
             
                 Des2:Bracket
             
                 Des3:Frame
             
                 Des4:LeadBox
             


Use Cases:

             User wants to retrieve the information for an existing key-LOV using the key-LOV's
             unique identifier. The operation is similar to getKeyLOVs2().
             But getKeyLOVs2()provides more detailed
             information about any key-LOVs .
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param KeyLOVIds: 
                         List of IDs of classification key-LOV, for which information is required. The key-LOV
                         ID is a unique negative integer that identifies a key-LOV. In the Teamcenter rich
                         client, key-LOVs can be accessed in the "Key LOVs" tab of the Classification Administration
                         application. The key-LOV ID can be found in the "Key/ID" field of a key-LOV definition
                         there.
             
        :return: 
        """
        ...
    def GetParents(self, ChildIds: list[str]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.GetParentsResponse:
        """    
             Gets the classification class ID(s) of all parent classes in a hierarchy, based on
             given classification class ID. The parent class IDs are sorted as immediate parent
             first, toplevel parent last.
             

Use Cases:

             User needs to determine all the parent classes for any given class in a classification
             hierarchy.  If user needs to get the children of the given class ID, then getChildren() operation shall be used.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ChildIds: 
                         The unique identifier IDs for classification classes for which parent class ID information
                         is being requested
             
        :return: 
        """
        ...
    def GetPartFamilyTemplates(self, ClsClassIds: list[str]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.GetPartFamilyTemplatesResponse:
        """    
             Finds the information for part family templates (PFT) based on the classification
             class IDs. Part family templates can be used to define geometry and certain properties
             of the geometry as variable properties. They can be attached to a classification
             class. For any classification class, user can find out the associated part family
             templates and their information.
             

Use Cases:

             While using graphics builder, users often require information about the part family
             template attached to the classification classes.  Graphics builder is a program used
             by classification administration that communicates with the Teamcenter server to
             generate graphics. The graphics builder uses NX libraries.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClsClassIds: 
                         List of IDs of classification classes for which the associated part family template
                         information is required.
             
        :return: 
        """
        ...
    def Search(self, SearchCriteria: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.SearchClassAttributes]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.SearchResponse:
        """    
             Finds all the classification objects based on classification class IDs, classification
             attribute ID and an expression for classification attribute value. A classification
             object is also called an ICO.
             

Use Cases:

             User needs to search for classification objects based on the class where they are
             classified and the value of classification attributes.Another related operation for
             searching classification objects is searchByInstanceID(),
             that can search for classification objects based on their IDs
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param SearchCriteria: 
                         List of structures containing classification class ID, classification attribute ID,
                         and an expression for classification attribute value (e.g. &gt;= 20.00 ).
             
        :return: 
        """
        ...
    def SearchByInstanceId(self, InstanceIdQueries: list[str]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.SearchByInstanceIdResponse:
        """    
             Finds all the classification objects based on their IDs. A classification object
             is also called an ICO. If the ICO classifies a workspace object, then ICO ID would
             be same as the workspace object ID
             

Use Cases:

             User wants to search for classification objects based on their IDs. The returned
             objects can then be used as input for operations like findClassifiedObjects(),
             which is used to search workspace objects associated with the ICOs.
             
             Another related operation for searching classification objects is search(), that can search for classification objects based
             on class ID and attribute values
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param InstanceIdQueries: 
                         List of IDs of classification objects. These can contain wildcards ( e.g. ICO00*
                         ).
             
        :return: 
        """
        ...
    def SearchForClasses(self, Criteria: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.SearchForClassesCriteria]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.SearchForClassesResponse:
        """    
             Finds the classification classes based on provided search criteria and provides detailed
             information about those classes.  The user can search using a search expression on
             attributes of the class (Class ID, Name, Type etc.)  . For example, the user shall
             be able to search all the classes whose name begins with a particular set of characters
             and where the class ID matches certain pattern. The order of search results can also
             be sorted on various criteria.
             

Use Cases:

             The user needs to search for classification classes using a search criterion based
             on various attributes of a class. The search criterion can be based on one or more
             attributes
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param Criteria: 
                         List of structure containing search expression, search attributes, and sort options
                         for search results
             
        :return: 
        """
        ...
    def UpdateClassificationObjects(self, ClsObjs: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.ClassificationObject]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.UpdateClassificationObjectsResponse:
        """    
             Updates existing classification objects. A classification object is also called ICO.
             Values of various ICO attributes can be modified
             

Use Cases:

             User wants to update values of the attributes for an existing classification object
             in Teamcenter. E.g. user wants to modify an integer value of a class attribute ("Length")
             for an existing ICO. This operation is typically used after creating the classification
             objects using createClassificationObjects().
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClsObjs: 
                         List of structures containing information about classification objects that needs
                         to be modified,  along with the information that needs to be updated
             
        :return: 
        """
        ...
    def FindClassificationObjects(self, WsoIds: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]) -> Teamcenter.Services.Strong.Classification._2007_01.Classification.FindClassificationObjectsResponse:
        """    
             Finds the classification objects associated with input workspace objects (WSO). A
             classification object is also called ICO. Each workspace object can have one or more
             ICOs associated with it.
             

Use Cases:

             When user need to find classification objects (ICO) based on workspace objects. Each
             time a workspace object is classified in a classification class a classification
             object (ICO) object is created.  After searching for all the classification objects
             corresponding to a workspace object, user can find more information about the classification(s)
             of a workspace object. The operation getClassificationObjects() can be used to get detailed information about
             the classification objects. After getting information on classification objects,
             user can also choose to modify or delete those using operation updateClassificationObjects() or deleteClassificationObjects()


Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param WsoIds: 
                         List of identifiers for classified workspace objects(WSO), for which the associated
                         classification objects(ICO) are required.
             
        :return: 
        """
        ...
    def CreateOrUpdateKeyLOVs(self, KeyLOVsInput: list[Teamcenter.Services.Strong.Classification._2009_10.Classification.KeyLOVDefinition2]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation creates or updates  the key-LOV objects based on the input such as
             name, id etc., if the input ID matches that of an existing key-LOV, it will be updated.
             Else new key-LOV object will be created. A key-LOV is a list of values used in classification.
             The key-LOVs are used to define one or more values that can be set for classification
             dictionary attributes
             

             Typical format of a Key-LOV



                 <key-LOV ID>:<key-LOV Name>
             
                 <Key10>:<Value10>
             
                 <Key20>:<Value20>
             

             Example of a Key-LOV:



             -33381 : Design Categories
             
                 Des1 : Bearing
             
                 Des2 : Bracket
             
                 Des3 : Frame
             
                 Des4 : LeadBox
             


Use Cases:

             User wants to create new key-LOVs to be used with classification or need to update
             the existing ones in classification.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param KeyLOVsInput: 
                         List of structure that contains information of the key-LOV that needs to be updated
                         or created.
             
        :return: list of partial errors.
        """
        ...
    def GetAttributesForClasses2(self, ClassIds: list[str]) -> Teamcenter.Services.Strong.Classification._2009_10.Classification.GetAttributesForClassesResponse2:
        """    
             Provides information on class attributes for the classification classes based on
             input classification class ids. Detailed information about class attributes is provided
             & includes class attribute name, description, format, unit system, minimum/maximum
             value, configuration set & extended properties.
             

Use Cases:

             When user wants to view details of all class attributes associated with a classification
             class. The method is similar to getAttributesForClasses()
             method, but provides information in a slightly different format. Also additional
             information like that on the extended properties of class attributes is provided
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClassIds: 
                         Identifier for the classification class whose attribute information is requested.
             
        :return: 
        """
        ...
    def GetKeyLOVs2(self, KeyLOVIds: list[str]) -> Teamcenter.Services.Strong.Classification._2009_10.Classification.GetKeyLOVsResponse2:
        """    
             Gets the information for classification key-LOVs  based on given ID(s). Information
             such as key-LOV's name, display options, owning site, shared sites, deprecation status
             and key and value entries can be obtained. A key-LOV is a list of values used in
             classification. The key-LOVs are used to define one or more values that can be set
             for classification dictionary attributes
             

             Typical format of a Key-LOV -
             

                 <key-LOV ID>:<key-LOV Name>
             
                 <Key10>:<Value10>
             
                 <Key20>:<Value20>
             

             Example of a KeyLOV:
             

             - 33381:Design Categories
             
                 Des1:Bearing
             
                 Des2:Bracket
             
                 Des3:Frame
             
                 Des4:LeadBox
             

Use Cases:

             User wants to retrieve the information for an existing key-LOV using the key-LOV's
             unique identifier. This operation is similar to getKeyLOVs()operation, but provides more detailed information
             about the required key-LOV.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param KeyLOVIds: 
                         List of IDs of classification key-LOV, for which information is required. The key-LOV
                         ID is a unique negative integer that identifies a key-LOV. In the Teamcenter rich
                         client, key-LOVs can be accessed in the "Key LOVs" tab of the Classification Administration
                         application. The key-LOV ID can be found in the "Key/ID" field of a key-LOV definition
                         there.
             
        :return: 
        """
        ...
    def AutoComputeAttributes(self, IcoId: str, Wso: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject, ClassId: str, ViewId: str, InputAttrs: System.Collections.Hashtable, UnitSystem: int, Mode: int) -> Teamcenter.Services.Strong.Classification._2009_10.Classification.AutoComputeAttributesResponse:
        """    
             Computes the attribute values  of classification object based on other attribute
             values within the same object or an associated classification view. Or the value
             can be computed based on attribute values of the object being classified. A classification
             object is also called ICO.
             

Use Cases:

             User need to automatically compute classification attribute values for attributes
             marked as 'AutoComputed'. The values can be computed based on - other attribute values
             belonging to same classification object or an associated classification view or attribute
             values of the object being classified.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param IcoId: 
                         Unique ID of classification objects (ICOs) whose attributes are being computed.
             
        :param Wso: 
                         The workspace object  that is being classified. This input is optional and a NULL
                         value can be specified. A NULL value indicates that there is no workspace object
                         associated with classification object corresponding to input icoId
             
        :param ClassId: 
                         Unique Id of classification class, in which classification object(ICO) is created/workspace
                         object is classified.
             
        :param ViewId: 
                         Unique ID of a classification view that is associated to a classification class,
                         under which input ICO is created/input workspace object is classified.
             
        :param InputAttrs: 
                         Input attributes map with values and properties along with a flag indicating whether
                         the attribute value has changed.
             
        :param UnitSystem: 
<ul>
<li type="disc">0 = Metric
                         </li>
<li type="disc">1 = Nonmetric
                         </li>
</ul>

        :param Mode: 
                         If the mode is specified as load mode, then attribute properties (mandatory, read-only,
                         unique, propogated or hidden) are computed. Else both the attribute properties &amp;
                         values are computed
             
        :return: 
        """
        ...
    def DeleteChildrenInHierarchy(self, OptionsInput: list[Teamcenter.Services.Strong.Classification._2011_06.Classification.HierarchyInfoAndOptions]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Deletes classification class hierarchy based on the classification class identifier.
             All the child classes can be recursively deleted along with any classification views
             associated with those classification classes. If needed, the classification objects
             associated with classification classes & any workspace objects associated with
             the classification objects can also be deleted
             

Use Cases:

             User wants to delete a classification class hierarchy, or a part of it. User may
             also need to delete the associated data for these classes such as classification
             views, classification objects or workspace objects
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param OptionsInput: 
                         List of structure <font face="courier" height="10"><b>HierarchyInfoAndOptions</b></font>
                         that specifies the identifiers for classification classes whose class hierarchy needs
                         to be deleted. It also includes information on the objects that needs to be deleted
                         along with the classes &amp; also the options for deleting children
             
        :return: list of partial errors.
        """
        ...
    def GetLibraryHierarchy(self, LibraryValues: list[str]) -> Teamcenter.Services.Strong.Classification._2011_06.Classification.GetLibraryHierarchyResponse:
        """    
             Gets the classification class details such as class ID, parent information, child
             count etc. for the specified library values criteria
             

Use Cases:

             The operation is called when the user queries to get class hierarchy information
             using the given library values.  The operation is typically used for data dictionary
             related functionality in classification area, and the library components are created
             using this feature in Teamcenter. Data dictionary is a central organizational repository
             for reusable components.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param LibraryValues: 
                         The library value is passed as an input to the operation and is used as a search
                         criteria to get library hierarchy information
             
        :return: 
        """
        ...
    def GetClassificationObjectInfo(self, IcoUids: list[str], AttributeIds: list[int], GetOptimizedValues: bool, FetchDescriptor: bool, Locale: str) -> Teamcenter.Services.Strong.Classification._2011_12.Classification.ClassificationInfoResponse:
        """    
             Provides detailed information on classification objects based on their unique identifiers
             (UID). A classification object is also called an ICO
             

Use Cases:

             When user needs to get details of a classification object (ICO).  These details include
             the classification class to which ICO belongs, the unit system, ICO ID, various ICO
             attributes and their values and property descriptor for these attributes
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param IcoUids: 
                         Unique IDs of classification objects whose details are required
             
        :param AttributeIds: 
                         Unique Identifiers of classification attribute associated with input classification
                         object,  whose values are to be fetched
             
        :param GetOptimizedValues: 
                         Boolean flag to get optimized classification attribute values. When Teamcenter optimizes
                         an attribute value, it provides the most readable value with the least number of
                         leading or trailing zeros. For example, 1 km is easier to read than 1000 m
             
        :param FetchDescriptor: 
                         Boolean flag to indicate whether  property descriptor for each of class attributes
                         is to be fetched
             
        :param Locale: 
                         Locale in which classification objects attribute  values and properties descriptor
                         are to be fetched.
             
        :return: 
        """
        ...
    def GetKeyLOVsForDependentAttributes(self, DependencyAttributeStruct: list[Teamcenter.Services.Strong.Classification._2015_03.Classification.DependencyAttributeStruct]) -> Teamcenter.Services.Strong.Classification._2015_03.Classification.GetDependencyKeyLOVsResponse:
        """    
             This operation returns the Classification KeyLOV (stxt) definitions based
             on the dependency settings on class or view attributes.
             

Use Cases:

             If a user changes the value for any attribute in a dependency chain while working
             in a class containing interdependent KeyLOV (stxt) attributes, the other dependent
             attributes should get configured KeyLOV structures and potential auto populated value.
             

             This operation is used to get the value and the KeyLOV definition for the dependent
             KeyLOV attributes.
             
             Consider a class containing two interdependent KeyLOV attributes
             
             Country
             
                 United States
             
                 Canada
             
             State
             
                 Ohio
             
                 California
             
                 Ontario
             
                 Quebec
             

If a user first selects the value for Country attribute say "United
             States" the State attribute will only show states belonging "United States".
             
If a user first selects the value for State attribute say "Ohio";
             value for Country attribute will be auto populated to "United States". Now, if a
             user deselects the value for Country attribute; the value for State attribute gets
             deselected as well.
             



Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param DependencyAttributeStruct: 
                         List of structure containing class ID, the changed attribute ID, its value and all
                         other UI attribute IDs and corresponding values.
             
        :return: 
        """
        ...
    def GetClassDefinitions(self, ClassIDs: list[str]) -> Teamcenter.Services.Strong.Classification._2015_10.Classification.GetClassDefinitionsResponse:
        """    
             This operation returns Classification class definition, its attribute definitions
             including the details of associated Classification KeyLOV (Stxt) objects.
             

Use Cases:

             User wants to get details of classification class along with all associated class
             attributes. This operation is combination of getClassDescriptions and getAttributesForClasses2,
             but provides information in a different format to cater additional information like
             extended properties, attribute dependency and KeyLOVs (Stxt)  associated to
             class attributes.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClassIDs: 
                         A list of Classification class IDs.
             
        :return: 
        """
        ...
    def ConvertValues(self, ValueConversionInputs: list[Teamcenter.Services.Strong.Classification._2016_03.Classification.ValueConversionInput]) -> Teamcenter.Services.Strong.Classification._2016_03.Classification.ConvertValuesResponse:
        """    
             This operation converts the input value using provided input and output unit.
             

             The conversion happens only when the output format represents a numerical format.
             For String and KeyLOV(Stxt) formats, no conversion will occur, and the input
             string will be returned as is.
             

Use Cases:

             When creating classification classes, you can define whether a class contains only
             metric ICOs, only nonmetric ICOs, or both. If the classification administrator specifies
             that a class can contain both, you can search for an object using either of the unit
             systems you define, and the search mechanism finds a match, regardless of the unit
             in which the object is stored. For example, if you search for a bolt with a width
             of 5/8th inches, the classification search mechanism finds a bolt that is stored
             with a width of 1.6 centimeters. This operation supplies this conversion mechanism.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ValueConversionInputs: 
                         The values to be converted.
             
        :return: 
        """
        ...
    def GetChildrenExtended(self, ClassObjects: list[Teamcenter.Soa.Client.Model.ModelObject], FilterForWriteAccess: bool, Options: int) -> Teamcenter.Services.Strong.Classification._2016_03.Classification.GetChildrenExtendedResponse:
        """    
             Gets the detailed information about immediate children in the classification hierarchy
             for given group(s) or class(es). It also contains all detailed information about
             the parent classes within the hierarchy.
             

             In comparison to getChildren it contains
             extended information about the class itself and also extended information about its
             parent classes.
             

Use Cases:

             User wants to get the details of the class "Tools and Components" and all the classes
             under it, to render the entire hierarchy.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClassObjects: 
                         The class objects for which the children should be retrieved.
             
        :param FilterForWriteAccess: 
                         If true, the classes which are not available for the classify action (that is, to
                         which the user does not have write access) are not returned.
             
        :param Options: 
<ul>
<li type="disc">1 &lt;&lt; 0 - return parent information as part of the ExtendedClassDef
                         </li>
<li type="disc">1 &lt;&lt; 1 - return the child count as part of the ExtendedClassDef
                         </li>
<li type="disc">1 &lt;&lt; 2 - return the instances count as part of the ExtendedClassDef
                         </li>
<li type="disc">1 &lt;&lt; 3 - return the icon documents as part of the BaseClassDef
                         </li>
<li type="disc">1 &lt;&lt; 4 - return the class image documents as part of the ExtendedClassDef
                         </li>
</ul>

        :return: 
        """
        ...
    def SearchClassesExtended(self, SearchCriterias: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.SearchAttribute], SortAttributes: list[int], FilterForWriteAccess: bool, Options: int) -> Teamcenter.Services.Strong.Classification._2016_03.Classification.SearchClassesExtendedResponse:
        """    
             Finds the classification classes based on provided search criteria and provides detailed
             information about those classes. The user can search using a search expression on
             attributes of the class (class ID, name, used attribute etc.). For example, the user
             shall be able to search all the classes whose name begins with a particular set of
             characters and where the class ID matches certain pattern. The order of search results
             can also be sorted on various criteria.
             

             In comparison to searchForClasses it contains
             extended information about the class itself and also extended information about its
             parent classes.
             

Use Cases:

             The user needs to search for classification classes using a search criterion based
             on various attributes of a class. The search criterion can be based on one or more
             attributes.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param SearchCriterias: 
<ul>
<li type="disc">class ID search "-600 = 123"
                         </li>
<li type="disc">class name search "-607 = abc"
                         </li>
<li type="disc">class short name search "-608 = abc"
                         </li>
<li type="disc">class user data 1 "-612 = abc"
                         </li>
<li type="disc">class user data 2 "-613 = abc"
                         </li>
<li type="disc">for all classes using a specific attribute "8 = attribute ID"
                         </li>
<li type="disc">for all classes using a specific attribute "3 = attribute name"
                         </li>
</ul>

        :param SortAttributes: 
<ul>
<li type="disc">class ID = -600
                         </li>
<li type="disc">class name = -607
                         </li>
<li type="disc">class short name = -608
                         </li>
<li type="disc">class user data 1 = -612
                         </li>
<li type="disc">class user data 2 = -613
                         </li>
</ul>

        :param FilterForWriteAccess: 
                         If true, the classes which are not available for the classify action (that is, to
                         which the user does not have write access) are not returned.
             
        :param Options: 
<ul>
<li type="disc">1 &lt;&lt; 0 - return parent information as part of the <font face="courier" height="10">ExtendedClassDef</font>
</li>
<li type="disc">1 &lt;&lt; 1 - return the child count as part of the <font face="courier" height="10">ExtendedClassDef</font>
</li>
<li type="disc">1 &lt;&lt; 2 - return the instances count as part of the <font face="courier" height="10">ExtendedClassDef</font>
</li>
<li type="disc">1 &lt;&lt; 3 - return the icon documents as part of the <font face="courier" height="10">BaseClassDef</font>
</li>
<li type="disc">1 &lt;&lt; 4 - return the class image documents as part of the <font face="courier" height="10">ExtendedClassDef</font>
</li>
</ul>

        :return: 
        """
        ...
    def FindValues(self, FindValueInputs: list[Teamcenter.Services.Strong.Classification._2016_09.Classification.FindValueInput]) -> Teamcenter.Services.Strong.Classification._2016_09.Classification.FindValuesResponse:
        """    
             This operation returns all values available for an attribute in the context of where
             it is called.
             
             For example, it returns all the values of a particular attribute in a given class
             or in the entire database.  Some examples are:
             

Find all the available length values in the Sheet Metal Screw class.
             It will return responses such as 5mm, 6mm, 7.5 mm, etc.
             
Find all the values for the Supplier attribute. It will return all
             values in all classes providing a list of all used suppliers stored in the classification.
             



             The operation can take other attribute values into consideration to narrow the results,
             for example:
             

Find all the available length values in the Sheet Metal Screw class
             where the diameter is 4mm. It will return responses such as 5mm, 6mm, etc.
             



Use Cases:

             Teamcenter Classification displays the List of Values dialog box containing a list
             of attribute values stored for the input attribute, their count and unit system in
             which those values are stored. This operation helps user to search for such stored
             values for multiple input attributes.
             
             The search can be constrained by setting other attribute values, the operations returns
             only the attribute values that are valid given the current search criteria (helping
             the user to efficiently narrow down the search and choose valid values that will
             find classified objects).
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param FindValueInputs: 
                         The input to find the values for.
             
        :return: 
        """
        ...

