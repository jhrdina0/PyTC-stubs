import Teamcenter.Services.Strong.Core._2016_05.DataManagement
import typing

class GenerateContextIDsInput2:
    """
    
            This structure is the input sructure for the generateContextSpecificIDs service.
            
            This contains the informanion of context name and number of IDs to be generated for
            that context name.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string supplied by the caller. This ID is used to identify returned GenerateContextIDResponse
            elements and Partial Errors associated with this input GenerateContextIDsInput2.
            """
    ContextName: str
    """
            Name of the context for which IDs to be generated. A context name is a string that
            can be up to 256 characters long. This string should not be empty, in order to generate
            IDs, an error is returned if user tries to generate ID for a empty context name.
            """
    ContextTypeName: str
    """
            The name of the business object for which the property values are to be generated
            and validated. An error 39007 is returned by the operation if the type name is not
            valid.
            """
    ContextPropName: str
    """
            Property name associated with the Context Name. This property name will be used to
            validate ID uniqueness.
            """
    ValidateIDs: bool
    """
            If true, the IDs should be validated for uniquness, otherwise no validation will
            be done. If false, contextType and contextPropName can be NULL.
            """
    NumberOfIDs: int
    """
            The number of IDs to be generated for a given context name. This is a mandatory field
            and should not be 0 or any negative number to generate IDs. An error is returned,
            if user tries to generate ID for a context name with invalid value (0 or negative
            number) for this field.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GenerateContextSpecificIDs2(self, GenerateContextIDsIn: list[GenerateContextIDsInput2]) -> Teamcenter.Services.Strong.Core._2016_05.DataManagement.GenerateContextSpecificIDsResponse:
        """    
             Generates the range of unique IDs for input context names. The number of IDs generated
             for each context name depends on the input. If for a given context name, the ID has
             been reset using Teamcenter service resetContextID, then this service generates IDs
             for that context from the beginning.
             

             ID generation will also reset when the maximum limit is met. This limit is maximum
             number supported on 64 bit machine.
             

             If the validation flag is true and both contextType and contextPropName are provided,
             the generated IDs will be validated for uniquness.
             

Teamcenter Component:

             Core Naming Rules - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Naming
             Rules and Revision Naming Rules.
             
        :param GenerateContextIDsIn: 
                         A list of GenerateContextIDsInput2 which contains the context name, type, property
                         name, validation flag, and number of IDs to be generated for that context. Context
                         name string length is supported up to 256 characters. There is no limit for the number
                         fo IDs that can be generated for a given context name.
             
        :return: 
        """
        ...

