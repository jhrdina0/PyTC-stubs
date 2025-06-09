import Imp0.Services.Strong.Labelmanagement._2021_06.LabelManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class LabelManagementRestBindingStub(LabelManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def UpdateLabelSystemPaths(self, LabelSystemPathsInput: list[Imp0.Services.Strong.Labelmanagement._2021_06.LabelManagement.LabelSystemPathInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class LabelManagementService:
    """
    
            This service provides integration of Teamcenter with Label Management Systems for
            Medical Devices.
            


Library Reference:

Imp0SoaLabelManagementStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> LabelManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def UpdateLabelSystemPaths(self, LabelSystemPathsInput: list[Imp0.Services.Strong.Labelmanagement._2021_06.LabelManagement.LabelSystemPathInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation updates the attribute imp0LSPath used to store the Label System Path
             of the business objects of type Imp0LabelDesignRevision, Pka0DigitalAssetRevision
             and Imd0MedDevIdfrRevision. Label System Path (LS Path) is the unique attribute
             assigned to the objects by the Label Management Systems, used for the labeling of
             the medical devices. Currently Teamcenter has integrations with "NiceLabel" and "PRISYM
             ID" Label Management Systems.
             

             When Teamcenter sends the digital assets of type Pka0DigitalAssetRevision
             object or label design of type Imp0LabelDesignRevision to the Label Management
             System as part of the integration, it receives the LS Path information of each
             of the objects as part of the response from the Label Management System. Digital
             assets like company logo, standard symbols like single use, recyclable, brand information,
             lot symbol are sent once to the Label Management System and used across the
             label designs of the different medical devices. The Label Management System
             recognizes the digital assets or an existing label design or an existing medical
             device identifier by the LS Path attribute of it.
             

             If the objects of type Imp0LabelDesignRevision, Pka0DigitalAssetRevision
             and Imd0MedDevIdfrRevision are released in Teamcenter, this operation can
             update the imp0LSPath attribute of them.
             

             This operation also updates "imp0LSPath" attribute of objects of type Imp0LabelDesignRevision,
             Pka0DigitalAssetRevision and Imd0MedDevIdfrRevision even if the objects
             are owned by a different group than that of the integration user.
             

Teamcenter Component:

             Teamcenter Integration for Label Management Systems - Solution to integrate Teamcenter
             with Label Management Software.
             
        :param LabelSystemPathsInput: 
                         A list containing UIDs of objects type: <b>Imp0LabelDesignRevision</b>, <b>Pka0DigitalAssetRevision</b>
                         and <b>Imd0MedDevIdfrRevision</b> and their <i>Label System Path</i> as stored by
                         the <i>Label Management System</i>.
             
        :return: 
        """
        ...

