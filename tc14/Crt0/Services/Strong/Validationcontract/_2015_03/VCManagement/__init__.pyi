import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ContractDefnOutput:
    """
    
            This structure contains detailed information of the Contract Definition (i.e. the
            Contract Package that is attached to the Contract Definition)
            
    """
    def __init__(self, ) -> None: ...
    GroupName: str
    """
            Section group name (Example: View, Results, etc)
            
"""
    ContractDefnSections: list[ContractDefnSection]
    """A list of ContractDefnSection objects detailing Section information."""

class ContractDefnResponse:
    """
    
            This structure contains detailed information about Contract Definitions. The information
            contains  Section Group names, Section display names, allowed object types for each
            Section, and common properties for the object types in each Section, etc.
            
    """
    def __init__(self, ) -> None: ...
    ContractDefnOutputs: list[ContractDefnOutput]
    """A list of ContractDefnOutput objects detailing information of the Contract Definition."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """This is an SOA Service Data structure."""

class ContractDefnSection:
    """
    
            This structure contains detailed information of the sections specified within a group
            in a Contract Definition.
            
    """
    def __init__(self, ) -> None: ...
    DisplayName: str
    """Display name of Contract Definition Section"""
    ObjectInfos: list[ObjectInfo]
    """A list of object types and quantities that must be displayed in a section."""
    PropertyNames: list[str]
    """
            Teamcenter object properties that must be displayed in a section. These properties
            are common to all the objects in the section.
            """
    PropertyDisplayNames: list[str]
    """Teamcenter object property's display name."""

class ObjectInfo:
    """
    
            This structure contains information of the object types and their quantities that
            are expected to appear in a section.
            
    """
    def __init__(self, ) -> None: ...
    Type: str
    """Teamcenter Business object type"""
    Quantity: str
    """
            Number of objects of a given type. Allowed values are:
            
            a.    "0" (Zero)
            

            b.    Any positive number
            
            Example: Value of 1 allows only one object of the given type in the section.
            

            c.    "*". Value of * allows any number of objects of the given
            type in the section.
            
"""

class VCManagement:
    """
    Interface VCManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetContractDefnDetails(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.Crt0VCDefnRevision]) -> ContractDefnResponse:
        """    
             This operation retrieves the details of the input Contract Definitions by reading
             the attached Contract Package. The operation will return the details only if the
             package is valid.
             

             For a Contract Package to be valid:
             

It must adhere to the Contract schema. The schema can be found in
             the dataset "Crt0ContractPkgSchema" which gets deployed to Teamcenter database during
             installation of the "Validation Contract" feature.
             
Business objects used in the package must exist in Teamcenter.
             
Property names used in the package must exist in Teamcenter.
             



Teamcenter Component:

             Validation Contract - This component is used to manage data for Validation Contract.
             
        :param Inputs: 
                         Vector of inputs for getting details of the Contract Definition object
             
        :return: 
        """
        ...

