import Teamcenter.Soa.Client.Model
import typing

class AdvancedImportInput:
    """
    Advanced Input for importing the manufacturing features.
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """
            A BOMLine object in the product structure. Under this object the connected parts
            of imported manufacturing features are searched.
            """
    Content: list[ImportScope]
    """
            List of detail inputs. The detail input elaborates about the container, the import
            mode and the input PLMXML file.
            """

class AdvancedImportResponse:
    """
    The response of PLMXML import of the manufacturing features.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The service data.The error conditions and the corresponding error codes are as listed
            below.      200373 Import is tried to be done from an incomplete PLMXML file.
            200374 The preference MEImportMFGsManufacturingFeatureIdAttributeName does not
            have any value.      200376 The preference MEImportMFGsManufacturingFeatureIdAttributeName
            has incorrect value.      200375 The preference MEImportMFGsManufacturingFeatureIdAttributeName
            does not have any value.      200377 The preference MEImportMFGsManufacturingFeatureIdAttributeName
            has incorrect value.      200xxx Import has failed for a container.
            """
    LogFileName: str
    """The name of the generated log file."""
    LogFileTicket: str
    """The fms ticket for the transient file that captures the log of import."""

class ImportScope:
    """
    The detail input for importing manufacturing features.
    """
    def __init__(self, ) -> None: ...
    FileName: str
    """The full path of the PLMXML file"""
    Container: Teamcenter.Soa.Client.Model.ModelObject
    """The container under which manufacturing features are to be imported."""
    ImportMode: str
    """
            The mode of import. The possible values of the import mode are as follows.      keepExistingFeatures
            - The existing discrete manufacturing features (MFGs)under the container should not
            be deleted.      refreshWholeContainer - The existing discrete manufacturing features
            under the container may be deleted.
            """

class ImportExport:
    """
    Interface ImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ImportManufacturingFeatures(self, Input: AdvancedImportInput) -> AdvancedImportResponse:
        """    
             This service operation imports the discrete manufacturing features (MFGs) from a
             PLMXML file into a target product structure in Teamcenter.        This operation
             takes a scope line (container) as additional input and imports the MFGs under the
             container.        Moreover, it takes the import mode as input which allows deciding
             whether MFGs already present under the chosen container should be deleted or not.
             
        :param Input: 
                         Input for PLMXML import of manufacturing features.
             
        :return: Response of the import functionality.        The response contains the FMS file ticket
             of the log file, the log file name and a ServiceData that contains errors.
             The error conditions and the corresponding error codes are as listed below.
             200373 Import is tried to be done from an incomplete PLMXML file.        200374
             The preference MEImportMFGsManufacturingFeatureIdAttributeName does not have any
             value.        200376 The preference MEImportMFGsManufacturingFeatureIdAttributeName
             has incorrect value.        200375 The preference MEImportMFGsManufacturingFeatureIdAttributeName
             does not have any value.        200377 The preference MEImportMFGsManufacturingFeatureIdAttributeName
             has incorrect value.        200xxx Import has failed for a container.
        """
        ...

