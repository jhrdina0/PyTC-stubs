import System
import Teamcenter.Services.Internal.Strong.Projectmanagement._2009_10.ScheduleManagement
import Teamcenter.Services.Internal.Strong.Projectmanagement._2011_06.ScheduleManagement
import typing

class TranslatorResponseScheduleModifyContainer:
    def __init__(self, ) -> None: ...
    TranslatorResponseScheduleModifyContainerSub: list[TranslatorResponseScheduleModifyContainerSub]

class TranslatorResponseScheduleModifyContainerSub:
    def __init__(self, ) -> None: ...
    ScheduleUid: str
    ScheduleModifyContainer: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2011_06.ScheduleManagement.ScheduleModifyContainer]
    TranslatorExceptions: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2009_10.ScheduleManagement.TranslatorException]

class ScheduleManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def TranslateFive(self, ScheduleUid: str) -> TranslatorResponseScheduleModifyContainer: ...

