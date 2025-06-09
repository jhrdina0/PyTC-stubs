import Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class Cae0CreateObjectInput2:
    def __init__(self, ) -> None: ...
    BoName: str
    PropertyNameValues: System.Collections.Hashtable
    CompoundCreateInput: System.Collections.Hashtable

class Cae0PackageInputConfig2:
    def __init__(self, ) -> None: ...
    InputDescriptor: str
    ObjUID: str

class Cae0PackageOutputConfig2:
    def __init__(self, ) -> None: ...
    Selected: bool
    OutputDescriptor: str
    OutputType: str
    UseExistingObject: bool
    OutputObjUID: str
    CreateData: Cae0CreateObjectInput2

class SimDataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ProcessCAEPackage(self, InputConfigList: list[Cae0PackageInputConfig2], OutputConfigList: list[Cae0PackageOutputConfig2], DatasetConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDatasetConfig], BvrConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageBVRConfig], DestinationFolder: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDestFolderConfig, DetailsLogConfig: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDetailsLogConfig, WorkflowConfig: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageWorkFlowConfig, ConfigObject: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision) -> Teamcenter.Soa.Client.Model.ServiceData: ...

