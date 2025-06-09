import Att0.Services.Strong.Attrtargetmgmt._2015_03.AttributeTargetManagement
import Att0.Services.Strong.Attrtargetmgmt._2015_10.AttributeTargetManagement
import Att0.Services.Strong.Attrtargetmgmt._2018_06.AttributeTargetManagement
import Att0.Services.Strong.Attrtargetmgmt._2018_11.AttributeTargetManagement
import Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement
import Att0.Services.Strong.Attrtargetmgmt._2021_12.AttributeTargetManagement
import Att0.Services.Strong.Attrtargetmgmt._2022_12.AttributeTargetManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class AttributeTargetManagementRestBindingStub(AttributeTargetManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetLatestDefinitions(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2015_03.AttributeTargetManagement.DefinitionCriteria]) -> Att0.Services.Strong.Attrtargetmgmt._2015_03.AttributeTargetManagement.DefinitionsResponse: ...
    def SynchronizeMeasuableAttributes(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2015_03.AttributeTargetManagement.SyncMeasurableAttributeInput], Pref: Att0.Services.Strong.Attrtargetmgmt._2015_03.AttributeTargetManagement.SyncMeasurableAttributePref) -> Att0.Services.Strong.Attrtargetmgmt._2015_03.AttributeTargetManagement.SyncMeasurableAttributeResponse: ...
    def DeleteMeasurableAttributes(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2015_10.AttributeTargetManagement.DeleteMeasurableAttributeInput]) -> Att0.Services.Strong.Attrtargetmgmt._2015_10.AttributeTargetManagement.DeleteMeasurableAttributesResponse: ...
    def SetAttributeComplexData(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2018_06.AttributeTargetManagement.SetAttributeComplexDataIn]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetAttributeComplexData(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2018_11.AttributeTargetManagement.GetAttributeComplexDataIn]) -> Att0.Services.Strong.Attrtargetmgmt._2018_11.AttributeTargetManagement.GetAttributeComplexDataResp: ...
    def AttachParameters(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.AttachParamsInput]) -> Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.AttachParamsResponse: ...
    def CreateParameters(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.CreateParamsInput]) -> Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.CreateParamsResponse: ...
    def GetLatestMeasureValues(self, Parameters: list[Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute], Methods: list[str], ValueFileRequired: bool) -> Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.GetLatestMeasureValuesResp: ...
    def GetParameters(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.GetParamsInput], Pref: Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.GetParamsPref) -> Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.GetParamsResponse: ...
    def UpdateParameters(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.UpdateParamsInput]) -> Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.UpdateParamsResponse: ...
    def ReplaceParameters(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2021_12.AttributeTargetManagement.ReplaceParamsInput]) -> Att0.Services.Strong.Attrtargetmgmt._2021_12.AttributeTargetManagement.ReplaceParametersResp: ...
    def UpdateParameters2(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2021_12.AttributeTargetManagement.UpdateParamsInput2]) -> Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.UpdateParamsResponse: ...
    def GetParametersForStructureData(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2022_12.AttributeTargetManagement.GetStructureParamsInput], Pref: Att0.Services.Strong.Attrtargetmgmt._2022_12.AttributeTargetManagement.GetStructureParamsPref) -> Att0.Services.Strong.Attrtargetmgmt._2022_12.AttributeTargetManagement.GetStructureParamsResponse: ...

class AttributeTargetManagementService:
    """
    
            This operation gets the list of ItemRevision objects based on given criteria.
            The DefinitionCriteria holds criteria such as item revision name, item or
            item revision type name, enabled release status as well as disabled release status;
            if and only if the latest ItemRevision or sub type objects will be returned
            when it matches these criteria.
            


Library Reference:

Att0SoaAttrTargetMgmtStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> AttributeTargetManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetLatestDefinitions(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2015_03.AttributeTargetManagement.DefinitionCriteria]) -> Att0.Services.Strong.Attrtargetmgmt._2015_03.AttributeTargetManagement.DefinitionsResponse:
        """    
             This operation gets the list of ItemRevision objects based on given criteria.
             The DefinitionCriteria holds criteria such as item revision name, item or
             item revision type name, enabled release status as well as disabled release status;
             if and only if the latest ItemRevision or sub type objects will be returned
             when it matches these criteria.
             

Use Cases:

             Creates an Attribute Definition Revision into Teamcenter like below and following
             story:
             
             {ItemID=000001, Name=AttributeDef_1, Revision=B, Release Status="Released"}
             
             {ItemID=000001, Name=AttributeDef_1, Revision=C, Release Status="Obsolete"}
             
             {ItemID=000001, Name=AttributeDef_1, Revision=D, Release Status=""}
             

             When DefinitionCriteria is set as objectName=AttributeDef_1, itemOrRevType=Att0AttributeDefRevision
             enabledStatus=Released, disabledStatus=Obsolete
             

             At first case, revision B will be returned since it is released and status matches
             "Released"
             
             At second case, none revision is returned since latest revision C is "Obsolete"
             
             At third case, none revision is returned since latest revision D is in progress,
             while revision C is obsoleted
             


Teamcenter Component:

             Attribute Target Management - This component consists of the Client and Enterprise
             Tier code and constructs that support Attribute and Target related functionality
             including such things as Teamcenter Active Workspace application plus SOA, ITK and
             Preferences.
             
        :param Inputs: 
                         The criteria for filtering the list of latest <b>ItemRevision</b> objects.
             
        :return: 
        """
        ...
    def SynchronizeMeasuableAttributes(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2015_03.AttributeTargetManagement.SyncMeasurableAttributeInput], Pref: Att0.Services.Strong.Attrtargetmgmt._2015_03.AttributeTargetManagement.SyncMeasurableAttributePref) -> Att0.Services.Strong.Attrtargetmgmt._2015_03.AttributeTargetManagement.SyncMeasurableAttributeResponse:
        """    
             This operation is used to synchronize Att0MeasurableAttribute objects between
             source Att0MeasurableAttribute instances and target Att0MeasurableAttribute
             instances.  This synchronization operation has two process flows: synchronize from
             source Att0MeasurableAttribute instances to input Att0MeasurableAttribute
             instances; and publish from output Att0MeasurableAttribute instances to source
             Att0MeasurableAttribute instances.
             

When synchronize from source to input Att0MeasurableAttribute,
             an update operation is done against input Att0MeasurableAttribute with latest
             property values from source Att0MeasurableAttribute. Meanwhile copies the latest
             Att0MeasurableValue of source Att0MeasurableAttribute and inserts it into
             the input Att0MeasurableAttribute.
             
When publish from output to source Att0MeasurableAttribute,
             the latest Att0MeasurableValue is retrieved from output Att0MeasurableAttribute
             and inserts it into the latest Att0MeasurableValue list on the source Att0MeasurableAttribute.
             The source Att0MeasurableAttribute properties will not be updated.
             
If there is an issue during publication, the process stops and all
             modified objects are be restored.
             



Use Cases:

             1.    A system architect creates a product structure of logical
             blocks (Fnd0LogicalBlock), and defines for each block its measurable attributes
             (Att0MeasurableAttribute). As the design of the product architecture evolves,
             the system architect requests a partial or complete validation of the system. As
             part of the request system architect defines the logical blocks to be validated,
             their attributes that will inputs for the validation and the ones that need to be
             measured. As the system architect sets a logical block attribute (Att0MeasurableAttribute)
             as an input of the validation, the system builds a copy of the attribute for the
             validation context. The goal is to isolate the validation context from any updates
             that can be done on the product context.
             
             However when processing the validation request, the validation engineer should know
             if the input attributes are up to date with the product logical blocks attributes.
             If they are not the validation engineer can run synchronize input attributes command.
             
             2.    A system architect creates a product structure of logical
             blocks (Fnd0LogicalBlock), and defines for each block its measurable attributes
             (Att0MeasurableAttribute). As the design of the product architecture evolves,
             the system architect requests a partial or complete validation of the system. As
             part of the request system architect defines the logical blocks to be validated,
             their attributes that will inputs for the validation and the ones that need to be
             measured. As the system architect sets a logical block attribute (Att0MeasurableAttribute)
             as an input of the validation, the system builds a copy of the attribute for the
             validation context. The goal is to isolate the validation context from any updates
             that can be done on the product context.
             
             However when processing the validation request, the validation engineer should know
             if the output attributes are measured which comes out a new measurement value (Att0MeasureValue).
             If new measurement value is generated, the validation engineer can run publish command
             to publish output attribute measurement value to logical block attribute.
             

Teamcenter Component:

             Attribute Target Management - This component consists of the Client and Enterprise
             Tier code and constructs that support Attribute and Target related functionality
             including such things as Teamcenter Active Workspace application plus SOA, ITK and
             Preferences.
             
        :param Inputs: 
                         The synchronization measurable attribute inputs.
             
        :param Pref: 
                         The synchronization measurable attribute preference.
             
        :return: 
        """
        ...
    def DeleteMeasurableAttributes(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2015_10.AttributeTargetManagement.DeleteMeasurableAttributeInput]) -> Att0.Services.Strong.Attrtargetmgmt._2015_10.AttributeTargetManagement.DeleteMeasurableAttributesResponse:
        """    
             This operation deletes measurable attribute (Att0MeasurableAttribute) objects
             from given parent object.
             

If the given measurable attribute(Att0MeasurableAttribute)
             is a source attribute,  it is is deleted directly.
             
If the given measurable attribute(Att0MeasurableAttribute)
             is an overridden attribute, the overridden attribute itself is deleted as well as
             its related source attribute.
             
If the given measurable attribute(Att0MeasurableAttribute)
             is a source attribute and it is assigned as Input/Output attribute to an Analysis
             Request(Crt0VldnContractRevision), then the delete actions is discarded  and
             a warning message is returned.
             



Use Cases:


A system architect creates a product structure of logical blocks
             (Fnd0LogicalBlock), and defines for each block its measurable attributes (Att0MeasurableAttribute).
             A system designer may override measurable attribute in context of product. As the
             design of the product architecture evolves or need to re-design, the system designer
             may need to delete the already created measurable attributes from product architecture
             and will re-create measurable attribute.
             
A system architect may revise the logical block (Fnd0LogicalBlock),
             it copies measurable attributes from previous logical block revision (Fnd0LogicalBlockRevision)
             to new revision block. A system designer may want to delete attributes from previous
             logical block revision, and re-create attributes (Att0MeasurableAttribute)
             in the new logical block revision.
             



Teamcenter Component:

             Attribute Target Management - This component consists of the Client and Enterprise
             Tier code and constructs that support Attribute and Target related functionality
             including such things as Teamcenter Active Workspace application plus SOA, ITK and
             Preferences.
             
        :param Inputs: 
                         The list of measurable attributes and their parent objects.
             
        :return: 
        """
        ...
    def SetAttributeComplexData(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2018_06.AttributeTargetManagement.SetAttributeComplexDataIn]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetAttributeComplexData(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2018_11.AttributeTargetManagement.GetAttributeComplexDataIn]) -> Att0.Services.Strong.Attrtargetmgmt._2018_11.AttributeTargetManagement.GetAttributeComplexDataResp:
        """    
             This operation gets the complex data for the given Attribute Definition or Measurable
             Attribute.
             

Use Cases:

             The System Engineer opens Attribute Definition or Measurable Attribute in Active
             Workspace and reviews the complex data (if existing) for Goal or Min or Max properties.
             

Teamcenter Component:

             Attribute Target Management - This component consists of the Client and Enterprise
             Tier code and constructs that support Attribute and Target related functionality
             including such things as Teamcenter Active Workspace application plus SOA, ITK and
             Preferences.
             
        :param Inputs: 
                         Input information required for the getAttributeComplexData in the form of GetAttributeComplexDataIn.
             
        :return: * 185050 - The property does not exist on Att0MeasurableAttribute, please provide
             valid property name.
        """
        ...
    def AttachParameters(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.AttachParamsInput]) -> Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.AttachParamsResponse: ...
    def CreateParameters(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.CreateParamsInput]) -> Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.CreateParamsResponse: ...
    def GetLatestMeasureValues(self, Parameters: list[Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute], Methods: list[str], ValueFileRequired: bool) -> Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.GetLatestMeasureValuesResp: ...
    def GetParameters(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.GetParamsInput], Pref: Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.GetParamsPref) -> Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.GetParamsResponse: ...
    def UpdateParameters(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.UpdateParamsInput]) -> Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.UpdateParamsResponse: ...
    def ReplaceParameters(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2021_12.AttributeTargetManagement.ReplaceParamsInput]) -> Att0.Services.Strong.Attrtargetmgmt._2021_12.AttributeTargetManagement.ReplaceParametersResp: ...
    def UpdateParameters2(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2021_12.AttributeTargetManagement.UpdateParamsInput2]) -> Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.UpdateParamsResponse: ...
    def GetParametersForStructureData(self, Inputs: list[Att0.Services.Strong.Attrtargetmgmt._2022_12.AttributeTargetManagement.GetStructureParamsInput], Pref: Att0.Services.Strong.Attrtargetmgmt._2022_12.AttributeTargetManagement.GetStructureParamsPref) -> Att0.Services.Strong.Attrtargetmgmt._2022_12.AttributeTargetManagement.GetStructureParamsResponse: ...

