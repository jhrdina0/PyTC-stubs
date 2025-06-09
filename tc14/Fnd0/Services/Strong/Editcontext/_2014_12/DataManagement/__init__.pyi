import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SetEditContext(self, Context: Teamcenter.Soa.Client.Model.Strong.Fnd0EditContext, Objects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             If input parameter "context" is not null, the SOA response will contain the input
             Business Objects configured with the configuration parameter belonging to the input
             context. If any of the input Business Objects are not POM Revisable, they will be
             returned without configuration parameter. The Business Objects will be added to the
             Plain Objects array in ServiceData.
             
             If input parameter "context" is null, the input Business Objects will be configured
             for Public edits and returned in the SOA response.
             

Use Cases:

             This operation will enable the user to enter or exit edit mode and subsequently save
             the edits as Private Edits.
             

Teamcenter Component:

             Edit Context - Teamcenter Component for Edit Context.
             
        :param Context: 
                         A context containing a configuration parameter that is used to configure the input
                         Business Objects.
             
        :param Objects: 
                         The array of objects to be configured for edit.
             
        :return: 
        """
        ...

