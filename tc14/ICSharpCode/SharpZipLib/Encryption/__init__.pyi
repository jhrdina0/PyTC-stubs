import System
import System.IO
import System.Security.Cryptography
import System.Threading
import System.Threading.Tasks

class PkzipClassic(System.Security.Cryptography.SymmetricAlgorithm):
    @staticmethod
    def GenerateKeys(seed: list[System.Byte]) -> list[System.Byte]: ...

class PkzipClassicCryptoBase:
    def __init__(self, ) -> None: ...

class PkzipClassicEncryptCryptoTransform(PkzipClassicCryptoBase):
    CanReuseTransform: bool
    InputBlockSize: int
    OutputBlockSize: int
    CanTransformMultipleBlocks: bool
    def TransformFinalBlock(self, inputBuffer: list[System.Byte], inputOffset: int, inputCount: int) -> list[System.Byte]: ...
    def TransformBlock(self, inputBuffer: list[System.Byte], inputOffset: int, inputCount: int, outputBuffer: list[System.Byte], outputOffset: int) -> int: ...
    def get_CanReuseTransform(self) -> bool: ...
    def get_InputBlockSize(self) -> int: ...
    def get_OutputBlockSize(self) -> int: ...
    def get_CanTransformMultipleBlocks(self) -> bool: ...
    def Dispose(self) -> None: ...

class PkzipClassicDecryptCryptoTransform(PkzipClassicCryptoBase):
    CanReuseTransform: bool
    InputBlockSize: int
    OutputBlockSize: int
    CanTransformMultipleBlocks: bool
    def TransformFinalBlock(self, inputBuffer: list[System.Byte], inputOffset: int, inputCount: int) -> list[System.Byte]: ...
    def TransformBlock(self, inputBuffer: list[System.Byte], inputOffset: int, inputCount: int, outputBuffer: list[System.Byte], outputOffset: int) -> int: ...
    def get_CanReuseTransform(self) -> bool: ...
    def get_InputBlockSize(self) -> int: ...
    def get_OutputBlockSize(self) -> int: ...
    def get_CanTransformMultipleBlocks(self) -> bool: ...
    def Dispose(self) -> None: ...

class PkzipClassicManaged(PkzipClassic):
    def __init__(self, ) -> None: ...
    BlockSize: int
    LegalKeySizes: list[System.Security.Cryptography.KeySizes]
    LegalBlockSizes: list[System.Security.Cryptography.KeySizes]
    Key: list[System.Byte]
    def get_BlockSize(self) -> int: ...
    def set_BlockSize(self, value: int) -> None: ...
    def get_LegalKeySizes(self) -> list[System.Security.Cryptography.KeySizes]: ...
    def GenerateIV(self) -> None: ...
    def get_LegalBlockSizes(self) -> list[System.Security.Cryptography.KeySizes]: ...
    def get_Key(self) -> list[System.Byte]: ...
    def set_Key(self, value: list[System.Byte]) -> None: ...
    def GenerateKey(self) -> None: ...
    def CreateEncryptor(self, rgbKey: list[System.Byte], rgbIV: list[System.Byte]) -> System.Security.Cryptography.ICryptoTransform: ...
    def CreateDecryptor(self, rgbKey: list[System.Byte], rgbIV: list[System.Byte]) -> System.Security.Cryptography.ICryptoTransform: ...

class ZipAESStream(System.Security.Cryptography.CryptoStream):
    def __init__(self, stream: System.IO.Stream, transform: ZipAESTransform, mode: System.Security.Cryptography.CryptoStreamMode) -> None: ...
    def Read(self, buffer: list[System.Byte], offset: int, count: int) -> int: ...
    def ReadAsync(self, buffer: list[System.Byte], offset: int, count: int, cancellationToken: System.Threading.CancellationToken) -> list[int]: ...
    def Write(self, buffer: list[System.Byte], offset: int, count: int) -> None: ...

class ZipAESTransform:
    def __init__(self, key: str, saltBytes: list[System.Byte], blockSize: int, writeMode: bool) -> None: ...
    PwdVerifier: list[System.Byte]
    InputBlockSize: int
    OutputBlockSize: int
    CanTransformMultipleBlocks: bool
    CanReuseTransform: bool
    def TransformBlock(self, inputBuffer: list[System.Byte], inputOffset: int, inputCount: int, outputBuffer: list[System.Byte], outputOffset: int) -> int: ...
    def get_PwdVerifier(self) -> list[System.Byte]: ...
    def GetAuthCode(self) -> list[System.Byte]: ...
    def TransformFinalBlock(self, inputBuffer: list[System.Byte], inputOffset: int, inputCount: int) -> list[System.Byte]: ...
    def get_InputBlockSize(self) -> int: ...
    def get_OutputBlockSize(self) -> int: ...
    def get_CanTransformMultipleBlocks(self) -> bool: ...
    def get_CanReuseTransform(self) -> bool: ...
    def Dispose(self) -> None: ...

class IncrementalHash(System.Security.Cryptography.HMACSHA1):
    def __init__(self, key: list[System.Byte]) -> None: ...
    @staticmethod
    def CreateHMAC(n: str, key: list[System.Byte]) -> IncrementalHash: ...
    def AppendData(self, buffer: list[System.Byte], offset: int, count: int) -> None: ...
    def GetHashAndReset(self) -> list[System.Byte]: ...

class HashAlgorithmName:
    SHA1: str

