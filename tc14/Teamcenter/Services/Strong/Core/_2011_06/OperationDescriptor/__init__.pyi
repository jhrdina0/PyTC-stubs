import System
import System.Collections
import Teamcenter.Services.Strong.Core._2008_06.PropDescriptor
import Teamcenter.Soa.Client.Model
import typing

class SaveAsInput:
    """
    
            This structure stores all the property input that are to be set to the object copy
            by the SaveAs operation.
            
    """
    def __init__(self, ) -> None: ...
    BoName: str
    """Business object name"""
    StringProps: System.Collections.Hashtable
    """Map (string, string) containing propName, stringValue> pairs for string properties"""
    StringArrayProps: System.Collections.Hashtable
    """
            Map (string, vector<string>) containing <propName,
            stringList> pairs for string array properties
            """
    DoubleProps: System.Collections.Hashtable
    """
            Map (string, double) containing <propName, doubleValue>
            pairs for double properties
            """
    DoubleArrayProps: System.Collections.Hashtable
    """
            Map (string, vector<double>) containing <propName,
            doubleList> for double array properties
            """
    FloatProps: System.Collections.Hashtable
    """
            Map (string, float) containing <propName, floatValue>
            for float properties
            """
    FloatArrayProps: System.Collections.Hashtable
    """
            Map (string, vector<float>) containing <propName,
            floatList> for float  array properties
            """
    IntProps: System.Collections.Hashtable
    """
            Map (string, int) containing <propName, intValue>
            for int properties
            """
    IntArrayProps: System.Collections.Hashtable
    """
            Map (string, vector<int>) containing <propName,
            intList> for int array properties
            """
    BoolProps: System.Collections.Hashtable
    """
            Map (string, bool) containing <propName, boolValue>
            for bool properties
            """
    BoolArrayProps: System.Collections.Hashtable
    """
            Map (string, vector<bool>) containing <propName,
            boolList> for bool array properties
            """
    DateProps: System.Collections.Hashtable
    """
            Map (string, DateTime) containing <propName,
            dateTimeValue> for date properties
            """
    DateArrayProps: System.Collections.Hashtable
    """
            Map (string, vector<DateTime>) containing <propName,
            dateTimeList> for date  array properties
            """
    TagProps: System.Collections.Hashtable
    """
            Map (string, BusinessObject) containing <propName,
            businessObject> for reference properties
            """
    TagArrayProps: System.Collections.Hashtable
    """
            Map (string, vector<BusinessObject>) containing <propName,
            businessObjectList> for reference array properties
            """

class DeepCopyData:
    """
    
            DeepCopyData stores the deep copy information and OperationInput
            data of the objects that will be copied via saveAs
            or revise operation. It also stores the nested deep copy data at the next level.
            
    """
    def __init__(self, ) -> None: ...
    AttachedObject: Teamcenter.Soa.Client.Model.ModelObject
    """Other side object"""
    PropertyName: str
    """
            Name of relation type or reference property for which DeepCopy
            rule is configured
            """
    PropertyType: str
    """
            Enumeration indicating if DeepCopyRule is
            configured for relation or feference property
            """
    CopyAction: str
    """DeepCopy action [NoCopy, CopyAsReference, CopyAsObject or Select]"""
    IsTargetPrimary: bool
    """Flag indicating if target object is primary or secondary"""
    IsRequired: bool
    """If flag is false, the copy action can be dynamicaly changed by user"""
    CopyRelations: bool
    """
            Flag indicating whether the properties on the relation object itself need to be copied
            or not
            """
    SaveAsInputTypeName: str
    """SaveAsInput type name"""
    ChildDeepCopyData: list[DeepCopyData]
    """
            List of DeepCopy data for the objects on the other side of the relation property
            or reference property
            """
    SaveAsInput: SaveAsInput
    """
            Store the user inputs on the SaveAs dialog.
            NOTE: This field is not used in the getSaveAsDesc
            operation. It is used in the saveAsObjects
            operation
            """

class PropDescSaveAs:
    """
    
            This structure captures a property definition for a SaveAs
            Descriptor.
            
    """
    def __init__(self, ) -> None: ...
    Parent: Teamcenter.Services.Strong.Core._2008_06.PropDescriptor.PropDesc
    """Core property descriptor structure"""
    CopyFromOriginal: bool
    """
            Indicating if the property value is to be copied from original object to the object
            copy -  true indicates the property value is to be copied.
            """

class SaveAsDesc:
    """
    
            This structure captures the list of property description data for SaveAs Descriptor. Clients can use this information to generically
            construct SaveAs dialogs for any business
            object.
            
    """
    def __init__(self, ) -> None: ...
    BusinessObjectName: str
    """Name of business object that owns the descriptor"""
    PropDescs: list[PropDescSaveAs]
    """List of property description data"""

class SaveAsDescResponse:
    """
    
            Structure that contains metadata information about the properties relevant to the
            SaveAs operation i.e, property is mandatory, property is visible, if value is to
            be copied from original object, etc. It also has the DeepCopyData
            embedded within which is a recursive data structure. The DeepCopyData
            contains information about how the secondary objects (related and referenced objects)
            are to be copied (reference, copy as object, no copy).
            
    """
    def __init__(self, ) -> None: ...
    SaveAsDescMap: System.Collections.Hashtable
    """
            A map of business object types and SaveAs Descriptors (string/SaveAsDesc).  This
            is the container of metadata for SaveAs that can be used by clients to generically
            construct SaveAs dialogs for business objects.
            """
    DeepCopyInfoMap: System.Collections.Hashtable
    """
            A map of business objects and DeepCopyData
            (business object/DeepCopyData). Each business
            object from the method input will have a DeepCopyData
            in the map. The DeepCopyData object contains
            all the information about how the attached objects are to be copied (Copy as Object,
            Copy as Reference, NoCopy, etc.).  DeepCopyData
            is a recursive data structure that contains the details for the attached objects
            at the next level.
            
            NOTE: Attached objects can be either referenced objects or related objects.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data containing errors, etc. The plain object list of the Service data is
            populated with the target objects which are to be copied as part of the SaveAs operation.
            If there is an error retrieving Business Object for the business object name corresponding
            to the target object, it is added to the error stack of the ServiceData as a partial error
            """

class OperationDescriptor:
    """
    Interface OperationDescriptor
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetSaveAsDesc(self, TargetObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> SaveAsDescResponse:
        """    
             This operation returns information required to save a business object. The SaveAsDescriptor includes the metadata information
             for the properties required when saving a business object, i.e., the property is
             mandatory, the property is visible, if value is to be copied from original object,
             etc.  The SaveAsDescriptor also includes
             the DeepCopyData which is a recursive data
             structure. The DeepCopyData contains information
             about how the secondary objects (related and referenced objects) are to be copied
             (reference, copy as object, no copy).
             

Use Cases:

Get SaveAsDescriptor for the SaveAs wizard

             Client constructs the SaveAs dialog for a Business Object using this operation. The
             information returned by this operation allows a client to construct the SaveAs dialogs
             and DeepCopy panels for user input. Once the user input is received, client can make
             subsequent invocation to the DataManagement.saveAsObjects
             operation to execute SaveAs on the object.
             

Dependencies:

             saveAsObjects
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param TargetObjects: 
                         Set of objects for which the SaveAs Descriptor is needed.
             
        :return: contains information about how the secondary objects (related and referenced objects)
             are to be copied (reference, copy as object, no copy).
        """
        ...

