import Teamcenter.Soa.Client.Model
import typing

class ProcessAttrExchangeConfigInput:
    def __init__(self, ) -> None: ...
    LogicalObjectType: Teamcenter.Soa.Client.Model.ModelObject
    PropertyData: list[PropertyData]

class PropertyData:
    def __init__(self, ) -> None: ...
    PresentedPropertyName: str
    Action: str

class AttributeExchange:
    def __init__(self , *args: typing.Any) -> None: ...
    def ProcessAttrExchangeConfigurations(self, ProcessAttrExchConfInputInfo: ProcessAttrExchangeConfigInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...

