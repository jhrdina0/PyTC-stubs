import System
import Teamcenter.Services.Internal.Strong.Projectmanagement._2007_01.ScheduleManagement
import Teamcenter.Services.Internal.Strong.Projectmanagement._2007_06.ScheduleManagement
import Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement
import Teamcenter.Services.Strong.Projectmanagement._2009_10.ScheduleManagement
import Teamcenter.Soa.Client.Model
import typing

class KeyValuePair:
    def __init__(self, ) -> None: ...
    Key: int
    Value: str

class TranslationSchedules:
    def __init__(self, ) -> None: ...
    TranslationDataSchedule: list[TranslationDataSchedule]

class TranslationModelMetaData:
    def __init__(self, ) -> None: ...
    ModelClass: list[TranslationModelClass]

class TranslationPreferences:
    def __init__(self, ) -> None: ...
    Preferences: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2007_06.ScheduleManagement.StringValContainer]

class TranslationDataRequest:
    def __init__(self, ) -> None: ...
    GenericContainers: list[Teamcenter.Services.Strong.Projectmanagement._2009_10.ScheduleManagement.GenericAttributesContainer]
    ScheduleModifyContainer: list[Teamcenter.Services.Strong.Projectmanagement._2009_10.ScheduleManagement.ScheduleModifyContainer]

class TranslationDataContainer:
    def __init__(self, ) -> None: ...
    Schedules: TranslationSchedules
    ModelMetaData: TranslationModelMetaData
    Preferences: TranslationPreferences
    RequestData: TranslationDataRequest

class TranslationDataSchedule:
    def __init__(self, ) -> None: ...
    DataObjects: list[Teamcenter.Soa.Client.Model.ModelObject]

class TranslationModelClass:
    def __init__(self, ) -> None: ...
    Attribute: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2007_01.ScheduleManagement.StringValueContainer]
    Name: str
    ParentClassName: str

class TranslatorException:
    def __init__(self, ) -> None: ...
    ObjectUid: str
    Operation: int
    ErrorNumber: int
    ErrorSeverity: int
    ErrorString: str
    ParameterValues: list[KeyValuePair]

class TranslatorResponseContainer:
    def __init__(self, ) -> None: ...
    TranslatorResponseContainerSub: list[TranslatorResponseContainerSub]

class TranslatorResponseContainerSub:
    def __init__(self, ) -> None: ...
    ScheduleUid: str
    GenericAttributesContainer: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement.GenericAttributesContainer]
    TranslatorExceptions: list[TranslatorException]

class TranslatorResponseScheduleModifyContainer:
    def __init__(self, ) -> None: ...
    TranslatorResponseScheduleModifyContainerSub: list[TranslatorResponseScheduleModifyContainerSub]

class TranslatorResponseScheduleModifyContainerSub:
    def __init__(self, ) -> None: ...
    ScheduleUid: str
    ScheduleModifyContainer: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement.ScheduleModifyContainer]
    TranslatorExceptions: list[TranslatorException]

class ScheduleManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def TranslateOne(self, ScheduleUid: str) -> TranslatorResponseContainer: ...
    def TranslateThree(self, ScheduleUid: str) -> TranslationDataContainer: ...
    def TranslateTwo(self, ScheduleUid: str) -> TranslatorResponseScheduleModifyContainer: ...

