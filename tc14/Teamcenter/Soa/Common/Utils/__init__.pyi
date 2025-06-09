import System
import System.IO
import System.Text
import typing

class XmlBindingUtils:
    """
    
Utility class to serialize and deserialize the Xml sent to/from the server.
    """
    def __init__(self, ) -> None: ...
    def Serialize(self, requestObject: typing.Any) -> list[System.Byte]:
        """    
            Serialize the requestObject into Byte Array.
            
        :param requestObject: requestObject; an object with service request information
        :return: Request object in Byte Array form
        """
        ...
    def Deserialize3(self, inpXml: str, type: System.Type, extraTypes: list[System.Type], encoding: System.Text.Encoding) -> typing.Any:
        """    
            Deserialize the input xml into RequestObject
            
        :param inpXml: Response from server
        :param type: Type of response
        :param extraTypes: Extra type if any
        :param encoding: Encoding used to deserialize
        :return: request object
        """
        ...
    def Deserialize2(self, inpXml: str, type: System.Type, extraTypes: list[System.Type]) -> typing.Any:
        """    
            Deserialize the input xml into RequestObject
            
        :param inpXml: Response from server
        :param type: Type of response
        :param extraTypes: Extra type if any
        :return: request object
        """
        ...
    @typing.overload
    def Deserialize(self, inpXml: str, type: System.Type, extraTypes: list[System.Type]) -> typing.Any: ...
    @typing.overload
    def Deserialize(self, inpXmlStream: System.IO.Stream, type: System.Type, extraTypes: list[System.Type]) -> typing.Any: ...
    @staticmethod
    def UTF8ByteArrayToString(chars: list[System.Byte]) -> str:
        """    
            It takes a UTF-8 byte array and converts it to string 
            A string by definition is UTF-16
            
        :param chars: Byte formatted request
        :return: returns string format of service request
        """
        ...
    @staticmethod
    def StringToUTF8ByteArray(xmlString: str) -> list[System.Byte]:
        """    
            It takes a string and convert it to UTF-8 byte Array.  
            
        :param xmlString: response xml string
        :return: Byte format of service response
        """
        ...
    @staticmethod
    def StringToEncodedByteArray(xmlString: str, encoding: System.Text.Encoding) -> list[System.Byte]:
        """    
            It takes a string and convert it to encoded UTF-8 byte Array. 
            
        :param xmlString: xml string of response
        :param encoding: Encoding to be used
        :return: Byte array with the given encoding format
        """
        ...

