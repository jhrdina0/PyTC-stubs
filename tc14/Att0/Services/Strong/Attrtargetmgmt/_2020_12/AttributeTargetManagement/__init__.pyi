import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttachParamData:
    """
    AttachParamData represents the attached parameter data.
    """
    def __init__(self, ) -> None: ...
    InputParameter: Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute
    """The input parameter to be attached."""
    AttachedParameter: Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute
    """
            The attached parameter. If AttachParamsInput.createCopy is true, it equals to the
            copy of the input parameter. Otherwise, it equals to the input parameter.
            """

class AttachParamsInput:
    """
    
            AttachParamsInput structure represents the parameters to be attached to the input
            parent object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """
            The parent object where to attach parameters. The valid parent object is ItemRevision
            or BOMLine.
            """
    Parameters: list[Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute]
    """
            A list of Att0MeasurableAttribute objects to be attached to the input parent
            object.
            """
    CreateCopy: bool
    """
            If true, create the copy of the input parameter and attach the copied parameter to
            the parent object. If false, attach the input parameter to the parent object directly.
            """
    ParamDirection: str

class AttachParamsOutput:
    """
    AttachParamsOutput represents the attached parameters on a given parent object.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """The parent object where to attach parameters."""
    AttachedParams: list[AttachParamData]
    """A list of attached parameters."""
    IgnoredParams: list[Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute]
    """A list of ignored parameters."""
    ParamDirection: str

class AttachParamsResponse:
    """
    AttachParamsResponse represents the attached parameters.
    """
    def __init__(self, ) -> None: ...
    Outputs: list[AttachParamsOutput]
    """The list of attached parameters."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData object to hold the partial errors that the operation encounters."""

class CreateParamsInput:
    """
    
            CreateParamsInput structure represents the list of parameters to be created on a
            given parent object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    ParamProperties: list[ParameterProperties]
    """A list of properties to create new Att0MeasurableAttribute objects."""
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """The parent object where contains the created Att0MeasurableAttribute objects."""

class CreateParamsOutput:
    """
    CreateParamsOutput represents the created parameters on the given parent object.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the ParameterProperties.clientId. This is used by the caller
            to identify this data structure with the source input data.
            """
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """The parent object that contains the created parameters."""
    CreatedParams: list[ParameterData]
    """The list of created parameters on the parent object."""

class CreateParamsResponse:
    """
    CreateParamsResponse represents created parameters for all the inputs.
    """
    def __init__(self, ) -> None: ...
    Outputs: list[CreateParamsOutput]
    """Represents a list of created parameters on the given parent objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData object to hold the partial errors that the operation encounters."""

class FileProperties:
    """
    
            FileProperties structure represents the properties information needed to create a
            Dataset.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            The input Dataset object, optional. If empty, the system creates a new Dataset
            object; otherwise, replace the file on the given Dataset.
            """
    FileName: str
    """
            Full name with the file extension, for example: goal.txt. The system creates the
            dataset with the name (without the file extension).
            """
    Description: str
    """File description."""
    NamedReference: str
    """File named reference, for example: txt"""
    Type: str
    """Dataset type, for example: Text"""

class GetLatestMeasureValuesResp:
    """
    
            GetLatestMeasureValuesResp structure represents the latest Att0MeasureValue
            for the input parameters.
            
    """
    def __init__(self, ) -> None: ...
    Outputs: list[MeasureValuesOutput]
    """A list of latest Att0MeasureValue for the input parameters."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData object to hold the partial errors that the operation encounters."""

class GetParameterData:
    """
    GetParameterData represents the returned parameter.
    """
    def __init__(self, ) -> None: ...
    Parameter: Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute
    """Att0MeasurableAttribute object."""
    ParamDirection: str
    GoalFiles: list[ParameterFileData]
    """The associated goal files on the parameter."""
    OverrideContext: Teamcenter.Soa.Client.Model.ModelObject
    """
            When the parameter is under the occurrence, it represents the corresponding override
            context. Otherwise it is null.
            """

class ParameterConfigData:
    """
    ParameterConfigData structure represents the configuration data applied to the parameters.
    """
    def __init__(self, ) -> None: ...
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """Applied revision rule, optional."""
    VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule
    """Applied variant rule, optional."""

class GetParamsInput:
    """
    
            GetParamsInput structure represents the input object where to get the associated
            parameters.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """
            The parent object where to get the associated parameters. The valid parent is a WorkspaceObject,
            or BOMLine
"""
    ParamConfig: ParameterConfigData
    """
            The given configuration (i.e. RevisionRule, VariantRule) to filter
            parameters, optional. It is processed when GetParamsPref.appliedConfig is true.
            """

class GetParamsOutput:
    """
    GetParamsOutput represents associated parameters on a given parent object.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """The parent object from where to get the associated parameters."""
    ParamData: list[GetParameterData]
    """Represents the associated parameters on the parent."""

class GetParamsPref:
    """
    GetParamsPref structure represents the preference to get parameters.
    """
    def __init__(self, ) -> None: ...
    Application: str
    """The application that will be used to filter the returned parameters."""
    ParamDirection: str
    GoalFileRequired: bool
    """
            true/false. If true, the system gets the associated Dataset on the returned parameters
            via the relation Att0HasGoalFile.
            """
    AppliedConfig: bool
    """
            If true, the system applies the given configuration (variant rule)  and then returns
            the configured parameters on the BOMLine. If  false, the system gets the configured
            parameters on the BOMLine based on the active variant rule from the current
            BOMWindow.
            """

class GetParamsResponse:
    """
    GetParamsResponse represents associated parameters for all the inputs.
    """
    def __init__(self, ) -> None: ...
    Outputs: list[GetParamsOutput]
    """Represents associated parameters for all the inputs."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData object to hold the partial errors that the operation encounters."""

class MeasureValueData:
    """
    MeasureValueData represents the returned measure value data.
    """
    def __init__(self, ) -> None: ...
    MeasureValue: Teamcenter.Soa.Client.Model.ModelObject
    """Att0MeasureValue object."""
    Method: str
    ValueFiles: list[ParameterFileData]
    """A list of value files on the Att0MeasureValue."""

class MeasureValuesOutput:
    """
    
            MeasureValuesOutput structure represents the latest Att0MeasureValue for the input
            parameter.
            
    """
    def __init__(self, ) -> None: ...
    Parameter: Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute
    """The parameter where to get the latest Att0MeasureValue."""
    MeasureValues: list[MeasureValueData]
    """A list of latest Att0MeasureValue data for the input parameter."""

class ParameterData:
    """
    ParameterData represents the returned parameter data.
    """
    def __init__(self, ) -> None: ...
    Parameter: Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute
    """Att0MeasurableAttribute object."""
    ParamDirection: str
    GoalFiles: list[ParameterFileData]
    """The associated goal files on the parameter."""

class ParameterFileData:
    """
    ParameterFileData represents the associated file to the parameter.
    """
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Dataset object."""
    FileName: str
    """The corresponding ImanFile name."""
    FileTicket: str
    """The corresponding ImanFile ticket."""

class ParameterProperties:
    """
    
            ParameterProperties structure represents the properties information needed to create
            a parameter.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    ParamInput: Teamcenter.Soa.Client.Model.CreateInput
    """The input parameter data for create operation."""
    ParamDirection: str
    GoalFiles: list[FileProperties]
    """A list of properties to create the parameter goal files."""

class UpdateMeasureValueProperties:
    """
    UpdateMeasureValueProperties represents the input measure value to update or create.
    """
    def __init__(self, ) -> None: ...
    ToCreate: bool
    """
            If true, a new measure value is created on the input parameter. Otherwise, update
            the given measure value.
            """
    Method: str
    MeasureValue: Teamcenter.Soa.Client.Model.ModelObject
    """The input measure value to be updated."""
    ValueProps: System.Collections.Hashtable
    ValueFileInputs: list[FileProperties]
    """
            A list of value files to be created or replaced. When the given Dataset is
            null, the system creates a new Dataset for the value file. Otherwise, the
            system replaces the existing value file.
            """

class UpdateParamData:
    """
    
            UpdateParamData represents the updated parameter, as well as the updated Measure
            Values.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the UpdateParamProperties.clientId. This is used by the
            caller to identify this data structure with the source input data.
            """
    InputParameter: Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute
    """The source parameter to be updated."""
    RetParameter: ParameterData
    """The updated or newly created parameter in the override scenario."""
    RetMeasureValues: list[MeasureValueData]
    """A list of updated or created measure values."""

class UpdateParamProperties:
    """
    ParameterProperties structure represents all the information needed to create a parameter.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    Parameter: Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute
    """The input parameter to be updated."""
    ParamDirection: str
    ParamProps: System.Collections.Hashtable
    GoalFileInputs: list[FileProperties]
    ValueInputs: list[UpdateMeasureValueProperties]
    """A list of measure values to be created or updated."""

class UpdateParamsInput:
    """
    
            UpdateParamsInput structure represents a list of parameters to be updated on the
            input parent object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    Parameters: list[UpdateParamProperties]
    """A list of parameters to be updated."""
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """
            The parent that contains the parameters to be updated. The valid parent is a WorkspaceObject,
            or BOMLine.
            """

class UpdateParamsOutput:
    """
    
            UpdateParamOutput represents the updated parameter, as well as the updated Measure
            Values.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the UpdateParamProperties.clientId. This is used by the
            caller to identify this data structure with the source input data.
            """
    UpdatedParams: list[UpdateParamData]
    """A list of updated parameters data."""
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """The parent object that includes the list of parameters."""

class UpdateParamsResponse:
    """
    UpdateParamsResponse represents the updated parameters for all inputs.
    """
    def __init__(self, ) -> None: ...
    Outputs: list[UpdateParamsOutput]
    """A list of updated parameters."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """UpdateParamsResponse represents the updated parameters for all inputs."""

class AttributeTargetManagement:
    """
    Interface AttributeTargetManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AttachParameters(self, Inputs: list[AttachParamsInput]) -> AttachParamsResponse: ...
    def CreateParameters(self, Inputs: list[CreateParamsInput]) -> CreateParamsResponse: ...
    def GetLatestMeasureValues(self, Parameters: list[Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute], Methods: list[str], ValueFileRequired: bool) -> GetLatestMeasureValuesResp: ...
    def GetParameters(self, Inputs: list[GetParamsInput], Pref: GetParamsPref) -> GetParamsResponse: ...
    def UpdateParameters(self, Inputs: list[UpdateParamsInput]) -> UpdateParamsResponse: ...

