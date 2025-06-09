import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class ChangeMinorConfigurationResponse:
    """
    Response from the changeMinorConfiguration operation. Returns reconfigured objects.
    """
    def __init__(self, ) -> None: ...
    TargetObjectMap: System.Collections.Hashtable
    """
            Map (business object / business object) with source object keys and (re-configured)
            target object values. If a source object is not revisable, the key (source object)
            and value (target object) will be the same. If a target object is not readable, not
            present at this Teamcenter site, or otherwise not available, the map will contain
            a key for the source object with a null value (target object). If a target object
            is logically deleted (as a POM-deleted minor revision), the map will contain a key
            for the source object with a null value (target object).
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            ServiceData for error and object information. Reconfigured objects are returned in
            the Plain object list.
            """

class ModelConfiguration:
    """
    Interface ModelConfiguration
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ChangeMinorConfiguration(self, TargetSample: Teamcenter.Soa.Client.Model.ModelObject, SourceObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> ChangeMinorConfigurationResponse:
        """    
             Change the minor configuration of each sourceObject
             to match the minor revision configuration of targetSample.
             

Use Cases:

             A user is viewing a historical minor revision of an object and wishes to display
             the latest minor revision. You call the changeMinorConfiguration service, passing
             in a targetSample of null and a sourceObjects array containing the historical minor
             revision.
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param TargetSample: 
                         Sample object, configured using the target minor configuration. If the sample object
                         is null, the "POM latest" target minor configuration will be used. See <b>Fnd0Cparam</b>.
             
        :param SourceObjects: 
                         A list of objects to re-configure. Both revisable and non-revisable objects are allowed.
             
        :return: 
        """
        ...

