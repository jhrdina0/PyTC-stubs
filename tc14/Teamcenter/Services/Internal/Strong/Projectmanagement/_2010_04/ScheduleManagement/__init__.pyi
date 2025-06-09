import System
import Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement
import Teamcenter.Services.Internal.Strong.Projectmanagement._2009_10.ScheduleManagement
import typing

class TranslationModelMetaData:
    def __init__(self, ) -> None: ...
    ModelClass: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2009_10.ScheduleManagement.TranslationModelClass]
    SubMasterRelationship: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement.SubMasterMetaData]

class TranslationDataContainer:
    def __init__(self, ) -> None: ...
    Schedules: Teamcenter.Services.Internal.Strong.Projectmanagement._2009_10.ScheduleManagement.TranslationSchedules
    ModelMetaData: TranslationModelMetaData
    Preferences: Teamcenter.Services.Internal.Strong.Projectmanagement._2009_10.ScheduleManagement.TranslationPreferences
    RequestData: Teamcenter.Services.Internal.Strong.Projectmanagement._2009_10.ScheduleManagement.TranslationDataRequest

class ScheduleManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def TranslateFour(self, ScheduleUid: str) -> TranslationDataContainer: ...

