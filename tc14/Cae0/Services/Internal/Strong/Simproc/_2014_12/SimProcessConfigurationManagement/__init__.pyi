import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CAEToolTabProps:
    def __init__(self, ) -> None: ...
    BoName: str
    PropNameValueMap: System.Collections.Hashtable
    RefObjNameValueMap: System.Collections.Hashtable

class CAEToolTabPropsValueInfo:
    def __init__(self, ) -> None: ...
    ToolPropValue: CAEToolTabProps
    GeneralConfigTabPropValue: CAEToolTabProps
    LaunchPropConfigTabPropValue: CAEToolTabProps
    EnvVarConfigTabPropValue: CAEToolTabProps
    InputConfigTabPropValue: CAEToolTabProps
    OutputConfigTabPropValue: CAEToolTabProps
    InputParamConfigTabPropValue: CAEToolTabProps
    AttributeConfigTabPropValue: CAEToolTabProps
    UserFeedbackConfigTabPropValue: CAEToolTabProps
    AccessControlConfigTabPropValue: CAEToolTabProps
    ParentGeneralConfigTabPropValue: CAEToolTabProps
    ParentLaunchPropConfigTabPropValue: CAEToolTabProps
    ParentEnvVarConfigTabPropValue: CAEToolTabProps
    ParentInputConfigTabPropValue: CAEToolTabProps
    ParentOutputConfigTabPropValue: CAEToolTabProps
    ParentInputParamConfigTabPropValue: CAEToolTabProps
    ParentAttributeConfigTabPropValue: CAEToolTabProps
    ParentUserFeedbackConfigTabPropValue: CAEToolTabProps
    ParentAccessControlConfigTabPropValue: CAEToolTabProps

class CAEToolItemPropStruct:
    def __init__(self, ) -> None: ...
    ToolObject: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    ToolTabPropValue: CAEToolTabPropsValueInfo
    ChildTools: list[CAEToolItemPropStruct]

class CAEToolBOMPropStructResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    ItemsPropValueStruct: CAEToolItemPropStruct

class CreateInput:
    def __init__(self, ) -> None: ...
    BoName: str
    BoUID: str
    IsDelete: bool
    StringProps: System.Collections.Hashtable
    StringArrayProps: System.Collections.Hashtable
    DoubleProps: System.Collections.Hashtable
    DoubleArrayProps: System.Collections.Hashtable
    FloatProps: System.Collections.Hashtable
    FloatArrayProps: System.Collections.Hashtable
    IntProps: System.Collections.Hashtable
    IntArrayProps: System.Collections.Hashtable
    BoolProps: System.Collections.Hashtable
    BoolArrayProps: System.Collections.Hashtable
    DateProps: System.Collections.Hashtable
    DateArrayProps: System.Collections.Hashtable
    TagProps: System.Collections.Hashtable
    TagArrayProps: System.Collections.Hashtable
    CompoundCreateInput: System.Collections.Hashtable

class CAEToolTabConfigInfo:
    def __init__(self, ) -> None: ...
    TabIdentifier: str
    IsInherited: bool
    TabAttributes: CreateInput

class SimProcessConfigurationManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def DeleteTool(self, ToolsToBDeleted: list[Teamcenter.Soa.Client.Model.ModelObject], ShouldDeleteItemAndAllRev: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def PasteTool(self, ToolsTobePasted: list[Teamcenter.Soa.Client.Model.ModelObject], TargetBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ReleaseTools(self, ToolBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], IsReleaseAll: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ReviseSimTool(self, ToolBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

