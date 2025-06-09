import Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement
import Cae0.Services.Internal.Strong.Simproc._2020_04.SimDataManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class Cae0PackageOutputConfig3:
    def __init__(self, ) -> None: ...
    Selected: bool
    OutputDescriptor: str
    OutputType: str
    UseExistingObject: bool
    OutputObjUID: str
    CreateData: Cae0.Services.Internal.Strong.Simproc._2020_04.SimDataManagement.Cae0CreateObjectInput2
    ValueForPatternN: str
    InputItemId: str
    InputItemName: str
    InputItemRev: str
    IsPatternResolved: bool

class Cae0PackagePatternValues:
    def __init__(self, ) -> None: ...
    OutputObjectItemId: str
    OutputObjectItemName: str
    OutputObjectItemDesc: str
    ValueForInputItemIdPattern: str
    ValueForInputItemRevPattern: str
    ValueForInputItemNamePattern: str
    ValueForNPattern: str

class Cae0PackagePatternValuesResp:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    OutputDescToPatternValuesMap: System.Collections.Hashtable
    PatternToCounterListMap: System.Collections.Hashtable

class SimDataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ProcessCAEPackageWithPatterns(self, InputConfigList: list[Cae0.Services.Internal.Strong.Simproc._2020_04.SimDataManagement.Cae0PackageInputConfig2], OutputConfigList: list[Cae0PackageOutputConfig3], DatasetConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDatasetConfig], BvrConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageBVRConfig], DestinationFolder: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDestFolderConfig, DetailsLogConfig: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDetailsLogConfig, WorkflowConfig: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageWorkFlowConfig, PatternToCounterListMap: System.Collections.Hashtable, ConfigObject: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ResolveCAEPackagePatterns(self, CaePackageConfig: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision, OutputDescToInputObjMap: System.Collections.Hashtable, PatternToCounterListMap: System.Collections.Hashtable) -> Cae0PackagePatternValuesResp: ...

