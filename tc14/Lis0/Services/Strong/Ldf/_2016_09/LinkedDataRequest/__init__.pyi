import Lis0.Services.Strong.Ldf._2016_03.LinkedDataRequest
import typing

class LinkedDataRequest:
    """
    Interface LinkedDataRequest
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetLDFPropertiesRelationTypes(self, UidContextObject: str, Url: str, UidServiceProvider: str) -> Lis0.Services.Strong.Ldf._2016_03.LinkedDataRequest.PropertiesValueStructure:
        """    
             This Operation invokes the Rest Get call to remote site and fetches the property
             values for the remote linked object and find all the available relation types that
             the remote system object should be linked with given Teamcenter Context Object.
             

Teamcenter Component:

             Linked Data Framework - Component for Linked Data Framework (LDF)
             
        :param UidContextObject: 
                         The UID for primary Teamcenter Business Object associated to LDF Link, representing
                         remote object via Relation Object.
             
        :param Url: 
                         Example:-http://pnv6s282.net.plm.eds.com:8085/polarion/oslc/services/projects/TcLDFConnectorProject01/changeRequests/TcLDFConnectorProject01-529.
             
        :param UidServiceProvider: 
                         The UID of the Service Provider, (of type <b>Lis0ServiceProvider</b>) representing
                         remote site project container, defined in Teamcenter.
             
        :return: contains map "propMap" (string, string)
             representing property names and their values from the remote linked object.
        """
        ...

