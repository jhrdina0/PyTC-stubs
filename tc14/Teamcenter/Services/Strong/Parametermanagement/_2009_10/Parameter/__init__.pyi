import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BitDefinitionInfo:
    """
    
BitDefinitionInfo structure represents all
            the details of bit definition to be created/updated.
    """
    def __init__(self, ) -> None: ...
    BitDefinitionObject: Teamcenter.Soa.Client.Model.ModelObject
    """
BitDef business object. If it is null, setBitDefinitionProperties operation
            creates a new BitDef business object. If not null, setBitDefinitionProperties
            updates this BitDef.
            """
    ByteNum: int
    """Index of the byte within a BitDef business object"""
    BitNum: int
    """Index of the bit within a byte"""
    Name: str
    """Bit name"""
    MeaningOf0: str
    """Meaning if the bit equals to 0"""
    MeaningOf1: str
    """Meaning if the bit equals to 1"""

class BitValueInfo:
    """
    
BitValueInfo structure represents all the
            details of bit value to be updated.
    """
    def __init__(self, ) -> None: ...
    BitValueObject: Teamcenter.Soa.Client.Model.ModelObject
    """BitValue business object."""
    Value: bool
    """Bit value"""
    BitDefinition: BitDefinitionInfo
    """Bit Definition"""

class GetBitDefinitionPropertiesResponse:
    """
    
GetBitDefinitionPropertiesResponse structure
            represents all the details of bit definition for the input BitDef.
    """
    def __init__(self, ) -> None: ...
    BitDefinitionInfo: list[BitDefinitionInfo]
    """Bit definition for each BitDef business object"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data to hold Teamcenter Services framework objects that were created or updated
            by the service.
            """

class GetBitValuePropertiesResponse:
    """
    
GetBitValuePropertiesResponse structure represents
            all the details of bit value for the input BitValue.
    """
    def __init__(self, ) -> None: ...
    BitValueInfo: list[BitValueInfo]
    """Bit value for each BitValue business object"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data to hold Teamcenter Services framework objects that were created or updated
            by the service.
            """

class Parameter:
    """
    Interface Parameter
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetBitDefinitionProperties(self, BitDefinitions: list[Teamcenter.Soa.Client.Model.Strong.BitDef]) -> GetBitDefinitionPropertiesResponse:
        """    
             This operation loads the bit definition for each ccdm::BitDef
             supplied. Bit definition contains information for properties such as byte number,
             bit number within the byte, name, meaning of 0 and meaning of 1.
             

Use Cases:

Use case 1: Get bit definition for a BitDef

             You can get the bit definition data using getBitDefinitionProperties operation
             by providing the BitDef tag.
             

Teamcenter Component:

             Calibration and Configuration Data Management - Calibration and Configuration Data
             Management
             
        :param BitDefinitions: 
                         BitDef objects
             
        :return: .
        """
        ...
    def GetBitValueProperties(self, BitValues: list[Teamcenter.Soa.Client.Model.Strong.BitValue]) -> GetBitValuePropertiesResponse:
        """    
             This operation loads the bit value for each ccdm::BitValue
             supplied. Bit value contains information for properties such as value (true/false),
             bit definition object.
             

Use Cases:

Use case 1: Get bit value for a BitValue object

             You can get the bit value data using getBitValueProperties operation by providing
             the BitValue object.
             

Teamcenter Component:

             Calibration and Configuration Data Management - Calibration and Configuration Data
             Management
             
        :param BitValues: 
<b>BitValue</b> objects
             
        :return: .
        """
        ...
    def SetBitDefinitionProperties(self, BitDefinitionInfo: list[BitDefinitionInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates or modifies a BitDef business object for each BitDefinitionInfo supplied. The BitDefinitionInfo contains information for properties such as
             byte number, bit number within the byte, name, meaning of 0, and meaning of 1. If
             the BitDef is not null in BitDefinitionInfo
             structure, the operation updates this BitDef with the rest of the property
             values. Otherwise the operation creates a new BitDef with the specific property
             values.
             

Use Cases:

Use case 1: Create a Bit Definition

             You can create a new BitDef using setBitDefinitionProperties operation
             by providing bitDefinitionObject as null
             in BitDefinitionInfo structure.
             

Use case 2: Modify a Bit Definition

             You can modify an existing BitDef using setBitDefinitionProperties
             operation by providing bitDefinitionObject
             as an existing BitDef in BitDefinitionInfo
             structure.
             


Teamcenter Component:

             Calibration and Configuration Data Management - Calibration and Configuration Data
             Management
             
        :param BitDefinitionInfo: 
                         Structures containing the details of the bit definition to be created/modified.
             
        :return: in Created/Updated lists.
        """
        ...
    def SetBitValueProperties(self, BitValInfo: list[BitValueInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation modifies a BitValue business object for each BitValueInfo supplied. The BitValueInfo
             contains information for properties such as value (true/false), bit definition object.
             The BitValue business object is specified in BitValueInfo
             structure as well.
             

Use Cases:

Use case 1: Modify a Bit Value

             You can modify an existing BitValue using setBitValueProperties operation
             by providing bitValueObject as an existing BitValue in BitValueInfo structure.
             


Teamcenter Component:

             Calibration and Configuration Data Management - Calibration and Configuration Data
             Management
             
        :param BitValInfo: 
                         Structures containing the details of the bit value to be modified.
             
        :return: in Updated lists.
        """
        ...

