import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetStructureParamsInput:
    """
    
            GetStructureParamsInput is the input structure for the operation to fetch the associated
            parameters.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The application that will invoke this operation to fetch all the parameters for the
            given parent.
            """
    ParentBVRs: list[Teamcenter.Soa.Client.Model.Strong.PSBOMViewRevision]
    """
            A list of all the PSBOMViewRevision objects  in the structure for which the parameters
            are to be fetched. parentBVRs, revisions and occThreadChains must have the same lenghts.
            At the same index, PSBOMViewRevision, ItemRevision, Occ Thread Chain from these 3
            vectors belong to the same structure line.
            """
    Revisions: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    """
            A list of ItemRevision objects in the structure for which the parameters are to be
            fetched.
            """
    OccThreadChains: list[str]
    """
            List of Occurrence Thread chain in the structure for which the associated parameters
            are to be fetched.
            """
    VariantRules: list[Teamcenter.Soa.Client.Model.Strong.VariantRule]
    """A list of VariantRule objects  to be applied on the parameters being fetched."""
    RevisionRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """RevisionRule objects to be applied on the parameters being fetched."""
    ConfiguratorContext: Teamcenter.Soa.Client.Model.ModelObject
    """Configurator Context in the input structure."""

class GetStructureParamsPref:
    """
    GetStructureParamsPref structure represents the preference to get parameters.
    """
    def __init__(self, ) -> None: ...
    Application: str
    """The application that will be used to filter the returned parameters."""
    ParamDirection: str
    """
            The parameter direction that will be used to filter the returned parameters. If it
            is empty, the system returns all associated parameters on the parent.
            """
    Options: System.Collections.Hashtable
    IsComplexDataEnabled: bool
    """
            If true, the operation will fetch the corresponding parameter complex data files.
            Will be implemented later. This is just a placeholder created.
            """

class GetStructureParamsResponse:
    """
    
            GetStructureParamsResponse Represents all the associated parameters along with all
            its overridden information, such as contextInfo, source.
            
    """
    def __init__(self, ) -> None: ...
    Outputs: list[StructureParamsOutput]
    """
            A list of StructureParamsOutput that contain  the details of overridden and the source
            parameters.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData that contains errors that the operation may encounter."""

class ParameterComplexFileData:
    """
    
            ParameterComplexFileData is a structure containing the complex data information of
            the parameter.
            
    """
    def __init__(self, ) -> None: ...
    CurrentValueTableJson: str
    """Json string representing the latest value table of the complex data."""
    GoalTableJson: str
    """Json string representing the goal table of the complex data."""

class OverriddenStructureParams:
    """
    
            OverriddenStructureParams is a structure containing the overridden parameter and
            all it associated information such as direction, context information, its source
            and the complexdata files.
            
    """
    def __init__(self, ) -> None: ...
    Parameter: Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute
    """The overridden parameter Att0MeasurableAttribute obtained for the given inputs."""
    ContextInfo: Teamcenter.Soa.Client.Model.Strong.PSBOMViewRevision
    """The PSBOMViewRevision objects when the parameter is overridden."""
    SourceParam: Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute
    """Corresponding source parameter for the overridden parameter."""
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """Revision Rule applied on the parameter."""
    ComplexdataFiles: ParameterComplexFileData
    """
            ComplexData associated with Parameter. Will be implemented later. This is just a
            placeholder created.
            """

class SourceStructureParams:
    """
    
            SourceStructureParams is a structure containing the source parameter on the Item
            Revisions. And, all its associated information such as direction and the complexdata
            files.
            
    """
    def __init__(self, ) -> None: ...
    Parameter: Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute
    """The Att0MeasurableAttribute obtained  for the given inputs."""
    ParamDirection: str
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """Revision Rule applied on the parameter"""
    VariantRules: list[Teamcenter.Soa.Client.Model.Strong.VariantRule]
    """A list of VariantRule objects applied on the parameter."""
    ComplexDataFiles: ParameterComplexFileData
    """
            ComplexData associated with Parameter. Will be implemented later. This is just a
            placeholder created.
            """

class StructureParamsOutput:
    """
    
            StructureParamsOutput is a structure containing all the information of all the source
            parameters and the overridden parameters.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the GetStructureParamsInput.clientId. This is used by the
            caller to identify this data structure with the source input data.
            """
    OverriddenParams: System.Collections.Hashtable
    """
            Map (string  , list of OverriddenStructureParams) of thread chain and its corresponding
            overridden parameter information.
            """
    SourceParams: System.Collections.Hashtable
    """
            Map (ItemRevision, list of SourceStructureParams)  of Item Revision and its associated
            parameter information.
            """

class AttributeTargetManagement:
    """
    Interface AttributeTargetManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetParametersForStructureData(self, Inputs: list[GetStructureParamsInput], Pref: GetStructureParamsPref) -> GetStructureParamsResponse: ...

