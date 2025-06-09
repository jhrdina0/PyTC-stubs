import System
import System.Collections
import Teamcenter.Services.Strong.Core._2008_06.DataManagement
import Teamcenter.Services.Strong.Core._2011_06.DataManagement
import Teamcenter.Services.Strong.Core._2012_09.DataManagement
import Teamcenter.Services.Strong.Core._2013_05.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ChildrenInputData:
    """
    
            This is the input structure which will be used by the AddChildren and RemoveChildren
            service operations.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            An unique string supplied by the caller. This Id is used by the response to identify
            the failed add/remove children.
            
"""
    ParentObj: Teamcenter.Soa.Client.Model.ModelObject
    """A parent object to which the child objects would be added or removed."""
    ChildrenObj: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of objects which are added or removed as children to parent object."""
    PropertyName: str
    """
            The name of  the property that relates  the child objects to the parent.
            
            The property can be a relation property or reference property or empty.
            
"""

class DeepCopyData:
    """
    
            DeepCopyData stores the deep copy information that will be copied via saveAs or revise
            operation. It also stores the nested deep copy data at the next level.
            
    """
    def __init__(self, ) -> None: ...
    AttachedObject: Teamcenter.Soa.Client.Model.ModelObject
    """The related object to be deep copied."""
    PropertyValuesMap: System.Collections.Hashtable
    """
            Map of DeepCopyData ( string, list of strings ). It can contain the following attributes:
            


isRequired If true, the copy action can not be modified. If false,
            the copy action can be changed different action by the user.
            
propertyName Name of relation type or reference property for which
            DeepCopy rule is configured.
            
copyAction DeepCopy action Supported values are as following: NoCopy,
            CopyAsReference, CopyAsObject or Select.
            
isTargetPrimary If true the target object is processed as primary,
            otherwise it is processed as a secondary object.
            
copy_relations If true, the custom properties on the source relation
            object are copied over to the newly-created relation. If false, custom properties
            are not copied.
            
secondaryIsDuplicated if true, the attached object already appears
            in deep copy data
            
propertyType If Relation, it represents Relation type property. If
            Reference, it represents Reference property.
            

"""
    OperationInputTypeName: str
    """Object type name of the operation being perfomed"""
    ChildDeepCopyData: list[DeepCopyData]
    """
            List of DeepCopyData for the objects of the relation or reference property objects
            of the attached object.
            """
    OperationInputs: System.Collections.Hashtable
    """
            Map to provide input property names and values of attached object. These property
            values will be applied on copied object. Map of property name(key) and property values(values)
            (string, list of strings) in string format of attached object, to be set on copied
            object of attached object. The calling client is responsible for converting the different
            property types (int, float, date .etc) to a string using the appropriate toXXXString
            functions in the SOA client framework Property class.
            """

class DeepCopyDataInput:
    """
    Input structure for getDeepCopyData operation
    """
    def __init__(self, ) -> None: ...
    Operation: str
    """This is the operation types such as SaveAs,Revise, etc."""
    BusinessObject: Teamcenter.Soa.Client.Model.ModelObject
    """object reference to get the deepcopydata"""

class GenerateIdInput:
    """
    

createInputÂ Â Â Â Holds property-value information
            for creating objects.
            
propertyNameÂ Â Â Â Name of the Business Object's
            Property for which the ID is generated.
            
quantityÂ Â Â Â Number of IDs to be generated.
            


    """
    def __init__(self, ) -> None: ...
    CreateInput: Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateInput
    """Holds property-value information for Item and its subtypes."""
    PropertyName: str
    """Name of the Business Object's Property for which the ID is generated."""
    Quantity: int
    """Number of IDs to be generated."""

class GenerateIdResponseStruct:
    """
    Structure for holding GenerateIdResponse for each CreateIdInput.
    """
    def __init__(self, ) -> None: ...
    GeneratedIDs: list[str]
    """List of generated IDs."""

class GenerateIdsResponse:
    """
    

generateIdsOutput : Multiple lists of Generated IDs. Each list corresponds
            to the individual elements in GenerateIdInputs
            
serviceData : Holds error stacks
            


    """
    def __init__(self, ) -> None: ...
    GenerateIdsOutput: list[GenerateIdResponseStruct]
    """
            Multiple lists of Generated IDs. Each list corresponds to the individual elements
            in GenerateIdInputs.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Holds error stacks."""

class GetDeepCopyDataResponse:
    """
    
            Structure that contains the DeepCopyData embedded within which is a recursive data
            structure. The DeepCopyData contains information about how the secondary objects
            (related and referenced objects) are to be copied (reference, copy as object, no
            copy).
            
    """
    def __init__(self, ) -> None: ...
    DeepCopyInfoMap: System.Collections.Hashtable
    """
            A map of business objects and DeepCopyData (POM_object/DeepCopyData). Each business
            object from the method input will have a DeepCopyData in the map. The DeepCopyData
            object contains all the information about how the attached objects are to be copied
            (Copy as Object, Copy as Reference, NoCopy, etc.). DeepCopyData is a recursive data
            structure that contains the details for the attached objects at the next level.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data containing errors, etc. The plain object list of the Service data is
            populated with the target objects which are to be copied as part of the SaveAs/revise
            operation. If there is an error retrieving Business Object for the business object
            name corresponding to the target object, it is added to the error stack of the ServiceData
            as a partial error
            """

class GetPasteRelationsOutput2:
    """
    
            The struct data to be returned. This struct contains a clientId, a list of PasteRelationInfo2
            instances, and a preferred index of relation in the list pasreRelInfo.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique client identifier"""
    PasteRelInfo: list[PasteRelationsInfo2]
    """A list of paste relations info to be returned"""
    IndexOfPreferred: int
    """
            The zero-based index of the preferred paste relation in the list pasreRelInfo.
            

"""

class GetPasteRelationsResponse2:
    """
    Response structure contains a list of GetPasteRelationsOutput2 and ServiceData
    """
    def __init__(self, ) -> None: ...
    Outputs: list[GetPasteRelationsOutput2]
    """A list of paste relation output."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
Service Data including partial errors that
            are mapped to the client id from the input. Created objects are also added to the
            created objects list in the Service Data.
            """

class PasteRelationsInfo2:
    """
    
            This struct contains the internal name and display name of the relation as well as
            a flag indicating whether the relation will enable the children to be shown under
            the parent when expanded.
            
    """
    def __init__(self, ) -> None: ...
    PastRelName: str
    """The internal name of paste relation"""
    PastRelDisplayName: str
    """The displayname of paste relation"""
    IsExpandable: bool
    """
            If true, will enable the children to be shown under the parent when expanded.
            

"""

class SaveAsIn:
    """
    
            This structure holds information about the target object, a map of the property name
            as key and as a value carries a list of the corresponding values for that property
            name and the deep copy data of the objects attached to the target object.
            
    """
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """The target business object."""
    InputPropValues: System.Collections.Hashtable
    """
            A map of property name (as key) and property values (as value) in string format.
            Each value is a list of strings to support both single valued and multi valued properties
            of types. The calling client is responsible for converting the different property
            types (like integer, double, date, etc) to a string using the appropriate to<
            type >String function (e.g. toIntString and toDateString) in the
            client framework's Property class.
            """
    DeepCopyDatas: list[Teamcenter.Services.Strong.Core._2013_05.DataManagement.DeepCopyData]
    """DeepCopyData of the objects attached to the target object."""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddChildren(self, InputData: list[ChildrenInputData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation adds a list of objects as children to a list of parent objects which
             could be related by relation or reference properties. If the property name is not
             supplied as input it will use the default relation property between the parent and
             the children given by <ParentTypeName>_<ChildTypeName>_default_relation.
             
             Please see the Preferences and Environment variables reference in the Rich client
             interface guide for information on configuring these preferences.
             


Use Cases:

Add MSWord object as target attachments to EPMTask object.


             Use AddChildren operation and provide EPMTask as the parentObj, MSWord
             object as the childrenObj and target_attachments as the property name. Also,
             provide clientId value to identify this add operation.
             
             Here, the target_attachments property is a runtime property. The AddChildren
             operation internally will modify two properties attachments and attachment_types
             which are saved in the database.
             


Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param InputData: 

        :return: 
        """
        ...
    def GetPasteRelations2(self, Inputs: list[Teamcenter.Services.Strong.Core._2013_05.DataManagement.GetPasteRelationsInputData]) -> GetPasteRelationsResponse2:
        """    
             This operation returns the paste relation names for the given parent business objects
             and the child business objects name; the expandable relations and the preferred paste
             relation are also indicated.
             



Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param Inputs: 
                         List of parent parent and child buiness objects<b> </b>with clientId
             
        :return: 
        """
        ...
    def RemoveChildren(self, InputData: list[ChildrenInputData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation removes a list of objects as children to a list of parent objects
             which could be related by relation or reference properties. If the property name
             is not supplied as input it will use the default relation property between the parent
             and the children given by ParentTypeName>_ChildTypeName>_default_relation.
             
             Please see the Preferences and Environment variables reference in the Rich client
             interface guide for information on configuring these preferences.
             


Use Cases:

Remove Item object from Folder object with contents property name.


             Use RemoveChildren operation and provide Folder object as the parent object,
             Item object as the children object and contents as the property name. Also,
             provide clientId value to identify this remove children operation. The RemoveChildren
             operation will remove Item object from the Folder parent object.
             

Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param InputData: 

        :return: 
        """
        ...
    def GenerateIdsUsingIDGenerationRules(self, GenerateIdsInputs: list[GenerateIdInput]) -> GenerateIdsResponse:
        """    
             This operation generates object ids using ID Generation Rules associated with the
             business object's property. Currently only Item and its subtypes are supported. Object
             ids are generated using information provided in createInput.
             
             This operation should be called in case of a specific requirement where ID Generation
             is independent of creating Objects. (e.g. in case of some CAD applications where
             ids are created first, used in the system with temporary objects which can be saved
             at the later point of time). In most of the cases 'Teamcenter::Soa::Core::_2008_06::createObjects(const
             std::vector<CreateIn> &input)' handles id Generation and object creation.
             
             This operation should be invoked when an ID Generation Rule is attached to a Business
             Object. To identify whether the ID Generation Rule is attached to the Business Object,
             check if 'fnd0IdGenerator' property points to the compound Create Descriptor of same
             Business Object.
             

             For more information on how to configure ID Generation RUles, refer to the Business
             Modeler IDE Guide.
             


Teamcenter Component:

             Core Naming Rules - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Naming
             Rules and Revision Naming Rules.
             
        :param GenerateIdsInputs: 
<ul>
<li type="disc">A Structure containing input values for the operation
                         </li>
</ul>

        :return: 74033  : No ID Generation Rule is attached to the type Type. Please contact your
             system administrator.
        """
        ...
    def GetDeepCopyData(self, DeepCopyDataInput: list[DeepCopyDataInput]) -> GetDeepCopyDataResponse:
        """    
             This operation returns information required to perform save-as/revise on a POM_object.
             

Use Cases:

             Client constructs the saveas dialog for a business object using this operation. The
             information returned by this operation allows a client to construct the DeepCopy
             panels in save-as wizard for user input. Once the user input is received, client
             can make subsequent invocation to the DataManagement.saveAsObjectsAndRelate operation
             to execute SaveAs on the object.
             

Dependencies:

             saveAsObjectsAndRelate
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param DeepCopyDataInput: 
                         A list ofPOM_objects and operation type.
             
        :return: 
        """
        ...
    def SaveAsObjectsAndRelate(self, IVecSoaSavAsIn: list[SaveAsIn], IVecSoaRelteInfoIn: list[Teamcenter.Services.Strong.Core._2012_09.DataManagement.RelateInfoIn]) -> Teamcenter.Services.Strong.Core._2011_06.DataManagement.SaveAsObjectsResponse:
        """    
             This operation performs SaveAs on the input target business object and its related
             objects as new instances. Related objects are identifed using deep copy rules. Optionally,
             this method relates the new object to the input target object or to a default folder.
             

Use Cases:

Use Case 1:     SaveAs without relate

             Client constructs the "SaveAs" dialog for a business object using SaveAs operation
             descriptor. The information returned by that operation allows client to construct
             the SaveAs dialogs and DeepCopy panels for user input.
             
             Once the user input is received, client makes subsequent invocation to this operation
             to execute SaveAs on the object. The method is invoked with "relate" option as false.
             
             New object is created using values passed in. It is not found under Home / NewStuff
             folder / anyother parent object. The new object stays dangling.
             
Use Case 2:     SaveAs and relate to default folder

             Client invokes SaveAs operation as mentioned in use case 1 with "relate" as true
             but chooses not to specify target object or relation. This operation will choose
             a default folder and choose a default relation to be used. The default folder is
             decided based on the value set for the preference, WsoInsertNoSelectionsPref. When
             the preference value is set as 1 the default folder will be the New Stuff folder
             of the service user. When the preference value is 2 the default folder will be the
             Home folder of the service user.
             
             Newly created object is related to the default folder using default relation. For
             any other value of the preference, the relation will not be created.
             
Use Case 3:     SaveAs and relate to specified target object using specified
             relation

             Client invokes SaveAs operation as mentioned in use case 1. The input parameter carrying
             the relation info has the boolean "relate" flag which is true, a valid target object
             and a property name to which the relation is to be created.
             
             After a successful creation, this operation relates the newly created object to the
             specified target object using specified relation.
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param IVecSoaSavAsIn: 
                         Input data containing target object, map (PropertyValuesMap) of properties and their
                         corresponding values and DeepCopyData of the attached objects.
             
        :param IVecSoaRelteInfoIn: 
                         Input data containing the paste options used to relate the newly created object.
             
        :return: :     The SaveAs operation performed on the object input in the parameter
             carrying the SaveAs info has failed.
        """
        ...
    def PruneNamedReferences(self, NamedReferences: list[Teamcenter.Soa.Client.Model.Strong.POM_object]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation performs a prune operation by a given list of Dataset named references, per the following criteria
             
             1. Remove the input named references from their owning Dataset

             2. Delete the input named reference objects
             
             3. Delete the owning Dataset objects which contain no named references after the prune operation
             
             4. The pruned named references, deleted Datasets
             and updated Datasets will be returned
             


Teamcenter Component:

             Core Model Dataset - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform.  This component defines class
             'Dataset' behavior.
             
        :param NamedReferences: 
                         List of <b>Dataset</b> <font face="courier" height="10">named references</font> to
                         be pruned
             
        :return: 
        """
        ...

