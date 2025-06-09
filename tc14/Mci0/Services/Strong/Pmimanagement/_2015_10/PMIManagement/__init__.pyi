import Mci0.Services.Strong.Pmimanagement._2011_12.PMIManagement
import System
import Teamcenter.Soa.Client.Model
import typing

class GetPMIPropertiesInputData:
    """
    
            An object containing business objects, search criteria to search PMIs (Product Manufacturing
            Information) and list of PMI properties to fetch
            
    """
    def __init__(self, ) -> None: ...
    InputBO: Teamcenter.Soa.Client.Model.ModelObject
    """A business object representing Item Revision or BOM Line"""
    OccTypes: list[str]
    """A list of occurrence types"""
    ObjTypes: list[str]
    """A list of object types"""
    PmiPropertyNames: list[str]
    """A list of property names"""
    ContextBO: Teamcenter.Soa.Client.Model.ModelObject
    """
            A business object representing collaboration context under which the business object
            inputBO is present
            """

class GetPMIPropertiesOutput:
    """
    
            An object containing PMI properties information for an input Item Revision or BOM
            Line object
            
    """
    def __init__(self, ) -> None: ...
    InputBO: Teamcenter.Soa.Client.Model.ModelObject
    """The input Business Object"""
    PmiInfos: list[PMIInfo]
    """A collection of PMIInfo object type"""

class GetPMIPropertiesResponse:
    """
    
            An object containing collection of GetPMIPropertiesOutput objects and ServiceData
            object
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetPMIPropertiesOutput]
    """A collection of GetPMIPropertiesOutput objects"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData object"""

class ImportPMIInputInfo2:
    """
    The input ImportPMIInputInfo2 for importPMI2 SOA.
    """
    def __init__(self, ) -> None: ...
    SourceObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The source object containing a DirectModel or a mci0PMIXml dataset to import PMIs
            information.
            """
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """The selected object where PMIs will be imported to."""
    RelationTypeObject: Teamcenter.Soa.Client.Model.ModelObject
    """Could be either a mci0PMIXmlRel or IMAN_Rendering."""
    DatasetTypeName: str
    """The type name of the dataset containing the pmi xml."""
    NamedReferenceTypeName: str
    """The type name of the named reference representing the pmi xml."""
    PmiFormTypeName: str
    """The type name of the PMI forms to be created."""
    AccountabilityIdsToImport: list[int]
    """
            The list of accountability IDs identifying PMIs within the JT part to be imported
            (created / updated) in order to allow to import just a subset of PMIs and not all.
            """

class PMIBoolPropertyInfo:
    """
    A structure representing single PMI property name and value of boolean property type
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the PMI property"""
    Value: bool
    """The boolean value of the PMI property"""

class PMIDatePropertyInfo:
    """
    
            A structure representing single PMI property name and value of the date property
            type
            
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the PMI property"""
    Value: System.DateTime
    """The date value of the PMI property"""

class PMIDoublePropertyInfo:
    """
    A structure representing single PMI property name and value of double property type
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the PMI property"""
    Value: float
    """The double value of PMI property"""

class PMIInfo:
    """
    An object representing single PMI and its properties
    """
    def __init__(self, ) -> None: ...
    PmiID: str
    """ID name of PMI object"""
    PmiIntPropertyInfos: list[PMIIntPropertyInfo]
    """The collection of PMIIntPropertyInfo objects"""
    PmiDoublePropertyInfos: list[PMIDoublePropertyInfo]
    """The collection of PMIDoublePropertyInfo objects"""
    PmiStringPropertyInfos: list[PMIStringPropertyInfo]
    """The collection of PMIStringPropertyInfo objects"""
    PmiDatePropertyInfos: list[PMIDatePropertyInfo]
    """The collection of PMIDatePropertyInfo objects"""
    PmiBoolPropertyInfos: list[PMIBoolPropertyInfo]
    """The collection of PMIBoolPropertyInfo objects"""

class PMIIntPropertyInfo:
    """
    A structure representing single PMI property name and value of integer property type
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the PMI property"""
    Value: int
    """The integer value of the PMI property"""

class PMIStringPropertyInfo:
    """
    A structure representing single PMI property name and value of string property type
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the PMI property"""
    Value: str
    """The string value of the PMI property"""

class PMIManagement:
    """
    Interface PMIManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPMIProperties(self, Input: list[GetPMIPropertiesInputData]) -> GetPMIPropertiesResponse:
        """    
             This SOA operation takes Business Object, Search criteria and PMI Property names
             as input. It finds out if PMIs exist based on the criteria(objcet type and occurrence
             type). If PMIs exist it returns values of specified PMI properties.
             

Teamcenter Component:

             Product Manufacturing Information (PMI) Component - Product Manufacturing Information
             (PMI) solution to manage the PMI information in Teamcenter.
             
        :param Input: 
                         A collection of objects which holds business object, information about PMI filter
                         criteria and PMI properties
             
        :return: 69022 :  The PMI property "%1$" does not exist. Please contact your system administrator.
        """
        ...
    def ImportPMIs2(self, InputInfo: list[ImportPMIInputInfo2]) -> Mci0.Services.Strong.Pmimanagement._2011_12.PMIManagement.ImportPMIsResponse:
        """    
             This operation imports a list of PMIs from the Named References .xml or .JT file,
             attached to a Dataset related to an ItemRevision. New Mci0PMI objects are either
             created, updated, or mark as deleted under the target ItemRevision. A list of PMI
             IDs (accountability ID) in order to allow an import of these PMIs. In case this list
             is empty all the existing PMIs will be imported from the file.
             

Teamcenter Component:

             Product Manufacturing Information (PMI) Component - Product Manufacturing Information
             (PMI) solution to manage the PMI information in Teamcenter.
             
        :param InputInfo: 
                         The input ImportPMIInputInfo.
             
        :return: 69020:The traversing of the following Dataset Named Reference JT file has failed.
             Please check the syslog for more details.
        """
        ...

