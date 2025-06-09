import Teamcenter.Soa.Client.Model
import typing

class ImportInput:
    """
    Input for importManufacturingFeatures
    """
    def __init__(self, ) -> None: ...
    FileName: str
    """The unique name of the PLMXML File in the transient volume."""
    Root: Teamcenter.Soa.Client.Model.ModelObject
    """
            The root object (in the structure to which we import the data). The root is always
            a BOMLine that corresponds to an item in the product structure.
            """

class ImportResponse:
    """
    The output of importManufaturingFeatures
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data"""
    LogFileFullPath: str
    """The full path of the log file (created by the import)."""

class ImportExport:
    """
    Interface ImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ImportManufaturingFeatures(self, Input: ImportInput) -> ImportResponse:
        """    imports MFGs from a given PLMXML file to TC.
        :param Input: 
                         The input contains the PLMXML file and the root of the structure to which the data
                         should be imported.
             
        :return: return a path to the log file and a ServiceData that contains errors
        """
        ...

