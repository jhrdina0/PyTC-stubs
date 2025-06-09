import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ObjectsICEInfo:
    """
    A structure to hold BOMLine or the MECfgLine component and their corresponding
ICE.
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """Business object (e.g. BOMLine, MECfgLine) for which the list of ICE are mapped with."""
    Ices: list[Teamcenter.Soa.Client.Model.Strong.IncrementalChangeElement]
    """The list of structural ICE elements for the given business object."""

class IncrementalChange:
    """
    Interface IncrementalChange
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def RemoveIncrementalChanges(self, ListOfObjects: list[ObjectsICEInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes the list of Incremental Change Elements (ICE) on the given
             BOMLine or the MECfgLine.
             

Teamcenter Component:

             Incremental Change - An incremental change collects a number of structure changes
             to a component such as add or remove of components or changes to attachments (data).
             Incremental change is an alternative to revision-based effectivity configuration.
             
        :param ListOfObjects: 
                         A list of BOMLine or the MECfgLine component and their corresponding ICE.
             
        :return: For successfully deleted ICEs, corresponding business object will be sent back in
             the ServiceData lists of updated object. If an invalid business object is detected,
             72035 is returned as a partial error with the corresponding business object. If an
             ICE does not affect the corresponding BOMLine, 46000 is returned as a partial error.
             Similarly, if an ICE does not affect the corresponding MECfgLine, 200165 is returned
             as a partial error.
        """
        ...

