import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class SaveAsInput:
    """
    Input properties for new revision
    """
    def __init__(self, ) -> None: ...
    BoName: str
    """Business object name"""
    StringProps: System.Collections.Hashtable
    """Map containing string property value pairs<string,string>"""
    StringArrayProps: System.Collections.Hashtable
    """Map containing string array property name value pairs<string,vector<string>>"""
    DoubleProps: System.Collections.Hashtable
    """Map containing double property name value pairs<string,vector<float>>"""
    DoubleArrayProps: System.Collections.Hashtable
    """Map containing double array property name value pairs<string,vector<double>>"""
    FloatProps: System.Collections.Hashtable
    """Map containing float property name value pairs<string,float>"""
    FloatArrayProps: System.Collections.Hashtable
    """Map containing float array property name value pairs<string,vector<float>>"""
    IntProps: System.Collections.Hashtable
    """Map containing int property name value pairs<string,int>"""
    IntArrayProps: System.Collections.Hashtable
    """Map containing int array property name value pairs<string,vector<int>>"""
    BoolProps: System.Collections.Hashtable
    """Map containing bool property name value pairs<string,bool>"""
    BoolArrayProps: System.Collections.Hashtable
    """Map containing bool array property name value pairs<string,vector<bool>>"""
    DateProps: System.Collections.Hashtable
    """Map containing date property name value pairs<string,DateTime>"""
    DateArrayProps: System.Collections.Hashtable
    """Map containing date array property name value pairs<string,vector<DateTime>>"""
    TagProps: System.Collections.Hashtable
    """Map containing tag business object property name value pairs<string,BusinessObject>"""
    TagArrayProps: System.Collections.Hashtable
    """Map containing tag array property name value pairs<string,vector<BusinessObject>>"""

class DeepCopyData:
    """
    
DeepCopyData describes information regarding
            related objects to be copied or referenced during a revise operation.This structure
            is the same as that used for save as operations.
            
    """
    def __init__(self, ) -> None: ...
    AttachedObject: Teamcenter.Soa.Client.Model.ModelObject
    """Other side object"""
    PropertyName: str
    """Name of relation type or reference property for which DeepCopy rule is configured"""
    PropertyType: str
    """
            Indicates if property represents a reference or a relation; valid values are:
            

Relation

Reference


"""
    CopyAction: str
    """
            The type of deep copy action to be performed; These are the valid values:
            

NoCopy

copyAsReference

CopyAsObject


"""
    IsTargetPrimary: bool
    """Flag indicating if target object is primary or secondary"""
    IsRequired: bool
    """If this flag is false, the copy action can be changed by the user."""
    SaveAsInput: SaveAsInput
    """Captures user inputs for copied properties on revised and deep copied objects"""
    ChildDeepCopyData: list[DeepCopyData]
    """
            Vector of DeepCopyData for secondary objects on the other side of the reference
            or relation.
            """
    CopyRelations: bool
    """
            Flag to specify whether or not  relation properties should be copied during a deep
            copy.
            """

class DeleteModelContentResponse:
    """
    
            The response (DeleteModelContentResponse)
            contains list of any input objects that could not be deleted.The service data contains
            any errors and list of objects deleted by the operation.
            
    """
    def __init__(self, ) -> None: ...
    UndeletedObjects: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """list of input objects that could not be deleted by the system"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains error information and a list of deleted objects."""

class PropDesc:
    """
    
PropDesc describes information about a Teamcenter
            property.
            
    """
    def __init__(self, ) -> None: ...
    PropName: str
    """Name of property"""
    DisplayName: str
    """Display Name of property"""
    DefaultValue: str
    """Default value of property"""
    PropValueType: int
    """Value type for property"""
    PropType: int
    """Type for the property"""
    IsDisplayable: bool
    """Specifies if property is displayable."""
    IsArray: bool
    """Specifies whether the property is an array or single value"""
    MaxNumElems: int
    """Specifies the max number of elements in the array"""
    Lov: Teamcenter.Soa.Client.Model.Strong.ListOfValues
    """List of values (LOV) object attached to property (if any)"""
    IsRequired: bool
    """Specifies if property is required"""
    IsEnabled: bool
    """Specifies if property is enabled"""
    IsModifiable: bool
    """Specifies if property is modifiable"""
    AttachedSpecifier: int
    """LOV attach specifier"""
    MaxLength: int
    """Specifies maximum length of property(e.g. max string length)"""
    InterdependentProps: list[str]
    """List of other property names which are interdependent with the property."""
    NamingPatterns: list[str]
    """Naming patterns for property, can be null"""

class PropDescSaveAs:
    """
    
PropDescSaveAs property descriptor for save
            as and revise operations
            
    """
    def __init__(self, ) -> None: ...
    Parent: PropDesc
    """Core Property Descriptor Structure"""
    CopyFromOriginal: bool
    """
            Flag indicating if value is to be copied from original object for SaveAs[true indicates
            value is to be copied from original object]
            """

class SaveAsDesc:
    """
    
saveAsDesc is a descriptor for inputs into
            save as and revise operations.It is a container of metadata which clients can use
            to generically construct SaveAs dialogs for business objects
            
    """
    def __init__(self, ) -> None: ...
    BusinessObjectName: str
    """Business Object that owns the descriptor"""
    PropDescs: list[PropDescSaveAs]
    """Property Descriptors for SaveAs"""

class SaveAsDescResponse:
    """
    
SaveAsDescResponse is used to return data
            from the getReviseDesc operation.  It contains
            descriptors and deep copy information needed to perform the reviseObjects operation.
            
    """
    def __init__(self, ) -> None: ...
    SaveAsDescMap: System.Collections.Hashtable
    """
            Map of business object type name to its save as descriptor (SaveAsDesc).
            """
    DeepCopyInfoMap: System.Collections.Hashtable
    """Map of input object to a list of its DeepCopyInfo."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data containing created objects, errors, etc."""

class SaveAsIn:
    """
    
            Input structure for revise operation.  Contains a reference to an object to be revised
            (targetObject), its save as input and its
            deep copy data.
            
            Note:revise uses same input descriptor as save as operation
            

targetObjectÂ Â Â Â Â Â Â Â 
            An object to be revised  must be a subtype of
            


            Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â 
             Mdl0ConditionalElement.
            

saveAsInputÂ Â Â Â Â Â Â Â 
            User/application input property values for the revise operation.
            
deepCopyDatasÂ Â Â Â 
            Deep copy information regarding other objects referenced  by or related
            


            Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â 
            to the revised object.
            
    """
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """An object to be revised must be a subtype of Mdl0ConditionalElement"""
    SaveAsInput: SaveAsInput
    """User/application input property values for the revise operation."""
    DeepCopyDatas: list[DeepCopyData]
    """
            Deepcopy information regarding other objects referenced by or related to the revised
            object.
            """

class SaveAsObjectsResponse:
    """
    
            Response from reviseObjects operation. Returns
            a list of the input object and its new revision.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[SaveAsOut]
    """List that holds original input object and new objects."""
    SaveAsTrees: list[SaveAsTree]
    """List that holds mapping between original objects and copied objects"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data containing created objects and error"""

class SaveAsOut:
    """
    
            Output data from reviseObjects operation.
            Contains an input object and the set of new objects created when it was revised.
            
    """
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """The original object that was revised"""
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of all new objects created in conjunction with revising targetObject
"""

class SaveAsTree:
    """
    
SaveAsTree is used to capture the result
            tree of the deep copy process carried out as part of a reviseObjects
            operation. It contains a reference to an original object, a reference to the new
            object that resulted from copying the original object and recursive child results
            from copying objects reached by traversing relations and references recursively from
            the original object.
            
    """
    def __init__(self, ) -> None: ...
    OriginalObject: Teamcenter.Soa.Client.Model.ModelObject
    """Original object being saved as"""
    ObjectCopy: Teamcenter.Soa.Client.Model.ModelObject
    """Object copy after save as"""
    ChildSaveAsNodes: list[SaveAsTree]
    """Nested Information for next level"""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def DeleteModelContent(self, ObjectsToDelete: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]) -> DeleteModelContentResponse:
        """    
             Deletes Mdl0ModelElement objects from an Mdl0ApplicationModel.This
             operation will attempt to delete as many objects as it can and returns a list of
             any objects that could not be deleted.Order of objects in the input list is not important.This
             operation handles the case when one input object has a non circular reference to
             another input object; deletion of the referenced object will occur after its referencing
             object is deleted.
             

Use Cases:

             This API supports model element authoring use cases, specifically the bulk deletion
             of objects within a model.
             
             the following steps can be used for deleting model elements from a model.
             

Find through query or navigate the model elements to be deleted.
             
Call the delete operation deleteModelContent
             to delete a list of existing model elements from a model.
             


             Note:  deleteObjects operation can also be
             used, but requires proper ordering of input   elements to handle the case when one
             model element in the input list references another model element in the input list.
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param ObjectsToDelete: 
                         The input list of model elements to be deleted.
             
        :return: 
        """
        ...
    def GetReviseDesc(self, TargetObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> SaveAsDescResponse:
        """    
             Gets a save as descriptor for a revise operation.Clients may use the output of this
             call to construct generic UI dialogs to collect user input for the revise operation.This
             operation takes in a list of objects to be revised, and returns save as descriptors
             and deep copy for each object input.
             

Use Cases:

             See the reviseObjects operation documentation
             for applicable use cases.
             

Dependencies:

             getReviseDesc, reviseObjects
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param TargetObjects: 
                         Input list of objects to be revised. It must be a subtype of <b>Mdl0ConditionalElement</b>

        :return: The response contains a map of business object types to their save as descriptor
             (used for revise operations as well), and a map of the deep copy data for each of
             input objects.
        """
        ...
    def ReviseObjects(self, SaveAsIn: list[SaveAsIn]) -> SaveAsObjectsResponse:
        """    
             Revises a set of input objects and performs a deep copy of related objects.New objects
             are saved in the Teamcenter database and returned in the response.
             

Use Cases:

             This API supports the authoring use case where an object or a set of objects requires
             a new revision. Objects which are a subtype of Mdl0ConditionalElement support
             the concept of revise.   The elements are first created by a user, undergo edits,
             and then are approved through a workflow and given status. At this point, a new revision
             of the object must be created to further modify it.
             
             The reviseObjects  operation is used to create
             the new revision.  Deep copy rules, defined in BMIDE and deployed to Teamcenter,
             control the sub object copy process during the revise operation.  The operation getReviseDesc is called prior to calling reviseObjects to construct the deep copy information
             and descriptors for the objects to be revised.
             
             Use Case : Revise a conditional element  

             The following assumes an initial revision has been created and released.
             

Construct list of existing, released objects to be revised (objects
             must be valid subtypes of Mdl0ConditionalElement).
             
Construct deep copy data and get saveAs descriptors for the input
             set of objects by using operation getReviseDesc.
             
Revise the objects in Teamcenter by using the reviseObjects operation.
             
Post process / display new object revisions in client
             



Dependencies:

             getReviseDesc
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param SaveAsIn: 
                         List of input data  containing object to be revised and its deep copy data.
             
        :return: A list of objects that were created and saved during the revise operation. Any failure
             will be returned with Business object mapped to error message in the ServiceData
             list of partial errors.
        """
        ...

