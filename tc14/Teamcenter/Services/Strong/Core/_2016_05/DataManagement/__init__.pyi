import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class GenerateContextIDsInput:
    """
    
            This structure is the input sructure for the generateContextSpecificIDs service.
            
            This contains the informanion of context name and number of IDs to be generated for
            that context name.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string supplied by the caller. This ID is used to identify returned GenerateContextIDResponse
            elements and Partial Errors associated with this input GenerateContextIDsInput.
            """
    ContextName: str
    """
            Name of the context for which IDs to be generated. A context name is a string that
            can be up to 256 characters long. This string should not be empty, in order to generate
            IDs, an error is returned if user tries to generate ID for a empty context name.
            """
    NumberOfIDs: int
    """
            Represents number of IDs to be generated for a given context name. This is a mandatory
            field and should not be 0 or any negative number to generate IDs. An error is returned,
            if user tries to generate ID for a context name with invalid value (0 or negative
            number) for this field.
            """

class GenerateContextSpecificIDsResponse:
    """
    Contains the returned information of generateContextSpecificIDs service.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Partial Errors are returned in the ServiceData when service generateContextSpecificIDs
            fails to generate IDs of any of the context name. Errors are mapped back to input
            context name based on the client ID field provided in structure GenerateContextIDsInput.
            """
    GeneratedContextIDValues: list[GeneratedContextIDs]
    """
            A list of GeneratedContextIDs, which contains each of the context names and IDs generated
            for it by service generateContextSpecificIDs.
            """

class GeneratedContextIDs:
    """
    
            Contains the combination of context name and its generated IDs based on the user
            input.
            
    """
    def __init__(self, ) -> None: ...
    ContextName: str
    """
            Name of the context for which IDs has been generated. This value is provided by the
            user in GenerateContextIDsInput for generating IDs.
            """
    GeneratedIDs: list[str]
    """
            List of generated IDs for a given context name. This contains one or more generated
            IDs for a given context name based on the user input in input structure GenerateContextIDsInput.
            """

class PropData:
    """
    
            This structure holds information about Teamcenter business object, its last saved
            date when exported to client and list of property name/value pair information.
            
    """
    def __init__(self, ) -> None: ...
    BusinessObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The business object for which the properties to be set. All business object types
            are supported.
            """
    VecPropNameVal: list[PropertyNameValuesStruct]
    """List of property name/value pair information."""
    LastSavedDateExportedToClient: System.DateTime
    """Last saved date of the object when object was exported to client."""

class PropertyNameValuesStruct:
    """
    
            This structure contains property name, list of old values for the property and list
            of new values to be set for the property.
            
    """
    def __init__(self, ) -> None: ...
    PropertyName: str
    """Name of the property"""
    OldValues: list[str]
    NewValues: list[str]

class SetPropsAndDetectOverwriteResponse:
    """
    
            Response structure for setPropertiesAndDetectOverwrite operation. It returns the
            information about overwritten objects and the properties/objects which are not saved
            due to conflict.
            
    """
    def __init__(self, ) -> None: ...
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """This is the service data. It contains the updated objects and their properties."""
    OverwriteDetectedObjPropMap: System.Collections.Hashtable
    """
            The  map ( business object / list of string ) contains the objects and properties
            list for which overwrite condition has been detected.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GenerateContextSpecificIDs(self, GenerateContextIDsIn: list[GenerateContextIDsInput]) -> GenerateContextSpecificIDsResponse:
        """    
             Generates the range of unique IDs for input context names. The number of IDs generated
             for each context name depends on the input. If for a given context name, the ID has
             been reset using Teamcenter service resetContextID, then this service generates IDs
             for that context from the beginning.
             
             ID generation will also reset when the maximum limit is met. This limit is maximum
             number supported on 64 bit machine.
             

             WARNING: IDs generated using this service  are unique within a given context name,
             but are not guaranteed to be unique in all Teamcenter contextx. Caution should be
             used if requesting ids for item or other Teamcenter objects that require unique ids.
             The caller may choose to validate uniqueness in the use cases. By default Teamcenter
             will not allow an object be saved if it violates defined uniqueness criteria.
             

Use Cases:

             A user has a context name for which he wants to generate IDs. The user provides the
             context name and the number for IDs to be generated to this Teamcenter service. In
             response the user recives a block of IDs. If the user again uses this service to
             generate additional IDs for the same context name, new IDs are generated and returned
             in the response structure. The IDs generated in two calls of this service for a given
             context name are unique unless the service resetContextID has been called for that
             context between the two calls to generate IDs.
             

Teamcenter Component:

             Core Model Property Layer - A set of capabilities/functionality (data model and behaviours)
             that form the very core of our PLM platform.  This component defines properties.
             
        :param GenerateContextIDsIn: 
                         List of GenerateContextIDsInput which contains the context name and number of IDs
                         to be generated for that context. Context name string length is supported up to 256
                         characters. There is no limit for the number fo IDs that can be generated for a given
                         context name.
             
        :return: 
        """
        ...
    def ResetContextID(self, ContextNames: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service enables the client to reset the ID for given context names. When the
             IDs for a context name are reset, ID generation will begain from beginning value.
             

             WARNING: Be advised that if a client resets the ID for a context name, it is possible
             that repeated IDs will be returned from generateContextSpecificIDs service for that
             context name.
             

Use Cases:

             A client has a context name for which it has generated IDs and now wants to generate
             the IDs for that context name again from the beginning. Client calls this Teamcenter
             service to reset the ID for this context name. The next time the client calls generateContextSpecificIDs
             for this context block of returned IDs starts from the beginning value 0.
             

Teamcenter Component:

             Core Model Property Layer - A set of capabilities/functionality (data model and behaviours)
             that form the very core of our PLM platform.  This component defines properties.
             
        :param ContextNames: 
                         List of the context names for those, IDs to be reset. Empty strings should not be
                         used to reset ID. An error is returned, if the client tries to send empty string
                         as context name.
             
        :return: 
        """
        ...
    def SetPropertiesAndDetectOverwrite(self, PropData: list[PropData], Options: System.Collections.Hashtable) -> SetPropsAndDetectOverwriteResponse: ...

