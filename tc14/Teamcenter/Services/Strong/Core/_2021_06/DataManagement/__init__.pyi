import System
import Teamcenter.Services.Strong.Core._2007_09.DataManagement
import Teamcenter.Services.Strong.Core._2010_04.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AddNamedReferenceToDatasetInfo:
    """
    
            Input structure for the addNamedReferenceToDatasets operation. This contains information
            of Dataset,
            
            list of named referenced which are going to be added with a specific reference type.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """A unique string supplied by the caller."""
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """The Dataset object to which the specified named references will be added."""
    NrInfo: list[Teamcenter.Services.Strong.Core._2010_04.DataManagement.NamedReferenceObjectInfo]
    """
            A list of named reference information to be added which contains information about
            named reference type value, object reference and object type name.
            """
    CreateNewDatasetVersion: bool
    """
            If true, a new Dataset version is created after the addition of a named reference;
            otherwise, no new version is created for a Dataset.
            """

class RemoveNamedReferenceFromDataset:
    """
    
            Input structure for the removeNamedReferenceFromDataset2 operation. This contains
            information of Dataset, a list of named referenced which are going to be removed.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """A unique string supplied by the caller."""
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """The Dataset object from which to remove the specified named references."""
    NrInfo: list[Teamcenter.Services.Strong.Core._2007_09.DataManagement.NamedReferenceInfo]
    """
            A list of named reference information to be removed which contains information of
            named reference type value, object reference.
            """
    CreateNewDatasetVersion: bool
    """
            If true, a new Dataset version is created after the removal of named reference;
            otherwise, no new version is created for a Dataset.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddNamedReferenceToDatasets(self, AddNamedReferenceIn: list[AddNamedReferenceToDatasetInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RemoveNamedReferenceFromDataset2(self, RemoveNamedReferenceIn: list[RemoveNamedReferenceFromDataset]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

