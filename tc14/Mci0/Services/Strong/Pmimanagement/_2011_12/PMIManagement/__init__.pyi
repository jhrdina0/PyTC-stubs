import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class PMIData:
    """
    PMI information to be saved.
    """
    def __init__(self, ) -> None: ...
    FormType: str
    """The type name of the business object"""
    StringProps: System.Collections.Hashtable
    """The map of property names and string property values."""
    StringArrayProps: System.Collections.Hashtable
    """The map of property names and string array property values."""
    DoubleProps: System.Collections.Hashtable
    """The map of property names and double property values."""
    DoubleArrayProps: System.Collections.Hashtable
    """The map of property names and double array property values."""
    FloatProps: System.Collections.Hashtable
    """The map of property names and float property values."""
    FloatArrayProps: System.Collections.Hashtable
    """The map of property names and float array property values."""
    IntProps: System.Collections.Hashtable
    """The map of property names and int property values."""
    IntArrayProps: System.Collections.Hashtable
    """The map of property names and int array property values."""
    BoolProps: System.Collections.Hashtable
    """The map of property names and bool property values."""
    BoolArrayProps: System.Collections.Hashtable
    """The map of property names and bool array property values."""
    DateProps: System.Collections.Hashtable
    """The map of property names and date property values."""
    DateArrayProps: System.Collections.Hashtable
    """The map of property names and date array property values."""
    BusinessObjectProps: System.Collections.Hashtable
    """The map of property names and business object property values."""
    BusinessObjectArrayProps: System.Collections.Hashtable
    """The map of property names and business object array property values."""

class CreatePMIInputInfo:
    """
    The input info for Create PMI.
    """
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """The selected target BOMLine object."""
    PmiData: PMIData
    """PMI properties to be saved."""

class CreatePMIOutput:
    """
    The output CreatePMIOutput.
    """
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """The object for which PMI has created."""
    CreatedPMI: Teamcenter.Soa.Client.Model.ModelObject
    """The newly created Mci0PMI object."""

class CreatePMIResponse:
    """
    The newly created PMI along with the target object and serviceData as partial errors.
    """
    def __init__(self, ) -> None: ...
    CreatePMIOutput: list[CreatePMIOutput]
    """The newly created PMI along with the target object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Including partial errors."""

class ImportPMIInputInfo:
    """
    The input ImportPMIInputInfo.
    """
    def __init__(self, ) -> None: ...
    SourceObject: Teamcenter.Soa.Client.Model.ModelObject
    """The source object containing Mci0PMIXml dataset to import PMIs information."""
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """The selected object where PMIs information will be imported."""
    RelationTypeObject: Teamcenter.Soa.Client.Model.ModelObject
    """The type of relationship between the source ItemRevision and the Mci0PMIXml."""
    DatasetTypeName: str
    """The type name of the dataset containing the pmi xml."""
    NamedReferenceTypeName: str
    """The type name of the named reference representing the pmi xml."""
    PmiFormTypeName: str
    """The type name of the PMI forms to be created."""

class ImportPMIsOutput:
    """
    The output ImportPMIsOutput.
    """
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """The object where PMIs got imported."""
    CreatedPMIs: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The newly created PMIs."""
    UpdatedPMIs: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The existing PMIs that were updated."""
    MarkedAsDeletedPMIs: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The PMIs that were  marked as deleted."""

class ImportPMIsResponse:
    """
    The ImportPMI Response.
    """
    def __init__(self, ) -> None: ...
    ImportPMIsOutput: list[ImportPMIsOutput]
    """The returned ImportPMIsOutput."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Including partial errors."""

class PMIManagement:
    """
    Interface PMIManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreatePMI(self, CreatePMIInputInfo: list[CreatePMIInputInfo]) -> CreatePMIResponse:
        """    
             This operation creates  Mci0PMI objects under the target ItemRevision. The Mci0PMI
             data will be stored in a Mci0PMIChracteristicFrm in context of the target ItemRevision.
             

Teamcenter Component:

             Product Manufacturing Information (PMI) Component - Product Manufacturing Information
             (PMI) solution to manage the PMI information in Teamcenter.
             
        :param CreatePMIInputInfo: 
                         The input  for createPMIInput
             
        :return: This operation returns the newly created GDELines referring to the new created Mci0PMI.
             The following partial errors may be returned: 69013: Unable to create the Mci0PMIChracteristicFrm
             for the PMI.
        """
        ...
    def ImportPMIs(self, InputInfo: list[ImportPMIInputInfo]) -> ImportPMIsResponse:
        """    
             The operation imports all the PMIs data from the Mci0PMIXml dataset attached to the
             source ItemRevision. New Mci0PMI objects will be created under the target ItemRevision.
             Existing  Mci0PMI  will be updated or marked as deleted as necessary.
             

Teamcenter Component:

             Product Manufacturing Information (PMI) Component - Product Manufacturing Information
             (PMI) solution to manage the PMI information in Teamcenter.
             
        :param InputInfo: 
                         The input ImportPMIInfo.
             
        :return: The ImportPMIsOutput contains all the information regarding the created, updated
             and marked as deleted PMIs along with target object. The following partial errors
             may be returned: 69005: The dataset is not attached to the BOM Structure. 69011:
             Import PMI operation failed.
        """
        ...

