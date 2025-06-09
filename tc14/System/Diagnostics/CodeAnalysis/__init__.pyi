import System

import System

import System

import System

import System

import System

import System
import typing

import System
import typing

import System
import typing

import System
import typing

import System
import typing

import System
import typing

import System
import typing

import System

import System

import System

import System

import System

import System

from System import Attribute, Boolean, String, Void

from System import Attribute, Boolean, String, Void

from System import Attribute, Boolean

from System import Attribute, Boolean

from System import *

from System import *

from System import *

from System import *

from System import *

from System import *

from System import *

from System import *

from System import *

from System import *

from __future__ import annotations

from typing import Tuple

from System import Attribute
from System import Guid
from System import IntPtr
from System import Type
from System.Runtime.InteropServices import _Attribute

class ExcludeFromCodeCoverageAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SuppressMessageAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, category: str, checkId: str):
        """

        :param category:
        :param checkId:
        """
    @property
    def Category(self) -> str:
        """

        :return:
        """
    @property
    def CheckId(self) -> str:
        """

        :return:
        """
    @property
    def Justification(self) -> str:
        """

        :return:
        """
    @Justification.setter
    def Justification(self, value: str) -> None: ...
    @property
    def MessageId(self) -> str:
        """

        :return:
        """
    @MessageId.setter
    def MessageId(self, value: str) -> None: ...
    @property
    def Scope(self) -> str:
        """

        :return:
        """
    @Scope.setter
    def Scope(self, value: str) -> None: ...
    @property
    def Target(self) -> str:
        """

        :return:
        """
    @Target.setter
    def Target(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    pass

    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

    pass

    pass

    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class ConstructorHandling(Enum):
    Default = 0
    AllowNonPublicDefaultConstructor = 1

class DateFormatHandling(Enum):
    IsoDateFormat = 0
    MicrosoftDateFormat = 1

class DateParseHandling(Enum):
    None = 0
    DateTime = 1
    DateTimeOffset = 2

class DateTimeZoneHandling(Enum):
    Local = 0
    Utc = 1
    Unspecified = 2
    RoundtripKind = 3

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class ConstructorHandling(Enum):
    Default = 0
    AllowNonPublicDefaultConstructor = 1

class DateFormatHandling(Enum):
    IsoDateFormat = 0
    MicrosoftDateFormat = 1

class DateParseHandling(Enum):
    None = 0
    DateTime = 1
    DateTimeOffset = 2

class DateTimeZoneHandling(Enum):
    Local = 0
    Utc = 1
    Unspecified = 2
    RoundtripKind = 3

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class ConstructorHandling(Enum):
    Default = 0
    AllowNonPublicDefaultConstructor = 1

class DateFormatHandling(Enum):
    IsoDateFormat = 0
    MicrosoftDateFormat = 1

class DateParseHandling(Enum):
    None = 0
    DateTime = 1
    DateTimeOffset = 2

class DateTimeZoneHandling(Enum):
    Local = 0
    Utc = 1
    Unspecified = 2
    RoundtripKind = 3

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: Boolean
    def get_ReturnValue(self) -> Boolean: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: Boolean
    def get_ParameterValue(self) -> Boolean: ...

class ConstructorHandling(Enum):
    Default = 0
    AllowNonPublicDefaultConstructor = 1

class DateFormatHandling(Enum):
    IsoDateFormat = 0
    MicrosoftDateFormat = 1

class DateParseHandling(Enum):
    None = 0
    DateTime = 1
    DateTimeOffset = 2

class DateTimeZoneHandling(Enum):
    Local = 0
    Utc = 1
    Unspecified = 2
    RoundtripKind = 3

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: String
    CheckId: String
    Scope: String
    Target: String
    MessageId: String
    Justification: String
    def get_Category(self) -> String: ...
    def get_CheckId(self) -> String: ...
    def get_Scope(self) -> String: ...
    def set_Scope(value: String) -> Void: ...
    def get_Target(self) -> String: ...
    def set_Target(value: String) -> Void: ...
    def get_MessageId(self) -> String: ...
    def set_MessageId(value: String) -> Void: ...
    def get_Justification(self) -> String: ...
    def set_Justification(value: String) -> Void: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: Boolean
    def get_ReturnValue(self) -> Boolean: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: Boolean
    def get_ParameterValue(self) -> Boolean: ...

class ConstructorHandling(Enum):
    Default = 0
    AllowNonPublicDefaultConstructor = 1

class DateFormatHandling(Enum):
    IsoDateFormat = 0
    MicrosoftDateFormat = 1

class DateParseHandling(Enum):
    None = 0
    DateTime = 1
    DateTimeOffset = 2

class DateTimeZoneHandling(Enum):
    Local = 0
    Utc = 1
    Unspecified = 2
    RoundtripKind = 3

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: String
    CheckId: String
    Scope: String
    Target: String
    MessageId: String
    Justification: String
    def get_Category(self) -> String: ...
    def get_CheckId(self) -> String: ...
    def get_Scope(self) -> String: ...
    def set_Scope(value: String) -> Void: ...
    def get_Target(self) -> String: ...
    def set_Target(value: String) -> Void: ...
    def get_MessageId(self) -> String: ...
    def set_MessageId(value: String) -> Void: ...
    def get_Justification(self) -> String: ...
    def set_Justification(value: String) -> Void: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: Boolean
    def get_ReturnValue(self) -> Boolean: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: Boolean
    def get_ParameterValue(self) -> Boolean: ...

class ConstructorHandling(Enum):
    Default = 0
    AllowNonPublicDefaultConstructor = 1

class DateFormatHandling(Enum):
    IsoDateFormat = 0
    MicrosoftDateFormat = 1

class DateParseHandling(Enum):
    None = 0
    DateTime = 1
    DateTimeOffset = 2

class DateTimeZoneHandling(Enum):
    Local = 0
    Utc = 1
    Unspecified = 2
    RoundtripKind = 3

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: String
    CheckId: String
    Scope: String
    Target: String
    MessageId: String
    Justification: String
    def get_Category(self) -> String: ...
    def get_CheckId(self) -> String: ...
    def get_Scope(self) -> String: ...
    def set_Scope(value: String) -> Void: ...
    def get_Target(self) -> String: ...
    def set_Target(value: String) -> Void: ...
    def get_MessageId(self) -> String: ...
    def set_MessageId(value: String) -> Void: ...
    def get_Justification(self) -> String: ...
    def set_Justification(value: String) -> Void: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: Boolean
    def get_ReturnValue(self) -> Boolean: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: Boolean
    def get_ParameterValue(self) -> Boolean: ...

class ConstructorHandling(Enum):
    Default = 0
    AllowNonPublicDefaultConstructor = 1

class DateFormatHandling(Enum):
    IsoDateFormat = 0
    MicrosoftDateFormat = 1

class DateParseHandling(Enum):
    None = 0
    DateTime = 1
    DateTimeOffset = 2

class DateTimeZoneHandling(Enum):
    Local = 0
    Utc = 1
    Unspecified = 2
    RoundtripKind = 3

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: String
    CheckId: String
    Scope: String
    Target: String
    MessageId: String
    Justification: String
    def get_Category(self) -> String: ...
    def get_CheckId(self) -> String: ...
    def get_Scope(self) -> String: ...
    def set_Scope(value: String) -> Void: ...
    def get_Target(self) -> String: ...
    def set_Target(value: String) -> Void: ...
    def get_MessageId(self) -> String: ...
    def set_MessageId(value: String) -> Void: ...
    def get_Justification(self) -> String: ...
    def set_Justification(value: String) -> Void: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: Boolean
    def get_ReturnValue(self) -> Boolean: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: Boolean
    def get_ParameterValue(self) -> Boolean: ...

class ConstructorHandling(Enum):
    Default = 0
    AllowNonPublicDefaultConstructor = 1

class DateFormatHandling(Enum):
    IsoDateFormat = 0
    MicrosoftDateFormat = 1

class DateParseHandling(Enum):
    None = 0
    DateTime = 1
    DateTimeOffset = 2

class DateTimeZoneHandling(Enum):
    Local = 0
    Utc = 1
    Unspecified = 2
    RoundtripKind = 3

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: String
    CheckId: String
    Scope: String
    Target: String
    MessageId: String
    Justification: String
    def get_Category(self) -> String: ...
    def get_CheckId(self) -> String: ...
    def get_Scope(self) -> String: ...
    def set_Scope(self, value: String) -> Void: ...
    def get_Target(self) -> String: ...
    def set_Target(self, value: String) -> Void: ...
    def get_MessageId(self) -> String: ...
    def set_MessageId(self, value: String) -> Void: ...
    def get_Justification(self) -> String: ...
    def set_Justification(self, value: String) -> Void: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: Boolean
    def get_ReturnValue(self) -> Boolean: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: Boolean
    def get_ParameterValue(self) -> Boolean: ...

class ConstructorHandling(Enum):
    Default = 0
    AllowNonPublicDefaultConstructor = 1

class DateFormatHandling(Enum):
    IsoDateFormat = 0
    MicrosoftDateFormat = 1

class DateParseHandling(Enum):
    None = 0
    DateTime = 1
    DateTimeOffset = 2

class DateTimeZoneHandling(Enum):
    Local = 0
    Utc = 1
    Unspecified = 2
    RoundtripKind = 3

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: String
    CheckId: String
    Scope: String
    Target: String
    MessageId: String
    Justification: String
    def get_Category(self) -> String: ...
    def get_CheckId(self) -> String: ...
    def get_Scope(self) -> String: ...
    def set_Scope(self, value: String) -> Void: ...
    def get_Target(self) -> String: ...
    def set_Target(self, value: String) -> Void: ...
    def get_MessageId(self) -> String: ...
    def set_MessageId(self, value: String) -> Void: ...
    def get_Justification(self) -> String: ...
    def set_Justification(self, value: String) -> Void: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: Boolean
    def get_ReturnValue(self) -> Boolean: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: Boolean
    def get_ParameterValue(self) -> Boolean: ...

class ConstructorHandling(Enum):
    Default = 0
    AllowNonPublicDefaultConstructor = 1

class DateFormatHandling(Enum):
    IsoDateFormat = 0
    MicrosoftDateFormat = 1

class DateParseHandling(Enum):
    None = 0
    DateTime = 1
    DateTimeOffset = 2

class DateTimeZoneHandling(Enum):
    Local = 0
    Utc = 1
    Unspecified = 2
    RoundtripKind = 3

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: String
    CheckId: String
    Scope: String
    Target: String
    MessageId: String
    Justification: String
    def get_Category(self) -> String: ...
    def get_CheckId(self) -> String: ...
    def get_Scope(self) -> String: ...
    def set_Scope(self, value: String) -> Void: ...
    def get_Target(self) -> String: ...
    def set_Target(self, value: String) -> Void: ...
    def get_MessageId(self) -> String: ...
    def set_MessageId(self, value: String) -> Void: ...
    def get_Justification(self) -> String: ...
    def set_Justification(self, value: String) -> Void: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: Boolean
    def get_ReturnValue(self) -> Boolean: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: Boolean
    def get_ParameterValue(self) -> Boolean: ...

class ConstructorHandling(Enum):
    Default = 0
    AllowNonPublicDefaultConstructor = 1

class DateFormatHandling(Enum):
    IsoDateFormat = 0
    MicrosoftDateFormat = 1

class DateParseHandling(Enum):
    None = 0
    DateTime = 1
    DateTimeOffset = 2

class DateTimeZoneHandling(Enum):
    Local = 0
    Utc = 1
    Unspecified = 2
    RoundtripKind = 3

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: String
    CheckId: String
    Scope: String
    Target: String
    MessageId: String
    Justification: String
    def get_Category(self) -> String: ...
    def get_CheckId(self) -> String: ...
    def get_Scope(self) -> String: ...
    def set_Scope(self, value: String) -> Void: ...
    def get_Target(self) -> String: ...
    def set_Target(self, value: String) -> Void: ...
    def get_MessageId(self) -> String: ...
    def set_MessageId(self, value: String) -> Void: ...
    def get_Justification(self) -> String: ...
    def set_Justification(self, value: String) -> Void: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: Boolean
    def get_ReturnValue(self) -> Boolean: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: Boolean
    def get_ParameterValue(self) -> Boolean: ...

class ConstructorHandling(Enum):
    Default = 0
    AllowNonPublicDefaultConstructor = 1

class DateFormatHandling(Enum):
    IsoDateFormat = 0
    MicrosoftDateFormat = 1

class DateParseHandling(Enum):
    None = 0
    DateTime = 1
    DateTimeOffset = 2

class DateTimeZoneHandling(Enum):
    Local = 0
    Utc = 1
    Unspecified = 2
    RoundtripKind = 3

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: String
    CheckId: String
    Scope: String
    Target: String
    MessageId: String
    Justification: String
    def get_Category(self) -> String: ...
    def get_CheckId(self) -> String: ...
    def get_Scope(self) -> String: ...
    def set_Scope(self, value: String) -> Void: ...
    def get_Target(self) -> String: ...
    def set_Target(self, value: String) -> Void: ...
    def get_MessageId(self) -> String: ...
    def set_MessageId(self, value: String) -> Void: ...
    def get_Justification(self) -> String: ...
    def set_Justification(self, value: String) -> Void: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: Boolean
    def get_ReturnValue(self) -> Boolean: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: Boolean
    def get_ParameterValue(self) -> Boolean: ...

class ConstructorHandling(Enum):
    Default = 0
    AllowNonPublicDefaultConstructor = 1

class DateFormatHandling(Enum):
    IsoDateFormat = 0
    MicrosoftDateFormat = 1

class DateParseHandling(Enum):
    None = 0
    DateTime = 1
    DateTimeOffset = 2

class DateTimeZoneHandling(Enum):
    Local = 0
    Utc = 1
    Unspecified = 2
    RoundtripKind = 3

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: String
    CheckId: String
    Scope: String
    Target: String
    MessageId: String
    Justification: String
    def get_Category(self) -> String: ...
    def get_CheckId(self) -> String: ...
    def get_Scope(self) -> String: ...
    def set_Scope(self, value: String) -> Void: ...
    def get_Target(self) -> String: ...
    def set_Target(self, value: String) -> Void: ...
    def get_MessageId(self) -> String: ...
    def set_MessageId(self, value: String) -> Void: ...
    def get_Justification(self) -> String: ...
    def set_Justification(self, value: String) -> Void: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: Boolean
    def get_ReturnValue(self) -> Boolean: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: Boolean
    def get_ParameterValue(self) -> Boolean: ...

class ConstructorHandling(Enum):
    Default = 0
    AllowNonPublicDefaultConstructor = 1

class DateFormatHandling(Enum):
    IsoDateFormat = 0
    MicrosoftDateFormat = 1

class DateParseHandling(Enum):
    None = 0
    DateTime = 1
    DateTimeOffset = 2

class DateTimeZoneHandling(Enum):
    Local = 0
    Utc = 1
    Unspecified = 2
    RoundtripKind = 3

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: String
    CheckId: String
    Scope: String
    Target: String
    MessageId: String
    Justification: String
    def get_Category(self) -> String: ...
    def get_CheckId(self) -> String: ...
    def get_Scope(self) -> String: ...
    def set_Scope(self, value: String) -> Void: ...
    def get_Target(self) -> String: ...
    def set_Target(self, value: String) -> Void: ...
    def get_MessageId(self) -> String: ...
    def set_MessageId(self, value: String) -> Void: ...
    def get_Justification(self) -> String: ...
    def set_Justification(self, value: String) -> Void: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: Boolean
    def get_ReturnValue(self) -> Boolean: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: Boolean
    def get_ParameterValue(self) -> Boolean: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: String
    CheckId: String
    Scope: String
    Target: String
    MessageId: String
    Justification: String
    def get_Category(self) -> String: ...
    def get_CheckId(self) -> String: ...
    def get_Scope(self) -> String: ...
    def set_Scope(self, value: String) -> Void: ...
    def get_Target(self) -> String: ...
    def set_Target(self, value: String) -> Void: ...
    def get_MessageId(self) -> String: ...
    def set_MessageId(self, value: String) -> Void: ...
    def get_Justification(self) -> String: ...
    def set_Justification(self, value: String) -> Void: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: Boolean
    def get_ReturnValue(self) -> Boolean: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: Boolean
    def get_ParameterValue(self) -> Boolean: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: String
    CheckId: String
    Scope: String
    Target: String
    MessageId: String
    Justification: String
    def get_Category(self) -> String: ...
    def get_CheckId(self) -> String: ...
    def get_Scope(self) -> String: ...
    def set_Scope(self, value: String) -> Void: ...
    def get_Target(self) -> String: ...
    def set_Target(self, value: String) -> Void: ...
    def get_MessageId(self) -> String: ...
    def set_MessageId(self, value: String) -> Void: ...
    def get_Justification(self) -> String: ...
    def set_Justification(self, value: String) -> Void: ...

class NotNullAttribute(Attribute):
    pass

class NotNullWhenAttribute(Attribute):
    ReturnValue: Boolean
    def get_ReturnValue(self) -> Boolean: ...

class MaybeNullAttribute(Attribute):
    pass

class AllowNullAttribute(Attribute):
    pass

class DoesNotReturnIfAttribute(Attribute):
    ParameterValue: Boolean
    def get_ParameterValue(self) -> Boolean: ...

class UnconditionalSuppressMessageAttribute(Attribute):
    Category: String
    CheckId: String
    Scope: String
    Target: String
    MessageId: String
    Justification: String
    def get_Category(self) -> String: ...
    def get_CheckId(self) -> String: ...
    def get_Scope(self) -> String: ...
    def set_Scope(self, value: String) -> Void: ...
    def get_Target(self) -> String: ...
    def set_Target(self, value: String) -> Void: ...
    def get_MessageId(self) -> String: ...
    def set_MessageId(self, value: String) -> Void: ...
    def get_Justification(self) -> String: ...
    def set_Justification(self, value: String) -> Void: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: System.Boolean
    def get_ReturnValue(self) -> System.Boolean: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: System.Boolean
    def get_ParameterValue(self) -> System.Boolean: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: System.String
    CheckId: System.String
    Scope: System.String
    Target: System.String
    MessageId: System.String
    Justification: System.String
    def get_Category(self) -> System.String: ...
    def get_CheckId(self) -> System.String: ...
    def get_Scope(self) -> System.String: ...
    def set_Scope(self, value: System.String) -> System.Void: ...
    def get_Target(self) -> System.String: ...
    def set_Target(self, value: System.String) -> System.Void: ...
    def get_MessageId(self) -> System.String: ...
    def set_MessageId(self, value: System.String) -> System.Void: ...
    def get_Justification(self) -> System.String: ...
    def set_Justification(self, value: System.String) -> System.Void: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: System.Boolean
    def get_ReturnValue(self) -> System.Boolean: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: System.Boolean
    def get_ParameterValue(self) -> System.Boolean: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: System.Boolean
    def get_ReturnValue(self) -> System.Boolean: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: System.Boolean
    def get_ParameterValue(self) -> System.Boolean: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: System.Boolean
    def get_ReturnValue(self) -> System.Boolean: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: System.Boolean
    def get_ParameterValue(self) -> System.Boolean: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: System.Boolean
    def get_ReturnValue(self) -> System.Boolean: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: System.Boolean
    def get_ParameterValue(self) -> System.Boolean: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: System.Boolean
    def get_ReturnValue(self) -> System.Boolean: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: System.Boolean
    def get_ParameterValue(self) -> System.Boolean: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: System.String
    CheckId: System.String
    Scope: System.String
    Target: System.String
    MessageId: System.String
    Justification: System.String
    def get_Category(self) -> System.String: ...
    def get_CheckId(self) -> System.String: ...
    def get_Scope(self) -> System.String: ...
    def set_Scope(self, value: System.String) -> System.Void: ...
    def get_Target(self) -> System.String: ...
    def set_Target(self, value: System.String) -> System.Void: ...
    def get_MessageId(self) -> System.String: ...
    def set_MessageId(self, value: System.String) -> System.Void: ...
    def get_Justification(self) -> System.String: ...
    def set_Justification(self, value: System.String) -> System.Void: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: System.Boolean
    def get_ReturnValue(self) -> System.Boolean: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: System.Boolean
    def get_ParameterValue(self) -> System.Boolean: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: System.String
    CheckId: System.String
    Scope: System.String
    Target: System.String
    MessageId: System.String
    Justification: System.String
    def get_Category(self) -> System.String: ...
    def get_CheckId(self) -> System.String: ...
    def get_Scope(self) -> System.String: ...
    def set_Scope(self, value: System.String) -> System.Void: ...
    def get_Target(self) -> System.String: ...
    def set_Target(self, value: System.String) -> System.Void: ...
    def get_MessageId(self) -> System.String: ...
    def set_MessageId(self, value: System.String) -> System.Void: ...
    def get_Justification(self) -> System.String: ...
    def set_Justification(self, value: System.String) -> System.Void: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(self, value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(self, value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(self, value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(self, value: str) -> None: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(self, value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(self, value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(self, value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(self, value: str) -> None: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(self, value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(self, value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(self, value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(self, value: str) -> None: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(self, value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(self, value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(self, value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(self, value: str) -> None: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(self, value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(self, value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(self, value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(self, value: str) -> None: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    @staticmethod
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    @staticmethod
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    @staticmethod
    def get_Category(self) -> str: ...
    @staticmethod
    def get_CheckId(self) -> str: ...
    @staticmethod
    def get_Scope(self) -> str: ...
    @staticmethod
    def set_Scope(value: str) -> None: ...
    @staticmethod
    def get_Target(self) -> str: ...
    @staticmethod
    def set_Target(value: str) -> None: ...
    @staticmethod
    def get_MessageId(self) -> str: ...
    @staticmethod
    def set_MessageId(value: str) -> None: ...
    @staticmethod
    def get_Justification(self) -> str: ...
    @staticmethod
    def set_Justification(value: str) -> None: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(self, value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(self, value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(self, value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(self, value: str) -> None: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(self, value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(self, value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(self, value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(self, value: str) -> None: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(self, value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(self, value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(self, value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(self, value: str) -> None: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(self, value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(self, value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(self, value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(self, value: str) -> None: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(self, value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(self, value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(self, value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(self, value: str) -> None: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(self, value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(self, value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(self, value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(self, value: str) -> None: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(self, value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(self, value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(self, value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(self, value: str) -> None: ...

class NotNullAttribute(System.Attribute):
    pass

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    pass

class AllowNullAttribute(System.Attribute):
    pass

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(self, value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(self, value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(self, value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(self, value: str) -> None: ...

class NotNullAttribute(System.Attribute):
    def __init__(self, ) -> NotNullAttribute: ...

class NotNullWhenAttribute(System.Attribute):
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...
    def __init__(self, returnValue: bool) -> NotNullWhenAttribute: ...

class MaybeNullAttribute(System.Attribute):
    def __init__(self, ) -> MaybeNullAttribute: ...

class AllowNullAttribute(System.Attribute):
    def __init__(self, ) -> AllowNullAttribute: ...

class DoesNotReturnIfAttribute(System.Attribute):
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...
    def __init__(self, parameterValue: bool) -> DoesNotReturnIfAttribute: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(self, value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(self, value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(self, value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(self, value: str) -> None: ...
    def __init__(self, category: str, checkId: str) -> UnconditionalSuppressMessageAttribute: ...

class NotNullAttribute(System.Attribute):
    def __init__(self, ) -> None: ...

class NotNullWhenAttribute(System.Attribute):
    def __init__(self, returnValue: bool) -> None: ...
    ReturnValue: bool
    def get_ReturnValue(self) -> bool: ...

class MaybeNullAttribute(System.Attribute):
    def __init__(self, ) -> None: ...

class AllowNullAttribute(System.Attribute):
    def __init__(self, ) -> None: ...

class DoesNotReturnIfAttribute(System.Attribute):
    def __init__(self, parameterValue: bool) -> None: ...
    ParameterValue: bool
    def get_ParameterValue(self) -> bool: ...

class UnconditionalSuppressMessageAttribute(System.Attribute):
    def __init__(self, category: str, checkId: str) -> None: ...
    Category: str
    CheckId: str
    Scope: str
    Target: str
    MessageId: str
    Justification: str
    def get_Category(self) -> str: ...
    def get_CheckId(self) -> str: ...
    def get_Scope(self) -> str: ...
    def set_Scope(self, value: str) -> None: ...
    def get_Target(self) -> str: ...
    def set_Target(self, value: str) -> None: ...
    def get_MessageId(self) -> str: ...
    def set_MessageId(self, value: str) -> None: ...
    def get_Justification(self) -> str: ...
    def set_Justification(self, value: str) -> None: ...

