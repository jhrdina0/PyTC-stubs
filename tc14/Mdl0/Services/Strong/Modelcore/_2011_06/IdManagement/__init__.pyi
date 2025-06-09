import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class InputData:
    """
    
            A generic structure for holding operation input data for which values will be auto
            assigned
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """Client ID to uniquely identify this data; also used in error reporting."""
    Bo: Teamcenter.Soa.Client.Model.ModelObject
    """
            Business object that will be used as original object for revise and copy operations;
            set to NULLTAG if object is being created.
            """
    BoType: str
    """Business Object name; required when operation input is create, must be empty otherwise."""
    StringProps: System.Collections.Hashtable
    """Map containing string property name value pairs<string,string>"""
    StringArrayProps: System.Collections.Hashtable
    """Map containing string array property name value pairs<string,vector<string>>"""
    DoubleProps: System.Collections.Hashtable
    """Map containing double property name value pairs<string,double>"""
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
    """Map containing tag property name value pairs<string,BusinessObject>"""
    TagArrayProps: System.Collections.Hashtable
    """Map containing tag array property name value pairs<string,vector<BusinessObject>>"""
    CompoundInputData: System.Collections.Hashtable
    """
            A map of compound input data, for operations and object types that support compound
            objects.  Key value is property name, value is a list of InputData
            for the compound objects
            """
    ModifiableAssignedValues: System.Collections.Hashtable
    """
            A map of auto assignable properties that were assigned for the object. The key is
            the property name, and the value is a boolean flag which indicates if the assigned
            value can be further modified by the client application.
            """

class AssignInput:
    """
    Inputs required for auto generating attribute values for a workspace object.
    """
    def __init__(self, ) -> None: ...
    Data: InputData
    """
            Property name value pairs from the objects operation descriptor.  Assignable properties
            having no input value will be assigned a value in the response.
            """
    Operation: str

class AssignResponse:
    """
    
AssignResponse contains the input data with
            auto generated attribute values filled in.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[InputData]
    """The list of input data with key values auto assigned"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains error information"""

class IdManagement:
    """
    Interface IdManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AutoAssignValues(self, Input: list[AssignInput]) -> AssignResponse:
        """    
             Auto generates the values of the auto assignable  properties in bulk. The input parameters
             expected on the input, include the business object or the business object name.
             For cases where the assignment is based on other properties, those values must be
             supplied on input; this includes any reference objects.  The output includes the
             generated values as well as other properties defined in the input.
             

             Support is currently limited to the following Collaborative Product Development (CPD)
             specific classes:
             
    Mdl0ApplicationModel (mdl0model_id)
             
                 Ptn0Partition (ptn0partition_id)
             
                 Cpd0DesignElement (cpd0design_element_id)
             
                 Cpd0DesignFeature (cpd0design_feature_id)
             
                 Cpd0DesignControlElement (cpd0design_control_element_id)
             



Use Cases:

             This API supports the authoring use case for model content.It is used to fill in
             autoassignable property values. Applications may choose to allow a user to enter
             a value or assign one.
             
             Use Case 1: Assign ID during Create 

             During creation of a new object, the user requests the system to assign a value
             

Application constructs AssignInput
             and specifies the business object type (boType) of the object being created and an
             operationType: CreateOperation.  A client
             ID (unique for the call) is also specified on the AssignInput
             for error reporting.
             
Generate new ID values for the object using the autoAssignValues operation.
             
Post process the new ID value (e.g. display it back to the user).
             


             Use Case 2: Assign ID during Revise 

             During revise of an existing object, the user requests the system to assign an ID
             value to the new revision.
             

Application constructs AssignInput and specifies the business object
             (bo) of the object being revised and an operationType: ReviseOperation.
             A client ID (unique for the call) can be optionally specified on the AssignInput.
             
Generate ID value for new revision using the autoAssignValues operation.
             
Post process the ID value (e.g. display it back to the user).
             


             Use Case 3: Assign ID during SaveAs 

             During saveas (copy) of an existing object, the user requests the system to assign
             an ID value to the new object.
             

Application constructs AssignInput
             and specifies the business object (bo) of the object being revised and an operationType:
             SaveAsOperation.A client ID (unique for the
             call) can be optionally specified on the AssignInput.
             
Generate ID value for new revision using the autoAssignValues operation.
             
Post process the ID value (e.g. display it back to the user).
             



Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Input: 
                         A list of <font face="courier" height="10">AssignInput</font> for which property
                         values should be autoassigned.
             
        :return: The the input data with autoassigned values filled in.The errors if any are returned
             in the service data.
        """
        ...

