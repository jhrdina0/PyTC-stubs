import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class Cae0CreateObjectInput:
    def __init__(self, ) -> None: ...
    BoTypeName: str
    PropertyNameValues: System.Collections.Hashtable
    CompoundCreateObjectInput: System.Collections.Hashtable

class Cae0PackageBVRConfig:
    def __init__(self, ) -> None: ...
    Selected: bool
    ParentDescriptor: str
    ChildDescriptorList: list[str]
    BvrType: str

class Cae0PackageDatasetConfig:
    def __init__(self, ) -> None: ...
    Selected: bool
    Descriptor: str
    DsType: str
    DsSource: str
    DsName: str
    DsRelation: str
    DsUID: str

class Cae0PackageDestFolderConfig:
    def __init__(self, ) -> None: ...
    Uid: str
    UseSubFolder: bool
    SubFolderName: str
    PasteInputObject: bool

class Cae0PackageDetailsLogConfig:
    def __init__(self, ) -> None: ...
    PersistDetailsLog: bool
    DetailsLogDSName: str

class Cae0PackageInputConfig:
    def __init__(self, ) -> None: ...
    InputDescriptor: str
    Uid: str
    IsBOMLine: bool
    InputBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine

class Cae0PackageOutputConfig:
    def __init__(self, ) -> None: ...
    Selected: bool
    OutputDescriptor: str
    OutputType: str
    CreateData: Cae0CreateObjectInput

class Cae0PackageWorkFlowConfig:
    def __init__(self, ) -> None: ...
    ProcessTemplateName: str
    ProcessAssignmentName: str

class SimDataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ProcessCAEPackage(self, InputConfigList: list[Cae0PackageInputConfig], OutputConfigList: list[Cae0PackageOutputConfig], DatasetConfigList: list[Cae0PackageDatasetConfig], BvrConfigList: list[Cae0PackageBVRConfig], DestinationFolder: Cae0PackageDestFolderConfig, DetailsLogConfig: Cae0PackageDetailsLogConfig, WorkflowConfig: Cae0PackageWorkFlowConfig, ConfigObject: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision) -> Teamcenter.Soa.Client.Model.ServiceData: ...

